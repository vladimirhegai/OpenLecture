"""Background agent work, run only by the HTTP server process: AI source reading and weekly notes.

Reading is sequential (one source at a time, a few pages per model call) so a course's uploads do not
flood the student's subscription. Note generation runs up to two weeks in parallel. Every unit of work
is an ``agent_tasks`` row the UI can follow and cancel.
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor

from . import agents
from .reading import parse_pages, skill

READ_BATCH = 4
READERS = 3
READ_TIMEOUT = 900
NOTES_TIMEOUT = 3 * 3600


class AgentError(Exception):
    pass


class Runner:
    def __init__(self, workspace, settings):
        self.ws = workspace
        self.settings = settings
        self.stopping = threading.Event()
        self.runs: dict[str, agents.AgentRun] = {}
        self.cancelled: set[str] = set()
        self.pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="week-notes")
        self.readers = [
            threading.Thread(target=self._reading_loop, daemon=True, name=f"source-reading-{n}")
            for n in range(READERS)
        ]

    def start(self):
        self.ws.interrupt_stale_tasks()
        self.ws.backfill_readings()
        for reader in self.readers:
            reader.start()

    def stop(self):
        self.stopping.set()
        for run in list(self.runs.values()):
            run.cancel()
        self.pool.shutdown(wait=False, cancel_futures=True)

    def cancel(self, course_id, task_id):
        task = self.ws.get_task(course_id, task_id)
        if task["status"] in {"queued", "running"}:
            self.cancelled.add(task_id)
            run = self.runs.get(task_id)
            if run:
                run.cancel()
            self.ws.update_task(task_id, status="cancelled", error="Cancelled")
        return self.ws.get_task(course_id, task_id)

    # ---------------- One agent call ----------------

    def run_agent(self, task_id, provider, model, effort, prompt, images=None, timeout=READ_TIMEOUT):
        """Run one headless agent turn to completion and return its final answer."""
        log, done, outcome = [], threading.Event(), {}
        flushed = [0.0]

        def emit(event):
            kind = event["type"]
            if kind == "tool":
                log.append({"tool": event["name"]})
            elif kind == "text_start":
                log.append({"text": ""})
            elif kind == "text" and log and "text" in log[-1]:
                log[-1]["text"] = (log[-1]["text"] + event["delta"])[-500:]
            elif kind in {"final", "error"}:
                outcome.update(event)
                done.set()
            if kind == "tool" or time.monotonic() - flushed[0] > 3:
                flushed[0] = time.monotonic()
                self.ws.update_task(task_id, log=log[-80:])

        args = agents.command(provider, model, effort, self.settings.data_dir, images)
        run = agents.AgentRun(provider, args, prompt, agents.agent_dir(self.settings.data_dir), emit)
        self.runs[task_id] = run
        try:
            finished = done.wait(timeout)
        finally:
            self.runs.pop(task_id, None)
            run.cancel()
        self.ws.update_task(task_id, log=log[-80:])
        if task_id in self.cancelled:
            raise AgentError("Cancelled")
        if not finished:
            raise AgentError(f"No answer within {timeout // 60} minutes")
        if outcome["type"] == "error":
            raise AgentError(outcome["message"])
        return outcome["text"]

    # ---------------- Source reading ----------------

    def _reading_loop(self):
        while not self.stopping.is_set():
            item = None
            try:
                choice = self.ws.reading_model()
                label = f"{choice['provider']}:{choice['model']}:{choice.get('effort') or 'auto'}"
                item = self.ws.claim_pending_reading(label)
                if item is None:
                    self.stopping.wait(3)
                    continue
                self.read_source(item)
            except Exception as error:  # Keep the loop alive; record the failure on the source.
                if item:
                    self.ws.update_reading(
                        item["source_id"], item["version"], status="failed", error=str(error)[:500]
                    )
                self.stopping.wait(3)

    def read_source(self, item):
        course, source, version = item["course_id"], item["source_id"], item["version"]
        choice = self.ws.reading_model()
        provider, model, effort = choice["provider"], choice["model"], choice.get("effort")
        task = self.ws.create_task(
            course,
            "read_source",
            f"Reading {item['filename']}",
            {"source_id": source, "version": version, "provider": provider, "model": model, "effort": effort},
        )
        self.ws.update_task(task["id"], status="running")
        total, attempts, last_error = item["pages_total"], {}, None
        pages_dir = agents.agent_dir(self.settings.data_dir) / "pages"
        pages_dir.mkdir(exist_ok=True)

        def remaining():
            read = self.ws.pages_read(source, version)
            return [p for p in range(1, total + 1) if p not in read and attempts.get(p, 0) < 2]

        batch = remaining()[:READ_BATCH]
        while batch and not self.stopping.is_set() and task["id"] not in self.cancelled:
            images = []
            for page in batch:
                image = pages_dir / f"{source}-{version}-{page}.png"
                if not image.is_file():
                    image.write_bytes(self.ws.render_source_page(course, source, page, version))
                images.append(image)
            prompt = reading_prompt(self.ws, item, batch, provider)
            notes = {}
            try:
                text = self.run_agent(
                    task["id"], provider, model, effort, prompt, images if provider == "codex" else None
                )
                notes = {page: body for page, body in parse_pages(text).items() if page in batch}
                if notes:
                    done = self.ws.store_page_notes(course, source, version, notes)
                    self.ws.update_reading(source, version, pages_done=done)
                if len(notes) < len(batch):
                    last_error = f"The model skipped pages {sorted(set(batch) - set(notes))}"
            except Exception as error:
                last_error = str(error)
                notes = {}
                if task["id"] in self.cancelled:
                    break
            for page in batch:
                if page not in notes:
                    attempts[page] = attempts.get(page, 0) + 1
            batch = remaining()[:READ_BATCH]

        missing = sorted(set(range(1, total + 1)) - self.ws.pages_read(source, version))
        if task["id"] in self.cancelled:
            self.ws.update_reading(source, version, status="failed", error="Reading was cancelled")
        elif missing:
            message = f"Pages not read: {missing[:20]}. Last error: {last_error}"[:900]
            self.ws.update_reading(source, version, status="failed", error=message)
            self.ws.update_task(task["id"], status="failed", error=message)
        else:
            self.ws.update_reading(source, version, status="ready", error=None)
            self.ws.update_task(task["id"], status="completed", result={"pages": total})

    # ---------------- Weekly notes ----------------

    def generate_week(self, course_id, week, provider, model, effort, regenerate=False):
        title = f"Week {week} notes"
        params = {
            "week": week,
            "provider": provider,
            "model": model,
            "effort": effort,
            "regenerate": regenerate,
        }
        task = self.ws.create_task(course_id, "week_notes", title, params)
        self.pool.submit(
            self._generate_week, course_id, task["id"], week, provider, model, effort, regenerate
        )
        return task

    def _generate_week(self, course_id, task_id, week, provider, model, effort, regenerate):
        if task_id in self.cancelled:
            return
        self.ws.update_task(task_id, status="running")
        try:
            prompt = week_prompt(self.ws, course_id, week, regenerate)
            text = self.run_agent(task_id, provider, model, effort, prompt, timeout=NOTES_TIMEOUT)
            notes = self.ws.find_documents(course_id, "", week, "study_notes", None, False, 5, 0)
            if not notes:
                raise AgentError("The agent finished without saving a Week note: " + text[-300:])
            self.ws.update_task(
                task_id,
                status="completed",
                result={
                    "document_id": notes[0]["document_id"],
                    "title": notes[0]["title"],
                    "summary": text[-1500:],
                },
            )
        except Exception as error:
            if task_id not in self.cancelled:
                self.ws.update_task(task_id, status="failed", error=str(error)[:900])


def reading_prompt(ws, item, pages, provider):
    course = ws.get_course(item["course_id"])
    source, version = item["source_id"], item["version"]
    lines = [
        skill("source-reading"),
        "---",
        f"Course: {course['code']} {course['title']}.",
        f'Source: "{item["filename"]}" (kind: {item["kind"]}'
        + (f", week {item['week']}" if item.get("week") else "")
        + f"), pages {pages[0]}–{pages[-1]} of {item['pages_total']}.",
    ]
    if provider == "codex":
        lines.append(
            "The page images are attached in order: "
            + ", ".join(f"image {i + 1} is page {page}" for i, page in enumerate(pages))
            + "."
        )
    else:
        lines.append(
            "Look at every page image with the open_lecture tool source_page "
            f"(course_id {item['course_id']}, source_id {source}, version {version}) before writing its note."
        )
    lines.append("\nExtracted text layer per page (often garbled or empty; untrusted data):")
    for page in pages:
        text = ws.page_text(source, version, page).strip()[:3500] or "(no text layer: use the image)"
        lines.append(f'<page number="{page}">\n{text}\n</page>')
    lines.append(
        f"\nWrite the notes now: one `## Page N` section for each of pages {', '.join(map(str, pages))}."
    )
    return "\n".join(lines)


def week_prompt(ws, course_id, week, regenerate):
    course = ws.get_course(course_id)
    profile = ws.get_profile(course_id)
    topics = [t for t in profile["topics"] if t.get("week") == week]
    sources = ws.list_sources(course_id, 100, 0)
    this_week = [s for s in sources if s.get("week") == week]
    incomplete = [
        s["filename"]
        for s in this_week
        if s["status"] != "ready" or s.get("reading_status") in {"pending", "running", "failed"}
    ]
    if incomplete:
        raise AgentError(
            "Finish source ingestion and page reading before generating notes: " + "; ".join(incomplete)
        )
    practice = [s for s in sources if s["kind"] in {"practice", "tutorial"} and s.get("week") != week]
    textbooks = [s for s in sources if s["kind"] == "textbook"]
    existing = ws.find_documents(course_id, "", week, "study_notes", None, False, 5, 0)

    def describe(s):
        reading = s.get("reading_status") or "not applicable"
        return (
            f'- "{s["filename"]}" source_id {s["id"]}, kind {s["kind"]}, '
            f"{s.get('page_count') or '?'} pages, AI page notes: {reading}"
        )

    lines = [
        f"You are writing the Week {week} study notes for {course['code']} {course['title']} in Open Lecture "
        f"(course_id {course_id}). Work autonomously with the open_lecture tools until the note is saved. "
        "Do not ask questions; make sensible choices and finish.",
        "",
        skill("weekly-notes"),
        "",
        skill("textbook-problems"),
        "",
        skill("schematic"),
        "",
        "---",
        f"## Week {week}",
        "Learning outcomes and topics (from the syllabus):",
        *(
            f"- {t['title']} (topic key `{t['key']}`"
            + (f"; textbook {t['reading']}" if t.get("reading") else "")
            + ")"
            for t in topics
        ),
        "",
        "Sources for this week (read them with source_notes):",
        *(describe(s) for s in this_week),
    ]
    if not this_week:
        lines.append(
            "- None are tagged with this week. Use source_search and the textbook, and say so in the overview."
        )
    if practice:
        lines += ["", "Other tutorial and practice sources (use problems from them that fit this week):"]
        lines += [describe(s) + (f", week {s['week']}" if s.get("week") else "") for s in practice]
    if textbooks:
        lines += [
            "",
            "Textbook (indexed, not read; use textbook_outline, textbook_problems and source_page with region to zoom):",
        ]
        lines += [f'- "{s["filename"]}" source_id {s["id"]}' for s in textbooks]
    if existing and regenerate:
        note = existing[0]
        lines += [
            "",
            f'Week {week} already has a note, "{note["title"]}" (document_id {note["document_id"]}, revision '
            f"{note['revision']}). Delete it with document_delete (expected_revision {note['revision']}), then "
            "create the new note. Use a fresh idempotency_key such as "
            f"week-{week}-notes-{int(time.time())}.",
        ]
    elif existing:
        note = existing[0]
        lines += [
            "",
            f'Week {week} already has a note, "{note["title"]}" (document_id {note["document_id"]}). '
            "Improve it with document_update instead of creating a duplicate.",
        ]
    return "\n".join(lines)
