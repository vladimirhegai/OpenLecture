import { FileText, Search as SearchIcon, TextQuote } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { api, course as coursePath, type Course, type DocumentSummary, type SearchHit, type Source } from "../api";
import { Dialog } from "./ui";
import type { Route } from "./Views";

type Result =
  | { kind: "doc"; doc: DocumentSummary }
  | { kind: "source"; source: Source }
  | { kind: "hit"; hit: SearchHit };

function snippet(text: string, query: string) {
  const clean = text.replace(/\s+/g, " ").trim();
  const word = query.split(/\s+/).find((w) => w.length > 2);
  const at = word ? clean.toLowerCase().indexOf(word.toLowerCase()) : -1;
  const start = Math.max(0, at - 60);
  return (start > 0 ? "…" : "") + clean.slice(start, start + 220);
}

export function SearchPalette({
  course,
  docs,
  sources,
  onOpen,
  onClose,
}: {
  course: Course;
  docs: DocumentSummary[];
  sources: Source[];
  onOpen: (route: Route) => void;
  onClose: () => void;
}) {
  const [query, setQuery] = useState("");
  const [hits, setHits] = useState<SearchHit[]>([]);
  const [noteHits, setNoteHits] = useState<DocumentSummary[] | null>(null);
  const [loading, setLoading] = useState(false);
  const [active, setActive] = useState(0);

  useEffect(() => {
    const q = query.trim();
    if (!q) {
      setHits([]);
      setNoteHits(null);
      return;
    }
    setLoading(true);
    const timer = setTimeout(() => {
      Promise.all([
        api<SearchHit[]>(`${coursePath(course.id)}/search?query=${encodeURIComponent(q)}&limit=12`).catch(() => []),
        api<DocumentSummary[]>(`${coursePath(course.id)}/documents?query=${encodeURIComponent(q)}&limit=8`).catch(() => []),
      ]).then(([passages, notes]) => {
        setHits(passages);
        setNoteHits(notes);
        setLoading(false);
        setActive(0);
      });
    }, 180);
    return () => clearTimeout(timer);
  }, [query, course.id]);

  const results: Result[] = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return [...docs.slice(0, 6).map((doc) => ({ kind: "doc" as const, doc })), ...sources.slice(0, 6).map((source) => ({ kind: "source" as const, source }))];
    const matchedSources = sources.filter((s) => s.filename.toLowerCase().includes(q));
    return [
      ...(noteHits ?? []).map((doc) => ({ kind: "doc" as const, doc })),
      ...matchedSources.map((source) => ({ kind: "source" as const, source })),
      ...hits.map((hit) => ({ kind: "hit" as const, hit })),
    ];
  }, [query, docs, sources, hits, noteHits]);

  function choose(result: Result) {
    if (result.kind === "doc") onOpen({ kind: "doc", id: result.doc.document_id });
    else if (result.kind === "source") onOpen({ kind: "source", id: result.source.id });
    else onOpen({ kind: "source", id: result.hit.source_id, page: result.hit.page ?? undefined });
    onClose();
  }

  return (
    <Dialog onClose={onClose} className="palette" bare title="Search">
      <div className="palette-input">
        <SearchIcon size={17} />
        <input
          autoFocus
          value={query}
          placeholder={`Search notes and sources in ${course.code}`}
          aria-label="Search"
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "ArrowDown") {
              e.preventDefault();
              setActive((a) => Math.min(results.length - 1, a + 1));
            } else if (e.key === "ArrowUp") {
              e.preventDefault();
              setActive((a) => Math.max(0, a - 1));
            } else if (e.key === "Enter" && results[active]) choose(results[active]);
          }}
        />
        {loading && <span className="spinner" />}
      </div>
      <div className="palette-results" role="listbox">
        {results.length === 0 && !loading && (
          <div className="palette-empty">{query.trim() ? `Nothing matches "${query.trim()}".` : "This course has no notes or sources yet."}</div>
        )}
        {results.map((result, i) => {
          const key = result.kind === "doc" ? result.doc.document_id : result.kind === "source" ? result.source.id : result.hit.id;
          return (
            <button key={key} className="result" role="option" aria-selected={i === active} onMouseMove={() => setActive(i)} onClick={() => choose(result)}>
              {result.kind === "hit" ? <TextQuote size={16} /> : <FileText size={16} />}
              <span className="grow">
                {result.kind === "doc" && (
                  <>
                    <div>{result.doc.title}</div>
                    <div className="where">Note</div>
                  </>
                )}
                {result.kind === "source" && (
                  <>
                    <div>{result.source.filename}</div>
                    <div className="where">Source</div>
                  </>
                )}
                {result.kind === "hit" && (
                  <>
                    <div className="snippet">{snippet(result.hit.text, query)}</div>
                    <div className="where">
                      {result.hit.filename}
                      {result.hit.page ? `, page ${result.hit.page}` : ""}
                    </div>
                  </>
                )}
              </span>
            </button>
          );
        })}
      </div>
    </Dialog>
  );
}
