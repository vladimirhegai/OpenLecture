import { useEffect, useState } from "react";
import { ChevronRight, Pencil } from "lucide-react";
import { api, relativeTime, type Course } from "../api";
import { Markdown } from "./Markdown";
import { useToast } from "./ui";
import { Toolbar, type Route } from "./Views";

type Plan = { text: string; updated_at: string | null };

/** The one study plan (Markdown), shared by every course: links like /courses/…/docs/…#b6 jump straight to a section. */
export function StudyPlan({ course, onOpen }: { course: Course; onOpen: (route: Route) => void }) {
  const toast = useToast();
  const [plan, setPlan] = useState<Plan | null>(null);
  const [draft, setDraft] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  useEffect(() => {
    api<Plan>("/study-plan").then(setPlan, (e) => toast(e.message));
  }, [toast]);

  async function save() {
    if (draft === null) return;
    setBusy(true);
    try {
      setPlan(await api<Plan>("/study-plan", { method: "PUT", json: { text: draft } }));
      setDraft(null);
    } catch (e) {
      toast((e as Error).message);
    } finally {
      setBusy(false);
    }
  }

  return (
    <>
      <Toolbar
        crumbs={
          <>
            <button onClick={() => onOpen({ kind: "home" })}>{course.code}</button>
            <ChevronRight size={14} />
            <span className="here">Study plan</span>
          </>
        }
      >
        {plan && draft === null && (
          <button className="icon-btn" title="Edit plan" aria-label="Edit plan" onClick={() => setDraft(plan.text)}>
            <Pencil size={16} />
          </button>
        )}
      </Toolbar>
      <div className="scroll" data-scroll-memory>
        {plan ? (
          <article className="sheet study-plan">
            <h1 className="doc-title">Study plan</h1>
            <div className="doc-meta">
              <span>Shown in every course</span>
              {plan.updated_at && <span>Updated {relativeTime(plan.updated_at)}</span>}
            </div>
            {draft !== null ? (
              <div className="plan-editor">
                <textarea
                  value={draft}
                  disabled={busy}
                  autoFocus
                  aria-label="Study plan (Markdown)"
                  placeholder={"## Tonight\n- [B1 · Separable](/courses/…/docs/…#b1)"}
                  onChange={(event) => setDraft(event.target.value)}
                  onKeyDown={(event) => {
                    if ((event.ctrlKey || event.metaKey) && event.key === "s") {
                      event.preventDefault();
                      save();
                    }
                    if (event.key === "Escape") setDraft(null);
                  }}
                />
                <p className="plan-hint">Markdown. Link a section with its note’s address plus <code>#</code> and how its title starts, like <code>#b6</code> or <code>#problem-29</code>.</p>
                <div className="plan-actions">
                  <button className="btn quiet" disabled={busy} onClick={() => setDraft(null)}>Cancel</button>
                  <button className="btn primary" disabled={busy} onClick={save}>Save</button>
                </div>
              </div>
            ) : plan.text ? (
              <Markdown text={plan.text} />
            ) : (
              <div className="plan-empty">
                <p>Write what to study and when. Links to note sections take you straight there.</p>
                <button className="btn primary" onClick={() => setDraft("")}>Write a plan</button>
              </div>
            )}
          </article>
        ) : (
          <div className="empty">
            <div className="spinner" />
          </div>
        )}
      </div>
    </>
  );
}
