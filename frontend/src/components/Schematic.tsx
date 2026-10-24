import { useEffect, useMemo, useRef, useState } from "react";
import { schematicImage, schematicSeen } from "../api";
import { CurrentFlow } from "./flow/CurrentFlow";
import { parseFlow } from "./flow/circuit";
import { drawingOnly, ElevationButton, ElevationDialog, ElevationInline, parseElevation } from "./Elevation";
import { Markdown } from "./Markdown";
import { loadSvg, useAutoLayout, wrapPart, type Parsed } from "./mathtools/svgLayout";

/** The server's SVG drawn inline (not as an <img>) so autoLayout can move overlapping labels apart. */
function InlineSchematic({ drawing, alt, fallback }: { drawing: string; alt: string; fallback: string }) {
  const [parsed, setParsed] = useState<Parsed | null>(null);
  const [failed, setFailed] = useState(false);
  useEffect(() => {
    let live = true;
    loadSvg(drawing).then(
      (p) => live && setParsed(p),
      () => live && setFailed(true),
    );
    return () => {
      live = false;
    };
  }, [drawing]);
  const html = useMemo(() => parsed?.parts.map((p) => wrapPart(p)).join("") ?? "", [parsed]);
  const ref = useRef<SVGSVGElement>(null);
  useAutoLayout(ref, [html]);
  if (failed) return <img src={fallback} alt={alt} />;
  if (!parsed) return <div className="schematic-wait" />;
  const { x, y, w, h } = parsed.box;
  return (
    <svg ref={ref} className="schematic-svg" viewBox={`${x} ${y} ${w} ${h}`} width={(w * 4) / 3} role="img" aria-label={alt}>
      <g dangerouslySetInnerHTML={{ __html: html }} />
    </svg>
  );
}

/** A circuit drawn in the schematic language, rendered by the server as SVG. */
export function Schematic({ source, caption }: { source: string; caption?: string }) {
  const [state, setState] = useState<{ url?: string; error?: string }>({});
  const [heightView, setHeightView] = useState(false);
  // `#@` comment lines carry an optional height view; the server only needs the drawing.
  const drawing = useMemo(() => drawingOnly(source), [source]);
  const elevation = useMemo(() => parseElevation(source), [source]);
  const flow = useMemo(() => parseFlow(source), [source]);
  useEffect(() => {
    let live = true;
    const load = () =>
      schematicImage(drawing).then(
        (url) => live && setState({ url }),
        (error: Error) => live && setState({ error: error.message }),
      );
    // Debounced so a drawing that is still streaming into a chat reply is not rendered at every token;
    // drawings seen before (e.g. when returning to a note) appear at once.
    const timer = window.setTimeout(load, schematicSeen(drawing) ? 0 : 250);
    return () => {
      live = false;
      window.clearTimeout(timer);
    };
  }, [drawing]);

  if (state.error)
    return (
      <figure className="schematic broken">
        <pre>
          <code>{source}</code>
        </pre>
        <figcaption>Circuit could not be drawn: {state.error}</figcaption>
      </figure>
    );
  return (
    <figure className={`schematic ${elevation ? "has-elevation" : ""}`}>
      {elevation && state.url && <ElevationButton onClick={() => setHeightView(true)} />}
      {state.url && flow && typeof flow === "object" ? (
        <CurrentFlow url={state.url} spec={flow} alt={caption || "Circuit diagram"} />
      ) : state.url ? (
        <InlineSchematic drawing={drawing} alt={caption || "Circuit diagram"} fallback={state.url} />
      ) : (
        <div className="schematic-wait" />
      )}
      {typeof flow === "string" && <figcaption className="flow-error">Current flow: {flow}</figcaption>}
      {elevation?.inline && state.url && <ElevationInline spec={elevation} />}
      {caption && (
        <figcaption>
          <Markdown text={caption} inline />
        </figcaption>
      )}
      {heightView && elevation && <ElevationDialog spec={elevation} onClose={() => setHeightView(false)} />}
    </figure>
  );
}
