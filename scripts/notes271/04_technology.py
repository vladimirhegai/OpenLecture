"""Section 3 and PS2: voltage levels, MOS switches, CMOS, programmable logic."""

from itertools import product

from lib import Doc, S, cite

for a, b, c in product((0, 1), repeat=3):
    assert (not (a and (b or c))) == ((not a) or ((not b) and (not c)))
    assert (not (a and b)) == ((not a) or (not b))
assert 2.4 - 2.0 > 0 and abs((0.8 - 0.4) - 0.4) < 1e-12

D = Doc(
    4,
    "Voltage Levels, CMOS, and Implementation Technology",
    ["implementation_technology", "cmos", "programmable_logic"],
)
D.H("Topic 1: Logic levels and transistor switches", cite("C", 4, 5, 6, 9))
D.P(
    "In **positive logic**, low voltage represents 0 and high voltage represents 1. A range between the valid low and high input levels is undefined; it is not a third valid binary value.",
    cite("C", 4),
)
D.T(
    ["Quantity", "Meaning"],
    [
        [r"$V_{OL(\max)}$", "Largest guaranteed low output voltage"],
        [r"$V_{OH(\min)}$", "Smallest guaranteed high output voltage"],
        [r"$V_{IL(\max)}$", "Largest voltage guaranteed to be accepted as a low input"],
        [r"$V_{IH(\min)}$", "Smallest voltage guaranteed to be accepted as a high input"],
    ],
    cite("C", 5),
)
D.E(r"NM_L=V_{IL(\max)}-V_{OL(\max)}", cite("C", 5))
D.E(r"NM_H=V_{OH(\min)}-V_{IH(\min)}", cite("C", 5))
D.X(
    "Noise margin",
    r"A driver guarantees $V_{OL}\le0.4$ V and $V_{OH}\ge2.4$ V. The receiver accepts low through 0.8 V and high from 2.0 V. Find both margins.",
    [
        S(
            "Low-level noise may raise the low output toward the receiver threshold.",
            r"NM_L=0.8-0.4=0.4\ \mathrm V",
        ),
        S("High-level noise may lower the high output toward its threshold.", r"NM_H=2.4-2.0=0.4\ \mathrm V"),
    ],
    "Both margins are 0.4 V. A voltage in the undefined input band has no guaranteed binary interpretation.",
)
D.P(
    "Use the ideal switch model for the course transistor networks.\n\n- **NMOS:** conducts when its gate input is high; typically used to pull the output down to ground.\n- **PMOS:** conducts when its gate input is low; typically used to pull the output up to $V_{DD}$.\n\nThese rules describe the rail-driven logic switches here; they are not a general analog MOSFET model.",
    cite("C", 6, 8, 9, 10),
)
D.P(
    "In resistor-load NMOS logic, an open pull-down network lets the resistor pull the output high. When the NMOS network conducts, the output goes low and the resistor can carry steady current.",
    cite("C", 11, 12, 15),
)
D.Q(
    "Try it: identify a pull-down function",
    "Two NMOS switches controlled by A and B are in parallel below a resistor pull-up. Is the output AND, OR, NAND, or NOR?",
    [
        S("Either high input completes a path to ground.", r"\text{PDN conducts}=A+B"),
        S("The output is low when that path conducts.", r"F=\overline{A+B}"),
    ],
    "NOR.",
)
D.H("Topic 2: Complementary CMOS networks", cite("C", 16, 17, 18, 19, 21, 24))
D.P(
    "Static complementary CMOS replaces the resistor with a **PMOS pull-up network (PUN)**. It pairs that with an **NMOS pull-down network (PDN)**.\n\n- Derive when the output must be 0: that is the PDN conduction condition $\\overline F$.\n- AND in a conduction condition means switches in series. OR means parallel branches.\n- Build the PUN by swapping series and parallel and replacing NMOS with PMOS, keeping the same gate signals.",
    cite("C", 16, 17, 24),
)
D.F(
    {"kind": "cmos", "title": "CMOS inverter", "pdn": {"gate": "A"}},
    "A=0 turns the PMOS on and NMOS off; A=1 does the reverse.",
    cite("C", 18),
)
D.P(
    "For a valid steady binary input, the ideal complementary network provides one path to a supply rail while the other network is off. Real CMOS still has leakage and dissipates energy during switching; “zero static power” is an ideal approximation.",
    cite("C", 18),
)
D.X(
    "NAND: trace both networks",
    r"Design static CMOS for $F=\overline{AB}$.",
    [
        S("The PDN must conduct only when both inputs are high.", r"\overline F=AB"),
        S("Put NMOS A and B in series. The dual PUN has PMOS A and B in parallel."),
        S("At A=B=1 the PDN is on. Otherwise at least one PMOS provides a pull-up path."),
    ],
    "Two NMOS + two PMOS = four transistors.",
    cite("C", 19, 20),
)
D.F(
    {"kind": "cmos", "title": "CMOS NAND", "pdn": {"series": [{"gate": "A"}, {"gate": "B"}]}},
    "PMOS gate bubbles indicate conduction for a low gate input.",
    cite("C", 19),
)
D.X(
    "NOR and transistor counting",
    r"How does a 2-input NOR differ from a 2-input NAND? How many transistors implement a 2-input AND in basic static CMOS?",
    [
        S("NOR needs parallel NMOS and series PMOS.", r"F=\overline{A+B}"),
        S("AND is a NAND followed by an inverter.", r"N_{\mathrm{AND}}=4+2=6"),
    ],
    "NOR uses four transistors with the opposite series/parallel arrangement. Basic AND uses six.",
    cite("C", 21, 22, 23),
)
D.X(
    "Lecture complex gate: derive the conducting paths",
    r"Implement $F=\overline A+\overline B\,\overline C$.",
    [
        S("Complement the function to obtain the PDN condition.", r"\overline F=A(B+C)"),
        S("Use NMOS A in series with parallel NMOS B and C."),
        S("The dual PUN is PMOS A in parallel with series PMOS B and C."),
    ],
    "Three NMOS + three PMOS = six transistors. The output is high when A=0, or when B=C=0.",
    cite("C", 24),
)
D.F(
    {
        "kind": "cmos",
        "title": "Complex complementary CMOS gate",
        "pdn": {"series": [{"gate": "A"}, {"parallel": [{"gate": "B"}, {"gate": "C"}]}]},
    },
    "Always distinguish the function at f from the condition that makes the PDN conduct.",
    cite("C", 24),
)
D.Q(
    "Try it: preserve the outer inversion",
    r"Build the PDN and count transistors for $F=\overline{AB+C}$.",
    [
        S("The PDN condition is AB+C: a series A–B branch in parallel with C."),
        S("The PUN is parallel PMOS A/B in series with PMOS C. Each network has three transistors."),
    ],
    "Six transistors total. This one complex gate gives the inverted function; an extra inverter would produce AB+C.",
)
D.H("Topic 3: Chip choices, LUTs, and physical limits", cite("N", 19, 21, 23, 24))
D.P(
    "The supplied implementation lecture develops transistor networks; its outline also names the chip families and delay topics below. PS2 supplies the PLA/LUT design tasks. The following descriptions connect those topics, without assuming an additional supplied lecture.",
    cite("C", 2),
)
D.T(
    ["Implementation", "How the function is chosen"],
    [
        ["Standard fixed-function IC", "Select an existing function and connect chips"],
        ["PLA", "Program product terms in an AND plane and select them in an OR plane"],
        [
            "PAL / CPLD",
            "PAL: programmable AND terms with a fixed OR structure; CPLD: interconnected programmable blocks",
        ],
        ["FPGA", "Configure logic blocks (often LUTs), routing, and storage"],
        [
            "ASIC / standard cells / gate array",
            "Implement a custom circuit with the chosen fabrication/design approach",
        ],
    ],
    cite("N", 19),
)
D.X(
    "A LUT stores a truth table",
    "What four stored bits implement XOR in a 2-input LUT addressed by AB=00,01,10,11?",
    [S("Evaluate XOR at each address.", r"0,1,1,0")],
    "Store 0,1,1,0 in address order. A k-input LUT needs $2^k$ truth-table entries.",
    cite("P2", 2),
)
D.X(
    "PLA product terms can be shared",
    r"For $F=AB+C$ and $G=AB+D$, give the product terms and output connections.",
    [
        S("Create product lines P1=AB, P2=C, P3=D."),
        S("Select product lines for each OR output.", r"F=P_1+P_2,\quad G=P_1+P_3"),
    ],
    "The AB term is generated once and used twice. This illustrates the programmable AND–OR structure.",
    cite("P2", 2),
)
D.P(
    "**Propagation delay** is the time between an input transition and the resulting output transition. **Fan-in** counts a gate’s inputs; **fan-out** describes the load it drives. More loading can increase delay, so fewer gates need not mean the fastest circuit.",
    cite("C", 2),
)
D.P(
    "A buffer reproduces its input and can provide drive. A **tri-state buffer** drives 0 or 1 when enabled and disconnects its output when disabled; that disconnected state is **Z**, not logic 0. A shared bus needs controls that prevent conflicting drivers.",
    cite("C", 2),
)
D.Q(
    "Try it: tri-state bus control",
    "Driver A drives 1 and driver B drives 0 onto the same bus. Is the bus value an OR of their outputs?",
    [
        S(
            "Both outputs actively try to impose different voltages. Boolean OR does not model this connection."
        ),
        S("Disable one driver to Z before allowing the other to drive."),
    ],
    "No; the bus has contention. With both drivers disabled, the bus is undriven unless another circuit establishes its level.",
)
D.save()
