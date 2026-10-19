"""Canonical forms, NAND/NOR realizations, and a first complete VHDL description."""

from itertools import product

from lib import Doc, S, circuit, cite, node, wire

for a, b, c in product((0, 1), repeat=3):
    m = 4 * a + 2 * b + c
    assert (((not b) and c) or (a and not c)) == (m in {1, 4, 5, 6})
    assert (b or (a and not c)) == (m in {2, 3, 4, 6, 7})
    assert ((a or b) and (b or not c)) == (m in {2, 3, 4, 6, 7})

D = Doc(
    3, "SOP, POS, NAND/NOR Networks, and VHDL", ["logic_synthesis", "canonical_forms", "nand_nor", "vhdl"]
)
D.H("Topic 1: Build an expression from a truth table", cite("L", 34, 38, 39, 43))
D.P(
    "Fix the variable order before numbering rows. For $A,B,C$, the index is $4A+2B+C$.\n\n- A **minterm** $m_i$ is 1 at row $i$ and 0 everywhere else. AND all variables, complementing those whose row bit is 0.\n- A **maxterm** $M_i$ is 0 at row $i$ and 1 everywhere else. OR all variables, complementing those whose row bit is 1.",
    cite("L", 38),
)
D.T(
    ["Row ABC", "Index", "Minterm", "Maxterm"],
    [
        ["000", "0", r"$\overline A\overline B\overline C$", r"$A+B+C$"],
        ["101", "5", r"$A\overline B C$", r"$\overline A+B+\overline C$"],
        ["111", "7", r"$ABC$", r"$\overline A+\overline B+\overline C$"],
    ],
    cite("L", 38),
)
D.P(
    "**SOP** ORs product terms; canonical SOP uses the minterms of every 1 row. **POS** ANDs sum terms; canonical POS uses the maxterms of every 0 row. A simplified SOP/POS need not contain every variable in every term.",
    cite("L", 39, 43),
)
D.E(r"F=\sum m(1,4,5,6)=\prod M(0,2,3,7)", cite("L", 40, 44))
D.X(
    "Lecture example: canonical to simplified SOP",
    r"Derive an SOP for $F(A,B,C)=\sum m(1,4,5,6)$.",
    [
        S(
            "Write one product for each 1 row.",
            r"F=\overline A\overline B C+A\overline B\overline C+A\overline B C+AB\overline C",
        ),
        S(
            "Use m5 with m1, and m4 with m6. A term may be reused.",
            r"F=\overline B C(\overline A+A)+A\overline C(\overline B+B)",
        ),
        S("Each parenthesis is 1.", r"F=\overline B C+A\overline C"),
    ],
    r"$F=\overline B C+A\overline C$.",
    cite("L", 40),
)
D.X(
    "Read the zero rows for POS",
    r"Write a simplified POS for the same function.",
    [
        S("The zero rows are 0,2,3,7.", r"F=M_0M_2M_3M_7"),
        S("Group rows 0 and 2: A=0,C=0, so the sum term is A+C."),
        S(
            "Group rows 3 and 7: B=1,C=1, so the sum term is NOT B + NOT C.",
            r"F=(A+C)(\overline B+\overline C)",
        ),
    ],
    r"$(A+C)(\overline B+\overline C)$. A maxterm must evaluate to zero on its selected rows.",
    cite("L", 44),
)
D.P(
    "Analysis starts with a circuit and finds its function. Synthesis starts with the required behavior and chooses a circuit. Verify a synthesized circuit by comparing all input rows with the specification.",
    cite("L", 15, 52),
)
D.Q(
    "Try it: read the other canonical form",
    r"For three inputs, $F=\prod M(0,1,5)$. Write the 1-row indices and the minterm $m_6$.",
    [
        S("All rows except 0,1,5 are 1.", r"F=\sum m(2,3,4,6,7)"),
        S("Index 6 is binary 110.", r"m_6=AB\overline C"),
    ],
    r"$\sum m(2,3,4,6,7)$; $m_6=AB\overline C$.",
)
D.H("Topic 2: Use only NAND or only NOR", cite("L", 47, 48, 49, 50, 51))
D.P(
    "A tied-input NAND or NOR acts as an inverter.\n\n- SOP becomes **NAND–NAND**: complement each product, then NAND those results.\n- POS becomes **NOR–NOR**: complement each sum, then NOR those results.\n\nThe two inversions cancel by De Morgan. Required complemented literals still need to be generated.",
    cite("L", 48, 49, 50),
)
D.STEPS(
    "Convert an SOP into NANDs",
    [
        (r"F=P+Q", "Start with two product terms."),
        (r"F=\overline{\overline{P+Q}}", "Insert a double complement."),
        (r"F=\overline{\overline P\;\overline Q}", "The outer operation is a NAND."),
    ],
    cite("L", 49),
)
D.X(
    "Past midterm: a one-literal product term",
    r"Implement $F=B+A\overline C$ using only two-input NANDs.",
    [
        S("A NAND with tied inputs generates NOT C.", r"N_C=\operatorname{NAND}(C,C)=\overline C"),
        S(
            "The one-literal term B also needs its complement at the last NAND.",
            r"N_B=\operatorname{NAND}(B,B)=\overline B",
        ),
        S("Complement the other product.", r"N_P=\operatorname{NAND}(A,N_C)=\overline{A\overline C}"),
        S("The final NAND restores the desired OR.", r"F=\operatorname{NAND}(N_B,N_P)"),
    ],
    "Four two-input NAND gates when complemented inputs are not supplied.",
    cite("MID", 2),
)
D.F(
    circuit(
        "NAND-only past midterm circuit",
        [
            node("B", "INPUT", 70, 85),
            node("C", "INPUT", 70, 265),
            node("A", "INPUT", 260, 190),
            node("NB", "NAND", 260, 85),
            node("NC", "NAND", 260, 265),
            node("NP", "NAND", 450, 225),
            node("G", "NAND", 640, 145),
            node("F", "OUTPUT", 820, 145),
        ],
        [
            wire("B.out", "NB.0"),
            wire("B.out", "NB.1"),
            wire("C.out", "NC.0"),
            wire("C.out", "NC.1"),
            wire("A.out", "NP.0"),
            wire("NC.out", "NP.1"),
            wire("NB.out", "G.0"),
            wire("NP.out", "G.1"),
            wire("G.out", "F.0"),
        ],
    ),
    "Tied inputs generate NOT B and NOT C. Every drawn gate is a NAND.",
    cite("MID", 2),
)
D.X(
    "The same function with NORs",
    r"Use $F=(A+B)(B+\overline C)$ to obtain a NOR-only realization.",
    [
        S("Generate NOT C with a tied-input NOR.", r"N_C=\operatorname{NOR}(C,C)"),
        S("Complement the two sum terms.", r"U=\operatorname{NOR}(A,B),\quad V=\operatorname{NOR}(B,N_C)"),
        S("NOR the complemented sums.", r"F=\operatorname{NOR}(U,V)"),
    ],
    "Four two-input NOR gates. Confirm equivalence to the SOP on all eight rows.",
    cite("L", 51),
)
D.Q(
    "Try it: an inversion bubble changes the function",
    r"If $U=\overline{AB}$ and $V=\overline{CD}$, what does NAND(U,V) produce? What does OR(U,V) produce?",
    [
        S("Apply De Morgan to the final NAND.", r"\overline{UV}=AB+CD"),
        S("OR does not provide the final complement.", r"U+V=\overline{AB}+\overline{CD}=\overline{ABCD}"),
    ],
    r"NAND: $AB+CD$. OR: $\overline{ABCD}$.",
)
D.H("Topic 3: Describe the circuit in VHDL", cite("L", 55, 56, 57, 58, 59))
D.P(
    "An **entity** declares the interface; an **architecture** describes the hardware implementing it. Concurrent assignments describe connections that exist together, rather than a list of software operations executed once from top to bottom.",
    cite("L", 56, 57, 59),
)
D.CODE(
    """library ieee;
use ieee.std_logic_1164.all;

entity logic_example is
  port (a, b, c : in std_logic;
        f       : out std_logic);
end entity;

architecture rtl of logic_example is
begin
  f <= b or (a and not c);
end architecture;""",
    cite("L", 56, 57),
)
D.P(
    "`std_logic` includes 0 and 1 plus simulation states such as `U` (uninitialized), `X` (unknown), and `Z` (high impedance). A Boolean truth-table proof checks the binary cases; it does not establish behavior for every simulation state.",
    cite("L", 56),
)
D.X(
    "Three-way light control",
    "The light is on when an odd number of three switches is closed. Derive a compact expression.",
    [
        S("The 1 rows are 001,010,100,111.", r"F=\sum m(1,2,4,7)"),
        S("XOR tracks odd parity.", r"F=A\oplus B\oplus C"),
    ],
    "`f <= a xor b xor c;` implements the binary truth table.",
    cite("L", 52, 53),
)
D.P(
    "The design flow is specification → schematic/HDL → synthesis and functional verification → physical implementation and timing verification. A correct truth table does not guarantee that a physical implementation meets timing.",
    cite("L", 55),
)
D.Q(
    "Try it: two outputs are concurrent",
    "Does exchanging the order of `f <= a and b;` and `g <= not a;` change these two outputs?",
    [S("Each concurrent assignment defines its own logic; neither reads the other output.")],
    "No. Both connections exist concurrently. Ordering inside a process is a separate question.",
)
D.P(
    "The HDL examples in these notes are teaching descriptions. Their binary behavior is checked with the corresponding equations; no HDL simulator or synthesis run is claimed."
)
D.save()
