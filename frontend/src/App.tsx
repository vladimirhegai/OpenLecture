import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import {
  api,
  course as coursePath,
  resolveCitation,
  setToken,
  upload,
  type Citation,
  type Course,
  type DocumentReference,
  type DocumentSummary,
  type Provider,
  type Source,
  type Task,
} from "./api";
import { Chat, type Viewing } from "./components/Chat";
import { effortName, modelLabel, type Selection } from "./components/ModelPicker";
import { SearchPalette } from "./components/Search";
import { Settings } from "./components/Settings";
import { Sidebar } from "./components/Sidebar";
import { BrandMark, Dialog, useToast } from "./components/ui";
import { CourseHome, DocumentView, Shell, SourceView, Toolbar, type Ask, type Route } from "./components/Views";
import { useStored, useTheme } from "./theme";
import { newEntry, rememberScroll } from "./scroll";
import { SCHEDULE_COURSE, SCHEDULE_ID } from "./schedule";
import { StudySchedule } from "./components/StudySchedule";
import { StudyPlan } from "./components/StudyPlan";

/* URL shape matches the backend's document reference routes: /courses/:id/docs/:doc */
function parseLocation(): { courseId: string | null; route: Route } {
  const parts = location.pathname.split("/").filter(Boolean);
  const params = new URLSearchParams(location.search);
  if (parts[0] === SCHEDULE_ID) return { courseId: SCHEDULE_ID, route: { kind: "home" } };
  if (parts[0] !== "courses" || !parts[1]) return { courseId: null, route: { kind: "home" } };
  if (parts[2] === "docs" && parts[3]) {
    const revision = Number(params.get("revision")) || undefined;
    return { courseId: parts[1], route: { kind: "doc", id: parts[3], revision, block: location.hash.slice(1) || undefined } };
  }
  if (parts[2] === "sources" && parts[3]) {
    return { courseId: parts[1], route: { kind: "source", id: parts[3], page: Number(params.get("page")) || undefined } };
  }
  if (parts[2] === "plan") return { courseId: parts[1], route: { kind: "plan" } };
  return { courseId: parts[1], route: { kind: "home" } };
}

function toUrl(courseId: string, route: Route) {
  if (courseId === SCHEDULE_ID) return "/study-schedule";
  const base = `/courses/${courseId}`;
  if (route.kind === "doc") return `${base}/docs/${route.id}${route.revision ? `?revision=${route.revision}` : ""}${route.block ? `#${route.block}` : ""}`;
  if (route.kind === "source") return `${base}/sources/${route.id}${route.page ? `?page=${route.page}` : ""}`;
  if (route.kind === "plan") return `${base}/plan`;
  return base;
}

const KINDS = [
  ["lecture", "Lecture"],
  ["tutorial", "Tutorial"],
  ["practice", "Problems"],
  ["textbook", "Textbook"],
  ["lab", "Lab"],
  ["syllabus", "Syllabus"],
  ["reference", "Reference"],
  ["student_notes", "My notes"],
] as const;

function guessWeek(name: string) {
  const match = name.match(/(?:week|wk)[\s_-]*0?(\d{1,2})|(?:^|[^a-z0-9])w0?(\d{1,2})(?=[_\s.-])/i);
  return match ? match[1] ?? match[2] : "";
}

export default function App() {
  const toast = useToast();
  const { pref: theme, setPref: setTheme, dark } = useTheme();
  const initial = useMemo(parseLocation, []);
  const [courses, setCourses] = useState<Course[] | null>(null);
  const [courseId, setCourseId] = useStored<string | null>("ol-course", initial.courseId);
  const [route, setRoute] = useState<Route>(initial.route);
  const [docs, setDocs] = useState<DocumentSummary[]>([]);
  const [sources, setSources] = useState<Source[]>([]);
  const [tasks, setTasks] = useState<Task[]>([]);
  const [refresh, setRefresh] = useState(0);
  const [providers, setProviders] = useState<Provider[]>([]);
  const [checking, setChecking] = useState(false);
  const [selection, setSelection] = useStored<Selection>("ol-model", { provider: "claude", model: "default", effort: null });
  const [pending, setPending] = useState<Provider["id"] | null>(null);
  const [manualCommand, setManualCommand] = useState<string | null>(null);
  const [chatOpen, setChatOpen] = useStored("ol-chat-open", window.innerWidth > 900);
  const [navOpen, setNavOpen] = useState(false);
  const [dialog, setDialog] = useState<null | "settings" | "search" | "course" | "token">(null);
  const [uploadFile, setUploadFile] = useState<File | null>(null);
  const [ask, setAsk] = useState<(Ask & { nonce: number }) | null>(null);
  const [page, setPage] = useState<number | undefined>(initial.route.kind === "source" ? initial.route.page : undefined);
  const [history, setHistory] = useState<Route[]>([]);
  const pollTimer = useRef<number | null>(null);

  const course = courses?.find((c) => c.id === courseId) ?? null;
  const isSchedule = courseId === SCHEDULE_ID;

  useEffect(() => {
    if (initial.courseId) setCourseId(initial.courseId);
  }, [initial, setCourseId]);

  /* ---------- Data ---------- */

  const loadCourses = useCallback(() => api<Course[]>("/courses?limit=100").then(setCourses), []);

  useEffect(() => {
    loadCourses().catch((e) => {
      setCourses([]);
      if (e.status !== 401) toast(`Can't reach the Open Lecture server: ${e.message}`);
    });
    const unauthorized = () => setDialog("token");
    window.addEventListener("ol:unauthorized", unauthorized);
    return () => window.removeEventListener("ol:unauthorized", unauthorized);
  }, [loadCourses, toast]);

  useEffect(() => {
    if (courses && !isSchedule && !courses.some((c) => c.id === courseId)) setCourseId(courses[0]?.id ?? SCHEDULE_ID);
  }, [courses, courseId, isSchedule, setCourseId]);

  const loadLists = useCallback(() => {
    if (!courseId || courseId === SCHEDULE_ID) return;
    api<DocumentSummary[]>(`${coursePath(courseId)}/documents?limit=100`).then(
      (list) => setDocs([...list].sort((a, b) => (a.academic_week ?? 0) - (b.academic_week ?? 0) || a.title.localeCompare(b.title))),
      () => setDocs([]),
    );
    api<Source[]>(`${coursePath(courseId)}/sources?limit=100`).then(setSources, () => setSources([]));
  }, [courseId]);

  const loadTasks = useCallback(() => {
    if (!courseId || courseId === SCHEDULE_ID) return;
    api<Task[]>(`${coursePath(courseId)}/tasks?limit=40`).then(setTasks, () => setTasks([]));
  }, [courseId]);

  useEffect(() => {
    setDocs([]);
    setSources([]);
    setTasks([]);
    loadLists();
    loadTasks();
  }, [loadLists, loadTasks]);

  // Background agents report steps without workspace events; poll while any are active.
  const busy = tasks.some((task) => task.status === "queued" || task.status === "running");
  useEffect(() => {
    if (!busy) return;
    const timer = window.setInterval(() => {
      loadTasks();
      loadLists();
    }, 4000);
    return () => window.clearInterval(timer);
  }, [busy, loadTasks, loadLists]);

  // Live workspace events: lists and the open view refresh when an agent or another client writes.
  useEffect(() => {
    if (!courseId || courseId === SCHEDULE_ID || localStorage.getItem("ol-token")) return;
    const key = `ol-seq:${courseId}`;
    let timer: number | undefined;
    const source = new EventSource(`/api/v1${coursePath(courseId)}/events?after=${Number(localStorage.getItem(key)) || 0}`);
    const onEvent = (raw: MessageEvent) => {
      const event = JSON.parse(raw.data);
      try {
        localStorage.setItem(key, String(event.sequence));
      } catch {
        /* storage unavailable */
      }
      window.dispatchEvent(new CustomEvent("ol:event", { detail: event }));
      clearTimeout(timer);
      timer = window.setTimeout(() => {
        loadLists();
        if (/^(task|source)\./.test(event.type)) loadTasks();
        if (/^(document|source|job)\./.test(event.type)) setRefresh((n) => n + 1);
      }, 250);
    };
    const types = [
      "document.created", "document.updated", "document.deleted", "document.restored",
      "source.ingestion_queued", "source.ingestion_started", "source.ingestion_completed", "job.failed",
      "chat.message_added", "artifact.created", "course.profile_updated", "task.updated", "source.reading_updated",
    ];
    types.forEach((type) => source.addEventListener(type, onEvent));
    return () => {
      clearTimeout(timer);
      source.close();
    };
  }, [courseId, loadLists, loadTasks]);

  const loadProviders = useCallback(async (fresh = false) => {
    setChecking(true);
    try {
      const list = await api<Provider[]>(`/agents${fresh ? "?refresh=true" : ""}`);
      setProviders(list);
      return list;
    } catch {
      return [];
    } finally {
      setChecking(false);
    }
  }, []);

  useEffect(() => {
    loadProviders().then((list) => {
      // Default to a provider that is actually signed in.
      const chosen = list.find((p) => p.id === selection.provider);
      if (!chosen?.signed_in) {
        const ready = list.find((p) => p.signed_in);
        if (ready) setSelection({ provider: ready.id, model: "default", effort: null });
      }
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  /* ---------- Navigation ---------- */

  const open = useCallback(
    (next: Route, options: { replace?: boolean; course?: string } = {}) => {
      const target = options.course ?? courseId;
      if (!target) return;
      if (options.course && options.course !== courseId) setCourseId(options.course);
      setHistory((list) => (options.replace ? list : [...list.slice(-30), route]));
      setRoute(next);
      setPage(next.kind === "source" ? next.page : undefined);
      setNavOpen(false);
      const url = toUrl(target, next);
      if (options.replace) window.history.replaceState(newEntry(), "", url);
      else {
        rememberScroll();
        window.history.pushState(newEntry(), "", url);
      }
    },
    [courseId, route, setCourseId],
  );

  useEffect(() => {
    const onPop = () => {
      const parsed = parseLocation();
      if (parsed.courseId) setCourseId(parsed.courseId);
      setRoute(parsed.route);
      setPage(parsed.route.kind === "source" ? parsed.route.page : undefined);
    };
    window.addEventListener("popstate", onPop);
    return () => window.removeEventListener("popstate", onPop);
  }, [setCourseId]);

  useEffect(() => {
    if (courseId && location.pathname === "/") window.history.replaceState(null, "", toUrl(courseId, route));
  }, [courseId, route]);

  const cite = useCallback(
    async (citation: Citation) => {
      if (!courseId) return;
      try {
        const { page } = await resolveCitation(courseId, citation);
        open({ kind: "source", id: citation.source_id, page: page ?? 1 });
      } catch (e) {
        toast((e as Error).message);
      }
    },
    [courseId, open, toast],
  );

  /* ---------- Accounts ---------- */

  const signIn = useCallback(
    async (id: Provider["id"]) => {
      try {
        const result = await api<{ opened: boolean; command: string }>(`/agents/${id}/login`, { method: "POST" });
        const name = providers.find((p) => p.id === id)?.name ?? id;
        if (!result.opened) {
          setManualCommand(result.command);
          setDialog("settings");
          return;
        }
        setManualCommand(null);
        setPending(id);
        toast(`Finish signing in to ${name} in the terminal window that opened`);
        const started = Date.now();
        if (pollTimer.current) clearInterval(pollTimer.current);
        pollTimer.current = window.setInterval(async () => {
          const list = await loadProviders(true);
          const done = list.find((p) => p.id === id)?.signed_in;
          if (done || Date.now() - started > 180_000) {
            clearInterval(pollTimer.current!);
            pollTimer.current = null;
            setPending(null);
            if (done) {
              toast(`Signed in to ${name}`);
              setSelection((s) => (providers.find((p) => p.id === s.provider)?.signed_in ? s : { provider: id, model: "default", effort: null }));
            }
          }
        }, 3000);
      } catch (e) {
        toast((e as Error).message);
      }
    },
    [providers, loadProviders, toast, setSelection],
  );

  const signOut = useCallback(
    async (id: Provider["id"]) => {
      try {
        const status = await api<Provider>(`/agents/${id}/logout`, { method: "POST" });
        setProviders((list) => list.map((p) => (p.id === id ? status : p)));
        toast(status.signed_in ? `${status.name} is still signed in` : `Signed out of ${status.name}`);
      } catch (e) {
        toast((e as Error).message);
      }
    },
    [toast],
  );

  /* ---------- Keyboard ---------- */

  useEffect(() => {
    const key = (event: KeyboardEvent) => {
      const mod = event.ctrlKey || event.metaKey;
      if (mod && event.key.toLowerCase() === "k" && course) {
        event.preventDefault();
        setDialog((d) => (d === "search" ? null : "search"));
      } else if (mod && event.key.toLowerCase() === "j") {
        event.preventDefault();
        setChatOpen((o) => !o);
      }
    };
    window.addEventListener("keydown", key);
    return () => window.removeEventListener("keydown", key);
  }, [course, setChatOpen]);

  /* ---------- Chat context ---------- */

  const openDoc = route.kind === "doc" ? docs.find((d) => d.document_id === route.id) : undefined;
  const openSource = route.kind === "source" ? sources.find((s) => s.id === route.id) : undefined;
  const viewing: Viewing =
    route.kind === "doc" && openDoc
      ? { kind: "doc", label: openDoc.title, document_id: openDoc.document_id, revision: route.revision ?? openDoc.revision }
      : route.kind === "source" && openSource
        ? { kind: "source", label: `${openSource.filename}${page ? `, page ${page}` : ""}`, source_id: openSource.id, page }
        : null;

  const requestAsk = useCallback(
    (request: Ask) => {
      setChatOpen(true);
      setAsk({ ...request, nonce: Date.now() });
    },
    [setChatOpen],
  );

  const writer = providers.find((p) => p.id === selection.provider);
  const modelName = modelLabel(providers, selection) + (selection.effort ? ` (${effortName(selection.effort).toLowerCase()} effort)` : "");

  const generateWeek = useCallback(
    async (week: number, regenerate = false) => {
      if (!courseId) return;
      try {
        await api(`${coursePath(courseId)}/weeks/${week}/generate`, { method: "POST", json: { ...selection, regenerate } });
        toast(`Writing Week ${week} notes with ${modelLabel(providers, selection)}`);
        loadTasks();
      } catch (e) {
        toast((e as Error).message);
      }
    },
    [courseId, selection, providers, toast, loadTasks],
  );

  const cancelTask = useCallback(
    (task: Task) => {
      if (!courseId) return;
      api(`${coursePath(courseId)}/tasks/${task.id}/cancel`, { method: "POST" }).then(loadTasks, (e) => toast(e.message));
    },
    [courseId, loadTasks, toast],
  );

  /* ---------- Render ---------- */

  const shell = useMemo(
    () => ({ openNav: () => setNavOpen(true), chatOpen: isSchedule || chatOpen, toggleChat: () => setChatOpen((o) => !o), dark }),
    [chatOpen, isSchedule, setChatOpen, dark],
  );

  let main;
  if (courses === null) main = <div className="empty"><div className="spinner" /></div>;
  else if (isSchedule) main = <StudySchedule courses={courses} onCourse={(id) => open({ kind: "home" }, { course: id })} />;
  else if (!course)
    main = (
      <>
        <Toolbar crumbs={<span className="here">Open Lecture</span>} />
        <div className="empty">
          <div>
            <BrandMark className="brand-mark" />
            <h2>Create your first course</h2>
            <p>Add a course, then upload lecture slides, tutorials or a syllabus. Ask questions and get notes with page citations.</p>
            <button className="btn primary" onClick={() => setDialog("course")}>
              New course
            </button>
          </div>
        </div>
      </>
    );
  else if (route.kind === "doc")
    main = (
      <DocumentView
        key={route.id}
        course={course}
        route={route}
        refresh={refresh}
        onOpen={open}
        onAsk={requestAsk}
        onCite={cite}
        onDeleted={() => {
          loadLists();
          open({ kind: "home" }, { replace: true });
        }}
        onRegenerate={(week) => {
          generateWeek(week, true);
          open({ kind: "home" });
        }}
      />
    );
  else if (route.kind === "plan") main = <StudyPlan course={course} onOpen={open} />;
  else if (route.kind === "source")
    main = (
      <SourceView
        key={route.id}
        course={course}
        route={route}
        refresh={refresh}
        onOpen={open}
        onAsk={requestAsk}
        onPage={setPage}
        back={history.length && history[history.length - 1].kind === "doc" ? () => window.history.back() : null}
      />
    );
  else
    main = (
      <CourseHome
        course={course}
        docs={docs}
        sources={sources}
        tasks={tasks}
        onAsk={requestAsk}
        onOpen={open}
        onGenerate={(week) => generateWeek(week)}
        canGenerate={!!writer?.signed_in}
        modelName={modelName}
      />
    );

  return (
    <Shell.Provider value={shell}>
      <div className={`shell ${chatOpen && course ? "" : "chat-closed"} ${navOpen ? "nav-open" : ""}`}>
        {navOpen && <div className="nav-scrim mobile-only" onClick={() => setNavOpen(false)} />}
        <Sidebar
          courses={[SCHEDULE_COURSE, ...(courses ?? [])]}
          course={isSchedule ? SCHEDULE_COURSE : course}
          docs={docs}
          sources={sources}
          tasks={tasks}
          onCancelTask={cancelTask}
          route={route}
          providers={providers}
          selection={selection}
          theme={theme}
          onTheme={setTheme}
          onCourse={(id) => {
            setCourseId(id);
            setRoute({ kind: "home" });
            setNavOpen(false);
            window.history.pushState(null, "", toUrl(id, { kind: "home" }));
          }}
          onNewCourse={() => setDialog("course")}
          onOpen={open}
          onSearch={() => setDialog("search")}
          onUpload={setUploadFile}
          onSettings={() => {
            setNavOpen(false);
            setDialog("settings");
            loadProviders(true);
          }}
        />
        <main className="main">{main}</main>
        {course && (
          <Chat
            course={course}
            docs={docs}
            viewing={viewing}
            ask={ask}
            providers={providers}
            selection={selection}
            onSelection={setSelection}
            onSignIn={signIn}
            pending={pending}
            onManage={() => {
              setDialog("settings");
              loadProviders(true);
            }}
            onClose={() => setChatOpen(false)}
            onOpenReference={(reference: DocumentReference) => open({ kind: "doc", id: reference.document_id, block: reference.block_id ?? undefined })}
          />
        )}
      </div>

      {dialog === "settings" && (
        <Settings
          onClose={() => setDialog(null)}
          theme={theme}
          onTheme={setTheme}
          providers={providers}
          onRefresh={() => loadProviders(true)}
          refreshing={checking}
          selection={selection}
          onSelection={setSelection}
          onSignIn={signIn}
          onSignOut={signOut}
          pending={pending}
          manualCommand={manualCommand}
        />
      )}
      {dialog === "search" && course && (
        <SearchPalette course={course} docs={docs} sources={sources} onOpen={open} onClose={() => setDialog(null)} />
      )}
      {dialog === "course" && (
        <NewCourse
          onClose={() => setDialog(null)}
          onCreated={async (created) => {
            await loadCourses();
            setCourseId(created.id);
            setRoute({ kind: "home" });
            window.history.pushState(null, "", toUrl(created.id, { kind: "home" }));
            toast(`Created ${created.code}`);
          }}
        />
      )}
      {dialog === "token" && <TokenDialog onClose={() => setDialog(null)} />}
      {uploadFile && course && (
        <UploadDialog
          file={uploadFile}
          course={course}
          onClose={() => setUploadFile(null)}
          onUploaded={(sourceId, duplicate) => {
            loadLists();
            open({ kind: "source", id: sourceId });
            toast(duplicate ? `${uploadFile.name} is already in ${course.code}` : `Added ${uploadFile.name}`);
          }}
        />
      )}
    </Shell.Provider>
  );
}

function NewCourse({ onClose, onCreated }: { onClose: () => void; onCreated: (course: Course) => void }) {
  const [code, setCode] = useState("");
  const [title, setTitle] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  async function submit(event: React.FormEvent) {
    event.preventDefault();
    setBusy(true);
    try {
      const created = await api<Course>("/courses", { method: "POST", json: { code: code.trim(), title: title.trim() } });
      onCreated(created);
      onClose();
    } catch (e) {
      setError((e as Error).message);
      setBusy(false);
    }
  }
  return (
    <Dialog title="New course" onClose={onClose}>
      <form className="dialog-body" onSubmit={submit}>
        <label className="field">
          <span>Course code</span>
          <input className="input" value={code} onChange={(e) => setCode(e.target.value)} placeholder="ELEC 221" maxLength={40} required />
        </label>
        <label className="field">
          <span>Title</span>
          <input className="input" value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Electric Circuits" maxLength={200} required />
        </label>
        {error && <p style={{ color: "var(--danger)", margin: "12px 0 0" }}>{error}</p>}
        <div className="dialog-actions">
          <button type="button" className="btn" onClick={onClose}>
            Cancel
          </button>
          <button className="btn primary" disabled={busy || !code.trim() || !title.trim()}>
            Create course
          </button>
        </div>
      </form>
    </Dialog>
  );
}

function UploadDialog({
  file,
  course,
  onClose,
  onUploaded,
}: {
  file: File;
  course: Course;
  onClose: () => void;
  onUploaded: (sourceId: string, duplicate: boolean) => void;
}) {
  const guess = /syllab/i.test(file.name)
    ? "syllabus"
    : /text\s*book/i.test(file.name)
      ? "textbook"
      : /tut/i.test(file.name)
        ? "tutorial"
        : /problem|assessment|practice/i.test(file.name)
          ? "practice"
          : /lab/i.test(file.name)
            ? "lab"
            : "lecture";
  const [kind, setKind] = useState<string>(guess);
  const [week, setWeek] = useState<string>(guessWeek(file.name));
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  async function submit() {
    setBusy(true);
    try {
      const result = await upload(course.id, file, kind, kind === "textbook" ? null : Number(week) || null);
      onUploaded(result.source_id, result.duplicate);
      onClose();
    } catch (e) {
      setError((e as Error).message);
      setBusy(false);
    }
  }
  return (
    <Dialog title="Add source" onClose={onClose}>
      <div className="dialog-body">
        <p>
          <strong style={{ color: "var(--ink)" }}>{file.name}</strong> will be added to {course.code} and indexed for search.
          The original file stays on this computer.
        </p>
        <div className="field">
          <span>What is it?</span>
          <div className="segmented" style={{ flexWrap: "wrap" }}>
            {KINDS.map(([value, label]) => (
              <button key={value} aria-pressed={kind === value} onClick={() => setKind(value)}>
                {label}
              </button>
            ))}
          </div>
        </div>
        {kind !== "textbook" && (
          <label className="field">
            <span>Week (optional)</span>
            <input
              className="input"
              style={{ width: 120 }}
              inputMode="numeric"
              value={week}
              placeholder="e.g. 3"
              onChange={(e) => setWeek(e.target.value.replace(/\D/g, "").slice(0, 2))}
            />
          </label>
        )}
        <p style={{ margin: "12px 0 0", fontSize: 13 }}>
          {kind === "textbook"
            ? "Textbooks are indexed by chapter and problem, not read in full. Notes pull practice problems from them."
            : "PDFs and images are read page by page by AI, including handwriting and diagrams."}
        </p>
        {error && <p style={{ color: "var(--danger)", margin: "12px 0 0" }}>{error}</p>}
        <div className="dialog-actions">
          <button className="btn" onClick={onClose}>
            Cancel
          </button>
          <button className="btn primary" onClick={submit} disabled={busy}>
            {busy && <span className="spinner" />}
            Add source
          </button>
        </div>
      </div>
    </Dialog>
  );
}

function TokenDialog({ onClose }: { onClose: () => void }) {
  const [value, setValue] = useState("");
  return (
    <Dialog title="Access token required" onClose={onClose}>
      <form
        className="dialog-body"
        onSubmit={(e) => {
          e.preventDefault();
          setToken(value.trim());
          location.reload();
        }}
      >
        <p>This Open Lecture server requires the access token set in OPENLECTURE_API_TOKEN.</p>
        <label className="field">
          <span>Token</span>
          <input className="input" type="password" value={value} onChange={(e) => setValue(e.target.value)} autoComplete="off" />
        </label>
        <div className="dialog-actions">
          <button className="btn primary" disabled={!value.trim()}>
            Continue
          </button>
        </div>
      </form>
    </Dialog>
  );
}
