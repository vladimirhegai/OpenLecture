"""PS6: storage, registers, counters, and timing constraints."""

from itertools import product

from lib import Doc, S, cite

clk = "00110011"
data = "00010110"
q = 0
qff = []
ql = 0
latch = []
for i, (c, d) in enumerate(zip(clk, data)):
    if i and clk[i - 1] == "0" and c == "1":
        q = int(d)
    if c == "1":
        ql = int(d)
    qff.append(str(q))
    latch.append(str(ql))
assert "".join(qff) == "00000011" and "".join(latch) == "00011110"
for d, q2, q1, q0 in product((0, 1), repeat=4):
    q = (q2 << 2) | (q1 << 1) | q0
    ts = [1, q0 ^ d, (q0 ^ d) & (q1 ^ d)]
    nextq = sum((v ^ t) << i for i, (v, t) in enumerate(zip([q0, q1, q2], ts)))
    assert nextq == (q + (-1 if d else 1)) % 8
assert abs(1 / (10.5e-9) / 1e6 - 95.238095) < 1e-5

D = Doc(
    8,
    "Latches, Flip-Flops, Registers, Counters, and Timing",
    ["flip_flops", "registers", "counters", "timing"],
)
D.P(
    "This note develops the storage and timing tasks in Problem Set 6. The referenced textbook figure distinguishes a latch and two edge-triggered flip-flops; the supplied figure pages are available beside these notes.",
    cite("P6", 1, 2),
)
D.H("Topic 1: Store a bit at a level or an edge", cite("P6", 1))
D.P(
    "A combinational output depends on current inputs. A **sequential** circuit also depends on stored state. Write $Q$ for the present stored bit and $Q^+$ for its next value.\n\n- **D latch:** transparent while enable is active; it holds its last value while enable is inactive.\n- **D flip-flop:** samples D only at its active clock edge; it holds between edges.\n- A clock triangle means edge triggering. A bubble at a control input indicates active-low polarity."
)
D.P(
    "A NOR-based **SR latch** holds for S=R=0, sets for S=1,R=0, and resets for S=0,R=1. S=R=1 is forbidden for normal use: both outputs become 0, and release may not establish a predictable state. A NAND SR latch uses active-low controls and different input cases."
)
D.F(
    {
        "kind": "timing",
        "title": "D latch versus rising-edge DFF",
        "unit": "equal intervals; ideal propagation",
        "signals": [
            {"name": "CLK / EN", "wave": clk},
            {"name": "D", "wave": data},
            {"name": "Latch Q", "wave": "".join(latch)},
            {"name": "DFF Q", "wave": "".join(qff)},
        ],
        "edges": [2, 6],
    },
    "Both Q values start at 0. D is stable around each rising edge. The latch follows changes during high intervals; the DFF does not.",
)
D.X(
    "Read the waveform without guessing",
    "Why does the latch change in interval 3 while the DFF waits until interval 6?",
    [
        S("CLK is already high in interval 3, so the latch remains transparent."),
        S("The DFF sampled D=0 at the rising boundary 2 and retains that stored bit."),
        S("At rising boundary 6, D=1, so the DFF stores 1."),
    ],
    "A level-sensitive latch can change several times during one enable window; an edge-triggered DFF updates only at its sampling edge.",
)
D.T(
    ["Storage element", "Characteristic equation", "Input behavior"],
    [
        ["D flip-flop", r"$Q^+=D$", "Copy D at the edge"],
        ["T flip-flop", r"$Q^+=Q\oplus T$", "T=0 hold; T=1 toggle"],
        ["JK flip-flop", r"$Q^+=J\overline Q+\overline KQ$", "00 hold; 01 reset; 10 set; 11 toggle"],
    ],
)
D.T(
    ["Q → Q+", "D required", "T required", "J required", "K required"],
    [
        ["0 → 0", "0", "0", "0", "X"],
        ["0 → 1", "1", "1", "1", "X"],
        ["1 → 0", "0", "1", "X", "1"],
        ["1 → 1", "1", "0", "X", "0"],
    ],
)
D.P(
    "The **excitation table** works backward from a desired state transition to the required flip-flop inputs. X means either binary choice works for that transition; it does not mean a physical unknown should be driven into the pin."
)
D.X(
    "PS6 Q2: make a JK flip-flop using a T flip-flop",
    r"Find T as a function of J,K,Q.",
    [
        S("A T flip-flop toggles exactly when the desired next state differs from Q.", r"T=Q\oplus Q^+"),
        S(
            "When Q=0, the desired next state is J, so T=J. When Q=1, the desired next state is NOT K, so T=K.",
            r"T=J\overline Q+KQ",
        ),
    ],
    r"$T=J\overline Q+KQ$.",
    cite("P6", 1),
)
D.X(
    "PS6 Q3: asynchronous reset in VHDL",
    "Describe a T flip-flop whose active-high reset forces Q=0 immediately.",
    [
        S("Include reset in the sensitivity list and test it before the clock edge."),
        S("Only the non-reset branch requires a rising clock edge."),
    ],
    "Reset does not wait for the clock. Deassertion still has physical recovery/removal constraints.",
    cite("P6", 1),
)
D.CODE(
    """library ieee;
use ieee.std_logic_1164.all;
entity t_ff is
  port (clk, reset, t : in std_logic; q : out std_logic);
end entity;
architecture rtl of t_ff is
  signal state : std_logic;
begin
  process(clk, reset)
  begin
    if reset='1' then state <= '0';
    elsif rising_edge(clk) then state <= state xor t;
    end if;
  end process;
  q <= state;
end architecture;""",
    cite("P6", 1),
)
D.Q(
    "Try it: synchronous clear",
    "How would the code change if reset must clear the T flip-flop only on a rising edge?",
    [
        S(
            "Use a process sensitive to clk. Test rising_edge(clk) first; inside that branch, test reset before toggling."
        )
    ],
    "Make reset a synchronous decision inside the rising-edge branch. Merely removing reset from the sensitivity list does not change asynchronous-reset logic correctly.",
)
D.H("Topic 2: Registers and counters", cite("P6", 1, 2))
D.P(
    "A **register** stores a vector of bits with a shared clock. A parallel load stores all input bits on one edge. A shift register moves stored bits to neighboring positions at each enabled edge; all flip-flops sample their old inputs together."
)
D.X(
    "PS6 Q4: universal four-bit shift register",
    "Let Q3Q2Q1Q0 be the stored word. Define mode 00=hold, 01=shift right, 10=shift left, 11=parallel load P3P2P1P0. Fill shifts with 0.",
    [
        S("Each D input is selected by the same mode bits."),
        S("For D3, the four choices are Q3, 0, Q2, P3."),
        S("For D2, the choices are Q2, Q3, Q1, P2."),
        S("For D1, the choices are Q1, Q2, Q0, P1; for D0: Q0, Q1, 0, P0."),
    ],
    "Use one 4-to-1 mux before each DFF. Bit 3 is leftmost/MSB here, so “right” means movement toward bit 0.",
    cite("P6", 1),
)
D.P(
    "For mode bits $M_1M_0$, define selectors $h=\\overline M_1\\overline M_0$, $r=\\overline M_1M_0$, $l=M_1\\overline M_0$, and $p=M_1M_0$. For example:"
)
D.E(r"D_2=hQ_2+rQ_3+lQ_1+pP_2")
D.X(
    "PS6 Q7–8: synchronous up/down counter",
    "Design a three-bit counter. Direction d=0 counts up; d=1 counts down. All flip-flops share one clock.",
    [
        S("The LSB toggles on every count.", r"T_0=1"),
        S("Bit 1 toggles when Q0=1 going up, or Q0=0 going down.", r"T_1=Q_0\oplus d"),
        S(
            "Bit 2 toggles when both lower bits are 1 going up, or both are 0 going down.",
            r"T_2=(Q_1\oplus d)(Q_0\oplus d)",
        ),
        S("Convert to D inputs by XORing the present bit with its toggle command.", r"D_i=Q_i\oplus T_i"),
    ],
    "T equations implement PS6 Q7; the D equations implement Q8. The direction input must satisfy timing at the sampling edge.",
    cite("P6", 1),
)
D.X(
    "PS6 Q6: divide a clock",
    "How can T flip-flops generate 50 MHz and 25 MHz from a 100 MHz clock?",
    [
        S(
            "A TFF with T=1 toggles on every active edge. Its output needs two input periods to complete one period."
        ),
        S("Use that 50-MHz output to clock another toggling stage to obtain 25 MHz."),
    ],
    "Each stage divides frequency by two. This ripple arrangement has cumulative clock-to-Q delays; a synchronous counter is another design with a different timing structure.",
    cite("P6", 1),
)
q1 = q2 = 0
waves = [[], [], []]
for t in range(40):
    if t >= 6 and (t - 6) % 10 == 0:
        q1 ^= 1
    if t >= 7 and (t - 7) % 20 == 0:
        q2 ^= 1
    for arr, v in zip(waves, [(t // 5) % 2, q1, q2]):
        arr.append(str(v))
D.F(
    {
        "kind": "timing",
        "title": "Ripple frequency division",
        "unit": "1 ns per interval; 1 ns delay per FF",
        "signals": [{"name": n, "wave": "".join(w)} for n, w in zip(["100 MHz", "50 MHz", "25 MHz"], waves)],
    },
    "Positive-edge TFFs, initially zero. Q1 rises 1 ns after the input edge; Q2 rises another 1 ns later. Illustrative delays, not measured device values.",
    cite("P6", 1),
)
D.Q(
    "Try it: trace one edge",
    "A right-shifting four-bit register stores 1011 and uses zero fill. What are its values after the next two active edges?",
    [S("Every flip-flop reads the old neighboring bit at the edge.", r"1011\to0101\to0010")],
    "0101, then 0010. Do not repeatedly overwrite bits within a single clock edge.",
)
D.H("Topic 3: Setup, hold, and maximum clock frequency", cite("P6", 2))
D.P(
    "A flip-flop needs input D stable during a small interval around its active clock edge.\n\n- **Setup time** $t_{setup}$: stable before the edge.\n- **Hold time** $t_{hold}$: stable after the edge.\n- **Clock-to-Q** $t_{cq}$: delay from the edge until its output changes.\n\nViolations can lead to an incorrect capture or metastability; the exact resolved output is not determined by an ideal timing diagram."
)
D.P(
    "For a register → combinational logic → register path with the same clock, zero clock skew, and no added timing uncertainty:"
)
D.E(r"T_{clk}\ge t_{cq,\max}+t_{comb,\max}+t_{setup}")
D.E(r"t_{cq,\min}+t_{comb,\min}\ge t_{hold}")
D.P(
    "Use the **longest** data path for setup and the **shortest** for hold. Clock skew and uncertainty alter these bounds; the equations above explicitly omit them."
)
D.X(
    "Find the clock limit and check hold",
    r"Let $t_{cq,max}=2$ ns, $t_{comb,max}=7.5$ ns, $t_{setup}=1$ ns. The corresponding minimum delays are 0.6 ns and 0.4 ns; hold is 0.8 ns. Assume zero skew.",
    [
        S("Add the maximum delays and setup time.", r"T_{min}=2+7.5+1=10.5\ \mathrm{ns}"),
        S("Invert the minimum period.", r"f_{max}=\tfrac1{10.5\ \mathrm{ns}}\approx95.24\ \mathrm{MHz}"),
        S("Check the minimum path separately.", r"0.6+0.4=1.0\ \mathrm{ns}\ge0.8\ \mathrm{ns}"),
    ],
    "Setup limits the clock to about 95.24 MHz; hold passes with 0.2 ns slack. These illustrative values are not a solution to PS6 Q11’s unsupplied textbook timing data.",
)
D.Q(
    "Try it: does slowing the clock fix hold?",
    "A path has tcq,min=0.2 ns, tcomb,min=0.1 ns, and thold=0.5 ns. Can increasing the clock period fix the violation under the same zero-skew assumptions?",
    [
        S("The earliest new data arrives in 0.3 ns, which is 0.2 ns too early."),
        S("The same-edge hold inequality contains no clock-period term."),
    ],
    "No. The minimum path or clock timing must change; a slower clock alone does not repair this hold violation.",
)
D.save()
