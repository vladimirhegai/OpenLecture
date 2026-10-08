import {
  Check,
  Clock,
  Loader,
  X,
  ChevronsUpDown,
  FileText,
  Monitor,
  Moon,
  NotebookPen,
  Plus,
  Presentation,
  Search,
  Settings,
  Sun,
  Upload,
} from "lucide-react";
import { useRef } from "react";
import type { Course, DocumentSummary, Provider, Source, Task } from "../api";
import type { ThemePref } from "../theme";
import { toolVerb } from "../labels";
import { modelLabel, type Selection } from "./ModelPicker";
import { BrandMark, Popover } from "./ui";
import type { Route } from "./Views";

const THEME_NEXT: Record<ThemePref, ThemePref> = { system: "light", light: "dark", dark: "system" };
const THEME_ICON = { system: Monitor, light: Sun, dark: Moon };
const THEME_NAME = { system: "Theme: match system", light: "Theme: light", dark: "Theme: dark" };

function sourceIcon(filename: string) {
  return /\.(pptx?)$/i.test(filename) ? Presentation : FileText;
}

function SourceState({ source }: { source: Source }) {
  if (source.status === "failed" || source.reading_status === "failed")
    return <span className="status-dot failed" title={source.error ?? "AI reading did not finish. Open the source to retry."} />;
  if (source.status !== "ready") return <span className="status-dot" title="Processing the file" />;
  const progress = `${source.reading_pages_done ?? 0}/${source.reading_pages_total ?? 0} pages`;
  if (source.reading_status === "running")
    return <Loader size={13} className="reading-icon spin" aria-label={`AI is reading: ${progress}`} />;
  if (source.reading_status === "pending")
    return <Clock size={13} className="reading-icon" aria-label={`Waiting for AI reading (${progress})`} />;
  return null;
}

function Activity({ tasks, onCancel }: { tasks: Task[]; onCancel: (task: Task) => void }) {
  const active = tasks.filter((task) => task.status === "queued" || task.status === "running");
  if (!active.length) return null;
  const reading = active.filter((task) => task.kind === "read_source").length;
  const writing = active.length - reading;
  const summary = [writing && `Writing ${writing === 1 ? "1 note" : `${writing} notes`}`, reading && `reading ${reading === 1 ? "1 source" : `${reading} sources`}`]
    .filter(Boolean)
    .join(", ");
  return (
    <Popover
      style={{ left: 10, right: 10, top: 40, maxHeight: 360, overflowY: "auto" }}
      trigger={({ toggle, open }) => (
        <button className="activity-trigger" onClick={toggle} aria-expanded={open}>
          <span className="spinner" />
          <span>{summary.charAt(0).toUpperCase() + summary.slice(1)}</span>
        </button>
      )}
    >
      {() => (
        <>
          <div className="menu-label">AI at work</div>
          {active.map((task) => {
            const step = [...task.log].reverse().find((entry) => entry.tool)?.tool;
            return (
              <div key={task.id} className="task-row">
                {task.status === "running" ? <span className="spinner" /> : <Clock size={14} style={{ marginTop: 3, color: "var(--ink-3)" }} />}
                <span className="grow">
                  {task.title}
                  <span className="sub">
                    {task.status === "queued"
                      ? "Waiting to start"
                      : task.kind === "read_source"
                        ? "Reading pages"
                        : step
                          ? toolVerb(step)
                          : "Starting"}
                    {task.params.model ? `, ${task.params.model}` : ""}
                  </span>
                </span>
                <button className="icon-btn" onClick={() => onCancel(task)} title="Stop" aria-label={`Stop ${task.title}`}>
                  <X size={14} />
                </button>
              </div>
            );
          })}
        </>
      )}
    </Popover>
  );
}

export function Sidebar({
  courses,
  course,
  docs,
  sources,
  tasks,
  onCancelTask,
  route,
  providers,
  selection,
  theme,
  onTheme,
  onCourse,
  onNewCourse,
  onOpen,
  onSearch,
  onUpload,
  onSettings,
}: {
  courses: Course[];
  course: Course | null;
  docs: DocumentSummary[];
  sources: Source[];
  tasks: Task[];
  onCancelTask: (task: Task) => void;
  route: Route;
  providers: Provider[];
  selection: Selection;
  theme: ThemePref;
  onTheme: (theme: ThemePref) => void;
  onCourse: (id: string) => void;
  onNewCourse: () => void;
  onOpen: (route: Route) => void;
  onSearch: () => void;
  onUpload: (file: File) => void;
  onSettings: () => void;
}) {
  const file = useRef<HTMLInputElement>(null);
  const ThemeIcon = THEME_ICON[theme];
  const provider = providers.find((p) => p.id === selection.provider);
  const signedIn = providers.some((p) => p.signed_in);
  const isMac = /Mac|iPhone|iPad/.test(navigator.platform);

  return (
    <nav className="sidebar" aria-label="Course navigation">
      <div className="brand">
        <BrandMark />
        Open Lecture
        <span className="spacer" />
      </div>

      <Popover
        wrapStyle={{ margin: "0 10px 6px" }}
        style={{ left: 0, right: 0, top: 54 }}
        trigger={({ toggle, open }) => (
          <button className="course-trigger" onClick={toggle} aria-expanded={open} aria-haspopup="menu">
            <span className="grow">
              <span className="code">{course?.code ?? "No course"}</span>
              <span className="title">{course?.title ?? "Create a course to begin"}</span>
            </span>
            <ChevronsUpDown size={15} color="var(--ink-3)" />
          </button>
        )}
      >
        {(close) => (
          <>
            {courses.map((c) => (
              <button
                key={c.id}
                className="menu-item"
                role="menuitemradio"
                aria-checked={c.id === course?.id}
                onClick={() => {
                  onCourse(c.id);
                  close();
                }}
              >
                <span className="grow">
                  {c.code}
                  <span className="sub">{c.title}</span>
                </span>
                {c.id === course?.id && <Check size={15} className="check" />}
              </button>
            ))}
            {courses.length > 0 && <div className="menu-sep" />}
            <button
              className="menu-item"
              onClick={() => {
                close();
                onNewCourse();
              }}
            >
              <Plus size={16} /> New course
            </button>
          </>
        )}
      </Popover>

      <button className="search-trigger" onClick={onSearch} disabled={!course}>
        <Search size={15} />
        <span>Search</span>
        <kbd>{isMac ? "⌘K" : "Ctrl K"}</kbd>
      </button>

      <Activity tasks={tasks} onCancel={onCancelTask} />

      <div className="nav">
        {course && (
          <>
            <div className="nav-section">
              <button className="nav-item" aria-current={route.kind === "home" ? "page" : undefined} onClick={() => onOpen({ kind: "home" })}>
                <NotebookPen size={16} />
                <span className="label">Overview</span>
              </button>
            </div>

            <div className="nav-section">
              <div className="nav-head">
                <span>Notes</span>
              </div>
              {docs.length === 0 && <div className="nav-empty">Notes you ask for appear here.</div>}
              {docs.map((doc) => (
                <button
                  key={doc.document_id}
                  className="nav-item"
                  aria-current={route.kind === "doc" && route.id === doc.document_id ? "page" : undefined}
                  onClick={() => onOpen({ kind: "doc", id: doc.document_id })}
                  title={doc.title}
                >
                  <FileText size={16} />
                  <span className="label">{doc.title.replace(`${course.code}: `, "")}</span>
                  {doc.potentially_outdated && <span className="status-dot" title="May be out of date" />}
                  {doc.academic_week && <span className="meta">W{doc.academic_week}</span>}
                </button>
              ))}
            </div>

            <div className="nav-section">
              <div className="nav-head">
                <span>Sources</span>
                <button className="icon-btn" onClick={() => file.current?.click()} title="Upload a source" aria-label="Upload a source">
                  <Upload size={14} />
                </button>
                <input
                  ref={file}
                  type="file"
                  hidden
                  accept=".pdf,.docx,.pptx,.md,.txt,.csv,.json,.png,.jpg,.jpeg,.webp"
                  onChange={(e) => {
                    const chosen = e.target.files?.[0];
                    if (chosen) onUpload(chosen);
                    e.target.value = "";
                  }}
                />
              </div>
              {sources.length === 0 && (
                <button className="nav-item" onClick={() => file.current?.click()}>
                  <Plus size={16} />
                  <span className="label">Add lecture slides or notes</span>
                </button>
              )}
              {sources.map((source) => {
                const Icon = sourceIcon(source.filename);
                return (
                  <button
                    key={source.id}
                    className="nav-item"
                    aria-current={route.kind === "source" && route.id === source.id ? "page" : undefined}
                    onClick={() => onOpen({ kind: "source", id: source.id })}
                    title={source.filename}
                  >
                    <Icon size={16} />
                    <span className="label">{source.filename}</span>
                    <SourceState source={source} />
                    {source.kind === "textbook" ? (
                      <span className="meta">Book</span>
                    ) : (
                      source.week && <span className="meta">W{source.week}</span>
                    )}
                  </button>
                );
              })}
            </div>
          </>
        )}
      </div>

      <div className="sidebar-foot">
        <button className="account" onClick={onSettings} title="AI accounts and settings">
          <span className={`presence ${signedIn ? "on" : ""}`} />
          <span>{signedIn ? (provider?.signed_in ? modelLabel(providers, selection) : "Choose a model") : "Connect an AI"}</span>
        </button>
        <button className="icon-btn" onClick={() => onTheme(THEME_NEXT[theme])} title={THEME_NAME[theme]} aria-label={THEME_NAME[theme]}>
          <ThemeIcon size={16} />
        </button>
        <button className="icon-btn" onClick={onSettings} title="Settings" aria-label="Settings">
          <Settings size={16} />
        </button>
      </div>
    </nav>
  );
}
