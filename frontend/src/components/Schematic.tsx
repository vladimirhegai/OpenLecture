import { useEffect, useState } from "react";
import { schematicImage, schematicSeen } from "../api";
import { Markdown } from "./Markdown";

/** A circuit drawn in the schematic language, rendered by the server as SVG. */
export function Schematic({ source, caption }: { source: string; caption?: string }) {
  const [state, setState] = useState<{ url?: string; error?: string }>({});
  useEffect(() => {
    let live = true;
    const load = () =>
      schematicImage(source.trim()).then(
        (url) => live && setState({ url }),
        (error: Error) => live && setState({ error: error.message }),
      );
    // Debounced so a drawing that is still streaming into a chat reply is not rendered at every token;
    // drawings seen before (e.g. when returning to a note) appear at once.
    const timer = window.setTimeout(load, schematicSeen(source.trim()) ? 0 : 250);
    return () => {
      live = false;
      window.clearTimeout(timer);
    };
  }, [source]);

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
    <figure className="schematic">
      {state.url ? <img src={state.url} alt={caption || "Circuit diagram"} /> : <div className="schematic-wait" />}
      {caption && <figcaption><Markdown text={caption} inline /></figcaption>}
    </figure>
  );
}
