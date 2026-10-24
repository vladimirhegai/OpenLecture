# 09 · Later · Finite-State Machines and Sequential Design

**Later study — outside this midterm study set.** Keep this material for subsequent assessments; prioritize notes 01–03 now.

This note follows Problem Set 7. State-table equations and the sequence detector below are checked exhaustively; the supplied material does not include a separate Section 8 lecture.

## Topic 1: From a state table to flip-flop inputs

A **finite-state machine (FSM)** combines a state register with next-state and output logic.

- **Present state** Q: what the register stores now.
- **Next state** $Q^+$: what it will store on the next active edge.
- **Moore output:** a function of present state.
- **Mealy output:** a function of present state and current input.

Specify reset state and clock edge before tracing a machine.

For D flip-flops, each D input equals the corresponding next-state bit. Write a truth table whose inputs are all present-state bits plus external inputs; simplify each next-state bit as a separate Boolean output.

| Present Q1Q0 | Next if w=0 | Next if w=1 | z |
|---|---|---|---|
| 00 | 10 | 11 | 0 |
| 01 | 01 | 00 | 0 |
| 10 | 11 | 00 | 0 |
| 11 | 10 | 01 | 1 |

**Example: PS7 Q1: derive the D inputs**

Use the state table above. The source calls its bits y2,y1; here Q1 is the MSB and Q0 the LSB. Choose reset 00 for this implementation.

1. D1 is 1 at Q1Q0w=000,001,100,110.

   $$D_1=\overline Q_1\overline Q_0+Q_1\overline w$$
2. D0 is 1 at 001,010,100,111: exactly the odd-parity rows.

   $$D_0=Q_1\oplus Q_0\oplus w$$
3. The Moore output is 1 only in present state 11.

   $$z=Q_1Q_0$$

**Answer:** Connect these two equations to DFFs sharing one rising-edge clock. Reset 00 is an explicit design choice; it is not given by the supplied state table.

**Example: Trace the source machine**

Starting in 00, sample inputs 1,0,1. Give the states and the Moore output after each edge.

1. At 00 with w=1, go to 11; z becomes 1 after the state update.
2. At 11 with w=0, go to 10; z becomes 0.
3. At 10 with w=1, go to 00; z stays 0.

**Answer:** States 00 → 11 → 10 → 00. Outputs after the edges: 1,0,0.

With T flip-flops, use $T_i=Q_i\oplus Q_i^+$. With JK flip-flops, fill the excitation table: 0→1 requires J=1; 1→0 requires K=1. The other input is irrelevant in each case and can be used as a don’t-care during minimization.

**Example: A direct JK implementation**

If a next-state bit is $F_i(Q,w)$, give one correct JK realization without minimizing excitation don’t-cares.

1. Set J to the desired next-state bit and K to its complement.

   $$J_i=F_i,\quad K_i=\overline F_i$$
2. Substitute into the JK characteristic equation.

   $$Q_i^+=F_i\overline Q_i+F_iQ_i=F_i$$

**Answer:** This always reproduces the desired binary next-state function. Minimizing J and K separately can reduce the hardware.

**Problem: Try it: an unusual counting order** (intermediate)

Design D equations for the sequence 0,2,1,3,0 using Q1 as the MSB. Assume reset 00 and count on every rising edge.

<details><summary>Solution</summary>

1. Write the bit sequence: 00→10→01→11→00.
2. The MSB toggles every time; the LSB toggles when the old MSB is 1.

   $$D_1=\overline Q_1,\quad D_0=Q_0\oplus Q_1$$

**Answer:** $D_1=\overline Q_1$, $D_0=Q_0\oplus Q_1$.

</details>

## Topic 2: Sequence detection and overlapping matches

A sequence detector remembers enough of the input history to recognize the target pattern. A useful state meaning is “the longest suffix already seen that is also a prefix of the target.” This prevents losing a possible overlap.

| State | Remembered suffix | w=0 → next/z | w=1 → next/z |
|---|---|---|---|
| A | none | A / 0 | B / 0 |
| B | 1 | C / 0 | B / 0 |
| C | 10 | A / 0 | B / 1 |

```digital
{"kind":"fsm","title":"Overlapping Mealy detector for 101","initial":"A","states":[{"id":"A","x":110,"y":150},{"id":"B","x":350,"y":150},{"id":"C","x":590,"y":150}],"transitions":[{"start":"A","end":"A","label":"0 / 0"},{"start":"A","end":"B","label":"1 / 0"},{"start":"B","end":"B","label":"1 / 0"},{"start":"B","end":"C","label":"0 / 0","bend":-65},{"start":"C","end":"B","label":"1 / 1","bend":-65},{"start":"C","end":"A","label":"0 / 0","bend":-150}]}
```

*Labels are input/output. Reset to A. Interpret the transition and its output using the input stable before the next rising edge.*

**Example: Why detection returns to B**

When state C has remembered 10 and the next input is 1, why go to B instead of A?

1. The new input completes 101, so output 1.
2. That last 1 is also the first bit of another possible 101.
3. State B preserves that suffix so 10101 produces two matches.

**Answer:** For input 10101, the Mealy outputs for the sampled transitions are 00101. A reset to A after each match would miss the overlap.

**Example: Turn the same detector into a Moore machine**

Where must the output go if z may depend only on state?

1. Add a detected state D with z=1. States A,B,C keep z=0.
2. Use C --1→ D. From D, input 0 leaves suffix 10, so go to C; input 1 leaves suffix 1, so go to B.
3. The other transitions are A: 0→A,1→B; B: 0→C,1→B; C: 0→A.

**Answer:** Moore uses four states here. Its detection output becomes high after the edge that enters D; compare timing conventions explicitly when matching a sample waveform.

A Mealy output may react when an input changes between clock edges; a Moore output changes with state, apart from propagation effects. If the output is registered, state clearly which edge captures it. “Mealy is one cycle earlier” is not a complete timing specification by itself.

```vhdl
library ieee;
use ieee.std_logic_1164.all;
entity detect101 is
  port (clk, reset, w : in std_logic; z : out std_logic);
end entity;
architecture rtl of detect101 is
  type state_t is (a, b, c);
  signal present, next_state : state_t;
begin
  process(present, w)
  begin
    next_state <= present;
    z <= '0';
    case present is
      when a =>
        if w='1' then next_state <= b; end if;
      when b =>
        if w='0' then next_state <= c; end if;
      when c =>
        if w='1' then next_state <= b; z <= '1';
        else next_state <= a;
        end if;
    end case;
  end process;
  process(clk, reset)
  begin
    if reset='1' then present <= a;
    elsif rising_edge(clk) then present <= next_state;
    end if;
  end process;
end architecture;
```

The combinational process gives defaults before the case branches so every output is assigned on every binary path. The clocked process stores the state. This teaching example’s state transitions are checked in Python; VHDL compilation and synthesis have not been run.

**Problem: Try it: repeated 1s** (intermediate)

A detector must recognize 111 with overlaps. After seeing the third 1, what history should be retained?

<details><summary>Solution</summary>

1. The suffix 11 is already the first two bits of another 111.

**Answer:** Retain “11,” so each subsequent 1 produces another detection. Clearing all history would miss overlaps.

</details>

## Topic 3: Encoding and state minimization

**Binary encoding** uses at least $\lceil\log_2N\rceil$ flip-flops for N states. **One-hot encoding** uses one flip-flop per state, with exactly one asserted. More storage can simplify next-state decoding; neither encoding is universally smaller or faster.

**Example: PS7 Q3: one-hot equations for the source table**

Rename binary states 00,01,10,11 as A,B,C,D. Give one-hot next-state equations, where A,B,C,D now denote individual state bits.

1. An incoming transition from B or C on w=1 reaches A.

   $$A^+=w(B+C)$$
2. B is reached from B on 0 or D on 1.

   $$B^+=\overline wB+wD$$
3. C is reached from A or D on 0.

   $$C^+=\overline w(A+D)$$
4. D is reached from A on 1 or C on 0.

   $$D^+=wA+\overline wC$$

**Answer:** Use four DFFs, z=D, and reset to A=1 with the other bits 0. These equations are derived only for valid one-hot states.

Unused encodings require a deliberate policy. They can be don’t-cares only under a justified reachability assumption. If recovery is required, define the transition from invalid states rather than assuming the circuit will recover.

For a fully specified **Moore** FSM, minimize states by repeated partition refinement.

1. Remove states unreachable from reset.
2. Partition the remaining states by output value.
3. Split a partition when its states transition into different partitions for some input.
4. Repeat until stable; merge states left in the same partition.

For Mealy machines, compare each input’s output as well as the destination partition.

| State / output | w=0 | w=1 |
|---|---|---|
| A / 0 | A | B |
| B / 0 | C | D |
| C / 0 | C | D |
| D / 1 | A | D |

**Example: Minimize by future behavior**

Minimize the original Moore machine in the table immediately above, with reset A.

1. Start with output partitions {A,B,C} and {D}.
2. A goes to the 0-output partition on both inputs. B and C go to {D} on input 1, so A must split from them.
3. B and C have matching transitions into the final partitions: {B,C} on 0 and {D} on 1.

**Answer:** Merge B and C. The minimized machine has three states: A, BC, D. Equal present outputs alone would not justify merging A with them.

**Problem: Try it: output equality is insufficient** (intermediate)

Two states both output z=0. On input 1, one goes to a state with z=1 and the other stays in a state with z=0. Can they be equivalent Moore states?

<details><summary>Solution</summary>

1. Apply input 1 and compare the resulting output. A future input distinguishes their behaviors.

**Answer:** No. Equivalent states must produce the same future output behavior for every input sequence.

</details>
