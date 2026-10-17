# The Height Method: Complete Guide

## The idea

Give every node a **height**: its voltage above one node you choose as ground (0 V). Then a circuit becomes a landscape. Sources lift charge up, resistors let it slide back down, and every question about voltage, current or power becomes a question about the picture: how high is this node, how far does the charge fall through that element, which way is it going. Every circuit in these notes has a **Height view** button that draws it this way, and most worked problems have a **Walk me through it** solution that builds the picture one step at a time.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$"
wire 3,3 -> 6,3
R3 6,3 -> 6,0 "$4\,\Omega$"
wire 6,0 -> 0,0
label 3,3 "$m$" above
ground 0,0
#@ node t 12 "top: $12\,\mathrm{V}$"
#@ node m 4 "$m$: $4\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V t g "$12\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=t id=es
#@ el R t m "$4\,\Omega$: falls $8\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=m id=e1
#@ el R m g2 "$4\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=g2 id=e2
#@ el R m g3 "$4\,\Omega$: falls $4\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=g3 id=e3
#@ step "Ground the bottom wire. The source is a fixed step: its + end is $12\,\mathrm{V}$ up."
#@ step "Seen from the top, the circuit is $4\,\Omega$ followed by two $4\,\Omega$ side by side ($2\,\Omega$): $6\,\Omega$ in all, so the source lifts $\dfrac{12}{6}=2\,\mathrm{A}$." show=es
#@ step "The first $4\,\Omega$ falls $(2)(4)=8\,\mathrm{V}$, so $m$ sits at $4\,\mathrm{V}$." show=e1,m
#@ step "At $m$ the river splits. Both branches fall the same $4\,\mathrm{V}$ to ground, so each carries $\dfrac{4}{4}=1\,\mathrm{A}$." show=e2,e3
#@ step "Power = current × height change: the source lifts $2\,\mathrm{A}$ through $12\,\mathrm{V}$ ($24\,\mathrm{W}$); the falls absorb $16+4+4=24\,\mathrm{W}$."
#@ note "Straight line view: the $12\,\mathrm{V}$ supply rail on top, one stream falling to $m$, then splitting into two streams that each reach ground."
```

> **Tip:** **Reading any height view.** Orange arrows ▼: current falls through the element, so it **absorbs** energy. Green arrows ▲: current climbs, so the element **delivers**. Black $+/-$: the element's actual polarity ($+$ on the higher end). Blue $+/-$ with a name: the problem's own reference for that voltage; when the blue $+$ sits on the lower end, that voltage is negative. A dashed level: a node whose height nothing fixes. **Straight line** draws a grounded supply as a rail on top; **Full loop** draws every source.

## The rules, element by element

| Element | In the picture | What it fixes, and what it leaves free |
|---|---|---|
| Wire, closed switch, ideal ammeter | Flat: both ends at one height | No step; any current. |
| Resistor | A slope | Current always runs **downhill**; the fall is $iR$ and it always absorbs $i\times$fall. |
| Voltage source | A rigid step: the $+$ end is higher by $v_s$ | Fixes the step; any current, either way. |
| Current source | A stretchy step | Fixes the current; its step is whatever the rest of the circuit needs, even negative (then it absorbs). |
| Dependent voltage source | A rigid step whose size is read from its controller | Find the controller on the picture first, then treat it as a step. |
| Dependent current source | A stretchy step whose current is read from its controller | Same as a current source once the controller is known. |
| Open switch, ideal voltmeter | A gap | No current; it spans whatever step is left over. |
| Capacitor (Week 6) | A **held step** $v_C$ | $v_C$ cannot jump; it moves at $\dfrac{dv_C}{dt}=\dfrac{i}{C}$. In DC steady state it is a gap (no current). |
| Inductor (Week 6) | A **held current** $i_L$ | $i_L$ cannot jump; its step $L\dfrac{di}{dt}$ is whatever the circuit forces. In DC steady state it is flat (a wire). |
| Ground | The 0 level | Any node may be chosen; moving ground shifts every height equally and changes no answer. |

### The laws as pictures

- **KVL:** every node has exactly one height, so any loop walk comes back to the height it started from. If some node would need two heights, the connection is invalid.
- **KCL:** the current arriving at a level equals the current leaving it; charge never piles up.
- **Power:** current × height change. Climbs deliver, falls absorb, and the total of the climbs equals the total of the falls.
- **Downhill is a resistor rule only.** Sources, capacitors and inductors can carry current uphill; that is exactly when they deliver energy.

### The recipe

Every walkthrough in every week follows these six steps, in this order:

1. **Pick ground**: usually the $-$ end of the main source, or the node most elements touch. It is the 0 V level.
2. **Place the fixed heights**: step across every voltage source from a known height (its $+$ end is higher by its value).
3. **Find currents**: a current source fixes its own current (never its step); a resistor carries fall ÷ $R$, always downhill; use KCL where branches meet.
4. **Place the rest**: walk down each resistor by $iR$ in the current's direction.
5. **If heights depend on each other** (two or more unknown nodes, Week 2 onward): name the unknown heights, write KCL at each, solve, then place them. The picture checks the algebra; it does not replace it.
6. **Answer and check**: voltages are height differences. Every node must have one height (KVL; if it can't, the connection is invalid), the currents must balance at every node (KCL), and the climbs must equal the falls (power: climbing delivers, falling absorbs).

## Reading answers off the picture

| The question asks for… | On the height picture | Week |
|---|---|---|
| A voltage $v$ marked $+$ at $a$, $-$ at $b$ | height($a$) − height($b$); negative when the $+$ end is lower | 1 |
| Absorbing or delivering? | Current falls through it: absorbs. Climbs: delivers. | 1 |
| Power of an element; total power developed | current × height change; add the climbs (they equal the falls) | 1 |
| Is the connection valid? Is the answer unique? | One height per node and balanced currents? A node joined only through current sources floats. | 1 |
| Electrons | Against the current; a charge $-e$ gains energy going down in voltage | 1 |
| Series or parallel? | Stacked in one column (one current) or side by side between the same two levels (one fall) | 2 |
| A divider's output | Where the midpoint sits on the slope; a load is a second path down that makes it sag | 2 |
| Bridge balance; a meter's effect | Balanced: the two midpoints level, the detector flat. Real voltmeter: drags the probed node down; real ammeter: steals a small step | 2 |
| A node voltage | It is the height. A node joined only by resistors sits at the conductance-weighted average of its neighbours | 3 |
| $V_{\mathrm{Th}}$, $R_{\mathrm{Th}}$, $I_N$ | Open terminal height; sag per amp drawn; current when the terminal is pulled down to $b$ | 4 |
| Maximum power to a load | The load sits at half the open-circuit height $V_{\mathrm{Th}}/2$ | 5 |
| Superposition | Draw each source alone and add heights node by node (never powers) | 5 |
| Capacitor or inductor at $0^+$ and $\infty$ | $0^+$: $C$ holds its step, $L$ holds its current. $\infty$: $C$ is a gap, $L$ is flat. Between them every height slides exponentially with one $\tau$ | 6 |

## Week 2: series, parallel, dividers, bridges

- **Series** elements stack in one column and share one current; their falls add up to the column's total. **Parallel** elements span the same two levels side by side; they share one fall and split the current.
- An **equivalent resistance** keeps the top and bottom heights and the total current but erases the levels in between. Restore them afterwards to answer branch questions.
- **Voltage divider:** one slope from $v_s$ to 0. Each resistor's share of the fall is proportional to its resistance, so the midpoint sits $\dfrac{R_2}{R_1+R_2}$ of the way up.
- **Current divider:** paths that fall the same height. The gentler slope (smaller $R$, larger $G$) carries more current: $i_k\propto G_k$.
- **A load** hung from a divider's midpoint is a second way down, so the midpoint **sags**. A real voltmeter is such a load; a real ammeter is a small extra slope in the path it measures.
- **Wheatstone bridge:** two dividers hanging from one rail. Balanced means their midpoints are level, so the detector between them lies flat and carries nothing.
- **Δ–Y:** the swap keeps the heights of the three terminals and the currents into them. Only the inside changes (a new center level). Solve the easy circuit, copy the terminal heights back, and read each original resistor as fall ÷ $R$.

```schematic
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
R1 0,3 -> 3,3 "$10\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$20\,\mathrm{k\Omega}$" v="$v_o$" flip
wire 3,3 -> 6,3
wire 3,0 -> 6,0
wire 0,0 -> 3,0
terminal 6,3 "a" right
terminal 6,0 "b" right
ground 0,0
#@ view "No load"
#@ node t 30 "top: $30\,\mathrm{V}$"
#@ node m 20 "midpoint: $20\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ el V t g "$30\,\mathrm{V}$" col=0 i="$1\,\mathrm{mA}$" to=t
#@ el R t m "$10\,\mathrm{k\Omega}$: falls $10\,\mathrm{V}$" col=1 i="$1\,\mathrm{mA}$" to=m
#@ el R m g2 "$20\,\mathrm{k\Omega}$: falls $20\,\mathrm{V}$" col=1 i="$1\,\mathrm{mA}$" to=g2 plus=m v="$v_o$"
#@ note "One current, so the fall is shared in proportion to resistance: the midpoint sits $\dfrac{20}{30}$ of the way up."
#@ view "With a 20 kΩ load"
#@ node t 30 "top: $30\,\mathrm{V}$"
#@ node m 15 "midpoint: $15\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V t g "$30\,\mathrm{V}$" col=0 i="$1.5\,\mathrm{mA}$" to=t id=es
#@ el R t m "$10\,\mathrm{k\Omega}$: falls $15\,\mathrm{V}$" col=1 i="$1.5\,\mathrm{mA}$" to=m id=e1
#@ el R m g2 "$20\,\mathrm{k\Omega}$: falls $15\,\mathrm{V}$" col=1 i="$0.75\,\mathrm{mA}$" to=g2 id=e2 plus=m v="$v_o$"
#@ el R m g3 "load $20\,\mathrm{k\Omega}$: falls $15\,\mathrm{V}$" col=2 i="$0.75\,\mathrm{mA}$" to=g3 id=eL
#@ step "The load is a second path from the midpoint down to ground: below the midpoint there are now $20\parallel20=10\,\mathrm{k\Omega}$."
#@ step "Divide again: the midpoint sits $\dfrac{10}{20}$ of the way up, at $15\,\mathrm{V}$. It sagged by $5\,\mathrm{V}$." show=m
#@ step "More current now flows ($\dfrac{30}{20\,\mathrm{k\Omega}}=1.5\,\mathrm{mA}$), so the top resistor's fall grows to $15\,\mathrm{V}$; below the midpoint the current splits $0.75+0.75\,\mathrm{mA}$." show=es,e1,e2,eL
```

## Week 3: node voltages are heights

- The **node-voltage method** is the height method written as algebra: the unknowns are the heights of the essential nodes.
- **Averaging rule:** a node joined only by resistors sits at the conductance-weighted average of its neighbours' heights, plus a lift for any current injected into it:
- So with only voltage sources and resistors, no node can rise above the highest source terminal. **Current sources and dependent sources can** push a node above every voltage source.
- **Supernode:** a voltage source between two unknown nodes is a **rigid rod**: it locks their heights a fixed distance apart, and the rod as a whole floats until KCL around it (net current in = 0) pins it.
- **Mesh currents** have no height picture; a mesh equation is just a loop walk (rises = falls). In the height view only the real branch currents appear: a shared branch carries the difference of its two mesh currents. A current source is a stretchy step, which is why a supermesh walk skips it.
- **Dependent sources often absorb** in these circuits: current falls through them. Read it off the arrow colour.

$$v_k=\frac{\sum_j G_j\,v_j+I_{\text{in}}}{\sum_j G_j}$$

```schematic
I1 0,0 -> 0,3 "$4\,\mathrm{A}$"
wire 0,3 -> 2,3
R1 2,3 -> 2,0 "$5\,\Omega$"
V1 5,3 -> 2,3 "$10\,\mathrm{V}$"
R2 5,3 -> 5,0 "$5\,\Omega$" flip
wire 5,0 -> 0,0
label 2,3 "$a$" above
label 5,3 "$b$" above
ground 0,0
#@ node b 15 "$b$: $15\,\mathrm{V}$"
#@ node a 5 "$a$: $5\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el I g a "$4\,\mathrm{A}$" col=0 i="$4\,\mathrm{A}$" to=a id=es
#@ el R a g2 "$5\,\Omega$: falls $5\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=g2 id=e1
#@ el V b a "$10\,\mathrm{V}$" col=2 i="$3\,\mathrm{A}$" to=b id=ev
#@ el R b g3 "$5\,\Omega$: falls $15\,\mathrm{V}$" col=3 i="$3\,\mathrm{A}$" to=g3 id=e2
#@ step "Ground the bottom wire. Two unknown heights, $a$ and $b$, but the $10\,\mathrm{V}$ source is a rigid rod between them: $b=a+10$. One unknown is left."
#@ step "KCL around the whole rod: the $4\,\mathrm{A}$ that comes in must leave down the two resistors, $4=\dfrac{a}{5}+\dfrac{a+10}{5}$, so $a=5\,\mathrm{V}$ and $b=15\,\mathrm{V}$." show=a,b
#@ step "Each resistor's current is its fall over $5\,\Omega$: $1\,\mathrm{A}$ and $3\,\mathrm{A}$. So $3\,\mathrm{A}$ climbs through the source from $a$ to $b$." show=e1,e2,ev,es
#@ step "Power: the current source lifts $4\,\mathrm{A}$ through $5\,\mathrm{V}$ ($20\,\mathrm{W}$) and the voltage source lifts $3\,\mathrm{A}$ through $10\,\mathrm{V}$ ($30\,\mathrm{W}$); the resistors absorb $5+45=50\,\mathrm{W}$."
```

## Week 4: source transformations and Thévenin

- Two circuits are **equivalent at a–b** when the terminal height is the same for every load current. A source transformation and a Thévenin or Norton equivalent are such swaps: they keep the **terminal** heights, not the inside ones, so never read an original resistor's power from the equivalent.
- **Thévenin picture:** one rigid step $V_{\mathrm{Th}}$, then one slope $R_{\mathrm{Th}}$ down to terminal $a$. Draw nothing and $a$ sits at $V_{\mathrm{Th}}$ (open circuit). Draw current $i$ and $a$ **sags** by $R_{\mathrm{Th}}i$: $v_{ab}=V_{\mathrm{Th}}-R_{\mathrm{Th}}i$. A short pulls $a$ down to $b$, and the current that flows is $I_N=\dfrac{V_{\mathrm{Th}}}{R_{\mathrm{Th}}}$.
- Ground $b$ for Thévenin pictures, so the terminal's height is $v_{ab}$ directly. $b$ need not be the lowest node.
- **Turning sources off** (for $R_{\mathrm{Th}}$): a voltage source's step flattens to a wire; a current source's lift is cut (a gap). Dependent sources are never turned off.
- **Test source:** push current $i_T$ into $a$ and see how high $a$ climbs: $R_{\mathrm{Th}}=\dfrac{v_T}{i_T}$. With only dependent sources inside, every height is proportional to the test value, so any convenient value works.
- A resistor across a voltage source spans a fixed step and changes no other height (drop it to find heights, but it still absorbs power). A resistor in series with a current source changes only the height of the node between them.

```schematic
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
R1 0,3 -> 3,3 "$12\,\Omega$"
R2 3,3 -> 3,0 "$12\,\Omega$" flip
wire 3,3 -> 6,3
wire 3,0 -> 6,0
wire 0,0 -> 3,0
terminal 6,3 "a" right
terminal 6,0 "b" right
ground 0,0
#@ view "Open: nothing attached"
#@ node t 24 "top: $24\,\mathrm{V}$"
#@ node a 12 "$a$: $12\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V t g "$24\,\mathrm{V}$" col=0 i="$1\,\mathrm{A}$" to=t
#@ el R t a "$12\,\Omega$: falls $12\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=a
#@ el R a g2 "$12\,\Omega$: falls $12\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=g2
#@ note "Open circuit: the terminal sits at $V_{\mathrm{Th}}=12\,\mathrm{V}$. Seen from a–b with the source flattened, the two $12\,\Omega$ are side by side: $R_{\mathrm{Th}}=6\,\Omega$."
#@ view "Matched load: 6 Ω"
#@ node t 24 "top: $24\,\mathrm{V}$"
#@ node a 6 "$a$: $6\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V t g "$24\,\mathrm{V}$" col=0 i="$1.5\,\mathrm{A}$" to=t
#@ el R t a "$12\,\Omega$: falls $18\,\mathrm{V}$" col=1 i="$1.5\,\mathrm{A}$" to=a
#@ el R a g2 "$12\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$0.5\,\mathrm{A}$" to=g2
#@ el R a g3 "load $6\,\Omega$: falls $6\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=g3
#@ note "The load draws $1\,\mathrm{A}$, so $a$ sags by $R_{\mathrm{Th}}i=6\,\mathrm{V}$, from $12$ to $6\,\mathrm{V}$: exactly half the open height. That is the maximum-power load (Week 5): $(6\,\mathrm{V})(1\,\mathrm{A})=6\,\mathrm{W}=\dfrac{V_{\mathrm{Th}}^2}{4R_{\mathrm{Th}}}$."
#@ view "Short: a pulled to b"
#@ node t 24 "top: $24\,\mathrm{V}$"
#@ node g 0 "$a=b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$a=b$: $0\,\mathrm{V}$" ground
#@ el V t g "$24\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=t
#@ el R t g2 "$12\,\Omega$: falls $24\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2
#@ note "With $a$ shorted to $b$, the lower $12\,\Omega$ has no fall and carries nothing; the whole $24\,\mathrm{V}$ falls across the top $12\,\Omega$, and its $2\,\mathrm{A}$ all goes through the short: $I_N=2\,\mathrm{A}=\dfrac{V_{\mathrm{Th}}}{R_{\mathrm{Th}}}$."
```

## Week 5: maximum power and superposition

- **Maximum power:** a load drawing current from a Thévenin source sits at height $h$, and receives $p=h\cdot\dfrac{V_{\mathrm{Th}}-h}{R_{\mathrm{Th}}}$. Two numbers with a fixed sum ($h$ and $V_{\mathrm{Th}}-h$) have the largest product when they are equal, so the best load sits at **half the open-circuit height**, $h=\dfrac{V_{\mathrm{Th}}}{2}$, which happens when $R_L=R_{\mathrm{Th}}$. No calculus needed.
- Half of $V_{\mathrm{Th}}$, not half of the supply: the Thévenin step is often smaller than the real rail. Efficiency compares the load's fall × current with the real sources' climbs.
- If the load is fixed and you choose a series resistor instead, the series resistor can only steal height, so the best choice is zero.
- **Superposition:** draw the picture once per independent source (the others turned off), then **add the heights node by node** and the currents element by element. Dependent sources stay on in every picture.
- **Power does not add.** It is current × fall, a product: the partial pictures' powers have cross terms. Find the summed currents and heights first, then compute power once.
- In a partial picture a resistor may carry current the 'wrong' way relative to the final answer; only the summed picture has to obey the downhill rule for the real current.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$" flip
wire 3,3 -> 6,3
I1 6,0 -> 6,3 "$3\,\mathrm{A}$" flip
wire 6,0 -> 0,0
label 3,3 "$m$" above
ground 0,0
#@ view "12 V alone"
#@ node t 12 "top: $12\,\mathrm{V}$"
#@ node m 6 "$m$: $6\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V t g "$12\,\mathrm{V}$" col=0 i="$1.5\,\mathrm{A}$" to=t
#@ el R t m "$4\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$1.5\,\mathrm{A}$" to=m
#@ el R m g2 "$4\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$1.5\,\mathrm{A}$" to=g2
#@ el S m g3 "$3\,\mathrm{A}$ source off: a gap" col=2
#@ note "Current source off (a gap): a plain divider, so $m=6\,\mathrm{V}$. The left resistor carries $1.5\,\mathrm{A}$ to the right."
#@ view "3 A alone"
#@ node m 6 "$m$: $6\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el R m g "left $4\,\Omega$ (12 V source off: a wire)" col=0 i="$1.5\,\mathrm{A}$" to=g
#@ el R m g2 "$4\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$1.5\,\mathrm{A}$" to=g2
#@ el I g3 m "$3\,\mathrm{A}$" col=2 i="$3\,\mathrm{A}$" to=m
#@ straight off
#@ note "Voltage source off (flattened to a wire): both resistors now hang from $m$ to ground, $2\,\Omega$ in all, so $m=(3)(2)=6\,\mathrm{V}$. The left resistor now carries $1.5\,\mathrm{A}$ to the **left**."
#@ view "Both: add the heights"
#@ node t 12 "top: $12\,\mathrm{V}$"
#@ node m 12 "$m$: $6+6=12\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V t g "$12\,\mathrm{V}$" col=0
#@ el R t m "$4\,\Omega$: flat, no current" col=0
#@ el R m g2 "$4\,\Omega$: falls $12\,\mathrm{V}$" col=1 i="$3\,\mathrm{A}$" to=g2
#@ el I g3 m "$3\,\mathrm{A}$" col=2 i="$3\,\mathrm{A}$" to=m
#@ note "Heights add: $m=6+6=12\,\mathrm{V}$. Currents add: the left resistor's $1.5\,\mathrm{A}$ right plus $1.5\,\mathrm{A}$ left is $0$, so it lies flat. Powers do **not** add: it absorbed $9\,\mathrm{W}$ in each partial picture but $0\,\mathrm{W}$ in reality."
```

## Week 6: capacitors, inductors and switching

- **Snapshot rule:** at any single instant, a capacitor is a voltage step equal to its present $v_C$ and an inductor is a current source equal to its present $i_L$. With those two substitutions every snapshot is an ordinary Week 1 picture.
- **Three snapshots** answer most switching questions. $0^-$: the old circuit in DC steady state ($C$ a gap, $L$ a wire). $0^+$: the new circuit with each $C$ holding its $v_C(0^-)$ and each $L$ holding its $i_L(0^-)$. **Only those carry over**; every other height and current may jump. $\infty$: the new circuit in DC steady state.
- **The slide:** after $0^+$ (with DC sources), every height and every current moves exponentially from its $0^+$ value to its $\infty$ value, all with the same time constant: $h(t)=h(\infty)+[h(0^+)-h(\infty)]e^{-t/\tau}$.
- **Finding $\tau$ from the picture:** distance the held quantity must travel ÷ its starting speed. A capacitor's speed is $\dfrac{i_C}{C}$, an inductor's is $\dfrac{v_L}{L}$, both read off the $0^+$ picture. (It agrees with $RC$ and $\dfrac{L}{R}$.)
- **Uphill is normal here:** current climbing through a $C$ or $L$ means it is giving stored energy back; falling through it means storing. 'Downhill' is a resistor-only rule.
- **Energy:** a capacitor is like a water tank of area $C$ filled to level $v$: $w=\dfrac12Cv^2$ (the charge was lifted gradually, so on average only halfway). It depends on the step across $C$, not on how high the capacitor sits. An inductor's $\dfrac12Li^2$ is energy of moving current (momentum), with no height picture.

```schematic
V1 0,3 -> 0,0 "$10\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$2\,\mathrm{k\Omega}$"
C1 6,3 -> 6,0 "$1\,\mu\mathrm{F}$" v="$v_C$" flip
wire 6,0 -> 0,0
ground 0,0
#@ view "t = 0+"
#@ node t 10 "source +, resistor top: $10\,\mathrm{V}$"
#@ node n 0 "capacitor top: $0\,\mathrm{V}$ (held)"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ el V t g "$10\,\mathrm{V}$" col=0 i="$5\,\mathrm{mA}$" to=t
#@ el R t n "$2\,\mathrm{k\Omega}$: falls $10\,\mathrm{V}$" col=1 i="$5\,\mathrm{mA}$" to=n
#@ el C n g "$C$ holds $0\,\mathrm{V}$, charging" col=1 i="$5\,\mathrm{mA}$" to=g
#@ step "Before the switch closes nothing flows, so $v_C(0^-)=0$. Only that carries over: at $0^+$ the capacitor is still a $0\,\mathrm{V}$ step, so its top sits at ground level."
#@ step "The resistor now spans the whole $10\,\mathrm{V}$: it falls $10\,\mathrm{V}$ and carries $\dfrac{10}{2000}=5\,\mathrm{mA}$ into the capacitor."
#@ step "That current raises the capacitor's step at $\dfrac{i}{C}=\dfrac{0.005}{10^{-6}}=5000\,\mathrm{V/s}=5\,\mathrm{V/ms}$. It has $10\,\mathrm{V}$ to travel, so $\tau=\dfrac{10}{5}=2\,\mathrm{ms}=RC$."
#@ view "t = τ = 2 ms"
#@ node t 10 "source +: $10\,\mathrm{V}$"
#@ node n 6.32 "capacitor top: $6.32\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ el V t g "$10\,\mathrm{V}$" col=0 i="$1.84\,\mathrm{mA}$" to=t
#@ el R t n "$2\,\mathrm{k\Omega}$: falls $3.68\,\mathrm{V}$" col=1 i="$1.84\,\mathrm{mA}$" to=n
#@ el C n g "$C$: $6.32\,\mathrm{V}$" col=1 i="$1.84\,\mathrm{mA}$" to=g plus=n v="$v_C$"
#@ note "One time constant in, every height has slid $63\%$ of the way from its $0^+$ value to its $\infty$ value: $v_C=10(1-e^{-1})=6.32\,\mathrm{V}$, and the resistor's fall has shrunk to $3.68\,\mathrm{V}$."
#@ view "t → ∞"
#@ node t 10 "source +: $10\,\mathrm{V}$"
#@ node n 10 "capacitor top: $10\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ el V t g "$10\,\mathrm{V}$" col=0
#@ el R t n "$2\,\mathrm{k\Omega}$: flat" col=0
#@ el C n g "$C$: full, acts as a gap" col=1 plus=n v="$v_C$"
#@ note "Steady state: no current, so the resistor lies flat and the capacitor holds the whole $10\,\mathrm{V}$ step. It stores $\dfrac12Cv^2=\dfrac12(10^{-6})(10)^2=50\,\mu\mathrm{J}$."
```

## When not to force heights

- Pure waveform questions about one element (given $i(t)$, find $v$, $p$, $w$): use graphs of $i$, $v$, $p$ against time.
- Counting nodes, branches and meshes, and choosing between node-voltage and mesh analysis.
- Equivalent-resistance arithmetic on its own (series/parallel reduction, Δ–Y formulas): no potentials are involved until you restore the circuit.
- Coupled unknowns: two or more node heights that depend on each other need the equations. Use the picture to set them up and to check the answer, not to replace the algebra.
- Mesh currents: they are bookkeeping, not real currents, and have no height. Only the branch currents they produce do.
- Inductor currents in parallel combinations: the information is in the currents, which are all at the same pair of heights.

> **Info:** **Where to practise.** Week 1 spreads height problems through every topic and its practice set, and Week 2's Height method workout trains the method on textbook problems, and every worked example with a circuit has a **Walk me through it** height solution.
