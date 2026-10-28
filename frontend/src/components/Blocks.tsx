import { AlertTriangle, BookOpen, ChevronRight, History, Info, Lightbulb, MessageSquarePlus } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { resolveCitation, type Block, type Citation, type Step } from "../api";
import { ArtifactCard } from "./ArtifactCard";
import { Markdown, Tex } from "./Markdown";
import { Schematic } from "./Schematic";
import { DigitalFigure } from "./DigitalFigure";

type Handlers = {
  courseId: string;
  onCite: (citation: Citation) => void;
  onAsk?: (block: Block) => void;
};

/** A heading, or a block taller than the note's scroll area, is scrolled to its top; anything else to the centre. */
export function scrollsToTop(element: HTMLElement) {
  const viewport = element.closest(".scroll")?.clientHeight ?? window.innerHeight;
  return element.classList.contains("block-heading") || element.offsetHeight > viewport * 0.8;
}

function Reveal({ label, children, open }: { label: string; children: React.ReactNode; open?: boolean }) {
  return (
    <details className="reveal" open={open}>
      <summary>
        <ChevronRight size={14} />
        <Markdown text={label} inline />
      </summary>
      <div className="reveal-body">{children}</div>
    </details>
  );
}

/** Opens the page a sourced practice problem came from, e.g. the textbook page with its figure. */
function ProblemSource({ courseId, citation, onCite }: { courseId: string; citation: Citation; onCite: Handlers["onCite"] }) {
  const [where, setWhere] = useState<{ filename: string; page: number | null } | null>(null);
  useEffect(() => {
    resolveCitation(courseId, citation).then(setWhere, () => setWhere(null));
  }, [courseId, citation]);
  const book = where && /text\s*book/i.test(where.filename);
  const name = book ? "Textbook" : (where?.filename.replace(/\.[a-z0-9]+$/i, "").replace(/_/g, " ") ?? "Source");
  const short = name.length > 26 ? `${name.slice(0, 24).trimEnd()}…` : name;
  return (
    <button className="problem-source" onClick={() => onCite(citation)} title={`Open ${where?.filename ?? "the source"}${where?.page ? ` at page ${where.page}` : ""}`}>
      <BookOpen size={13} />
      {short}
      {where?.page ? `, p. ${where.page}` : ""}
    </button>
  );
}

function Steps({ steps }: { steps: Step[] }) {
  return (
    <ol className="steps">
      {steps.map((step, i) => (
        <li key={i}>
          <Markdown text={step.explanation} />
          {step.latex && <Tex latex={step.latex} />}
        </li>
      ))}
    </ol>
  );
}

function Answer({ text }: { text?: string }) {
  if (!text) return null;
  return (
    <div className="answer">
      <span className="answer-label">Answer</span>
      <Markdown text={text} />
    </div>
  );
}

function Content({ block, courseId, onCite, toggle }: { block: Block; courseId: string; onCite: Handlers["onCite"]; toggle?: React.ReactNode }) {
  switch (block.type) {
    case "heading": {
      const Tag = `h${Math.min(block.level + 1, 6)}` as "h2";
      return (
        <Tag className={`heading-${Math.min(block.level, 4)} collapsible-heading`}>
          {toggle}
          <Markdown text={block.text} inline />
        </Tag>
      );
    }
    case "paragraph":
      return <Markdown text={block.text} />;
    case "equation":
      return <Tex latex={block.latex} display={block.display} />;
    case "list": {
      const List = block.ordered ? "ol" : "ul";
      return (
        <List>
          {block.items.map((item, i) => (
            <li key={i}>
              <Markdown text={item} inline />
            </li>
          ))}
        </List>
      );
    }
    case "callout": {
      const Icon =
        block.tone === "warning" ? AlertTriangle : block.tone === "tip" ? Lightbulb : block.tone === "reminder" ? History : Info;
      return (
        <aside className={`callout ${block.tone}`}>
          <Icon size={17} />
          <div>
            <Markdown text={block.text} />
          </div>
        </aside>
      );
    }
    case "table":
      return (
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                {block.columns.map((column, i) => (
                  <th key={i}>
                    <Markdown text={column} inline />
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {block.rows.map((row, r) => (
                <tr key={r}>
                  {row.map((cell, c) => (
                    <td key={c}>
                      <Markdown text={cell} inline />
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
    case "code":
      if (block.language === "schematic") return <Schematic source={block.text} />;
      if (block.language === "digital") return <DigitalFigure source={block.text} />;
      return (
        <pre>
          <code>{block.text}</code>
        </pre>
      );
    case "derivation":
      return (
        <div>
          <div className="derivation-title">
            <Markdown text={block.title} inline />
          </div>
          <Steps steps={block.steps} />
        </div>
      );
    case "practice_problem":
      return (
        <div className="problem">
          <div className="problem-head">
            <span className="problem-kind">Problem</span>
            {block.title && (
              <span className="problem-title">
                <Markdown text={block.title} inline />
              </span>
            )}
            <span className="tag">{block.difficulty}</span>
            {block.citations[0] && <ProblemSource courseId={courseId} citation={block.citations[0]} onCite={onCite} />}
          </div>
          <div className="problem-body">
            <Markdown text={block.prompt} />
          </div>
          <Reveal label="Show solution">
            {block.steps?.length ? <Steps steps={block.steps} /> : null}
            {block.solution && <Markdown text={block.solution} />}
            <Answer text={block.answer} />
          </Reveal>
        </div>
      );
    case "worked_example":
      return (
        <div className="problem example">
          <div className="problem-head">
            <span className="problem-kind">Example</span>
            <span className="problem-title">
              <Markdown text={block.title} inline />
            </span>
            {block.citations[0] && <ProblemSource courseId={courseId} citation={block.citations[0]} onCite={onCite} />}
          </div>
          <div className="problem-body">
            <Markdown text={block.prompt} />
          </div>
          <div className="example-solution">
            <div className="example-label">Solution</div>
            <Steps steps={block.steps} />
          </div>
          <Answer text={block.answer} />
        </div>
      );
    case "schematic":
      return <Schematic source={block.source} caption={block.caption} />;
    case "solution":
      return (
        <Reveal label={block.title} open={!block.collapsed}>
          <Markdown text={block.text} />
        </Reveal>
      );
    case "artifact_reference":
      return <ArtifactCard courseId={courseId} id={block.artifact_id} caption={block.caption} />;
  }
}

function shortName(filename: string) {
  if (/text\s*book/i.test(filename)) return "Textbook";
  const name = filename
    .replace(/\.[a-z0-9]+$/i, "")
    .replace(/_/g, " ")
    .replace(/\s+(copy|updated|Fall\s*\d{4}|F\d{4})\b/gi, "")
    .trim();
  return name.length > 30 ? `${name.slice(0, 28).trimEnd()}…` : name;
}

/** One quiet pill per source file, with each cited page as its own link. */
function CitationGroup({ courseId, citations, onCite }: { courseId: string; citations: Citation[]; onCite: Handlers["onCite"] }) {
  const [resolved, setResolved] = useState<{ citation: Citation; filename: string; page: number | null }[] | null>(null);
  useEffect(() => {
    let live = true;
    Promise.all(
      citations.map((citation) =>
        resolveCitation(courseId, citation).then(
          (where) => ({ citation, ...where }),
          () => ({ citation, filename: "Source", page: null }),
        ),
      ),
    ).then((list) => live && setResolved(list));
    return () => {
      live = false;
    };
  }, [courseId, citations]);
  if (!resolved) return null;
  const groups = new Map<string, { filename: string; pages: { page: number | null; citation: Citation }[] }>();
  for (const item of resolved) {
    const key = item.citation.source_id;
    if (!groups.has(key)) groups.set(key, { filename: item.filename, pages: [] });
    const group = groups.get(key)!;
    if (!group.pages.some((p) => p.page === item.page)) group.pages.push({ page: item.page, citation: item.citation });
  }
  return (
    <>
      {[...groups.values()].map((group) => {
        const pages = group.pages.sort((a, b) => (a.page ?? 0) - (b.page ?? 0));
        return (
          <span key={group.filename} className="cite-pill" title={group.filename}>
            <button className="cite-name" onClick={() => onCite(pages[0].citation)}>
              {shortName(group.filename)}
            </button>
            {pages.some((p) => p.page) && <span className="cite-sep">p.</span>}
            {pages.map(
              (p) =>
                p.page && (
                  <button key={p.page} className="cite-page" onClick={() => onCite(p.citation)} aria-label={`Open ${group.filename} page ${p.page}`}>
                    {p.page}
                  </button>
                ),
            )}
          </span>
        );
      })}
    </>
  );
}

const OWN_SOURCE = new Set(["practice_problem", "worked_example"]);

/**
 * Sources are shown once per section, under its heading, instead of on every block.
 * Problems and examples keep their own source button.
 */
function sectionSources(blocks: Block[]) {
  const lines = new Map<string, Citation[]>(); // key: heading block id, or "" before the first heading
  let current = "";
  for (const block of blocks) {
    if (block.type === "heading" && block.level <= 2) current = block.id;
    if (OWN_SOURCE.has(block.type)) continue;
    const list = lines.get(current) ?? [];
    for (const citation of block.citations) if (!list.some((c) => c.chunk_id === citation.chunk_id)) list.push(citation);
    lines.set(current, list);
  }
  return lines;
}

const COLLAPSED_KEY = "ol-collapsed-headings";

/** Heading block ids the reader has collapsed; ids are UUIDs, so one set serves every note. */
function loadCollapsed(): Set<string> {
  try {
    return new Set(JSON.parse(localStorage.getItem(COLLAPSED_KEY) ?? "[]"));
  } catch {
    return new Set();
  }
}

function saveCollapsed(ids: Set<string>) {
  try {
    localStorage.setItem(COLLAPSED_KEY, JSON.stringify([...ids]));
  } catch {
    // Storage can be unavailable (private window); collapsing still works for this visit.
  }
}

/** For each block, the headings it sits under: a heading owns blocks until the next heading of the same or a higher level. */
function headingAncestors(blocks: Block[]) {
  const ancestors = new Map<string, string[]>();
  const open: { id: string; level: number }[] = [];
  for (const block of blocks) {
    if (block.type === "heading") {
      while (open.length && open[open.length - 1].level >= block.level) open.pop();
      ancestors.set(block.id, open.map((h) => h.id));
      open.push({ id: block.id, level: block.level });
    } else {
      ancestors.set(block.id, open.map((h) => h.id));
    }
  }
  return ancestors;
}

export function Blocks({ blocks, courseId, onCite, onAsk, flash }: Handlers & { blocks: Block[]; flash?: string | null }) {
  const sources = useMemo(() => sectionSources(blocks), [blocks]);
  const ancestors = useMemo(() => headingAncestors(blocks), [blocks]);
  const [collapsed, setCollapsed] = useState(loadCollapsed);
  const isHidden = (id: string) => (ancestors.get(id) ?? []).some((h) => collapsed.has(h));

  function toggle(id: string) {
    setCollapsed((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      saveCollapsed(next);
      return next;
    });
  }

  // A link to a block inside a collapsed section opens that section, then scrolls to the block.
  useEffect(() => {
    if (!flash) return;
    const closed = (ancestors.get(flash) ?? []).filter((h) => collapsed.has(h));
    if (!closed.length) return;
    setCollapsed((prev) => {
      const next = new Set(prev);
      closed.forEach((h) => next.delete(h));
      saveCollapsed(next);
      return next;
    });
    requestAnimationFrame(() => {
      const element = document.getElementById(`b-${flash}`);
      element?.scrollIntoView({ block: scrollsToTop(element) ? "start" : "center" });
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [flash]);

  const sourceLine = (key: string) => {
    const list = sources.get(key);
    return list?.length ? (
      <div className="section-sources">
        <CitationGroup courseId={courseId} citations={list} onCite={onCite} />
      </div>
    ) : null;
  };
  return (
    <>
      {sourceLine("")}
      {blocks.map((block) => {
        const closed = block.type === "heading" && collapsed.has(block.id);
        const toggleButton =
          block.type === "heading" ? (
            <button
              className={`collapse-toggle ${closed ? "closed" : ""}`}
              onClick={() => toggle(block.id)}
              aria-expanded={!closed}
              aria-label={closed ? "Expand section" : "Collapse section"}
              title={closed ? "Expand section" : "Collapse section"}
            >
              <ChevronRight size={18} />
            </button>
          ) : undefined;
        return (
          <section
            key={block.id}
            id={`b-${block.id}`}
            hidden={isHidden(block.id)}
            className={`block block-${block.type} ${flash === block.id ? "flash" : ""} ${closed ? "collapsed" : ""}`}
          >
            {onAsk && block.type !== "heading" && (
              <button className="icon-btn block-ask" onClick={() => onAsk(block)} title="Ask about this" aria-label="Ask about this block">
                <MessageSquarePlus size={15} />
              </button>
            )}
            <Content block={block} courseId={courseId} onCite={onCite} toggle={toggleButton} />
            {block.type === "heading" && block.level <= 2 && !closed && sourceLine(block.id)}
          </section>
        );
      })}
    </>
  );
}
