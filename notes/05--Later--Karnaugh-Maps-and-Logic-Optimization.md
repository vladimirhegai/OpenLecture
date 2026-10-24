# 05 · Later · Karnaugh Maps and Logic Optimization

**Later study — outside this midterm study set.** Keep this material for subsequent assessments; prioritize notes 01–03 now.

This note develops the optimization methods requested in Problem Set 3. No separate Section 4 lecture was supplied.

## Topic 1: A map makes adjacent minterms visible

A **Karnaugh map** rearranges a truth table so adjacent cells differ in exactly one input bit. The axes use **Gray order**: 00, 01, 11, 10. The last position is adjacent to the first.

For SOP, group 1 cells into rectangles containing 1, 2, 4, 8, … cells.

- Use horizontal/vertical neighbors, including wraparound; diagonal neighbors do not count.
- A group may overlap another group.
- Cover every required 1 without including any required 0.
- A variable that changes inside a group disappears from its product term.

```digital
{"kind":"kmap","title":"Three-input SOP grouping","variables":["A","B","C"],"ones":[1,2,3,5],"groups":[{"cells":[2,3],"label":"A=0, B=1 -> NOT A B"},{"cells":[1,5],"label":"B=0, C=1 -> NOT B C"}]}
```

*Columns are BC=00,01,11,10. The two groups cover all four required 1s.*

**Example: PS3 Q1: minimum SOP**

Find a minimum SOP for $F(A,B,C)=\sum m(1,2,3,5)$.

1. Cells 2=010 and 3=011 differ only in C.

   $$m_2+m_3=\overline A B$$
2. Cells 1=001 and 5=101 differ only in A.

   $$m_1+m_5=\overline B C$$
3. OR the two implicants.

   $$F=\overline A B+\overline B C$$

**Answer:** Two products with four literals. Cell 2 forces the first pair and cell 5 forces the second; one product cannot cover all four 1s.

An **implicant** covers only 1s and allowed Xs. A **prime implicant** cannot expand to a larger allowed group. It is **essential** if it uniquely covers a required 1. Choose essentials first, then cover any remaining 1s at the lowest allowed cost.

**Example: The same map gives POS**

Find the POS for $F=\sum m(1,2,3,5)$.

1. The required zero rows are 0,4,6,7.
2. Rows 0 and 4 keep B=C=0: the factor B+C is zero there.
3. Rows 6 and 7 keep A=B=1: use NOT A + NOT B.

   $$F=(B+C)(\overline A+\overline B)$$

**Answer:** $(B+C)(\overline A+\overline B)$. For a zero group, a constant 0 gives an uncomplemented literal; a constant 1 gives a complemented literal.

```digital
{"kind":"kmap","title":"Group zeros for POS","variables":["A","B","C"],"ones":[1,2,3,5],"target":0,"groups":[{"cells":[0,4],"label":"B=0, C=0 -> (B+C)"},{"cells":[6,7],"label":"A=1, B=1 -> (NOT A+NOT B)"}]}
```

*The POS factors identify where F must become zero.*

**Problem: Try it: four corners** (intermediate)

A four-variable map has 1s only at 0,2,8,10. Give one product term covering all four.

<details><summary>Solution</summary>

1. The corners are adjacent through both map boundaries.
2. A and C change; B and D stay at zero.

   $$F=\overline B\,\overline D$$

**Answer:** $\overline B\,\overline D$.

</details>

## Topic 2: Don’t-care conditions

A **don’t-care** X is an input combination for which the specification allows either output. Use it as 0 or 1 when that helps simplify the circuit; it does not have to be covered.

An X is permission from the specification, not a missing answer you may choose arbitrarily.

```digital
{"kind":"kmap","title":"Use X cells to enlarge groups","variables":["A","B","C","D"],"ones":[0,2,8,9,10,15],"dont_cares":[1,3,6,7],"groups":[{"cells":[0,1,8,9],"label":"NOT B NOT C"},{"cells":[0,2,8,10],"label":"NOT B NOT D (wraparound)"},{"cells":[7,15],"label":"BCD"}]}
```

*PS3 Q2: use X at 1 and 7; X at 3 and 6 need not be included.*

**Example: PS3 Q2: use Xs without changing required rows**

$F=\sum m(0,2,8,9,10,15)+D(1,3,6,7)$. Find a minimum SOP.

1. Group 0,1,8,9; B and C are zero.

   $$P_1=\overline B\overline C$$
2. Group 0,2,8,10 across the edge.

   $$P_2=\overline B\overline D$$
3. Pair required cell 15 with X cell 7.

   $$P_3=BCD$$

**Answer:** $F=\overline B\overline C+\overline B\overline D+BCD$. The chosen values on X rows are allowed to differ from another valid realization.

**Example: A different legal choice: minimum POS**

Find a POS for that same incompletely specified function.

1. Group zero cells 4,5,12,13.

   $$C+\overline B$$
2. Use X=6 with zero cells 4,12,14.

   $$D+\overline B$$
3. Use X=3 with zero cell 11.

   $$B+\overline C+\overline D$$

**Answer:** $F=(C+\overline B)(D+\overline B)(B+\overline C+\overline D)$. Check equality only on required rows.

For five variables, use two four-variable maps, one for each value of the fifth variable. Corresponding cells in the two maps are adjacent. A group repeated in both maps can eliminate the fifth variable.

**Problem: Try it: when an X assumption breaks** (intermediate)

A controller treats binary input 111 as unreachable and uses it as X. Later, 111 becomes a valid command whose output must be 0. Can the old simplified circuit be accepted unchanged?

<details><summary>Solution</summary>

1. The old circuit was not constrained at 111.
2. Evaluate that row under the new requirement and redesign if it produces 1.

**Answer:** Only if it already produces 0 at 111; the earlier proof did not establish that.

</details>

## Topic 3: Minimum expression versus circuit cost

The lecture’s cost convention is **number of gates + total gate inputs**. Count inverters unless complemented inputs are supplied. Check fan-in limits and shared terms before declaring a circuit cheapest.

**Example: Factoring changes cost**

Compare $F=AB+AC$ with $F=A(B+C)$ using two-input AND/OR gates. Inputs are uncomplemented.

1. Direct SOP: two ANDs and one OR.

   $$C_{\mathrm{SOP}}=3+(2+2+2)=9$$
2. Factored circuit: one OR and one AND.

   $$C_{\mathrm{factored}}=2+(2+2)=6$$

**Answer:** The factored implementation has cost 6 rather than 9. A minimum SOP is not automatically a minimum-cost multilevel circuit.

**Example: Share a product across outputs**

Compare separate and shared implementations of $F=AB+C$ and $G=AB+D$.

1. Separately, each output needs one AND and one OR: four gates, eight inputs.

   $$C_{\mathrm{separate}}=4+8=12$$
2. Share the AND AB, then keep the two output OR gates.

   $$C_{\mathrm{shared}}=3+6=9$$

**Answer:** Sharing saves one AND gate and its two inputs. PS3 Q5 asks for this type of joint optimization.

**Functional decomposition** expresses a function using smaller intermediate functions. Shannon decomposition on input A uses cofactors $F_0=F|_{A=0}$ and $F_1=F|_{A=1}$:

$$F=\overline A F_0+AF_1$$

A two-input gate limit can make a wide SOP expensive. For example, a 4-input AND needs three 2-input ANDs; a balanced tree has two levels rather than the three levels of a serial chain. The next note on building blocks uses Shannon decomposition to construct multiplexers.

**Example: Consensus and a static-1 hazard**

For $F=AB+\overline A C$, hold $B=C=1$ while A changes from 0 to 1. What should happen logically, and what could happen physically?

1. Before the change, NOT A C is 1; afterward, AB is 1. The ideal output remains 1.
2. Unequal path delays can briefly make both products zero.
3. Add the consensus product BC, which stays high throughout.

   $$F_{\mathrm{covered}}=AB+\overline A C+BC$$

**Answer:** BC preserves the truth table and covers the transition between the two terms. This addresses the single-input static-1 hazard, not every possible dynamic or multiple-input glitch.

**Problem: Try it: count with complemented inputs supplied** (intermediate)

Count the gates-plus-inputs cost of $F=\overline A B+C\overline D$ as a direct AND–OR network when both polarities of every input are supplied.

<details><summary>Solution</summary>

1. Use two two-input ANDs and one two-input OR; no input inverters are needed.

   $$C=3+6=9$$

**Answer:** Cost 9. If complements had to be generated, the two inverters would add 2 gates + 2 inputs, giving 13.

</details>
