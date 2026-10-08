"""Independent agent acceptance scenario over the real stdio transport."""

import base64
import os
import sys
from datetime import timedelta
from uuid import uuid4

import pymupdf
import pytest
from conftest import wait_job
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


@pytest.mark.anyio
async def test_agent_pdf_notes_targeted_edits_artifacts_and_course_isolation(client, course, settings):
    base = f"/api/v1/courses/{course}"
    other = client.post("/api/v1/courses", json={"code": "ELEC 326", "title": "Probability"}).json()["id"]
    with pymupdf.open() as pdf:
        pdf.new_page().insert_text((72, 72), "A voltage divider has output Vout = Vin R2 / (R1 + R2).")
        uploaded = client.post(base + "/sources", files={"file": ("divider.pdf", pdf.tobytes())}).json()
    assert wait_job(client, course, uploaded["job_id"])["status"] == "completed"

    parameters = StdioServerParameters(
        command=sys.executable,
        args=["-m", "open_lecture.mcp_server"],
        env={**os.environ, "OPENLECTURE_DATA_DIR": str(settings.data_dir)},
    )
    async with stdio_client(parameters) as (read, write):
        async with ClientSession(read, write, read_timeout_seconds=timedelta(seconds=30)) as session:
            await session.initialize()

            async def call(name, **arguments):
                result = await session.call_tool(name, arguments)
                assert not result.isError, result.content
                return result.structuredContent

            async def rejected(name, **arguments):
                result = await session.call_tool(name, arguments)
                assert result.isError, f"{name} unexpectedly accepted {arguments}"

            found = await call("document_find", course_id=course, academic_week=2)
            assert found["documents"] == []
            plan = await call(
                "document_plan", course_id=course, data={"intent": "create", "academic_week": 2}
            )
            assert plan["action"] == "create_document"
            passages = (await call("source_search", course_id=course, query="voltage divider"))["passages"]
            assert passages and passages[0]["source_id"] == uploaded["source_id"]
            assert passages[0]["page"] == 1
            citation = {
                "source_id": passages[0]["source_id"],
                "version": passages[0]["version"],
                "chunk_id": passages[0]["id"],
            }
            source = await call("source_read", course_id=course, source_id=uploaded["source_id"])
            assert any(chunk["id"] == citation["chunk_id"] for chunk in source["chunks"])

            circuit = await call(
                "circuit_create",
                course_id=course,
                data={
                    "definition": (
                        'circuit "Divider example"\nV1 vin 0 DC 10V\nR1 vin out 2kOhm\n'
                        "R2 out 0 3kOhm\nanalyze dc\nprobe V(out)"
                    )
                },
            )
            simulation = await call("circuit_simulate", course_id=course, artifact_id=circuit["id"])
            assert simulation["payload"]["node_voltages"]["out"] == pytest.approx(6)
            assert simulation["payload"]["circuit_artifact_id"] == circuit["id"]

            heading_id, paragraph_id = str(uuid4()), str(uuid4())
            body = {
                "title": "Week 2 divider notes",
                "academic_week": 2,
                "topic_keys": ["voltage_divider"],
                "actor": "agent",
                "idempotency_key": "agent-divider-notes",
                "blocks": [
                    {"type": "heading", "id": heading_id, "text": "Voltage divider"},
                    {
                        "type": "paragraph",
                        "id": paragraph_id,
                        "text": "The output follows the resistor ratio.",
                        "citations": [citation],
                    },
                    {"type": "equation", "latex": r"V_o=V_i\frac{R_2}{R_1+R_2}", "citations": [citation]},
                    {
                        "type": "artifact_reference",
                        "artifact_id": simulation["id"],
                        "caption": "Computed DC result",
                    },
                    {
                        "type": "practice_problem",
                        "prompt": "Find output for 10 V, 2 kohm and 3 kohm.",
                        "solution": "6 V",
                        "origin": "original",
                    },
                ],
            }
            created = await call("document_create", course_id=course, data=body)
            document = created["document"]
            document_id = document["document_id"]
            url = base + f"/documents/{document_id}"
            # MCP writes return a compact reference; the full note is read separately.
            assert "blocks" not in document
            document = client.get(url).json()
            assert created["document"]["block_count"] == len(document["blocks"])
            retry = await call("document_create", course_id=course, data=body)
            assert not retry["created"] and retry["document"]["document_id"] == document_id
            catalog = (await call("document_find", course_id=course, topic="voltage_divider"))["documents"]
            assert len(catalog) == 1 and "blocks" not in catalog[0]
            plan = await call(
                "document_plan", course_id=course, data={"intent": "create", "academic_week": 2}
            )
            assert plan["action"] == "reuse_document"
            assert plan["targets"][0]["document_id"] == document_id
            await rejected(
                "document_create", course_id=course, data={"title": "Duplicate", "academic_week": 2}
            )

            chat = await call("chat_create", course_id=course, data={"title": "Divider follow-up"})
            reference = {"document_id": document_id, "revision": 1, "block_id": paragraph_id}
            await call(
                "chat_add_message",
                course_id=course,
                chat_id=chat["id"],
                data={"role": "assistant", "content": "Saved your divider notes.", "references": [reference]},
            )
            state = await call("context_select", course_id=course, chat_id=chat["id"], data=reference)
            assert state["block_id"] == paragraph_id
            question = await call("document_plan", course_id=course, data={"intent": "question"})
            assert question["action"] == "answer_in_chat"
            assert client.get(url).json()["revision"] == 1

            # HTTP changes and subsequent MCP edits must agree on the same revision.
            assert (
                client.patch(
                    url, json={"expected_revision": 1, "title": "Divider: student title"}
                ).status_code
                == 200
            )
            await rejected(
                "document_update",
                course_id=course,
                document_id=document_id,
                data={"expected_revision": 1, "title": "Stale agent title"},
            )
            current = await call("document_read", course_id=course, document_id=document_id)
            assert current["revision"] == 2 and current["title"] == "Divider: student title"
            replacement = current["blocks"][1] | {"text": "At 10 V, a 2 kohm/3 kohm divider produces 6 V."}
            updated = await call(
                "document_update",
                course_id=course,
                document_id=document_id,
                data={
                    "expected_revision": 2,
                    "actor": "agent",
                    "operations": [{"op": "replace", "block_id": paragraph_id, "block": replacement}],
                },
            )
            assert updated["revision"] == 3 and "blocks" not in updated
            updated = client.get(url).json()
            assert updated["blocks"][0] == document["blocks"][0]
            assert updated["blocks"][2:] == document["blocks"][2:]
            assert client.get(url).json()["blocks"][1] == replacement
            historical = await call("document_read", course_id=course, document_id=document_id, revision=1)
            assert historical["blocks"] == document["blocks"]
            revisions = await call("document_list_revisions", course_id=course, document_id=document_id)
            assert [revision["revision"] for revision in revisions["revisions"]] == [3, 2, 1]

            # An invalid insert rolls back an otherwise valid edit in the same request.
            await rejected(
                "document_update",
                course_id=course,
                document_id=document_id,
                data={
                    "expected_revision": 3,
                    "title": "Must not persist",
                    "operations": [
                        {
                            "op": "insert",
                            "block": {
                                "type": "paragraph",
                                "text": "False provenance",
                                "citations": [citation | {"chunk_id": str(uuid4())}],
                            },
                        }
                    ],
                },
            )
            assert client.get(url).json()["title"] == "Divider: student title"
            assert client.get(url).json()["revision"] == 3

            assert (await call("source_search", course_id=other, query="voltage divider"))["passages"] == []
            assert (await call("document_find", course_id=other))["documents"] == []
            assert (await call("artifact_list", course_id=other))["artifacts"] == []
            for name, arguments in [
                ("source_read", {"source_id": uploaded["source_id"]}),
                ("job_get", {"job_id": uploaded["job_id"]}),
                ("document_read", {"document_id": document_id}),
                ("artifact_get", {"artifact_id": simulation["id"]}),
                ("circuit_simulate", {"artifact_id": circuit["id"]}),
                ("chat_messages", {"chat_id": chat["id"]}),
            ]:
                await rejected(name, course_id=other, **arguments)
            for block in [
                {"type": "paragraph", "text": "Wrong course evidence", "citations": [citation]},
                {"type": "artifact_reference", "artifact_id": simulation["id"]},
                {
                    "type": "practice_problem",
                    "prompt": "From tutorial",
                    "solution": "6 V",
                    "origin": "source",
                },
            ]:
                await rejected(
                    "document_create", course_id=other, data={"title": "Invalid note", "blocks": [block]}
                )
            other_chat = await call("chat_create", course_id=other, data={"title": "Probability study"})
            await rejected(
                "chat_add_message",
                course_id=other,
                chat_id=other_chat["id"],
                data={"role": "assistant", "content": "Wrong course link", "references": [reference]},
            )
            await rejected("context_select", course_id=other, chat_id=other_chat["id"], data=reference)
            assert client.get(f"/api/v1/courses/{other}/documents").json() == []
            artifact = await call("artifact_get", course_id=course, artifact_id=simulation["id"])
            assert artifact["payload"] == simulation["payload"]
            assert (
                client.get(base + f"/artifacts/{simulation['id']}").json()["payload"] == simulation["payload"]
            )


@pytest.mark.anyio
async def test_agent_course_guidance_new_tools_pdf_image_and_rich_notes(client, course, settings):
    base = f"/api/v1/courses/{course}"
    with pymupdf.open() as pdf:
        page = pdf.new_page()
        page.insert_text((72, 72), "Course scope: normal probability, ODEs and Boolean logic.")
        page.draw_rect(pymupdf.Rect(100, 100, 200, 150))
        uploaded = client.post(base + "/sources", files={"file": ("scope.pdf", pdf.tobytes())}).json()
    assert wait_job(client, course, uploaded["job_id"])["status"] == "completed"
    parameters = StdioServerParameters(
        command=sys.executable,
        args=["-m", "open_lecture.mcp_server"],
        env={**os.environ, "OPENLECTURE_DATA_DIR": str(settings.data_dir)},
    )
    async with stdio_client(parameters) as (read, write):
        async with ClientSession(read, write, read_timeout_seconds=timedelta(seconds=30)) as session:
            await session.initialize()

            async def call(name, **arguments):
                result = await session.call_tool(name, arguments)
                assert not result.isError, result.content
                return result.structuredContent

            tools = {tool.name: tool for tool in (await session.list_tools()).tools}
            assert {
                "course_profile_update",
                "course_study_guidance",
                "probability_distribution",
                "math_linear_ode",
                "logic_truth_table",
                "probability_save_card",
                "math_save_ode",
                "logic_save_card",
                "source_page",
            } <= tools.keys()
            assert tools["probability_distribution"].inputSchema["properties"]["data"]["oneOf"]

            chunk = (await call("source_search", course_id=course, query="scope"))["passages"][0]
            citation = {"source_id": chunk["source_id"], "version": chunk["version"], "chunk_id": chunk["id"]}
            pack_ids = ["probability", "differential_equations", "digital_systems", "pdf_study"]
            skills = await call("study_skill_list")
            assert set(pack_ids) <= {pack["id"] for pack in skills["course_packs"]}
            assert {"weekly-notes", "source-reading", "textbook-problems"} <= {
                s["name"] for s in skills["workflow_skills"]
            }
            profile = await call(
                "course_profile_update",
                course_id=course,
                data={
                    "expected_revision": 0,
                    "term": "Fall 2026",
                    "pack_ids": pack_ids,
                    "topics": [{"key": "probability", "title": "Normal probability", "week": 3}],
                    "syllabus_citations": [citation],
                    "study_preferences": ["Show intermediate derivation steps."],
                },
            )
            assert profile["revision"] == 1 and profile["syllabus_citations"] == [citation]
            guidance = await call("course_study_guidance", course_id=course)
            assert guidance["profile"] == profile
            assert {pack["id"] for pack in guidance["course_packs"]} == set(pack_ids)
            assert guidance["note_recipe"] and guidance["provenance_rule"]
            conflict = await session.call_tool(
                "course_profile_update",
                {"course_id": course, "data": {"expected_revision": 0, "pack_ids": []}},
            )
            assert conflict.isError
            assert (await call("course_study_guidance", course_id=course))["profile"] == profile

            # Exercise every discriminated-union branch through the client/server schema boundary.
            for data in [
                {"distribution": "normal", "mean": 0, "std": 1, "x": 0},
                {"distribution": "poisson", "rate": 2, "x": 1},
                {"distribution": "exponential", "rate": 2, "x": 1},
                {"distribution": "uniform", "low": 0, "high": 2, "x": 1},
                {"distribution": "gamma", "shape": 2, "scale": 1, "x": 1},
            ]:
                result = await call("probability_distribution", data=data)
                assert result["verified"] and result["distribution"] == data["distribution"]
                assert result["chart"]["x"] and len(result["chart"]["x"]) == len(result["chart"]["y"])
                assert 0 <= result["outputs"]["cdf"] <= 1
            ode_request = {"order": 2, "a": 0, "b": -1, "y0": 1, "dy0": 0, "duration": 2, "samples": 11}
            ode = await call("math_linear_ode", data=ode_request)
            assert ode["verified"] and len(ode["chart"]["x"]) == 11
            logic_request = {"expression": "(A & B) | (~A & B)", "variables": ["A", "B"]}
            logic = await call("logic_truth_table", data=logic_request)
            assert logic["verified"] and len(logic["rows"]) == 4
            assert logic["simplified_sop"] == "B" and logic["karnaugh_map"]

            saved = [
                await call(
                    "probability_save_card", course_id=course, data={"distribution": "normal", "x": 0}
                ),
                await call("math_save_ode", course_id=course, data=ode_request),
                await call("logic_save_card", course_id=course, data=logic_request),
            ]
            assert [artifact["kind"] for artifact in saved] == ["math_card", "math_card", "logic_card"]
            assert saved[1]["payload"] == ode and saved[2]["payload"] == logic
            blocks = [
                {
                    "type": "derivation",
                    "title": "A decaying exponential",
                    "steps": [
                        {"explanation": "Separate variables for nonzero y.", "latex": r"\frac{dy}{y}=-dt"},
                        {"explanation": "Integrate and apply y(0)=1.", "latex": r"y=e^{-t}"},
                    ],
                },
                {
                    "type": "solution",
                    "title": "Check the initial value",
                    "text": "At t=0, exp(0)=1.",
                    "collapsed": True,
                },
            ]
            blocks += [{"type": "artifact_reference", "artifact_id": artifact["id"]} for artifact in saved]
            document = (
                await call(
                    "document_create",
                    course_id=course,
                    data={"title": "Computed study examples", "actor": "agent", "blocks": blocks},
                )
            )["document"]
            persisted = client.get(base + f"/documents/{document['document_id']}").json()
            assert document["block_count"] == len(persisted["blocks"]) == len(blocks)
            assert persisted["blocks"][0]["type"] == "derivation"
            assert persisted["blocks"][1]["collapsed"] is True
            for artifact in saved:
                read_back = await call("artifact_get", course_id=course, artifact_id=artifact["id"])
                assert read_back["payload"] == artifact["payload"]
                assert (
                    client.get(base + f"/artifacts/{artifact['id']}").json()["payload"] == artifact["payload"]
                )

            image_result = await session.call_tool(
                "source_page",
                {"course_id": course, "source_id": uploaded["source_id"], "page": 1, "version": 1},
            )
            assert not image_result.isError, image_result.content
            images = [part for part in image_result.content if part.type == "image"]
            assert len(images) == 1 and images[0].mimeType == "image/png"
            png = base64.b64decode(images[0].data, validate=True)
            assert png.startswith(b"\x89PNG\r\n\x1a\n")
            pixmap = pymupdf.Pixmap(png)
            assert pixmap.width > 100 and pixmap.height > 100
            descriptions = [part.text for part in image_result.content if part.type == "text"]
            assert any(uploaded["source_id"] in text and "page 1" in text for text in descriptions)
            bad_page = await session.call_tool(
                "source_page", {"course_id": course, "source_id": uploaded["source_id"], "page": 2}
            )
            assert bad_page.isError
