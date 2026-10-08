import json
import threading
from pathlib import Path

import pytest

from open_lecture import agents


def collect(parse, lines):
    state, events = {}, []
    for line in lines:
        events.extend(parse(line, state))
    return events


def test_claude_stream_events_are_normalized():
    lines = [
        {"type": "system", "subtype": "init", "tools": ["ToolSearch"]},
        {"type": "assistant", "message": {"content": [{"type": "tool_use", "name": "ToolSearch"}]}},
        {
            "type": "assistant",
            "message": {"content": [{"type": "tool_use", "name": "mcp__open_lecture__source_search"}]},
        },
        {"type": "stream_event", "event": {"type": "content_block_start", "content_block": {"type": "text"}}},
        {
            "type": "stream_event",
            "event": {"type": "content_block_delta", "delta": {"type": "text_delta", "text": "25%"}},
        },
        {
            "type": "stream_event",
            "event": {"type": "content_block_delta", "delta": {"type": "thinking_delta"}},
        },
        {"type": "result", "subtype": "success", "is_error": False, "result": "25%"},
    ]
    assert collect(agents.parse_claude, lines) == [
        {"type": "tool", "name": "source search"},
        {"type": "text_start"},
        {"type": "text", "delta": "25%"},
        {"type": "final", "text": "25%"},
    ]
    failed = [{"type": "result", "subtype": "success", "is_error": True, "result": "Not logged in"}]
    assert collect(agents.parse_claude, failed) == [{"type": "error", "message": "Not logged in"}]


def test_codex_json_events_are_normalized():
    lines = [
        {"type": "thread.started", "thread_id": "t"},
        {"type": "item.completed", "item": {"type": "agent_message", "text": "Checking the syllabus."}},
        {
            "type": "item.started",
            "item": {"type": "mcp_tool_call", "server": "open_lecture", "tool": "source_search"},
        },
        {"type": "item.completed", "item": {"type": "agent_message", "text": "The final is 45%."}},
        {"type": "turn.completed", "usage": {}},
    ]
    events = collect(agents.parse_codex, lines)
    assert {"type": "tool", "name": "source search"} in events
    assert events[-1] == {"type": "final", "text": "The final is 45%."}
    assert collect(agents.parse_codex, [{"type": "turn.failed", "error": {"message": "quota"}}]) == [
        {"type": "error", "message": "quota"}
    ]
    retry = {"type": "error", "message": "Reconnecting... 1/5 (stream disconnected before completion)"}
    assert collect(agents.parse_codex, [retry]) == []


def test_agent_commands_expose_only_workspace_tools(monkeypatch, tmp_path):
    monkeypatch.setattr(agents, "executable", lambda provider: f"/bin/{provider}")
    claude = agents.command("claude", "opus", "high", tmp_path)
    assert claude[claude.index("--tools") + 1] == "ToolSearch"
    assert claude[claude.index("--allowedTools") + 1] == "mcp__open_lecture"
    assert "--strict-mcp-config" in claude and "--no-session-persistence" in claude
    assert claude[claude.index("--model") + 1] == "opus"
    config = json.loads((tmp_path / "agent" / "mcp.json").read_text(encoding="utf-8"))
    assert config["mcpServers"]["open_lecture"]["args"] == ["-m", "open_lecture.mcp_server"]

    codex = agents.command("codex", "default", None, tmp_path)
    assert codex[codex.index("-s") + 1] == "read-only"
    disabled = {codex[i + 1] for i, arg in enumerate(codex) if arg == "--disable"}
    assert {"shell_tool", "browser_use", "computer_use", "plugins"} <= disabled
    assert "-m" not in codex and codex[-1] == "-"

    with pytest.raises(agents.DomainError):
        agents.command("claude", "opus; rm -rf /", None, tmp_path)


def test_provider_status_when_cli_missing(monkeypatch):
    monkeypatch.setattr(agents, "executable", lambda provider: None)
    agents._status_cache.clear()
    try:
        status = {p["id"]: p for p in agents.providers(refresh=True)}
        assert not status["claude"]["installed"] and not status["claude"]["signed_in"]
        assert status["claude"]["models"][0]["id"] == "default"
        assert status["codex"]["login_command"] == "codex login"
    finally:
        agents._status_cache.clear()


class FakeRun:
    instances = []

    def __init__(self, provider, args, prompt, cwd, emit):
        self.prompt, self.cancelled = prompt, False
        FakeRun.instances.append(self)

        def answer():
            emit({"type": "tool", "name": "source search"})
            emit({"type": "text_start"})
            emit({"type": "text", "delta": "Midterms are worth 25%."})
            emit({"type": "final", "text": "Midterms are worth 25%."})

        threading.Thread(target=answer).start()

    def cancel(self):
        self.cancelled = True


def test_chat_run_streams_and_saves_messages(client, course, monkeypatch):
    monkeypatch.setattr(agents, "command", lambda *args: ["fake"])
    monkeypatch.setattr(agents, "AgentRun", FakeRun)
    base = f"/api/v1/courses/{course}"
    chat = client.post(base + "/chats", json={"title": "Grading"}).json()["id"]
    body = {"provider": "claude", "model": "haiku", "content": "How much are midterms worth?"}
    with client.stream("POST", f"{base}/chats/{chat}/runs", json=body) as response:
        assert response.status_code == 200
        events = [json.loads(line[6:]) for line in response.iter_lines() if line.startswith("data: ")]
    assert [e["type"] for e in events] == ["user_message", "tool", "text_start", "text", "done"]
    assert events[-1]["message"]["role"] == "assistant"
    run = FakeRun.instances[-1]
    assert run.cancelled  # the process is always cleaned up when the stream ends
    assert "How much are midterms worth?" in run.prompt and "untrusted data" in run.prompt
    messages = client.get(f"{base}/chats/{chat}/messages").json()
    assert [m["role"] for m in messages] == ["user", "assistant"]
    assert client.post(f"{base}/chats/{chat}/runs", json=body | {"model": "bad model"}).status_code == 422


def test_source_detail_reports_page_count(client, course):
    import pymupdf
    from conftest import wait_job

    document = pymupdf.open()
    for text in ("First page", "Second page"):
        document.new_page().insert_text((72, 72), text)
    upload = client.post(
        f"/api/v1/courses/{course}/sources",
        files={"file": ("slides.pdf", document.tobytes(), "application/pdf")},
    ).json()
    wait_job(client, course, upload["job_id"])
    assert client.get(f"/api/v1/courses/{course}/sources/{upload['source_id']}").json()["pages"] == 2


def test_built_frontend_is_served_with_spa_routes(client):
    if not (Path(agents.__file__).parent / "web" / "index.html").is_file():
        pytest.skip("Frontend not built; run npm run build in frontend/")
    page = client.get("/courses/abc/docs/def")
    assert page.status_code == 200 and '<div id="root">' in page.text
    assert client.get("/api/v1/not-a-route").status_code == 404
    assert client.get("/api/v1/health").json()["status"] == "ok"
