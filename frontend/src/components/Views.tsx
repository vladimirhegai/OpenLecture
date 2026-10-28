import {
  AlertCircle,
  ArrowLeft,
  ChevronLeft,
  ChevronRight,
  Clock,
  Download,
  History,
  Link2,
  Menu,
  MessageSquare,
  MoreHorizontal,
  PanelRightOpen,
  Sparkles,
  SunMoon,
  Trash2,
  ZoomIn,
  ZoomOut,
} from "lucide-react";
import { createContext, useContext, useEffect, useRef, useState, type ReactNode } from "react";
import {
  api,
  course as coursePath,
  originalUrl,
  pageImage,
  relativeTime,
  type Block,
  type Citation,
  type Course,
  type Doc,
  type DocumentSummary,
  type Profile,
  type Revision,
  type Source,
  type SourceDetail,
  type Task,
  type Topic,
} from "../api";
import { useStored } from "../theme";
import { toolVerb } from "../labels";
import { Blocks, scrollsToTop } from "./Blocks";
import { Markdown, slug } from "./Markdown";
import { Popover, useToast } from "./ui";
import { savedScroll, useScrollMemory } from "../scroll";

export type Route =
  | { kind: "home" }
  | { kind: "doc"; id: string; revision?: number; block?: string }
  | { kind: "source"; id: string; page?: number }
  | { kind: "plan" };

/** The block a `#target` names: its id, or else a label such as `b6`, `problem-29` or `topic-1` that matches how a
 * heading's or a problem's title starts. Hand-written links (the study plan) use labels, so they survive a note rebuild
 * that changes the block ids. */
function resolveBlock(blocks: Block[], target: string) {
  if (blocks.some((block) => block.id === target)) return target;
  const want = slug(decodeURIComponent(target));
  const label = (block: Block) =>
    block.type === "heading" ? block.text : block.type === "practice_problem" || block.type === "worked_example" ? block.title ?? "" : "";
  return blocks.find((block) => {
    const text = slug(label(block));
    return text && (text === want || text.startsWith(want + "-"));
  })?.id ?? target;
}

export type Ask = { text?: string; send?: boolean; block?: Block };

export const Shell = createContext<{
  openNav: () => void;
  chatOpen: boolean;
  toggleChat: () => void;
  dark: boolean;
}>({ openNav: () => {}, chatOpen: true, toggleChat: () => {}, dark: false });

export function Toolbar({ crumbs, children }: { crumbs: ReactNode; children?: ReactNode }) {
  const shell = useContext(Shell);
  return (
    <header className="toolbar">
      <button className="icon-btn mobile-only" onClick={shell.openNav} aria-label="Open navigation">
        <Menu size={18} />
      </button>
      <div className="crumbs">{crumbs}</div>
      {children}
      {!shell.chatOpen && (
        <>
          <span className="sep desktop-only" />
          <button className="icon-btn" onClick={shell.toggleChat} title="Open chat (Ctrl+J)" aria-label="Open chat">
            <span className="desktop-only" style={{ display: "contents" }}>
              <PanelRightOpen size={17} />
            </span>
            <span className="mobile-only" style={{ display: "contents" }}>
              <MessageSquare size={17} />
            </span>
          </button>
        </>
      )}
    </header>
  );
}

const DOC_TYPES: Record<string, string> = {
  study_notes: "Study notes",
  revision_sheet: "Revision sheet",
  practice_set: "Practice set",
  reference: "Reference",
};

/* ---------------- Course home ---------------- */

export type WeekState = {
  week: number;
  topics: Topic[];
  note: DocumentSummary | null;
  task: Task | null;
  failed: Task | null;
  sources: Source[];
  unread: Source[];
};

export function weekStates(profile: Profile | null, docs: DocumentSummary[], sources: Source[], tasks: Task[]) {
  const weeks = new Map<number, WeekState>();
  const get = (week: number) => {
    if (!weeks.has(week)) weeks.set(week, { week, topics: [], note: null, task: null, failed: null, sources: [], unread: [] });
    return weeks.get(week)!;
  };
  for (const topic of profile?.topics ?? []) if (topic.week) get(topic.week).topics.push(topic);
  for (const doc of docs) if (doc.academic_week && doc.document_type === "study_notes") get(doc.academic_week).note ??= doc;
  for (const source of sources) {
    if (!source.week || source.kind === "textbook") continue;
    const state = get(source.week);
    state.sources.push(source);
    if (source.reading_status === "pending" || source.reading_status === "running") state.unread.push(source);
  }
  for (const task of tasks) {
    if (task.kind !== "week_notes") continue;
    const state = get(task.params.week);
    if (task.status === "queued" || task.status === "running") state.task ??= task;
    else if (task.status === "failed" && !state.failed && !state.note) state.failed = task;
  }
  return [...weeks.values()].sort((a, b) => a.week - b.week);
}

export function taskStep(task: Task) {
  const last = [...task.log].reverse().find((entry) => entry.tool);
  return last?.tool ? toolVerb(last.tool) : task.status === "queued" ? "Waiting to start" : "Starting";
}

function WeekRow({
  state,
  onOpen,
  onGenerate,
  canGenerate,
}: {
  state: WeekState;
  onOpen: (route: Route) => void;
  onGenerate: (week: number) => void;
  canGenerate: boolean;
}) {
  const { week, topics, note, task, failed, unread } = state;
  const waiting = !note && !task && unread.length > 0;
  const action = note
    ? () => onOpen({ kind: "doc", id: note.document_id })
    : task || waiting || !canGenerate
      ? undefined
      : () => onGenerate(week);
  const readingDone = unread.reduce((n, s) => n + (s.reading_pages_done ?? 0), 0);
  const readingTotal = unread.reduce((n, s) => n + (s.reading_pages_total ?? 0), 0);
  return (
    <li>
      <button className={`week-row ${note ? "has-note" : ""}`} onClick={action} disabled={!action} aria-label={`Week ${week}`}>
        <span className="week-num">Week {week}</span>
        <span className="week-body">
          {note && <span className="week-note">{note.title.replace(/^Week \d+:\s*/, "")}</span>}
          <span className="week-topics">
            {topics.map((topic) => (
              <span key={topic.key}>{topic.title}</span>
            ))}
          </span>
          {task && (
            <span className="week-status working">
              <span className="spinner" />
              Writing notes: {taskStep(task)}
            </span>
          )}
          {waiting && (
            <span className="week-status">
              <Clock size={13} />
              Reading this week's sources first ({readingDone}/{readingTotal} pages)
            </span>
          )}
          {failed && !task && (
            <span className="week-status failed" title={failed.error ?? ""}>
              <AlertCircle size={13} />
              Last attempt failed. Select to try again.
            </span>
          )}
        </span>
        <span className="week-action">
          {note ? (
            <ChevronRight size={16} />
          ) : !task && !waiting ? (
            <span className="week-generate">
              <Sparkles size={14} />
              Generate notes
            </span>
          ) : null}
        </span>
      </button>
    </li>
  );
}

export function CourseHome({
  course,
  docs,
  sources,
  tasks,
  onAsk,
  onOpen,
  onGenerate,
  canGenerate,
  modelName,
}: {
  course: Course;
  docs: DocumentSummary[];
  sources: Source[];
  tasks: Task[];
  onAsk: (ask: Ask) => void;
  onOpen: (route: Route) => void;
  onGenerate: (week: number) => void;
  canGenerate: boolean;
  modelName: string;
}) {
  const [profile, setProfile] = useState<Profile | null>(null);
  useEffect(() => {
    setProfile(null);
    api<Profile>(`${coursePath(course.id)}/profile`).then(setProfile, () => setProfile(null));
  }, [course.id]);
  const map = docs.find((doc) => doc.topic_keys.includes("course_map"));
  const weeks = weekStates(profile, docs, sources, tasks);
  const prompts = [
    "What should I focus on first in this course?",
    "How is this course graded, and when are the big deadlines?",
    "Quiz me on last week's material, one question at a time.",
  ];

  return (
    <>
      <Toolbar crumbs={<span className="here">{course.code}</span>} />
      <div className="scroll">
        <div className="home">
          <div className="home-kicker">
            {course.code}
            {profile?.term ? `, ${profile.term}` : ""}
          </div>
          <h1>{course.title}</h1>
          <div className="home-stats">
            <span>{docs.length === 1 ? "1 note" : `${docs.length} notes`}</span>
            <span>{sources.length === 1 ? "1 source" : `${sources.length} sources`}</span>
            {map && (
              <button className="text-link" onClick={() => onOpen({ kind: "doc", id: map.document_id })}>
                Open course map
              </button>
            )}
          </div>

          {weeks.length > 0 && (
            <section className="home-section">
              <div className="section-head">
                <h2>Weeks</h2>
                <span>New notes are written by {modelName}</span>
              </div>
              <ul className="weeks">
                {weeks.map((state) => (
                  <WeekRow key={state.week} state={state} onOpen={onOpen} onGenerate={onGenerate} canGenerate={canGenerate} />
                ))}
              </ul>
            </section>
          )}

          <section className="home-section">
            <h2>Start with a question</h2>
            <div className="prompts">
              {prompts.map((prompt) => (
                <button key={prompt} className="prompt-chip" onClick={() => onAsk({ text: prompt, send: true })}>
                  {prompt}
                </button>
              ))}
            </div>
          </section>
        </div>
      </div>
    </>
  );
}

/* ---------------- Note reader ---------------- */

export function DocumentView({
  course,
  route,
  refresh,
  onOpen,
  onAsk,
  onCite,
  onDeleted,
  onRegenerate,
}: {
  course: Course;
  route: Extract<Route, { kind: "doc" }>;
  refresh: number;
  onOpen: (route: Route) => void;
  onAsk: (ask: Ask) => void;
  onCite: (citation: Citation) => void;
  onDeleted: () => void;
  onRegenerate: (week: number) => void;
}) {
  const toast = useToast();
  const [doc, setDoc] = useState<Doc | null>(null);
  const [latest, setLatest] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [revisions, setRevisions] = useState<Revision[]>([]);
  const [flash, setFlash] = useState<string | null>(null);
  const scroller = useRef<HTMLDivElement>(null);
  const base = `${coursePath(course.id)}/documents/${route.id}`;
  useScrollMemory(scroller, doc !== null);

  useEffect(() => {
    let live = true;
    setError(null);
    const query = route.revision ? `?revision=${route.revision}` : "";
    Promise.all([api<Doc>(base + query), route.revision ? api<Doc>(base) : null]).then(
      ([view, current]) => {
        if (!live) return;
        setDoc(view);
        setLatest((current ?? view).revision);
      },
      (e) => live && setError(e.message),
    );
    return () => {
      live = false;
    };
  }, [base, route.revision, refresh]);

  // False until this note has been shown once: arriving from elsewhere lands on the target at once, while a jump
  // inside a note that is already open scrolls smoothly.
  const settled = useRef(false);
  useEffect(() => {
    if (!doc) return;
    const behavior: ScrollBehavior = settled.current ? "smooth" : "instant";
    settled.current = true;
    if (!route.block) {
      // Back to an entry with no target (e.g. after an in-note link): return to where the reader was.
      const top = savedScroll();
      if (behavior === "smooth" && top !== undefined) scroller.current?.scrollTo({ top, behavior });
      return;
    }
    const target = resolveBlock(doc.blocks, route.block);
    const element = document.getElementById(`b-${target}`);
    // A heading is the start of what the reader asked for, so it goes to the top; other blocks are centred, unless they're
    // taller than the screen (a long worked example), where centring would hide the title.
    element?.scrollIntoView({ block: scrollsToTop(element) ? "start" : "center", behavior });
    setFlash(target);
    const timer = setTimeout(() => setFlash(null), 1600);
    return () => clearTimeout(timer);
  }, [route.block, doc]);

  async function remove() {
    if (!doc || latest === null) return;
    try {
      const deleted = await api<Doc>(`${base}/delete`, { method: "POST", json: { expected_revision: latest } });
      onDeleted();
      toast("Note deleted", {
        label: "Undo",
        run: () =>
          api(`${base}/restore`, { method: "POST", json: { expected_revision: deleted.revision } }).then(
            () => {
              onDeleted();
              onOpen({ kind: "doc", id: route.id });
            },
            (e) => toast(e.message),
          ),
      });
    } catch (e) {
      toast((e as Error).message);
    }
  }

  const crumbs = (
    <>
      <button onClick={() => onOpen({ kind: "home" })}>{course.code}</button>
      <ChevronRight size={14} />
      <span className="here">{doc?.title ?? "Note"}</span>
    </>
  );

  if (error) {
    return (
      <>
        <Toolbar crumbs={crumbs} />
        <div className="empty">
          <div>
            <h2>This note can't be opened</h2>
            <p>{error}</p>
            <button className="btn" onClick={() => onOpen({ kind: "home" })}>
              Back to {course.code}
            </button>
          </div>
        </div>
      </>
    );
  }

  const old = doc && latest !== null && doc.revision !== latest;

  return (
    <>
      <Toolbar crumbs={crumbs}>
        <Popover
          style={{ right: 0, top: 36, width: 260 }}
          trigger={({ toggle }) => (
            <button
              className="icon-btn"
              title="Revision history"
              aria-label="Revision history"
              onClick={() => {
                toggle();
                api<Revision[]>(`${base}/revisions`).then(setRevisions, () => setRevisions([]));
              }}
            >
              <History size={17} />
            </button>
          )}
        >
          {(close) => (
            <>
              <div className="menu-label">Revision history</div>
              {revisions.map((revision) => (
                <button
                  key={revision.revision}
                  className="menu-item"
                  onClick={() => {
                    onOpen({ kind: "doc", id: route.id, revision: revision.revision === latest ? undefined : revision.revision });
                    close();
                  }}
                >
                  <span className="grow">
                    Revision {revision.revision}
                    <span className="sub">
                      {revision.actor === "agent" ? "By AI" : "By you"}, {relativeTime(revision.created_at)}
                    </span>
                  </span>
                  {doc?.revision === revision.revision && <span className="check">Viewing</span>}
                </button>
              ))}
            </>
          )}
        </Popover>
        <button
          className="icon-btn"
          title="Ask about this note"
          aria-label="Ask about this note"
          onClick={() => onAsk({})}
        >
          <MessageSquare size={17} />
        </button>
        <Popover
          style={{ right: 0, top: 36 }}
          trigger={({ toggle }) => (
            <button className="icon-btn" onClick={toggle} aria-label="More actions" title="More">
              <MoreHorizontal size={17} />
            </button>
          )}
        >
          {(close) => (
            <>
              <button
                className="menu-item"
                onClick={() => {
                  navigator.clipboard.writeText(location.href).then(() => toast("Link copied"));
                  close();
                }}
              >
                <Link2 size={16} /> Copy link
              </button>
              {doc?.academic_week && doc.document_type === "study_notes" && (
                <button
                  className="menu-item"
                  onClick={() => {
                    close();
                    onRegenerate(doc.academic_week!);
                  }}
                >
                  <Sparkles size={16} /> Regenerate Week {doc.academic_week} notes
                </button>
              )}
              <div className="menu-sep" />
              <button
                className="menu-item danger"
                onClick={() => {
                  close();
                  remove();
                }}
              >
                <Trash2 size={16} /> Delete note
              </button>
            </>
          )}
        </Popover>
      </Toolbar>
      {old && (
        <div className="banner">
          <History size={15} />
          You're viewing revision {doc.revision}. The latest is revision {latest}.
          <button className="btn" onClick={() => onOpen({ kind: "doc", id: route.id })}>
            View latest
          </button>
        </div>
      )}
      {!old && doc?.potentially_outdated && (
        <div className="banner warn">
          A source this note cites has a newer version, so parts may be out of date.
          <button
            className="btn"
            onClick={() => onAsk({ text: "A cited source changed. Check this note against the latest source version and update what's out of date.", send: true })}
          >
            Ask to update
          </button>
        </div>
      )}
      <div className="scroll" ref={scroller} data-scroll-memory>
        {doc ? (
          <article className="sheet">
            <h1 className="doc-title">{doc.title}</h1>
            <div className="doc-meta">
              <span>{DOC_TYPES[doc.document_type] ?? doc.document_type}</span>
              {doc.academic_week && <span>Week {doc.academic_week}</span>}
              <span>Updated {relativeTime(doc.updated_at)}</span>
              <span>Revision {doc.revision}</span>
            </div>
            <Blocks blocks={doc.blocks} courseId={course.id} onCite={onCite} onAsk={old ? undefined : (block) => onAsk({ block })} flash={flash} />
            {doc.blocks.length === 0 && <p style={{ color: "var(--ink-3)" }}>This note is empty.</p>}
          </article>
        ) : (
          <div className="empty">
            <div className="spinner" />
          </div>
        )}
      </div>
    </>
  );
}

/* ---------------- Source viewer ---------------- */

function PageImage({
  course,
  source,
  page,
  width,
  ratio,
  onRatio,
  dim,
}: {
  course: string;
  source: string;
  page: number;
  width: number | null;
  ratio: number;
  onRatio: (ratio: number) => void;
  dim: boolean;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const [url, setUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => entry.isIntersecting && setVisible(true), {
      rootMargin: "800px 0px",
    });
    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    if (!visible) return;
    const controller = new AbortController();
    let created: string | null = null;
    pageImage(course, source, page, controller.signal).then(
      (blobUrl) => {
        created = blobUrl;
        setUrl(blobUrl);
      },
      (e) => e.name !== "AbortError" && setError(e.message),
    );
    return () => {
      controller.abort();
      if (created) URL.revokeObjectURL(created);
    };
  }, [visible, course, source, page]);

  return (
    <div ref={ref} className="page" data-page={page} style={{ width: width ? `${width}px` : "min(860px, 100%)" }}>
      {url ? (
        <img
          src={url}
          alt={`Page ${page}`}
          className={dim ? "dim" : ""}
          onLoad={(event) => page === 1 && onRatio(event.currentTarget.naturalWidth / event.currentTarget.naturalHeight)}
        />
      ) : (
        <div className="page-skeleton" style={{ aspectRatio: String(ratio) }}>
          {error ?? <div className="spinner" />}
        </div>
      )}
      <div className="page-num">{page}</div>
    </div>
  );
}

export function SourceView({
  course,
  route,
  refresh,
  onOpen,
  onAsk,
  onPage,
  back,
}: {
  course: Course;
  route: Extract<Route, { kind: "source" }>;
  refresh: number;
  onOpen: (route: Route) => void;
  onAsk: (ask: Ask) => void;
  onPage: (page: number) => void;
  back: (() => void) | null;
}) {
  const shell = useContext(Shell);
  const [source, setSource] = useState<SourceDetail | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [zoom, setZoom] = useStored("ol-zoom", 100);
  const [dim, setDim] = useStored("ol-dim-pages", false);
  const [ratio, setRatio] = useState(8.5 / 11);
  const [current, setCurrent] = useState(route.page ?? 1);
  const [input, setInput] = useState(String(route.page ?? 1));
  const pagesReady = useRef(false);
  const scroller = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (pagesReady.current) onPage(current);
  }, [current, onPage]);

  useEffect(() => {
    let live = true;
    setError(null);
    api<SourceDetail>(`${coursePath(course.id)}/sources/${route.id}?limit=100`).then(
      (detail) => live && setSource(detail),
      (e) => live && setError(e.message),
    );
    return () => {
      live = false;
    };
  }, [course.id, route.id, refresh]);

  const pages = source?.status === "ready" && source.filename.toLowerCase().endsWith(".pdf") ? source.pages ?? 0 : 0;

  function jump(page: number, smooth = true) {
    const target = Math.max(1, Math.min(pages || 1, page));
    const element = scroller.current?.querySelector(`[data-page="${target}"]`);
    element?.scrollIntoView({ behavior: smooth ? "smooth" : "auto", block: "start" });
    setCurrent(target);
    setInput(String(target));
  }

  useEffect(() => {
    if (!pages) return;
    pagesReady.current = true;
    const timer = setTimeout(() => jump(route.page ?? 1, false), 30);
    return () => clearTimeout(timer);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [pages, route.page, route.id]);

  useEffect(() => {
    const root = scroller.current;
    if (!root || !pages) return;
    const observer = new IntersectionObserver(
      (entries) => {
        const top = entries.filter((e) => e.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
        if (top) {
          const page = Number((top.target as HTMLElement).dataset.page);
          setCurrent(page);
          setInput(String(page));
        }
      },
      { root, threshold: 0.5 },
    );
    root.querySelectorAll("[data-page]").forEach((el) => observer.observe(el));
    return () => observer.disconnect();
  }, [pages, zoom]);

  const width = zoom === 100 ? null : Math.round((860 * zoom) / 100);
  const crumbs = (
    <>
      {back && (
        <button onClick={back} title="Back" aria-label="Back" style={{ display: "inline-grid", placeItems: "center" }}>
          <ArrowLeft size={15} />
        </button>
      )}
      <button onClick={() => onOpen({ kind: "home" })}>{course.code}</button>
      <ChevronRight size={14} />
      <span className="here">{source?.filename ?? "Source"}</span>
    </>
  );

  return (
    <>
      <Toolbar crumbs={crumbs}>
        {pages > 0 && (
          <>
            <div className="pager desktop-only">
              <button className="icon-btn" disabled={current <= 1} onClick={() => jump(current - 1)} aria-label="Previous page">
                <ChevronLeft size={17} />
              </button>
              <input
                value={input}
                aria-label="Page number"
                onChange={(e) => setInput(e.target.value.replace(/\D/g, ""))}
                onKeyDown={(e) => e.key === "Enter" && jump(Number(input) || 1)}
                onBlur={() => setInput(String(current))}
              />
              <span style={{ padding: "0 6px" }}>of {pages}</span>
              <button className="icon-btn" disabled={current >= pages} onClick={() => jump(current + 1)} aria-label="Next page">
                <ChevronRight size={17} />
              </button>
            </div>
            <span className="sep desktop-only" />
            <button className="icon-btn desktop-only" onClick={() => setZoom(Math.max(50, zoom - 25))} disabled={zoom <= 50} aria-label="Zoom out" title="Zoom out">
              <ZoomOut size={17} />
            </button>
            <button className="btn quiet zoom-label desktop-only" style={{ height: 28, padding: 0 }} onClick={() => setZoom(100)} title="Fit width">
              {zoom === 100 ? "Fit" : `${zoom}%`}
            </button>
            <button className="icon-btn desktop-only" onClick={() => setZoom(Math.min(250, zoom + 25))} disabled={zoom >= 250} aria-label="Zoom in" title="Zoom in">
              <ZoomIn size={17} />
            </button>
            {shell.dark && (
              <button className="icon-btn" aria-pressed={dim} onClick={() => setDim(!dim)} title="Dark pages" aria-label="Dark pages">
                <SunMoon size={17} />
              </button>
            )}
            <span className="sep desktop-only" />
          </>
        )}
        <a className="icon-btn" href={originalUrl(course.id, route.id)} download title="Download original" aria-label="Download original">
          <Download size={17} />
        </a>
        <button className="icon-btn" title="Ask about this page" aria-label="Ask about this source" onClick={() => onAsk({})}>
          <MessageSquare size={17} />
        </button>
      </Toolbar>
      {source?.reading_status === "failed" && (
        <div className="banner warn">
          AI reading stopped before every page was read{source.reading_error ? `: ${source.reading_error}` : "."}
          <button
            className="btn"
            onClick={() =>
              api(`${coursePath(course.id)}/sources/${route.id}/read`, { method: "POST", json: {} }).then(
                () => setSource({ ...source, reading_status: "pending" }),
                () => {},
              )
            }
          >
            Try again
          </button>
        </div>
      )}
      <div className="scroll" ref={scroller} style={{ scrollBehavior: "auto" }}>
        {error && (
          <div className="empty">
            <div>
              <h2>This source can't be opened</h2>
              <p>{error}</p>
            </div>
          </div>
        )}
        {source && source.status !== "ready" && (
          <div className="empty">
            <div>
              {source.status === "failed" ? (
                <>
                  <h2>Couldn't read this file</h2>
                  <p>{source.error ?? "Text extraction failed."} Try uploading it again, or download the original.</p>
                </>
              ) : (
                <>
                  <div className="spinner" style={{ margin: "0 auto 12px" }} />
                  <h2>Reading {source.filename}</h2>
                  <p>Extracting text and indexing it for search. This usually takes a few seconds.</p>
                </>
              )}
            </div>
          </div>
        )}
        {pages > 0 && (
          <div className="pages" style={{ gap: 36 }}>
            {Array.from({ length: pages }, (_, i) => (
              <PageImage
                key={i + 1}
                course={course.id}
                source={route.id}
                page={i + 1}
                width={width}
                ratio={ratio}
                onRatio={setRatio}
                dim={shell.dark && dim}
              />
            ))}
          </div>
        )}
        {source?.status === "ready" && pages === 0 && (
          <article className="sheet text-source">
            <h1 className="doc-title">{source.filename}</h1>
            <div className="doc-meta">
              <span>Text extracted from the original file</span>
            </div>
            {source.chunks.map((chunk, i) => {
              const previous = source.chunks[i - 1];
              const markdown = /\.(md|markdown|txt)$/i.test(source.filename);
              const slide = chunk.page !== null && chunk.page !== previous?.page;
              const heading = !markdown && chunk.section && chunk.section !== previous?.section && chunk.text !== chunk.section;
              return (
                <div key={chunk.id}>
                  {slide && <div className="slide-label">{/\.pptx?$/i.test(source.filename) ? "Slide" : "Page"} {chunk.page}</div>}
                  <div className="chunk">
                    {heading && <h3>{chunk.section}</h3>}
                    {markdown ? <Markdown text={chunk.text} /> : <div className="plain">{chunk.text}</div>}
                  </div>
                </div>
              );
            })}
          </article>
        )}
      </div>
    </>
  );
}
