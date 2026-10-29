import json
from xml.etree import ElementTree

import pytest

from open_lecture import digital
from open_lecture.errors import DomainError
from open_lecture.schemas import Paragraph

FIGURES = [
    {"kind": "venn", "variables": ["A", "B"], "shaded": [0, 1, 2]},
    {
        "kind": "circuit",
        "nodes": [
            {"id": "A", "gate": "INPUT", "x": 70, "y": 90},
            {"id": "G", "gate": "NOT", "x": 250, "y": 90},
            {"id": "F", "gate": "OUTPUT", "x": 430, "y": 90},
        ],
        "wires": [{"start": "A.out", "end": "G.0"}, {"start": "G.out", "end": "F.0"}],
    },
    {
        "kind": "kmap",
        "variables": ["A", "B", "C", "D"],
        "ones": [0, 2, 8, 10],
        "groups": [{"cells": [0, 2, 8, 10], "label": "corners"}],
    },
    {"kind": "timing", "signals": [{"name": "CLK", "wave": "0101"}, {"name": "Q", "wave": "0.1."}]},
    {
        "kind": "fsm",
        "initial": "A",
        "states": [{"id": "A", "x": 100, "y": 150}],
        "transitions": [{"start": "A", "end": "A", "label": "0/1"}],
    },
    {"kind": "cmos", "pdn": {"series": [{"gate": "A"}, {"parallel": [{"gate": "B"}, {"gate": "C"}]}]}},
]


@pytest.mark.parametrize("figure", FIGURES)
def test_figures_render_as_safe_deterministic_svg(figure):
    source = json.dumps(figure)
    svg = digital.render_svg(source)
    checked = digital.check(source)
    assert checked["kind"] == figure["kind"]
    assert digital.render_svg(json.dumps(checked["figure"])) == svg
    assert ElementTree.fromstring(svg).tag.endswith("svg")
    assert digital.render_svg(source) == svg
    Paragraph(text=f"```digital\n{source}\n```")


def test_map_order_and_invalid_groups():
    assert digital.gray_order(3) == [[0, 1, 3, 2], [4, 5, 7, 6]]
    assert digital.gray_order(4)[-1] == [8, 9, 11, 10]
    for cells in ([0, 3], [0, 1, 2], [0, 16]):
        with pytest.raises(DomainError):
            digital.check(
                json.dumps(
                    {
                        "kind": "kmap",
                        "variables": ["A", "B", "C", "D"],
                        "ones": [0, 1, 2, 3],
                        "groups": [{"cells": cells, "label": "bad"}],
                    }
                )
            )
    digital.check(
        json.dumps(
            {
                "kind": "kmap",
                "variables": ["A", "B"],
                "ones": [1, 3],
                "dont_cares": [0],
                "target": 0,
                "groups": [{"cells": [0, 2], "label": "zeros"}],
            }
        )
    )


@pytest.mark.parametrize(
    "figure",
    [
        {"kind": "timing", "signals": [{"name": "A", "wave": ".0"}]},
        {"kind": "timing", "signals": [{"name": "A", "wave": "01"}, {"name": "B", "wave": "0"}]},
        {"kind": "cmos", "pdn": {"series": [{"gate": "A"}]}},
        {"kind": "fsm", "initial": "B", "states": [{"id": "A", "x": 100, "y": 150}]},
        {"kind": "kmap", "variables": ["A", "B"], "ones": [0], "dont_cares": [0]},
    ],
)
def test_invalid_figures_rejected(figure):
    with pytest.raises(DomainError):
        digital.check(json.dumps(figure))


def test_circuit_rejects_missing_pins_and_multiple_drivers():
    original = next(f for f in FIGURES if f["kind"] == "circuit")
    f = json.loads(json.dumps(original))
    f["wires"][0]["end"] = "G.2"
    with pytest.raises(DomainError):
        digital.check(json.dumps(f))
    f["wires"] = []
    with pytest.raises(DomainError):
        digital.check(json.dumps(f))
    f["wires"] = [*original["wires"], original["wires"][0]]
    with pytest.raises(DomainError):
        digital.check(json.dumps(f))


def test_labels_escape_markup():
    svg = digital.render_svg(
        json.dumps(
            {
                "kind": "timing",
                "title": "<script>x</script>",
                "signals": [{"name": "<img src=x>", "wave": "01"}],
            }
        )
    )
    assert "<script>" not in svg and "<img " not in svg
    assert "&lt;img src=x&gt;" in svg


def test_api_and_document_validation(client):
    source = json.dumps(next(f for f in FIGURES if f["kind"] == "kmap"))
    r = client.post("/api/v1/digital/render", json={"source": source})
    assert r.status_code == 200 and r.headers["content-type"].startswith("image/svg+xml")
    assert client.post("/api/v1/digital/check", json={"source": source}).json()["kind"] == "kmap"
    assert client.post("/api/v1/digital/render", json={"source": "{bad"}).status_code == 400
    course = client.post("/api/v1/courses", json={"code": "DS", "title": "Digital"}).json()["id"]
    url = f"/api/v1/courses/{course}/documents"
    body = {"title": "Logic", "blocks": [{"type": "paragraph", "text": f"```digital\n{source}\n```"}]}
    assert client.post(url, json=body).status_code == 201
    body["blocks"][0]["text"] = '```digital\n{"kind":"unknown"}\n```'
    assert client.post(url, json=body).status_code == 422
    body["blocks"] = [{"type": "code", "language": "digital", "text": '{"kind":"unknown"}'}]
    assert client.post(url, json=body).status_code == 422


def test_circuit_highlight_and_values_render():
    source = json.dumps(
        {
            "kind": "circuit",
            "nodes": [
                {"id": "a", "gate": "INPUT", "x": 80, "y": 90, "value": 1},
                {"id": "b", "gate": "INPUT", "x": 80, "y": 170, "value": 0},
                {"id": "G", "gate": "NAND", "x": 300, "y": 130, "highlight": True, "value": 1},
                {"id": "f", "gate": "OUTPUT", "x": 480, "y": 130, "value": 1},
            ],
            "wires": [
                {"start": "a.out", "end": "G.0", "value": 1},
                {"start": "b.out", "end": "G.1", "value": 0},
                {"start": "G.out", "end": "f.0", "highlight": True},
            ],
        }
    )
    svg = digital.render_svg(source)
    assert 'fill="#dbeafe"' in svg  # highlighted gate
    assert 'stroke="#16a34a"' in svg and 'stroke="#94a3b8"' in svg  # wires at 1 and 0
    assert svg.count('rx="4" fill="#16a34a"') == 3  # 1-chips on a, G, f
    with pytest.raises(DomainError):
        digital.parse(source.replace('"value": 0', '"value": 2'))


def test_cmos_rows_hidden_halves_and_resistor_pullup():
    nand = {"kind": "cmos", "pdn": {"series": [{"gate": "x1"}, {"gate": "x2"}]}}
    plain = digital.render_svg(json.dumps(nand))
    row = digital.render_svg(json.dumps({**nand, "inputs": {"x1": 1, "x2": 1}}))
    assert 'stroke="#16a34a"' not in plain and "f = 0" in row and "PDN conducts" in row
    assert "PUN conducts" in digital.render_svg(json.dumps({**nand, "inputs": {"x1": 0, "x2": 1}}))
    assert "PUN: ?" in digital.render_svg(json.dumps({**nand, "show": "pdn"}))
    nmos = digital.render_svg(json.dumps({**nand, "pullup": "resistor", "inputs": {"x1": 1, "x2": 1}}))
    assert "Current flows" in nmos and "PUN" not in nmos
    with pytest.raises(DomainError):
        digital.parse(json.dumps({**nand, "inputs": {"x1": 2}}))
