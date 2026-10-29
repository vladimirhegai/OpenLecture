# Midterm Practice Problems

Exam-style practice for the **October 29 midterm** (40 minutes, Weeks 1–5). The wording copies the 2025 midterm, the problem sets and the tutorial, so nothing here should surprise you on the day.

*Sources: ELEC_271_Fall2025_Midterm.pdf, p. 1*

- **Marks are in [brackets].** The 2025 midterm was 15 marks in 40 minutes, so budget about 2½ minutes per mark.
- **Do each part on paper first**, then open its *Solution*. Every part has its own.
- **The exam's formula sheet** sits under each question that needs it (collapsed). Practise with it, not from memory.
- Each solution ends with the note section to review if you got it wrong.

| Exam topic (from the announcement) | Problems |
|---|---|
| Binary ↔ decimal ↔ hex, with fractions | 1 |
| Boolean algebra: proofs and simplifying | 2, 3 (also 4d, 5, 7b) |
| Truth table from a description | 4 |
| Canonical SOP / POS, $\sum m$ / $\prod M$ | 4, 5b, 8, 9a, 10a |
| Complementing a function | 5 |
| Venn diagrams | 6 |
| Gates → function (working backward) | 7, 9b |
| Timing diagrams, both directions | 7d, 8 |
| Drawing gate circuits | 4e, 9a, 10 |
| SOP → NAND–NAND, POS → NOR–NOR | 9, 10 |
| Transistor switches and NMOS gates | 11d |
| CMOS: draw one, read one | 11a–c |

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 1*

> **Timed run (15 marks, 40 minutes, like the real thing):** Problem 9(a) [6], 1(a) [2], 1(c) [2], 6(a) [2], 11(a) [3]. Set a timer, no peeking, then mark yourself with the solutions.

## Binary numbers

*Sources: Tutorial Week 2.pdf, p. 1*

### Problem 1 · Conversions [7 marks]

*Like past midterm Q2 and Tutorial Week 2 (1.1, 1.6, 1.8).*

**1.** (a) Convert decimal 25.6875 to binary. Then write the result in hexadecimal. **[2]**

(b) Convert $(\mathrm{A7.4})_{16}$ to binary, then to decimal. **[2]**

(c) Calculate the binary equivalent of 0.1 out to six places. Then convert from binary to decimal. How close is the result to 0.1? **[2]**

(d) What is the minimum number of bits needed to represent $(300)_{10}$ and $(512)_{10}$ in binary? **[1]**

*Sources: ELEC_271_Fall2025_Midterm.pdf, p. 3; Tutorial Week 2.pdf, p. 1*

<details><summary>Formula sheet: binary numbers (given in the exam)</summary>

Base $k$ to decimal, with digits $b_i$ ($n$ digits before the point, $m$ after):

$$
\text{Value}=\sum_{i=-m}^{n-1} b_i\,k^i
$$

| Hex | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Binary | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |

</details>

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 1*

<details><summary>Solution (a)</summary>

**Integer part, 25:** divide by 2 and keep the remainders. Read them **bottom → top**.

| Operation | Quotient | Remainder |
|---|---|---|
| 25 / 2 | 12 | 1 |
| 12 / 2 | 6 | 0 |
| 6 / 2 | 3 | 0 |
| 3 / 2 | 1 | 1 |
| 1 / 2 | 0 | 1 |

So $25 = 11001_2$.

**Fraction part, .6875:** multiply by 2 and keep the whole-number bit. Read them **top → bottom**. Stop when the fraction hits 0.

| Operation | Result | Bit |
|---|---|---|
| 0.6875 × 2 | 1.375 | 1 |
| 0.375 × 2 | 0.75 | 0 |
| 0.75 × 2 | 1.5 | 1 |
| 0.5 × 2 | 1.0 | 1 |

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

</details>

<details><summary>Solution (b)</summary>

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

</details>

<details><summary>Solution (c)</summary>

**Multiply by 2 six times** and keep the whole-number bits.

| Operation | Result | Bit |
|---|---|---|
| 0.1 × 2 | 0.2 | 0 |
| 0.2 × 2 | 0.4 | 0 |
| 0.4 × 2 | 0.8 | 0 |
| 0.8 × 2 | 1.6 | 1 |
| 0.6 × 2 | 1.2 | 1 |
| 0.2 × 2 | 0.4 | 0 |

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

</details>

<details><summary>Solution (d)</summary>

**Rule:** $n$ bits can count from 0 up to $2^n-1$. Find the smallest $n$ that reaches your number.

- **300:** $2^8=256$ is too small, $2^9=512$ is enough ($0$ to $511$). **9 bits.**
- **512:** 9 bits only reach 511. $512 = 1\underbrace{000000000}_{9\text{ zeros}}$ needs **10 bits**.

**Trap:** an exact power of two, $2^n$, always needs $n+1$ bits.

*Review: Note 01, Extras (bits needed).*

</details>

## Boolean algebra

*Sources: Practice questions chapter 2.pdf, p. 1*

This is where most marks get lost, so here are the moves that keep showing up. Every one is on the formula sheet.

- **Copy a term (7b), $x+x=x$.** A minterm can pair with two different neighbours if you write it twice.
- **Consensus (17a).** Two terms with $x$ and $\bar x$, like $x_1x_3$ and $\bar x_1x_2$: multiply the leftovers ($x_3x_2$). If that term is also there, delete it.
- **16a, $x+\bar xy=x+y$.** A barred copy of something you already have just disappears: $x_1+\bar x_1x_2=x_1+x_2$.
- **Treat a bracket as one letter.** Rules work on whole groups: $(x_1+x_2)+\overline{(x_1+x_2)}\,x_3=x_1+x_2+x_3$.
- **12b backwards.** $(x+y)(x+z)=x+yz$ turns a POS into an SOP in one line.
- **Stuck? Expand to minterms** and pair rows that differ in one bit (past midterm Q1 style). It always works.
- **Check by plugging in a couple of rows.** If both sides disagree anywhere, there's a mistake.

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 2*

### Problem 2 · Prove it with algebra [8 marks]

*Like PS1 Q1 and textbook 2.1–2.3. Name the formula-sheet rule for every step.*

**2.** Use algebraic manipulation to prove each identity. Name the rule you use at each step.

(a) $\bar x_1\bar x_2+\bar x_1x_2+x_1x_2=\bar x_1+x_2$ **[2]**

(b) $(x_1+x_2)(\bar x_1+x_3)=x_1x_3+\bar x_1x_2$ **[2]**

(c) $x_1+\bar x_1x_2+\bar x_1\bar x_2x_3=x_1+x_2+x_3$ **[2]**

(d) $\overline{\overline{x_1+x_2}+\overline{x_1+\bar x_2}}=x_1$ **[2]**

*Sources: Practice questions chapter 2.pdf, p. 1; Practice questions chapter 2.pdf, p. 2; Problem_set_1_solutions2.pdf, p. 1*

<details><summary>Formula sheet: Boolean algebra (given in the exam)</summary>

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

</details>

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 2*

<details><summary>Solution (a)</summary>

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

</details>

<details><summary>Solution (b)</summary>

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

</details>

<details><summary>Solution (c)</summary>

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

</details>

<details><summary>Solution (d)</summary>

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

</details>

### Problem 3 · Simplify with algebra [8 marks]

*Like PS1 Q5 and Q8. No K-map: show the Boolean algebra.*

**3.** Use Boolean algebra to find the minimum sum-of-products expression for each function. Name the rule you use at each step. **[2]** each

(a) $f=x_1x_2+x_1\bar x_2x_3+\bar x_1x_3$

(b) $f=x_1\bar x_2+\bar x_1x_3+\bar x_2x_3$

(c) $f=(x_1+x_2)(x_1+\bar x_2+x_3)$

(d) $f=\overline{(x_1+\bar x_2)(\bar x_1+x_3)}+x_2\bar x_3$

*Sources: Problem_set_1_solutions2.pdf, p. 3; Problem_set_1_solutions2.pdf, p. 4*

<details><summary>Formula sheet: Boolean algebra (given in the exam)</summary>

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

</details>

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 2*

<details><summary>Solution (a)</summary>

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

</details>

<details><summary>Solution (b)</summary>

1. **Look for consensus.** $x_1\bar x_2$ and $\bar x_1x_3$ contain $x_1$ and $\bar x_1$. Multiply the leftovers: $\bar x_2\cdot x_3$.

2. **That's the third term, so delete it (17a)**, with $x=x_1$, $y=\bar x_2$, $z=x_3$.

   $$
   f=x_1\bar x_2+\bar x_1x_3
   $$

**Check:** $\bar x_2x_3$ is rows 1 (001) and 5 (101). Row 1 is already covered by $\bar x_1x_3$, and row 5 by $x_1\bar x_2$. Both versions are $\sum m(1,3,4,5)$ ✓

**Trap:** no two terms combine with 14a, so it *looks* finished. Always check for a consensus term before you stop.

*Review: Note 02 §4.*

</details>

<details><summary>Solution (c)</summary>

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

</details>

<details><summary>Solution (d)</summary>

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

</details>

## Truth tables, canonical forms and complements

*Sources: Section2_Logic_Circuits.pdf, p. 38; Section2_Logic_Circuits.pdf, p. 43*

### Problem 4 · Description → truth table → circuit [7 marks]

*Like PS1 Q9 and textbook 2.20 (design the simplest circuit).*

**4.** A circuit has three inputs $x_1, x_2, x_3$. Together they form the 3-bit number $N=x_1x_2x_3$ ($x_1$ is the most significant bit). The output $f$ is 1 when $N$ is a prime number. Otherwise $f$ is 0.

(a) Show the truth table for $f$. **[1]**

(b) Write the canonical SOP expression for $f$. **[1]**

(c) Write the canonical POS expression for $f$. **[1]**

(d) Use Boolean algebra to find the minimum SOP and the minimum POS expressions. **[3]**

(e) Draw the minimum SOP circuit using AND, OR and NOT gates. **[1]**

*Sources: Problem_set_1_solutions2.pdf, p. 4; Practice questions chapter 2.pdf, p. 3*

<details><summary>Formula sheet: minterms and maxterms (given in the exam)</summary>

| Row | $x_1x_2x_3$ | Minterm $m_i$ | Maxterm $M_i$ |
|---|---|---|---|
| 0 | 000 | $m_0=\bar x_1\bar x_2\bar x_3$ | $M_0=x_1+x_2+x_3$ |
| 1 | 001 | $m_1=\bar x_1\bar x_2x_3$ | $M_1=x_1+x_2+\bar x_3$ |
| 2 | 010 | $m_2=\bar x_1x_2\bar x_3$ | $M_2=x_1+\bar x_2+x_3$ |
| 3 | 011 | $m_3=\bar x_1x_2x_3$ | $M_3=x_1+\bar x_2+\bar x_3$ |
| 4 | 100 | $m_4=x_1\bar x_2\bar x_3$ | $M_4=\bar x_1+x_2+x_3$ |
| 5 | 101 | $m_5=x_1\bar x_2x_3$ | $M_5=\bar x_1+x_2+\bar x_3$ |
| 6 | 110 | $m_6=x_1x_2\bar x_3$ | $M_6=\bar x_1+\bar x_2+x_3$ |
| 7 | 111 | $m_7=x_1x_2x_3$ | $M_7=\bar x_1+\bar x_2+\bar x_3$ |

Also on the sheet: $\overline{m_i}=M_i$.

</details>

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 2*

<details><summary>Solution (a)</summary>

The primes up to 7 are 2, 3, 5, 7. **0 and 1 are not prime** (that's the trap).

| Row | $x_1$ | $x_2$ | $x_3$ | $N$ | Prime? | $f$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | no | 0 |
| 1 | 0 | 0 | 1 | 1 | no | 0 |
| 2 | 0 | 1 | 0 | 2 | yes | 1 |
| 3 | 0 | 1 | 1 | 3 | yes | 1 |
| 4 | 1 | 0 | 0 | 4 | no | 0 |
| 5 | 1 | 0 | 1 | 5 | yes | 1 |
| 6 | 1 | 1 | 0 | 6 | no | 0 |
| 7 | 1 | 1 | 1 | 7 | yes | 1 |

*Review: Note 02 §2, Truth table from a description.*

</details>

<details><summary>Solution (b)</summary>

One minterm per 1 row. A 1 bit is written plain, a 0 bit with a bar.

$$
f=\sum m(2,3,5,7)=\bar x_1x_2\bar x_3+\bar x_1x_2x_3+x_1\bar x_2x_3+x_1x_2x_3
$$

*Review: Note 02 §3.*

</details>

<details><summary>Solution (c)</summary>

One maxterm per **0** row: rows 0, 1, 4, 6. Now it's the opposite: a 0 bit is plain, a 1 bit gets a bar.

$$
f=\prod M(0,1,4,6)=(x_1+x_2+x_3)(x_1+x_2+\bar x_3)(\bar x_1+x_2+x_3)(\bar x_1+\bar x_2+x_3)
$$

*Review: Note 02 §3.*

</details>

<details><summary>Solution (d)</summary>

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

</details>

<details><summary>Solution (e)</summary>

```digital
{"kind":"circuit","title":"f = NOT x1 x2 + x1 x3","nodes":[{"id":"x2","gate":"INPUT","x":70,"y":90,"label":"x₂"},{"id":"x1","gate":"INPUT","x":70,"y":200,"label":"x₁"},{"id":"x3","gate":"INPUT","x":70,"y":320,"label":"x₃"},{"id":"N1","gate":"NOT","x":260,"y":200,"label":"x̄₁"},{"id":"A1","gate":"AND","x":450,"y":120,"label":"x̄₁x₂"},{"id":"A2","gate":"AND","x":450,"y":290,"label":"x₁x₃"},{"id":"G","gate":"OR","x":640,"y":200,"label":"x̄₁x₂ + x₁x₃"},{"id":"f","gate":"OUTPUT","x":820,"y":200,"label":"f"}],"wires":[{"start":"x1.out","end":"N1.0"},{"start":"x2.out","end":"A1.0"},{"start":"N1.out","end":"A1.1"},{"start":"x1.out","end":"A2.0","via":[[160,200],[160,280]]},{"start":"x3.out","end":"A2.1"},{"start":"A1.out","end":"G.0"},{"start":"A2.out","end":"G.1"},{"start":"G.out","end":"f.0"}]}
```

*One NOT makes x̄₁, one AND per product term, and an OR collects them.*

*Review: Note 02 §5, Expression → gates.*

</details>

### Problem 5 · Complements [5 marks]

*Like the lecture's De Morgan examples and PS1 Q4.*

**5.** (a) Find the complement of $f=x_1\bar x_2+\bar x_1x_3$. Give $\bar f$ first as a POS, then as a minimum SOP. **[2]**

(b) $f(x_1,x_2,x_3)=\sum m(0,2,3,6)$. Write $\bar f$ in both $\sum m$ and $\prod M$ form, and write $f$ in $\prod M$ form. **[1]**

(c) Find the complement of $f=x_1+\bar x_2(x_3+\bar x_1)$ and simplify it. **[2]**

*Sources: Section2_Logic_Circuits.pdf, p. 24; Section2_Logic_Circuits.pdf, p. 25*

<details><summary>Formula sheet: Boolean algebra (given in the exam)</summary>

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

</details>

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 2*

<details><summary>Solution (a)</summary>

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

</details>

<details><summary>Solution (b)</summary>

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

</details>

<details><summary>Solution (c)</summary>

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

</details>

## Venn diagrams

*Sources: ELEC_271_Fall2025_Midterm.pdf, p. 4*

### Problem 6 · Venn diagrams [5 marks]

*Past midterm Q3 proved 15a. Textbook 2.5 asks for 15b, and PS1 Q6 places minterms in a 3-circle diagram.*

**6.** (a) Use the Venn diagram to prove DeMorgan's theorem, identity 15b: $\overline{x+y}=\bar x\cdot\bar y$. **[2]**

(b) Use a three-variable Venn diagram to prove the distributive rule, identity 12b: $x+yz=(x+y)(x+z)$. **[2]**

(c) Which function is shaded in the diagram below? Give it as a minimum SOP. **[1]**

```digital
{"kind":"venn","title":"Problem 6(c)","variables":["x1","x2","x3"],"shaded":[3,5,6,7]}
```

*Problem 6(c): the shaded function.*

*Sources: ELEC_271_Fall2025_Midterm.pdf, p. 4; Practice questions chapter 2.pdf, p. 1; Practice questions chapter 2.pdf, p. 3*

<details><summary>Solution (a)</summary>

**Left side.** First shade $x+y$: everything inside **either** circle.

```digital
{"kind":"venn","title":"x + y","variables":["x","y"],"shaded":[1,2,3]}
```

*x + y: both circles.*

The bar flips it: $\overline{x+y}$ is everything **outside both** circles.

```digital
{"kind":"venn","title":"NOT (x + y)","variables":["x","y"],"shaded":[0]}
```

*The complement: only the outside is left.*

**Right side.** $\bar x$ is everything outside circle $x$. $\bar y$ is everything outside circle $y$. AND keeps only what is shaded in **both**, which is the area outside both circles.

```digital
{"kind":"venn","title":"NOT x · NOT y","variables":["x","y"],"shaded":[0]}
```

*x̄ · ȳ: outside x and outside y at the same time.*

The two pictures match, so $\overline{x+y}=\bar x\cdot\bar y$ ✓

**Marking (2025):** 1 mark for each side, so always draw both.

*Review: Note 02 §8.*

</details>

<details><summary>Solution (b)</summary>

**Left side, $x+yz$.** $x$ is the whole $x$ circle. $yz$ is where the $y$ and $z$ circles overlap. OR shades both.

```digital
{"kind":"venn","title":"x + yz","variables":["x","y","z"],"shaded":[3,4,5,6,7]}
```

*x + yz: circle x plus the y–z overlap.*

**Right side.** Shade each bracket, then AND keeps the area shaded in **both**.

```digital
{"kind":"venn","title":"x + y","variables":["x","y","z"],"shaded":[2,3,4,5,6,7]}
```

*x + y: circles x and y.*

```digital
{"kind":"venn","title":"x + z","variables":["x","y","z"],"shaded":[1,3,4,5,6,7]}
```

*x + z: circles x and z.*

```digital
{"kind":"venn","title":"(x + y)(x + z)","variables":["x","y","z"],"shaded":[3,4,5,6,7]}
```

*Shaded in both pictures above.*

The left and right pictures match, so $x+yz=(x+y)(x+z)$ ✓

*Review: Note 02 §8.*

</details>

<details><summary>Solution (c)</summary>

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

</details>

## Circuits and timing diagrams

*Sources: Problem_set_1_solutions2.pdf, p. 2*

### Problem 7 · Read a circuit, then draw its timing diagram [6 marks]

*Like PS1 Q3 and textbook 2.8.*

**7.** Consider the circuit shown below.

```digital
{"kind":"circuit","title":"Problem 7","nodes":[{"id":"x1","gate":"INPUT","x":70,"y":90,"label":"x₁"},{"id":"x2","gate":"INPUT","x":70,"y":200,"label":"x₂"},{"id":"x3","gate":"INPUT","x":70,"y":320,"label":"x₃"},{"id":"G1","gate":"NAND","x":330,"y":100,"label":"g₁"},{"id":"G2","gate":"OR","x":330,"y":300,"label":"g₂"},{"id":"F","gate":"AND","x":560,"y":200,"label":" "},{"id":"f","gate":"OUTPUT","x":740,"y":200,"label":"f"}],"wires":[{"start":"x1.out","end":"G1.0"},{"start":"x2.out","end":"G1.1","via":[[180,200],[180,110]]},{"start":"x2.out","end":"G2.0","via":[[180,200],[180,290]]},{"start":"x3.out","end":"G2.1"},{"start":"G1.out","end":"F.0"},{"start":"G2.out","end":"F.1"},{"start":"F.out","end":"f.0"}]}
```

*Problem 7: inputs x₁, x₂, x₃; gate outputs g₁, g₂ and f.*

(a) Find the expression for $f$ by working through the circuit. **[1]**

(b) Use Boolean algebra to reduce $f$ to a minimum SOP. **[2]**

(c) Show the truth table for $f$ as $\sum m(\ldots)$. **[1]**

(d) Draw a timing diagram for the circuit, with the inputs counting 000, 001, …, 111. Show the waveforms on all wires. **[2]**

*Sources: Problem_set_1_solutions2.pdf, p. 2*

<details><summary>Formula sheet: Boolean algebra (given in the exam)</summary>

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

</details>

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 2*

<details><summary>Solution (a)</summary>

```logicsteps
title "Problem 7: read it left to right"
== Start at the inputs
{"kind":"circuit","title":"Problem 7","nodes":[{"id":"x1","gate":"INPUT","x":70,"y":90,"label":"x₁"},{"id":"x2","gate":"INPUT","x":70,"y":200,"label":"x₂"},{"id":"x3","gate":"INPUT","x":70,"y":320,"label":"x₃"},{"id":"G1","gate":"NAND","x":330,"y":100,"label":"g₁ = ?"},{"id":"G2","gate":"OR","x":330,"y":300,"label":"g₂ = ?"},{"id":"F","gate":"AND","x":560,"y":200,"label":" "},{"id":"f","gate":"OUTPUT","x":740,"y":200,"label":"f"}],"wires":[{"start":"x1.out","end":"G1.0"},{"start":"x2.out","end":"G1.1","via":[[180,200],[180,110]]},{"start":"x2.out","end":"G2.0","via":[[180,200],[180,290]]},{"start":"x3.out","end":"G2.1"},{"start":"G1.out","end":"F.0"},{"start":"G2.out","end":"F.1"},{"start":"F.out","end":"f.0"}]}
--
A gate can only be named once both wires going into it are named. $x_2$ splits and feeds **both** first gates.
== The first two gates
{"kind":"circuit","title":"Problem 7","nodes":[{"id":"x1","gate":"INPUT","x":70,"y":90,"label":"x₁"},{"id":"x2","gate":"INPUT","x":70,"y":200,"label":"x₂"},{"id":"x3","gate":"INPUT","x":70,"y":320,"label":"x₃"},{"id":"G1","gate":"NAND","x":330,"y":100,"label":"g₁ = NOT(x₁x₂)"},{"id":"G2","gate":"OR","x":330,"y":300,"label":"g₂ = x₂ + x₃"},{"id":"F","gate":"AND","x":560,"y":200,"label":" "},{"id":"f","gate":"OUTPUT","x":740,"y":200,"label":"f"}],"wires":[{"start":"x1.out","end":"G1.0"},{"start":"x2.out","end":"G1.1","via":[[180,200],[180,110]]},{"start":"x2.out","end":"G2.0","via":[[180,200],[180,290]]},{"start":"x3.out","end":"G2.1"},{"start":"G1.out","end":"F.0"},{"start":"G2.out","end":"F.1"},{"start":"F.out","end":"f.0"}]}
#+ $g_1=\overline{x_1x_2}$
#+ $g_2=x_2+x_3$
--
The top gate is a **NAND** (bubble on the output) of $x_1$ and $x_2$. The bottom gate is an OR of $x_2$ and $x_3$.
== The AND gives f
{"kind":"circuit","title":"Problem 7","nodes":[{"id":"x1","gate":"INPUT","x":70,"y":90,"label":"x₁"},{"id":"x2","gate":"INPUT","x":70,"y":200,"label":"x₂"},{"id":"x3","gate":"INPUT","x":70,"y":320,"label":"x₃"},{"id":"G1","gate":"NAND","x":330,"y":100,"label":"g₁ = NOT(x₁x₂)"},{"id":"G2","gate":"OR","x":330,"y":300,"label":"g₂ = x₂ + x₃"},{"id":"F","gate":"AND","x":560,"y":200,"label":"f = g₁g₂"},{"id":"f","gate":"OUTPUT","x":740,"y":200,"label":"f"}],"wires":[{"start":"x1.out","end":"G1.0"},{"start":"x2.out","end":"G1.1","via":[[180,200],[180,110]]},{"start":"x2.out","end":"G2.0","via":[[180,200],[180,290]]},{"start":"x3.out","end":"G2.1"},{"start":"G1.out","end":"F.0"},{"start":"G2.out","end":"F.1"},{"start":"F.out","end":"f.0"}]}
#+ $f=\overline{x_1x_2}\,(x_2+x_3)$
--
The AND multiplies the two:

$$
f=\overline{x_1x_2}\,(x_2+x_3)
$$

Turn on **Try inputs** and test row 5 (101): $g_1=1$, $g_2=1$, so $f=1$.
```

*Review: Note 02 §5, Gates → expression.*

</details>

<details><summary>Solution (b)</summary>

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

</details>

<details><summary>Solution (c)</summary>

$\bar x_1x_2$ is 1 on rows 2, 3 (pattern 01-). $\bar x_2x_3$ is 1 on rows 1, 5 (pattern -01).

$$
f=\sum m(1,2,3,5)
$$

**Check from the circuit:** $g_1$ is 0 only when $x_1=x_2=1$ (rows 6, 7). $g_2$ is 0 only when $x_2=x_3=0$ (rows 0, 4). The AND is 1 on every other row: 1, 2, 3, 5 ✓

*Review: Note 02 §5.*

</details>

<details><summary>Solution (d)</summary>

Feed the inputs in counting order, then fill in each wire one time slot at a time, exactly like a truth table.

```digital
{"kind":"timing","title":"Problem 7: every wire","unit":"one slot = one input row (000 to 111); ideal gates, no delay","signals":[{"name":"x1","wave":"00001111"},{"name":"x2","wave":"00110011"},{"name":"x3","wave":"01010101"},{"name":"g1 = NAND(x1, x2)","wave":"11111100"},{"name":"g2 = x2 + x3","wave":"01110111"},{"name":"f = g1 · g2","wave":"01110100"}]}
```

*g₁ drops only in the last two slots (x₁ = x₂ = 1). g₂ drops only when x₂ and x₃ are both low. f is high when both are high.*

$f$ is high in slots 1, 2, 3, 5, which matches part (c) ✓

*Review: Note 02 §6, Circuit → waveforms.*

</details>

### Problem 8 · Timing diagram → function [6 marks]

*Like textbook 2.31 and 2.32 (PS1 Q10), but the inputs are not in counting order.*

**8.** For the timing diagram below:

```digital
{"kind":"timing","title":"Problem 8","unit":"equal time slots","signals":[{"name":"x1","wave":"01100110"},{"name":"x2","wave":"00111100"},{"name":"x3","wave":"00001111"},{"name":"f","wave":"11100101"}]}
```

*Problem 8: read each slot straight down.*

(a) Find $f$ as $\sum m(\ldots)$. **[2]**

(b) Synthesize $f$ in the simplest sum-of-products form. **[2]**

(c) Synthesize $f$ in the simplest product-of-sums form. Which form needs fewer gates? **[2]**

*Sources: Problem_set_1_solutions2.pdf, p. 5*

<details><summary>Formula sheet: minterms and maxterms (given in the exam)</summary>

| Row | $x_1x_2x_3$ | Minterm $m_i$ | Maxterm $M_i$ |
|---|---|---|---|
| 0 | 000 | $m_0=\bar x_1\bar x_2\bar x_3$ | $M_0=x_1+x_2+x_3$ |
| 1 | 001 | $m_1=\bar x_1\bar x_2x_3$ | $M_1=x_1+x_2+\bar x_3$ |
| 2 | 010 | $m_2=\bar x_1x_2\bar x_3$ | $M_2=x_1+\bar x_2+x_3$ |
| 3 | 011 | $m_3=\bar x_1x_2x_3$ | $M_3=x_1+\bar x_2+\bar x_3$ |
| 4 | 100 | $m_4=x_1\bar x_2\bar x_3$ | $M_4=\bar x_1+x_2+x_3$ |
| 5 | 101 | $m_5=x_1\bar x_2x_3$ | $M_5=\bar x_1+x_2+\bar x_3$ |
| 6 | 110 | $m_6=x_1x_2\bar x_3$ | $M_6=\bar x_1+\bar x_2+x_3$ |
| 7 | 111 | $m_7=x_1x_2x_3$ | $M_7=\bar x_1+\bar x_2+\bar x_3$ |

Also on the sheet: $\overline{m_i}=M_i$.

</details>

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 2*

<details><summary>Solution (a)</summary>

The inputs jump around, so **read each slot straight down**, turn $x_1x_2x_3$ into a row number, and note $f$.

| Slot | $x_1x_2x_3$ | Row | $f$ |
|---|---|---|---|
| 0 | 000 | 0 | 1 |
| 1 | 100 | 4 | 1 |
| 2 | 110 | 6 | 1 |
| 3 | 010 | 2 | 0 |
| 4 | 011 | 3 | 0 |
| 5 | 111 | 7 | 1 |
| 6 | 101 | 5 | 0 |
| 7 | 001 | 1 | 1 |

Every row 0–7 shows up exactly once, so the table is complete.

$$
f=\sum m(0,1,4,6,7)
$$

*Review: Note 02 §6, Waveforms → function.*

</details>

<details><summary>Solution (b)</summary>

1. $m_0+m_1$: 000 and 001 differ only in $x_3$ (14a) → $\bar x_1\bar x_2$.
2. $m_6+m_7$: 110 and 111 differ only in $x_3$ → $x_1x_2$.
3. $m_4$ (100) is left. Copy $m_6$ (7b) and pair $m_4+m_6$: they differ only in $x_2$ → $x_1\bar x_3$.

$$
f=\bar x_1\bar x_2+x_1x_2+x_1\bar x_3
$$

Pairing $m_4$ with $m_0$ instead gives $\bar x_2\bar x_3$ in place of $x_1\bar x_3$. Both are correct and equally small.

*Review: Note 02 §4.*

</details>

<details><summary>Solution (c)</summary>

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

</details>

## NAND–NAND and NOR–NOR

*Sources: Section2_Logic_Circuits.pdf, p. 47; Section2_Logic_Circuits.pdf, p. 48; Section2_Logic_Circuits.pdf, p. 49; Section2_Logic_Circuits.pdf, p. 50; Section2_Logic_Circuits.pdf, p. 51*

> **Reminder card: NAND–NAND / NOR–NOR in 4 steps**
> 
> 1. **Simplify first.** NAND–NAND needs a minimum **SOP**. NOR–NOR needs a minimum **POS**.
> 2. **Draw the 2-level circuit:** AND → OR for an SOP, OR → AND for a POS.
> 3. **Swap every gate** for a NAND (SOP) or a NOR (POS). The two layers of bubbles cancel each other.
> 4. **Fix the leftovers:** a one-letter term goes into the last gate **flipped**, and every NOT becomes a gate with its inputs tied together.
> 
> **Gate count** = NOTs + one gate per multi-letter term + 1 output gate.
> 
> **Reading one back:** a two-level NAND–NAND is an SOP (each first-level NAND is one product). A NOR–NOR is a POS.
> 
> **Got an SOP but asked for NOR only?** Turn it into a POS first (12b, or complement twice).

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 2; ELEC 271 Midterm Formula Sheet.pdf, p. 3*

### Problem 9 · SOP → NAND only [8 marks]

*Part (a) is past midterm Q1 with a new function. Marking scheme then: 3 for the minimum, 1.5 for the SOP, 1.5 for the NAND drawing.*

**9.** (a) Consider the function $f(x_1,x_2,x_3)=\sum m(0,2,3,6,7)$. First, find the canonical SOP expression. Then, find the minimum SOP expression and implement it using only NAND gates. **[6]**

(b) What function does the NAND-only circuit below implement? Give it as a minimum SOP. **[2]**

```digital
{"kind":"circuit","title":"Problem 9(b)","nodes":[{"id":"x2","gate":"INPUT","x":70,"y":90,"label":"x₂"},{"id":"x1","gate":"INPUT","x":70,"y":230,"label":"x₁"},{"id":"x3","gate":"INPUT","x":70,"y":380,"label":"x₃"},{"id":"N1","gate":"NAND","x":260,"y":230},{"id":"N2","gate":"NAND","x":450,"y":120},{"id":"N3","gate":"NAND","x":450,"y":330},{"id":"F","gate":"NAND","x":640,"y":225,"label":" "},{"id":"f","gate":"OUTPUT","x":820,"y":225,"label":"f"}],"wires":[{"start":"x1.out","end":"N1.0"},{"start":"x1.out","end":"N1.1"},{"start":"x2.out","end":"N2.0"},{"start":"N1.out","end":"N2.1"},{"start":"x1.out","end":"N3.0","via":[[160,230],[160,320]]},{"start":"x3.out","end":"N3.1"},{"start":"N2.out","end":"F.0"},{"start":"N3.out","end":"F.1"},{"start":"F.out","end":"f.0"}]}
```

*Problem 9(b): every gate is a NAND.*

*Sources: ELEC_271_Fall2025_Midterm.pdf, p. 2*

<details><summary>Formula sheet: NAND and NOR (given in the exam)</summary>

- **NAND gate:** $\overline{x_1x_2}=\bar x_1+\bar x_2$. A NAND is an OR with bubbles on its inputs.
- **NOR gate:** $\overline{x_1+x_2}=\bar x_1\,\bar x_2$. A NOR is an AND with bubbles on its inputs.
- **NOT:** a NAND or a NOR with both inputs tied together.
- The sheet also draws **SOP → NAND–NAND** and **POS → NOR–NOR** networks.

</details>

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 2*

<details><summary>Solution (a)</summary>

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

```logicsteps
title "Problem 9(a): AND–OR into NAND–NAND"
== Draw the normal AND–OR circuit
{"kind":"circuit","title":"f = x2 + NOT x1 NOT x3","nodes":[{"id":"x2","gate":"INPUT","x":70,"y":90,"label":"x₂"},{"id":"x1","gate":"INPUT","x":70,"y":200,"label":"x₁"},{"id":"x3","gate":"INPUT","x":70,"y":320,"label":"x₃"},{"id":"N1","gate":"NOT","x":260,"y":200,"label":"x̄₁"},{"id":"N3","gate":"NOT","x":260,"y":320,"label":"x̄₃"},{"id":"P","gate":"AND","x":450,"y":260,"label":"x̄₁x̄₃"},{"id":"G","gate":"OR","x":640,"y":150,"label":"x₂ + x̄₁x̄₃"},{"id":"f","gate":"OUTPUT","x":820,"y":150,"label":"f"}],"wires":[{"start":"x1.out","end":"N1.0"},{"start":"x3.out","end":"N3.0"},{"start":"N1.out","end":"P.0"},{"start":"N3.out","end":"P.1","via":[[380,320],[380,270]]},{"start":"x2.out","end":"G.0","via":[[520,90],[520,140]]},{"start":"P.out","end":"G.1"},{"start":"G.out","end":"f.0"}]}
--
From $f=x_2+\bar x_1\bar x_3$: two NOTs, one AND for $\bar x_1\bar x_3$, and an OR at the end. $x_2$ is a one-letter term, so it goes straight into the OR.
== Swap the AND and the OR for NANDs
{"kind":"circuit","title":"f = x2 + NOT x1 NOT x3","nodes":[{"id":"x2","gate":"INPUT","x":70,"y":90,"label":"x₂"},{"id":"x1","gate":"INPUT","x":70,"y":200,"label":"x₁"},{"id":"x3","gate":"INPUT","x":70,"y":320,"label":"x₃"},{"id":"N1","gate":"NOT","x":260,"y":200,"label":"x̄₁"},{"id":"N3","gate":"NOT","x":260,"y":320,"label":"x̄₃"},{"id":"P","gate":"NAND","x":450,"y":260,"label":"NOT(x̄₁x̄₃)"},{"id":"G","gate":"NAND","x":640,"y":150,"label":"x̄₂ + x̄₁x̄₃  ✗"},{"id":"f","gate":"OUTPUT","x":820,"y":150,"label":"f"}],"wires":[{"start":"x1.out","end":"N1.0"},{"start":"x3.out","end":"N3.0"},{"start":"N1.out","end":"P.0"},{"start":"N3.out","end":"P.1","via":[[380,320],[380,270]]},{"start":"x2.out","end":"G.0","via":[[520,90],[520,140]]},{"start":"P.out","end":"G.1"},{"start":"G.out","end":"f.0"}]}
--
The last NAND flips **both** of its inputs (De Morgan). That undoes the bubble on the product, but it also flips $x_2$: right now $f=\bar x_2+\bar x_1\bar x_3$. **Wrong.** Try inputs 010: it should give 1 but gives 0.
== Flip the one-letter term
{"kind":"circuit","title":"f = x2 + NOT x1 NOT x3","nodes":[{"id":"x2","gate":"INPUT","x":70,"y":90,"label":"x₂"},{"id":"x1","gate":"INPUT","x":70,"y":200,"label":"x₁"},{"id":"x3","gate":"INPUT","x":70,"y":320,"label":"x₃"},{"id":"N1","gate":"NOT","x":260,"y":200,"label":"x̄₁"},{"id":"N3","gate":"NOT","x":260,"y":320,"label":"x̄₃"},{"id":"P","gate":"NAND","x":450,"y":260,"label":"NOT(x̄₁x̄₃)"},{"id":"G","gate":"NAND","x":640,"y":150,"label":"x₂ + x̄₁x̄₃  ✓"},{"id":"f","gate":"OUTPUT","x":820,"y":150,"label":"f"},{"id":"N2","gate":"NOT","x":260,"y":90,"label":"x̄₂"}],"wires":[{"start":"x1.out","end":"N1.0"},{"start":"x3.out","end":"N3.0"},{"start":"N1.out","end":"P.0"},{"start":"N3.out","end":"P.1","via":[[380,320],[380,270]]},{"start":"P.out","end":"G.1"},{"start":"G.out","end":"f.0"},{"start":"x2.out","end":"N2.0"},{"start":"N2.out","end":"G.0","via":[[520,90],[520,140]]}]}
--
Feed $x_2$ in already flipped. The last NAND flips it back:

$$
f=\overline{\bar x_2\cdot\overline{\bar x_1\bar x_3}}=x_2+\bar x_1\bar x_3
$$
== Make the NOTs out of NANDs
{"kind":"circuit","title":"f = x2 + NOT x1 NOT x3","nodes":[{"id":"x2","gate":"INPUT","x":70,"y":90,"label":"x₂"},{"id":"x1","gate":"INPUT","x":70,"y":200,"label":"x₁"},{"id":"x3","gate":"INPUT","x":70,"y":320,"label":"x₃"},{"id":"N1","gate":"NAND","x":260,"y":200,"label":"x̄₁ (tied NAND)"},{"id":"N3","gate":"NAND","x":260,"y":320,"label":"x̄₃ (tied NAND)"},{"id":"P","gate":"NAND","x":450,"y":260,"label":"NOT(x̄₁x̄₃)"},{"id":"G","gate":"NAND","x":640,"y":150,"label":"x₂ + x̄₁x̄₃  ✓"},{"id":"f","gate":"OUTPUT","x":820,"y":150,"label":"f"},{"id":"N2","gate":"NAND","x":260,"y":90,"label":"x̄₂ (tied NAND)"}],"wires":[{"start":"x1.out","end":"N1.0"},{"start":"x3.out","end":"N3.0"},{"start":"N1.out","end":"P.0"},{"start":"N3.out","end":"P.1","via":[[380,320],[380,270]]},{"start":"P.out","end":"G.1"},{"start":"G.out","end":"f.0"},{"start":"x2.out","end":"N2.0"},{"start":"N2.out","end":"G.0","via":[[520,90],[520,140]]},{"start":"x1.out","end":"N1.1"},{"start":"x2.out","end":"N2.1"},{"start":"x3.out","end":"N3.1"}]}
--
Tie both inputs of a NAND together to get a NOT. Every gate is now a NAND. Try any inputs: it matches the AND–OR circuit on all 8 rows.
```

**Answer:** $f=x_2+\bar x_1\bar x_3$ with **5 NAND gates**: 3 tied NANDs for $\bar x_1, \bar x_2, \bar x_3$, one for the product, one at the output.

*Review: Note 02 §9, SOP → NAND–NAND.*

</details>

<details><summary>Solution (b)</summary>

```logicsteps
title "Problem 9(b): read the NAND circuit"
== Start at the inputs
{"kind":"circuit","title":"Problem 9(b)","nodes":[{"id":"x2","gate":"INPUT","x":70,"y":90,"label":"x₂"},{"id":"x1","gate":"INPUT","x":70,"y":230,"label":"x₁"},{"id":"x3","gate":"INPUT","x":70,"y":380,"label":"x₃"},{"id":"N1","gate":"NAND","x":260,"y":230},{"id":"N2","gate":"NAND","x":450,"y":120},{"id":"N3","gate":"NAND","x":450,"y":330},{"id":"F","gate":"NAND","x":640,"y":225,"label":" "},{"id":"f","gate":"OUTPUT","x":820,"y":225,"label":"f"}],"wires":[{"start":"x1.out","end":"N1.0"},{"start":"x1.out","end":"N1.1"},{"start":"x2.out","end":"N2.0"},{"start":"N1.out","end":"N2.1"},{"start":"x1.out","end":"N3.0","via":[[160,230],[160,320]]},{"start":"x3.out","end":"N3.1"},{"start":"N2.out","end":"F.0"},{"start":"N3.out","end":"F.1"},{"start":"F.out","end":"f.0"}]}
--
Spot the NAND whose two inputs are **both** $x_1$. That's a tied NAND, so it's a NOT.
== The tied NAND
{"kind":"circuit","title":"Problem 9(b)","nodes":[{"id":"x2","gate":"INPUT","x":70,"y":90,"label":"x₂"},{"id":"x1","gate":"INPUT","x":70,"y":230,"label":"x₁"},{"id":"x3","gate":"INPUT","x":70,"y":380,"label":"x₃"},{"id":"N1","gate":"NAND","x":260,"y":230,"label":"x̄₁"},{"id":"N2","gate":"NAND","x":450,"y":120,"label":""},{"id":"N3","gate":"NAND","x":450,"y":330,"label":""},{"id":"F","gate":"NAND","x":640,"y":225,"label":" "},{"id":"f","gate":"OUTPUT","x":820,"y":225,"label":"f"}],"wires":[{"start":"x1.out","end":"N1.0"},{"start":"x1.out","end":"N1.1"},{"start":"x2.out","end":"N2.0"},{"start":"N1.out","end":"N2.1"},{"start":"x1.out","end":"N3.0","via":[[160,230],[160,320]]},{"start":"x3.out","end":"N3.1"},{"start":"N2.out","end":"F.0"},{"start":"N3.out","end":"F.1"},{"start":"F.out","end":"f.0"}]}
#+ $\overline{x_1x_1}=\bar x_1$
--
$\overline{x_1x_1}=\bar x_1$ (7a, then the bar).
== The middle NANDs
{"kind":"circuit","title":"Problem 9(b)","nodes":[{"id":"x2","gate":"INPUT","x":70,"y":90,"label":"x₂"},{"id":"x1","gate":"INPUT","x":70,"y":230,"label":"x₁"},{"id":"x3","gate":"INPUT","x":70,"y":380,"label":"x₃"},{"id":"N1","gate":"NAND","x":260,"y":230,"label":"x̄₁"},{"id":"N2","gate":"NAND","x":450,"y":120,"label":"NOT(x̄₁x₂)"},{"id":"N3","gate":"NAND","x":450,"y":330,"label":"NOT(x₁x₃)"},{"id":"F","gate":"NAND","x":640,"y":225,"label":" "},{"id":"f","gate":"OUTPUT","x":820,"y":225,"label":"f"}],"wires":[{"start":"x1.out","end":"N1.0"},{"start":"x1.out","end":"N1.1"},{"start":"x2.out","end":"N2.0"},{"start":"N1.out","end":"N2.1"},{"start":"x1.out","end":"N3.0","via":[[160,230],[160,320]]},{"start":"x3.out","end":"N3.1"},{"start":"N2.out","end":"F.0"},{"start":"N3.out","end":"F.1"},{"start":"F.out","end":"f.0"}]}
#+ $\overline{\bar x_1x_2}$
#+ $\overline{x_1x_3}$
--
Top: NAND of $\bar x_1$ and $x_2$. Bottom: NAND of $x_1$ and $x_3$.
== The output NAND
{"kind":"circuit","title":"Problem 9(b)","nodes":[{"id":"x2","gate":"INPUT","x":70,"y":90,"label":"x₂"},{"id":"x1","gate":"INPUT","x":70,"y":230,"label":"x₁"},{"id":"x3","gate":"INPUT","x":70,"y":380,"label":"x₃"},{"id":"N1","gate":"NAND","x":260,"y":230,"label":"x̄₁"},{"id":"N2","gate":"NAND","x":450,"y":120,"label":"NOT(x̄₁x₂)"},{"id":"N3","gate":"NAND","x":450,"y":330,"label":"NOT(x₁x₃)"},{"id":"F","gate":"NAND","x":640,"y":225,"label":"x̄₁x₂ + x₁x₃"},{"id":"f","gate":"OUTPUT","x":820,"y":225,"label":"f"}],"wires":[{"start":"x1.out","end":"N1.0"},{"start":"x1.out","end":"N1.1"},{"start":"x2.out","end":"N2.0"},{"start":"N1.out","end":"N2.1"},{"start":"x1.out","end":"N3.0","via":[[160,230],[160,320]]},{"start":"x3.out","end":"N3.1"},{"start":"N2.out","end":"F.0"},{"start":"N3.out","end":"F.1"},{"start":"F.out","end":"f.0"}]}
#+ $f=\bar x_1x_2+x_1x_3$
--
De Morgan (15a), then the double bars cancel (9):

$$
f=\overline{\overline{\bar x_1x_2}\cdot\overline{x_1x_3}}=\bar x_1x_2+x_1x_3
$$
```

**Shortcut:** a two-level NAND–NAND is always an SOP. Each first-level NAND is one product term, so you can read $\bar x_1x_2+x_1x_3$ straight off.

**Answer:** $f=\bar x_1x_2+x_1x_3$. That's the prime-number function from Problem 4.

*Review: Note 02 §9.*

</details>

### Problem 10 · POS → NOR only [6 marks]

*The NOR mirror image of past midterm Q1.*

**10.** (a) Consider the function $f(x_1,x_2,x_3)=\prod M(1,3,4,5)$. First, find the canonical POS expression. Then, find the minimum POS expression and implement it using only NOR gates. **[4]**

(b) Implement $g=x_1x_2+\bar x_3$ using only NOR gates. **[2]**

*Sources: Section2_Logic_Circuits.pdf, p. 50; Section2_Logic_Circuits.pdf, p. 51*

<details><summary>Formula sheet: NAND and NOR (given in the exam)</summary>

- **NAND gate:** $\overline{x_1x_2}=\bar x_1+\bar x_2$. A NAND is an OR with bubbles on its inputs.
- **NOR gate:** $\overline{x_1+x_2}=\bar x_1\,\bar x_2$. A NOR is an AND with bubbles on its inputs.
- **NOT:** a NAND or a NOR with both inputs tied together.
- The sheet also draws **SOP → NAND–NAND** and **POS → NOR–NOR** networks.

</details>

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 2*

<details><summary>Solution (a)</summary>

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

```logicsteps
title "Problem 10(a): OR–AND into NOR–NOR"
== Draw the normal OR–AND circuit
{"kind":"circuit","title":"f = (x1 + NOT x3)(NOT x1 + x2)","nodes":[{"id":"x3","gate":"INPUT","x":70,"y":90,"label":"x₃"},{"id":"x1","gate":"INPUT","x":70,"y":200,"label":"x₁"},{"id":"x2","gate":"INPUT","x":70,"y":380,"label":"x₂"},{"id":"N3","gate":"NOT","x":260,"y":90,"label":"x̄₃"},{"id":"N1","gate":"NOT","x":260,"y":290,"label":"x̄₁"},{"id":"U","gate":"OR","x":450,"y":120,"label":"x₁ + x̄₃"},{"id":"V","gate":"OR","x":450,"y":300,"label":"x̄₁ + x₂"},{"id":"G","gate":"AND","x":640,"y":210,"label":"(x₁ + x̄₃)(x̄₁ + x₂)"},{"id":"f","gate":"OUTPUT","x":860,"y":210,"label":"f"}],"wires":[{"start":"x3.out","end":"N3.0"},{"start":"N3.out","end":"U.0","via":[[330,90],[330,110]]},{"start":"x1.out","end":"U.1","via":[[370,200],[370,130]]},{"start":"x1.out","end":"N1.0","via":[[160,200],[160,290]]},{"start":"N1.out","end":"V.0"},{"start":"x2.out","end":"V.1","via":[[360,380],[360,310]]},{"start":"U.out","end":"G.0"},{"start":"V.out","end":"G.1"},{"start":"G.out","end":"f.0"}]}
--
Two NOTs, one OR per bracket, and an AND at the end.
== Swap every OR and the AND for NORs
{"kind":"circuit","title":"f = (x1 + NOT x3)(NOT x1 + x2)","nodes":[{"id":"x3","gate":"INPUT","x":70,"y":90,"label":"x₃"},{"id":"x1","gate":"INPUT","x":70,"y":200,"label":"x₁"},{"id":"x2","gate":"INPUT","x":70,"y":380,"label":"x₂"},{"id":"N3","gate":"NOT","x":260,"y":90,"label":"x̄₃"},{"id":"N1","gate":"NOT","x":260,"y":290,"label":"x̄₁"},{"id":"U","gate":"NOR","x":450,"y":120,"label":"NOT(x₁ + x̄₃)"},{"id":"V","gate":"NOR","x":450,"y":300,"label":"NOT(x̄₁ + x₂)"},{"id":"G","gate":"NOR","x":640,"y":210,"label":"(x₁ + x̄₃)(x̄₁ + x₂)  ✓"},{"id":"f","gate":"OUTPUT","x":860,"y":210,"label":"f"}],"wires":[{"start":"x3.out","end":"N3.0"},{"start":"N3.out","end":"U.0","via":[[330,90],[330,110]]},{"start":"x1.out","end":"U.1","via":[[370,200],[370,130]]},{"start":"x1.out","end":"N1.0","via":[[160,200],[160,290]]},{"start":"N1.out","end":"V.0"},{"start":"x2.out","end":"V.1","via":[[360,380],[360,310]]},{"start":"U.out","end":"G.0"},{"start":"V.out","end":"G.1"},{"start":"G.out","end":"f.0"}]}
--
Each first-level NOR gives a flipped sum. The last NOR is an AND with bubbles on its inputs (De Morgan), so it flips them back:

$$
\overline{\overline{x_1+\bar x_3}+\overline{\bar x_1+x_2}}=(x_1+\bar x_3)(\bar x_1+x_2)
$$

There's no one-letter term here, so nothing needs flipping.
== Make the NOTs out of NORs
{"kind":"circuit","title":"f = (x1 + NOT x3)(NOT x1 + x2)","nodes":[{"id":"x3","gate":"INPUT","x":70,"y":90,"label":"x₃"},{"id":"x1","gate":"INPUT","x":70,"y":200,"label":"x₁"},{"id":"x2","gate":"INPUT","x":70,"y":380,"label":"x₂"},{"id":"N3","gate":"NOR","x":260,"y":90,"label":"x̄₃ (tied NOR)"},{"id":"N1","gate":"NOR","x":260,"y":290,"label":"x̄₁ (tied NOR)"},{"id":"U","gate":"NOR","x":450,"y":120,"label":"NOT(x₁ + x̄₃)"},{"id":"V","gate":"NOR","x":450,"y":300,"label":"NOT(x̄₁ + x₂)"},{"id":"G","gate":"NOR","x":640,"y":210,"label":"(x₁ + x̄₃)(x̄₁ + x₂)  ✓"},{"id":"f","gate":"OUTPUT","x":860,"y":210,"label":"f"}],"wires":[{"start":"x3.out","end":"N3.0"},{"start":"N3.out","end":"U.0","via":[[330,90],[330,110]]},{"start":"x1.out","end":"U.1","via":[[370,200],[370,130]]},{"start":"N1.out","end":"V.0"},{"start":"x2.out","end":"V.1","via":[[360,380],[360,310]]},{"start":"U.out","end":"G.0"},{"start":"V.out","end":"G.1"},{"start":"G.out","end":"f.0"},{"start":"x3.out","end":"N3.1"},{"start":"x1.out","end":"N1.0","via":[[160,200],[160,280]]},{"start":"x1.out","end":"N1.1","via":[[160,200],[160,300]]}]}
--
Tie both inputs of a NOR together to get a NOT. All 5 gates are NORs now. Try inputs to compare with the first step.
```

**Answer:** **5 NOR gates.**

*Review: Note 02 §9, POS → NOR–NOR.*

</details>

<details><summary>Solution (b)</summary>

1. **NOR–NOR needs a POS, but $g$ is an SOP.** Convert it with the distributive rule 12b, $x+yz=(x+y)(x+z)$, using $x=\bar x_3$, $y=x_1$, $z=x_2$.

   $$
   g=\bar x_3+x_1x_2=(x_1+\bar x_3)(x_2+\bar x_3)
   $$

2. **Build it with NORs.** One tied NOR makes $\bar x_3$ and feeds **both** sum terms.

```digital
{"kind":"circuit","title":"NOR only: g = (x1 + NOT x3)(x2 + NOT x3)","nodes":[{"id":"x1","gate":"INPUT","x":70,"y":90,"label":"x₁"},{"id":"x3","gate":"INPUT","x":70,"y":200,"label":"x₃"},{"id":"x2","gate":"INPUT","x":70,"y":330,"label":"x₂"},{"id":"N3","gate":"NOR","x":260,"y":200,"label":"x̄₃"},{"id":"U","gate":"NOR","x":450,"y":110,"label":"NOT(x₁ + x̄₃)"},{"id":"V","gate":"NOR","x":450,"y":290,"label":"NOT(x₂ + x̄₃)"},{"id":"G","gate":"NOR","x":640,"y":200,"label":"g"},{"id":"g","gate":"OUTPUT","x":820,"y":200,"label":"g"}],"wires":[{"start":"x3.out","end":"N3.0"},{"start":"x3.out","end":"N3.1"},{"start":"x1.out","end":"U.0"},{"start":"N3.out","end":"U.1"},{"start":"N3.out","end":"V.0"},{"start":"x2.out","end":"V.1"},{"start":"U.out","end":"G.0"},{"start":"V.out","end":"G.1"},{"start":"G.out","end":"g.0"}]}
```

*U and V are the two sums, flipped. The last NOR flips them back and ANDs them.*

**Check:** $\overline{U+V}=\bar U\,\bar V=(x_1+\bar x_3)(x_2+\bar x_3)=g$ ✓

**Answer:** **4 NOR gates.**

*Review: Note 02 §9.*

</details>

## Transistors and CMOS

*Sources: Chapter3_Implementation_technology Lecture 1.pdf, p. 6*

### Problem 11 · CMOS and NMOS gates [8 marks]

*Like PS2 Q1 and Q3–Q5 and the Week 5 lecture.*

**11.** (a) Draw a CMOS circuit (one complex gate) that implements $f=\bar x_1\bar x_2+\bar x_3$. How many transistors does it use? **[3]**

(b) What function does the CMOS circuit below implement? Give its truth table as $\sum m(\ldots)$. **[3]**

```digital
{"kind":"cmos","title":"Problem 11(b)","pdn":{"parallel":[{"series":[{"gate":"x1"},{"gate":"x2"}]},{"gate":"x3"}]}}
```

*Problem 11(b): read the NMOS half first.*

(c) How many transistors does $f=x_1x_2+x_3$ need in basic static CMOS? **[1]**

(d) The NMOS gate below uses a pull-up resistor and two NMOS switches in parallel. Name the gate. When $x_1=1$ and $x_2=0$, is the output high or low, and does current flow from $V_{DD}$ to ground? **[1]**

```schematic
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

*Ideal-switch model: each NMOS closes when its input is 1.*

*Sources: Problem_set_2.pdf, p. 1; Problem_set_2.pdf, p. 2; Chapter3_Implementation_technology Lecture 1.pdf, p. 11; Chapter3_Implementation_technology Lecture 1.pdf, p. 12; Chapter3_Implementation_technology Lecture 1.pdf, p. 24*

<details><summary>Formula sheet: NMOS and PMOS (given in the exam)</summary>

| | Gate at $V_{DD}$ (logic 1) | Gate at 0 V (logic 0) |
|---|---|---|
| **NMOS** | on: closed switch, pulls the drain **down** to ground | off: open switch |
| **PMOS** | off: open switch | on: closed switch, pulls the drain **up** to $V_{DD}$ |

</details>

*Sources: ELEC 271 Midterm Formula Sheet.pdf, p. 3*

<details><summary>Solution (a)</summary>

1. **Complement first.** The NMOS pull-down network (PDN) must conduct exactly when $f=0$. So find $\bar f$ with De Morgan (15b, then 15a).

   $$
   \bar f=\overline{\bar x_1\bar x_2+\bar x_3}=\overline{\bar x_1\bar x_2}\cdot x_3=(x_1+x_2)\,x_3
   $$

2. **PDN (NMOS):** OR = parallel, AND = series. NMOS $x_1$ in parallel with NMOS $x_2$, then in series with NMOS $x_3$.

3. **PUN (PMOS) is the dual:** swap series and parallel, keep the same gate labels. PMOS $x_1$ and $x_2$ in series, in parallel with PMOS $x_3$.

```digital
{"kind":"cmos","title":"f = NOT x1 NOT x2 + NOT x3","pdn":{"series":[{"parallel":[{"gate":"x1"},{"gate":"x2"}]},{"gate":"x3"}]}}
```

*PDN: (x₁ ∥ x₂) in series with x₃. PUN: (x₁ — x₂ in series) ∥ x₃.*

4. **Check the pull-up.** Series PMOS $x_1, x_2$ both conduct when $x_1=x_2=0$, giving $\bar x_1\bar x_2$. PMOS $x_3$ conducts when $x_3=0$, giving $\bar x_3$. So the output is pulled up exactly when $\bar x_1\bar x_2+\bar x_3=1$ ✓

**Answer:** 3 NMOS + 3 PMOS = **6 transistors**. No inverters needed: the bars in $f$ come free, because a CMOS gate always inverts.

*Review: Note 03 §3, Function → pull-down → dual pull-up.*

</details>

<details><summary>Solution (b)</summary>

1. **Read the NMOS half.** Find every path from $f$ down to ground: through $x_1$ **and** $x_2$ in series, **or** through $x_3$.

   $$
   \text{PDN conducts when } x_1x_2+x_3=1
   $$

2. **When the PDN conducts, the output is 0.** So complement once:

   $$
   f=\overline{x_1x_2+x_3}=(\bar x_1+\bar x_2)\,\bar x_3
   $$

3. **Truth table:** $f=1$ needs $x_3=0$ (rows 0, 2, 4, 6) and not both $x_1, x_2$ (that removes row 6).

| Row | $x_1x_2x_3$ | PDN on? | $f$ |
|---|---|---|---|
| 0 | 000 | no | 1 |
| 1 | 001 | yes | 0 |
| 2 | 010 | no | 1 |
| 3 | 011 | yes | 0 |
| 4 | 100 | no | 1 |
| 5 | 101 | yes | 0 |
| 6 | 110 | yes | 0 |
| 7 | 111 | yes | 0 |

**Answer:** $f=\overline{x_1x_2+x_3}=\sum m(0,2,4)$.

**Check with the PMOS half:** PMOS $x_1 \parallel x_2$ in series with PMOS $x_3$ conducts when $(\bar x_1+\bar x_2)\bar x_3=1$. Same thing ✓

*Review: Note 03 §4, CMOS drawing → function.*

</details>

<details><summary>Solution (c)</summary>

CMOS gates always invert. One complex gate gives $\overline{x_1x_2+x_3}$: that's the circuit in part (b), 6 transistors. Add an inverter (2 transistors) to undo the bar.

$$
6+2=8 \text{ transistors}
$$

**Compare:** separate gates would be a 2-input AND (NAND + NOT = 6) and a 2-input OR (NOR + NOT = 6), so 12. The complex gate is cheaper.

*Review: Note 03 §2, transistor counting.*

</details>

<details><summary>Solution (d)</summary>

1. **Name it.** Either closed switch connects $f$ to ground, so the output is 0 when $x_1+x_2=1$.

   $$
   f=\overline{x_1+x_2}\quad\text{(NOR)}
   $$

2. **$x_1=1$:** that NMOS has its gate at $V_{DD}$, so it's on (a closed switch). The output is pulled **low**.

3. **Current: yes.** There's a complete path $V_{DD}$ → resistor → closed NMOS → ground, so current flows the whole time the output is low. That wasted power is why CMOS replaces the resistor with PMOS transistors: in CMOS, one of the two networks is always off.

*Review: Note 03 §1, Transistor switches and resistor-load NMOS gates.*

</details>
