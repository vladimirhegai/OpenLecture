"""ELEC 271 "Midterm Practice Problems": exam-style problems for the Oct 29 midterm, one hidden solution per part.

    .venv/Scripts/python.exe scripts/notes271/practice.py            # check every answer, write out/practice.json
    .venv/Scripts/python.exe scripts/notes271/practice.py --publish  # also create / revise the course document

Wording follows the 2025 midterm, PS1, PS2, Tutorial Week 2 and the Chapter 2 practice questions; marks are in
[brackets]. Every number, function, waveform, gate network and CMOS network below is checked at build time.
The exam's formula sheet is shown (collapsed) under each question that uses it.
Write this file with the Write tool, never a shell heredoc (heredocs collapse \\ in LaTeX).
"""

import copy
from decimal import Decimal
from fractions import Fraction
from itertools import product

from lib import Doc, circuit, cite, figure, logicsteps, node, wire
from midterm import callout, relabel, regate, rows, sub

from open_lecture import schematic

TARGET = "e736b151-064d-40fa-bda2-65764a925a2a"  # the live document; publishing revises it in place


# ---------------------------------------------------------------- checking helpers
def run(spec, **inputs):
    """Simulate a circuit figure; inputs by node id (x1, x2, x3)."""
    nodes = {n["id"]: n for n in spec["nodes"]}
    source = {w["end"]: w["start"].split(".")[0] for w in spec["wires"]}

    def value(i):
        n = nodes[i]
        if n["gate"] == "INPUT":
            return inputs[i]
        count = 1 if n["gate"] in ("NOT", "OUTPUT") else n.get("inputs", 2)
        v = [value(source[f"{i}.{k}"]) for k in range(count)]
        return {
            "AND": all(v), "OR": any(v), "NAND": not all(v), "NOR": not any(v), "NOT": not v[0], "OUTPUT": v[0],
        }[n["gate"]]

    return int(value(next(i for i, n in nodes.items() if n["gate"] == "OUTPUT")))


def circuit_rows(spec):
    return {i for i, (a, b, c) in enumerate(product((0, 1), repeat=3)) if run(spec, x1=a, x2=b, x3=c)}


def conducts(net, env):
    if "gate" in net:
        return env[net["gate"]]
    return (all if "series" in net else any)(conducts(n, env) for n in net.get("series") or net["parallel"])


def cmos_rows(spec):
    return {
        i
        for i, (a, b, c) in enumerate(product((0, 1), repeat=3))
        if not conducts(spec["pdn"], dict(x1=a, x2=b, x3=c))
    }


def dec(x):
    """Exact decimal text of a Fraction with a finite decimal expansion."""
    return format(Decimal(x.numerator) / Decimal(x.denominator), "f")


def md(columns, table):
    lines = ["| " + " | ".join(columns) + " |", "|" + "---|" * len(columns)]
    return "\n".join(lines + ["| " + " | ".join(str(c) for c in r) + " |" for r in table])


def divide(n):
    out = []
    while n:
        out.append([f"{n} / 2", n // 2, n % 2])
        n //= 2
    return out


def double(x, places):
    out = []
    for _ in range(places):
        result = dec(2 * x)
        out.append([f"{dec(x)} × 2", result if "." in result else result + ".0", int(2 * x >= 1)])
        x = 2 * x - int(2 * x >= 1)
    return out


# ---------------------------------------------------------------- note helpers
def problem(d, n, title, marks, source, prompt, cites=()):
    sub(d, f"Problem {n} · {title} [{marks} marks]")
    d.P(f"*{source}*\n\n{prompt.strip()}", cites)


def solution(d, part, text):
    d.add("solution", (), title=f"Solution {part}", text=text.strip(), collapsed=True)


def sheet(d, name):
    title, page, text = SHEETS[name]
    d.add("solution", cite("FORM", page), title=f"Formula sheet: {title}", text=text.strip(), collapsed=True)


SHEETS = {
    "numbers": (
        "binary numbers (given in the exam)",
        1,
        r"""
Base $k$ to decimal, with digits $b_i$ ($n$ digits before the point, $m$ after):

$$
\text{Value}=\sum_{i=-m}^{n-1} b_i\,k^i
$$

"""
        + md(["Hex"] + list("0123456789ABCDEF"), [["Binary"] + [format(i, "04b") for i in range(16)]]),
    ),
    "boolean": (
        "Boolean algebra (given in the exam)",
        2,
        r"""
| # | (a) | (b) | Name |
|---|---|---|---|
| 5 | $x\cdot 0=0$ | $x+1=1$ | |
| 6 | $x\cdot 1=x$ | $x+0=x$ | |
| 7 | $x\cdot x=x$ | $x+x=x$ | |
| 8 | $x\cdot\bar x=0$ | $x+\bar x=1$ | |
| 9 | $\bar{\bar x}=x$ | | |
| 10 | $xy=yx$ | $x+y=y+x$ | Commutative |
| 11 | $x(yz)=(xy)z$ | $x+(y+z)=(x+y)+z$ | Associative |
| 12 | $x(y+z)=xy+xz$ | $x+yz=(x+y)(x+z)$ | Distributive |
| 13 | $x+xy=x$ | $x(x+y)=x$ | Absorption |
| 14 | $xy+x\bar y=x$ | $(x+y)(x+\bar y)=x$ | Combining |
| 15 | $\overline{xy}=\bar x+\bar y$ | $\overline{x+y}=\bar x\,\bar y$ | DeMorgan |
| 16 | $x+\bar xy=x+y$ | $x(\bar x+y)=xy$ | |
| 17 | $xy+yz+\bar xz=xy+\bar xz$ | $(x+y)(y+z)(\bar x+z)=(x+y)(\bar x+z)$ | Consensus |
""",
    ),
    "minterms": (
        "minterms and maxterms (given in the exam)",
        2,
        md(
            ["Row", "$x_1x_2x_3$", "Minterm $m_i$", "Maxterm $M_i$"],
            [
                [
                    i,
                    f"{a}{b}{c}",
                    "$m_" + str(i) + "=" + "".join(f"x_{k}" if v else f"\\bar x_{k}" for k, v in enumerate((a, b, c), 1)) + "$",
                    "$M_" + str(i) + "=" + "+".join(f"\\bar x_{k}" if v else f"x_{k}" for k, v in enumerate((a, b, c), 1)) + "$",
                ]
                for i, (a, b, c) in enumerate(product((0, 1), repeat=3))
            ],
        )
        + "\n\nAlso on the sheet: $\\overline{m_i}=M_i$.",
    ),
    "nandnor": (
        "NAND and NOR (given in the exam)",
        2,
        r"""
- **NAND gate:** $\overline{x_1x_2}=\bar x_1+\bar x_2$. A NAND is an OR with bubbles on its inputs.
- **NOR gate:** $\overline{x_1+x_2}=\bar x_1\,\bar x_2$. A NOR is an AND with bubbles on its inputs.
- **NOT:** a NAND or a NOR with both inputs tied together.
- The sheet also draws **SOP → NAND–NAND** and **POS → NOR–NOR** networks.
""",
    ),
    "transistors": (
        "NMOS and PMOS (given in the exam)",
        3,
        r"""
| | Gate at $V_{DD}$ (logic 1) | Gate at 0 V (logic 0) |
|---|---|---|
| **NMOS** | on: closed switch, pulls the drain **down** to ground | off: open switch |
| **PMOS** | off: open switch | on: closed switch, pulls the drain **up** to $V_{DD}$ |
""",
    ),
}


# ---------------------------------------------------------------- circuits used in questions and solutions
PRIME_SOP = circuit(
    "f = NOT x1 x2 + x1 x3",
    [
        node("x2", "INPUT", 70, 90, label="x₂"),
        node("x1", "INPUT", 70, 200, label="x₁"),
        node("x3", "INPUT", 70, 320, label="x₃"),
        node("N1", "NOT", 260, 200, label="x̄₁"),
        node("A1", "AND", 450, 120, label="x̄₁x₂"),
        node("A2", "AND", 450, 290, label="x₁x₃"),
        node("G", "OR", 640, 200, label="x̄₁x₂ + x₁x₃"),
        node("f", "OUTPUT", 820, 200, label="f"),
    ],
    [
        wire("x1.out", "N1.0"),
        wire("x2.out", "A1.0"),
        wire("N1.out", "A1.1"),
        wire("x1.out", "A2.0", [[160, 200], [160, 280]]),
        wire("x3.out", "A2.1"),
        wire("A1.out", "G.0"),
        wire("A2.out", "G.1"),
        wire("G.out", "f.0"),
    ],
)

Q7 = circuit(
    "Problem 7",
    [
        node("x1", "INPUT", 70, 90, label="x₁"),
        node("x2", "INPUT", 70, 200, label="x₂"),
        node("x3", "INPUT", 70, 320, label="x₃"),
        node("G1", "NAND", 330, 100, label="g₁"),
        node("G2", "OR", 330, 300, label="g₂"),
        node("F", "AND", 560, 200, label=" "),
        node("f", "OUTPUT", 740, 200, label="f"),
    ],
    [
        wire("x1.out", "G1.0"),
        wire("x2.out", "G1.1", [[180, 200], [180, 110]]),
        wire("x2.out", "G2.0", [[180, 200], [180, 290]]),
        wire("x3.out", "G2.1"),
        wire("G1.out", "F.0"),
        wire("G2.out", "F.1"),
        wire("F.out", "f.0"),
    ],
)

# Problem 9(a): AND–OR → NAND–NAND for f = x2 + NOT x1 NOT x3
Q9_AND_OR = circuit(
    "f = x2 + NOT x1 NOT x3",
    [
        node("x2", "INPUT", 70, 90, label="x₂"),
        node("x1", "INPUT", 70, 200, label="x₁"),
        node("x3", "INPUT", 70, 320, label="x₃"),
        node("N1", "NOT", 260, 200, label="x̄₁"),
        node("N3", "NOT", 260, 320, label="x̄₃"),
        node("P", "AND", 450, 260, label="x̄₁x̄₃"),
        node("G", "OR", 640, 150, label="x₂ + x̄₁x̄₃"),
        node("f", "OUTPUT", 820, 150, label="f"),
    ],
    [
        wire("x1.out", "N1.0"),
        wire("x3.out", "N3.0"),
        wire("N1.out", "P.0"),
        wire("N3.out", "P.1", [[380, 320], [380, 270]]),
        wire("x2.out", "G.0", [[520, 90], [520, 140]]),
        wire("P.out", "G.1"),
        wire("G.out", "f.0"),
    ],
)
Q9_SWAPPED = regate(relabel(Q9_AND_OR, P="NOT(x̄₁x̄₃)", G="x̄₂ + x̄₁x̄₃  ✗"), P="NAND", G="NAND")
Q9_FLIPPED = copy.deepcopy(Q9_SWAPPED)
Q9_FLIPPED["nodes"].append(node("N2", "NOT", 260, 90, label="x̄₂"))
Q9_FLIPPED["wires"] = [w for w in Q9_FLIPPED["wires"] if w["end"] != "G.0"] + [
    wire("x2.out", "N2.0"),
    wire("N2.out", "G.0", [[520, 90], [520, 140]]),
]
Q9_FLIPPED = relabel(Q9_FLIPPED, G="x₂ + x̄₁x̄₃  ✓")
Q9_NANDS = regate(
    relabel(Q9_FLIPPED, N1="x̄₁ (tied NAND)", N2="x̄₂ (tied NAND)", N3="x̄₃ (tied NAND)"), N1="NAND", N2="NAND", N3="NAND"
)
Q9_NANDS["wires"] += [wire("x1.out", "N1.1"), wire("x2.out", "N2.1"), wire("x3.out", "N3.1")]

# Problem 9(b): read a NAND-only circuit
Q9B = circuit(
    "Problem 9(b)",
    [
        node("x2", "INPUT", 70, 90, label="x₂"),
        node("x1", "INPUT", 70, 230, label="x₁"),
        node("x3", "INPUT", 70, 380, label="x₃"),
        node("N1", "NAND", 260, 230),
        node("N2", "NAND", 450, 120),
        node("N3", "NAND", 450, 330),
        node("F", "NAND", 640, 225, label=" "),
        node("f", "OUTPUT", 820, 225, label="f"),
    ],
    [
        wire("x1.out", "N1.0"),
        wire("x1.out", "N1.1"),
        wire("x2.out", "N2.0"),
        wire("N1.out", "N2.1"),
        wire("x1.out", "N3.0", [[160, 230], [160, 320]]),
        wire("x3.out", "N3.1"),
        wire("N2.out", "F.0"),
        wire("N3.out", "F.1"),
        wire("F.out", "f.0"),
    ],
)

# Problem 10(a): OR–AND → NOR–NOR for f = (x1 + NOT x3)(NOT x1 + x2)
Q10_OR_AND = circuit(
    "f = (x1 + NOT x3)(NOT x1 + x2)",
    [
        node("x3", "INPUT", 70, 90, label="x₃"),
        node("x1", "INPUT", 70, 200, label="x₁"),
        node("x2", "INPUT", 70, 380, label="x₂"),
        node("N3", "NOT", 260, 90, label="x̄₃"),
        node("N1", "NOT", 260, 290, label="x̄₁"),
        node("U", "OR", 450, 120, label="x₁ + x̄₃"),
        node("V", "OR", 450, 300, label="x̄₁ + x₂"),
        node("G", "AND", 640, 210, label="(x₁ + x̄₃)(x̄₁ + x₂)"),
        node("f", "OUTPUT", 860, 210, label="f"),
    ],
    [
        wire("x3.out", "N3.0"),
        wire("N3.out", "U.0", [[330, 90], [330, 110]]),
        wire("x1.out", "U.1", [[370, 200], [370, 130]]),
        wire("x1.out", "N1.0", [[160, 200], [160, 290]]),
        wire("N1.out", "V.0"),
        wire("x2.out", "V.1", [[360, 380], [360, 310]]),
        wire("U.out", "G.0"),
        wire("V.out", "G.1"),
        wire("G.out", "f.0"),
    ],
)
Q10_SWAPPED = regate(
    relabel(Q10_OR_AND, U="NOT(x₁ + x̄₃)", V="NOT(x̄₁ + x₂)", G="(x₁ + x̄₃)(x̄₁ + x₂)  ✓"), U="NOR", V="NOR", G="NOR"
)
Q10_NORS = regate(relabel(Q10_SWAPPED, N1="x̄₁ (tied NOR)", N3="x̄₃ (tied NOR)"), N1="NOR", N3="NOR")
Q10_NORS["wires"] = [w for w in Q10_NORS["wires"] if w["end"] != "N1.0"] + [
    wire("x3.out", "N3.1"),
    wire("x1.out", "N1.0", [[160, 200], [160, 280]]),
    wire("x1.out", "N1.1", [[160, 200], [160, 300]]),
]

# Problem 10(b): g = x1x2 + NOT x3 = (x1 + NOT x3)(x2 + NOT x3), NOR only
Q10B = circuit(
    "NOR only: g = (x1 + NOT x3)(x2 + NOT x3)",
    [
        node("x1", "INPUT", 70, 90, label="x₁"),
        node("x3", "INPUT", 70, 200, label="x₃"),
        node("x2", "INPUT", 70, 330, label="x₂"),
        node("N3", "NOR", 260, 200, label="x̄₃"),
        node("U", "NOR", 450, 110, label="NOT(x₁ + x̄₃)"),
        node("V", "NOR", 450, 290, label="NOT(x₂ + x̄₃)"),
        node("G", "NOR", 640, 200, label="g"),
        node("g", "OUTPUT", 820, 200, label="g"),
    ],
    [
        wire("x3.out", "N3.0"),
        wire("x3.out", "N3.1"),
        wire("x1.out", "U.0"),
        wire("N3.out", "U.1"),
        wire("N3.out", "V.0"),
        wire("x2.out", "V.1"),
        wire("U.out", "G.0"),
        wire("V.out", "G.1"),
        wire("G.out", "g.0"),
    ],
)

CMOS_A = {"kind": "cmos", "title": "f = NOT x1 NOT x2 + NOT x3", "pdn": {"series": [{"parallel": [{"gate": "x1"}, {"gate": "x2"}]}, {"gate": "x3"}]}}
CMOS_B = {"kind": "cmos", "title": "Problem 11(b)", "pdn": {"parallel": [{"series": [{"gate": "x1"}, {"gate": "x2"}]}, {"gate": "x3"}]}}
NMOS_NOR = """```schematic
terminal 0,6 "VDD" above
R1 0,6 -> 0,4 "R"
wire 0,4 -> 2,4
S1 0,4 -> 0,0 "x1"
S2 2,4 -> 2,0 "x2"
wire 0,0 -> 2,0
ground 0,0
wire 2,4 -> 4,4
terminal 4,4 "f" right
```

*Ideal-switch model: each NMOS closes when its input is 1.*"""

Q8_ORDER = [0, 4, 6, 2, 3, 7, 5, 1]  # the rows the inputs visit, slot by slot
Q8_ONES = {0, 1, 4, 6, 7}


def bits(i):
    return [(i >> 2) & 1, (i >> 1) & 1, i & 1]


def build():
    d = Doc(10, "Midterm Practice Problems", ["number_systems", "boolean_algebra", "canonical_forms", "nand_nor", "implementation_technology"])
    d.title = "Midterm Practice Problems"
    d.slug = "practice"
    d.document_type = "practice_set"
    if TARGET:
        d.target_document_id = TARGET

    d.P(
        "Exam-style practice for the **October 29 midterm** (40 minutes, Weeks 1–5). "
        "The wording copies the 2025 midterm, the problem sets and the tutorial, so nothing here should surprise you on the day.",
        cite("MID", 1),
    )
    d.add(
        "list",
        (),
        ordered=False,
        items=[
            "**Marks are in [brackets].** The 2025 midterm was 15 marks in 40 minutes, so budget about 2½ minutes per mark.",
            "**Do each part on paper first**, then open its *Solution*. Every part has its own.",
            "**The exam's formula sheet** sits under each question that needs it (collapsed). Practise with it, not from memory.",
            "Each solution ends with the note section to review if you got it wrong.",
        ],
    )
    d.T(
        ["Exam topic (from the announcement)", "Problems"],
        [
            ["Binary ↔ decimal ↔ hex, with fractions", "1"],
            ["Boolean algebra: proofs and simplifying", "2, 3 (also 4d, 5, 7b)"],
            ["Truth table from a description", "4"],
            ["Canonical SOP / POS, $\\sum m$ / $\\prod M$", "4, 5b, 8, 9a, 10a"],
            ["Complementing a function", "5"],
            ["Venn diagrams", "6"],
            ["Gates → function (working backward)", "7, 9b"],
            ["Timing diagrams, both directions", "7d, 8"],
            ["Drawing gate circuits", "4e, 9a, 10"],
            ["SOP → NAND–NAND, POS → NOR–NOR", "9, 10"],
            ["Transistor switches and NMOS gates", "11d"],
            ["CMOS: draw one, read one", "11a–c"],
        ],
        cite("FORM", 1),
    )
    callout(
        d,
        "**Timed run (15 marks, 40 minutes, like the real thing):** Problem 9(a) [6], 1(a) [2], 1(c) [2], 6(a) [2], 11(a) [3]. "
        "Set a timer, no peeking, then mark yourself with the solutions.",
        "tip",
    )

    # ------------------------------------------------------------ 1. numbers
    d.H("Binary numbers", cite("T", 1))
    problem(
        d,
        1,
        "Conversions",
        7,
        "Like past midterm Q2 and Tutorial Week 2 (1.1, 1.6, 1.8).",
        r"""
**1.** (a) Convert decimal 25.6875 to binary. Then write the result in hexadecimal. **[2]**

(b) Convert $(\mathrm{A7.4})_{16}$ to binary, then to decimal. **[2]**

(c) Calculate the binary equivalent of 0.1 out to six places. Then convert from binary to decimal. How close is the result to 0.1? **[2]**

(d) What is the minimum number of bits needed to represent $(300)_{10}$ and $(512)_{10}$ in binary? **[1]**
""",
        cite("MID", 3) + cite("T", 1),
    )
    sheet(d, "numbers")
    assert int("11001", 2) == 25 and Fraction(int("1011", 2), 16) == Fraction(6875, 10000)
    assert [r[2] for r in divide(25)][::-1] == [1, 1, 0, 0, 1]
    assert [r[2] for r in double(Fraction(6875, 10000), 4)] == [1, 0, 1, 1]
    solution(
        d,
        "(a)",
        r"""
**Integer part, 25:** divide by 2 and keep the remainders. Read them **bottom → top**.

"""
        + md(["Operation", "Quotient", "Remainder"], divide(25))
        + r"""

So $25 = 11001_2$.

**Fraction part, .6875:** multiply by 2 and keep the whole-number bit. Read them **top → bottom**. Stop when the fraction hits 0.

"""
        + md(["Operation", "Result", "Bit"], double(Fraction(6875, 10000), 4))
        + r"""

So $.6875 = .1011_2$, and

$$
25.6875 = 11001.1011_2
$$

**To hex:** group the bits in fours **starting at the point**, going outward. Pad the ends with 0s.

$$
\underbrace{0001}_{1}\;\underbrace{1001}_{9}\;.\;\underbrace{1011}_{B} = 19.\mathrm{B}_{16}
$$

**Check:** $1\times16+9+\tfrac{11}{16}=25.6875$ ✓

*Review: Note 01, Decimal → binary and Hexadecimal.*
""",
    )
    assert int("10100111", 2) == 167 and int("A7", 16) == 167
    solution(
        d,
        "(b)",
        r"""
**To binary:** each hex digit becomes exactly 4 bits (formula-sheet table).

$$
\mathrm{A}=1010,\quad 7=0111,\quad 4=0100 \;\Rightarrow\; (\mathrm{A7.4})_{16}=10100111.0100_2
$$

**To decimal:** add up the place values of the 1 bits.

$$
10100111.01_2 = 128+32+4+2+1+\tfrac14 = 167.25
$$

**Check straight from hex:** $10\times16+7+\tfrac{4}{16}=167.25$ ✓

*Review: Note 01, Binary → decimal and Hexadecimal.*
""",
    )
    tenth = double(Fraction(1, 10), 6)
    approx = Fraction(int("".join(str(r[2]) for r in tenth), 2), 64)
    assert "".join(str(r[2]) for r in tenth) == "000110" and approx == Fraction(3, 32)
    assert dec(Fraction(1, 10) - approx) == "0.00625"
    solution(
        d,
        "(c)",
        r"""
**Multiply by 2 six times** and keep the whole-number bits.

"""
        + md(["Operation", "Result", "Bit"], tenth)
        + r"""

So $0.1 \approx .000110_2$ (six places).

**Back to decimal:** only the $2^{-4}$ and $2^{-5}$ places are 1.

$$
.000110_2 = 2^{-4}+2^{-5} = 0.0625+0.03125 = 0.09375
$$

**How close:**

$$
0.1-0.09375 = 0.00625
$$

**Why it isn't exact:** the bits never stop. After the first 0, the pattern 0011 repeats forever (like $\tfrac13 = 0.333\ldots$ in decimal), so any fixed number of places is a little short.

*Review: Note 01, Extras (repeating fractions, past midterm Q2b).*
""",
    )
    assert 2**8 <= 300 < 2**9 and len(bin(300)) - 2 == 9 and len(bin(512)) - 2 == 10
    solution(
        d,
        "(d)",
        r"""
**Rule:** $n$ bits can count from 0 up to $2^n-1$. Find the smallest $n$ that reaches your number.

- **300:** $2^8=256$ is too small, $2^9=512$ is enough ($0$ to $511$). **9 bits.**
- **512:** 9 bits only reach 511. $512 = 1\underbrace{000000000}_{9\text{ zeros}}$ needs **10 bits**.

**Trap:** an exact power of two, $2^n$, always needs $n+1$ bits.

*Review: Note 01, Extras (bits needed).*
""",
    )

    # ------------------------------------------------------------ 2–3. Boolean algebra
    d.H("Boolean algebra", cite("PQ", 1))
    d.P("This is where most marks get lost, so here are the moves that keep showing up. Every one is on the formula sheet.")
    d.add(
        "list",
        cite("FORM", 2),
        ordered=False,
        items=[
            r"**Copy a term (7b), $x+x=x$.** A minterm can pair with two different neighbours if you write it twice.",
            r"**Consensus (17a).** Two terms with $x$ and $\bar x$, like $x_1x_3$ and $\bar x_1x_2$: multiply the leftovers ($x_3x_2$). If that term is also there, delete it.",
            r"**16a, $x+\bar xy=x+y$.** A barred copy of something you already have just disappears: $x_1+\bar x_1x_2=x_1+x_2$.",
            r"**Treat a bracket as one letter.** Rules work on whole groups: $(x_1+x_2)+\overline{(x_1+x_2)}\,x_3=x_1+x_2+x_3$.",
            r"**12b backwards.** $(x+y)(x+z)=x+yz$ turns a POS into an SOP in one line.",
            r"**Stuck? Expand to minterms** and pair rows that differ in one bit (past midterm Q1 style). It always works.",
            "**Check by plugging in a couple of rows.** If both sides disagree anywhere, there's a mistake.",
        ],
    )
    problem(
        d,
        2,
        "Prove it with algebra",
        8,
        "Like PS1 Q1 and textbook 2.1–2.3. Name the formula-sheet rule for every step.",
        r"""
**2.** Use algebraic manipulation to prove each identity. Name the rule you use at each step.

(a) $\bar x_1\bar x_2+\bar x_1x_2+x_1x_2=\bar x_1+x_2$ **[2]**

(b) $(x_1+x_2)(\bar x_1+x_3)=x_1x_3+\bar x_1x_2$ **[2]**

(c) $x_1+\bar x_1x_2+\bar x_1\bar x_2x_3=x_1+x_2+x_3$ **[2]**

(d) $\overline{\overline{x_1+x_2}+\overline{x_1+\bar x_2}}=x_1$ **[2]**
""",
        cite("PQ", 1, 2) + cite("P1S", 1),
    )
    sheet(d, "boolean")
    assert rows(lambda a, b, c: (not a and not b) or (not a and b) or (a and b)) == rows(lambda a, b, c: not a or b)
    assert rows(lambda a, b, c: (a or b) and (not a or c)) == rows(lambda a, b, c: (a and c) or (not a and b))
    assert rows(lambda a, b, c: a or (not a and b) or (not a and not b and c)) == rows(lambda a, b, c: a or b or c)
    assert rows(lambda a, b, c: not ((not (a or b)) or (not (a or not b)))) == rows(lambda a, b, c: a)
    solution(
        d,
        "(a)",
        r"""
1. **Copy the middle term (7b).** $\bar x_1x_2$ needs to pair with **both** of its neighbours, so write it twice.

   $$
   \bar x_1\bar x_2+\bar x_1x_2+\bar x_1x_2+x_1x_2
   $$

2. **Factor each pair (12a).** The first pair shares $\bar x_1$, the second pair shares $x_2$.

   $$
   =\bar x_1(\bar x_2+x_2)+x_2(\bar x_1+x_1)
   $$

3. **Each bracket is 1 (8b), and $x\cdot1=x$ (6a).**

   $$
   =\bar x_1+x_2 \quad\checkmark
   $$

**Faster route:** the first two terms combine to $\bar x_1$ (14a). Then $\bar x_1+x_1x_2=\bar x_1+x_2$ by 16a, with $x=\bar x_1$.

**Why the copy matters:** without it you can only use $\bar x_1x_2$ once, and you end up stuck at $\bar x_1+x_1x_2$.

*Review: Note 02 §4, Simplifying with Boolean algebra.*
""",
    )
    solution(
        d,
        "(b)",
        r"""
1. **Multiply out (12a).** Every term in the first bracket times every term in the second.

   $$
   (x_1+x_2)(\bar x_1+x_3)=x_1\bar x_1+x_1x_3+x_2\bar x_1+x_2x_3
   $$

2. **$x_1\bar x_1=0$ (8a)**, and adding 0 changes nothing (6b).

   $$
   =x_1x_3+\bar x_1x_2+x_2x_3
   $$

3. **Consensus (17a):** $xy+yz+\bar xz=xy+\bar xz$ with $x=x_1$, $y=x_3$, $z=x_2$. The term $x_2x_3$ is the consensus of the other two, so it goes.

   $$
   =x_1x_3+\bar x_1x_2 \quad\checkmark
   $$

**How to spot consensus:** $x_1x_3$ and $\bar x_1x_2$ contain $x_1$ and $\bar x_1$. Multiply what's left of them: $x_3\cdot x_2$. That term is in the expression, so delete it.

*Review: Note 02 §4. You'll reuse this result in Problem 4.*
""",
    )
    solution(
        d,
        "(c)",
        r"""
1. **16a on the first two terms**, $x+\bar xy=x+y$ with $x=x_1$, $y=x_2$.

   $$
   x_1+\bar x_1x_2+\bar x_1\bar x_2x_3=x_1+x_2+\bar x_1\bar x_2x_3
   $$

2. **De Morgan (15b) backwards:** $\bar x_1\bar x_2=\overline{x_1+x_2}$.

   $$
   =(x_1+x_2)+\overline{(x_1+x_2)}\,x_3
   $$

3. **16a again, with the whole bracket as one letter** ($x=x_1+x_2$, $y=x_3$).

   $$
   =x_1+x_2+x_3 \quad\checkmark
   $$

**The trick:** a rule works on a whole bracket, not only on single letters. The TA solution to textbook 2.3 does the same thing ("assume $xy$ is a single variable").

*Review: Note 02 §4 and §7 (De Morgan).*
""",
    )
    solution(
        d,
        "(d)",
        r"""
1. **De Morgan (15b) on the big bar:** $\overline{A+B}=\bar A\,\bar B$, with $A=\overline{x_1+x_2}$ and $B=\overline{x_1+\bar x_2}$.

   $$
   =\overline{\overline{x_1+x_2}}\cdot\overline{\overline{x_1+\bar x_2}}
   $$

2. **Double bars cancel (9).**

   $$
   =(x_1+x_2)(x_1+\bar x_2)
   $$

3. **Combining (14b):** $(x+y)(x+\bar y)=x$.

   $$
   =x_1 \quad\checkmark
   $$

**Look familiar?** Two NORs feeding a third NOR: that's a NOR–NOR circuit. Peeling the bars off always leaves a POS (more in Problem 10).

*Review: Note 02 §7 (De Morgan) and §9.*
""",
    )

    problem(
        d,
        3,
        "Simplify with algebra",
        8,
        "Like PS1 Q5 and Q8. No K-map: show the Boolean algebra.",
        r"""
**3.** Use Boolean algebra to find the minimum sum-of-products expression for each function. Name the rule you use at each step. **[2]** each

(a) $f=x_1x_2+x_1\bar x_2x_3+\bar x_1x_3$

(b) $f=x_1\bar x_2+\bar x_1x_3+\bar x_2x_3$

(c) $f=(x_1+x_2)(x_1+\bar x_2+x_3)$

(d) $f=\overline{(x_1+\bar x_2)(\bar x_1+x_3)}+x_2\bar x_3$
""",
        cite("P1S", 3, 4),
    )
    sheet(d, "boolean")
    assert rows(lambda a, b, c: (a and b) or (a and not b and c) or (not a and c)) == rows(lambda a, b, c: (a and b) or c) == {1, 3, 5, 6, 7}
    assert rows(lambda a, b, c: (a and not b) or (not a and c) or (not b and c)) == rows(lambda a, b, c: (a and not b) or (not a and c)) == {1, 3, 4, 5}
    assert rows(lambda a, b, c: (a or b) and (a or not b or c)) == rows(lambda a, b, c: a or (b and c)) == {3, 4, 5, 6, 7}
    assert rows(lambda a, b, c: (not ((a or not b) and (not a or c))) or (b and not c)) == rows(lambda a, b, c: (not a and b) or (a and not c)) == {2, 3, 4, 6}
    solution(
        d,
        "(a)",
        r"""
1. **Factor $x_3$ out of the last two terms (12a).**

   $$
   f=x_1x_2+x_3(x_1\bar x_2+\bar x_1)
   $$

2. **Inside the bracket, 16a** with $x=\bar x_1$, $y=\bar x_2$: $\;\bar x_1+x_1\bar x_2=\bar x_1+\bar x_2$.

   $$
   f=x_1x_2+x_3(\bar x_1+\bar x_2)
   $$

3. **De Morgan (15a):** $\bar x_1+\bar x_2=\overline{x_1x_2}$.

   $$
   f=x_1x_2+\overline{x_1x_2}\,x_3
   $$

4. **16a with the whole product as one letter** ($x=x_1x_2$, $y=x_3$).

   $$
   f=x_1x_2+x_3
   $$

**Check:** both versions are 1 on rows 1, 3, 5, 6, 7 ✓

**Didn't see it?** Fallback: expand to $\sum m(1,3,5,6,7)$ and pair rows. $m_1+m_3+m_5+m_7=x_3$ and $m_6+m_7=x_1x_2$ (copy $m_7$, 7b).

*Review: Note 02 §4.*
""",
    )
    solution(
        d,
        "(b)",
        r"""
1. **Look for consensus.** $x_1\bar x_2$ and $\bar x_1x_3$ contain $x_1$ and $\bar x_1$. Multiply the leftovers: $\bar x_2\cdot x_3$.

2. **That's the third term, so delete it (17a)**, with $x=x_1$, $y=\bar x_2$, $z=x_3$.

   $$
   f=x_1\bar x_2+\bar x_1x_3
   $$

**Check:** $\bar x_2x_3$ is rows 1 (001) and 5 (101). Row 1 is already covered by $\bar x_1x_3$, and row 5 by $x_1\bar x_2$. Both versions are $\sum m(1,3,4,5)$ ✓

**Trap:** no two terms combine with 14a, so it *looks* finished. Always check for a consensus term before you stop.

*Review: Note 02 §4.*
""",
    )
    solution(
        d,
        "(c)",
        r"""
1. **Distributive rule backwards (12b):** $(x+y)(x+z)=x+yz$, with $x=x_1$, $y=x_2$, $z=\bar x_2+x_3$.

   $$
   f=x_1+x_2(\bar x_2+x_3)
   $$

2. **16b:** $x(\bar x+y)=xy$, so $x_2(\bar x_2+x_3)=x_2x_3$.

   $$
   f=x_1+x_2x_3
   $$

**Check:** $f$ is 0 on rows 0, 1 (first bracket) and row 2 (second bracket). $x_1+x_2x_3$ is 0 on exactly 000, 001, 010 ✓

**Long way (also fine):** multiply out with 12a to get $x_1+x_1\bar x_2+x_1x_3+x_1x_2+x_2\bar x_2+x_2x_3$. Absorb every $x_1(\ldots)$ term into $x_1$ (13a) and drop $x_2\bar x_2=0$.

*Review: Note 02 §4.*
""",
    )
    solution(
        d,
        "(d)",
        r"""
1. **De Morgan (15a) on the bar over the AND.**

   $$
   \overline{(x_1+\bar x_2)(\bar x_1+x_3)}=\overline{x_1+\bar x_2}+\overline{\bar x_1+x_3}
   $$

2. **De Morgan (15b) on each piece, then double bars cancel (9).**

   $$
   =\bar x_1x_2+x_1\bar x_3
   \qquad\Rightarrow\qquad
   f=\bar x_1x_2+x_1\bar x_3+x_2\bar x_3
   $$

3. **Consensus (17a):** $\bar x_1x_2$ and $x_1\bar x_3$ contain $\bar x_1$ and $x_1$. The leftovers multiply to $x_2\bar x_3$, which is the last term, so drop it.

   $$
   f=\bar x_1x_2+x_1\bar x_3
   $$

**Check:** $\sum m(2,3,4,6)$ both ways ✓

*Review: Note 02 §7 (De Morgan) and §4.*
""",
    )

    # ------------------------------------------------------------ 4–5. tables, canonical forms, complements
    d.H("Truth tables, canonical forms and complements", cite("L", 38, 43))
    prime = {2, 3, 5, 7}
    problem(
        d,
        4,
        "Description → truth table → circuit",
        7,
        "Like PS1 Q9 and textbook 2.20 (design the simplest circuit).",
        r"""
**4.** A circuit has three inputs $x_1, x_2, x_3$. Together they form the 3-bit number $N=x_1x_2x_3$ ($x_1$ is the most significant bit). The output $f$ is 1 when $N$ is a prime number. Otherwise $f$ is 0.

(a) Show the truth table for $f$. **[1]**

(b) Write the canonical SOP expression for $f$. **[1]**

(c) Write the canonical POS expression for $f$. **[1]**

(d) Use Boolean algebra to find the minimum SOP and the minimum POS expressions. **[3]**

(e) Draw the minimum SOP circuit using AND, OR and NOT gates. **[1]**
""",
        cite("P1S", 4) + cite("PQ", 3),
    )
    sheet(d, "minterms")
    assert rows(lambda a, b, c: (not a and b) or (a and c)) == prime
    assert rows(lambda a, b, c: (a or b) and (not a or c)) == prime
    assert circuit_rows(PRIME_SOP) == prime
    solution(
        d,
        "(a)",
        "The primes up to 7 are 2, 3, 5, 7. **0 and 1 are not prime** (that's the trap).\n\n"
        + md(
            ["Row", "$x_1$", "$x_2$", "$x_3$", "$N$", "Prime?", "$f$"],
            [[i, *bits(i), i, "yes" if i in prime else "no", int(i in prime)] for i in range(8)],
        )
        + "\n\n*Review: Note 02 §2, Truth table from a description.*",
    )
    solution(
        d,
        "(b)",
        r"""
One minterm per 1 row. A 1 bit is written plain, a 0 bit with a bar.

$$
f=\sum m(2,3,5,7)=\bar x_1x_2\bar x_3+\bar x_1x_2x_3+x_1\bar x_2x_3+x_1x_2x_3
$$

*Review: Note 02 §3.*
""",
    )
    solution(
        d,
        "(c)",
        r"""
One maxterm per **0** row: rows 0, 1, 4, 6. Now it's the opposite: a 0 bit is plain, a 1 bit gets a bar.

$$
f=\prod M(0,1,4,6)=(x_1+x_2+x_3)(x_1+x_2+\bar x_3)(\bar x_1+x_2+x_3)(\bar x_1+\bar x_2+x_3)
$$

*Review: Note 02 §3.*
""",
    )
    solution(
        d,
        "(d)",
        r"""
**Minimum SOP:** pair 1 rows that differ in exactly one bit (14a).

1. $m_2+m_3$: 010 and 011 differ only in $x_3$.

   $$
   \bar x_1x_2\bar x_3+\bar x_1x_2x_3=\bar x_1x_2
   $$

2. $m_5+m_7$: 101 and 111 differ only in $x_2$.

   $$
   x_1\bar x_2x_3+x_1x_2x_3=x_1x_3
   $$

$$
f=\bar x_1x_2+x_1x_3
$$

**Minimum POS:** pair 0 rows the same way (14b).

3. $M_0M_1$: 000 and 001 differ only in $x_3$.

   $$
   (x_1+x_2+x_3)(x_1+x_2+\bar x_3)=x_1+x_2
   $$

4. $M_4M_6$: 100 and 110 differ only in $x_2$.

   $$
   (\bar x_1+x_2+x_3)(\bar x_1+\bar x_2+x_3)=\bar x_1+x_3
   $$

$$
f=(x_1+x_2)(\bar x_1+x_3)
$$

**Check:** Problem 2(b) proved these two are equal ✓

*Review: Note 02 §4.*
""",
    )
    solution(
        d,
        "(e)",
        figure(PRIME_SOP, "One NOT makes x̄₁, one AND per product term, and an OR collects them.")
        + "\n\n*Review: Note 02 §5, Expression → gates.*",
    )

    problem(
        d,
        5,
        "Complements",
        5,
        "Like the lecture's De Morgan examples and PS1 Q4.",
        r"""
**5.** (a) Find the complement of $f=x_1\bar x_2+\bar x_1x_3$. Give $\bar f$ first as a POS, then as a minimum SOP. **[2]**

(b) $f(x_1,x_2,x_3)=\sum m(0,2,3,6)$. Write $\bar f$ in both $\sum m$ and $\prod M$ form, and write $f$ in $\prod M$ form. **[1]**

(c) Find the complement of $f=x_1+\bar x_2(x_3+\bar x_1)$ and simplify it. **[2]**
""",
        cite("L", 24, 25),
    )
    sheet(d, "boolean")
    f5a = rows(lambda a, b, c: (a and not b) or (not a and c))
    assert set(range(8)) - f5a == rows(lambda a, b, c: (not a or b) and (a or not c)) == rows(lambda a, b, c: (not a and not c) or (a and b)) == {0, 2, 6, 7}
    assert set(range(8)) - rows(lambda a, b, c: a or (not b and (c or not a))) == rows(lambda a, b, c: not a and b) == {2, 3}
    solution(
        d,
        "(a)",
        r"""
1. **Bracket the AND groups first.**

   $$
   f=(x_1\bar x_2)+(\bar x_1x_3)
   $$

2. **Break the bar, flip the sign (15a, 15b).** OR becomes AND, AND becomes OR, every letter flips. That's the POS:

   $$
   \bar f=(\bar x_1+x_2)(x_1+\bar x_3)
   $$

3. **Multiply out (12a) and drop $\bar x_1x_1=0$ (8a).**

   $$
   \bar f=\bar x_1\bar x_3+x_1x_2+x_2\bar x_3
   $$

4. **Consensus (17a):** $\bar x_1\bar x_3$ and $x_1x_2$ contain $\bar x_1$ and $x_1$. The leftovers multiply to $\bar x_3x_2$, the last term, so drop it.

   $$
   \bar f=\bar x_1\bar x_3+x_1x_2
   $$

**Check:** $f=\sum m(1,3,4,5)$, so $\bar f$ must be $\sum m(0,2,6,7)$. $\bar x_1\bar x_3$ gives rows 0, 2 and $x_1x_2$ gives rows 6, 7 ✓

*Review: Note 02 §7.*
""",
    )
    solution(
        d,
        "(b)",
        r"""
$\bar f$ is 1 exactly where $f$ is 0, so it takes the **other** row numbers:

$$
\bar f=\sum m(1,4,5,7)
$$

$\bar f$ is 0 where $f$ is 1, so its maxterms use $f$'s minterm numbers:

$$
\bar f=\prod M(0,2,3,6)
$$

$f$ is 0 on rows 1, 4, 5, 7:

$$
f=\prod M(1,4,5,7)
$$

**Memory hook:** all four lists split the same 8 row numbers two ways. $\sum m$ of $f$ and $\prod M$ of $\bar f$ always have the **same** numbers.

*Review: Note 02 §3 and §7.*
""",
    )
    solution(
        d,
        "(c)",
        r"""
1. **Bracket the AND group.**

   $$
   f=x_1+\big(\bar x_2(x_3+\bar x_1)\big)
   $$

2. **The outer OR becomes AND (15b).**

   $$
   \bar f=\bar x_1\cdot\overline{\bar x_2(x_3+\bar x_1)}
   $$

3. **The inner AND becomes OR (15a), then 15b and 9 on the last bracket.**

   $$
   \overline{\bar x_2(x_3+\bar x_1)}=x_2+\overline{x_3+\bar x_1}=x_2+x_1\bar x_3
   \qquad\Rightarrow\qquad
   \bar f=\bar x_1(x_2+x_1\bar x_3)
   $$

4. **Multiply out (12a). $\bar x_1x_1=0$ (8a) kills the second term.**

   $$
   \bar f=\bar x_1x_2+\bar x_1x_1\bar x_3=\bar x_1x_2
   $$

**Check:** $f$ is 1 on rows 0, 1, 4, 5, 6, 7. So $\bar f$ is 1 only on rows 2 and 3 (010, 011), which is $\bar x_1x_2$ ✓

**Common mistake:** skipping step 1 and pushing the bar through without brackets. Bracket first, every time.

*Review: Note 02 §7.*
""",
    )

    # ------------------------------------------------------------ 6. Venn
    d.H("Venn diagrams", cite("MID", 4))
    problem(
        d,
        6,
        "Venn diagrams",
        5,
        "Past midterm Q3 proved 15a. Textbook 2.5 asks for 15b, and PS1 Q6 places minterms in a 3-circle diagram.",
        r"""
**6.** (a) Use the Venn diagram to prove DeMorgan's theorem, identity 15b: $\overline{x+y}=\bar x\cdot\bar y$. **[2]**

(b) Use a three-variable Venn diagram to prove the distributive rule, identity 12b: $x+yz=(x+y)(x+z)$. **[2]**

(c) Which function is shaded in the diagram below? Give it as a minimum SOP. **[1]**

"""
        + figure(
            {"kind": "venn", "title": "Problem 6(c)", "variables": ["x1", "x2", "x3"], "shaded": [3, 5, 6, 7]},
            "Problem 6(c): the shaded function.",
        ),
        cite("MID", 4) + cite("PQ", 1, 3),
    )

    def venn(title, variables, shaded, caption):
        return figure({"kind": "venn", "title": title, "variables": variables, "shaded": shaded}, caption)

    sets = {s: {i for i in range(8) if i & bit} for s, bit in (("x", 4), ("y", 2), ("z", 1))}
    assert sets["x"] | (sets["y"] & sets["z"]) == (sets["x"] | sets["y"]) & (sets["x"] | sets["z"]) == {3, 4, 5, 6, 7}
    assert rows(lambda a, b, c: a + b + c >= 2) == {3, 5, 6, 7}
    solution(
        d,
        "(a)",
        "**Left side.** First shade $x+y$: everything inside **either** circle.\n\n"
        + venn("x + y", ["x", "y"], [1, 2, 3], "x + y: both circles.")
        + "\n\nThe bar flips it: $\\overline{x+y}$ is everything **outside both** circles.\n\n"
        + venn("NOT (x + y)", ["x", "y"], [0], "The complement: only the outside is left.")
        + "\n\n**Right side.** $\\bar x$ is everything outside circle $x$. $\\bar y$ is everything outside circle $y$. "
        "AND keeps only what is shaded in **both**, which is the area outside both circles.\n\n"
        + venn("NOT x · NOT y", ["x", "y"], [0], "x̄ · ȳ: outside x and outside y at the same time.")
        + "\n\nThe two pictures match, so $\\overline{x+y}=\\bar x\\cdot\\bar y$ ✓\n\n"
        "**Marking (2025):** 1 mark for each side, so always draw both.\n\n*Review: Note 02 §8.*",
    )
    solution(
        d,
        "(b)",
        "**Left side, $x+yz$.** $x$ is the whole $x$ circle. $yz$ is where the $y$ and $z$ circles overlap. OR shades both.\n\n"
        + venn("x + yz", ["x", "y", "z"], [3, 4, 5, 6, 7], "x + yz: circle x plus the y–z overlap.")
        + "\n\n**Right side.** Shade each bracket, then AND keeps the area shaded in **both**.\n\n"
        + venn("x + y", ["x", "y", "z"], [2, 3, 4, 5, 6, 7], "x + y: circles x and y.")
        + "\n\n"
        + venn("x + z", ["x", "y", "z"], [1, 3, 4, 5, 6, 7], "x + z: circles x and z.")
        + "\n\n"
        + venn("(x + y)(x + z)", ["x", "y", "z"], [3, 4, 5, 6, 7], "Shaded in both pictures above.")
        + "\n\nThe left and right pictures match, so $x+yz=(x+y)(x+z)$ ✓\n\n*Review: Note 02 §8.*",
    )
    solution(
        d,
        "(c)",
        r"""
1. **Name the shaded regions** (1 = inside that circle, in the order $x_1x_2x_3$): 011, 101, 110, 111. That's every region inside **at least two** circles.

   $$
   f=\sum m(3,5,6,7)
   $$

2. **Pair each with $m_7$ (copy $m_7$ twice, 7b), using 14a.**

   $$
   m_3+m_7=x_2x_3,\qquad m_5+m_7=x_1x_3,\qquad m_6+m_7=x_1x_2
   $$

$$
f=x_1x_2+x_1x_3+x_2x_3
$$

That's the "at least two of three" (majority) function from Note 02 §2.

*Review: Note 02 §8.*
""",
    )

    # ------------------------------------------------------------ 7–8. circuits and timing
    d.H("Circuits and timing diagrams", cite("P1S", 2))
    problem(
        d,
        7,
        "Read a circuit, then draw its timing diagram",
        6,
        "Like PS1 Q3 and textbook 2.8.",
        r"""
**7.** Consider the circuit shown below.

"""
        + figure(Q7, "Problem 7: inputs x₁, x₂, x₃; gate outputs g₁, g₂ and f.")
        + r"""

(a) Find the expression for $f$ by working through the circuit. **[1]**

(b) Use Boolean algebra to reduce $f$ to a minimum SOP. **[2]**

(c) Show the truth table for $f$ as $\sum m(\ldots)$. **[1]**

(d) Draw a timing diagram for the circuit, with the inputs counting 000, 001, …, 111. Show the waveforms on all wires. **[2]**
""",
        cite("P1S", 2),
    )
    sheet(d, "boolean")
    f7 = {1, 2, 3, 5}
    assert circuit_rows(Q7) == f7 == rows(lambda a, b, c: (not a and b) or (not b and c))
    assert rows(lambda a, b, c: (not a and b) or (not a and c) or (not b and c)) == f7
    waves = {"g1": "", "g2": "", "f": ""}
    for a, b, c in product((0, 1), repeat=3):
        g1, g2 = int(not (a and b)), int(b or c)
        waves["g1"] += str(g1)
        waves["g2"] += str(g2)
        waves["f"] += str(g1 & g2)
    assert waves == {"g1": "11111100", "g2": "01110111", "f": "01110100"}
    q7_first = relabel(Q7, G1="g₁ = NOT(x₁x₂)", G2="g₂ = x₂ + x₃")
    solution(
        d,
        "(a)",
        logicsteps(
            "Problem 7: read it left to right",
            [
                ("Start at the inputs", relabel(Q7, G1="g₁ = ?", G2="g₂ = ?"), [], "A gate can only be named once both wires going into it are named. $x_2$ splits and feeds **both** first gates."),
                (
                    "The first two gates",
                    q7_first,
                    [r"$g_1=\overline{x_1x_2}$", r"$g_2=x_2+x_3$"],
                    r"The top gate is a **NAND** (bubble on the output) of $x_1$ and $x_2$. The bottom gate is an OR of $x_2$ and $x_3$.",
                ),
                (
                    "The AND gives f",
                    relabel(q7_first, F="f = g₁g₂"),
                    [r"$f=\overline{x_1x_2}\,(x_2+x_3)$"],
                    "The AND multiplies the two:\n\n$$\nf=\\overline{x_1x_2}\\,(x_2+x_3)\n$$\n\nTurn on **Try inputs** and test row 5 (101): $g_1=1$, $g_2=1$, so $f=1$.",
                ),
            ],
        )
        + "\n\n*Review: Note 02 §5, Gates → expression.*",
    )
    solution(
        d,
        "(b)",
        r"""
1. **De Morgan (15a)** on the NAND: $\overline{x_1x_2}=\bar x_1+\bar x_2$.

   $$
   f=(\bar x_1+\bar x_2)(x_2+x_3)
   $$

2. **Multiply out (12a).**

   $$
   f=\bar x_1x_2+\bar x_1x_3+\bar x_2x_2+\bar x_2x_3
   $$

3. **$\bar x_2x_2=0$ (8a).**

   $$
   f=\bar x_1x_2+\bar x_1x_3+\bar x_2x_3
   $$

4. **Consensus (17a):** $\bar x_1x_2$ and $\bar x_2x_3$ contain $x_2$ and $\bar x_2$. The leftovers multiply to $\bar x_1x_3$, the middle term, so drop it.

   $$
   f=\bar x_1x_2+\bar x_2x_3
   $$

*Review: Note 02 §4.*
""",
    )
    solution(
        d,
        "(c)",
        r"""
$\bar x_1x_2$ is 1 on rows 2, 3 (pattern 01-). $\bar x_2x_3$ is 1 on rows 1, 5 (pattern -01).

$$
f=\sum m(1,2,3,5)
$$

**Check from the circuit:** $g_1$ is 0 only when $x_1=x_2=1$ (rows 6, 7). $g_2$ is 0 only when $x_2=x_3=0$ (rows 0, 4). The AND is 1 on every other row: 1, 2, 3, 5 ✓

*Review: Note 02 §5.*
""",
    )
    solution(
        d,
        "(d)",
        "Feed the inputs in counting order, then fill in each wire one time slot at a time, exactly like a truth table.\n\n"
        + figure(
            {
                "kind": "timing",
                "title": "Problem 7: every wire",
                "unit": "one slot = one input row (000 to 111); ideal gates, no delay",
                "signals": [
                    {"name": "x1", "wave": "00001111"},
                    {"name": "x2", "wave": "00110011"},
                    {"name": "x3", "wave": "01010101"},
                    {"name": "g1 = NAND(x1, x2)", "wave": waves["g1"]},
                    {"name": "g2 = x2 + x3", "wave": waves["g2"]},
                    {"name": "f = g1 · g2", "wave": waves["f"]},
                ],
            },
            "g₁ drops only in the last two slots (x₁ = x₂ = 1). g₂ drops only when x₂ and x₃ are both low. f is high when both are high.",
        )
        + "\n\n$f$ is high in slots 1, 2, 3, 5, which matches part (c) ✓\n\n*Review: Note 02 §6, Circuit → waveforms.*",
    )

    q8 = {
        "kind": "timing",
        "title": "Problem 8",
        "unit": "equal time slots",
        "signals": [
            {"name": "x1", "wave": "".join(str(bits(r)[0]) for r in Q8_ORDER)},
            {"name": "x2", "wave": "".join(str(bits(r)[1]) for r in Q8_ORDER)},
            {"name": "x3", "wave": "".join(str(bits(r)[2]) for r in Q8_ORDER)},
            {"name": "f", "wave": "".join(str(int(r in Q8_ONES)) for r in Q8_ORDER)},
        ],
    }
    problem(
        d,
        8,
        "Timing diagram → function",
        6,
        "Like textbook 2.31 and 2.32 (PS1 Q10), but the inputs are not in counting order.",
        r"""
**8.** For the timing diagram below:

"""
        + figure(q8, "Problem 8: read each slot straight down.")
        + r"""

(a) Find $f$ as $\sum m(\ldots)$. **[2]**

(b) Synthesize $f$ in the simplest sum-of-products form. **[2]**

(c) Synthesize $f$ in the simplest product-of-sums form. Which form needs fewer gates? **[2]**
""",
        cite("P1S", 5),
    )
    sheet(d, "minterms")
    assert rows(lambda a, b, c: (not a and not b) or (a and b) or (a and not c)) == Q8_ONES
    assert rows(lambda a, b, c: (not a and not b) or (a and b) or (not b and not c)) == Q8_ONES
    assert rows(lambda a, b, c: (a or not b) and (not a or b or not c)) == Q8_ONES
    solution(
        d,
        "(a)",
        "The inputs jump around, so **read each slot straight down**, turn $x_1x_2x_3$ into a row number, and note $f$.\n\n"
        + md(
            ["Slot", "$x_1x_2x_3$", "Row", "$f$"],
            [[s, "".join(map(str, bits(r))), r, int(r in Q8_ONES)] for s, r in enumerate(Q8_ORDER)],
        )
        + "\n\nEvery row 0–7 shows up exactly once, so the table is complete.\n\n"
        "$$\nf=\\sum m(0,1,4,6,7)\n$$\n\n*Review: Note 02 §6, Waveforms → function.*",
    )
    solution(
        d,
        "(b)",
        r"""
1. $m_0+m_1$: 000 and 001 differ only in $x_3$ (14a) → $\bar x_1\bar x_2$.
2. $m_6+m_7$: 110 and 111 differ only in $x_3$ → $x_1x_2$.
3. $m_4$ (100) is left. Copy $m_6$ (7b) and pair $m_4+m_6$: they differ only in $x_2$ → $x_1\bar x_3$.

$$
f=\bar x_1\bar x_2+x_1x_2+x_1\bar x_3
$$

Pairing $m_4$ with $m_0$ instead gives $\bar x_2\bar x_3$ in place of $x_1\bar x_3$. Both are correct and equally small.

*Review: Note 02 §4.*
""",
    )
    solution(
        d,
        "(c)",
        r"""
Use the **0** rows: 2, 3, 5.

1. $M_2M_3$: 010 and 011 differ only in $x_3$ (14b).

   $$
   (x_1+\bar x_2+x_3)(x_1+\bar x_2+\bar x_3)=x_1+\bar x_2
   $$

2. $M_5$ (101) has no 0-row neighbour: rows 1, 4 and 7 are all 1s. It stays whole.

$$
f=(x_1+\bar x_2)(\bar x_1+x_2+\bar x_3)
$$

**Fewer gates:** the POS has 2 sum terms (2 ORs + 1 AND) and the SOP has 3 products (3 ANDs + 1 OR). With the 3 NOTs each needs, that's **6 gates for POS vs 7 for SOP**.

**Lesson:** when a function has fewer 0s than 1s, try the POS too.

*Review: Note 02 §3–4.*
""",
    )

    # ------------------------------------------------------------ 9–10. NAND / NOR
    d.H("NAND–NAND and NOR–NOR", cite("L", 47, 48, 49, 50, 51))
    callout(
        d,
        "**Reminder card: NAND–NAND / NOR–NOR in 4 steps**\n\n"
        "1. **Simplify first.** NAND–NAND needs a minimum **SOP**. NOR–NOR needs a minimum **POS**.\n"
        "2. **Draw the 2-level circuit:** AND → OR for an SOP, OR → AND for a POS.\n"
        "3. **Swap every gate** for a NAND (SOP) or a NOR (POS). The two layers of bubbles cancel each other.\n"
        "4. **Fix the leftovers:** a one-letter term goes into the last gate **flipped**, and every NOT becomes a gate with its inputs tied together.\n\n"
        "**Gate count** = NOTs + one gate per multi-letter term + 1 output gate.\n\n"
        "**Reading one back:** a two-level NAND–NAND is an SOP (each first-level NAND is one product). A NOR–NOR is a POS.\n\n"
        "**Got an SOP but asked for NOR only?** Turn it into a POS first (12b, or complement twice).",
        "reminder",
        cite("FORM", 2, 3),
    )
    problem(
        d,
        9,
        "SOP → NAND only",
        8,
        "Part (a) is past midterm Q1 with a new function. Marking scheme then: 3 for the minimum, 1.5 for the SOP, 1.5 for the NAND drawing.",
        r"""
**9.** (a) Consider the function $f(x_1,x_2,x_3)=\sum m(0,2,3,6,7)$. First, find the canonical SOP expression. Then, find the minimum SOP expression and implement it using only NAND gates. **[6]**

(b) What function does the NAND-only circuit below implement? Give it as a minimum SOP. **[2]**

"""
        + figure(Q9B, "Problem 9(b): every gate is a NAND."),
        cite("MID", 2),
    )
    sheet(d, "nandnor")
    f9 = {0, 2, 3, 6, 7}
    assert rows(lambda a, b, c: b or (not a and not c)) == f9
    for spec in (Q9_AND_OR, Q9_FLIPPED, Q9_NANDS):
        assert circuit_rows(spec) == f9
    assert circuit_rows(Q9_SWAPPED) == rows(lambda a, b, c: not b or (not a and not c)) != f9
    assert all(n["gate"] in ("INPUT", "OUTPUT", "NAND") for n in Q9_NANDS["nodes"])
    assert sum(n["gate"] == "NAND" for n in Q9_NANDS["nodes"]) == 5
    assert circuit_rows(Q9B) == prime
    solution(
        d,
        "(a)",
        r"""
**Canonical SOP:** one minterm per listed row.

$$
f=\bar x_1\bar x_2\bar x_3+\bar x_1x_2\bar x_3+\bar x_1x_2x_3+x_1x_2\bar x_3+x_1x_2x_3
$$

**Minimum SOP:**

1. $m_2+m_3=\bar x_1x_2$ and $m_6+m_7=x_1x_2$ (14a).
2. Those two differ only in $x_1$, so they combine again (14a): $\bar x_1x_2+x_1x_2=x_2$.
3. $m_0$ is left. Copy $m_2$ (7b) and pair $m_0+m_2$: 000 and 010 differ only in $x_2$, giving $\bar x_1\bar x_3$.

$$
f=x_2+\bar x_1\bar x_3
$$

**Check:** $x_2$ covers rows 2, 3, 6, 7 and $\bar x_1\bar x_3$ covers rows 0, 2. Together: 0, 2, 3, 6, 7 ✓

**NAND only:** click **Next** to convert the circuit one step at a time.

"""
        + logicsteps(
            "Problem 9(a): AND–OR into NAND–NAND",
            [
                ("Draw the normal AND–OR circuit", Q9_AND_OR, [], r"From $f=x_2+\bar x_1\bar x_3$: two NOTs, one AND for $\bar x_1\bar x_3$, and an OR at the end. $x_2$ is a one-letter term, so it goes straight into the OR."),
                (
                    "Swap the AND and the OR for NANDs",
                    Q9_SWAPPED,
                    [],
                    r"The last NAND flips **both** of its inputs (De Morgan). That undoes the bubble on the product, but it also flips $x_2$: right now $f=\bar x_2+\bar x_1\bar x_3$. **Wrong.** Try inputs 010: it should give 1 but gives 0.",
                ),
                (
                    "Flip the one-letter term",
                    Q9_FLIPPED,
                    [],
                    "Feed $x_2$ in already flipped. The last NAND flips it back:\n\n$$\n"
                    r"f=\overline{\bar x_2\cdot\overline{\bar x_1\bar x_3}}=x_2+\bar x_1\bar x_3"
                    "\n$$",
                ),
                ("Make the NOTs out of NANDs", Q9_NANDS, [], "Tie both inputs of a NAND together to get a NOT. Every gate is now a NAND. Try any inputs: it matches the AND–OR circuit on all 8 rows."),
            ],
        )
        + r"""

**Answer:** $f=x_2+\bar x_1\bar x_3$ with **5 NAND gates**: 3 tied NANDs for $\bar x_1, \bar x_2, \bar x_3$, one for the product, one at the output.

*Review: Note 02 §9, SOP → NAND–NAND.*
""",
    )
    q9b_first = relabel(Q9B, N1="x̄₁")
    q9b_mid = relabel(q9b_first, N2="NOT(x̄₁x₂)", N3="NOT(x₁x₃)")
    solution(
        d,
        "(b)",
        logicsteps(
            "Problem 9(b): read the NAND circuit",
            [
                ("Start at the inputs", Q9B, [], "Spot the NAND whose two inputs are **both** $x_1$. That's a tied NAND, so it's a NOT."),
                ("The tied NAND", q9b_first, [r"$\overline{x_1x_1}=\bar x_1$"], r"$\overline{x_1x_1}=\bar x_1$ (7a, then the bar)."),
                (
                    "The middle NANDs",
                    q9b_mid,
                    [r"$\overline{\bar x_1x_2}$", r"$\overline{x_1x_3}$"],
                    r"Top: NAND of $\bar x_1$ and $x_2$. Bottom: NAND of $x_1$ and $x_3$.",
                ),
                (
                    "The output NAND",
                    relabel(q9b_mid, F="x̄₁x₂ + x₁x₃"),
                    [r"$f=\bar x_1x_2+x_1x_3$"],
                    "De Morgan (15a), then the double bars cancel (9):\n\n$$\n"
                    r"f=\overline{\overline{\bar x_1x_2}\cdot\overline{x_1x_3}}=\bar x_1x_2+x_1x_3"
                    "\n$$",
                ),
            ],
        )
        + r"""

**Shortcut:** a two-level NAND–NAND is always an SOP. Each first-level NAND is one product term, so you can read $\bar x_1x_2+x_1x_3$ straight off.

**Answer:** $f=\bar x_1x_2+x_1x_3$. That's the prime-number function from Problem 4.

*Review: Note 02 §9.*
""",
    )

    problem(
        d,
        10,
        "POS → NOR only",
        6,
        "The NOR mirror image of past midterm Q1.",
        r"""
**10.** (a) Consider the function $f(x_1,x_2,x_3)=\prod M(1,3,4,5)$. First, find the canonical POS expression. Then, find the minimum POS expression and implement it using only NOR gates. **[4]**

(b) Implement $g=x_1x_2+\bar x_3$ using only NOR gates. **[2]**
""",
        cite("L", 50, 51),
    )
    sheet(d, "nandnor")
    f10 = set(range(8)) - {1, 3, 4, 5}
    assert rows(lambda a, b, c: (a or not c) and (not a or b)) == f10
    for spec in (Q10_OR_AND, Q10_SWAPPED, Q10_NORS):
        assert circuit_rows(spec) == f10
    assert all(n["gate"] in ("INPUT", "OUTPUT", "NOR") for n in Q10_NORS["nodes"])
    assert sum(n["gate"] == "NOR" for n in Q10_NORS["nodes"]) == 5
    g10 = rows(lambda a, b, c: (a and b) or not c)
    assert g10 == rows(lambda a, b, c: (a or not c) and (b or not c)) == circuit_rows(Q10B)
    assert sum(n["gate"] == "NOR" for n in Q10B["nodes"]) == 4
    solution(
        d,
        "(a)",
        r"""
**Canonical POS:** one maxterm per listed row (0 bit → plain, 1 bit → barred).

$$
f=(x_1+x_2+\bar x_3)(x_1+\bar x_2+\bar x_3)(\bar x_1+x_2+x_3)(\bar x_1+x_2+\bar x_3)
$$

**Minimum POS:** pair 0 rows that differ in one bit (14b).

1. $M_1M_3$: 001 and 011 differ only in $x_2$ → $(x_1+\bar x_3)$.
2. $M_4M_5$: 100 and 101 differ only in $x_3$ → $(\bar x_1+x_2)$.

$$
f=(x_1+\bar x_3)(\bar x_1+x_2)
$$

**NOR only:** same recipe as NAND, with OR → AND swapped to NOR → NOR.

"""
        + logicsteps(
            "Problem 10(a): OR–AND into NOR–NOR",
            [
                ("Draw the normal OR–AND circuit", Q10_OR_AND, [], r"Two NOTs, one OR per bracket, and an AND at the end."),
                (
                    "Swap every OR and the AND for NORs",
                    Q10_SWAPPED,
                    [],
                    "Each first-level NOR gives a flipped sum. The last NOR is an AND with bubbles on its inputs (De Morgan), so it flips them back:\n\n$$\n"
                    r"\overline{\overline{x_1+\bar x_3}+\overline{\bar x_1+x_2}}=(x_1+\bar x_3)(\bar x_1+x_2)"
                    "\n$$\n\nThere's no one-letter term here, so nothing needs flipping.",
                ),
                ("Make the NOTs out of NORs", Q10_NORS, [], "Tie both inputs of a NOR together to get a NOT. All 5 gates are NORs now. Try inputs to compare with the first step."),
            ],
        )
        + r"""

**Answer:** **5 NOR gates.**

*Review: Note 02 §9, POS → NOR–NOR.*
""",
    )
    solution(
        d,
        "(b)",
        r"""
1. **NOR–NOR needs a POS, but $g$ is an SOP.** Convert it with the distributive rule 12b, $x+yz=(x+y)(x+z)$, using $x=\bar x_3$, $y=x_1$, $z=x_2$.

   $$
   g=\bar x_3+x_1x_2=(x_1+\bar x_3)(x_2+\bar x_3)
   $$

2. **Build it with NORs.** One tied NOR makes $\bar x_3$ and feeds **both** sum terms.

"""
        + figure(Q10B, "U and V are the two sums, flipped. The last NOR flips them back and ANDs them.")
        + r"""

**Check:** $\overline{U+V}=\bar U\,\bar V=(x_1+\bar x_3)(x_2+\bar x_3)=g$ ✓

**Answer:** **4 NOR gates.**

*Review: Note 02 §9.*
""",
    )

    # ------------------------------------------------------------ 11. CMOS
    d.H("Transistors and CMOS", cite("C", 6))
    problem(
        d,
        11,
        "CMOS and NMOS gates",
        8,
        "Like PS2 Q1 and Q3–Q5 and the Week 5 lecture.",
        r"""
**11.** (a) Draw a CMOS circuit (one complex gate) that implements $f=\bar x_1\bar x_2+\bar x_3$. How many transistors does it use? **[3]**

(b) What function does the CMOS circuit below implement? Give its truth table as $\sum m(\ldots)$. **[3]**

"""
        + figure(CMOS_B, "Problem 11(b): read the NMOS half first.")
        + r"""

(c) How many transistors does $f=x_1x_2+x_3$ need in basic static CMOS? **[1]**

(d) The NMOS gate below uses a pull-up resistor and two NMOS switches in parallel. Name the gate. When $x_1=1$ and $x_2=0$, is the output high or low, and does current flow from $V_{DD}$ to ground? **[1]**

"""
        + NMOS_NOR,
        cite("P2", 1, 2) + cite("C", 11, 12, 24),
    )
    sheet(d, "transistors")
    schematic.check(NMOS_NOR.split("\n", 1)[1].split("```")[0])
    f11a =rows(lambda a, b, c: (not a and not b) or not c)
    assert cmos_rows(CMOS_A) == f11a
    assert cmos_rows(CMOS_B) == rows(lambda a, b, c: not ((a and b) or c)) == {0, 2, 4}
    solution(
        d,
        "(a)",
        r"""
1. **Complement first.** The NMOS pull-down network (PDN) must conduct exactly when $f=0$. So find $\bar f$ with De Morgan (15b, then 15a).

   $$
   \bar f=\overline{\bar x_1\bar x_2+\bar x_3}=\overline{\bar x_1\bar x_2}\cdot x_3=(x_1+x_2)\,x_3
   $$

2. **PDN (NMOS):** OR = parallel, AND = series. NMOS $x_1$ in parallel with NMOS $x_2$, then in series with NMOS $x_3$.

3. **PUN (PMOS) is the dual:** swap series and parallel, keep the same gate labels. PMOS $x_1$ and $x_2$ in series, in parallel with PMOS $x_3$.

"""
        + figure(CMOS_A, "PDN: (x₁ ∥ x₂) in series with x₃. PUN: (x₁ — x₂ in series) ∥ x₃.")
        + r"""

4. **Check the pull-up.** Series PMOS $x_1, x_2$ both conduct when $x_1=x_2=0$, giving $\bar x_1\bar x_2$. PMOS $x_3$ conducts when $x_3=0$, giving $\bar x_3$. So the output is pulled up exactly when $\bar x_1\bar x_2+\bar x_3=1$ ✓

**Answer:** 3 NMOS + 3 PMOS = **6 transistors**. No inverters needed: the bars in $f$ come free, because a CMOS gate always inverts.

*Review: Note 03 §3, Function → pull-down → dual pull-up.*
""",
    )
    solution(
        d,
        "(b)",
        r"""
1. **Read the NMOS half.** Find every path from $f$ down to ground: through $x_1$ **and** $x_2$ in series, **or** through $x_3$.

   $$
   \text{PDN conducts when } x_1x_2+x_3=1
   $$

2. **When the PDN conducts, the output is 0.** So complement once:

   $$
   f=\overline{x_1x_2+x_3}=(\bar x_1+\bar x_2)\,\bar x_3
   $$

3. **Truth table:** $f=1$ needs $x_3=0$ (rows 0, 2, 4, 6) and not both $x_1, x_2$ (that removes row 6).

"""
        + md(["Row", "$x_1x_2x_3$", "PDN on?", "$f$"], [[i, "".join(map(str, bits(i))), "no" if i in {0, 2, 4} else "yes", int(i in {0, 2, 4})] for i in range(8)])
        + r"""

**Answer:** $f=\overline{x_1x_2+x_3}=\sum m(0,2,4)$.

**Check with the PMOS half:** PMOS $x_1 \parallel x_2$ in series with PMOS $x_3$ conducts when $(\bar x_1+\bar x_2)\bar x_3=1$. Same thing ✓

*Review: Note 03 §4, CMOS drawing → function.*
""",
    )
    solution(
        d,
        "(c)",
        r"""
CMOS gates always invert. One complex gate gives $\overline{x_1x_2+x_3}$: that's the circuit in part (b), 6 transistors. Add an inverter (2 transistors) to undo the bar.

$$
6+2=8 \text{ transistors}
$$

**Compare:** separate gates would be a 2-input AND (NAND + NOT = 6) and a 2-input OR (NOR + NOT = 6), so 12. The complex gate is cheaper.

*Review: Note 03 §2, transistor counting.*
""",
    )
    solution(
        d,
        "(d)",
        r"""
1. **Name it.** Either closed switch connects $f$ to ground, so the output is 0 when $x_1+x_2=1$.

   $$
   f=\overline{x_1+x_2}\quad\text{(NOR)}
   $$

2. **$x_1=1$:** that NMOS has its gate at $V_{DD}$, so it's on (a closed switch). The output is pulled **low**.

3. **Current: yes.** There's a complete path $V_{DD}$ → resistor → closed NMOS → ground, so current flows the whole time the output is low. That wasted power is why CMOS replaces the resistor with PMOS transistors: in CMOS, one of the two networks is always off.

*Review: Note 03 §1, Transistor switches and resistor-load NMOS gates.*
""",
    )
    return d


if __name__ == "__main__":
    note = build()
    for b in note.blocks:
        if b["type"] == "solution":
            assert len(b["text"]) <= 10000, f"{b['title']} is too long ({len(b['text'])} chars)"
    note.save()
