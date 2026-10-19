"""PS5: mux/cofactors/LUTs, decoders/encoders, routing and comparisons."""

from itertools import product

from lib import Doc, S, circuit, cite, node, wire

for a, b, c in product((0, 1), repeat=3):
    f0 = (not b) and (not c)
    f1 = b or (not c)
    assert (f1 if a else f0) == ((4 * a + 2 * b + c) in {0, 4, 6, 7})
for w in range(16):
    assert ((w << 1) & 15) == sum(((w >> (i - 1)) & 1) << i for i in range(1, 4))

D = Doc(
    7,
    "Multiplexers, Decoders, and Combinational Building Blocks",
    ["multiplexers", "decoders", "encoders", "shifters"],
)
D.P(
    "This note follows the design tasks in Problem Set 5 and the lecture’s 2-to-1 multiplexer example.",
    cite("P5", 1, 2),
)
D.H("Topic 1: Multiplexers and Shannon expansion", cite("L", 54))
D.P(
    "A **multiplexer (MUX)** selects one data input. For a 2-to-1 mux, select $S=0$ chooses $D_0$; $S=1$ chooses $D_1$. The select bit is a control input, not a third data choice."
)
D.E(r"Y=\overline S D_0+SD_1", cite("L", 54))
D.F(
    circuit(
        "Two-to-one multiplexer",
        [
            node("D0", "INPUT", 70, 90),
            node("D1", "INPUT", 70, 160),
            node("SEL", "INPUT", 70, 230, label="S"),
            node("M", "MUX", 285, 160),
            node("Y", "OUTPUT", 485, 160),
        ],
        [wire("D0.out", "M.0"), wire("D1.out", "M.1"), wire("SEL.out", "M.2"), wire("M.out", "Y.0")],
    ),
    "MUX ports are labeled 0, 1 and S; the output equals the selected data input.",
    cite("L", 54),
)
D.P(
    "A **cofactor** fixes one input: $F_0=F|_{A=0}$ and $F_1=F|_{A=1}$. Shannon expansion says $F=\\overline A F_0+AF_1$. A mux therefore implements any function if its data inputs implement the two cofactors.",
    cite("P5", 1),
)
D.X(
    "PS5 Q3: design a mux from cofactors",
    r"Implement $F(A,B,C)=\sum m(0,4,6,7)$ with one 2-to-1 mux and other necessary gates. Select on A.",
    [
        S("When A=0, only BC=00 gives 1.", r"F_0=\overline B\overline C"),
        S("When A=1, BC=00,10,11 give 1.", r"F_1=B+\overline C"),
        S(
            "Connect the cofactors to the corresponding mux data pins.",
            r"S=A,\quad D_0=\overline B\overline C,\quad D_1=B+\overline C",
        ),
    ],
    "The mux chooses F0 for A=0 and F1 for A=1. Share NOT C between the two cofactor circuits.",
    cite("P5", 1),
)
D.X(
    "Use two select inputs instead",
    "Implement the same function with a 4-to-1 mux, selecting by AB.",
    [
        S("For AB=00, F follows NOT C; for 01, F is always 0."),
        S(
            "For AB=10, F follows NOT C; for 11, F is always 1.",
            r"D_0=\overline C,\ D_1=0,\ D_2=\overline C,\ D_3=1",
        ),
    ],
    "One 4-to-1 mux and an inverter; address order must match AB=00,01,10,11.",
)
D.P(
    "Applying Shannon expansion repeatedly eventually fixes every input. The result is the canonical sum of minterms. Stopping earlier gives a useful mux tree instead.",
    cite("P5", 1),
)
D.X(
    "Build a function from two-input LUTs",
    r"Implement $F=AB+AC+BC$ using five 2-input LUTs.",
    [
        S("Three LUTs generate P=AB, Q=AC, R=BC. Each stores 0001 in address order 00,01,10,11."),
        S("A fourth LUT generates U=P OR Q; the fifth generates F=U OR R. Each OR LUT stores 0111."),
    ],
    "Five LUTs suffice. These are truth-table contents, not FPGA configuration-file bit ordering.",
    cite("P2", 2),
)
D.Q(
    "Try it: a mux as an inverter",
    "Implement NOT A using one 2-to-1 mux with select A and constant data inputs.",
    [S("At A=0 the output must be 1; at A=1 it must be 0.", r"D_0=1,\quad D_1=0")],
    "Connect D0=1 and D1=0.",
)
D.H("Topic 2: Decoders and encoders", cite("P5", 1, 2))
D.P(
    "An active-high **n-to-$2^n$ decoder** activates exactly the output whose index equals the binary input. Its outputs are the input minterms. With an enable E, all outputs are inactive when E=0."
)
D.T(
    ["AB", "Y0", "Y1", "Y2", "Y3"],
    [
        ["00", "1", "0", "0", "0"],
        ["01", "0", "1", "0", "0"],
        ["10", "0", "0", "1", "0"],
        ["11", "0", "0", "0", "1"],
    ],
)
D.E(r"Y_0=E\overline A\overline B,\quad Y_1=E\overline A B")
D.E(r"Y_2=EA\overline B,\quad Y_3=EAB")
D.X(
    "PS5 Q1: implement a function with a decoder",
    r"$F(A,B,C)=\sum m(0,2,3,4,5,7)$. Use a 3-to-8 active-high decoder.",
    [
        S("Connect A,B,C to the decoder in that bit order."),
        S("OR the outputs corresponding to the required minterms.", r"F=Y_0+Y_2+Y_3+Y_4+Y_5+Y_7"),
    ],
    "A 3-to-8 decoder plus the OR of those six outputs. Active-low decoder outputs require a different combining gate.",
    cite("P5", 1),
)
D.X(
    "PS5 Q9: build a decoder hierarchically",
    "Construct an enabled 3-to-8 decoder from two enabled 2-to-4 decoders.",
    [
        S("Feed the low two input bits B,C into both decoders."),
        S("Enable the lower-output bank with E AND NOT A, and the upper bank with E AND A."),
        S("The lower bank drives Y0–Y3; the upper drives Y4–Y7."),
    ],
    "Exactly one bank can be enabled for a binary A. This requires the sub-decoders to have enable inputs.",
    cite("P5", 2),
)
D.P(
    "An **encoder** does the reverse when exactly one input is active: it outputs that input’s binary index. A **priority encoder** defines which active input wins when several are 1. A separate valid flag distinguishes “input 0 active” from “nothing active.”",
    cite("P5", 1),
)
D.T(
    ["D3 D2 D1 D0", "Valid", "Index (D3 highest priority)"],
    [
        ["1---", "1", "11"],
        ["01--", "1", "10"],
        ["001-", "1", "01"],
        ["0001", "1", "00"],
        ["0000", "0", "00 (chosen default)"],
    ],
)
D.CODE("""library ieee;
use ieee.std_logic_1164.all;

entity priority4 is
  port (d : in std_logic_vector(3 downto 0);
        code : out std_logic_vector(1 downto 0);
        valid : out std_logic);
end entity;
architecture rtl of priority4 is
begin
  code <= "11" when d(3)='1' else
          "10" when d(2)='1' else
          "01" when d(1)='1' else "00";
  valid <= d(3) or d(2) or d(1) or d(0);
end architecture;""")
D.Q(
    "Try it: active-low outputs",
    "A decoder produces active-low outputs N0–N7. How do you combine N1,N3,N6 to implement a function that is 1 at minterms 1,3,6?",
    [S("Each Ni is the complement of the corresponding minterm.", r"F=\overline{N_1N_3N_6}")],
    "Use a NAND of N1,N3,N6; an OR would give the wrong function.",
)
D.H("Topic 3: Shifters and equality", cite("P5", 2))
D.P(
    "A **logical shifter** routes bit positions and fills vacated positions with zeroes. Let $W=w_3w_2w_1w_0$ and $Y=y_3y_2y_1y_0$, with $w_3$ the MSB.\n\n- Hold: $Y=W$.\n- Shift left: $Y=w_2w_1w_0 0$.\n- Shift right: $Y=0w_3w_2w_1$."
)
D.X(
    "PS5 Q10: four-bit bidirectional shifter",
    "Design hold/left/right selection when Right and Left are never both 1.",
    [
        S(
            "Use the same two controls for one mux per output bit. Let H mean neither shift is requested.",
            r"H=\overline R\overline L",
        ),
        S("MSB chooses hold w3, left w2, or right zero.", r"y_3=Hw_3+Lw_2"),
        S("Interior bits choose their corresponding neighbors.", r"y_2=Hw_2+Lw_1+Rw_3"),
        S("Finish the low two positions.", r"y_1=Hw_1+Lw_0+Rw_2,\quad y_0=Hw_0+Rw_1"),
    ],
    "Four routing muxes. The equations rely on the specified exclusion of R=L=1.",
    cite("P5", 2),
)
D.X(
    "Follow the bit order",
    "For W=1011, give hold, one logical left shift, and one logical right shift.",
    [S("Keep four output positions and discard bits shifted out."), S("Fill the new position with zero.")],
    "Hold 1011; left 0110; right 0101. Arithmetic right shift is different for a negative signed value.",
)
D.P(
    "A four-bit equality detector compares corresponding bits using XNOR, then ANDs the four equality results. It checks bit-pattern equality regardless of whether those patterns are interpreted as signed or unsigned.",
    cite("P4", 1),
)
D.E(r"Equal=\prod_{i=0}^{3}\overline{A_i\oplus B_i}")
D.Q(
    "Try it: replace zero-fill with rotation",
    "What is the one-bit rotate-left result for W=1011? How must the shifter’s MSB/LSB routing change?",
    [S("A rotation returns the bit shifted out to the other end.", r"Y=w_2w_1w_0w_3")],
    "0111. For rotate left, y0 receives w3 instead of 0; the other left-shift connections are unchanged.",
)
D.save()
