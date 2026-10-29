import { useEffect, useState } from "react";
import { digitalImage } from "../api";
import { FigureZoom } from "./FigureZoom";

/** Server-validated digital-system drawings, shared by notes and chat Markdown. */
export function DigitalFigure({ source }: { source: string }) {
  const [state, setState] = useState<{ url?: string; error?: string }>({});
  const [zoomed, setZoomed] = useState(false);
  useEffect(() => {
    let live = true;
    setState({});
    const timer = window.setTimeout(() => {
      digitalImage(source).then(
        (url) => live && setState({ url }),
        (error: Error) => live && setState({ error: error.message }),
      );
    }, 150);
    return () => { live = false; window.clearTimeout(timer); };
  }, [source]);
  return (
    <figure className={`schematic digital-figure${state.error ? " broken" : ""}`}>
      {state.error ? <><pre><code>{source}</code></pre><figcaption>Figure could not be drawn: {state.error}</figcaption></>
        : state.url ? <img src={state.url} alt="Digital systems figure" className="zoomable" title="Click to zoom" onClick={() => setZoomed(true)} />
        : <div className="schematic-wait" />}
      {zoomed && state.url && <FigureZoom src={state.url} alt="Digital systems figure" onClose={() => setZoomed(false)} />}
    </figure>
  );
}
