# 01 · Binary Numbers — Midterm

**Midterm: Weeks 1–5.** This is one of the three main study sections for the 40-minute October 29 midterm.

## 1. Place value and unsigned binary

A **bit** is one binary digit: 0 or 1. A bit pattern gets its numerical meaning from its base, bit width, and encoding.

- **MSB:** the leftmost, highest-weight bit.
- **LSB:** the rightmost, lowest-weight bit.
- **Nibble:** 4 bits. **Byte:** 8 bits. These first examples are unsigned.

In base $k$, every digit is between $0$ and $k-1$. Moving one position left multiplies its weight by $k$; moving right across the radix point divides by $k$.

$$V=\sum_{i=-m}^{n-1}b_i k^i$$

$b_i$ is the digit at position $i$; $n$ digits lie before the radix point and $m$ after it. The units digit has index 0.

| Position | 3 | 2 | 1 | 0 | -1 | -2 | -3 |
|---|---|---|---|---|---|---|---|
| Binary weight | 8 | 4 | 2 | 1 | 1/2 | 1/4 | 1/8 |
| Example digit | 1 | 0 | 1 | 0 | 0 | 1 | 0 |

**Example: Lecture example: a binary fraction**

Convert $(1010.01)_2$ to decimal.

1. Only the 1 bits contribute.

   $$V=2^3+2^1+2^{-2}$$
2. Evaluate the weights.

   $$V=8+2+\tfrac14=10.25$$

**Answer:** $(1010.01)_2=(10.25)_{10}$.

An unsigned $n$-bit integer has $2^n$ distinct patterns, representing $0$ through $2^n-1$. Leading zeroes preserve the value but may specify the required width.

**Example: Tutorial 2: choosing a width**

How many bits are needed to represent decimal 1029 as an unsigned integer?

1. Ten bits represent only 0 through 1023.

   $$2^{10}-1=1023<1029$$
2. Eleven bits include the required value.

   $$1029<2^{11}=2048$$

**Answer:** 11 bits. Count the full range, including zero.

**Problem: Try it: decode the radix point** (intermediate)

Find the decimal value of $(110.101)_2$.

<details><summary>Solution</summary>

1. Use negative exponents to the right of the point.

   $$4+2+\tfrac12+\tfrac18=6.625$$

**Answer:** $6.625$.

</details>

## 2. Decimal ↔ binary, including fractions

Convert the two sides of the radix point separately.

- **Integer:** repeatedly divide by the target base; read the remainders from bottom to top.
- **Fraction:** repeatedly multiply by the target base; take each integer part in top-to-bottom order and continue with the remaining fraction.

**Example: Lecture example: $23.375$ to binary**

Convert $(23.375)_{10}$ to binary.

1. Divide the integer part by 2. The remainder is the next bit from the right.

   $$23=2(11)+1,\quad11=2(5)+1$$
2. Continue until the quotient is zero.

   $$5=2(2)+1,\quad2=2(1)+0,\quad1=2(0)+1$$
3. Read the remainders upward.

   $$23=(10111)_2$$
4. Multiply the fraction by 2; save each integer part.

   $$0.375(2)=0.75,\quad0.75(2)=1.5$$
5. Continue using only the remaining fractional part.

   $$0.5(2)=1.0\quad\Rightarrow\quad0.375=(.011)_2$$

**Answer:** $(23.375)_{10}=(10111.011)_2$.

The integer remainders arrive LSB first because each division removes the lowest-weight digit. Fractional multiplication reveals the highest-weight fractional digit first.

| Fraction remaining | Multiply by 2 | Next bit |
|---|---|---|
| 0.2 | 0.4 | 0 |
| 0.4 | 0.8 | 0 |
| 0.8 | 1.6 | 1 |
| 0.6 | 1.2 | 1 |

For $0.2$, the remaining fraction returns to $0.2$, so the bits repeat: $(0.2)_{10}=(.\overline{0011})_2$. A reduced fraction terminates in binary only when its denominator is a power of two.

**Example: Past midterm: limited precision**

Approximate $2/3$ with four binary fractional bits, truncating after the fourth bit. Find the absolute error.

1. Repeated doubling gives the repeating pattern 10.

   $$\tfrac23=(.101010\ldots)_2$$
2. Keep four fractional bits.

   $$(.1010)_2=\tfrac12+\tfrac18=\tfrac58$$
3. Subtract the approximation from the exact value.

   $$\tfrac23-\tfrac58=\tfrac1{24}\approx0.0416667$$

**Answer:** $0.625$, which is below $2/3$ by $1/24$. Truncation and rounding are different instructions.

With $m$ binary fractional bits, the spacing is $2^{-m}$. For a nonnegative value, truncation has error less than $2^{-m}$; rounding to nearest has error at most $2^{-(m+1)}$, assuming the rounded value fits.

**Problem: Try it: detect a repeating expansion** (intermediate)

Does $3/20$ terminate in binary? Find its first four fractional bits and the truncation error.

<details><summary>Solution</summary>

1. The reduced denominator 20 contains a factor of 5, so the binary expansion repeats.
2. Doubling gives integer parts 0, 0, 1, 0.

   $$(.0010)_2=\tfrac18$$
3. Compare exact fractions.

   $$\tfrac3{20}-\tfrac18=\tfrac1{40}=0.025$$

**Answer:** No; four-bit truncation is $.0010_2=0.125$, error $0.025$.

</details>

## 3. Hexadecimal, including fractions

Each hexadecimal digit corresponds to exactly four bits because $16=2^4$. A–F represent decimal 10–15.

Start at the radix point and group outward. Add leading zeroes on the integer side or trailing zeroes on the fraction side; never insert padding next to the radix point.

| Hex | Binary | Hex | Binary |
|---|---|---|---|
| 0 | 0000 | 8 | 1000 |
| 1 | 0001 | 9 | 1001 |
| 2 | 0010 | A | 1010 |
| 3 | 0011 | B | 1011 |
| 4 | 0100 | C | 1100 |
| 5 | 0101 | D | 1101 |
| 6 | 0110 | E | 1110 |
| 7 | 0111 | F | 1111 |

**Example: Binary to hex: pad from the radix point**

Convert $(10110110.101)_2$ to hexadecimal.

1. Group each side in fours.

   $$1011\;0110.1010$$
2. Translate each group independently.

   $$(10110110.101)_2=(\mathrm{B6.A})_{16}$$

**Answer:** $(\mathrm{B6.A})_{16}$. Padding .101 to .1010 preserves the fraction; .0101 would change it.

**Example: Decimal fraction directly to hex**

Convert $(13.625)_{10}$ to hexadecimal, then check it in decimal.

1. The integer 13 is the hex digit D.
2. Multiply the fractional part by 16 and keep its integer part.

   $$0.625(16)=10.0\quad\Rightarrow\quad.\mathrm A$$
3. Check the positional weights.

   $$(\mathrm{D.A})_{16}=13+10(16^{-1})=13.625$$

**Answer:** $(\mathrm{D.A})_{16}$. Read fractional hex digits in the order generated.

**Problem: Try it: reverse a fractional hex value** (intermediate)

Convert $(2\mathrm{F}.4)_{16}$ to decimal and binary.

<details><summary>Solution</summary>

1. Weight the integer and fractional digits.

   $$2(16)+15+4/16=47.25$$
2. Replace each hex digit with four bits.

   $$0010\;1111.0100$$

**Answer:** $47.25$ and $(101111.01)_2$.

</details>
