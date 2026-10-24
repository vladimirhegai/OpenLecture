# 06 · Later · Signed Numbers and Arithmetic Circuits

**Later study — outside this midterm study set.** Keep this material for subsequent assessments; prioritize notes 01–03 now.

Problem Set 4 provides the number-representation, adder, overflow, and carry-lookahead tasks for this note; no Section 5 lecture was supplied.

## Topic 1: Signed bit patterns

Always state the width and encoding. The same bit pattern can mean different values. For $n$ bits:

- **Unsigned:** 0 to $2^n-1$.
- **Sign-and-magnitude:** the MSB is the sign; remaining bits hold the magnitude. Two zero encodings.
- **One’s complement:** negate by inverting every bit. Two zero encodings.
- **Two’s complement:** negate by inverting every bit and adding 1 at the fixed width. One zero encoding.

| Encoding | Range for n bits | 8-bit -5 |
|---|---|---|
| Sign-and-magnitude | $-(2^{n-1}-1)$ to $2^{n-1}-1$ | 10000101 |
| One’s complement | $-(2^{n-1}-1)$ to $2^{n-1}-1$ | 11111010 |
| Two’s complement | $-2^{n-1}$ to $2^{n-1}-1$ | 11111011 |

$$V_{2\mathrm{C}}=-b_{n-1}2^{n-1}+\sum_{i=0}^{n-2}b_i2^i$$

A quick two’s-complement decode: interpret the pattern as unsigned $U$; if the MSB is 1, subtract $2^n$. If the MSB is 0, its value is simply $U$.

**Example: PS4 Q2: decode a negative number**

Decode the 10-bit two’s-complement pattern 1011100111.

1. The unsigned value is 512+128+64+32+4+2+1.

   $$U=743$$
2. The MSB is 1, so subtract 1024.

   $$V=743-1024=-281$$

**Answer:** $-281$.

**Example: PS4 Q3: encode -95 at 12 bits**

Represent -95 in sign-and-magnitude, one’s complement, and two’s complement.

1. Start with positive 95 padded to 12 bits.

   $$95=(000001011111)_2$$
2. For sign-and-magnitude, change only the sign bit.

   $$-95\longrightarrow100001011111$$
3. For one’s complement, invert all 12 bits.

   $$-95\longrightarrow111110100000$$
4. For two’s complement, add 1 to the inverted pattern.

   $$-95\longrightarrow111110100001$$

**Answer:** Sign-and-magnitude: 100001011111; one’s: 111110100000; two’s: 111110100001.

**Sign extension** preserves a two’s-complement value by repeating its sign bit on the left. Zero extension preserves an unsigned value. For example, 8-bit 11111011 becomes 12-bit 111111111011 and still means -5.

**Problem: Try it: the exceptional negative value** (intermediate)

Can 8-bit two’s complement represent +128? What happens if you negate 10000000 at 8 bits?

<details><summary>Solution</summary>

1. The signed range is -128 through +127.
2. Invert and add one: 01111111+1=10000000. The intended +128 is outside the range.

**Answer:** No; 10000000 represents -128. Its fixed-width negation overflows and produces the same bit pattern.

</details>

## Topic 2: Full adders, subtraction, and overflow

A **half adder** adds two bits: sum $S=A\oplus B$, carry $C=AB$. A **full adder** also accepts carry-in $C_{in}$. Its two outputs encode the integer $A+B+C_{in}$ as $2C_{out}+S$.

$$S=A\oplus B\oplus C_{in}$$

$$C_{out}=AB+(A\oplus B)C_{in}$$

```digital
{"kind":"circuit","title":"Full adder from XOR and carry gates","nodes":[{"id":"A","gate":"INPUT","x":70,"y":80},{"id":"B","gate":"INPUT","x":70,"y":150},{"id":"CI","gate":"INPUT","x":260,"y":390,"label":"Cin"},{"id":"P","gate":"XOR","x":260,"y":115},{"id":"G","gate":"AND","x":260,"y":215},{"id":"S","gate":"XOR","x":455,"y":115},{"id":"H","gate":"AND","x":455,"y":310},{"id":"CO","gate":"OR","x":650,"y":250,"label":"Cout"},{"id":"SUM","gate":"OUTPUT","x":650,"y":115,"label":"S"}],"wires":[{"start":"A.out","end":"P.0"},{"start":"B.out","end":"P.1"},{"start":"A.out","end":"G.0","via":[[150,80],[150,205]]},{"start":"B.out","end":"G.1","via":[[175,150],[175,225]]},{"start":"P.out","end":"S.0"},{"start":"CI.out","end":"S.1","via":[[370,390],[370,125]]},{"start":"P.out","end":"H.0","via":[[350,115],[350,300]]},{"start":"CI.out","end":"H.1"},{"start":"G.out","end":"CO.0"},{"start":"H.out","end":"CO.1"},{"start":"S.out","end":"SUM.0"}]}
```

*P=A XOR B; G=AB. The carry OR combines a generated carry with a propagated carry.*

**Example: PS4 Q5: why two half adders work**

Prove that a half adder for A,B followed by a half adder for its sum and Cin gives a full adder when their carries are ORed.

1. The first sum and carry are P=A XOR B and G=AB.
2. The second stage gives S=P XOR Cin and H=P Cin.
3. OR the carries.

   $$C_{out}=G+H=AB+(A\oplus B)C_{in}$$

**Answer:** The sum and carry match the full-adder equations for every one of the eight input cases.

An $n$-bit **ripple-carry adder** connects each bit’s carry-out to the next bit’s carry-in. Fixed-width arithmetic keeps the lowest $n$ sum bits. A final carry is a separate output, not automatically a signed overflow.

$$A-B=A+\overline B+1\pmod{2^n}$$

One adder can perform both operations. XOR each $B_i$ with mode $M$ and set $C_0=M$: M=0 adds B; M=1 complements B and adds the extra 1 for subtraction.

**Example: Carry-out and signed overflow differ**

Use eight-bit two’s-complement arithmetic for 100+60 and 100+(-60).

1. For 100+60, the stored pattern is 10100000, which decodes as -96.

   $$100+60=160>127$$
2. Two positive operands produced a negative result, so signed overflow occurred.
3. For 100+(-60), the bit sum is 100+196=296: carry-out 1 and stored value 40.

   $$100+(-60)=40$$

**Answer:** 100+60: signed overflow, carry-out 0. 100+(-60): no signed overflow, carry-out 1.

$$V=C_{n-1}\oplus C_n$$

$C_{n-1}$ is carry into the sign bit and $C_n$ is carry out. For addition, overflow also means “same-sign operands, result with the opposite sign.”

**Example: PS4 Q6: prove the carry test**

Why does XOR of the carries into and out of the sign position detect signed overflow?

1. When the operand sign bits differ, the carry-out equals carry-in. The sum lies between the operands and cannot exceed the signed range.
2. With signs 0,0, the output carry is 0; a carry-in 1 makes the result sign 1: positive overflow.
3. With signs 1,1, the output carry is 1; a carry-in 0 makes the result sign 0: negative overflow.

**Answer:** Exactly the overflow cases have unequal sign-position carries.

**Problem: Try it: three-input population count** (intermediate)

Design a circuit whose two-bit unsigned output gives the number of 1s among A,B,C.

<details><summary>Solution</summary>

1. A full adder already encodes A+B+C as carry and sum.

   $$N_1=AB+AC+BC,\quad N_0=A\oplus B\oplus C$$

**Answer:** Use a full adder; output N1N0 = Cout,S. For 111, the count is 11 (3).

</details>

## Topic 3: Carry lookahead

For bit $i$, define **generate** $G_i=A_iB_i$ and **propagate** $P_i=A_i\oplus B_i$. The carry relation is $C_{i+1}=G_i+P_iC_i$, and $S_i=P_i\oplus C_i$. Lookahead expands the carry equations so carries need not ripple one bit at a time.

$$C_1=G_0+P_0C_0$$

$$C_2=G_1+P_1G_0+P_1P_0C_0$$

$$C_3=G_2+P_2G_1+P_2P_1G_0+P_2P_1P_0C_0$$

**Example: Carry without a ripple chain**

For four-bit $A=1011$, $B=0101$, $C_0=0$, find the carries and sum.

1. Write P and G in MSB-to-LSB order.

   $$P=1110,\quad G=0001$$
2. Bit 0 generates a carry; every higher bit propagates it.

   $$C_1=C_2=C_3=C_4=1$$
3. XOR each P bit with its own carry-in.

   $$S=0000$$

**Answer:** Unsigned result is 1 0000 =16. As signed inputs, -5+5=0, with no signed overflow.

A two-bit block (low bit $i$, high bit $i+1$) has block propagate $P_b=P_{i+1}P_i$ and block generate $G_b=G_{i+1}+P_{i+1}G_i$. Its carry-out is $G_b+P_bC_i$.

**Example: PS4 Q8: hierarchical four-bit lookahead**

Build a four-bit carry scheme from two two-bit blocks, L for bits 1:0 and H for bits 3:2.

1. The lower block generates C2.

   $$C_2=G_L+P_LC_0$$
2. Substitute that carry into the upper block.

   $$C_4=G_H+P_HG_L+P_HP_LC_0$$
3. Within each block, compute its intermediate carry for the sum bits.

**Answer:** Use two two-bit blocks plus block-level carry logic; both propagate and generate signals are required.

**Example: PS4 Q7: count a flat lookahead implementation**

Count gates for an n-bit adder with XOR propagate, variable $C_0$, unrestricted fan-in, and separately expanded carries. Do not share product gates across carries.

1. P and S require 2n XORs; G requires n ANDs.
2. Carry Ck uses k new AND terms and one OR. Sum k from 1 to n.

   $$N_{\mathrm{AND,carry}}=\tfrac{n(n+1)}2$$
3. Add the n carry ORs.

   $$N_{\mathrm{gates}}=\tfrac{n(n+1)}2+4n$$

**Answer:** This count follows the stated architecture. Constants, sharing, library gates, or fan-in limits change it.

**Problem: Try it: carry versus propagate** (intermediate)

If a two-bit block has Pb=0 and Gb=1, does its output carry depend on the block carry-in?

<details><summary>Solution</summary>

1. Substitute the block values.

   $$C_{out}=G_b+P_bC_{in}=1$$

**Answer:** No. The block generates a carry regardless of its carry-in.

</details>
