import { useEffect, useState } from "react";

export type ThemePref = "system" | "light" | "dark";
const KEY = "ol-theme";
const media = () => window.matchMedia("(prefers-color-scheme: dark)");

export function readThemePref(): ThemePref {
  try {
    const value = localStorage.getItem(KEY);
    if (value === "light" || value === "dark") return value;
  } catch {
    /* storage unavailable */
  }
  return "system";
}

function apply(pref: ThemePref) {
  const dark = pref === "dark" || (pref === "system" && media().matches);
  document.documentElement.dataset.theme = dark ? "dark" : "light";
}

export function useTheme() {
  const [pref, setPref] = useState<ThemePref>(readThemePref);
  const [resolved, setResolved] = useState(() => document.documentElement.dataset.theme ?? "light");

  useEffect(() => {
    apply(pref);
    setResolved(document.documentElement.dataset.theme ?? "light");
    try {
      localStorage.setItem(KEY, pref);
    } catch {
      /* storage unavailable */
    }
    if (pref !== "system") return;
    const query = media();
    const listener = () => {
      apply("system");
      setResolved(document.documentElement.dataset.theme ?? "light");
    };
    query.addEventListener("change", listener);
    return () => query.removeEventListener("change", listener);
  }, [pref]);

  return { pref, setPref, dark: resolved === "dark" };
}

export function useStored<T>(key: string, initial: T) {
  const [value, setValue] = useState<T>(() => {
    try {
      const raw = localStorage.getItem(key);
      return raw === null ? initial : (JSON.parse(raw) as T);
    } catch {
      return initial;
    }
  });
  useEffect(() => {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch {
      /* storage unavailable */
    }
  }, [key, value]);
  return [value, setValue] as const;
}
