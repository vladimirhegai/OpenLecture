import katex from "katex";
import { memo } from "react";
import ReactMarkdown, { type Components } from "react-markdown";
import rehypeKatex from "rehype-katex";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import { Graph } from "./mathtools/Graph";
import { Graph3D } from "./mathtools/Graph3D";
import { CircuitSteps } from "./mathtools/CircuitSteps";
import { LogicSteps } from "./mathtools/LogicSteps";
import { Stepper } from "./mathtools/Stepper";
import { Schematic } from "./Schematic";
import { DigitalFigure } from "./DigitalFigure";
import { newEntry, rememberScroll } from "../scroll";

/** Agents often write \( \) and \[ \]; remark-math expects dollar delimiters. */
export function normalizeMath(text: string) {
  return text
    .replace(/\\\[([\s\S]+?)\\\]/g, (_, body) => `\n$$\n${body.trim()}\n$$\n`)
    .replace(/\\\(([\s\S]+?)\\\)/g, (_, body) => `$${body.trim()}$`);
}

export const slug = (text: string) => text.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

/** Navigate inside the app, the same way the sidebar does: remember this entry's scroll position (so Back returns
 * there), push a new history entry, and let App re-read the URL. Never a new tab. */
function openInApp(url: string) {
  rememberScroll();
  history.pushState(newEntry(), "", url);
  window.dispatchEvent(new PopStateEvent("popstate"));
}

/** In-note links name a heading, not a block id (ids change whenever a note is rebuilt): `[B2](#b2)` scrolls to the first
 * heading whose text starts with "B2". It goes through the URL hash, so collapsed sections open and Back returns. */
function jumpToHeading(label: string) {
  const want = slug(label);
  for (const section of document.querySelectorAll<HTMLElement>("section.block-heading")) {
    const text = slug(section.querySelector(".collapsible-heading")?.textContent ?? "");
    if (text !== want && !text.startsWith(want + "-")) continue;
    const hash = "#" + section.id.slice(2);
    if (location.hash === hash) section.scrollIntoView({ block: "start", behavior: "smooth" });
    else openInApp(location.pathname + location.search + hash);
    return;
  }
}

/** A link to a page of this app (a path, or a full URL on this host), as a path; null for external links. */
function appPath(href: string): string | null {
  try {
    const url = new URL(href, location.origin);
    return url.origin === location.origin ? url.pathname + url.search + url.hash : null;
  } catch {
    return null;
  }
}

const link: Components["a"] = ({ href, children }) => {
  const inApp = href && !href.startsWith("#") ? appPath(href) : null;
  return href?.startsWith("#") ? (
    <a
      href={href}
      className="note-link"
      onClick={(event) => {
        event.preventDefault();
        jumpToHeading(decodeURIComponent(href.slice(1)));
      }}
    >
      {children}
    </a>
  ) : inApp ? (
    <a
      href={inApp}
      // A link to another note ("Week 3 · Topic 2") renders as a small tag; other app links stay text.
      className={inApp.startsWith("/courses/") && inApp.includes("/docs/") ? "note-tag" : "note-link"}
      onClick={(event) => {
        if (event.ctrlKey || event.metaKey || event.shiftKey) return; // the reader asked for a new tab
        event.preventDefault();
        openInApp(inApp);
      }}
    >
      {children}
    </a>
  ) : (
    <a href={href} target="_blank" rel="noreferrer noopener">
      {children}
    </a>
  );
};

const inlineComponents: Components = { p: ({ children }) => <>{children}</>, a: link };
/** Fenced tools: ```schematic circuits, ```steps equation steppers, ```circuitsteps/```logicsteps step-through circuits, ```graph and ```graph3d interactive plots
 * (grammar in skills/math-tools.md). Other code blocks stay code. */
const TOOLS: Record<string, (source: string) => React.ReactNode> = {
  "language-digital": (source) => <DigitalFigure source={source} />,
  "language-schematic": (source) => <Schematic source={source} />,
  "language-steps": (source) => <Stepper source={source} />,
  "language-circuitsteps": (source) => <CircuitSteps source={source} />,
  "language-logicsteps": (source) => <LogicSteps source={source} />,
  "language-graph": (source) => <Graph source={source} />,
  "language-graph3d": (source) => <Graph3D source={source} />,
};

const pre: Components["pre"] = ({ children, node }) => {
  const code = node?.children[0];
  const classes = code && "properties" in code ? code.properties?.className : undefined;
  const tool = Array.isArray(classes) ? classes.map(String).find((c) => c in TOOLS) : undefined;
  if (tool && code && "children" in code) {
    const text = code.children.map((child) => ("value" in child ? child.value : "")).join("");
    return <>{TOOLS[tool](text)}</>;
  }
  return <pre>{children}</pre>;
};

const blockComponents: Components = {
  a: link,
  pre,
  table: ({ children }) => (
    <div className="table-wrap">
      <table>{children}</table>
    </div>
  ),
};

/** Markdown with GFM and KaTeX math. Raw HTML is never rendered. */
export const Markdown = memo(function Markdown({ text, inline }: { text: string; inline?: boolean }) {
  return (
    <ReactMarkdown
      remarkPlugins={[remarkGfm, [remarkMath, { singleDollarTextMath: true }]]}
      rehypePlugins={[[rehypeKatex, { throwOnError: false, strict: "ignore" }]]}
      components={inline ? inlineComponents : blockComponents}
    >
      {normalizeMath(text)}
    </ReactMarkdown>
  );
});

export function Tex({ latex, display = true }: { latex: string; display?: boolean }) {
  const html = katex.renderToString(latex, { displayMode: display, throwOnError: false, strict: "ignore" });
  return display ? (
    <div className="equation" dangerouslySetInnerHTML={{ __html: html }} />
  ) : (
    <span dangerouslySetInnerHTML={{ __html: html }} />
  );
}
