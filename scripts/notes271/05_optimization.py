"""PS3: K-maps, don't-cares, cost, decomposition, sharing, hazards."""

from itertools import product

from lib import Doc, S, cite
from sympy import symbols
from sympy.logic import POSform, SOPform

A, B, C, D = symbols("A B C D")
assert SOPform([A, B, C], [1, 2, 3, 5]) == ((B & ~A) | (C & ~B))
assert POSform([A, B, C], [1, 2, 3, 5]) == ((B | C) & (~A | ~B))
ones = {0, 2, 8, 9, 10, 15}
dc = {1, 3, 6, 7}
for a, b, c, d in product((0, 1), repeat=4):
    m = 8 * a + 4 * b + 2 * c + d
    sop = (b and c and d) or (not b and not c) or (not b and not d)
    pos = (c or not b) and (d or not b) and (b or not c or not d)
    if m not in dc:
        assert sop == pos == (m in ones)

D = Doc(5, "Karnaugh Maps and Logic Optimization", ["karnaugh_maps", "dont_cares", "logic_optimization"])
D.P(
    "This note develops the optimization methods requested in Problem Set 3. No separate Section 4 lecture was supplied.",
    cite("P3", 1, 2),
)
D.H("Topic 1: A map makes adjacent minterms visible", cite("P3", 1))
D.P(
    "A **Karnaugh map** rearranges a truth table so adjacent cells differ in exactly one input bit. The axes use **Gray order**: 00, 01, 11, 10. The last position is adjacent to the first.",
    cite("P3", 1),
)
D.P(
    "For SOP, group 1 cells into rectangles containing 1, 2, 4, 8, … cells.\n\n- Use horizontal/vertical neighbors, including wraparound; diagonal neighbors do not count.\n- A group may overlap another group.\n- Cover every required 1 without including any required 0.\n- A variable that changes inside a group disappears from its product term."
)
D.F(
    {
        "kind": "kmap",
        "title": "Three-input SOP grouping",
        "variables": ["A", "B", "C"],
        "ones": [1, 2, 3, 5],
        "groups": [
            {"cells": [2, 3], "label": "A=0, B=1 -> NOT A B"},
            {"cells": [1, 5], "label": "B=0, C=1 -> NOT B C"},
        ],
    },
    "Columns are BC=00,01,11,10. The two groups cover all four required 1s.",
    cite("P3", 1),
)
D.X(
    "PS3 Q1: minimum SOP",
    r"Find a minimum SOP for $F(A,B,C)=\sum m(1,2,3,5)$.",
    [
        S("Cells 2=010 and 3=011 differ only in C.", r"m_2+m_3=\overline A B"),
        S("Cells 1=001 and 5=101 differ only in A.", r"m_1+m_5=\overline B C"),
        S("OR the two implicants.", r"F=\overline A B+\overline B C"),
    ],
    r"Two products with four literals. Cell 2 forces the first pair and cell 5 forces the second; one product cannot cover all four 1s.",
    cite("P3", 1),
)
D.P(
    "An **implicant** covers only 1s and allowed Xs. A **prime implicant** cannot expand to a larger allowed group. It is **essential** if it uniquely covers a required 1. Choose essentials first, then cover any remaining 1s at the lowest allowed cost."
)
D.X(
    "The same map gives POS",
    r"Find the POS for $F=\sum m(1,2,3,5)$.",
    [
        S("The required zero rows are 0,4,6,7."),
        S("Rows 0 and 4 keep B=C=0: the factor B+C is zero there."),
        S("Rows 6 and 7 keep A=B=1: use NOT A + NOT B.", r"F=(B+C)(\overline A+\overline B)"),
    ],
    r"$(B+C)(\overline A+\overline B)$. For a zero group, a constant 0 gives an uncomplemented literal; a constant 1 gives a complemented literal.",
    cite("P3", 1),
)
D.F(
    {
        "kind": "kmap",
        "title": "Group zeros for POS",
        "variables": ["A", "B", "C"],
        "ones": [1, 2, 3, 5],
        "target": 0,
        "groups": [
            {"cells": [0, 4], "label": "B=0, C=0 -> (B+C)"},
            {"cells": [6, 7], "label": "A=1, B=1 -> (NOT A+NOT B)"},
        ],
    },
    "The POS factors identify where F must become zero.",
    cite("P3", 1),
)
D.Q(
    "Try it: four corners",
    r"A four-variable map has 1s only at 0,2,8,10. Give one product term covering all four.",
    [
        S("The corners are adjacent through both map boundaries."),
        S("A and C change; B and D stay at zero.", r"F=\overline B\,\overline D"),
    ],
    r"$\overline B\,\overline D$.",
)
D.H("Topic 2: Don’t-care conditions", cite("P3", 1))
D.P(
    "A **don’t-care** X is an input combination for which the specification allows either output. Use it as 0 or 1 when that helps simplify the circuit; it does not have to be covered.\n\nAn X is permission from the specification, not a missing answer you may choose arbitrarily."
)
D.F(
    {
        "kind": "kmap",
        "title": "Use X cells to enlarge groups",
        "variables": ["A", "B", "C", "D"],
        "ones": sorted(ones),
        "dont_cares": sorted(dc),
        "groups": [
            {"cells": [0, 1, 8, 9], "label": "NOT B NOT C"},
            {"cells": [0, 2, 8, 10], "label": "NOT B NOT D (wraparound)"},
            {"cells": [7, 15], "label": "BCD"},
        ],
    },
    "PS3 Q2: use X at 1 and 7; X at 3 and 6 need not be included.",
    cite("P3", 1),
)
D.X(
    "PS3 Q2: use Xs without changing required rows",
    r"$F=\sum m(0,2,8,9,10,15)+D(1,3,6,7)$. Find a minimum SOP.",
    [
        S("Group 0,1,8,9; B and C are zero.", r"P_1=\overline B\overline C"),
        S("Group 0,2,8,10 across the edge.", r"P_2=\overline B\overline D"),
        S("Pair required cell 15 with X cell 7.", r"P_3=BCD"),
    ],
    r"$F=\overline B\overline C+\overline B\overline D+BCD$. The chosen values on X rows are allowed to differ from another valid realization.",
    cite("P3", 1),
)
D.X(
    "A different legal choice: minimum POS",
    r"Find a POS for that same incompletely specified function.",
    [
        S("Group zero cells 4,5,12,13.", r"C+\overline B"),
        S("Use X=6 with zero cells 4,12,14.", r"D+\overline B"),
        S("Use X=3 with zero cell 11.", r"B+\overline C+\overline D"),
    ],
    r"$F=(C+\overline B)(D+\overline B)(B+\overline C+\overline D)$. Check equality only on required rows.",
    cite("P3", 1),
)
D.P(
    "For five variables, use two four-variable maps, one for each value of the fifth variable. Corresponding cells in the two maps are adjacent. A group repeated in both maps can eliminate the fifth variable.",
    cite("P3", 1),
)
D.Q(
    "Try it: when an X assumption breaks",
    "A controller treats binary input 111 as unreachable and uses it as X. Later, 111 becomes a valid command whose output must be 0. Can the old simplified circuit be accepted unchanged?",
    [
        S("The old circuit was not constrained at 111."),
        S("Evaluate that row under the new requirement and redesign if it produces 1."),
    ],
    "Only if it already produces 0 at 111; the earlier proof did not establish that.",
)
D.H("Topic 3: Minimum expression versus circuit cost", cite("P3", 1, 2))
D.P(
    "The lecture’s cost convention is **number of gates + total gate inputs**. Count inverters unless complemented inputs are supplied. Check fan-in limits and shared terms before declaring a circuit cheapest.",
    cite("L", 37, 40),
)
D.X(
    "Factoring changes cost",
    r"Compare $F=AB+AC$ with $F=A(B+C)$ using two-input AND/OR gates. Inputs are uncomplemented.",
    [
        S("Direct SOP: two ANDs and one OR.", r"C_{\mathrm{SOP}}=3+(2+2+2)=9"),
        S("Factored circuit: one OR and one AND.", r"C_{\mathrm{factored}}=2+(2+2)=6"),
    ],
    "The factored implementation has cost 6 rather than 9. A minimum SOP is not automatically a minimum-cost multilevel circuit.",
)
D.X(
    "Share a product across outputs",
    r"Compare separate and shared implementations of $F=AB+C$ and $G=AB+D$.",
    [
        S(
            "Separately, each output needs one AND and one OR: four gates, eight inputs.",
            r"C_{\mathrm{separate}}=4+8=12",
        ),
        S("Share the AND AB, then keep the two output OR gates.", r"C_{\mathrm{shared}}=3+6=9"),
    ],
    "Sharing saves one AND gate and its two inputs. PS3 Q5 asks for this type of joint optimization.",
    cite("P3", 1),
)
D.P(
    "**Functional decomposition** expresses a function using smaller intermediate functions. Shannon decomposition on input A uses cofactors $F_0=F|_{A=0}$ and $F_1=F|_{A=1}$:",
    cite("P3", 1),
)
D.E(r"F=\overline A F_0+AF_1")
D.P(
    "A two-input gate limit can make a wide SOP expensive. For example, a 4-input AND needs three 2-input ANDs; a balanced tree has two levels rather than the three levels of a serial chain. The next note on building blocks uses Shannon decomposition to construct multiplexers."
)
D.X(
    "Consensus and a static-1 hazard",
    r"For $F=AB+\overline A C$, hold $B=C=1$ while A changes from 0 to 1. What should happen logically, and what could happen physically?",
    [
        S("Before the change, NOT A C is 1; afterward, AB is 1. The ideal output remains 1."),
        S("Unequal path delays can briefly make both products zero."),
        S(
            "Add the consensus product BC, which stays high throughout.",
            r"F_{\mathrm{covered}}=AB+\overline A C+BC",
        ),
    ],
    "BC preserves the truth table and covers the transition between the two terms. This addresses the single-input static-1 hazard, not every possible dynamic or multiple-input glitch.",
    cite("L", 24, 37),
)
D.Q(
    "Try it: count with complemented inputs supplied",
    r"Count the gates-plus-inputs cost of $F=\overline A B+C\overline D$ as a direct AND–OR network when both polarities of every input are supplied.",
    [S("Use two two-input ANDs and one two-input OR; no input inverters are needed.", r"C=3+6=9")],
    "Cost 9. If complements had to be generated, the two inverters would add 2 gates + 2 inputs, giving 13.",
)
D.save()
