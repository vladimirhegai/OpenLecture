import os
import sys
from datetime import timedelta

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


@pytest.mark.anyio
async def test_real_stdio_mcp_shares_database_with_http(client, course, settings):
    parameters = StdioServerParameters(
        command=sys.executable,
        args=["-m", "open_lecture.mcp_server"],
        env={**os.environ, "OPENLECTURE_DATA_DIR": str(settings.data_dir)},
    )
    async with stdio_client(parameters) as (read, write):
        async with ClientSession(read, write, read_timeout_seconds=timedelta(seconds=30)) as session:
            await session.initialize()
            catalog = await session.list_tools()
            names = {tool.name for tool in catalog.tools}
            assert {
                "document_create",
                "document_update",
                "source_search",
                "math_evaluate",
                "circuit_simulate",
            } <= names
            found = await session.call_tool("course_list")
            assert not found.isError
            assert found.structuredContent["courses"][0]["id"] == course
            created = await session.call_tool(
                "document_create",
                {
                    "course_id": course,
                    "data": {
                        "title": "MCP notes",
                        "academic_week": 1,
                        "actor": "agent",
                        "blocks": [{"type": "paragraph", "text": "Persisted through MCP."}],
                    },
                },
            )
            assert not created.isError, created.content
            document = created.structuredContent["document"]
            base = f"/api/v1/courses/{course}/documents/{document['document_id']}"
            assert client.get(base).json()["blocks"][0]["text"] == "Persisted through MCP."
            client.patch(base, json={"expected_revision": 1, "title": "Edited over HTTP"})
            updated = await session.call_tool(
                "document_read", {"course_id": course, "document_id": document["document_id"]}
            )
            assert updated.structuredContent["revision"] == 2
            assert updated.structuredContent["title"] == "Edited over HTTP"
            conflict = await session.call_tool(
                "document_update",
                {
                    "course_id": course,
                    "document_id": document["document_id"],
                    "data": {"expected_revision": 1, "title": "Old"},
                },
            )
            assert conflict.isError
            math = await session.call_tool("math_evaluate", {"data": {"expression": "2 + 3"}})
            assert math.structuredContent["exact"] == "5"
            invalid = await session.call_tool(
                "document_create",
                {
                    "course_id": course,
                    "data": {"title": "Bad output", "blocks": [{"type": "raw_html", "html": "<script/>"}]},
                },
            )
            assert invalid.isError
