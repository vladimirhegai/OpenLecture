import { useEffect, useMemo, useState } from "react";
import { schematicImage, schematicSeen } from "../api";
import { drawingOnly, ElevationButton, ElevationDialog, ElevationInline, parseElevation } from "./Elevation";
import { Markdown } from "./Markdown";

/** A circuit drawn in the schematic language, rendered by the server as SVG. */
export function Schematic({ source, caption }: { source: string; caption?: string }) {
  const [state, setState] = useState<{ url?: string; error?: string }>({});
  const [heightView, setHeightView] = useState(false);
  // `#@` comment lines carry an optional height view; the server only needs the drawing.
  const drawing = useMemo(() => drawingOnly(source), [source]);
  const elevation = useMemo(() => parseElevation(source), [source]);
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
      {state.url ? <img src={state.url} alt={caption || "Circuit diagram"} /> : <div className="schematic-wait" />}
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
