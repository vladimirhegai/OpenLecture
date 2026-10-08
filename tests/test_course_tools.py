import math

import pymupdf
import pytest
from conftest import wait_job


def test_course_profiles_extensible_and_context_aware(client, course):
    base = f"/api/v1/courses/{course}"
    pack_ids = {pack["id"] for pack in client.get("/api/v1/course-packs").json()}
    assert {"circuits", "probability", "differential_equations", "digital_systems", "pdf_study"} <= pack_ids
    data = {
        "expected_revision": 0,
        "term": "Fall 2026",
        "pack_ids": ["digital_systems", "pdf_study"],
        "topics": [{"key": "boolean_algebra", "title": "Boolean algebra"}],
    }
    assert client.put(base + "/profile", json=data).json()["revision"] == 1
    assert client.put(base + "/profile", json=data).status_code == 409
    guidance = client.get(base + "/study-guidance").json()
    assert guidance["profile"]["topics"][0]["week"] is None
    assert len(guidance["course_packs"]) == 2
    assert guidance["note_recipe"]
    assert (
        client.put(base + "/profile", json={"expected_revision": 1, "pack_ids": ["made_up"]}).status_code
        == 400
    )
    # A future semester/course can compose the same subject tools without any four-course limit.
    later = client.post("/api/v1/courses", json={"code": "NEW 501", "title": "Future course"}).json()["id"]
    assert (
        client.put(f"/api/v1/courses/{later}/profile", json=data | {"term": "Winter 2027"}).status_code == 200
    )


@pytest.mark.parametrize(
    "parameters,expected",
    [
        ({"distribution": "normal", "mean": 0, "std": 1, "x": 0}, 0.5),
        ({"distribution": "poisson", "rate": 2, "x": 0}, math.exp(-2)),
        ({"distribution": "exponential", "rate": 2, "x": 0.5}, 1 - math.exp(-1)),
        ({"distribution": "uniform", "low": 0, "high": 10, "x": 5}, 0.5),
        ({"distribution": "gamma", "shape": 1, "scale": 2, "x": 2}, 1 - math.exp(-1)),
    ],
)
def test_probability_distributions(client, course, parameters, expected):
    response = client.post("/api/v1/math/distribution", json=parameters)
    assert response.status_code == 200, response.text
    result = response.json()
    assert result["outputs"]["cdf"] == pytest.approx(expected)
    assert result["outputs"]["survival_probability"] + expected == pytest.approx(1)
    assert len(result["chart"]["x"]) == len(result["chart"]["y"])
    artifact = client.post(f"/api/v1/courses/{course}/math-cards/distribution", json=parameters)
    assert artifact.status_code == 201
    assert artifact.json()["payload"] == result


def test_linear_ode_matches_rc_and_harmonic_oscillator(client):
    rc = client.post(
        "/api/v1/math/linear-ode", json={"order": 1, "a": -2, "forcing": 10, "y0": 0, "duration": 2}
    ).json()
    assert rc["chart"]["y"][-1] == pytest.approx(5 * (1 - math.exp(-4)))
    assert rc["initial_condition_error"] == 0
    oscillator = client.post(
        "/api/v1/math/linear-ode", json={"order": 2, "a": 0, "b": -1, "y0": 1, "dy0": 0, "duration": math.pi}
    ).json()
    assert oscillator["chart"]["y"][-1] == pytest.approx(-1)
    assert oscillator["chart"]["dy"][-1] == pytest.approx(0, abs=1e-12)
    assert client.post("/api/v1/math/linear-ode", json={"a": 2, "b": 1, "duration": 1}).status_code == 422


def test_logic_table_and_kmap(client, course):
    parameters = {"expression": "(A & B) | (A & ~B)", "variables": ["A", "B"]}
    result = client.post("/api/v1/logic/truth-table", json=parameters).json()
    assert result["simplified_sop"] == "A"
    assert [row["output"] for row in result["rows"]] == [0, 0, 1, 1]
    assert result["karnaugh_map"]["values"] == [[0, 0], [1, 1]]
    four = client.post(
        "/api/v1/logic/truth-table", json={"expression": "A ^ B ^ C ^ D", "variables": ["A", "B", "C", "D"]}
    ).json()
    assert four["karnaugh_map"]["column_labels"] == ["00", "01", "11", "10"]
    saved = client.post(f"/api/v1/courses/{course}/logic-cards", json=parameters).json()
    assert saved["payload"] == result
    for expression in ["eval('A')", "A.__class__", "A and B", "C | A"]:
        assert (
            client.post("/api/v1/logic/truth-table", json=parameters | {"expression": expression}).status_code
            == 422
        )


def test_pdf_visual_page_preserves_real_diagrams(client, course):
    with pymupdf.open() as doc:
        page = doc.new_page()
        page.insert_text((50, 50), "Voltage divider")
        page.draw_rect(pymupdf.Rect(50, 70, 100, 100))
        pdf = doc.tobytes()
    base = f"/api/v1/courses/{course}"
    upload = client.post(base + "/sources", files={"file": ("diagram.pdf", pdf)}).json()
    assert wait_job(client, course, upload["job_id"])["status"] == "completed"
    response = client.get(base + f"/sources/{upload['source_id']}/pages/1")
    assert response.status_code == 200 and response.content.startswith(b"\x89PNG")
    assert client.get(base + f"/sources/{upload['source_id']}/pages/2").status_code == 422
