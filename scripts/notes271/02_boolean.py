"""Section 2: gates, network analysis, Boolean algebra, and Venn reasoning."""

from itertools import product

from lib import Doc, S, circuit, cite, node, wire

for a, b, c in product((0, 1), repeat=3):
    assert ((not a) or (a and b)) == ((not a) or b)
    assert (a or (b and c)) == ((a or b) and (a or c))
    assert ((a and b) or ((not a) and c) or (b and c)) == ((a and b) or ((not a) and c))
    assert not (a and b) == ((not a) or (not b))

D = Doc(2, "Logic Gates and Boolean Algebra", ["logic_gates", "boolean_algebra", "truth_tables"])
D.H("Topic 1: Gates and truth tables", cite("L", 7, 10, 11, 13))
D.P(
    "A logic variable takes values 0 and 1. Here $+$ means OR, adjacency or $\\cdot$ means AND, and a bar means NOT.\n\n- $AB=1$ only if both inputs are 1.\n- $A+B=1$ if either or both inputs are 1.\n- $\\overline A$ reverses a single bit.\n\nNOT is evaluated first, then AND, then OR; parentheses override that order.",
    cite("L", 7, 10, 32),
)
D.T(
    ["A", "B", "AB", "A+B", r"$\overline{AB}$", r"$\overline{A+B}$", r"$A\oplus B$"],
    [[a, b, a & b, a | b, 1 - (a & b), 1 - (a | b), a ^ b] for a, b in product((0, 1), repeat=2)],
    cite("L", 11, 47),
)
D.P(
    "**NAND** is an AND followed by NOT; **NOR** is an OR followed by NOT. The small output bubble means inversion.\n\n**XOR**, $A\\oplus B$, is 1 when the inputs differ. XNOR is 1 when they match. XOR is not ordinary OR: $1\\oplus1=0$.",
    cite("L", 47),
)
D.F(
    circuit(
        "A simple gate network",
        [
            node("A", "INPUT", 70, 90),
            node("B", "INPUT", 70, 170),
            node("C", "INPUT", 250, 250),
            node("G", "OR", 250, 130),
            node("H", "AND", 440, 190),
            node("F", "OUTPUT", 620, 190),
        ],
        [
            wire("A.out", "G.0"),
            wire("B.out", "G.1"),
            wire("G.out", "H.0"),
            wire("C.out", "H.1"),
            wire("H.out", "F.0"),
        ],
    ),
    "An OR output feeds an AND: F=(A+B)C.",
    cite("L", 14),
)
D.X(
    "Read a circuit from left to right",
    r"For the diagram above, find $F$ and evaluate it at $A=0,B=1,C=0$.",
    [
        S("Name the output of the OR gate.", r"G=A+B"),
        S("The AND requires both G and C.", r"F=(A+B)C"),
        S("Substitute the input values.", r"F=(0+1)0=0"),
    ],
    "$F=0$.",
    cite("L", 14),
)
D.P(
    "A truth table lists all $2^n$ assignments of $n$ independent inputs. Keep the leftmost input as the MSB and list rows in binary order so no assignment is missed.",
    cite("L", 11, 12),
)
D.X(
    "Lecture network: track internal signals",
    r"Let $P=\overline A$, $Q=AB$, and $F=P+Q$. Find the complete output column.",
    [
        S("For AB=00,01,10,11, the inverter output is 1,1,0,0."),
        S("For those same rows, AB is 0,0,0,1."),
        S("OR the corresponding internal values.", r"F=1,1,0,1"),
    ],
    r"$F=\overline A+AB=\overline A+B$. Different gate networks can have the same truth table.",
    cite("L", 15, 20),
)
D.F(
    {
        "kind": "timing",
        "title": "Ideal network waveforms",
        "unit": "one row per interval; zero delay",
        "signals": [
            {"name": "A", "wave": "0011"},
            {"name": "B", "wave": "0101"},
            {"name": "P = NOT A", "wave": "1100"},
            {"name": "Q = A AND B", "wave": "0001"},
            {"name": "F = P OR Q", "wave": "1101"},
        ],
    },
    "Read vertically to evaluate one instant; read horizontally to follow a signal.",
    cite("L", 19),
)
D.P(
    "These are **ideal** waveforms: outputs change immediately. A physical gate has propagation delay, so a truth table alone does not describe glitches during a transition.",
    cite("L", 19, 37),
)
D.Q(
    "Try it: distinguish OR from XOR",
    r"For $F=A+B$ and $G=A\oplus B$, find every input row where $F\ne G$.",
    [S("Both give 0 at 00 and 1 at 01 and 10."), S("At 11, OR remains 1 while XOR is 0.")],
    "Only A=B=1.",
)
D.H("Topic 2: Simplifying expressions", cite("L", 23, 24))
D.P(
    "A **literal** is a variable or its complement. Simplification preserves every truth-table row while reducing the hardware needed to implement the expression.",
    cite("L", 21, 37, 38),
)
D.T(
    ["Rule", "OR form", "AND form"],
    [
        ["Identity", r"$A+0=A$", r"$A\cdot1=A$"],
        ["Domination", r"$A+1=1$", r"$A\cdot0=0$"],
        ["Idempotence", r"$A+A=A$", r"$AA=A$"],
        ["Complement", r"$A+\overline A=1$", r"$A\overline A=0$"],
        ["Absorption", r"$A+AB=A$", r"$A(A+B)=A$"],
        ["Distributive", r"$A+BC=(A+B)(A+C)$", r"$A(B+C)=AB+AC$"],
    ],
    cite("L", 23, 24),
)
D.P(
    "AND and OR are also commutative and associative: you may reorder inputs and regroup repeated instances of the same operation. Boolean $A+A=A$, so ordinary arithmetic cancellation is not valid.",
    cite("L", 24),
)
D.STEPS(
    "Absorb a redundant literal",
    [
        (r"\overline A+AB", "Start with the lecture network."),
        (r"(\overline A+A)(\overline A+B)", "Distribute OR over AND."),
        (r"1(\overline A+B)", "A variable OR its complement is 1."),
        (r"\overline A+B", "Remove the identity factor."),
    ],
    cite("L", 20, 24),
)
D.X(
    "Problem 1b: prove the second distributive law",
    r"Prove $x+yz=(x+y)(x+z)$.",
    [
        S("Expand the right-hand side.", r"(x+y)(x+z)=xx+xz+xy+yz"),
        S("Use xx=x, then absorption twice.", r"x+xz+xy+yz=x+yz"),
    ],
    "The expressions are equal for every x,y,z.",
    cite("P1B", 1),
)
D.X(
    "Consensus: a term can already be covered",
    r"Simplify $F=AB+\overline A C+BC$.",
    [
        S("Split the last term using A + NOT A = 1.", r"BC=ABC+\overline A BC"),
        S("AB absorbs ABC; NOT A C absorbs NOT A BC.", r"F=AB+\overline A C"),
    ],
    r"$F=AB+\overline A C$. The term $BC$ adds no new 1 rows, though it can suppress a static hazard in a physical implementation.",
    cite("L", 24, 31),
)
D.Q(
    "Try it: factor before expanding",
    r"Simplify $(A+B)(A+\overline B)$.",
    [
        S("Apply the OR-over-AND distributive law backward.", r"(A+B)(A+\overline B)=A+B\overline B"),
        S("A variable AND its complement is zero.", r"A+0=A"),
    ],
    r"$A$.",
)
D.H("Topic 3: Complement, duality, and Venn reasoning", cite("L", 24, 25, 29, 30, 31))
D.E(r"\overline{AB}=\overline A+\overline B", cite("L", 25))
D.E(r"\overline{A+B}=\overline A\,\overline B", cite("L", 24))
D.P(
    "**De Morgan:** when a complement crosses a group, swap AND with OR and complement every member. The bar applies to its entire group.\n\n**Duality:** swap AND with OR and 0 with 1, leaving each literal unchanged. A dual is not generally the complement.",
    cite("L", 24),
)
D.X(
    "Complement a nested expression",
    r"Find $\overline F$ for $F=(A+\overline B)C$.",
    [
        S("Complement the outer AND first.", r"\overline F=\overline{A+\overline B}+\overline C"),
        S(
            "Complement the inner OR, removing the double complement.",
            r"\overline F=\overline A B+\overline C",
        ),
    ],
    r"$\overline A B+\overline C$.",
)
D.P(
    "In a **Venn diagram**, a circle marks the input assignments where that variable is 1.\n\n- AND shades the intersection.\n- OR shades the union.\n- NOT shades the part of the surrounding universe outside the set.\n\nTo prove equality visually, shade both expressions in identical universes and compare the resulting regions.",
    cite("L", 29, 30),
)
D.X(
    "De Morgan through regions",
    r"Explain why $\overline{AB}=\overline A+\overline B$ using Venn regions.",
    [
        S("AB is the overlap of circles A and B."),
        S("Outside that overlap, a point lies outside A, outside B, or both."),
        S("Those are exactly the regions selected by NOT A OR NOT B."),
    ],
    "Both expressions shade everything except the overlap.",
    cite("P1", 1, 4),
)
D.F(
    {
        "kind": "venn",
        "title": "Everything except the intersection",
        "variables": ["A", "B"],
        "shaded": [0, 1, 2],
    },
    "The shaded regions are AB=00,01,10: NOT(AB), equivalently NOT A OR NOT B.",
    cite("L", 25, 29),
)
D.Q(
    "Try it: dual or complement?",
    r"Find both the dual and the complement of $F=A+BC$.",
    [
        S("For the dual, swap the operations but keep the literals.", r"F^{d}=A(B+C)"),
        S(
            "For the complement, also complement the literals.",
            r"\overline F=\overline A(\overline B+\overline C)",
        ),
    ],
    r"Dual $A(B+C)$; complement $\overline A(\overline B+\overline C)$.",
)
D.save()
