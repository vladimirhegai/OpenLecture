import { useCallback, useEffect, useState } from "react";
import { CalendarDays, ChevronLeft, ChevronRight, Plus, Trash2 } from "lucide-react";
import { api, type Course } from "../api";
import { courseMentions, PERIODS, type Exam, type Period, type Schedule, type ScheduleSlot } from "../schedule";
import { Dialog, useToast } from "./ui";
import { Toolbar } from "./Views";

function dateKey(date: Date) {
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}`;
}
function dayLabel(day: string) {
  return new Date(`${day}T12:00:00`).toLocaleDateString(undefined, { weekday: "long", month: "long", day: "numeric", year: "numeric" });
}

function CourseText({ text, courses, onCourse }: { text: string; courses: Course[]; onCourse: (id: string) => void }) {
  return <>{courseMentions(text, courses).map((part, index) => part.course
    ? <a key={index} href={`/courses/${part.course.id}`} title={part.course.title} onClick={(event) => {
      if (event.button === 0 && !event.ctrlKey && !event.metaKey && !event.shiftKey && !event.altKey) {
        event.preventDefault();
        onCourse(part.course!.id);
      }
    }}>{part.text}</a>
    : <span key={index}>{part.text}</span>)}</>;
}

export function StudySchedule({ courses, onCourse }: { courses: Course[]; onCourse: (id: string) => void }) {
  const toast = useToast();
  const [month, setMonth] = useState(() => new Date(new Date().getFullYear(), new Date().getMonth(), 1));
  const [data, setData] = useState<Schedule | null>(null);
  const [error, setError] = useState("");
  const [editing, setEditing] = useState<{ day: string; period: Period } | null>(null);
  const [draft, setDraft] = useState("");
  const [examOpen, setExamOpen] = useState(false);
  const [examDay, setExamDay] = useState(dateKey(new Date()));
  const [examTitle, setExamTitle] = useState("");
  const [busy, setBusy] = useState(false);
  const load = useCallback(() => {
    setError("");
    api<Schedule>("/study-schedule").then(setData, (e) => setError(e.message));
  }, []);
  useEffect(load, [load]);
  const closeEditor = useCallback(() => {
    if (!busy) setEditing(null);
  }, [busy]);
  const closeExam = useCallback(() => {
    if (!busy) setExamOpen(false);
  }, [busy]);
  // Keep unsaved edits safe when closing or reloading the browser.
  const dirty = editing && draft !== (data?.slots.find((slot) => slot.day === editing.day && slot.period === editing.period)?.text ?? "");
  useEffect(() => {
    if (!dirty) return;
    const beforeUnload = (event: BeforeUnloadEvent) => { event.preventDefault(); event.returnValue = ""; };
    window.addEventListener("beforeunload", beforeUnload);
    return () => window.removeEventListener("beforeunload", beforeUnload);
  }, [dirty]);

  async function save() {
    if (!editing) return;
    setBusy(true);
    try {
      const slot = await api<ScheduleSlot>(`/study-schedule/days/${editing.day}/${editing.period}`, { method: "PUT", json: { text: draft } });
      setData((current) => current && ({ ...current, slots: [...current.slots.filter((s) => s.day !== slot.day || s.period !== slot.period), ...(slot.text ? [slot] : [])] }));
      setEditing(null);
      toast("Study plan saved");
    } catch (e) { toast(`Couldn't save your plan: ${(e as Error).message}`); }
    finally { setBusy(false); }
  }
  async function addExam(event: React.FormEvent) {
    event.preventDefault();
    setBusy(true);
    try {
      const exam = await api<Exam>("/study-schedule/exams", { method: "POST", json: { day: examDay, title: examTitle } });
      setData((current) => current && ({ ...current, exams: [...current.exams, exam] }));
      setExamOpen(false);
      setExamTitle("");
      setMonth(new Date(`${examDay.slice(0, 7)}-01T12:00:00`));
    } catch (e) { toast((e as Error).message); }
    finally { setBusy(false); }
  }
  async function removeExam(exam: Exam) {
    setBusy(true);
    try {
      await api(`/study-schedule/exams/${exam.id}`, { method: "DELETE" });
      setData((current) => current && ({ ...current, exams: current.exams.filter((item) => item.id !== exam.id) }));
    } catch (e) { toast((e as Error).message); }
    finally { setBusy(false); }
  }

  const start = new Date(month.getFullYear(), month.getMonth(), 1);
  start.setDate(start.getDate() - (start.getDay() + 6) % 7);
  const count = Math.ceil(((month.getDay() + 6) % 7 + new Date(month.getFullYear(), month.getMonth() + 1, 0).getDate()) / 7) * 7;
  const days = Array.from({ length: count }, (_, index) => new Date(start.getFullYear(), start.getMonth(), start.getDate() + index));
  const today = dateKey(new Date());
  const monthKey = dateKey(month).slice(0, 7);
  const monthExams = (data?.exams ?? []).filter((exam) => exam.day.startsWith(monthKey)).sort((a, b) => a.day.localeCompare(b.day) || a.title.localeCompare(b.title));

  return <>
    <Toolbar crumbs={<span className="here">Study Schedule</span>} />
    <div className="study-schedule">
      <div className="schedule-heading">
        <div><div className="schedule-eyebrow"><CalendarDays size={16} /> YOUR STUDY PLANNER</div><h1>Make time to understand.</h1><p>Plan each part of your day. Write 231 or ELEC 231 to link to a course.</p></div>
        <button className="btn" disabled={!data} onClick={() => { setExamDay(dateKey(new Date(month.getFullYear(), month.getMonth(), 1))); setExamOpen(true); }}><Plus size={15} /> Add exam</button>
      </div>
      {error ? <div role="alert" className="schedule-error">Couldn't load your schedule: {error} <button className="btn" onClick={load}>Retry</button></div> : !data ? <div className="empty">Loading your schedule…</div> : <>
        <section className="schedule-exams" aria-label="Exams this month">
          <strong>Exams this month</strong>
          {monthExams.length ? monthExams.map((exam) => <div key={exam.id} className="schedule-exam-summary"><time dateTime={exam.day}>{new Date(`${exam.day}T12:00:00`).toLocaleDateString(undefined, { month: "short", day: "numeric" })}</time><span><CourseText text={exam.title} courses={courses} onCourse={onCourse} /></span><button className="icon-btn" disabled={busy} title={`Remove ${exam.title}`} aria-label={`Remove ${exam.title}`} onClick={() => removeExam(exam)}><Trash2 size={13} /></button></div>) : <span className="schedule-muted">No exams added for this month.</span>}
        </section>
        <div className="schedule-month-nav">
          <h2>{month.toLocaleDateString(undefined, { month: "long", year: "numeric" })}</h2>
          <div><button className="btn" onClick={() => setMonth(new Date(new Date().getFullYear(), new Date().getMonth(), 1))}>Today</button><button className="icon-btn" aria-label="Previous month" onClick={() => setMonth(new Date(month.getFullYear(), month.getMonth() - 1, 1))}><ChevronLeft size={18} /></button><button className="icon-btn" aria-label="Next month" onClick={() => setMonth(new Date(month.getFullYear(), month.getMonth() + 1, 1))}><ChevronRight size={18} /></button></div>
        </div>
        <div className="schedule-calendar-scroll" tabIndex={0} role="region" aria-label="Study calendar; scroll horizontally on small screens">
          <div className="schedule-calendar">
            {["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].map((day) => <div className="schedule-weekday" key={day}>{day}</div>)}
            {days.map((day) => {
              const key = dateKey(day);
              return <section key={key} aria-label={dayLabel(key)} className={`schedule-day ${day.getMonth() !== month.getMonth() ? "outside" : ""} ${key === today ? "today" : ""}`}>
                <time dateTime={key} className="schedule-date">{day.getDate()}{key === today && <span>Today</span>}</time>
                {data.exams.filter((exam) => exam.day === key).map((exam) => <div className="schedule-exam" key={exam.id}><span className="schedule-exam-label">EXAM</span><CourseText text={exam.title} courses={courses} onCourse={onCourse} /></div>)}
                {PERIODS.map((period) => {
                  const text = data.slots.find((slot) => slot.day === key && slot.period === period)?.text ?? "";
                  const edit = () => { setEditing({ day: key, period }); setDraft(text); };
                  return <div className="schedule-slot" key={period}>
                    <button className="schedule-period" aria-label={`Edit ${key} ${period}`} onClick={edit}>{period}<Plus size={11} /></button>
                    {text ? <div className="schedule-plan"><CourseText text={text} courses={courses} onCourse={onCourse} /></div> : <button className="schedule-add-plan" onClick={edit} aria-label={`Plan ${key} ${period}`}>Add a plan</button>}
                  </div>;
                })}
              </section>;
            })}
          </div>
        </div>
      </>}
    </div>
    {editing && <Dialog title={`${editing.period} · ${dayLabel(editing.day)}`} onClose={closeEditor}>
      <form className="schedule-editor" onSubmit={(event) => { event.preventDefault(); save(); }}>
        <label htmlFor="study-plan">What will you study?</label>
        <textarea id="study-plan" rows={7} maxLength={10000} value={draft} disabled={busy} onChange={(event) => setDraft(event.target.value)} placeholder="Review 231 chain rule, then practise ELEC 221 circuits…" />
        <p>Course numbers become links after saving. Clear the text to remove this plan.</p>
        <div className="schedule-preview"><CourseText text={draft} courses={courses} onCourse={(id) => { if (!dirty) onCourse(id); else toast("Save your plan before opening a course"); }} /></div>
        <div className="schedule-editor-actions"><button type="button" className="btn" disabled={busy} onClick={closeEditor}>Cancel</button><button className="btn primary" disabled={busy}>{busy ? "Saving…" : "Save plan"}</button></div>
      </form>
    </Dialog>}
    {examOpen && <Dialog title="Add exam" onClose={closeExam}><form className="schedule-editor" onSubmit={addExam}>
      <label htmlFor="exam-day">Date</label><input id="exam-day" type="date" required value={examDay} onChange={(event) => setExamDay(event.target.value)} disabled={busy} />
      <label htmlFor="exam-title">Exam</label><input id="exam-title" required maxLength={200} value={examTitle} onChange={(event) => setExamTitle(event.target.value)} placeholder="ELEC 231 midterm" disabled={busy} />
      <p>Exams are shown as all-day entries.</p><div className="schedule-editor-actions"><button className="btn" type="button" disabled={busy} onClick={closeExam}>Cancel</button><button className="btn primary" disabled={busy || !examTitle.trim()}>{busy ? "Saving…" : "Add exam"}</button></div>
    </form></Dialog>}
  </>;
}
