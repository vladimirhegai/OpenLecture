import { useEffect, type RefObject } from "react";

/**
 * Remembers each history entry's scroll position, so Back returns to where the reader was
 * (e.g. after opening a citation's source page from deep inside a note).
 */
const saved = new Map<string, number>();
let counter = 0;

export function newEntry() {
  return { key: `${Date.now().toString(36)}-${counter++}` };
}

function currentKey(): string {
  const state = window.history.state as { key?: string } | null;
  if (state?.key) return state.key;
  const entry = newEntry();
  window.history.replaceState({ ...(state ?? {}), ...entry }, "");
  return entry.key;
}

/** The scroll position saved for the current history entry, if the reader has been here before. */
export function savedScroll(): number | undefined {
  return saved.get(currentKey());
}

/** Call before navigating away from the current entry. */
export function rememberScroll() {
  const element = document.querySelector<HTMLElement>("[data-scroll-memory]");
  if (element) saved.set(currentKey(), element.scrollTop);
}

/**
 * Restores the saved position once `ready` (content loaded). Content such as diagrams can still grow
 * after that, so it keeps re-applying for a moment until the reader scrolls themselves.
 */
export function useScrollMemory(ref: RefObject<HTMLElement | null>, ready: boolean) {
  useEffect(() => {
    const element = ref.current;
    const target = saved.get(currentKey());
    if (!ready || !element || !target) return;
    let frame = 0;
    const started = performance.now();
    const stop = () => cancelAnimationFrame(frame);
    const apply = () => {
      element.scrollTop = target;
      if (performance.now() - started < 1500 && Math.abs(element.scrollTop - target) > 1) frame = requestAnimationFrame(apply);
      else if (performance.now() - started < 400) frame = requestAnimationFrame(apply);
    };
    apply();
    const options = { passive: true, once: true } as const;
    element.addEventListener("wheel", stop, options);
    element.addEventListener("touchstart", stop, options);
    element.addEventListener("keydown", stop, options);
    return () => {
      stop();
      element.removeEventListener("wheel", stop);
      element.removeEventListener("touchstart", stop);
      element.removeEventListener("keydown", stop);
    };
  }, [ref, ready]);
}
