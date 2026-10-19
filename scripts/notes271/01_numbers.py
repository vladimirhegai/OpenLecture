"""Lecture 1 and Tutorial 2: positional notation and base conversion."""

from fractions import Fraction as F

from lib import Doc, S, cite

assert F(10) + F(1, 4) == F(41, 4)
assert F(23) + F(3, 8) == F(int("10111", 2)) + F(1, 4) + F(1, 8)
assert int("10110110", 2) == int("B6", 16) == int("266", 8) == 182
assert int("527", 8) == int("157", 16) == 343
assert F(2, 3) - F(5, 8) == F(1, 24)
assert int("A25F", 16) == 41567
assert 2**10 <= 1029 < 2**11

D = Doc(1, "Number Systems and Base Conversion", ["number_systems", "binary_numbers", "base_conversion"])
D.H("Topic 1: Bits and place value", cite("N", 30, 31, 36))
D.P(
    "A **bit** is one binary digit: 0 or 1. A bit pattern gets its numerical meaning from its base, bit width, and encoding.\n\n- **MSB:** the leftmost, highest-weight bit.\n- **LSB:** the rightmost, lowest-weight bit.\n- **Nibble:** 4 bits. **Byte:** 8 bits. These first examples are unsigned.",
    cite("N", 33, 36),
)
D.P(
    "In base $k$, every digit is between $0$ and $k-1$. Moving one position left multiplies its weight by $k$; moving right across the radix point divides by $k$.",
    cite("N", 30, 31),
)
D.E(r"V=\sum_{i=-m}^{n-1}b_i k^i", cite("N", 31))
D.P(
    "$b_i$ is the digit at position $i$; $n$ digits lie before the radix point and $m$ after it. The units digit has index 0.",
    cite("N", 31),
)
D.T(
    ["Position", "3", "2", "1", "0", "-1", "-2", "-3"],
    [
        ["Binary weight", "8", "4", "2", "1", "1/2", "1/4", "1/8"],
        ["Example digit", "1", "0", "1", "0", "0", "1", "0"],
    ],
    cite("N", 31),
)
D.X(
    "Lecture example: a binary fraction",
    r"Convert $(1010.01)_2$ to decimal.",
    [
        S("Only the 1 bits contribute.", r"V=2^3+2^1+2^{-2}"),
        S("Evaluate the weights.", r"V=8+2+\tfrac14=10.25"),
    ],
    r"$(1010.01)_2=(10.25)_{10}$.",
    cite("N", 31),
)
D.P(
    "An unsigned $n$-bit integer has $2^n$ distinct patterns, representing $0$ through $2^n-1$. Leading zeroes preserve the value but may specify the required width.",
    cite("N", 35),
)
D.X(
    "Tutorial 2: choosing a width",
    "How many bits are needed to represent decimal 1029 as an unsigned integer?",
    [
        S("Ten bits represent only 0 through 1023.", r"2^{10}-1=1023<1029"),
        S("Eleven bits include the required value.", r"1029<2^{11}=2048"),
    ],
    "11 bits. Count the full range, including zero.",
    cite("T", 1),
)
D.Q(
    "Try it: decode the radix point",
    r"Find the decimal value of $(110.101)_2$.",
    [S("Use negative exponents to the right of the point.", r"4+2+\tfrac12+\tfrac18=6.625")],
    "$6.625$.",
)
D.H("Topic 2: Converting decimal integers and fractions", cite("N", 37, 38, 39, 40))
D.P(
    "Convert the two sides of the radix point separately.\n\n- **Integer:** repeatedly divide by the target base; read the remainders from bottom to top.\n- **Fraction:** repeatedly multiply by the target base; take each integer part in top-to-bottom order and continue with the remaining fraction.",
    cite("N", 37, 38, 39),
)
D.X(
    "Lecture example: $23.375$ to binary",
    r"Convert $(23.375)_{10}$ to binary.",
    [
        S(
            "Divide the integer part by 2. The remainder is the next bit from the right.",
            r"23=2(11)+1,\quad11=2(5)+1",
        ),
        S("Continue until the quotient is zero.", r"5=2(2)+1,\quad2=2(1)+0,\quad1=2(0)+1"),
        S("Read the remainders upward.", r"23=(10111)_2"),
        S("Multiply the fraction by 2; save each integer part.", r"0.375(2)=0.75,\quad0.75(2)=1.5"),
        S(
            "Continue using only the remaining fractional part.",
            r"0.5(2)=1.0\quad\Rightarrow\quad0.375=(.011)_2",
        ),
    ],
    r"$(23.375)_{10}=(10111.011)_2$.",
    cite("N", 38, 39),
)
D.P(
    "The integer remainders arrive LSB first because each division removes the lowest-weight digit. Fractional multiplication reveals the highest-weight fractional digit first.",
    cite("N", 37, 39),
)
D.T(
    ["Fraction remaining", "Multiply by 2", "Next bit"],
    [["0.2", "0.4", "0"], ["0.4", "0.8", "0"], ["0.8", "1.6", "1"], ["0.6", "1.2", "1"]],
    cite("N", 40),
)
D.P(
    r"For $0.2$, the remaining fraction returns to $0.2$, so the bits repeat: $(0.2)_{10}=(.\overline{0011})_2$. A reduced fraction terminates in binary only when its denominator is a power of two.",
    cite("N", 40),
)
D.X(
    "Past midterm: limited precision",
    r"Approximate $2/3$ with four binary fractional bits, truncating after the fourth bit. Find the absolute error.",
    [
        S("Repeated doubling gives the repeating pattern 10.", r"\tfrac23=(.101010\ldots)_2"),
        S("Keep four fractional bits.", r"(.1010)_2=\tfrac12+\tfrac18=\tfrac58"),
        S(
            "Subtract the approximation from the exact value.",
            r"\tfrac23-\tfrac58=\tfrac1{24}\approx0.0416667",
        ),
    ],
    r"$0.625$, which is below $2/3$ by $1/24$. Truncation and rounding are different instructions.",
    cite("MID", 3),
)
D.P(
    "With $m$ binary fractional bits, the spacing is $2^{-m}$. For a nonnegative value, truncation has error less than $2^{-m}$; rounding to nearest has error at most $2^{-(m+1)}$, assuming the rounded value fits."
)
D.Q(
    "Try it: detect a repeating expansion",
    r"Does $3/20$ terminate in binary? Find its first four fractional bits and the truncation error.",
    [
        S("The reduced denominator 20 contains a factor of 5, so the binary expansion repeats."),
        S("Doubling gives integer parts 0, 0, 1, 0.", r"(.0010)_2=\tfrac18"),
        S("Compare exact fractions.", r"\tfrac3{20}-\tfrac18=\tfrac1{40}=0.025"),
    ],
    r"No; four-bit truncation is $.0010_2=0.125$, error $0.025$.",
)
D.H("Topic 3: Binary, octal, and hexadecimal", cite("N", 41, 42, 43))
D.P(
    "Group bits because these bases are powers of two.\n\n- Base 4: 2 bits per digit.\n- Base 8: 3 bits per digit.\n- Base 16: 4 bits per digit; A–F mean decimal 10–15.\n\nStart each grouping at the radix point and work outward. Pad the far left of an integer or far right of a fraction with zeroes.",
    cite("N", 42, 43),
)
D.T(
    ["Hex", "Binary", "Hex", "Binary"],
    [[f"{i:X}", f"{i:04b}", f"{i + 8:X}", f"{i + 8:04b}"] for i in range(8)],
    cite("N", 41),
)
D.X(
    "One pattern, two compact forms",
    r"Convert $(10110110)_2$ to hex and octal.",
    [
        S("Group by four for hex.", r"1011\;0110\Rightarrow(\mathrm{B6})_{16}"),
        S("Group by three for octal, padding only at the far left.", r"010\;110\;110\Rightarrow(266)_8"),
        S("Check the value independently.", r"2(8^2)+6(8)+6=182"),
    ],
    r"$(\mathrm{B6})_{16}=(266)_8=182$. Slide 43 prints 226 in its octal result; the grouping gives 266.",
    cite("N", 43),
)
D.X(
    "Octal to hex through binary",
    r"Convert $(527)_8$ to hexadecimal.",
    [
        S("Replace every octal digit with exactly three bits.", r"(527)_8=(101\;010\;111)_2"),
        S("Regroup from the right in fours.", r"0001\;0101\;0111\Rightarrow(157)_{16}"),
    ],
    r"$(157)_{16}$; both forms equal 343.",
    cite("N", 43),
)
D.Q(
    "Try it: group a fraction",
    r"Convert $(11010.101)_2$ to hexadecimal and octal.",
    [
        S(
            "Use groups of four on each side of the radix point.",
            r"0001\;1010.1010\Rightarrow(1\mathrm{A.A})_{16}",
        ),
        S("Use groups of three on each side.", r"011\;010.101\Rightarrow(32.5)_8"),
    ],
    r"$(1\mathrm{A.A})_{16}=(32.5)_8=26.625$.",
)
D.save()
