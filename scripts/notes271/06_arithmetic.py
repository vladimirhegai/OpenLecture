"""PS4: signed encodings, add/subtract, overflow, full adders, carry lookahead."""

from itertools import product

from lib import Doc, S, circuit, cite, node, wire


def signed(v, n):
    return v - (1 << n) if v & (1 << (n - 1)) else v


assert format((-95) % 4096, "012b") == "111110100001"
assert format(2048 + 95, "012b") == "100001011111"
assert format((4095 ^ 95), "012b") == "111110100000"
assert signed(int("1011100111", 2), 10) == -281
assert signed((100 + 60) % 256, 8) == -96
assert signed((100 + 196) % 256, 8) == 40
for a, b, c in product((0, 1), repeat=3):
    s = a ^ b ^ c
    carry = (a & b) | ((a ^ b) & c)
    assert a + b + c == 2 * carry + s
for a, b in product(range(16), repeat=2):
    for ci in (0, 1):
        p = [((a >> i) & 1) ^ ((b >> i) & 1) for i in range(4)]
        g = [((a >> i) & 1) & ((b >> i) & 1) for i in range(4)]
        c = [ci]
        for i in range(4):
            c.append(g[i] | (p[i] & c[i]))
        result = sum((p[i] ^ c[i]) << i for i in range(4))
        assert result + 16 * c[4] == a + b + ci
        assert (c[3] ^ c[4]) == (not (-8 <= signed(a, 4) + signed(b, 4) + ci <= 7))

D = Doc(
    6, "Signed Numbers and Arithmetic Circuits", ["signed_numbers", "arithmetic_circuits", "carry_lookahead"]
)
D.P(
    "Problem Set 4 provides the number-representation, adder, overflow, and carry-lookahead tasks for this note; no Section 5 lecture was supplied.",
    cite("P4", 1),
)
D.H("Topic 1: Signed bit patterns", cite("P4", 1))
D.P(
    "Always state the width and encoding. The same bit pattern can mean different values. For $n$ bits:\n\n- **Unsigned:** 0 to $2^n-1$.\n- **Sign-and-magnitude:** the MSB is the sign; remaining bits hold the magnitude. Two zero encodings.\n- **One’s complement:** negate by inverting every bit. Two zero encodings.\n- **Two’s complement:** negate by inverting every bit and adding 1 at the fixed width. One zero encoding."
)
D.T(
    ["Encoding", "Range for n bits", "8-bit -5"],
    [
        ["Sign-and-magnitude", r"$-(2^{n-1}-1)$ to $2^{n-1}-1$", "10000101"],
        ["One’s complement", r"$-(2^{n-1}-1)$ to $2^{n-1}-1$", "11111010"],
        ["Two’s complement", r"$-2^{n-1}$ to $2^{n-1}-1$", "11111011"],
    ],
)
D.E(r"V_{2\mathrm{C}}=-b_{n-1}2^{n-1}+\sum_{i=0}^{n-2}b_i2^i")
D.P(
    "A quick two’s-complement decode: interpret the pattern as unsigned $U$; if the MSB is 1, subtract $2^n$. If the MSB is 0, its value is simply $U$."
)
D.X(
    "PS4 Q2: decode a negative number",
    r"Decode the 10-bit two’s-complement pattern 1011100111.",
    [
        S("The unsigned value is 512+128+64+32+4+2+1.", r"U=743"),
        S("The MSB is 1, so subtract 1024.", r"V=743-1024=-281"),
    ],
    r"$-281$.",
    cite("P4", 1),
)
D.X(
    "PS4 Q3: encode -95 at 12 bits",
    "Represent -95 in sign-and-magnitude, one’s complement, and two’s complement.",
    [
        S("Start with positive 95 padded to 12 bits.", r"95=(000001011111)_2"),
        S("For sign-and-magnitude, change only the sign bit.", r"-95\longrightarrow100001011111"),
        S("For one’s complement, invert all 12 bits.", r"-95\longrightarrow111110100000"),
        S("For two’s complement, add 1 to the inverted pattern.", r"-95\longrightarrow111110100001"),
    ],
    "Sign-and-magnitude: 100001011111; one’s: 111110100000; two’s: 111110100001.",
    cite("P4", 1),
)
D.P(
    "**Sign extension** preserves a two’s-complement value by repeating its sign bit on the left. Zero extension preserves an unsigned value. For example, 8-bit 11111011 becomes 12-bit 111111111011 and still means -5."
)
D.Q(
    "Try it: the exceptional negative value",
    "Can 8-bit two’s complement represent +128? What happens if you negate 10000000 at 8 bits?",
    [
        S("The signed range is -128 through +127."),
        S("Invert and add one: 01111111+1=10000000. The intended +128 is outside the range."),
    ],
    "No; 10000000 represents -128. Its fixed-width negation overflows and produces the same bit pattern.",
)
D.H("Topic 2: Full adders, subtraction, and overflow", cite("P4", 1))
D.P(
    "A **half adder** adds two bits: sum $S=A\\oplus B$, carry $C=AB$. A **full adder** also accepts carry-in $C_{in}$. Its two outputs encode the integer $A+B+C_{in}$ as $2C_{out}+S$."
)
D.E(r"S=A\oplus B\oplus C_{in}")
D.E(r"C_{out}=AB+(A\oplus B)C_{in}")
D.F(
    circuit(
        "Full adder from XOR and carry gates",
        [
            node("A", "INPUT", 70, 80),
            node("B", "INPUT", 70, 150),
            node("CI", "INPUT", 260, 390, label="Cin"),
            node("P", "XOR", 260, 115),
            node("G", "AND", 260, 215),
            node("S", "XOR", 455, 115),
            node("H", "AND", 455, 310),
            node("CO", "OR", 650, 250, label="Cout"),
            node("SUM", "OUTPUT", 650, 115, label="S"),
        ],
        [
            wire("A.out", "P.0"),
            wire("B.out", "P.1"),
            wire("A.out", "G.0", [[150, 80], [150, 205]]),
            wire("B.out", "G.1", [[175, 150], [175, 225]]),
            wire("P.out", "S.0"),
            wire("CI.out", "S.1", [[370, 390], [370, 125]]),
            wire("P.out", "H.0", [[350, 115], [350, 300]]),
            wire("CI.out", "H.1"),
            wire("G.out", "CO.0"),
            wire("H.out", "CO.1"),
            wire("S.out", "SUM.0"),
        ],
    ),
    "P=A XOR B; G=AB. The carry OR combines a generated carry with a propagated carry.",
    cite("P4", 1),
)
D.X(
    "PS4 Q5: why two half adders work",
    "Prove that a half adder for A,B followed by a half adder for its sum and Cin gives a full adder when their carries are ORed.",
    [
        S("The first sum and carry are P=A XOR B and G=AB."),
        S("The second stage gives S=P XOR Cin and H=P Cin."),
        S("OR the carries.", r"C_{out}=G+H=AB+(A\oplus B)C_{in}"),
    ],
    "The sum and carry match the full-adder equations for every one of the eight input cases.",
    cite("P4", 1),
)
D.P(
    "An $n$-bit **ripple-carry adder** connects each bit’s carry-out to the next bit’s carry-in. Fixed-width arithmetic keeps the lowest $n$ sum bits. A final carry is a separate output, not automatically a signed overflow."
)
D.E(r"A-B=A+\overline B+1\pmod{2^n}")
D.P(
    "One adder can perform both operations. XOR each $B_i$ with mode $M$ and set $C_0=M$: M=0 adds B; M=1 complements B and adds the extra 1 for subtraction."
)
D.X(
    "Carry-out and signed overflow differ",
    "Use eight-bit two’s-complement arithmetic for 100+60 and 100+(-60).",
    [
        S("For 100+60, the stored pattern is 10100000, which decodes as -96.", r"100+60=160>127"),
        S("Two positive operands produced a negative result, so signed overflow occurred."),
        S("For 100+(-60), the bit sum is 100+196=296: carry-out 1 and stored value 40.", r"100+(-60)=40"),
    ],
    "100+60: signed overflow, carry-out 0. 100+(-60): no signed overflow, carry-out 1.",
    cite("P4", 1),
)
D.E(r"V=C_{n-1}\oplus C_n")
D.P(
    "$C_{n-1}$ is carry into the sign bit and $C_n$ is carry out. For addition, overflow also means “same-sign operands, result with the opposite sign.”"
)
D.X(
    "PS4 Q6: prove the carry test",
    "Why does XOR of the carries into and out of the sign position detect signed overflow?",
    [
        S(
            "When the operand sign bits differ, the carry-out equals carry-in. The sum lies between the operands and cannot exceed the signed range."
        ),
        S("With signs 0,0, the output carry is 0; a carry-in 1 makes the result sign 1: positive overflow."),
        S("With signs 1,1, the output carry is 1; a carry-in 0 makes the result sign 0: negative overflow."),
    ],
    "Exactly the overflow cases have unequal sign-position carries.",
    cite("P4", 1),
)
D.Q(
    "Try it: three-input population count",
    "Design a circuit whose two-bit unsigned output gives the number of 1s among A,B,C.",
    [S("A full adder already encodes A+B+C as carry and sum.", r"N_1=AB+AC+BC,\quad N_0=A\oplus B\oplus C")],
    "Use a full adder; output N1N0 = Cout,S. For 111, the count is 11 (3).",
    cite("P4", 1),
)
D.H("Topic 3: Carry lookahead", cite("P4", 1))
D.P(
    "For bit $i$, define **generate** $G_i=A_iB_i$ and **propagate** $P_i=A_i\\oplus B_i$. The carry relation is $C_{i+1}=G_i+P_iC_i$, and $S_i=P_i\\oplus C_i$. Lookahead expands the carry equations so carries need not ripple one bit at a time."
)
D.E(r"C_1=G_0+P_0C_0")
D.E(r"C_2=G_1+P_1G_0+P_1P_0C_0")
D.E(r"C_3=G_2+P_2G_1+P_2P_1G_0+P_2P_1P_0C_0")
D.X(
    "Carry without a ripple chain",
    r"For four-bit $A=1011$, $B=0101$, $C_0=0$, find the carries and sum.",
    [
        S("Write P and G in MSB-to-LSB order.", r"P=1110,\quad G=0001"),
        S("Bit 0 generates a carry; every higher bit propagates it.", r"C_1=C_2=C_3=C_4=1"),
        S("XOR each P bit with its own carry-in.", r"S=0000"),
    ],
    "Unsigned result is 1 0000 =16. As signed inputs, -5+5=0, with no signed overflow.",
)
D.P(
    "A two-bit block (low bit $i$, high bit $i+1$) has block propagate $P_b=P_{i+1}P_i$ and block generate $G_b=G_{i+1}+P_{i+1}G_i$. Its carry-out is $G_b+P_bC_i$."
)
D.X(
    "PS4 Q8: hierarchical four-bit lookahead",
    "Build a four-bit carry scheme from two two-bit blocks, L for bits 1:0 and H for bits 3:2.",
    [
        S("The lower block generates C2.", r"C_2=G_L+P_LC_0"),
        S("Substitute that carry into the upper block.", r"C_4=G_H+P_HG_L+P_HP_LC_0"),
        S("Within each block, compute its intermediate carry for the sum bits."),
    ],
    "Use two two-bit blocks plus block-level carry logic; both propagate and generate signals are required.",
    cite("P4", 1),
)
D.X(
    "PS4 Q7: count a flat lookahead implementation",
    r"Count gates for an n-bit adder with XOR propagate, variable $C_0$, unrestricted fan-in, and separately expanded carries. Do not share product gates across carries.",
    [
        S("P and S require 2n XORs; G requires n ANDs."),
        S(
            "Carry Ck uses k new AND terms and one OR. Sum k from 1 to n.",
            r"N_{\mathrm{AND,carry}}=\tfrac{n(n+1)}2",
        ),
        S("Add the n carry ORs.", r"N_{\mathrm{gates}}=\tfrac{n(n+1)}2+4n"),
    ],
    "This count follows the stated architecture. Constants, sharing, library gates, or fan-in limits change it.",
    cite("P4", 1),
)
D.Q(
    "Try it: carry versus propagate",
    "If a two-bit block has Pb=0 and Gb=1, does its output carry depend on the block carry-in?",
    [S("Substitute the block values.", r"C_{out}=G_b+P_bC_{in}=1")],
    "No. The block generates a carry regardless of its carry-in.",
)
D.save()
