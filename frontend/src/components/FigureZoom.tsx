import { Minus, Plus, X } from "lucide-react";
import { useEffect, useLayoutEffect, useRef, useState } from "react";
import { createPortal } from "react-dom";

/** A full-screen viewer for one drawing: fits the screen, then zoom (buttons, Ctrl+wheel, +/-) and drag to pan. */
export function FigureZoom({ src, alt, onClose }: { src: string; alt: string; onClose: () => void }) {
  const box = useRef<HTMLDivElement>(null);
  const [ratio, setRatio] = useState<number>();
  const [scale, setScale] = useState(1);
  const drag = useRef<{ x: number; y: number; left: number; top: number } | undefined>(undefined);
  const fit = () => {
    if (!ratio) return 0;
    return Math.min(window.innerWidth * 0.94, (window.innerHeight - 90) * ratio);
  };
  const zoom = (factor: number) => {
    const el = box.current;
    if (!el) return;
    // keep the point in the middle of the screen where it is
    const cx = (el.scrollLeft + el.clientWidth / 2) / el.scrollWidth;
    const cy = (el.scrollTop + el.clientHeight / 2) / el.scrollHeight;
    setScale((s) => {
      const next = Math.min(6, Math.max(0.5, s * factor));
      requestAnimationFrame(() => {
        el.scrollLeft = cx * el.scrollWidth - el.clientWidth / 2;
        el.scrollTop = cy * el.scrollHeight - el.clientHeight / 2;
      });
      return next;
    });
  };
  useEffect(() => {
    const key = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
      else if (e.key === "+" || e.key === "=") zoom(1.25);
      else if (e.key === "-") zoom(0.8);
      else if (e.key === "0") setScale(1);
    };
    document.addEventListener("keydown", key);
    const overflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      document.removeEventListener("keydown", key);
      document.body.style.overflow = overflow;
    };
  });
  useLayoutEffect(() => {
    const el = box.current;
    if (!el) return;
    const wheel = (e: WheelEvent) => {
      if (!e.ctrlKey && !e.metaKey) return;
      e.preventDefault();
      zoom(e.deltaY < 0 ? 1.15 : 1 / 1.15);
    };
    el.addEventListener("wheel", wheel, { passive: false });
    return () => el.removeEventListener("wheel", wheel);
  });
  return createPortal(
    <div className="zoom-scrim" role="dialog" aria-modal="true" aria-label={alt}>
      <div className="zoom-bar">
        <button className="icon-btn" onClick={() => zoom(0.8)} aria-label="Zoom out" title="Zoom out (−)">
          <Minus size={16} />
        </button>
        <button className="btn quiet zoom-pct" onClick={() => setScale(1)} title="Fit to screen (0)">
          {scale === 1 ? "Fit" : `${Math.round(scale * 100)}%`}
        </button>
        <button className="icon-btn" onClick={() => zoom(1.25)} aria-label="Zoom in" title="Zoom in (+)">
          <Plus size={16} />
        </button>
        <span className="zoom-hint">Ctrl + scroll to zoom · drag to move</span>
        <button className="icon-btn" onClick={onClose} aria-label="Close" title="Close (Esc)">
          <X size={16} />
        </button>
      </div>
      <div
        ref={box}
        className={`zoom-box ${scale > 1 ? "can-drag" : ""}`}
        onPointerDown={(e) => {
          if (e.target === e.currentTarget && scale <= 1) return onClose();
          const el = box.current!;
          drag.current = { x: e.clientX, y: e.clientY, left: el.scrollLeft, top: el.scrollTop };
          el.setPointerCapture(e.pointerId);
        }}
        onPointerMove={(e) => {
          const d = drag.current;
          if (!d) return;
          box.current!.scrollLeft = d.left - (e.clientX - d.x);
          box.current!.scrollTop = d.top - (e.clientY - d.y);
        }}
        onPointerUp={() => (drag.current = undefined)}
      >
        <img
          src={src}
          alt={alt}
          className="zoom-img"
          draggable={false}
          onLoad={(e) => setRatio(e.currentTarget.naturalWidth / e.currentTarget.naturalHeight)}
          style={ratio ? { width: fit() * scale } : { visibility: "hidden" }}
        />
      </div>
    </div>,
    document.body,
  );
}
