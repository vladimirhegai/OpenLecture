import pytest

from open_lecture import schematic
from open_lecture.errors import DomainError

DIVIDER = r"""
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$" i="$i_a$"
R2 3,3 -> 3,0 "$10\,\Omega$" v="$v_o$"
wire 3,3 -> 6,3
G1 6,3 -> 6,0 "$2i_a$"
wire 6,0 -> 0,0   # bottom rail
label 3,3 "$a$" above
ground 0,0
"""


def test_topology_follows_wires_and_names_nodes():
    result = schematic.topology(DIVIDER)
    connections = {e["name"]: (e["from"], e["to"]) for e in result["elements"]}
    assert connections == {"V1": ("n1", "0"), "R1": ("n1", "a"), "R2": ("a", "0"), "G1": ("a", "0")}
    assert result["warnings"] == [] and result["errors"] == []
    assert {e["kind"] for e in result["elements"]} >= {"voltage_source", "dependent_current_source"}


def test_point_on_a_wire_joins_it_but_not_an_element_body():
    tee = "R1 0,0 -> 0,3\nwire 0,3 -> 6,3\nR2 3,3 -> 3,0\nwire 0,0 -> 3,0"
    connections = {e["name"]: (e["from"], e["to"]) for e in schematic.topology(tee)["elements"]}
    assert connections["R1"][1] == connections["R2"][0]
    with pytest.raises(DomainError, match="middle of R1"):
        schematic.check("R1 0,0 -> 0,3\nR2 0,1.5 -> 3,1.5\nwire 3,1.5 -> 3,0 -> 0,0")


@pytest.mark.parametrize(
    "source, message",
    [
        ("Q1 0,0 -> 3,0", "unknown statement"),
        ("R1 0,0 -> 3,0\nR1 3,0 -> 3,3", "defined twice"),
        ('R1 0,0 -> 3,0 bogus="x"', "unknown option"),
        ("R1 0,0 -> 0.5,0", "shorter"),
        ("wire 0,0", "two points"),
        ("R1 0,0 -> 99,0", "outside"),
    ],
)
def test_invalid_drawings_name_the_line(source, message):
    with pytest.raises(DomainError, match=message):
        schematic.check(source)


def test_render_and_document_validation(client, course):
    svg = client.post("/api/v1/schematics/render", json={"source": DIVIDER})
    assert svg.status_code == 200 and svg.headers["content-type"].startswith("image/svg+xml")
    assert "<svg" in svg.text and "<script" not in svg.text
    assert client.post("/api/v1/schematics/check", json={"source": DIVIDER}).json()["elements"]

    fence = f"Find $i_a$.\n\n```schematic\n{DIVIDER}\n```"
    blocks = [
        {"type": "schematic", "source": DIVIDER, "caption": "Divider"},
        {
            "type": "worked_example",
            "title": "Loop current",
            "prompt": fence,
            "steps": [{"explanation": "KVL around the loop.", "latex": "-50+15i_a=0"}],
            "answer": "$i_a=3.33\\,\\mathrm{A}$",
        },
        {
            "type": "practice_problem",
            "title": "Tutorial · Divider",
            "prompt": fence,
            "steps": [{"explanation": "Ohm's law."}],
            "answer": "**(a)** 2 A",
        },
    ]
    created = client.post(
        f"/api/v1/courses/{course}/documents", json={"title": "Schematics", "blocks": blocks}
    )
    assert created.status_code == 201, created.text
    saved = created.json()["document"]
    assert [b["type"] for b in saved["blocks"]] == ["schematic", "worked_example", "practice_problem"]

    broken = {"type": "paragraph", "text": '```schematic\nR1 0,0 -> 3,0 "unclosed\n```'}
    bad = client.post(f"/api/v1/courses/{course}/documents", json={"title": "Bad", "blocks": [broken]})
    assert bad.status_code == 422 and "Schematic line 1" in bad.text


def test_bare_current_and_voltage_marks_have_no_label():
    items = schematic.parse('L1 0,3 -> 0,0 "$L$" i v')["items"]
    assert items[0]["options"] == {"i": "", "v": ""}
    svg = schematic.render_svg('L1 0,3 -> 0,0 "$L$" i v\nwire 0,0 -> 0,3')
    assert "<svg" in svg
    assert schematic.parse('V1 0,3 -> 0,0 "$v$" i="$i_s$" i_rev')["items"][0]["options"] == {"i_rev": "$i_s$"}


def test_concurrent_renders_match_sequential():
    # A note page requests all its drawings at once; schemdraw's drawing state is global, so
    # renders on parallel server threads must not leak elements into each other's drawings.
    import sys
    from concurrent.futures import ThreadPoolExecutor

    sources = [
        f'X1 0,3 -> 0,0 "A"\nwire 0,3 -> {w},3\nwire 0,0 -> {w},0\nX2 {w},3 -> {w},0 "B" flip\n'
        f'gap {w / 2},3 -> {w / 2},0 v="$v$"\nR1 0,0 -> 0,-3 "$R$" i="$i$"'
        for w in range(2, 26)
    ]
    render = schematic.render_svg.__wrapped__  # bypass the cache so every call really draws
    expected = [render(s) for s in sources]
    interval = sys.getswitchinterval()
    sys.setswitchinterval(1e-6)  # switch threads often so overlapping renders actually interleave
    try:
        for _ in range(3):
            with ThreadPoolExecutor(len(sources)) as pool:
                assert list(pool.map(render, sources)) == expected
    finally:
        sys.setswitchinterval(interval)
