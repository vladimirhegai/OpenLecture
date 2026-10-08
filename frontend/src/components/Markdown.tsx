import katex from "katex";
import { memo } from "react";
import ReactMarkdown, { type Components } from "react-markdown";
import rehypeKatex from "rehype-katex";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import { Schematic } from "./Schematic";

/** Agents often write \( \) and \[ \]; remark-math expects dollar delimiters. */
export function normalizeMath(text: string) {
  return text
    .replace(/\\\[([\s\S]+?)\\\]/g, (_, body) => `\n$$\n${body.trim()}\n$$\n`)
    .replace(/\\\(([\s\S]+?)\\\)/g, (_, body) => `$${body.trim()}$`);
}

const link: Components["a"] = ({ href, children }) => (
  <a href={href} target="_blank" rel="noreferrer noopener">
    {children}
  </a>
);

const inlineComponents: Components = { p: ({ children }) => <>{children}</>, a: link };
/** ```schematic fences render as circuit diagrams; other code blocks stay code. */
const pre: Components["pre"] = ({ children, node }) => {
  const code = node?.children[0];
  const classes = code && "properties" in code ? code.properties?.className : undefined;
  if (Array.isArray(classes) && classes.includes("language-schematic") && code && "children" in code) {
    const text = code.children.map((child) => ("value" in child ? child.value : "")).join("");
    return <Schematic source={text} />;
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
