"""Reorganize the verified course content around the instructor's Week 1–5 midterm scope."""

import copy
import json
import uuid
from fractions import Fraction
from itertools import product

from lib import OUT, Doc, S, circuit, cite, node, wire

TARGETS = {
    1: "a20960cb-7622-43c0-8daf-c706abd4b2e5",
    2: "120cfcb1-7126-46ec-9e94-3780eabbd8cd",
    3: "22833a28-26bd-49d0-abf5-658b3a0fe16b",
    4: "eb495e0b-1700-4b5f-8c8c-0bc5ed5654f2",
    5: "94194019-710f-4708-a832-334dfe2a94ce",
    6: "24cd951d-3484-4122-931d-a6e1bf806334",
    7: "d89deb82-07b2-4f37-8601-a1ef1dca50e3",
    8: "11731286-840b-48ab-aec2-532865e6dcc1",
    9: "a693d4b9-a30c-4e29-b5e1-ee1f0ec71380",
}


def scope_citation(exclusions=False):
    citations = json.loads((OUT / "midterm-scope.json").read_text(encoding="utf-8"))
    return [citations["exclusions" if exclusions else "exam"]]


def append(doc, blocks):
    doc.blocks.extend(copy.deepcopy(blocks))


def heading(doc, text, cites=()):
    doc.H(text, cites)


def new(number, title, topics, main=False):
    doc = Doc(number, title, topics)
    doc.title = f"{number:02} · {title}"
    doc.target_document_id = TARGETS[number]
    if main:
        doc.P(
            "**Midterm: Weeks 1–5.** This is one of the three main study sections for the 40-minute October 29 midterm.",
            scope_citation(),
        )
    else:
        doc.P(
            "**Later study — outside this midterm study set.** Keep this material for subsequent assessments; prioritize notes 01–03 now.",
            scope_citation(),
        )
    return doc


def section1(original):
    d = new(1, "Binary Numbers — Midterm", ["number_systems", "binary_numbers", "base_conversion"], True)
    append(d, original.blocks[:19])
    d.blocks[1]["text"] = "1. Place value and unsigned binary"
    next(b for b in d.blocks if b.get("text", "").startswith("Topic 2:"))["text"] = (
        "2. Decimal ↔ binary, including fractions"
    )
    heading(d, "3. Hexadecimal, including fractions", cite("N", 41, 42, 43))
    d.P(
        "Each hexadecimal digit corresponds to exactly four bits because $16=2^4$. A–F represent decimal 10–15.\n\nStart at the radix point and group outward. Add leading zeroes on the integer side or trailing zeroes on the fraction side; never insert padding next to the radix point.",
        cite("N", 41, 42, 43),
    )
    append(d, [original.blocks[21]])
    d.X(
        "Binary to hex: pad from the radix point",
        r"Convert $(10110110.101)_2$ to hexadecimal.",
        [
            S("Group each side in fours.", r"1011\;0110.1010"),
            S("Translate each group independently.", r"(10110110.101)_2=(\mathrm{B6.A})_{16}"),
        ],
        r"$(\mathrm{B6.A})_{16}$. Padding .101 to .1010 preserves the fraction; .0101 would change it.",
        cite("N", 42, 43),
    )
    d.X(
        "Decimal fraction directly to hex",
        r"Convert $(13.625)_{10}$ to hexadecimal, then check it in decimal.",
        [
            S("The integer 13 is the hex digit D."),
            S(
                "Multiply the fractional part by 16 and keep its integer part.",
                r"0.625(16)=10.0\quad\Rightarrow\quad.\mathrm A",
            ),
            S("Check the positional weights.", r"(\mathrm{D.A})_{16}=13+10(16^{-1})=13.625"),
        ],
        r"$(\mathrm{D.A})_{16}$. Read fractional hex digits in the order generated.",
    )
    d.Q(
        "Try it: reverse a fractional hex value",
        r"Convert $(2\mathrm{F}.4)_{16}$ to decimal and binary.",
        [
            S("Weight the integer and fractional digits.", r"2(16)+15+4/16=47.25"),
            S("Replace each hex digit with four bits.", r"0010\;1111.0100"),
        ],
        r"$47.25$ and $(101111.01)_2$.",
    )
    assert Fraction(10, 16) == Fraction(5, 8)
    assert int("B6", 16) + Fraction(10, 16) == 182 + Fraction(5, 8)
    assert int("2F", 16) + Fraction(4, 16) == Fraction(189, 4)
    return d


def section2(logic, synthesis):
    b, c = logic.blocks, synthesis.blocks
    d = new(
        2,
        "Introduction to Logic Circuits — Midterm",
        ["logic_gates", "boolean_algebra", "truth_tables", "logic_synthesis", "canonical_forms", "nand_nor"],
        True,
    )
    heading(d, "1. Descriptions, truth tables, and gate drawings", cite("L", 7, 11, 14, 52))
    append(d, [b[1]])
    table = copy.deepcopy(b[2])
    table["columns"] = table["columns"][:-1]
    table["rows"] = [r[:-1] for r in table["rows"]]
    append(d, [table])
    d.P(
        "**NAND** complements an AND; **NOR** complements an OR. A small bubble at a gate output means inversion.",
        cite("L", 47, 48),
    )
    append(d, [b[6]])
    d.X(
        "A description becomes a truth table",
        "An indicator turns on when at least two of three inputs A,B,C are 1. Derive its truth table and an SOP.",
        [
            S("Enumerate all eight input assignments in binary order."),
            S("The qualifying rows are 011,101,110,111.", r"F=\sum m(3,5,6,7)"),
            S("Each pair of high inputs guarantees the condition.", r"F=AB+AC+BC"),
        ],
        r"$F=AB+AC+BC$; the table below checks every input row.",
    )
    d.T(["A", "B", "C", "F"], [[a, bb, cc, int(a + bb + cc >= 2)] for a, bb, cc in product((0, 1), repeat=3)])
    append(d, b[4:6])
    append(d, [b[7]])
    light = copy.deepcopy(c[20])
    light["steps"] = [
        light["steps"][0],
        S(
            "Every 1 row becomes one minterm.",
            r"F=\overline A\overline B C+\overline A B\overline C+A\overline B\overline C+ABC",
        ),
    ]
    light["answer"] = (
        r"$F=\sum m(1,2,4,7)$. This is the lecture’s three-switch light-controller specification."
    )
    append(d, [light])
    heading(d, "2. Timing diagrams: evaluate and reconstruct a function", cite("L", 19))
    append(d, b[8:10])
    d.P(
        "Treat each interval between input transitions as a truth-table row: read **all** inputs and F vertically at the same instant.\n\nFor an ideal combinational function, a repeated input combination must give the same output. A waveform that never visits an input combination does not determine that row."
    )
    d.X(
        "Work backward from the timing diagram",
        "For the A,B,F waveforms immediately above, recover a Boolean expression for F.",
        [
            S("Read the intervals left to right: AB=00,01,10,11 and F=1,1,0,1."),
            S("Write minterms for the 1 rows.", r"F=\overline A\overline B+\overline A B+AB"),
            S(
                "Combine the first two terms, then absorb the redundant literal.",
                r"F=\overline A+AB=\overline A+B",
            ),
        ],
        r"$F=\overline A+B$. The reconstructed function matches the gate network.",
        cite("L", 19, 20),
    )
    d.Q(
        "Try it: a waveform leaves a row unseen",
        "A waveform visits AB=00,01,11 with outputs 0,1,1. Can you claim F=B for every input?",
        [
            S("F=B matches the three observed rows."),
            S("AB=10 was not observed. Its output could be 0 or 1 without contradicting the waveform."),
        ],
        "No. F=B is one consistent possibility, but the waveform does not uniquely determine F at AB=10.",
    )
    heading(d, "3. Boolean algebra and complementing a function", cite("L", 23, 24, 25))
    append(d, b[12:19])
    consensus = next(x for x in d.blocks if x.get("title", "").startswith("Consensus:"))
    consensus["answer"] = r"$F=AB+\overline A C$. The product BC adds no new 1 rows."
    append(d, b[20:24])
    append(d, [b[27]])
    heading(d, "4. Venn diagrams", cite("L", 29, 30, 31))
    append(d, b[24:27])
    d.F(
        {
            "kind": "venn",
            "title": "Union restricted to outside C",
            "variables": ["A", "B", "C"],
            "shaded": [2, 4, 6],
        },
        "The shaded area lies inside A or B, while remaining outside C.",
    )
    d.X(
        "Read the expression from shaded regions",
        "In the three-circle diagram above, the shaded regions are inside A or B and outside C. Write the function.",
        [
            S("Inside either A or B gives the union A+B."),
            S("Outside C contributes NOT C, joined by AND.", r"F=(A+B)\overline C"),
        ],
        r"$(A+B)\overline C=A\overline C+B\overline C$. The regions are ABC=010,100,110.",
    )
    heading(d, "5. Canonical SOP/POS and AND–OR/OR–AND drawings", cite("L", 34, 38, 39, 43))
    append(d, c[1:9])
    d.P(
        "To draw an **SOP**, generate any complemented literals, place one AND gate per product, then OR their outputs.\n\nTo draw a **POS**, place one OR gate per sum, then AND their outputs. A literal used alone may connect directly; a complement bar must still be implemented."
    )
    # Draw the same algebraically reduced SOP from the lecture, rather than silently using a map.
    d.F(
        circuit(
            "SOP: NOT B C + A NOT C",
            [
                node("B", "INPUT", 70, 85),
                node("C", "INPUT", 70, 245),
                node("A", "INPUT", 260, 325),
                node("NB", "NOT", 260, 85),
                node("NC", "NOT", 260, 245),
                node("P", "AND", 455, 135),
                node("Q", "AND", 455, 285),
                node("G", "OR", 650, 210),
                node("F", "OUTPUT", 835, 210),
            ],
            [
                wire("B.out", "NB.0"),
                wire("C.out", "NC.0"),
                wire("NB.out", "P.0"),
                wire("C.out", "P.1", [[180, 245], [180, 145]]),
                wire("A.out", "Q.0", [[365, 325], [365, 275]]),
                wire("NC.out", "Q.1"),
                wire("P.out", "G.0"),
                wire("Q.out", "G.1"),
                wire("G.out", "F.0"),
            ],
        ),
        "F = NOT B C + A NOT C: two AND products feeding an OR.",
        cite("L", 40),
    )
    heading(d, "6. SOP → NAND–NAND; POS → NOR–NOR", cite("L", 47, 48, 49, 50, 51))
    append(d, c[10:16])
    d.F(
        circuit(
            "NOR-only realization",
            [
                node("A", "INPUT", 70, 85),
                node("B", "INPUT", 70, 165),
                node("C", "INPUT", 70, 285),
                node("NC", "NOR", 260, 285),
                node("U", "NOR", 450, 125),
                node("V", "NOR", 450, 245),
                node("G", "NOR", 645, 185),
                node("F", "OUTPUT", 830, 185),
            ],
            [
                wire("A.out", "U.0"),
                wire("B.out", "U.1"),
                wire("C.out", "NC.0"),
                wire("C.out", "NC.1"),
                wire("B.out", "V.0", [[160, 165], [160, 235]]),
                wire("NC.out", "V.1"),
                wire("U.out", "G.0"),
                wire("V.out", "G.1"),
                wire("G.out", "F.0"),
            ],
        ),
        "F=(A+B)(B+NOT C). NC uses tied NOR inputs; U and V complement the two sum terms.",
        cite("L", 51),
    )
    for a, bb, cc in product((0, 1), repeat=3):
        assert (a + bb + cc >= 2) == bool((a and bb) or (a and cc) or (bb and cc))
        assert ((a or bb) and not cc) == ((4 * a + 2 * bb + cc) in {2, 4, 6})
        u = not (a or bb)
        v = not (bb or not cc)
        assert not (u or v) == ((a or bb) and (bb or not cc))
    return d


def section3(technology):
    b = technology.blocks
    d = new(
        3,
        "Implementation Technology — Midterm (Week 5)",
        ["implementation_technology", "cmos", "transistor_switches"],
        True,
    )
    d.P(
        "**PS2 preparation:** Q1 and Q3–Q5 are in this study set. **Skip Q2 and Q6–Q8 for this midterm.**",
        scope_citation(True),
    )
    heading(d, "1. Transistor switches and resistor-load NMOS gates", cite("C", 6, 8, 9, 10, 11, 12, 13))
    append(d, [b[1], b[6], b[7]])
    d.T(
        ["NMOS pull-down arrangement", "Conducts when", "Output with a pull-up"],
        [
            ["One switch A", "A=1", r"$F=\overline A$ (NOT)"],
            ["A and B in series", "A=B=1", r"$F=\overline{AB}$ (NAND)"],
            ["A and B in parallel", "Either input is 1", r"$F=\overline{A+B}$ (NOR)"],
        ],
        cite("C", 11, 12, 13),
    )
    d.add(
        "schematic",
        cite("C", 12),
        source="""terminal 0,6 "VDD" above
R1 0,6 -> 0,4 "pull-up"
S1 0,4 -> 0,2 "A"
S2 0,2 -> 0,0 "B"
wire 0,4 -> 2,4
terminal 2,4 "F" right
ground 0,0""",
        caption="NMOS NAND in the ideal-switch model: A/B close for input 1. Only A=B=1 completes the ground path.",
    )
    append(d, [b[8]])
    heading(d, "2. Complementary CMOS: NOT, NAND, NOR, AND, OR", cite("C", 16, 17, 18, 19, 21, 23))
    append(d, b[10:16])
    d.F(
        {"kind": "cmos", "title": "CMOS NOR", "pdn": {"parallel": [{"gate": "A"}, {"gate": "B"}]}},
        "Parallel NMOS pull down when either input is 1. Series PMOS pull up only for A=B=0.",
        cite("C", 21),
    )
    d.P(
        "For basic complementary static CMOS, an n-input NAND/NOR uses n NMOS + n PMOS. An AND/OR adds a two-transistor inverter after the corresponding NAND/NOR. Count the gates actually drawn before considering a cheaper equivalent implementation.",
        cite("C", 23),
    )
    d.X(
        "PS2 Q1: count the circuit that was given",
        "The supplied gate drawing has three NOTs, four 3-input ANDs, and one 4-input OR. How many transistors implement those gates in basic static CMOS?",
        [
            S("The NOTs each use 2 transistors.", r"3(2)=6"),
            S("Each 3-input AND is a 3-input NAND followed by an inverter.", r"4(2\cdot3+2)=32"),
            S("The 4-input OR is a 4-input NOR followed by an inverter.", r"2\cdot4+2=10"),
            S("Add the counts for this drawn realization.", r"N=6+32+10=48"),
        ],
        "48 transistors. Replacing the drawing with a different equivalent circuit answers a different question.",
        cite("P2", 1),
    )
    heading(d, "3. Function → pull-down → dual pull-up", cite("C", 24, 25))
    append(d, b[16:19])
    d.X(
        "PS2 Q3: complete the missing PMOS half",
        r"The given PDN has NMOS B in parallel with the series path A–C, where A=x1, B=x2, C=x3. Derive the PUN and F.",
        [
            S("Write the condition for a complete ground path.", r"G=B+AC"),
            S("The output is the complement of the ground-path condition.", r"F=\overline{B+AC}"),
            S(
                "Dualize: PMOS B is in series with parallel PMOS A and C.",
                r"F=\overline B(\overline A+\overline C)",
            ),
        ],
        "Three NMOS and three PMOS. The dual network keeps the same gate labels; PMOS already conducts on 0.",
        cite("P2", 1),
    )
    d.F(
        {
            "kind": "cmos",
            "title": "PS2 Q3: complete complementary gate",
            "pdn": {"parallel": [{"gate": "B"}, {"series": [{"gate": "A"}, {"gate": "C"}]}]},
        },
        "A=x1, B=x2, C=x3. Compare the dual PMOS network with the supplied partial drawing.",
        cite("P2", 1),
    )
    d.Q(
        "PS2 Q5: simplify first, then draw CMOS",
        r"$F(A,B,C,D)=\sum m(0,1,2,4,6,8,10,12,14)$. Find the minimum SOP and the corresponding static CMOS network.",
        [
            S("All eight even rows have D=0 and contribute NOT D."),
            S(
                "The only remaining 1 is row 1; combine it with row 0 by Boolean algebra.",
                r"F=\overline D+\overline A\overline B\overline C",
            ),
            S("Complement before drawing the PDN.", r"\overline F=D(A+B+C)"),
            S("Use NMOS D in series with parallel A,B,C; dualize for the PUN."),
        ],
        "Four NMOS and four PMOS. PUN: PMOS D in parallel with series PMOS A,B,C. The eight-transistor complex gate directly implements F.",
        cite("P2", 2),
    )
    heading(d, "4. CMOS drawing → function → truth table", cite("P2", 2))
    d.P(
        "Read the **NMOS half** first: start at F and find every complete path to ground. Multiply gate conditions along a series path and OR parallel paths, then complement once to obtain F.\n\nCheck with the PMOS half: a pull-up path must exist exactly when F=1. A complemented gate label is a signal name, not an instruction to complement the final output twice."
    )
    d.F(
        {
            "kind": "cmos",
            "title": "PS2 Q4: interpret this CMOS circuit",
            "pdn": {
                "series": [
                    {"gate": "A"},
                    {"parallel": [{"gate": "D"}, {"series": [{"gate": "B"}, {"gate": "C"}]}]},
                ]
            },
        },
        "Redrawn from PS2 Q4: A=x1, B=x2, C=x3, D=x4.",
        cite("P2", 2),
    )
    d.X(
        "PS2 Q4: derive the output and canonical SOP",
        "Read the four-input CMOS circuit above. Give its output function, truth table, and canonical 1-row indices.",
        [
            S("A is in series with the parallel choice D or BC.", r"G=A(D+BC)"),
            S("A conducting PDN makes the output zero.", r"F=\overline{A(D+BC)}"),
            S(
                "Complement using De Morgan to check the PUN.",
                r"F=\overline A+\overline D(\overline B+\overline C)",
            ),
            S(
                "All A=0 rows are 1; for A=1, only BCD=000,010,100 remain high.",
                r"F=\sum m(0,1,2,3,4,5,6,7,8,10,12)",
            ),
        ],
        "The table below gives every row. Expand the listed minterms if a full canonical SOP is requested; each minterm must include A,B,C,D.",
        cite("P2", 2),
    )
    d.T(
        ["A", "B", "C", "D", "F"],
        [
            [a, bb, cc, dd, int(not (a and (dd or (bb and cc))))]
            for a, bb, cc, dd in product((0, 1), repeat=4)
        ],
        cite("P2", 2),
    )
    d.E(r"m_{10}=A\overline B C\overline D")
    d.P(
        "For example, row 10 is 1010, so its full minterm is the expression above. For the whole function, OR the minterms at all eleven listed 1 rows."
    )
    for a, bb, cc, dd in product((0, 1), repeat=4):
        m = 8 * a + 4 * bb + 2 * cc + dd
        assert bool(not dd or (not a and not bb and not cc)) == (m in {0, 1, 2, 4, 6, 8, 10, 12, 14})
        assert not (a and (dd or bb and cc)) == (m in {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12})
    return d


def later4(numbers, logic, synthesis, technology):
    d = new(
        4,
        "Later · VHDL, Voltage Levels, and Implementation Extras",
        ["vhdl", "implementation_technology", "programmable_logic"],
    )
    heading(d, "VHDL and digital design flow", cite("L", 55, 56, 57, 58, 59))
    append(d, synthesis.blocks[17:20])
    append(d, synthesis.blocks[21:])
    heading(d, "XOR and parity extensions")
    append(d, [logic.blocks[2], logic.blocks[3], logic.blocks[10], synthesis.blocks[20]])
    heading(d, "Voltage thresholds and noise margin", cite("C", 4, 5))
    append(d, technology.blocks[1:6])
    heading(d, "Programmable logic, LUTs, and physical limits", cite("C", 2))
    append(d, technology.blocks[20:])
    heading(d, "Other number bases: octal and base 4", cite("N", 41, 42, 43))
    append(d, [numbers.blocks[20]])
    append(d, numbers.blocks[22:])
    return d


def reorganize(originals):
    docs = [
        section1(originals[1]),
        section2(originals[2], originals[3]),
        section3(originals[4]),
        later4(originals[1], originals[2], originals[3], originals[4]),
    ]
    for n in range(5, 10):
        original = originals[n]
        title = original.title.split(" · ", 2)[-1]
        d = new(n, "Later · " + title, original.topics)
        append(d, original.blocks)
        docs.append(d)
    for doc in docs:
        for i, b in enumerate(doc.blocks):
            b["id"] = str(uuid.uuid5(uuid.NAMESPACE_URL, f"elec271/midterm-v2/{doc.number}/{i}"))
    return docs
