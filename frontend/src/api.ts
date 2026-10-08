export type Course = { id: string; code: string; title: string; created_at: string };

export type Citation = { source_id: string; version: number; chunk_id: string };

type BlockBase = { id: string; citations: Citation[] };
export type Step = { explanation: string; latex: string };
export type Block = BlockBase &
  (
    | { type: "paragraph"; text: string }
    | { type: "heading"; text: string; level: number }
    | { type: "equation"; latex: string; display: boolean }
    | { type: "list"; items: string[]; ordered: boolean }
    | { type: "callout"; text: string; tone: "info" | "warning" | "tip" }
    | { type: "table"; columns: string[]; rows: string[][] }
    | { type: "code"; language: string; text: string }
    | { type: "derivation"; title: string; steps: { explanation: string; latex: string }[] }
    | {
        type: "practice_problem";
        title?: string;
        prompt: string;
        solution: string;
        steps?: Step[];
        answer?: string;
        origin: "original" | "source";
        difficulty: "introductory" | "intermediate" | "advanced";
      }
    | { type: "worked_example"; title: string; prompt: string; steps: Step[]; answer: string }
    | { type: "schematic"; source: string; caption: string }
    | { type: "solution"; title: string; text: string; collapsed: boolean }
    | { type: "artifact_reference"; artifact_id: string; caption: string }
  );

export type DocumentSummary = {
  document_id: string;
  course_id: string;
  title: string;
  document_type: "study_notes" | "revision_sheet" | "practice_set" | "reference";
  academic_week: number | null;
  topic_keys: string[];
  revision: number;
  deleted: boolean;
  updated_at: string;
  potentially_outdated: boolean;
};
export type Doc = DocumentSummary & { blocks: Block[] };
export type Revision = { revision: number; actor: "student" | "agent"; created_at: string };

export type Source = {
  id: string;
  filename: string;
  kind: string;
  week: number | null;
  current_version: number;
  created_at: string;
  status: "queued" | "running" | "ready" | "failed";
  error: string | null;
  page_count: number | null;
  reading_status: "pending" | "running" | "ready" | "failed" | "skipped" | null;
  reading_pages_done: number | null;
  reading_pages_total: number | null;
  reading_error?: string | null;
};
export type Chunk = { id: string; source_id: string; version: number; page: number | null; section: string | null; text: string };
export type SourceDetail = Source & { version: number; pages: number | null; chunks: Chunk[] };
export type SearchHit = Chunk & { filename: string; kind: string };

export type Topic = { key: string; title: string; week: number | null; reading?: string };
export type Profile = {
  term: string;
  topics: Topic[];
  study_preferences: string[];
};

export type Chat = { id: string; title: string; created_at: string };
export type DocumentReference = { document_id: string; revision: number; block_id?: string | null };
export type Message = {
  id: string;
  role: "user" | "assistant";
  content: string;
  sequence: number;
  created_at: string;
  references: DocumentReference[];
};

export type Artifact = { id: string; kind: string; title: string; created_at: string; payload: Record<string, any> };

export type Model = { id: string; label: string; efforts: string[]; default_effort?: string | null };
export type Provider = {
  id: "claude" | "codex";
  name: string;
  installed: boolean;
  version: string | null;
  signed_in: boolean;
  account: string | null;
  plan: string | null;
  method: string | null;
  login_command: string;
  models: Model[];
  default_model: string | null;
  error?: string;
};

export type ModelChoice = { provider: "claude" | "codex"; model: string; effort: string | null };
export type AppSettings = { reading_model: ModelChoice };
export type TaskLogEntry = { tool?: string; text?: string };
export type Task = {
  id: string;
  kind: "read_source" | "week_notes";
  title: string;
  status: "queued" | "running" | "completed" | "failed" | "cancelled";
  params: Record<string, any>;
  log: TaskLogEntry[];
  result: Record<string, any> | null;
  error: string | null;
  created_at: string;
  updated_at: string;
};

export type RunEvent =
  | { type: "user_message"; message: Message }
  | { type: "text_start" }
  | { type: "text"; delta: string }
  | { type: "tool"; name: string }
  | { type: "done"; message: Message }
  | { type: "error"; message: string };

export class ApiError extends Error {
  constructor(
    public status: number,
    public code: string,
    message: string,
  ) {
    super(message);
  }
}

const TOKEN_KEY = "ol-token";
export function getToken() {
  try {
    return localStorage.getItem(TOKEN_KEY);
  } catch {
    return null;
  }
}
export function setToken(token: string) {
  try {
    localStorage.setItem(TOKEN_KEY, token);
  } catch {
    /* storage unavailable */
  }
}

function headers(extra?: HeadersInit): HeadersInit {
  const token = getToken();
  return { ...(token ? { Authorization: `Bearer ${token}` } : {}), ...extra };
}

async function failure(response: Response): Promise<ApiError> {
  let code = "http_error";
  let message = `Request failed (${response.status})`;
  try {
    const body = await response.json();
    if (body.error) ({ code, message } = body.error);
    else if (typeof body.detail === "string") message = body.detail;
  } catch {
    /* not JSON */
  }
  if (response.status === 401) window.dispatchEvent(new Event("ol:unauthorized"));
  return new ApiError(response.status, code, message);
}

export async function api<T>(path: string, init: RequestInit & { json?: unknown } = {}): Promise<T> {
  const { json, ...rest } = init;
  const response = await fetch(`/api/v1${path}`, {
    ...rest,
    headers: headers(json !== undefined ? { "Content-Type": "application/json" } : undefined),
    body: json !== undefined ? JSON.stringify(json) : rest.body,
  });
  if (!response.ok) throw await failure(response);
  return response.json() as Promise<T>;
}

export const course = (id: string) => `/courses/${id}`;

export async function pageImage(courseId: string, sourceId: string, page: number, signal?: AbortSignal) {
  const response = await fetch(`/api/v1${course(courseId)}/sources/${sourceId}/pages/${page}`, {
    headers: headers(),
    signal,
  });
  if (!response.ok) throw await failure(response);
  return URL.createObjectURL(await response.blob());
}

const schematicCache = new Map<string, Promise<string>>();

export const schematicSeen = (source: string) => schematicCache.has(source);

/** Render a schematic-language drawing to an SVG object URL; identical drawings render once. */
export function schematicImage(source: string) {
  if (!schematicCache.has(source)) {
    const load = (async () => {
      const response = await fetch("/api/v1/schematics/render", {
        method: "POST",
        headers: headers({ "Content-Type": "application/json" }),
        body: JSON.stringify({ source }),
      });
      if (!response.ok) throw await failure(response);
      return URL.createObjectURL(await response.blob());
    })();
    load.catch(() => schematicCache.delete(source));
    schematicCache.set(source, load);
  }
  return schematicCache.get(source)!;
}

const citationCache = new Map<string, Promise<{ filename: string; pages: Map<string, number | null> }>>();

/** Resolve a citation to its source filename and page. Chunk lists are fetched once per source version. */
export async function resolveCitation(courseId: string, citation: Citation) {
  const key = `${citation.source_id}:${citation.version}`;
  if (!citationCache.has(key)) {
    const load = (async () => {
      const pages = new Map<string, number | null>();
      let filename = "Source";
      for (let offset = 0; ; offset += 100) {
        const detail = await api<SourceDetail>(
          `${course(courseId)}/sources/${citation.source_id}?version=${citation.version}&limit=100&offset=${offset}`,
        );
        filename = detail.filename;
        for (const chunk of detail.chunks) pages.set(chunk.id, chunk.page);
        if (detail.chunks.length < 100) break;
      }
      return { filename, pages };
    })();
    load.catch(() => citationCache.delete(key));
    citationCache.set(key, load);
  }
  const { filename, pages } = await citationCache.get(key)!;
  return { filename, page: pages.get(citation.chunk_id) ?? null };
}

export function originalUrl(courseId: string, sourceId: string) {
  return `/api/v1${course(courseId)}/sources/${sourceId}/original`;
}

export async function upload(courseId: string, file: File, kind: string, week: number | null = null) {
  const form = new FormData();
  form.append("file", file);
  form.append("kind", kind);
  if (week) form.append("week", String(week));
  return api<{ source_id: string; job_id: string; status: string; duplicate: boolean }>(`${course(courseId)}/sources`, {
    method: "POST",
    body: form,
  });
}

/** POST a chat turn and yield server-sent events until the run ends or ``signal`` aborts. */
export async function* runAgent(
  courseId: string,
  chatId: string,
  body: Record<string, unknown>,
  signal: AbortSignal,
): AsyncGenerator<RunEvent> {
  const response = await fetch(`/api/v1${course(courseId)}/chats/${chatId}/runs`, {
    method: "POST",
    headers: headers({ "Content-Type": "application/json" }),
    body: JSON.stringify(body),
    signal,
  });
  if (!response.ok || !response.body) throw await failure(response);
  const reader = response.body.pipeThrough(new TextDecoderStream()).getReader();
  let buffer = "";
  for (;;) {
    const { value, done } = await reader.read();
    if (done) return;
    buffer += value;
    let boundary;
    while ((boundary = buffer.indexOf("\n\n")) !== -1) {
      const frame = buffer.slice(0, boundary);
      buffer = buffer.slice(boundary + 2);
      const data = frame
        .split("\n")
        .filter((line) => line.startsWith("data: "))
        .map((line) => line.slice(6))
        .join("\n");
      if (data) yield JSON.parse(data) as RunEvent;
    }
  }
}

export function relativeTime(iso: string) {
  const seconds = (Date.now() - new Date(iso).getTime()) / 1000;
  if (seconds < 60) return "just now";
  const units: [number, Intl.RelativeTimeFormatUnit][] = [
    [3600, "minute"],
    [86400, "hour"],
    [604800, "day"],
    [2629800, "week"],
    [31557600, "month"],
    [Infinity, "year"],
  ];
  const divisors = [60, 3600, 86400, 604800, 2629800, 31557600];
  const format = new Intl.RelativeTimeFormat(undefined, { numeric: "auto" });
  for (let index = 0; index < units.length; index++) {
    if (seconds < units[index][0]) return format.format(-Math.round(seconds / divisors[index]), units[index][1]);
  }
  return "";
}
