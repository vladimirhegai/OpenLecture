import asyncio
import hmac
import json
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Annotated
from uuid import UUID

from fastapi import FastAPI, File, Form, Header, Query, Request, UploadFile
from fastapi import Path as PathParam
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles

from . import __version__, agents, circuits, digital, schematic
from .config import Settings
from .errors import DomainError
from .math_engine import binomial, calculate
from .profiles import list_packs
from .reading import list_skills, skill
from .runner import Runner
from .schemas import (
    ActionRequest,
    AgentRunRequest,
    BinomialRequest,
    ChatCreate,
    CircuitRequest,
    ContextRequest,
    CourseCreate,
    CourseProfileUpdate,
    DigitalRequest,
    DistributionRequest,
    DocumentCreate,
    DocumentEdit,
    FolderCreate,
    LinearODERequest,
    LogicRequest,
    MathRequest,
    MessageCreate,
    ReadRequest,
    RevisionRequest,
    SchematicRequest,
    SettingsUpdate,
    ViewerState,
    WeekGenerate,
)
from .study_tools import distribution, linear_ode, truth_table
from .workspace import Workspace

Limit = Annotated[int, Query(ge=1, le=100)]
Offset = Annotated[int, Query(ge=0)]


def create_app(settings: Settings | None = None):
    settings = settings or Settings()

    @asynccontextmanager
    async def lifespan(app):
        app.state.workspace = Workspace(settings)
        app.state.runs = {}
        app.state.runner = Runner(app.state.workspace, settings) if settings.agent_runner else None
        if app.state.runner:
            app.state.runner.start()
        yield
        if app.state.runner:
            app.state.runner.stop()
        for run in list(app.state.runs.values()):
            run.cancel()
        app.state.workspace.close()

    app = FastAPI(
        title="Open Lecture",
        version=__version__,
        lifespan=lifespan,
        description="Local-first study workspace. Persistent documents and agent-friendly tools.",
    )

    @app.middleware("http")
    async def local_access(request: Request, call_next):
        if settings.api_token:
            supplied = request.headers.get("authorization", "")
            if not hmac.compare_digest(supplied.encode(), f"Bearer {settings.api_token}".encode()):
                return JSONResponse(
                    {"error": {"code": "unauthorized", "message": "Bearer token required"}}, 401
                )
        # Browser requests from unrelated origins may not mutate a local workspace.
        origin = request.headers.get("origin")
        expected_origin = f"{request.url.scheme}://{request.headers.get('host', '')}"
        if origin and origin != expected_origin:
            return JSONResponse(
                {"error": {"code": "origin_denied", "message": "Cross-origin access is disabled"}}, 403
            )
        if not settings.api_token and request.url.hostname not in {
            "127.0.0.1",
            "localhost",
            "::1",
            "testserver",
        }:
            return JSONResponse({"error": {"code": "host_denied", "message": "Local hostname required"}}, 403)
        return await call_next(request)

    @app.exception_handler(DomainError)
    async def domain_error(request, error):
        return JSONResponse(
            {"error": {"code": error.code, "message": error.message, "details": error.details}}, error.status
        )

    @app.exception_handler(RequestValidationError)
    async def validation_error(request, error):
        issues = [
            {"location": list(item["loc"]), "message": item["msg"], "type": item["type"]}
            for item in error.errors()
        ]
        return JSONResponse(
            {"error": {"code": "validation_error", "message": "Invalid request", "details": issues}}, 422
        )

    def ws() -> Workspace:
        return app.state.workspace

    @app.get("/api/v1/health")
    def health():
        return {
            "status": "ok",
            "version": __version__,
            "agent_runtime": "local_cli_bridge_and_mcp",
            "circuit_engine": "resistive_dc",
            "storage": "sqlite",
        }

    @app.post("/api/v1/courses", status_code=201)
    def create_course(data: CourseCreate):
        return ws().create_course(data)

    @app.get("/api/v1/courses")
    def courses(limit: Limit = 50, offset: Offset = 0):
        return ws().list_courses(limit, offset)

    @app.get("/api/v1/courses/{course_id}")
    def get_course(course_id: UUID):
        return ws().get_course(str(course_id))

    @app.get("/api/v1/course-packs")
    def course_packs():
        return list_packs()

    @app.get("/api/v1/courses/{course_id}/profile")
    def course_profile(course_id: UUID):
        return ws().get_profile(str(course_id))

    @app.put("/api/v1/courses/{course_id}/profile")
    def update_profile(course_id: UUID, data: CourseProfileUpdate):
        return ws().update_profile(str(course_id), data)

    @app.get("/api/v1/courses/{course_id}/study-guidance")
    def study_guidance(course_id: UUID):
        return ws().study_guidance(str(course_id))

    @app.post("/api/v1/courses/{course_id}/folders", status_code=201)
    def create_folder(course_id: UUID, data: FolderCreate):
        return ws().create_folder(str(course_id), data)

    @app.get("/api/v1/courses/{course_id}/folders")
    def folders(course_id: UUID, limit: Limit = 100, offset: Offset = 0):
        return ws().list_folders(str(course_id), limit, offset)

    @app.post("/api/v1/courses/{course_id}/documents", status_code=201)
    def create_document(course_id: UUID, data: DocumentCreate):
        return ws().create_document(str(course_id), data)

    @app.get("/api/v1/courses/{course_id}/documents")
    def documents(
        course_id: UUID,
        query: str = Query(default="", max_length=300),
        academic_week: int | None = Query(default=None, ge=1, le=60),
        document_type: str | None = None,
        topic: str | None = None,
        include_deleted: bool = False,
        limit: Limit = 50,
        offset: Offset = 0,
    ):
        return ws().find_documents(
            str(course_id), query, academic_week, document_type, topic, include_deleted, limit, offset
        )

    @app.post("/api/v1/courses/{course_id}/document-actions/plan")
    def plan(course_id: UUID, data: ActionRequest):
        return ws().plan_document_action(str(course_id), data)

    @app.get("/api/v1/courses/{course_id}/documents/{document_id}")
    def read_document(course_id: UUID, document_id: UUID, revision: int | None = Query(default=None, ge=1)):
        return ws().read_document(str(course_id), str(document_id), revision)

    @app.patch("/api/v1/courses/{course_id}/documents/{document_id}")
    def edit_document(course_id: UUID, document_id: UUID, data: DocumentEdit):
        return ws().edit_document(str(course_id), str(document_id), data)

    @app.post("/api/v1/courses/{course_id}/documents/{document_id}/delete")
    def delete_document(course_id: UUID, document_id: UUID, data: RevisionRequest):
        return ws().set_document_deleted(str(course_id), str(document_id), data, True)

    @app.post("/api/v1/courses/{course_id}/documents/{document_id}/restore")
    def restore_document(course_id: UUID, document_id: UUID, data: RevisionRequest):
        return ws().set_document_deleted(str(course_id), str(document_id), data, False)

    @app.get("/api/v1/courses/{course_id}/documents/{document_id}/revisions")
    def revisions(course_id: UUID, document_id: UUID, limit: Limit = 50, offset: Offset = 0):
        return ws().list_revisions(str(course_id), str(document_id), limit, offset)

    @app.post("/api/v1/courses/{course_id}/sources", status_code=202)
    async def upload(
        course_id: UUID,
        file: Annotated[UploadFile, File()],
        kind: Annotated[str, Form()] = "lecture",
        source_id: Annotated[UUID | None, Form()] = None,
        week: Annotated[int | None, Form(ge=1, le=60)] = None,
    ):
        try:
            content = await file.read(settings.max_upload_bytes + 1)
            return await asyncio.to_thread(
                ws().upload_source,
                str(course_id),
                file.filename,
                content,
                kind,
                str(source_id) if source_id else None,
                week,
            )
        finally:
            await file.close()

    @app.get("/api/v1/courses/{course_id}/sources")
    def sources(course_id: UUID, limit: Limit = 50, offset: Offset = 0):
        return ws().list_sources(str(course_id), limit, offset)

    @app.get("/api/v1/courses/{course_id}/sources/{source_id}")
    def read_source(
        course_id: UUID,
        source_id: UUID,
        version: int | None = Query(default=None, ge=1),
        limit: Limit = 50,
        offset: Offset = 0,
    ):
        return ws().read_source(str(course_id), str(source_id), version, limit, offset)

    @app.get("/api/v1/courses/{course_id}/sources/{source_id}/original")
    def original(course_id: UUID, source_id: UUID, version: int | None = Query(default=None, ge=1)):
        path, filename = ws().source_file(str(course_id), str(source_id), version)
        return FileResponse(path, filename=filename, media_type="application/octet-stream")

    @app.get("/api/v1/courses/{course_id}/sources/{source_id}/pages/{page}")
    def source_page(
        course_id: UUID,
        source_id: UUID,
        page: int,
        version: int | None = Query(default=None, ge=1),
        size: int = Query(default=1400, ge=300, le=2400),
        region: str | None = Query(default=None, pattern=r"^[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+$"),
    ):
        box = [float(v) for v in region.split(",")] if region else None
        png = ws().render_source_page(str(course_id), str(source_id), page, version, size, box)
        return Response(png, media_type="image/png")

    @app.get("/api/v1/courses/{course_id}/search")
    def search(course_id: UUID, query: str = Query(min_length=1, max_length=2000), limit: Limit = 10):
        return ws().search_sources(str(course_id), query, limit)

    @app.get("/api/v1/courses/{course_id}/jobs/{job_id}")
    def job(course_id: UUID, job_id: UUID):
        return ws().get_job(str(course_id), str(job_id))

    @app.post("/api/v1/courses/{course_id}/jobs/{job_id}/retry")
    def retry_job(course_id: UUID, job_id: UUID):
        return ws().retry_job(str(course_id), str(job_id))

    @app.post("/api/v1/courses/{course_id}/chats", status_code=201)
    def create_chat(course_id: UUID, data: ChatCreate):
        return ws().create_chat(str(course_id), data)

    @app.get("/api/v1/courses/{course_id}/chats")
    def chats(course_id: UUID, limit: Limit = 50, offset: Offset = 0):
        return ws().list_chats(str(course_id), limit, offset)

    @app.post("/api/v1/courses/{course_id}/chats/{chat_id}/messages", status_code=201)
    def message(course_id: UUID, chat_id: UUID, data: MessageCreate):
        return ws().add_message(str(course_id), str(chat_id), data)

    @app.get("/api/v1/courses/{course_id}/chats/{chat_id}/messages")
    def messages(course_id: UUID, chat_id: UUID, after: Offset = 0, limit: Limit = 50):
        return ws().list_messages(str(course_id), str(chat_id), after, limit)

    @app.put("/api/v1/courses/{course_id}/chats/{chat_id}/viewer-state")
    def viewer(course_id: UUID, chat_id: UUID, data: ViewerState):
        return ws().set_viewer_state(str(course_id), str(chat_id), data)

    @app.post("/api/v1/courses/{course_id}/chats/{chat_id}/context")
    def context(course_id: UUID, chat_id: UUID, data: ContextRequest):
        return ws().assemble_context(str(course_id), str(chat_id), data)

    @app.get("/api/v1/courses/{course_id}/chats/{chat_id}/context")
    def inspect_context(course_id: UUID, chat_id: UUID):
        return ws().inspect_context(str(course_id), str(chat_id))

    @app.post("/api/v1/schematics/render")
    def render_schematic(data: SchematicRequest):
        svg = schematic.render_svg(data.source)
        return Response(svg, media_type="image/svg+xml", headers={"Cache-Control": "private, max-age=86400"})

    @app.post("/api/v1/schematics/check")
    def check_schematic(data: SchematicRequest):
        return schematic.topology(data.source)

    @app.post("/api/v1/digital/render")
    def render_digital(data: DigitalRequest):
        svg = digital.render_svg(data.source)
        return Response(svg, media_type="image/svg+xml", headers={"Cache-Control": "private, max-age=86400"})

    @app.post("/api/v1/digital/check")
    def check_digital(data: DigitalRequest):
        return digital.check(data.source)

    @app.post("/api/v1/math/evaluate")
    def math_evaluate(data: MathRequest):
        return calculate(data)

    @app.post("/api/v1/math/binomial")
    def math_binomial(data: BinomialRequest):
        return binomial(data)

    @app.post("/api/v1/math/distribution")
    def probability_distribution(data: DistributionRequest):
        return distribution(data)

    @app.post("/api/v1/math/linear-ode")
    def math_linear_ode(data: LinearODERequest):
        return linear_ode(data)

    @app.post("/api/v1/logic/truth-table")
    def logic_truth_table(data: LogicRequest):
        return truth_table(data)

    @app.post("/api/v1/courses/{course_id}/math-cards/distribution", status_code=201)
    def save_distribution(course_id: UUID, data: DistributionRequest):
        return ws().save_artifact(
            str(course_id), "math_card", data.distribution.title() + " distribution", distribution(data)
        )

    @app.post("/api/v1/courses/{course_id}/math-cards/linear-ode", status_code=201)
    def save_ode(course_id: UUID, data: LinearODERequest):
        return ws().save_artifact(str(course_id), "math_card", "Linear ODE exploration", linear_ode(data))

    @app.post("/api/v1/courses/{course_id}/logic-cards", status_code=201)
    def save_logic(course_id: UUID, data: LogicRequest):
        return ws().save_artifact(str(course_id), "logic_card", "Truth table", truth_table(data))

    @app.post("/api/v1/courses/{course_id}/math-cards/binomial", status_code=201)
    def save_binomial(course_id: UUID, data: BinomialRequest):
        return ws().save_artifact(str(course_id), "math_card", "Binomial distribution", binomial(data))

    @app.post("/api/v1/circuits/validate")
    def validate_circuit(data: CircuitRequest):
        circuit = circuits.parse(data.definition)
        return {"circuit": circuit, "spice_netlist": circuits.compile_spice(circuit)}

    @app.post("/api/v1/courses/{course_id}/circuits", status_code=201)
    def create_circuit(course_id: UUID, data: CircuitRequest):
        circuit = circuits.parse(data.definition)
        return ws().save_artifact(
            str(course_id),
            "circuit",
            circuit["title"],
            {
                "definition": data.definition,
                "circuit": circuit,
                "spice_netlist": circuits.compile_spice(circuit),
            },
        )

    @app.post("/api/v1/courses/{course_id}/circuits/{artifact_id}/simulate", status_code=201)
    def simulate(course_id: UUID, artifact_id: UUID):
        return simulate_artifact(ws(), str(course_id), str(artifact_id))

    @app.get("/api/v1/courses/{course_id}/artifacts")
    def artifacts(course_id: UUID, limit: Limit = 50, offset: Offset = 0):
        return ws().list_artifacts(str(course_id), limit, offset)

    @app.get("/api/v1/courses/{course_id}/artifacts/{artifact_id}")
    def artifact(course_id: UUID, artifact_id: UUID):
        return ws().get_artifact(str(course_id), str(artifact_id))

    @app.get("/api/v1/courses/{course_id}/events")
    async def events(
        course_id: UUID,
        request: Request,
        after: Offset = 0,
        follow: bool = True,
        last_event_id: Annotated[str | None, Header()] = None,
    ):
        ws().get_course(str(course_id))
        if last_event_id:
            try:
                after = max(after, int(last_event_id))
            except ValueError as error:
                raise DomainError("invalid_event_id", "Last-Event-ID must be an integer") from error

        async def stream():
            cursor = after
            while True:
                batch = await asyncio.to_thread(ws().events, str(course_id), cursor)
                for event in batch:
                    yield f"id: {event['sequence']}\nevent: {event['type']}\ndata: {json.dumps(event)}\n\n"
                    cursor = event["sequence"]
                if len(batch) == 100:
                    continue
                if not follow or await request.is_disconnected():
                    break
                yield ": heartbeat\n\n"
                await asyncio.sleep(1)

        return StreamingResponse(
            stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache"}
        )

    @app.get("/api/v1/agents")
    async def agent_providers(refresh: bool = False):
        return await asyncio.to_thread(agents.providers, refresh, settings.data_dir)

    @app.get("/api/v1/settings")
    def get_settings():
        return {"reading_model": ws().reading_model()}

    @app.put("/api/v1/settings")
    def put_settings(data: SettingsUpdate):
        ws().set_setting("reading_model", data.reading_model.model_dump())
        return get_settings()

    @app.get("/api/v1/skills")
    def skills():
        return list_skills()

    @app.get("/api/v1/skills/{name}")
    def read_skill(name: str):
        if name not in {item["name"] for item in list_skills()}:
            raise DomainError("not_found", "Skill not found", 404)
        return {"name": name, "text": skill(name)}

    def runner() -> Runner:
        if app.state.runner is None:
            raise DomainError("runner_disabled", "Background agents are disabled on this server", 503)
        return app.state.runner

    @app.get("/api/v1/courses/{course_id}/tasks")
    def tasks(course_id: UUID, active: bool = False, limit: Limit = 30):
        return ws().list_tasks(str(course_id), active, limit)

    @app.post("/api/v1/courses/{course_id}/tasks/{task_id}/cancel")
    def cancel_task(course_id: UUID, task_id: UUID):
        return runner().cancel(str(course_id), str(task_id))

    @app.post("/api/v1/courses/{course_id}/weeks/{week}/generate", status_code=202)
    def generate_week(course_id: UUID, week: Annotated[int, PathParam(ge=1, le=60)], data: WeekGenerate):
        ws().get_course(str(course_id))
        active = [
            t
            for t in ws().list_tasks(str(course_id), True)
            if t["kind"] == "week_notes" and t["params"]["week"] == week
        ]
        if active:
            raise DomainError("task_active", f"Week {week} notes are already being written", 409)
        agents.command(data.provider, data.model, data.effort, settings.data_dir)
        return runner().generate_week(
            str(course_id), week, data.provider, data.model, data.effort, data.regenerate
        )

    @app.post("/api/v1/courses/{course_id}/sources/{source_id}/read", status_code=202)
    def read_source_again(course_id: UUID, source_id: UUID, data: ReadRequest):
        return ws().request_reading(str(course_id), str(source_id), data.pages)

    @app.get("/api/v1/courses/{course_id}/sources/{source_id}/notes")
    def source_notes(
        course_id: UUID,
        source_id: UUID,
        first_page: int = Query(default=1, ge=1),
        last_page: int | None = Query(default=None, ge=1),
    ):
        return ws().source_notes(str(course_id), str(source_id), first_page, last_page)

    @app.get("/api/v1/courses/{course_id}/textbook/outline")
    def textbook_outline(course_id: UUID, chapter: int | None = Query(default=None, ge=1, le=100)):
        return ws().textbook_outline(str(course_id), chapter)

    @app.get("/api/v1/courses/{course_id}/textbook/problems")
    def textbook_problems(
        course_id: UUID,
        chapter: int | None = Query(default=None, ge=1, le=100),
        section: str | None = Query(default=None, max_length=60),
        query: str | None = Query(default=None, max_length=300),
        limit: Limit = 20,
    ):
        return ws().textbook_problems(str(course_id), chapter, section, query, limit)

    @app.post("/api/v1/agents/{provider}/login")
    async def agent_login(provider: str):
        return await asyncio.to_thread(agents.open_login, provider)

    @app.post("/api/v1/agents/{provider}/logout")
    async def agent_logout(provider: str):
        return await asyncio.to_thread(agents.logout, provider)

    @app.post("/api/v1/courses/{course_id}/chats/{chat_id}/runs")
    async def agent_run(course_id: UUID, chat_id: UUID, data: AgentRunRequest):
        course_id, chat_id, workspace = str(course_id), str(chat_id), ws()
        if chat_id in app.state.runs:
            raise DomainError("run_active", "This chat is already answering; stop it or wait", 409)
        course = workspace.get_course(course_id)
        workspace.list_messages(course_id, chat_id, 0, 1)
        args = agents.command(data.provider, data.model, data.effort, settings.data_dir)
        viewing, references, viewer = (
            "The student is not viewing a specific note or source.",
            [],
            ViewerState(),
        )
        if data.document:
            doc = workspace.read_document(course_id, str(data.document.document_id), data.document.revision)
            references = [data.document]
            viewer = ViewerState(document_id=doc["document_id"], revision=doc["revision"])
            viewing = (
                f'The student is viewing the note "{doc["title"]}" '
                f"(document_id {doc['document_id']}, revision {doc['revision']})."
            )
        elif data.source_id:
            source = workspace.read_source(course_id, str(data.source_id), None, 1, 0)
            page = f", page {data.source_page}" if data.source_page else ""
            viewing = (
                f'The student is viewing the source "{source["filename"]}" (source_id {source["id"]}{page}).'
            )
        workspace.set_viewer_state(course_id, chat_id, viewer)
        user = await asyncio.to_thread(
            workspace.add_message,
            course_id,
            chat_id,
            MessageCreate(role="user", content=data.content, references=references),
        )
        inspection = await asyncio.to_thread(
            workspace.assemble_context, course_id, chat_id, ContextRequest(query=data.content)
        )
        prompt = agents.build_prompt(course, chat_id, data.content, viewing, inspection["context"])
        loop, queue = asyncio.get_running_loop(), asyncio.Queue()
        run = await asyncio.to_thread(
            agents.AgentRun,
            data.provider,
            args,
            prompt,
            agents.agent_dir(settings.data_dir),
            lambda event: loop.call_soon_threadsafe(queue.put_nowait, event),
        )
        app.state.runs[chat_id] = run

        def sse(event):
            return f"data: {json.dumps(event)}\n\n"

        async def stream():
            try:
                yield sse({"type": "user_message", "message": user})
                while True:
                    event = await queue.get()
                    if event["type"] == "final":
                        text = event["text"].strip() or "The agent finished without a written answer."
                        saved = await asyncio.to_thread(
                            workspace.add_message,
                            course_id,
                            chat_id,
                            MessageCreate(role="assistant", content=text[:30000]),
                        )
                        yield sse({"type": "done", "message": saved})
                        break
                    yield sse(event)
                    if event["type"] == "error":
                        break
            finally:
                run.cancel()
                app.state.runs.pop(chat_id, None)

        return StreamingResponse(
            stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache"}
        )

    web = Path(__file__).parent / "web"
    if (web / "index.html").is_file():
        app.mount("/assets", StaticFiles(directory=web / "assets"), name="assets")

        @app.get("/{path:path}", include_in_schema=False)
        def frontend(path: str):
            if path.startswith("api/"):
                raise DomainError("not_found", "Route not found", 404)
            file = (web / path).resolve()
            if path and file.is_file() and file.is_relative_to(web.resolve()):
                return FileResponse(file)
            return FileResponse(web / "index.html", headers={"Cache-Control": "no-cache"})

    return app


def simulate_artifact(workspace, course_id, artifact_id):
    artifact = workspace.get_artifact(course_id, artifact_id)
    if artifact["kind"] != "circuit":
        raise DomainError("artifact_type", "Simulation requires a circuit artifact")
    result = circuits.simulate_dc(artifact["payload"]["circuit"])
    return workspace.save_artifact(
        course_id,
        "simulation",
        artifact["title"] + " — DC result",
        result | {"circuit_artifact_id": artifact_id},
    )
