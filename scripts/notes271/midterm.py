"""Reorganize the verified course content around the instructor's Week 1–5 midterm scope."""

import copy
import json
import uuid
from fractions import Fraction
from itertools import product

from lib import OUT, Doc, S, circuit, cite, figure, node, wire

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


def sub(doc, text):
    doc.add("heading", (), level=2, text=text)


def bullets(doc, items, ordered=False, cites=()):
    doc.add("list", cites, ordered=ordered, items=items)


def callout(doc, text, tone="tip", cites=()):
    doc.add("callout", cites, text=text, tone=tone)


def relabel(spec, **labels):
    """A copy of a circuit figure with some node labels changed (for step-by-step views)."""
    spec = copy.deepcopy(spec)
    for n in spec["nodes"]:
        n["label"] = labels.get(n["id"], n.get("label", ""))
    return spec


def regate(spec, **gates):
    spec = copy.deepcopy(spec)
    for n in spec["nodes"]:
        n["gate"] = gates.get(n["id"], n["gate"])
    return spec


def section1():
    d = new(1, "Binary Numbers — Midterm", ["number_systems", "binary_numbers", "base_conversion"], True)

    heading(d, "1. What binary is", cite("N", 30, 31))
    d.P("Normal (decimal) numbers use ten digits, 0 to 9. Each place is worth **10 times** the place to its right.")
    d.E(r"352 = 3(100) + 5(10) + 2(1)")
    d.P(
        "Binary is the same idea with only two digits, 0 and 1. Each place is worth **2 times** the place to its right.\n\n"
        "So the places are worth 1, 2, 4, 8, 16, … going left. After the point they keep halving: ½, ¼, ⅛, …"
    )
    d.T(
        ["Place", "$2^4$", "$2^3$", "$2^2$", "$2^1$", "$2^0$", "$2^{-1}$", "$2^{-2}$", "$2^{-3}$", "$2^{-4}$"],
        [["Worth", 16, 8, 4, 2, 1, 0.5, 0.25, 0.125, 0.0625]],
        cite("N", 31),
    )
    d.P("The point sits between the $2^0$ place and the $2^{-1}$ place. Learn this row; you use it in every question.")
    bullets(
        d,
        [
            "**Bit:** one binary digit, 0 or 1.",
            "**MSB:** the leftmost bit (worth the most). **LSB:** the rightmost bit (worth the least).",
            r"$(1011)_2$ means 1011 in base 2. $(1011)_{10}$ would be one thousand and eleven.",
        ],
        cites=cite("N", 33, 36),
    )

    heading(d, "2. Binary → decimal", cite("N", 31))
    d.P("**Method:** write each place's worth above its bit. Add up the worths that have a 1 under them.")
    d.T(["Worth", "8", "4", "2", "1"], [["Bit", 1, 0, 1, 1]])
    d.E(r"(1011)_2 = 8 + 2 + 1 = 11")
    d.P("Fractions work the same way. The bits after the point are worth 0.5, 0.25, 0.125, …")
    d.T(["Worth", "8", "4", "2", "1", "0.5", "0.25"], [["Bit", 1, 0, 1, 0, 0, 1]], cite("N", 31))
    d.E(r"(1010.01)_2 = 8 + 2 + 0.25 = 10.25")
    d.P("The formula sheet writes the same idea as a sum. You don't need it if you use the table above.")
    d.E(r"V=\sum_{i=-m}^{n-1} b_i\,k^i", cite("FORM", 1))
    bullets(
        d,
        [
            "$k$ = the base (2 for binary, 16 for hex).",
            "$b_i$ = the digit in position $i$. Position 0 is just left of the point.",
            "Positions after the point are negative: $-1, -2, \\dots$",
        ],
    )
    d.Q(
        "Try it: Tutorial 2 Q1.6 and a fraction",
        r"Convert to decimal: (a) $(11100)_2$ (b) $(111111)_2$ (c) $(101010101010)_2$ (d) $(110.101)_2$",
        [
            S("(a) The 1s sit in the 16, 8 and 4 places.", r"16+8+4=28"),
            S(
                "(b) Six 1s in a row is one less than the next place (64). Adding every place also works.",
                r"64-1=63",
            ),
            S("(c) The 1s sit in places 11, 9, 7, 5, 3, 1.", r"2048+512+128+32+8+2=2730"),
            S("(d) Use 0.5, 0.25, 0.125 after the point.", r"4+2+0.5+0.125=6.625"),
        ],
        "28, 63, 2730, 6.625.",
        cite("T", 1),
    )

    heading(d, "3. Decimal → binary", cite("N", 37, 38, 39))
    d.P(
        "Split the number at the point. The whole part and the fraction part use **different** methods. "
        "We'll do last year's midterm question as the example."
    )
    d.P("**Past midterm Q2a:** convert $14.3125$ to binary.", cite("MID", 3))
    sub(d, "Whole part: keep dividing by 2")
    bullets(
        d,
        [
            "**Divide** the number by 2. Write down the remainder (always 0 or 1).",
            "**Repeat** with the quotient until the quotient is 0.",
            "**Read** the remainders from the **bottom up**.",
        ],
        ordered=True,
    )
    d.T(
        ["Operation", "Quotient", "Remainder"],
        [["14 ÷ 2", 7, 0], ["7 ÷ 2", 3, 1], ["3 ÷ 2", 1, 1], ["1 ÷ 2", 0, 1]],
        cite("MID", 3),
    )
    d.P("Bottom up: $14 = (1110)_2$. Check: $8+4+2=14$.")
    d.P(
        "Why bottom up? The first remainder tells you if the number is odd, which is the 1s place (the rightmost bit). "
        "Each division moves you one place further left."
    )
    sub(d, "Fraction part: keep multiplying by 2")
    bullets(
        d,
        [
            "**Multiply** the fraction by 2.",
            "The digit in front of the point (0 or 1) is your **next bit**.",
            "**Drop** that digit, keep only the part after the point, and repeat.",
            "**Stop** when you reach exactly 0 (or have as many bits as the question asks). Read the bits **top down**.",
        ],
        ordered=True,
    )
    d.T(
        ["Operation", "Result", "Bit"],
        [["0.3125 × 2", "0.625", 0], ["0.625 × 2", "1.25", 1], ["0.25 × 2", "0.5", 0], ["0.5 × 2", "1.0", 1]],
        cite("MID", 3),
    )
    d.P(
        "Top down: $0.3125 = (.0101)_2$.\n\n"
        "Why it works: multiplying by 2 slides the binary point one place right, so the first bit after the point pops out in front."
    )
    d.E(r"14.3125 = (1110.0101)_2")
    d.P("**Always check** by going back: $8+4+2+0.25+0.0625 = 14.3125$ ✓")
    d.Q(
        "Try it: Tutorial 2 Q1.1 and a lecture fraction",
        r"Convert to binary: (a) $20$ (b) $100$ (c) $129$ (d) $23.375$",
        [
            S("(a) Remainders 0,0,1,0,1, read bottom up.", r"20=(10100)_2"),
            S("(b) Remainders 0,0,1,0,0,1,1, read bottom up.", r"100=(1100100)_2"),
            S("(c) $129 = 128 + 1$, so only the 128 and 1 places get a 1.", r"129=(10000001)_2"),
            S(
                "(d) Whole part: $23 = 16+4+2+1$. Fraction: $0.375 \\times 2 = 0.75$ → 0, $0.75 \\times 2 = 1.5$ → 1, $0.5\\times 2=1.0$ → 1.",
                r"23.375=(10111.011)_2",
            ),
        ],
        "10100, 1100100, 10000001, 10111.011.",
        cite("T", 1),
    )
    callout(
        d,
        "**Quick check trick:** for a small number, find the biggest place worth that fits, subtract it, and repeat. "
        "$23$: take 16 (7 left), take 4 (3 left), take 2 (1 left), take 1. So the 16, 4, 2, 1 places are 1: $10111$.",
    )

    heading(d, "4. Extras: fractions that never end, and how many bits", cite("N", 40))
    d.P("What if the fraction never reaches 0? Try $0.2$:")
    d.T(
        ["Operation", "Result", "Bit"],
        [["0.2 × 2", "0.4", 0], ["0.4 × 2", "0.8", 0], ["0.8 × 2", "1.6", 1], ["0.6 × 2", "1.2", 1], ["0.2 × 2", "…", "repeats"]],
        cite("N", 40),
    )
    d.P(
        "We're back at $0.2$, so the bits repeat forever: $0.2 = (.001100110011\\ldots)_2$.\n\n"
        "**Rule:** a fraction ends in binary only if its bottom number is a power of 2. "
        "$\\tfrac38$ ends ($8=2^3$). $\\tfrac15$ and $\\tfrac23$ never end."
    )
    d.X(
        "Past midterm Q2b: how close do four bits get?",
        r"Write $2/3$ in binary to four places. Convert that back to decimal. How close is it to $2/3$?",
        [
            S(
                "Multiply by 2 four times. The fraction bounces between 0.666… and 0.333…",
                r"1.333\to1,\quad 0.666\to0,\quad 1.333\to1,\quad 0.666\to0",
            ),
            S("Keep the four bits.", r"\tfrac23 \approx (.1010)_2"),
            S("Convert back: the 1s are in the 0.5 and 0.125 places.", r"0.5+0.125=0.625"),
            S("Subtract to get the error.", r"0.6667-0.625\approx0.0417"),
        ],
        r"$(.1010)_2 = 0.625$, which is about $0.0417$ below $2/3$.",
        cite("MID", 3),
    )
    sub(d, "How many bits do I need?")
    d.P(
        "With $n$ bits you can count from $0$ to $2^n-1$. "
        "So find the **first power of 2 that is bigger** than your number. That power is your bit count."
    )
    d.E(r"1029:\quad 2^{10}=1024 \le 1029 < 2048=2^{11}\quad\Rightarrow\quad 11\text{ bits}", cite("T", 1))
    d.P("Tutorial 2 Q1.8 for practice: $270$ → 9 bits (512), $520$ → 10 bits (1024), $780$ → 10 bits (1024).", cite("T", 1))

    heading(d, "5. Hexadecimal", cite("N", 41, 42, 43))
    d.P(
        "Binary numbers get long fast, so we use hex as shorthand. Hex is base 16, and $16 = 2^4$, "
        "so **one hex digit is exactly 4 bits**.\n\n"
        "Hex needs 16 digits. After 9 it uses letters: A = 10, B = 11, C = 12, D = 13, E = 14, F = 15."
    )
    d.T(
        ["Hex", "Binary", "Hex", "Binary"],
        [
            ["0", "0000", "8", "1000"],
            ["1", "0001", "9", "1001"],
            ["2", "0010", "A (10)", "1010"],
            ["3", "0011", "B (11)", "1011"],
            ["4", "0100", "C (12)", "1100"],
            ["5", "0101", "D (13)", "1101"],
            ["6", "0110", "E (14)", "1110"],
            ["7", "0111", "F (15)", "1111"],
        ],
        cite("N", 41),
    )
    d.P("This table is on the formula sheet, so you don't need to memorize it.", cite("FORM", 1))
    sub(d, "Binary → hex: group by 4 from the point")
    bullets(
        d,
        [
            "**Start at the point.** Group bits in fours going **left** for the whole part and **right** for the fraction.",
            "**Pad with zeros on the outside ends** if a group is short (far left, or far right).",
            "**Swap** each group of 4 for its hex digit.",
        ],
        ordered=True,
    )
    d.E(r"(10110110.101)_2 \;\to\; 1011\;0110\,.\,1010 \;\to\; (\mathrm{B6.A})_{16}", cite("N", 42, 43))
    d.P(
        "Why pad on the outside? $.101$ and $.1010$ are the same number, just like $0.5 = 0.50$. "
        "Padding the inside, $.0101$, would change the value."
    )
    sub(d, "Hex → binary: swap each digit for 4 bits")
    d.E(r"(2\mathrm{F}.4)_{16} \;\to\; 0010\;1111\,.\,0100 \;\to\; (101111.01)_2")
    d.P("Drop the leading zeros on the left and the trailing zeros on the right at the end.")
    sub(d, "Hex → decimal: places are worth 16, 1, 1/16")
    d.P("Same idea as binary, but each place is worth 16 times the one to its right.")
    d.E(r"(2\mathrm{F}.4)_{16} = 2(16) + 15(1) + \tfrac{4}{16} = 32+15+0.25 = 47.25")
    sub(d, "Decimal → hex: go through binary")
    d.X(
        "Decimal to hex with a fraction",
        r"Convert $200.75$ to hexadecimal.",
        [
            S("Whole part to binary. $200 = 128+64+8$.", r"200=(11001000)_2"),
            S("Fraction to binary: $0.75\\times2=1.5$ → 1, $0.5\\times2=1.0$ → 1.", r"0.75=(.11)_2"),
            S("Group by 4 from the point, padding the fraction on the right.", r"1100\;1000\,.\,1100"),
            S("Swap each group for a hex digit.", r"(\mathrm{C8.C})_{16}"),
            S("Check in decimal.", r"12(16)+8+\tfrac{12}{16}=200.75"),
        ],
        r"$(\mathrm{C8.C})_{16}$.",
    )
    d.Q(
        "Try it: both directions",
        r"(a) Convert $(3\mathrm{A}.8)_{16}$ to decimal and to binary. (b) Convert $45.25$ to hex.",
        [
            S("(a) Decimal: A = 10 and the 8 sits in the 1/16 place.", r"3(16)+10+\tfrac8{16}=58.5"),
            S("(a) Binary: swap each digit for 4 bits.", r"0011\;1010\,.\,1000\to(111010.1)_2"),
            S("(b) $45 = 32+8+4+1$ and $0.25 = .01$.", r"45.25=(101101.01)_2"),
            S("(b) Group by 4 from the point.", r"0010\;1101\,.\,0100\to(\mathrm{2D.4})_{16}"),
        ],
        r"(a) $58.5$ and $(111010.1)_2$. (b) $(\mathrm{2D.4})_{16}$.",
    )

    assert int("1110", 2) + Fraction(5, 16) == Fraction(143125, 10000)
    assert [int(c) for c in "10100"] and int("10100", 2) == 20 and int("1100100", 2) == 100
    assert int("10000001", 2) == 129 and int("10111", 2) + Fraction(3, 8) == Fraction(23375, 1000)
    assert int("11100", 2) == 28 and int("111111", 2) == 63 and int("101010101010", 2) == 2730
    assert Fraction(2, 3) - Fraction(5, 8) == Fraction(1, 24)
    assert int("11001000", 2) == 200 and 0xC8 + Fraction(12, 16) == Fraction(803, 4)
    assert 0x3A + Fraction(8, 16) == Fraction(117, 2) and 0x2D + Fraction(4, 16) == Fraction(181, 4)
    assert 0x2F + Fraction(4, 16) == Fraction(189, 4) and int("101111", 2) == 47
    assert [n.bit_length() for n in (270, 520, 780, 1029)] == [9, 10, 10, 11]
    return d


def rows(f, n=3):
    """Minterm numbers where f(x1, ..., xn) is 1, with x1 as the MSB."""
    return {i for i, bits in enumerate(product((0, 1), repeat=n)) if f(*bits)}


def section2():
    d = new(
        2,
        "Introduction to Logic Circuits — Midterm",
        ["logic_gates", "boolean_algebra", "truth_tables", "logic_synthesis", "canonical_forms", "nand_nor"],
        True,
    )
    d.P(
        "The notes use $x_1, x_2, x_3$ like the lectures, the formula sheet and the exam. "
        "$x_1$ is always the leftmost bit."
    )

    heading(d, "1. The gates and how to write them", cite("L", 13, 32))
    d.P("Every signal is 0 or 1. There are three basic operations:")
    bullets(
        d,
        [
            "**AND**, written $x_1x_2$ or $x_1\\cdot x_2$: 1 only when **both** inputs are 1.",
            "**OR**, written $x_1+x_2$: 1 when **at least one** input is 1.",
            "**NOT**, written $\\bar x_1$: flips the bit. $\\bar 0 = 1$, $\\bar 1 = 0$.",
        ],
    )
    d.P("**NAND** is AND followed by NOT. **NOR** is OR followed by NOT. The small circle (bubble) on a gate means \"flip it\".")
    d.T(
        ["$x_1$", "$x_2$", "AND $x_1x_2$", "OR $x_1+x_2$", r"NAND $\overline{x_1x_2}$", r"NOR $\overline{x_1+x_2}$"],
        [[a, b, a & b, a | b, 1 - (a & b), 1 - (a | b)] for a, b in product((0, 1), repeat=2)],
        cite("L", 11, 47),
    )
    d.F(
        circuit(
            "The five gate symbols",
            [
                node("A", "AND", 330, 100, label="AND: x₁x₂"),
                node("Aa", "INPUT", 110, 65, label="x₁"),
                node("Ab", "INPUT", 110, 135, label="x₂"),
                node("NA", "NAND", 720, 100, label="NAND: NOT(x₁x₂)"),
                node("NAa", "INPUT", 500, 65, label="x₁"),
                node("NAb", "INPUT", 500, 135, label="x₂"),
                node("O", "OR", 330, 260, label="OR: x₁+x₂"),
                node("Oa", "INPUT", 110, 225, label="x₁"),
                node("Ob", "INPUT", 110, 295, label="x₂"),
                node("NO", "NOR", 720, 260, label="NOR: NOT(x₁+x₂)"),
                node("NOa", "INPUT", 500, 225, label="x₁"),
                node("NOb", "INPUT", 500, 295, label="x₂"),
                node("N", "NOT", 330, 400, label="NOT: x̄₁"),
                node("Na", "INPUT", 110, 400, label="x₁"),
            ],
            [
                wire("Aa.out", "A.0", [[220, 65], [220, 90]]),
                wire("Ab.out", "A.1", [[220, 135], [220, 110]]),
                wire("NAa.out", "NA.0", [[610, 65], [610, 90]]),
                wire("NAb.out", "NA.1", [[610, 135], [610, 110]]),
                wire("Oa.out", "O.0", [[220, 225], [220, 250]]),
                wire("Ob.out", "O.1", [[220, 295], [220, 270]]),
                wire("NOa.out", "NO.0", [[610, 225], [610, 250]]),
                wire("NOb.out", "NO.1", [[610, 295], [610, 270]]),
                wire("Na.out", "N.0"),
            ],
        ),
        "AND has a flat back, OR has a curved back. NAND and NOR (right) are the same shapes with a bubble on the output.",
        cite("L", 13, 47),
    )
    d.P(
        "**Order of operations:** NOT first, then AND, then OR (like × before + in normal math). "
        "So $x_1 + x_2\\bar x_3$ means $x_1 + (x_2\\bar x_3)$."
    )

    heading(d, "2. Truth table from a description", cite("L", 11, 12, 34, 52))
    d.P(
        "A truth table lists **every** possible input combination and the output for each one. "
        "$n$ inputs give $2^n$ rows: 2 inputs → 4 rows, 3 inputs → 8 rows."
    )
    sub(d, "Writing the input columns without missing a row")
    d.P("Just count in binary from 0. Row 0 is 000, row 1 is 001, row 2 is 010, … row 7 is 111. You get this pattern:")
    bullets(
        d,
        [
            "$x_3$ (the last column) flips **every** row: 0,1,0,1,0,1,0,1",
            "$x_2$ flips **every 2** rows: 0,0,1,1,0,0,1,1",
            "$x_1$ flips **every 4** rows: 0,0,0,0,1,1,1,1",
        ],
    )
    d.P(
        "Why: that's how counting works. The 1s place changes every time you add 1, the 2s place every second time, the 4s place every fourth time.\n\n"
        "Bonus: the row number is just the inputs read as a binary number. Row 5 is $x_1x_2x_3 = 101$. You'll use these row numbers for minterms next."
    )
    sub(d, "Filling in the output column")
    d.P("Go row by row and ask: \"does the description say the output is 1 here?\"")
    d.X(
        "Lecture example: two switches",
        "The output is 0 if switch $x_1$ is closed and switch $x_2$ is open. Otherwise the output is 1. (Closed = 1, open = 0.)",
        [
            S("Two inputs → 4 rows: 00, 01, 10, 11."),
            S("\"$x_1$ closed and $x_2$ open\" is $x_1=1$, $x_2=0$, which is row 10. That row gets 0."),
            S("Every other row gets 1.", r"f = 1,\;1,\;0,\;1"),
        ],
        "$f$ = 1, 1, 0, 1 for rows 00, 01, 10, 11.",
        cite("L", 34),
    )
    d.X(
        "At least two of three inputs",
        "A circuit outputs 1 when **at least two** of $x_1, x_2, x_3$ are 1. Write its truth table.",
        [
            S("Three inputs → 8 rows. Count from 000 to 111."),
            S("Add a helper column: how many 1s are in the row?"),
            S("$f = 1$ wherever that count is 2 or 3: rows 3, 5, 6, 7."),
        ],
        "See the table below.",
    )
    d.T(
        ["Row", "$x_1$", "$x_2$", "$x_3$", "Count of 1s", "$f$"],
        [[i, a, b, c, a + b + c, int(a + b + c >= 2)] for i, (a, b, c) in enumerate(product((0, 1), repeat=3))],
    )
    d.P("A helper column like \"count of 1s\" makes descriptions about counting easy to fill in. Leave it out of your final answer if you want.")
    d.Q(
        "Try it: lecture three-way light",
        "A room has three switches $x_1, x_2, x_3$. The light is off when no switches are closed, "
        "on when exactly one is closed, off when two are closed, and on when all three are closed. Which rows have $f=1$?",
        [
            S("Use the \"count of 1s\" helper column: the light is on when the count is 1 or 3 (an odd number)."),
            S("Count 1: rows 1 (001), 2 (010), 4 (100). Count 3: row 7 (111)."),
        ],
        "$f = 1$ in rows 1, 2, 4, 7.",
        cite("L", 52, 53),
    )

    heading(d, "3. Truth table → canonical SOP and POS", cite("L", 38, 39, 43))
    d.P("You have a truth table. How do you turn it into a formula? There are two standard ways.")
    sub(d, "Minterms and canonical SOP (use the 1 rows)")
    d.P(
        "A **minterm** is an AND of **all** the variables that equals 1 in exactly one row.\n\n"
        "**Rule:** look at the row. A 1 bit → write the variable plain. A 0 bit → write it with a bar."
    )
    d.E(r"\text{Row 5} = 101 \quad\Rightarrow\quad m_5 = x_1\,\bar x_2\,x_3")
    d.P("Why: an AND is 1 only when every piece is 1. $x_1$, $\\bar x_2$ and $x_3$ are all 1 only when $x_1=1, x_2=0, x_3=1$.")
    d.P(
        "**Canonical SOP** (sum of products): OR together the minterms of **every row where $f=1$**. "
        "Why: $f$ is 1 if you're in any one of those rows."
    )
    d.E(r"\text{Two switches: } f = m_0+m_1+m_3 = \bar x_1\bar x_2 + \bar x_1x_2 + x_1x_2 = \textstyle\sum m(0,1,3)", cite("L", 35))
    sub(d, "Maxterms and canonical POS (use the 0 rows)")
    d.P(
        "A **maxterm** is an OR of **all** the variables that equals 0 in exactly one row.\n\n"
        "**Rule (the opposite of minterms):** a 0 bit → plain. A 1 bit → with a bar."
    )
    d.E(r"\text{Row 5} = 101 \quad\Rightarrow\quad M_5 = \bar x_1 + x_2 + \bar x_3")
    d.P("Why: an OR is 0 only when every piece is 0. $\\bar x_1$, $x_2$ and $\\bar x_3$ are all 0 only at $101$.")
    d.P(
        "**Canonical POS** (product of sums): AND together the maxterms of **every row where $f=0$**. "
        "Why: each maxterm forces $f$ to 0 in its own row and is 1 everywhere else."
    )
    d.E(r"\text{Two switches: only row 2 is 0, so } f = M_2 = \bar x_1 + x_2 = \textstyle\prod M(2)", cite("L", 43))
    sub(d, "Shorthand, and the table on your formula sheet")
    bullets(
        d,
        [
            r"$\sum m(\ldots)$ lists the **1 rows**. $\prod M(\ldots)$ lists the **0 rows**.",
            r"They are the same function with the row numbers split up: $\sum m(1,4,5,6) = \prod M(0,2,3,7)$.",
            r"**SOP** in general = an OR of AND terms, like $x_2 + x_1\bar x_3$. **POS** = an AND of OR terms, like $(x_1+x_3)(\bar x_2+\bar x_3)$.",
            "**Canonical** means every term uses every variable (minterms/maxterms). It's correct but usually not the shortest.",
        ],
        cites=cite("L", 39, 43),
    )
    d.T(
        ["Row", "$x_1x_2x_3$", "Minterm $m_i$", "Maxterm $M_i$"],
        [
            [
                i,
                f"{a}{b}{c}",
                "$" + "".join(f"x_{k}" if v else f"\\bar x_{k}" for k, v in enumerate((a, b, c), 1)) + "$",
                "$" + "+".join(f"\\bar x_{k}" if v else f"x_{k}" for k, v in enumerate((a, b, c), 1)) + "$",
            ]
            for i, (a, b, c) in enumerate(product((0, 1), repeat=3))
        ],
        cite("FORM", 2),
    )
    d.Q(
        "Try it: both canonical forms",
        "For \"at least two of three inputs\" (1 rows: 3, 5, 6, 7), write the canonical SOP and the canonical POS.",
        [
            S("SOP: one minterm per 1 row.", r"f=\bar x_1x_2x_3+x_1\bar x_2x_3+x_1x_2\bar x_3+x_1x_2x_3"),
            S(
                "POS: the 0 rows are 0, 1, 2, 4. One maxterm per 0 row.",
                r"f=(x_1+x_2+x_3)(x_1+x_2+\bar x_3)(x_1+\bar x_2+x_3)(\bar x_1+x_2+x_3)",
            ),
        ],
        r"$\sum m(3,5,6,7) = \prod M(0,1,2,4)$, written out as above.",
    )

    heading(d, "4. Simplifying with Boolean algebra", cite("L", 23, 24, 36, 40))
    d.P(
        "Canonical forms are correct but big, and big means more gates. "
        "The exam asks for the **minimum** SOP or POS: the fewest terms and letters. "
        "Three rules do almost all the work (the numbers match your formula sheet):"
    )
    bullets(
        d,
        [
            r"**Combining (14a):** $xy + x\bar y = x$. Two terms that match except one variable is flipped → drop that variable. "
            r"Example: $\bar x_1x_2\bar x_3 + \bar x_1x_2x_3 = \bar x_1x_2$.",
            r"**Reuse a term (7b):** $x + x = x$. You can copy a term and use it in two different pairs.",
            r"**Absorption (13a):** $x + xy = x$. Example: $x_2 + x_1x_2 = x_2$ (if $x_2$ is already 1, the second term adds nothing).",
        ],
        cites=cite("FORM", 2),
    )
    d.P(
        "**How to spot pairs fast:** two minterms combine when their row numbers differ in **exactly one bit**. "
        "Rows 2 (010) and 3 (011) differ only in $x_3$, so $x_3$ drops out."
    )
    d.X(
        "Past midterm Q1: canonical SOP → minimum SOP",
        r"$f(x_1,x_2,x_3) = \sum m(2,3,4,6,7)$. Find the canonical SOP, then the minimum SOP.",
        [
            S("Canonical SOP: one minterm per listed row.", r"f=\bar x_1x_2\bar x_3+\bar x_1x_2x_3+x_1\bar x_2\bar x_3+x_1x_2\bar x_3+x_1x_2x_3"),
            S("Pair $m_2+m_3$ (010, 011): $x_3$ drops.", r"\bar x_1x_2\bar x_3+\bar x_1x_2x_3=\bar x_1x_2"),
            S("Pair $m_6+m_7$ (110, 111): $x_3$ drops.", r"x_1x_2\bar x_3+x_1x_2x_3=x_1x_2"),
            S("Pair $m_4+m_6$ (100, 110): $x_2$ drops. Using $m_6$ twice is fine (7b).", r"x_1\bar x_2\bar x_3+x_1x_2\bar x_3=x_1\bar x_3"),
            S("The first two results pair again (14a): $x_1$ drops.", r"\bar x_1x_2+x_1x_2=x_2"),
        ],
        r"$f = x_2 + x_1\bar x_3$. Check: $x_2=1$ covers rows 2, 3, 6, 7 and $x_1\bar x_3$ covers rows 4, 6. Together that's 2, 3, 4, 6, 7 ✓",
        cite("MID", 2),
    )
    d.P(
        "**Minimum POS** works the same way on the 0 rows, using combining (14b): $(x+y)(x+\\bar y) = x$. "
        "For $\\prod M(0,2,3,7)$, pair $M_0M_2$ ($x_2$ drops) and $M_3M_7$ ($x_1$ drops):"
    )
    d.E(r"f=(x_1+x_3)(\bar x_2+\bar x_3)", cite("L", 44))
    d.Q(
        "Try it: lecture minimum SOP",
        r"Find the minimum SOP of $f = \sum m(1,4,5,6)$.",
        [
            S("$m_1$ (001) and $m_5$ (101) differ only in $x_1$.", r"m_1+m_5=\bar x_2x_3"),
            S("$m_4$ (100) and $m_6$ (110) differ only in $x_2$.", r"m_4+m_6=x_1\bar x_3"),
        ],
        r"$f=\bar x_2x_3+x_1\bar x_3$.",
        cite("L", 40),
    )
    d.Q(
        "Try it: PS1 Q1, prove with algebra",
        r"Prove $x + yz = (x+y)(x+z)$, naming each rule from the formula sheet.",
        [
            S("Start from the right side and multiply out (12a).", r"(x+y)(x+z)=xx+xz+yx+yz"),
            S("$xx = x$ (7a).", r"=x+xz+xy+yz"),
            S("Factor $x$ out of the first three terms (12a).", r"=x(1+z+y)+yz"),
            S("Anything OR 1 is 1 (5b), then $x\\cdot1=x$ (6a).", r"=x+yz"),
        ],
        "Both sides are equal; this is rule 12b.",
        cite("P1S", 1),
    )

    heading(d, "5. Drawing a circuit, and reading one back", cite("L", 14, 15, 17, 40))
    sub(d, "Expression → gates")
    bullets(
        d,
        [
            "**NOT gates first:** one for each variable that appears with a bar.",
            "**SOP:** one AND gate per product term, then one OR gate that collects them. A one-letter term skips the AND and goes straight into the OR.",
            "**POS:** one OR gate per sum term, then one AND gate that collects them.",
        ],
        ordered=True,
    )
    d.P("**Past midterm Q1 (drawing part):** draw $f = x_2 + x_1\\bar x_3$.", cite("MID", 2))
    d.F(
        circuit(
            "SOP: f = x2 + x1 NOT x3",
            [
                node("x2", "INPUT", 70, 90, label="x₂"),
                node("x1", "INPUT", 70, 200, label="x₁"),
                node("x3", "INPUT", 70, 300, label="x₃"),
                node("N3", "NOT", 250, 300, label="x̄₃"),
                node("P", "AND", 440, 230, label="x₁x̄₃"),
                node("G", "OR", 630, 150, label="x₂ + x₁x̄₃"),
                node("f", "OUTPUT", 810, 150, label="f"),
            ],
            [
                wire("x3.out", "N3.0"),
                wire("x1.out", "P.0"),
                wire("N3.out", "P.1"),
                wire("x2.out", "G.0"),
                wire("P.out", "G.1"),
                wire("G.out", "f.0"),
            ],
        ),
        "One NOT for x̄₃, one AND for the product x₁x̄₃, and an OR at the end. x₂ is a one-letter term, so it goes straight into the OR.",
        cite("MID", 2),
    )
    sub(d, "Gates → expression (working backward)")
    d.P(
        "**Method:** go left to right. Write each gate's output as an expression right on its output wire. "
        "When you reach the last gate, you have $f$."
    )
    d.P("**PS1 Q3 circuit.** What function does this circuit make? Click **Next** to label it one gate at a time.", cite("P1S", 2))
    q3 = circuit(
        "PS1 Q3",
        [
            node("x2", "INPUT", 70, 90, label="x₂"),
            node("x3", "INPUT", 70, 230, label="x₃"),
            node("x1", "INPUT", 70, 330, label="x₁"),
            node("A", "NOT", 260, 90, label="A = ?"),
            node("B", "NOT", 260, 230, label="B = ?"),
            node("C", "AND", 450, 120, label="C = ?"),
            node("D", "AND", 450, 290, label="D = ?"),
            node("G", "OR", 640, 200, label="f = ?"),
            node("f", "OUTPUT", 820, 200, label="f"),
        ],
        [
            wire("x2.out", "A.0"),
            wire("x3.out", "B.0"),
            wire("A.out", "C.0"),
            wire("x3.out", "C.1", [[160, 230], [160, 130]]),
            wire("B.out", "D.0"),
            wire("x1.out", "D.1"),
            wire("C.out", "G.0"),
            wire("D.out", "G.1"),
            wire("G.out", "f.0"),
        ],
    )
    q3_nots = relabel(q3, A="A = x̄₂", B="B = x̄₃")
    q3_ands = relabel(q3_nots, C="C = x̄₂x₃", D="D = x₁x̄₃")
    q3_done = relabel(q3_ands, G="f = x̄₂x₃ + x₁x̄₃")
    d.LOGICSTEPS(
        "Read PS1 Q3 left to right",
        [
            (
                "Start at the inputs",
                q3,
                [],
                "Every gate's output is unknown so far. Work **left to right**: a gate can only be named once the wires going into it are named.",
            ),
            (
                "The NOT gates",
                q3_nots,
                [r"$A=\bar x_2$", r"$B=\bar x_3$"],
                r"Each NOT flips its one input. $x_2$ goes into the top NOT, so $A=\bar x_2$. $x_3$ goes into the bottom NOT, so $B=\bar x_3$.",
            ),
            (
                "The AND gates",
                q3_ands,
                [r"$C=\bar x_2x_3$", r"$D=x_1\bar x_3$"],
                r"Follow each AND's two input wires back. The top AND gets $A$ and $x_3$ (the wire that branches off $x_3$), so $C = \bar x_2x_3$. "
                r"The bottom AND gets $B$ and $x_1$, so $D = x_1\bar x_3$.",
            ),
            (
                "The OR gate gives f",
                q3_done,
                [r"$f=\bar x_2x_3+x_1\bar x_3$"],
                "The OR joins $C$ and $D$:\n\n$$\nf=\\bar x_2x_3+x_1\\bar x_3\n$$\n\n"
                "That's the lecture's $\\sum m(1,4,5,6)$ from Section 4. Turn on **Try inputs** and set $x_1x_2x_3 = 101$ (row 5): every wire lights up and $f=1$.",
            ),
        ],
        cite("P1S", 2),
    )
    d.P(
        r"To get the truth table, mark the rows each term covers: $\bar x_2x_3$ is rows 1 and 5, and $x_1\bar x_3$ is rows 4 and 6. "
        "Every other row is 0."
    )

    heading(d, "6. Timing diagrams", cite("L", 18, 19))
    d.P(
        "A timing diagram draws each signal over time: **high = 1, low = 0**. "
        "Freeze one moment and read **straight down** through all the signals. That gives you one row of the truth table."
    )
    sub(d, "Circuit → waveforms (PS1 Q3)")
    d.P(
        "Same circuit as above. Feed it the inputs in counting order (000, 001, …, 111). "
        "Then work out every wire one time slot at a time, exactly like filling a truth table."
    )
    d.F(
        {
            "kind": "timing",
            "title": "PS1 Q3: every wire, slot by slot",
            "unit": "one slot = one input row (000 to 111); ideal gates, no delay",
            "signals": [
                {"name": "x1", "wave": "00001111"},
                {"name": "x2", "wave": "00110011"},
                {"name": "x3", "wave": "01010101"},
                {"name": "A = NOT x2", "wave": "11001100"},
                {"name": "B = NOT x3", "wave": "10101010"},
                {"name": "C = A AND x3", "wave": "01000100"},
                {"name": "D = x1 AND B", "wave": "00001010"},
                {"name": "f = C OR D", "wave": "01001110"},
            ],
        },
        "A is x₂ flipped, B is x₃ flipped. C is high only when A and x₃ are both high, D only when x₁ and B are both high. f is high when C or D is.",
        cite("P1S", 2),
    )
    d.P("$f$ is high in slots 1, 4, 5, 6, which matches $\\sum m(1,4,5,6)$ ✓")
    sub(d, "Waveforms → function (working backward)")
    d.P("Notice the inputs above: $x_3$ flips every slot, $x_2$ every 2, $x_1$ every 4. **That's the truth-table counting pattern turned on its side.**")
    d.P("**PS1 Q10 (textbook Figure P2.3).** Find the simplest SOP for $f$ from these waveforms.", cite("P1S", 5))
    d.F(
        {
            "kind": "timing",
            "title": "Textbook Figure P2.3",
            "unit": "equal time slots",
            "signals": [
                {"name": "x1", "wave": "00001111"},
                {"name": "x2", "wave": "00110011"},
                {"name": "x3", "wave": "01010101"},
                {"name": "f", "wave": "10010110"},
            ],
        },
        "Read straight down each slot: the inputs give the row number, f gives that row's output.",
        cite("P1S", 5),
    )
    d.X(
        "PS1 Q10 (textbook P2.3): find f from its waveforms",
        "Find the simplest SOP for $f$ from the waveforms above.",
        [
            S("The inputs count 000, 001, …, 111, so slot $i$ is row $i$."),
            S("Read $f$ in each slot: 1, 0, 0, 1, 0, 1, 1, 0.", r"f=\textstyle\sum m(0,3,5,6)"),
            S(
                "Try to pair rows: 000, 011, 101, 110 all differ from each other in **two** bits, so nothing combines.",
                r"f=\bar x_1\bar x_2\bar x_3+\bar x_1x_2x_3+x_1\bar x_2x_3+x_1x_2\bar x_3",
            ),
        ],
        "The canonical SOP above is already the simplest SOP.",
        cite("P1S", 5),
    )
    d.P("If the inputs are **not** in counting order, it still works: read each slot's inputs, turn them into a row number, and fill in that row.")

    heading(d, "7. Complementing a function (De Morgan)", cite("L", 24, 25))
    d.P("$\\bar f$ is the opposite of $f$: it is 1 wherever $f$ is 0. De Morgan's theorem (15a, 15b on your sheet) lets you push a bar through a group:")
    d.E(r"\overline{x\cdot y}=\bar x+\bar y \qquad\qquad \overline{x+y}=\bar x\,\bar y", cite("FORM", 2))
    d.P("In words: **break the bar, flip the sign.** AND becomes OR, OR becomes AND, and every letter gets flipped.")
    sub(d, "Method")
    bullets(
        d,
        [
            "**Bracket** every AND group first, so you don't lose the grouping.",
            "**Swap** every AND ↔ OR.",
            "**Flip** every letter: $x \\to \\bar x$ and $\\bar x \\to x$.",
        ],
        ordered=True,
    )
    d.X(
        "Complement the past midterm answer",
        r"Find $\bar f$ for $f = x_2 + x_1\bar x_3$.",
        [
            S("Bracket the AND group.", r"f = x_2 + (x_1\bar x_3)"),
            S("Swap the signs and flip every letter.", r"\bar f = \bar x_2\,(\bar x_1 + x_3)"),
            S(
                "Check with rows: $f$ was 1 on rows 2, 3, 4, 6, 7, so $\\bar f$ must be 1 on rows 0, 1, 5. "
                "$\\bar x_2(\\bar x_1+x_3)$ is 1 on 000, 001 and 101 ✓"
            ),
        ],
        r"$\bar f = \bar x_2(\bar x_1+x_3)$.",
    )
    callout(
        d,
        r"**Common mistake:** forgetting the brackets. The complement of $x_1 + x_2x_3$ is $\bar x_1(\bar x_2+\bar x_3)$, **not** $\bar x_1\bar x_2 + \bar x_3$.",
        "warning",
    )
    d.P("**Shortcut from a truth table:** $\\bar f$ uses the rows that $f$ doesn't. If $f = \\sum m(2,3,4,6,7)$, then $\\bar f = \\sum m(0,1,5)$.")
    d.Q(
        "Try it: complement a POS",
        r"Find $\bar f$ for $f = (x_1 + \bar x_2)\,x_3$.",
        [
            S("The outer operation is AND, so it becomes OR.", r"\bar f=\overline{x_1+\bar x_2}+\bar x_3"),
            S("Break the inner bar: OR becomes AND and the letters flip.", r"\bar f=\bar x_1x_2+\bar x_3"),
        ],
        r"$\bar f=\bar x_1x_2+\bar x_3$.",
    )

    heading(d, "8. Venn diagrams", cite("L", 29, 30, 31))
    d.P("A Venn diagram is a picture of a function:")
    bullets(
        d,
        [
            "The **rectangle** is every possible input.",
            "The **circle** for $x$ is everywhere $x = 1$. Outside it, $x = 0$.",
            "**AND** = the overlap. **OR** = everything inside either circle. **NOT** = everything outside.",
        ],
    )
    d.P(
        "Each separate region is exactly one row (one minterm). To name a region, write 1 for each circle you're inside and 0 for each you're outside, in the order $x_1x_2x_3$. "
        "Inside $x_1$ and $x_3$ only → 101 → $m_5$. Outside everything → 000 → $m_0$.",
        cite("P1S", 3),
    )
    sub(d, "Past midterm Q3: prove De Morgan 15a with Venn diagrams")
    d.P(
        r"Prove $\overline{x\cdot y} = \bar x + \bar y$. Shade the left side, shade the right side, and show the pictures match. "
        "The marking gives 1 mark per side, so draw both.",
        cite("MID", 4),
    )
    d.P("**Left side.** First shade $x\\cdot y$ (the overlap), then flip it: $\\overline{x\\cdot y}$ is everything **except** the overlap.")
    d.F({"kind": "venn", "title": "x · y", "variables": ["x", "y"], "shaded": [3]}, "x · y: only the overlap.", cite("MID", 4))
    d.F(
        {"kind": "venn", "title": "NOT (x · y)", "variables": ["x", "y"], "shaded": [0, 1, 2]},
        "The complement of x · y: everything except the overlap.",
        cite("MID", 4),
    )
    d.P("**Right side.** $\\bar x$ is everything outside circle $x$. $\\bar y$ is everything outside circle $y$. OR keeps anything shaded in **either** picture.")
    d.F({"kind": "venn", "title": "NOT x", "variables": ["x", "y"], "shaded": [0, 1]}, "x̄: everything outside circle x.", cite("P1S", 1))
    d.F({"kind": "venn", "title": "NOT y", "variables": ["x", "y"], "shaded": [0, 2]}, "ȳ: everything outside circle y.", cite("P1S", 1))
    d.F(
        {"kind": "venn", "title": "NOT x + NOT y", "variables": ["x", "y"], "shaded": [0, 1, 2]},
        "x̄ + ȳ: shaded in either picture above. Only the overlap is left blank.",
        cite("P1S", 1),
    )
    d.P("The last picture matches $\\overline{x\\cdot y}$ exactly, so the two sides are equal ✓")
    d.F(
        {"kind": "venn", "title": "Try it: which function is this?", "variables": ["x1", "x2", "x3"], "shaded": [2, 4, 6]},
        "Which function is shaded here?",
    )
    d.Q(
        "Try it: read a 3-circle diagram",
        "Write the function shaded in the 3-circle diagram above, and list its rows.",
        [
            S("Inside $x_1$ or $x_2$ is $x_1 + x_2$. Outside $x_3$ is $\\bar x_3$. Both must hold, so AND them.", r"f=(x_1+x_2)\,\bar x_3"),
            S("The regions are 010, 100 and 110."),
        ],
        r"$f=(x_1+x_2)\bar x_3 = \sum m(2,4,6)$.",
    )

    heading(d, "9. NAND–NAND and NOR–NOR", cite("L", 47, 48, 49, 50, 51))
    d.P(
        "NAND and NOR gates are the cheapest to build (you'll see why in Note 03). "
        "So exams ask you to build a circuit out of **only** NANDs or **only** NORs. Two facts make it work, and both are on the formula sheet:"
    )
    bullets(
        d,
        [
            r"**A NOT from a NAND:** tie both inputs together. $\overline{x\cdot x}=\bar x$. Same for NOR.",
            r"**A NAND is an OR with bubbles on its inputs:** $\overline{x_1x_2}=\bar x_1+\bar x_2$ (De Morgan).",
        ],
        cites=cite("FORM", 2, 3),
    )
    sub(d, "SOP → NAND–NAND")
    bullets(
        d,
        [
            "**Draw** the normal AND–OR circuit from the SOP.",
            "**Replace** every AND and the final OR with a NAND.",
            "**One-letter terms** go straight into the last gate, so feed them in **flipped** ($x_2$ goes in as $\\bar x_2$).",
            "**NOT gates** become NANDs with their inputs tied together.",
        ],
        ordered=True,
    )
    d.STEPS(
        "Why AND–OR becomes NAND–NAND",
        [
            (r"f = P + Q", "Start with two product terms, $P$ and $Q$ (each one is an AND)."),
            (r"f = \overline{\overline{P + Q}}", "Flip twice. This changes nothing."),
            (r"f = \overline{\bar P\cdot\bar Q}", "Break the inner bar (De Morgan)."),
            (
                r"f = \operatorname{NAND}\big(\operatorname{NAND}(\ldots),\,\operatorname{NAND}(\ldots)\big)",
                "$\\bar P$ is a NAND of $P$'s letters, and the outside is a NAND too.",
            ),
        ],
        cite("L", 48, 49),
    )
    and_or = circuit(
        "f = x2 + x1 NOT x3",
        [
            node("x2", "INPUT", 70, 90, label="x₂"),
            node("x1", "INPUT", 70, 200, label="x₁"),
            node("x3", "INPUT", 70, 300, label="x₃"),
            node("N1", "NOT", 260, 300, label="x̄₃"),
            node("P", "AND", 450, 230, label="x₁x̄₃"),
            node("G", "OR", 640, 150, label="x₂ + x₁x̄₃"),
            node("f", "OUTPUT", 820, 150, label="f"),
        ],
        [
            wire("x3.out", "N1.0"),
            wire("x1.out", "P.0"),
            wire("N1.out", "P.1"),
            wire("x2.out", "G.0"),
            wire("P.out", "G.1"),
            wire("G.out", "f.0"),
        ],
    )
    swapped = regate(relabel(and_or, P="NOT(x₁x̄₃)", G="x̄₂ + x₁x̄₃  ✗"), P="NAND", G="NAND")
    flipped = copy.deepcopy(swapped)
    flipped["nodes"].append(node("N2", "NOT", 260, 90, label="x̄₂"))
    flipped["wires"] = [w for w in flipped["wires"] if w["end"] != "G.0"] + [wire("x2.out", "N2.0"), wire("N2.out", "G.0")]
    flipped = relabel(flipped, G="x₂ + x₁x̄₃  ✓")
    nands = regate(relabel(flipped, N1="x̄₃ (tied NAND)", N2="x̄₂ (tied NAND)"), N1="NAND", N2="NAND")
    nands["wires"] += [wire("x3.out", "N1.1"), wire("x2.out", "N2.1")]
    d.LOGICSTEPS(
        "Past midterm Q1: turn AND–OR into NAND–NAND",
        [
            (
                "Draw the normal AND–OR circuit",
                and_or,
                [],
                r"Start from the minimum SOP $f=x_2+x_1\bar x_3$: one NOT for $\bar x_3$, one AND for $x_1\bar x_3$, and an OR at the end.",
            ),
            (
                "Swap the AND and the OR for NANDs",
                swapped,
                [],
                r"The NAND on the product outputs $\overline{x_1\bar x_3}$. The last NAND flips both of its inputs and ORs them (De Morgan), so it gives back $x_1\bar x_3$. "
                r"**But it also flips $x_2$**, so right now $f=\bar x_2+x_1\bar x_3$. That's wrong. "
                "Check it with **Try inputs**: $x_2=1$, $x_1=0$ should give 1 but gives 0.",
            ),
            (
                "Flip the one-letter term",
                flipped,
                [],
                "$x_2$ went straight into the last gate, so feed it in flipped. The last NAND flips it back:\n\n$$\n"
                r"f=\overline{\bar x_2\cdot\overline{x_1\bar x_3}}=x_2+x_1\bar x_3"
                "\n$$",
            ),
            (
                "Make the NOTs out of NANDs",
                nands,
                [],
                "A NAND with both inputs tied together is a NOT. Now every gate is a NAND: **four** in total, matching the past-midterm solution. "
                "Try a few inputs: $f$ matches the AND–OR circuit on every row.",
            ),
        ],
        cite("MID", 2),
    )
    d.X(
        "Past midterm Q1 (last part): NAND-only circuit",
        r"Build $f = x_2 + x_1\bar x_3$ from NAND gates only.",
        [
            S("Make $\\bar x_3$ with a tied NAND.", r"N_1=\overline{x_3x_3}=\bar x_3"),
            S("The product $x_1\\bar x_3$ becomes a NAND.", r"N_2=\overline{x_1\bar x_3}"),
            S("$x_2$ is a one-letter term, so flip it with a tied NAND.", r"N_3=\overline{x_2x_2}=\bar x_2"),
            S("The final NAND turns the two flipped signals back into the OR.", r"f=\overline{N_3N_2}=x_2+x_1\bar x_3"),
        ],
        "Four NAND gates, as in the last step above.",
        cite("MID", 2),
    )
    sub(d, "POS → NOR–NOR")
    d.P(
        "Exactly the same recipe with NOR: draw the OR–AND circuit, replace every gate with a NOR, "
        "and feed one-letter terms in flipped. Example: $f = (x_1+x_3)(\\bar x_2+\\bar x_3)$."
    )
    d.F(
        circuit(
            "NOR-only: f = (x1 + x3)(NOT x2 + NOT x3)",
            [
                node("x1", "INPUT", 70, 90, label="x₁"),
                node("x3", "INPUT", 70, 200, label="x₃"),
                node("x2", "INPUT", 70, 320, label="x₂"),
                node("N2", "NOR", 260, 320, label="x̄₂"),
                node("N3", "NOR", 260, 220, label="x̄₃"),
                node("U", "NOR", 450, 120, label="U"),
                node("V", "NOR", 450, 280, label="V"),
                node("G", "NOR", 640, 200, label="f"),
                node("f", "OUTPUT", 820, 200, label="f"),
            ],
            [
                wire("x3.out", "N3.0"),
                wire("x3.out", "N3.1"),
                wire("x2.out", "N2.0"),
                wire("x2.out", "N2.1"),
                wire("x1.out", "U.0"),
                wire("x3.out", "U.1", [[160, 200], [160, 130]]),
                wire("N3.out", "V.0"),
                wire("N2.out", "V.1"),
                wire("U.out", "G.0"),
                wire("V.out", "G.1"),
                wire("G.out", "f.0"),
            ],
        ),
        "Tied NORs make x̄₂ and x̄₃. U and V are the two sums, flipped. The last NOR turns them back into the AND of the sums.",
    )
    bullets(
        d,
        [
            r"$U = \overline{x_1+x_3}$ and $V = \overline{\bar x_2+\bar x_3}$.",
            r"$f = \overline{U+V} = \bar U\,\bar V = (x_1+x_3)(\bar x_2+\bar x_3)$ by De Morgan ✓",
        ],
    )
    d.Q(
        "Try it: NAND-only for the lecture function",
        r"Build $f=\bar x_2x_3+x_1\bar x_3$ from NAND gates only. How many gates?",
        [
            S("Tied NANDs make $\\bar x_2$ and $\\bar x_3$."),
            S("One NAND per product.", r"P=\overline{\bar x_2x_3},\quad Q=\overline{x_1\bar x_3}"),
            S("A final NAND joins them.", r"f=\overline{PQ}=\bar x_2x_3+x_1\bar x_3"),
        ],
        "Five NAND gates: two inverters, two for the products, one at the end.",
    )

    # Every function and claim above, checked on all rows.
    assert rows(lambda a, b, c: a + b + c >= 2) == {3, 5, 6, 7}
    assert rows(lambda a, b, c: (a + b + c) % 2) == {1, 2, 4, 7}
    assert rows(lambda a, b, c: b or (a and not c)) == {2, 3, 4, 6, 7}
    assert rows(lambda a, b, c: (not b and c) or (a and not c)) == {1, 4, 5, 6}
    assert rows(lambda a, b, c: (a or c) and (not b or not c)) == {1, 4, 5, 6}
    assert rows(lambda a, b, c: not b and (not a or c)) == {0, 1, 5}
    assert rows(lambda a, b, c: not ((a or not b) and c)) == rows(lambda a, b, c: (not a and b) or not c)
    assert rows(lambda a, b, c: (a or b) and not c) == {2, 4, 6}
    assert rows(lambda a, b, c: (a + b + c) % 2 == 0) == {0, 3, 5, 6}
    assert rows(lambda x, y, z: x or (y and z)) == rows(lambda x, y, z: (x or y) and (x or z))
    waves = {"A": "11001100", "B": "10101010", "C": "01000100", "D": "00001010", "f": "01001110"}
    for i, (a, b, c) in enumerate(product((0, 1), repeat=3)):
        A, B = 1 - b, 1 - c
        C, D = A & c, a & B
        assert [int(waves[k][i]) for k in "ABCDf"] == [A, B, C, D, C | D]
        nand = lambda p, q: int(not (p and q))
        nor = lambda p, q: int(not (p or q))
        assert nand(nand(b, b), nand(a, nand(c, c))) == int(b or (a and not c))
        assert nor(nor(a, c), nor(nor(b, b), nor(c, c))) == int((a or c) and (not b or not c))
        assert nand(nand(nand(b, b), c), nand(a, nand(c, c))) == int((not b and c) or (a and not c))
        assert int("10010110"[i]) == ((a + b + c) % 2 == 0)
    return d


def g(name):
    return {"gate": name}


def ser(*parts):
    return {"series": list(parts)}


def par(*parts):
    return {"parallel": list(parts)}


def cmos(title, pdn, **kw):
    return {"kind": "cmos", "title": title, "pdn": pdn, **kw}


def row(spec, **inputs):
    return {**spec, "inputs": inputs}


def pdn_on(n, env):
    """Does this NMOS network connect f to ground for these inputs?"""
    if "gate" in n:
        return env[n["gate"]] == 1
    return (all if "series" in n else any)(pdn_on(c, env) for c in n.get("series") or n["parallel"])


def pun_on(n, env):
    """The dual PMOS network: series and parallel swapped, each PMOS on for a 0."""
    if "gate" in n:
        return env[n["gate"]] == 0
    return (any if "series" in n else all)(pun_on(c, env) for c in n.get("series") or n["parallel"])


def ones(pdn, n=3):
    """Rows where the CMOS gate outputs 1, checking that exactly one network conducts on every row."""
    out = set()
    for i, bits in enumerate(product((0, 1), repeat=n)):
        env = {f"x{k}": v for k, v in enumerate(bits, 1)}
        assert pdn_on(pdn, env) != pun_on(pdn, env), "PUN and PDN must never both conduct (or both be off)"
        if pun_on(pdn, env):
            out.add(i)
    return out


def section3():
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

    def answer(title, text, cites=()):
        d.add("solution", cites, title=title, text=text.strip(), collapsed=True)

    def ask(text, cites=()):
        d.P(text, cites)

    # ------------------------------------------------------------ 1
    heading(d, "1. The two transistors", cite("C", 6, 8, 10))
    d.T(
        ["", "On when input is", "Goes"],
        [["**NMOS**", "**1**", "bottom (between $f$ and ground)"], ["**PMOS** (has a bubble)", "**0**", "top (between $V_{DD}$ and $f$)"]],
        cite("FORM", 3),
    )
    d.P("Every CMOS circuit: **PMOS on top, NMOS on the bottom, $f$ in the middle.** (This table is on your formula sheet.)", cite("C", 17))

    # ------------------------------------------------------------ 2
    heading(d, "2. The rule", cite("C", 17, 24))
    bullets(d, ["**AND** ($\\cdot$) = **series** (one under the other)", "**OR** ($+$) = **parallel** (side by side)"])
    d.P("Draw one half **normal** (exactly as the expression says) and the other half **swapped** (series ↔ parallel). Which half is normal depends on the shape of $f$:")
    d.T(
        ["$f$ looks like", "PMOS (top)", "NMOS (bottom)"],
        [
            [r"**every letter barred:** $\bar x_1+\bar x_2\bar x_3$", "**normal**", "swapped"],
            [r"**one bar over plain letters:** $\overline{x_1+x_2x_3}$", "swapped", "**normal**"],
            [r"**no bars at all:** $x_1+x_2x_3$", "swapped", "**normal**, then a NOT on the output"],
        ],
        cite("C", 24),
    )
    d.P("Label every transistor with the plain letter ($x_1$, never $\\bar x_1$).")
    b1 = ser(g("x1"), par(g("x2"), g("x3")))
    d.LOGICSTEPS(
        r"Every letter barred: $f=\bar x_1+\bar x_2\bar x_3$",
        [
            ("PMOS normal", cmos("f = NOT x1 + NOT x2 NOT x3", b1, show="pun"), [], r"$\bar x_1+\bar x_2\bar x_3$: $x_1$ **parallel** with ($x_2$ **series** $x_3$)."),
            ("NMOS swapped", cmos("f = NOT x1 + NOT x2 NOT x3", b1), [], r"Same letters, series ↔ parallel: $x_1$ **series** with ($x_2$ **parallel** $x_3$). Done."),
        ],
        cite("C", 24),
    )
    b3 = par(g("x1"), ser(g("x2"), g("x3")))
    d.LOGICSTEPS(
        r"One bar over plain letters: $f=\overline{x_1+x_2x_3}$",
        [
            ("NMOS normal", cmos("f = NOT(x1 + x2 x3)", b3, show="pdn"), [], r"$x_1+x_2x_3$: $x_1$ **parallel** with ($x_2$ **series** $x_3$)."),
            ("PMOS swapped", cmos("f = NOT(x1 + x2 x3)", b3), [], r"Same letters, series ↔ parallel: $x_1$ **series** with ($x_2$ **parallel** $x_3$). Done."),
        ],
    )

    # ------------------------------------------------------------ 3
    heading(d, "3. Draw it", cite("C", 19, 21, 24, 25))
    d.P("For each one: which shape is it, then draw both halves. Open the answer to check.")

    nand = ser(g("x1"), g("x2"))
    ask(r"**Q1 (lecture NAND).** Draw a CMOS circuit for $f=\overline{x_1x_2}$.", cite("C", 19))
    answer(
        "Answer",
        "Bar over plain letters → **NMOS normal, PMOS swapped.**\n\n"
        "- NMOS: $x_1$ **series** $x_2$\n- PMOS: $x_1$ **parallel** $x_2$\n\n"
        + figure(cmos("CMOS NAND", nand), "4 transistors."),
    )

    nor = par(g("x1"), g("x2"))
    ask(r"**Q2 (lecture NOR).** Draw a CMOS circuit for $f=\overline{x_1+x_2}$.", cite("C", 21))
    answer(
        "Answer",
        "Bar over plain letters → **NMOS normal, PMOS swapped.**\n\n"
        "- NMOS: $x_1$ **parallel** $x_2$\n- PMOS: $x_1$ **series** $x_2$\n\n"
        + figure(cmos("CMOS NOR", nor), "4 transistors."),
    )

    ask(r"**Q3 (lecture Example B.1).** Draw a CMOS circuit for $f=\bar x_1+\bar x_2\bar x_3$.", cite("C", 24))
    answer(
        "Answer",
        "Every letter barred → **PMOS normal, NMOS swapped.**\n\n"
        "- PMOS: $x_1$ **parallel** ($x_2$ **series** $x_3$)\n- NMOS: $x_1$ **series** ($x_2$ **parallel** $x_3$)\n\n"
        + figure(cmos("Example B.1", b1), "6 transistors."),
    )

    q4 = ser(par(g("x1"), g("x2")), g("x3"))
    ask(r"**Q4.** Draw a CMOS circuit for $f=\overline{(x_1+x_2)\,x_3}$.")
    answer(
        "Answer",
        "Bar over plain letters → **NMOS normal, PMOS swapped.**\n\n"
        "- NMOS: ($x_1$ **parallel** $x_2$) **series** $x_3$\n- PMOS: ($x_1$ **series** $x_2$) **parallel** $x_3$\n\n"
        + figure(cmos("f = NOT((x1 + x2) x3)", q4), "6 transistors."),
    )

    b2 = ser(g("x1"), par(ser(g("x2"), g("x3")), g("x4")))
    ask(r"**Q5 (lecture Example B.2).** Draw a CMOS circuit for $f=\bar x_1+(\bar x_2+\bar x_3)\,\bar x_4$.", cite("C", 25))
    answer(
        "Answer",
        "Every letter barred → **PMOS normal, NMOS swapped.**\n\n"
        "- PMOS: $x_1$ **parallel** [ ($x_2$ **parallel** $x_3$) **series** $x_4$ ]\n"
        "- NMOS: $x_1$ **series** [ ($x_2$ **series** $x_3$) **parallel** $x_4$ ]\n\n"
        + figure(cmos("Example B.2", b2), "8 transistors."),
    )

    q5 = ser(g("x4"), par(g("x1"), g("x2"), g("x3")))
    ask(
        r"**Q6 (PS2 Q5).** Derive a CMOS complex gate for the minimum SOP of $f(x_1,x_2,x_3,x_4)=\sum m(0,1,2,4,6,8,10,12,14)$.",
        cite("P2", 2),
    )
    answer(
        "PS2 Q5: answer",
        "**Simplify first.** All the even rows are the rows with $x_4=0$, so they give $\\bar x_4$. Row 1 pairs with row 0 to give $\\bar x_1\\bar x_2\\bar x_3$.\n\n"
        "$$\nf=\\bar x_4+\\bar x_1\\bar x_2\\bar x_3\n$$\n\n"
        "Every letter barred → **PMOS normal, NMOS swapped.**\n\n"
        "- PMOS: $x_4$ **parallel** ($x_1$ **series** $x_2$ **series** $x_3$)\n"
        "- NMOS: $x_4$ **series** ($x_1$ **parallel** $x_2$ **parallel** $x_3$)\n\n"
        + figure(cmos("PS2 Q5", q5), "8 transistors."),
        cite("P2S", 3),
    )

    mixed = ser(g("x1"), g("y"))
    ask(r"**Q7 (mixed bars).** Draw a CMOS circuit for $f=\bar x_1+x_2$.")
    answer(
        "Answer",
        "$x_2$ has no bar, so it doesn't fit either shape. **Fix:** make $y=\\bar x_2$ with a NOT gate. Then $x_2=\\bar y$ and\n\n"
        "$$\nf=\\bar x_1+\\bar y\n$$\n\n"
        "Now every letter is barred → **PMOS normal, NMOS swapped.**\n\n"
        "- PMOS: $x_1$ **parallel** $y$\n- NMOS: $x_1$ **series** $y$\n\n"
        + figure(cmos("f = NOT x1 + x2, with y = NOT x2", mixed), "4 transistors + 2 for the NOT gate that makes y = 6."),
    )

    sub(d, "No bars at all")
    d.P(
        "A CMOS gate always comes out with a bar on top. So for $f$ with no bars: draw the gate for $\\bar f$ "
        "(**NMOS normal, PMOS swapped**), then add a **NOT gate** (2 transistors) on its output to flip it back.",
        cite("C", 23),
    )

    def plain(title, pdn, nmos, pmos, count, caption=""):
        return (
            "No bars → draw $\\bar f$ (**NMOS normal, PMOS swapped**), then a NOT on the output.\n\n"
            f"- NMOS: {nmos}\n- PMOS: {pmos}\n\n"
            + figure(cmos(title, pdn, output="g"), caption or "This gate gives g = f̄. A NOT gate after g gives f.")
            + f"\n\n**{count}**"
        )

    and2 = ser(g("x1"), g("x2"))
    ask(r"**Q8 (lecture AND).** Draw a CMOS circuit for $f=x_1x_2$.", cite("C", 23))
    answer("Answer", plain("NAND first", and2, "$x_1$ **series** $x_2$", "$x_1$ **parallel** $x_2$", "4 + 2 = 6 transistors (a NAND, then a NOT)."))

    p9 = par(g("x1"), ser(g("x2"), g("x3")))
    ask(r"**Q9.** Draw a CMOS circuit for $f=x_1+x_2x_3$.")
    answer("Answer", plain("g = NOT(x1 + x2 x3)", p9, "$x_1$ **parallel** ($x_2$ **series** $x_3$)", "$x_1$ **series** ($x_2$ **parallel** $x_3$)", "6 + 2 = 8 transistors."))

    p10 = ser(par(g("x1"), g("x2")), par(g("x3"), g("x4")))
    ask(r"**Q10.** Draw a CMOS circuit for $f=(x_1+x_2)(x_3+x_4)$.")
    answer(
        "Answer",
        plain(
            "g = NOT((x1 + x2)(x3 + x4))",
            p10,
            "($x_1$ **parallel** $x_2$) **series** ($x_3$ **parallel** $x_4$)",
            "($x_1$ **series** $x_2$) **parallel** ($x_3$ **series** $x_4$)",
            "8 + 2 = 10 transistors.",
        ),
    )

    p11 = ser(g("x1"), par(g("x2"), g("x3")))
    ask(r"**Q11 (simplify first).** Draw a CMOS circuit for $f=x_1x_2+x_1\bar x_2x_3$.")
    answer(
        "Answer",
        "It has a bar, but it simplifies away (factor $x_1$, then 16a):\n\n"
        "$$\nf=x_1(x_2+\\bar x_2x_3)=x_1(x_2+x_3)\n$$\n\n"
        + plain("g = NOT(x1 (x2 + x3))", p11, "$x_1$ **series** ($x_2$ **parallel** $x_3$)", "$x_1$ **parallel** ($x_2$ **series** $x_3$)", "6 + 2 = 8 transistors."),
    )
    for spec, f, n in (
        (and2, lambda a, b: a and b, 2),
        (p9, lambda a, b, c: a or (b and c), 3),
        (p10, lambda a, b, c, e: (a or b) and (c or e), 4),
        (p11, lambda a, b, c: (a and b) or (a and not b and c), 3),
    ):
        assert ones(spec, n) == set(range(2**n)) - rows(f, n)  # the gate gives f̄; the NOT makes f

    # ------------------------------------------------------------ 4
    heading(d, "4. Read it", cite("P2", 1, 2))
    d.P("Going backwards: read the **NMOS half normally** (series = $\\cdot$, parallel = $+$), then put **one bar over the whole thing**.")
    q3 = par(g("x2"), ser(g("x1"), g("x3")))
    ask("**Q12 (PS2 Q3).** Only the NMOS half is given. Find $f$ and draw the missing PMOS half.", cite("P2", 1))
    d.F(cmos("PS2 Q3", q3, show="pdn"), "PS2 Q3: the given NMOS half.", cite("P2", 1))
    answer(
        "PS2 Q3: answer",
        "NMOS read normally: $x_2$ parallel ($x_1$ series $x_3$) = $x_2+x_1x_3$. Bar over it:\n\n"
        "$$\nf=\\overline{x_2+x_1x_3}\n$$\n\n"
        "PMOS = swapped: $x_2$ **series** ($x_1$ **parallel** $x_3$).\n\n" + figure(cmos("PS2 Q3", q3), "The finished circuit."),
        cite("P2S", 2),
    )

    q4d = ser(g("x1"), par(ser(g("x2"), g("x3")), g("x4")))
    q4_ones = ones(q4d, 4)
    ask("**Q13 (PS2 Q4).** Find $f$ for this circuit, and list the rows where $f=1$.", cite("P2", 2))
    d.F(cmos("PS2 Q4", q4d), "PS2 Q4, redrawn.", cite("P2", 2))
    answer(
        "PS2 Q4: answer",
        "NMOS read normally: $x_1$ series [ ($x_2$ series $x_3$) parallel $x_4$ ] = $x_1(x_2x_3+x_4)$. Bar over it:\n\n"
        "$$\nf=\\overline{x_1(x_2x_3+x_4)}\n$$\n\n"
        "$f=0$ only when $x_1=1$ **and** ($x_4=1$ or $x_2x_3=1$). Every other row is 1:\n\n"
        "$$\nf=\\sum m(" + ",".join(map(str, sorted(q4_ones))) + ")\n$$",
        cite("P2S", 3),
    )

    twice = par(ser(g("x1"), g("x2")), ser(g("x1"), g("x3")))
    ask("**Q14.** Find $f$ for this circuit. Which earlier question does it match?")
    d.F(cmos("Q14", twice), "Read the NMOS half.")
    answer(
        "Answer",
        "NMOS: $x_1x_2+x_1x_3=x_1(x_2+x_3)$. Bar over it, then De Morgan:\n\n"
        "$$\nf=\\overline{x_1(x_2+x_3)}=\\bar x_1+\\bar x_2\\bar x_3\n$$\n\n"
        "Same function as Q3, but 8 transistors instead of 6. Simplify before you draw.",
    )

    # ------------------------------------------------------------ 5
    heading(d, "5. NMOS-only gates and counting", cite("C", 11, 12, 13, 23))
    d.P("**NMOS-only gate:** a resistor on top instead of PMOS. Draw the NMOS half normally, same as before.", cite("C", 11))
    ask(r"**Q15.** What gate is this? When $x_1=1$, $x_2=0$, what is $f$, and does current flow?", cite("C", 13))
    d.F(cmos("NMOS gate", nor, pullup="resistor"), "Resistor on top, two NMOS below.", cite("C", 13))
    answer(
        "Answer",
        "NMOS read normally: $x_1+x_2$. Bar over it: $f=\\overline{x_1+x_2}$, a **NOR**.\n\n"
        "$x_1=1$ closes its switch, so $f$ is connected to ground: $f=0$. **Yes**, current flows $V_{DD}$ → resistor → ground. "
        "That wasted power is why CMOS uses PMOS instead of a resistor.\n\n"
        + figure(cmos("NMOS NOR, row 10", nor, pullup="resistor", inputs={"x1": 1, "x2": 0}), "Green = the path the current takes."),
    )
    d.T(
        ["Gate", "Transistors"],
        [["NOT", "2"], ["$n$-input NAND or NOR", "$2n$"], ["$n$-input AND or OR", "$2n+2$ (NAND/NOR + NOT)"], ["Complex gate (section 3)", "2 per letter"]],
        cite("C", 23),
    )
    ask("**Q16 (PS2 Q1).** A circuit has three NOT gates, four 3-input AND gates and one 4-input OR gate. How many CMOS transistors?", cite("P2", 1))
    answer(
        "PS2 Q1: answer",
        "$$\n3(2)+4(2\\cdot3+2)+(2\\cdot4+2)=6+32+10=48\n$$",
        cite("P2S", 1),
    )

    # Every drawing gives the function claimed, and its PUN and PDN never conduct together.
    assert ones(b1) == rows(lambda a, b, c: not a or (not b and not c)) == ones(twice)
    assert ones(b3) == rows(lambda a, b, c: not (a or (b and c)))
    assert ones(nand, 2) == {0, 1, 2} and ones(nor, 2) == {0}
    assert ones(q4) == rows(lambda a, b, c: not ((a or b) and c))
    assert ones(b2, 4) == rows(lambda a, b, c, e: not a or ((not b or not c) and not e), 4)
    assert ones(q5, 4) == {0, 1, 2, 4, 6, 8, 10, 12, 14}
    assert ones(q3) == rows(lambda a, b, c: not (b or (a and c)))
    assert q4_ones == {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12}
    for a, b in product((0, 1), repeat=2):  # Q7: y = NOT x2 feeds the gate
        env = {"x1": a, "y": 1 - b}
        assert pun_on(mixed, env) == (not a or b) != pdn_on(mixed, env)
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
        section1(),
        section2(),
        section3(),
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
