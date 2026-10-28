# Frontend

A minimal study workspace: course navigation on the left, the note or source you're reading in the middle, and a chat on the right. It is a React + TypeScript single-page app in `frontend/`, built with Vite into `src/open_lecture/web/` and served by `open-lecture serve` at `http://127.0.0.1:8000/`. All fonts and libraries are bundled; the UI makes no requests to third-party servers.

## Run and develop

```sh
cd frontend
npm install
npm run build          # writes src/open_lecture/web/, served by `uv run open-lecture serve`
npm run dev            # hot reload at http://localhost:5173, proxying /api to 127.0.0.1:8000
npm run typecheck
```

Set `OPENLECTURE_API` to point the dev proxy elsewhere. The dev proxy strips the browser `Origin` header so the backend's cross-origin guard accepts it.

### Visual checks

`npm run screenshot -- [scenarios.json] [outdir]` drives an installed Edge/Chrome through `playwright-core`, saves screenshots, and exits non-zero on console errors. `scripts/scenarios.json` covers both themes, the model picker, settings, search, the signed-out state (mocked), and mobile. Set `OPENLECTURE_URL` for a non-default server and `PW_CHANNEL` for the browser. Mocked scenarios never sign anything out.

## Every control

**Sidebar**

| Control | Action |
|---|---|
| Course switcher | Lists courses; checkmark on the current one. **New course** opens a code + title dialog. |
| AI activity | Appears while agents work ("Writing 2 notes, reading 1 source"). Opens a list of running and queued tasks with their current step and a **Stop** button for each. |
| Search (Ctrl/⌘ K) | Palette searching note titles and full-text source passages. Arrow keys + Enter; a passage opens its source at the matching page. |
| Overview | Course home: term, title, note/source counts, the **Weeks** list, starter questions. Each week shows its syllabus topics. Selecting a week opens its notes; a week without notes shows **Generate notes**, which has the model chosen in the chat box write them in the background (progress shows on the row). A week waits while its sources are still being read, and a failed attempt can be retried. |
| Study plan | Under Overview in every course: one Markdown note shared by all courses (`/courses/:id/plan`). The pencil edits it (Save, Cancel, Ctrl/⌘ S, Esc). Links to `/courses/…/docs/…#target` jump to that block: `target` is a block id or a label matching how a heading or problem title starts (`#b6`, `#problem-29`, `#topic-1`), so hand-written links survive a rebuild. |
| Notes list | Opens a note. A dot marks a note whose cited source has a newer version; `W4` shows the academic week. |
| Sources ↑ (upload) | File picker (PDF, DOCX, PPTX, MD, TXT, CSV, JSON, PNG, JPG, WEBP), then **Add source** with a kind (Lecture, Tutorial, Problems, Textbook, Lab, Syllabus, Reference, My notes) and an optional week, both guessed from the filename. Duplicate files are detected. |
| Sources list | Opens the viewer. `W3` shows the week, `Book` the textbook. A clock means AI reading is queued, a spinning icon that it is reading pages, a red dot that processing or reading failed. |
| Account button | Shows the active model or **Connect an AI**; opens Settings. |
| Theme button | Cycles system → light → dark. |
| Settings (gear) | Opens Settings. |

**Note reader toolbar**: breadcrumb back to the course; **Revision history** (every revision, author AI/you, time; choosing an old one shows a banner with **View latest**); **Ask about this note**; **More** → Copy link, **Regenerate Week N notes** (weekly notes only; deletes and rewrites the note in the background), Delete note (toast with **Undo**). Hovering a block shows an **Ask about this** button that quotes the block into the chat. Each section shows its sources once, as a pill line under its heading ("ELEC 221 Week 3 p. 3 4 6"); each page opens the source there, and **Back** returns to the same scroll position in the note. Heading levels have their own colors. Worked examples are cards with the statement, circuit diagram, numbered solution steps and an **Answer** box. Practice problems show their title and difficulty, hide the steps behind **Show solution**, and have an **Open** button ("Textbook, p. 163") that opens the page they come from. Circuits written in the schematic language (fenced `schematic` blocks in any text, or `schematic` blocks) render as diagrams, inverted for dark mode; a drawing that fails shows its source and the error. Interactive math tools are fenced blocks in any text (grammar in `src/open_lecture/skills/math-tools.md`): `steps` is an equation stepper (Back/Next or ←/→, the previous line faded above the current one, highlighted changes, a show-all list); `graph` is a 2-D plot with sliders (optionally animated), draggable points, slope fields, solution curves through a dragged point, level curves, shaded regions and live readouts; `graph3d` is a surface you turn by dragging, with a slider plane that marks the level curve. A tool that fails shows its source and the line at fault. A banner offers **Ask to update** when a cited source changed.

**Source viewer toolbar**: Back (when you arrived from a citation), page ◀ [n] of N ▶ (type a page and press Enter), zoom out / Fit / zoom in, **Dark pages** (dark theme only, inverts PDF pages), **Download original**, **Ask about this page**. Pages load lazily as you scroll; the chat's context chip follows the page you're on. DOCX, PPTX and text files show their extracted text with slide/page labels. If AI reading stopped early, a banner offers **Try again**.

**Chat panel**

| Control | Action |
|---|---|
| Chat title ▾ | Chat history for the course, **New chat**. |
| New chat (pen) | Starts an empty chat. |
| Close (Ctrl/⌘ J toggles) | Hides the panel; a toolbar button reopens it. Full-screen overlay on mobile. |
| Context chip | What you're viewing (note, source + page, or a quoted block) is sent as context. × excludes it, + re-includes it. |
| Model picker | Claude / Codex tabs (green dot = signed in). Model list (Default uses the CLI's own setting) and effort chips (Auto, Low … Max/Ultra as the model supports). **Sign in** if needed, **Manage accounts**. |
| Send / Stop | Enter sends, Shift+Enter adds a line. Stop cancels the run and kills the CLI process tree. |
| Activity rows | Live tool steps ("Searching course sources", "Calculating", …) while the agent works. |
| Copy | Copies an answer. |
| Error box | **Try again**, or **Sign in to …** when the failure is an auth problem. |

**Settings**: Appearance (System, Light, Dark); AI accounts (status, account and plan, CLI version, **Sign in**, **Sign out** with confirmation, **How to install** when a CLI is missing, **Check again**); Chat model (provider, model, effort; also used for weekly notes); Source reading model (default Codex GPT-6-Luna, High); About (version, API reference link).

**Model names**: Claude models are listed by exact version (Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5) because the CLI's short aliases can point at older generations. **Default** shows what the CLI would actually use. Codex models come from Codex's own list and are remembered, so they never disappear.

**Sign-in flow**: **Sign in** asks the backend to open the CLI's own login (`claude auth login` or `codex login`) in a new terminal window. Finish there in the browser; the UI polls status every 3 s for up to 3 minutes and confirms with a toast. If no terminal can be opened, Settings shows the command with a copy button. **Sign out** signs the CLI out on this computer, not just in Open Lecture, and the confirmation says so.

## Design system

- **Palette** (tokens in `src/styles.css`): cool neutral chrome `#f3f4f6`, white paper, ink `#15171c`, one blue-black ink accent `#2d4a8a`. Dark mode has its own steps (graphite `#181a1f`/`#1e2026`, accent `#9db4f0`), selected rather than inverted. Tip, warning and danger tones are reserved for callouts and errors.
- **Type**: Notion's system font stack (Segoe UI Variable on Windows, San Francisco on macOS) for interface and notes; KaTeX for math. Sentence case everywhere.
- **Signature**: the reading sheet, a 720 px column with typeset math, numbered derivation steps, and citation pills that jump to the PDF page. Everything around it stays quiet.
- **Theme**: System/Light/Dark stored in `localStorage` (`ol-theme`) and applied by an inline script before first paint, so there is no flash.
- **Accessibility**: visible focus rings, `prefers-reduced-motion` honored, hover-only actions stay visible on touch devices, 16 px inputs on mobile to prevent zoom, ARIA labels on icon buttons.
- **Responsive**: three columns above 900 px; below that the sidebar becomes a drawer and the chat a full-screen overlay.

## Code map

- `App.tsx`: routing (`/courses/:id`, `/courses/:id/docs/:doc?revision=n#block`, `/courses/:id/sources/:src?page=n`), data loading, live SSE refresh, sign-in polling, dialogs.
- `components/Views.tsx`: course home, note reader, source viewer, shared toolbar.
- `components/Blocks.tsx`, `ArtifactCard.tsx`, `Chart.tsx`, `Markdown.tsx`: document block renderers, computed-result cards and single-series SVG charts (hover tooltips), Markdown + KaTeX (raw HTML is never rendered).
- `components/Chat.tsx`, `ModelPicker.tsx`: chat, streaming run display, provider/model/effort picker.
- `components/Sidebar.tsx`, `Settings.tsx`, `Search.tsx`, `ui.tsx`: navigation, settings, search palette, popover/dialog/toast primitives.
- `api.ts`: typed API client, SSE run reader, citation resolver. `theme.ts`: theme and stored-state hooks.

Per-viewer preferences in `localStorage`: theme, selected course, model selection, chat panel open, last chat per course, PDF zoom, dark pages, last event sequence. Everything else lives in the backend.

## Study Schedule

The built-in **Study Schedule** is always the first entry in the course picker, separated from ordinary courses by a thin divider. It opens at `/study-schedule` and cannot be created through the New course form. It is a single workspace planner rather than a course with sources, generated notes, or chat.

The monthly calendar starts on Monday and shows Morning, Afternoon, and Evening for every day. Click a period to edit its study note, then choose **Save plan**. Clear a note and save to remove it. Plans persist in the workspace SQLite database. Course codes and unambiguous three-digit numbers become course hyperlinks, including aliases for shared courses such as ELEC 226/326.

Use the month arrows or **Today** to navigate. **Add exam** creates an all-day exam entry; the trash button beside an exam in the monthly summary removes it. The initial exams are ELEC 221 on October 27, ELEC 271 on October 29, and ELEC 226 and ELEC 231 on October 30, 2026. They are seeded once during migration. On narrow screens, the calendar scrolls horizontally.
