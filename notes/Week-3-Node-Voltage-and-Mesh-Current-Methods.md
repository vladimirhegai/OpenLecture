# Week 3: Node-Voltage and Mesh-Current Methods

> **Info:** **Week 3 in one line:** two step-by-step ways to find every voltage in a big circuit. **Node voltages** = give each unknown height a letter and use in = out. **Mesh currents** = give each window a loop current and use climbs = falls.

## The height method (read this first)

| Part | In the height picture | Rule |
|---|---|---|
| Ground | the floor, $0\,\mathrm{V}$ | Pick one wire. The lowest one keeps the picture tidy. |
| Wire (node) | one flat level | Every point on a wire is at the same height. Its voltage **is** its height. |
| Battery (voltage source) | a fixed staircase | Its $+$ end is exactly $V$ higher than its $-$ end. Any current can flow. |
| Pump (current source) | a lift with a fixed flow | It forces its current. How far it lifts is whatever the circuit needs. |
| Resistor | a slide | Current slides **downhill**. Current $=\dfrac{\text{fall}}{R}$, fall $=$ current $\times R$. |
| Diamond (dependent source) | a battery or pump whose size is set elsewhere | Find the thing it depends on first, then treat it like a normal source. |

> **Tip:** **Two laws and one power rule.** At every wire: **current in = current out**. Around any loop: **total climbs = total falls** (you end at the height you started). Power = current $\times$ height change: climbing **gives** energy (green ▲), falling **uses** it (orange ▼).

> **Info:** **The recipe (every example uses it).** ① Ground the lowest wire. ② Place the heights the batteries fix. ③ Give each unknown height a letter and write **in = out** there. ④ Solve. ⑤ Currents $=$ fall $\div R$. ⑥ Power: climbs = falls.
> 
> **New this week:** **node voltages are just heights.** The whole node-voltage method is the recipe above, done carefully.

**Example: Example 0 · The recipe on one small circuit**

Find the height of $x$, every current, and the power of each source.

```schematic
V1 0,3 -> 0,0 "$10\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$" flip
wire 3,3 -> 6,3
I1 6,0 -> 6,3 "$1\,\mathrm{A}$" flip
wire 6,0 -> 0,0
label 3,3 "$x$" above
ground 0,0
#@ inline
#@ straight off
#@ node t 10 "top: $10\,\mathrm{V}$"
#@ node x 8 "$x$: $8\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V t g "$10\,\mathrm{V}$" col=0 i="$1\,\mathrm{A}$" to=t id=eV1
#@ el R t x "$2\,\Omega$: falls $2\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=x id=eR1
#@ el R x g2 "$4\,\Omega$: falls $8\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=eR2
#@ el I g3 x "$1\,\mathrm{A}$" col=2 i="$1\,\mathrm{A}$" to=x id=eI1
#@ step "① Ground: the bottom wire is $0\,\mathrm{V}$."
#@ step "② The battery lifts its top to $10\,\mathrm{V}$." show=t,eV1
#@ step "③ One unknown height, $x$. The pump pushes $1\,\mathrm{A}$ into it. In = out at $x$: in from the $2\,\Omega$ slide, $\dfrac{10-x}{2}$, plus the pump's $1\,\mathrm{A}$; out down the $4\,\Omega$, $\dfrac{x}{4}$." show=eI1
#@ step "④ Solve $\dfrac{10-x}{2}+1=\dfrac{x}{4}$: $x=8\,\mathrm{V}$." show=x
#@ step "⑤ Currents = fall ÷ R: the $2\,\Omega$ falls $2\,\mathrm{V}$ ($1\,\mathrm{A}$), the $4\,\Omega$ falls $8\,\mathrm{V}$ ($2\,\mathrm{A}$). In = out: $1+1=2$ ✓" show=eR1,eR2
#@ step "⑥ Power: the battery lifts $1\,\mathrm{A}$ by $10\,\mathrm{V}$ ($10\,\mathrm{W}$), the pump lifts $1\,\mathrm{A}$ by $8\,\mathrm{V}$ ($8\,\mathrm{W}$). The slides use $2+16=18\,\mathrm{W}$ ✓"
```

1. In = out at $x$.

   $$\frac{10-x}{2}+1=\frac{x}{4}\;\Rightarrow\;x=8\,\mathrm{V}$$
2. Power: climbs = falls.

   $$(10)(1)+(8)(1)=18\,\mathrm{W}=(2)(1)+(8)(2)$$

**Answer:** $x=8\,\mathrm{V}$; $1\,\mathrm{A}$ and $2\,\mathrm{A}$; the battery gives $10\,\mathrm{W}$, the pump $8\,\mathrm{W}$.

## Topic 1: Node voltages are heights

> **Tip:** **How it looks in heights.**
> 
> - Every unknown wire gets a letter (its height). At each one: **in = out**, with every slide's current $=\dfrac{\text{fall}}{R}$.
> - A battery from ground gives a height for free. A pump never fixes a height; it pushes current in (up) or pulls it out (down).
> - A battery (or diamond) **between two unknown wires** locks them a fixed distance apart. Draw a **bubble** around both and write in = out for the whole bubble (a *supernode*).
> - A **diamond**: first write the thing it depends on using your letters.

**Example: Example 1 · One pump, two slides**

Find the height of $x$ and the current in each resistor.

```schematic
I1 0,0 -> 0,3 "$3\,\mathrm{A}$"
wire 0,3 -> 6,3
R1 3,3 -> 3,0 "$4\,\Omega$"
R2 6,3 -> 6,0 "$12\,\Omega$"
wire 0,0 -> 6,0
label 3,3 "$x$" above
ground 0,0
#@ inline
#@ straight off
#@ node x 9 "$x$: $9\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el I g x "$3\,\mathrm{A}$" col=0 i="$3\,\mathrm{A}$" to=x id=eI1
#@ el R x g2 "$4\,\Omega$: falls $9\,\mathrm{V}$" col=1 i="$2.25\,\mathrm{A}$" to=g2 id=eR1
#@ el R x g3 "$12\,\Omega$: falls $9\,\mathrm{V}$" col=2 i="$0.75\,\mathrm{A}$" to=g3 id=eR2
#@ step "Ground the bottom wire. No battery here, only a pump."
#@ step "The pump pushes $3\,\mathrm{A}$ up into $x$. All of it has to slide back down through the $4\,\Omega$ and the $12\,\Omega$." show=eI1
#@ step "In = out at $x$: $3=\dfrac{x}{4}+\dfrac{x}{12}=\dfrac{x}{3}$, so $x=9\,\mathrm{V}$." show=x
#@ step "Currents = fall ÷ R: $\dfrac94=2.25\,\mathrm{A}$ and $\dfrac{9}{12}=0.75\,\mathrm{A}$. The easier slide (smaller $R$) takes more." show=eR1,eR2
#@ step "Power: the pump lifts $3\,\mathrm{A}$ by $9\,\mathrm{V}=27\,\mathrm{W}$; the slides use $20.25+6.75=27\,\mathrm{W}$ ✓"
```

1. In = out at $x$.

   $$3=\frac{x}{4}+\frac{x}{12}\;\Rightarrow\;x=9\,\mathrm{V}$$

**Answer:** $x=9\,\mathrm{V}$; $2.25\,\mathrm{A}$ in the $4\,\Omega$, $0.75\,\mathrm{A}$ in the $12\,\Omega$.

**Example: Example 2 · A battery and a pump feed one wire (Lecture 3)**

Use the node-voltage method to find $i_a$, $i_b$ and $i_c$.

```schematic
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$" i="$i_a$"
R2 3,3 -> 3,0 "$10\,\Omega$" i="$i_b$"
wire 3,3 -> 6,3
R3 6,3 -> 6,0 "$40\,\Omega$" i="$i_c$"
wire 6,3 -> 9,3
I1 9,0 -> 9,3 "$3\,\mathrm{A}$"
wire 9,0 -> 0,0
label 3,3 "$a$" above
ground 0,0
#@ inline
#@ straight off
#@ node s 50 "battery top: $50\,\mathrm{V}$"
#@ node a 40 "$a$: $40\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$50\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$5\,\Omega$: falls $10\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$10\,\Omega$: falls $40\,\mathrm{V}$" col=1 i="$4\,\mathrm{A}$" to=g2 id=eR2
#@ el R a g3 "$40\,\Omega$: falls $40\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=g3 id=eR3
#@ el I g4 a "$3\,\mathrm{A}$" col=3 i="$3\,\mathrm{A}$" to=a id=eI1
#@ step "Ground the bottom wire. The battery lifts its top to $50\,\mathrm{V}$."
#@ step "One unknown height, $a$. In = out at $a$: in from the $5\,\Omega$, $\dfrac{50-a}{5}$, plus the pump's $3\,\mathrm{A}$; out down the $10\,\Omega$ and $40\,\Omega$."
#@ step "$\dfrac{50-a}{5}+3=\dfrac{a}{10}+\dfrac{a}{40}$, so $a=40\,\mathrm{V}$." show=a
#@ step "Currents = fall ÷ R: $i_a=\dfrac{10}{5}=2$, $i_b=\dfrac{40}{10}=4$, $i_c=\dfrac{40}{40}=1\,\mathrm{A}$. In = out: $2+3=4+1$ ✓" show=eR1,eR2,eR3,eV1,eI1
#@ step "Power: battery $2\times50=100\,\mathrm{W}$, pump $3\times40=120\,\mathrm{W}$; the slides use $20+160+40=220\,\mathrm{W}$."
```

1. Ground the bottom wire; only $a$ is unknown. KCL at $a$, currents out; the $3\,\mathrm{A}$ comes in.

   $$\frac{v_a-50}{5}+\frac{v_a}{10}+\frac{v_a}{40}=3$$
2. Multiply by 40 and solve.

   $$8v_a-400+4v_a+v_a=120\;\Rightarrow\;v_a=40\,\mathrm{V}$$
3. Currents = fall ÷ R, in the arrow directions.

   $$i_a=\frac{50-40}{5}=2\,\mathrm{A},\quad i_b=4\,\mathrm{A},\quad i_c=1\,\mathrm{A}$$
4. Check KCL at $a$.

   $$2+3=4+1$$

**Answer:** $v_a=40\,\mathrm{V}$; $i_a=2\,\mathrm{A}$, $i_b=4\,\mathrm{A}$, $i_c=1\,\mathrm{A}$

**Example: Example 3 · Two batteries pull on one wire**

Find the height of $x$.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$" flip
R3 3,3 -> 6,3 "$4\,\Omega$"
V2 6,3 -> 6,0 "$6\,\mathrm{V}$"
wire 6,0 -> 0,0
label 3,3 "$x$" above
ground 0,0
#@ inline
#@ straight off
#@ node s 12 "left top: $12\,\mathrm{V}$"
#@ node x 7.5 "$x$: $7.5\,\mathrm{V}$"
#@ node r 6 "right top: $6\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$12\,\mathrm{V}$" col=0 i="$2.25\,\mathrm{A}$" to=s id=eV1
#@ el R s x "$2\,\Omega$: falls $4.5\,\mathrm{V}$" col=1 i="$2.25\,\mathrm{A}$" to=x id=eR1
#@ el R x g2 "$4\,\Omega$: falls $7.5\,\mathrm{V}$" col=1 i="$1.875\,\mathrm{A}$" to=g2 id=eR2
#@ el R x r "$4\,\Omega$: falls $1.5\,\mathrm{V}$" col=2 i="$0.375\,\mathrm{A}$" to=r id=eR3
#@ el V r g3 "$6\,\mathrm{V}$" col=2 i="$0.375\,\mathrm{A}$" to=g3 id=eV2
#@ step "Ground the bottom wire. Left battery top: $12\,\mathrm{V}$. Right battery top: $6\,\mathrm{V}$."
#@ step "$x$ is joined by slides to $12\,\mathrm{V}$ ($2\,\Omega$), to $0$ ($4\,\Omega$) and to $6\,\mathrm{V}$ ($4\,\Omega$). In = out: $\dfrac{12-x}{2}=\dfrac{x}{4}+\dfrac{x-6}{4}$, so $x=7.5\,\mathrm{V}$." show=x
#@ step "$x$ always lands **between** its neighbours, closest to the one with the smallest $R$ (that slide pulls hardest). Here: closest to $12\,\mathrm{V}$."
#@ step "Currents: $2.25\,\mathrm{A}$ in from the left, $1.875\,\mathrm{A}$ down, $0.375\,\mathrm{A}$ on to the right, where it falls **into** the $6\,\mathrm{V}$ battery (that battery absorbs)." show=eR1,eR2,eR3,eV1,eV2
```

1. In = out at $x$.

   $$\frac{12-x}{2}=\frac{x}{4}+\frac{x-6}{4}\;\Rightarrow\;x=7.5\,\mathrm{V}$$

**Answer:** $x=7.5\,\mathrm{V}$, between $6$ and $12\,\mathrm{V}$ and closest to $12\,\mathrm{V}$.

**Example: Example 4 · Two unknown heights (Lecture 3)**

Use the node-voltage method to find $v_1$ and $v_2$.

```schematic
V1 0,3 -> 0,0 "$10\,\mathrm{V}$"
R1 0,3 -> 3,3 "$1\,\Omega$"
R2 3,3 -> 3,0 "$5\,\Omega$" v="$v_1$"
R3 3,3 -> 6,3 "$2\,\Omega$"
R4 6,3 -> 6,0 "$10\,\Omega$" v="$v_2$"
wire 6,3 -> 9,3
I1 9,0 -> 9,3 "$2\,\mathrm{A}$"
wire 9,0 -> 0,0
label 3,3 "1" above
label 6,3 "2" above
ground 0,0
#@ inline
#@ straight off
#@ node n2 10.91 "node 2: $10.91\,\mathrm{V}$"
#@ node s 10 "battery top: $10\,\mathrm{V}$"
#@ node n1 9.09 "node 1: $9.09\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$10\,\mathrm{V}$" col=0 i="$0.9091\,\mathrm{A}$" to=s id=eV1
#@ el R s n1 "$1\,\Omega$: falls $0.9091\,\mathrm{V}$" col=1 i="$0.9091\,\mathrm{A}$" to=n1 id=eR1
#@ el R n1 g2 "$5\,\Omega$: falls $9.09\,\mathrm{V}$" col=1 i="$1.818\,\mathrm{A}$" to=g2 id=eR2 plus=n1 v="$v_1$"
#@ el R n1 n2 "$2\,\Omega$: falls $1.82\,\mathrm{V}$" col=2 i="$0.9091\,\mathrm{A}$" to=n1 id=eR3
#@ el R n2 g3 "$10\,\Omega$: falls $10.91\,\mathrm{V}$" col=3 i="$1.091\,\mathrm{A}$" to=g3 id=eR4 plus=n2 v="$v_2$"
#@ el I g4 n2 "$2\,\mathrm{A}$" col=4 i="$2\,\mathrm{A}$" to=n2 id=eI1
#@ step "Ground the bottom wire. The battery lifts its top to $10\,\mathrm{V}$."
#@ step "Two unknown heights, $v_1$ and $v_2$: one in = out for each. Node 1: $\dfrac{10-v_1}{1}+\dfrac{v_2-v_1}{2}=\dfrac{v_1}{5}$. Node 2: $2=\dfrac{v_2-v_1}{2}+\dfrac{v_2}{10}$."
#@ step "Solve the pair: $v_1=9.09\,\mathrm{V}$, $v_2=10.91\,\mathrm{V}$. Node 2 is **higher than the battery**: the pump pushed it up there." show=n1,n2
#@ step "Currents = fall ÷ R: $0.909\,\mathrm{A}$ from the battery, $1.818\,\mathrm{A}$ down the $5\,\Omega$, $0.909\,\mathrm{A}$ from node 2 **back** to node 1, $1.091\,\mathrm{A}$ down the $10\,\Omega$." show=eR1,eR2,eR3,eR4,eV1,eI1
#@ step "Power: battery $9.09\,\mathrm{W}$ + pump $2\times10.91=21.82\,\mathrm{W}$ = what the four slides use."
```

1. Ground the bottom wire. KCL at node 1 (currents out).

   $$\frac{v_1-10}{1}+\frac{v_1}{5}+\frac{v_1-v_2}{2}=0$$
2. KCL at node 2; the $2\,\mathrm{A}$ comes in.

   $$\frac{v_2-v_1}{2}+\frac{v_2}{10}=2$$
3. Multiply both by 10.

   $$17v_1-5v_2=100,\qquad -5v_1+6v_2=20$$
4. Solve.

   $$v_1=\frac{100}{11}\approx9.09\,\mathrm{V},\qquad v_2=\frac{120}{11}\approx10.91\,\mathrm{V}$$
5. The $2\,\Omega$ current from 1 to 2 is negative: it really flows from 2 to 1.

   $$i_{1\to2}=\frac{v_1-v_2}{2}=-\frac{10}{11}\,\mathrm{A}$$

**Answer:** $v_1=\dfrac{100}{11}\approx9.09\,\mathrm{V}$, $v_2=\dfrac{120}{11}\approx10.91\,\mathrm{V}$

**Example: Example 5 · A battery from ground gives a height for free (Lecture 3)**

Solve for $v_1$ and $v_2$.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$25\,\Omega$" v="$v_1$"
R2 3,3 -> 6,3 "$10\,\Omega$"
R3 6,3 -> 6,0 "$50\,\Omega$" v="$v_2$"
wire 6,3 -> 9,3
I1 9,0 -> 9,3 "$5\,\mathrm{A}$"
wire 9,0 -> 0,0
label 3,3 "1" above
label 6,3 "2" above
ground 0,0
#@ inline
#@ straight off
#@ node n2 125 "node 2: $125\,\mathrm{V}$"
#@ node n1 100 "node 1: $100\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ el V n1 g "$100\,\mathrm{V}$" col=0 i="$1.5\,\mathrm{A}$" to=n1 id=eV1
#@ el R n1 g2 "$25\,\Omega$: falls $100\,\mathrm{V}$" col=1 i="$4\,\mathrm{A}$" to=g2 id=eR1 plus=n1 v="$v_1$"
#@ el R n1 n2 "$10\,\Omega$: falls $25\,\mathrm{V}$" col=2 i="$2.5\,\mathrm{A}$" to=n1 id=eR2
#@ el R n2 g3 "$50\,\Omega$: falls $125\,\mathrm{V}$" col=3 i="$2.5\,\mathrm{A}$" to=g3 id=eR3 plus=n2 v="$v_2$"
#@ el I g4 n2 "$5\,\mathrm{A}$" col=4 i="$5\,\mathrm{A}$" to=n2 id=eI1
#@ step "Ground the bottom wire. The $100\,\mathrm{V}$ battery goes straight from ground to node 1: $v_1=100\,\mathrm{V}$, no equation needed." show=n1
#@ step "Only $v_2$ is unknown. In = out at node 2: $5=\dfrac{v_2-100}{10}+\dfrac{v_2}{50}$, so $v_2=125\,\mathrm{V}$." show=n2
#@ step "Currents: $2.5\,\mathrm{A}$ slides from node 2 down to node 1 and $2.5\,\mathrm{A}$ down the $50\,\Omega$. Node 1 sends $4\,\mathrm{A}$ down the $25\,\Omega$, so the battery only adds $1.5\,\mathrm{A}$." show=eR1,eR2,eR3,eV1,eI1
#@ step "Power: battery $1.5\times100=150\,\mathrm{W}$ + pump $5\times125=625\,\mathrm{W}$ = slides $400+62.5+312.5=775\,\mathrm{W}$ ✓"
```

1. Ground the bottom wire. The $100\,\mathrm{V}$ source sits between node 1 and ground.

   $$v_1=100\,\mathrm{V}$$
2. KCL at node 2 only (the $5\,\mathrm{A}$ comes in).

   $$\frac{v_2-100}{10}+\frac{v_2}{50}=5$$
3. Multiply by 50.

   $$5v_2-500+v_2=250\;\Rightarrow\;v_2=125\,\mathrm{V}$$

**Answer:** $v_1=100\,\mathrm{V}$, $v_2=125\,\mathrm{V}$

**Example: Example 6 · Two pumps, no battery: ground the lowest wire**

Find $V_1$ and the currents $I_1$–$I_4$. (The diagonal $4\,\mathrm{mA}$ source is redrawn straight down from node 2; it still joins node 2 to the bottom wire.)

```schematic
R1 0,3 -> 0,0 "$3\,\mathrm{k\Omega}$" v="$V_1$" i="$I_1$"
wire 0,3 -> 3,3
I1 3,3 -> 3,0 "$6\,\mathrm{mA}$"
R2 3,3 -> 7,3 "$2\,\mathrm{k\Omega}$" i="$I_2$"
I2 7,3 -> 7,0 "$4\,\mathrm{mA}$"
wire 7,3 -> 10,3
R3 10,3 -> 10,0 "$2\,\mathrm{k\Omega}$" i="$I_3$"
wire 10,3 -> 13,3
R4 13,3 -> 13,0 "$2\,\mathrm{k\Omega}$" i="$I_4$"
wire 13,0 -> 0,0
label 3,3 "1" above
label 7,3 "2" above
ground 3,0
#@ inline
#@ straight off
#@ node z0 11 "bottom wire: $11\,\mathrm{V}$"
#@ node n2 4.67 "node 2: $4.67\,\mathrm{V}$"
#@ node g 0 "node 1: $0\,\mathrm{V}$" ground
#@ node g2 0 "node 1: $0\,\mathrm{V}$" ground
#@ node g3 0 "node 1: $0\,\mathrm{V}$" ground
#@ el R g z0 "$3\,\mathrm{k\Omega}$: falls $11\,\mathrm{V}$" col=0 i="$3.667\,\mathrm{mA}$" to=g id=eR1 plus=g v="$V_1$"
#@ el I g2 z0 "$6\,\mathrm{mA}$" col=1 i="$6\,\mathrm{mA}$" to=z0 id=eI1
#@ el R g3 n2 "$2\,\mathrm{k\Omega}$: falls $4.67\,\mathrm{V}$" col=2 i="$2.333\,\mathrm{mA}$" to=g3 id=eR2
#@ el I n2 z0 "$4\,\mathrm{mA}$" col=3 i="$4\,\mathrm{mA}$" to=z0 id=eI2
#@ el R n2 z0 "$2\,\mathrm{k\Omega}$: falls $6.33\,\mathrm{V}$" col=4 i="$3.167\,\mathrm{mA}$" to=n2 id=eR3
#@ el R n2 z0 "$2\,\mathrm{k\Omega}$: falls $6.33\,\mathrm{V}$" col=5 i="$3.167\,\mathrm{mA}$" to=n2 id=eR4
#@ step "Ground **node 1**, the lowest wire (step 2 shows why). Moving ground never changes an answer: $V_1$ is still node 1 measured from the bottom wire."
#@ step "Read the pumps: both pull current **out of** their node and push it into the bottom wire. That current must slide back down to the nodes, so the bottom wire sits **above** both of them." show=eI1,eI2
#@ step "In = out at each node (mA, kΩ, measured from the bottom wire): $\dfrac{V_1}{3}+6+\dfrac{V_1-V_2}{2}=0$ and $\dfrac{V_2-V_1}{2}+4+\dfrac{V_2}{2}+\dfrac{V_2}{2}=0$. So $V_1=-11$, $V_2=-6.33\,\mathrm{V}$: here the bottom wire is $11\,\mathrm{V}$ up and node 2 is $4.67\,\mathrm{V}$ up." show=z0,n2
#@ step "Currents = fall ÷ R: $3.67\,\mathrm{mA}$ slides from the bottom wire to node 1, $2.33\,\mathrm{mA}$ from node 2 to node 1, $3.17\,\mathrm{mA}$ in each right $2\,\mathrm{k\Omega}$. All flow **up** the drawing, so $I_1=-3.67$, $I_2=-2.33$, $I_3=I_4=-3.17\,\mathrm{mA}$." show=eR1,eR2,eR3,eR4
#@ step "Power: both pumps lift current up to the bottom wire ($66+25.3=91.3\,\mathrm{mW}$); the slides use the same."
```

1. Ground the bottom wire. No voltage source, so both node heights are unknown. KCL at node 1 (currents out, mA and kΩ).

   $$\frac{V_1}{3}+6+\frac{V_1-V_2}{2}=0$$
2. KCL at node 2.

   $$\frac{V_2-V_1}{2}+4+\frac{V_2}{2}+\frac{V_2}{2}=0\;\Rightarrow\;V_1=3V_2+8$$
3. Substitute into node 1.

   $$\tfrac56(3V_2+8)-\tfrac12V_2=-6\;\Rightarrow\;V_2=-\tfrac{19}{3}\,\mathrm{V},\quad V_1=-11\,\mathrm{V}$$
4. Branch currents in their arrow directions.

   $$\begin{aligned}&I_1=\frac{V_1}{3}=-3.67\,\mathrm{mA},\quad I_2=\frac{V_1-V_2}{2}=-2.33\,\mathrm{mA}\\&I_3=I_4=\frac{V_2}{2}=-3.17\,\mathrm{mA}\end{aligned}$$
5. Power check: both sources deliver, the resistors absorb.

   $$(6)(11)+(4)(6.33)=91.3\,\mathrm{mW}=40.3+10.9+20.1+20.1$$

**Answer:** $V_1=-11\,\mathrm{V}$ ($V_2=-6.33\,\mathrm{V}$); $I_1=-3.67\,\mathrm{mA}$, $I_2=-2.33\,\mathrm{mA}$, $I_3=I_4=-3.17\,\mathrm{mA}$. Both current sources deliver power.

**Example: Example 7 · Three pumps, two of them absorbing**

Find $I_0$. The right edge runs down into the bottom wire, so the $2\,\mathrm{mA}$ source and the horizontal $4\,\mathrm{k\Omega}$ both end on the ground node.

```schematic
R1 0,6 -> 0,0 "$2\,\mathrm{k\Omega}$"
wire 0,6 -> 6,6
I1 3,3 -> 3,6 "$4\,\mathrm{mA}$"
I2 3,0 -> 3,3 "$6\,\mathrm{mA}$"
R2 6,6 -> 6,3 "$4\,\mathrm{k\Omega}$"
R3 6,3 -> 6,0 "$12\,\mathrm{k\Omega}$" i="$I_0$"
wire 3,3 -> 6,3
R4 6,3 -> 9,3 "$4\,\mathrm{k\Omega}$"
I3 6,6 -> 9,6 "$2\,\mathrm{mA}$"
wire 9,6 -> 9,0
wire 9,0 -> 0,0
label 0,6 "$a$" left
label 4.5,3 "$b$" above
ground 0,0
#@ inline
#@ straight off
#@ node b 5.33 "$b$ (middle): $5.33\,\mathrm{V}$"
#@ node a 4.44 "$a$ (top): $4.44\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ node g5 0 "ground: $0\,\mathrm{V}$" ground
#@ el R a b "$4\,\mathrm{k\Omega}$: falls $0.8889\,\mathrm{V}$" col=0 i="$0.2222\,\mathrm{mA}$" to=a id=eR2
#@ el R a g "$2\,\mathrm{k\Omega}$: falls $4.44\,\mathrm{V}$" col=0 i="$2.222\,\mathrm{mA}$" to=g id=eR1
#@ el I b a "$4\,\mathrm{mA}$" col=1 i="$4\,\mathrm{mA}$" to=a id=eI1
#@ el I a g2 "$2\,\mathrm{mA}$" col=1 i="$2\,\mathrm{mA}$" to=g2 id=eI3
#@ el I g3 b "$6\,\mathrm{mA}$" col=2 i="$6\,\mathrm{mA}$" to=b id=eI2
#@ el R b g4 "$12\,\mathrm{k\Omega}$: falls $5.33\,\mathrm{V}$" col=3 i="$0.4444\,\mathrm{mA}$" to=g4 id=eR3
#@ el R b g5 "$4\,\mathrm{k\Omega}$: falls $5.33\,\mathrm{V}$" col=4 i="$1.333\,\mathrm{mA}$" to=g5 id=eR4
#@ step "Ground the bottom wire. No battery, so no height is given: $a$ (top wire) and $b$ (middle wire) are both unknown."
#@ step "Read the pumps: $6\,\mathrm{mA}$ pushed up into $b$; $4\,\mathrm{mA}$ moved from $b$ to $a$; $2\,\mathrm{mA}$ drained from $a$ to ground." show=eI1,eI2,eI3
#@ step "In = out (mA, kΩ). At $a$: $4=\dfrac{a}{2}+\dfrac{a-b}{4}+2$. At $b$: $6=\dfrac{b-a}{4}+\dfrac{b}{12}+\dfrac{b}{4}+4$. So $a=4.44$, $b=5.33\,\mathrm{V}$." show=a,b
#@ step "$I_0=\dfrac{5.33}{12}=0.444\,\mathrm{mA}$. And $b$ is above $a$, so $0.222\,\mathrm{mA}$ slides from $b$ to $a$." show=eR1,eR2,eR3,eR4
#@ step "Power: only the $6\,\mathrm{mA}$ pump climbs ($32\,\mathrm{mW}$). The other two carry current **downhill**, so they absorb."
```

1. Ground the bottom wire; name the top wire $a$ and the middle wire $b$. KCL at $a$ (mA and kΩ): the $4\,\mathrm{mA}$ comes in, the $2\,\mathrm{mA}$ goes out.

   $$\frac{a}{2}+\frac{a-b}{4}+2=4\;\Rightarrow\;3a-b=8$$
2. KCL at $b$: the $6\,\mathrm{mA}$ comes in, the $4\,\mathrm{mA}$ goes out.

   $$\frac{b-a}{4}+\frac{b}{12}+\frac{b}{4}+4=6\;\Rightarrow\;-3a+7b=24$$
3. Add the two equations.

   $$6b=32\;\Rightarrow\;b=\tfrac{16}{3}\,\mathrm{V},\qquad a=\tfrac{40}{9}\,\mathrm{V}$$
4. $I_0$ is the current down the $12\,\mathrm{k\Omega}$.

   $$I_0=\frac{16/3}{12}=\frac{4}{9}\approx0.444\,\mathrm{mA}$$

**Answer:** $I_0=\dfrac{4}{9}\,\mathrm{mA}\approx0.444\,\mathrm{mA}$ (with $a=4.44\,\mathrm{V}$, $b=5.33\,\mathrm{V}$). Only the $6\,\mathrm{mA}$ source delivers power; the other two absorb.

**Example: Example 8 · A battery between two unknown wires: the bubble**

Find $p$ and $q$.

```schematic
I1 0,0 -> 0,3 "$3\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$2\,\Omega$" flip
V1 6,3 -> 3,3 "$6\,\mathrm{V}$"
R2 6,3 -> 6,0 "$4\,\Omega$"
wire 6,0 -> 0,0
label 3,3 "$p$" above
label 6,3 "$q$" above
ground 0,0
#@ inline
#@ straight off
#@ node q 8 "$q$: $8\,\mathrm{V}$"
#@ node p 2 "$p$: $2\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el I g p "$3\,\mathrm{A}$" col=0 i="$3\,\mathrm{A}$" to=p id=eI1
#@ el R p g2 "$2\,\Omega$: falls $2\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=g2 id=eR1
#@ el V q p "$6\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=q id=eV1
#@ el R q g3 "$4\,\Omega$: falls $8\,\mathrm{V}$" col=3 i="$2\,\mathrm{A}$" to=g3 id=eR2
#@ step "Ground the bottom wire. The $6\,\mathrm{V}$ battery sits between $p$ and $q$, and **neither** is known. It locks them: $q=p+6$, always."
#@ step "So draw a bubble around $p$ and $q$ and treat it as one wire. In = out for the bubble: the pump pushes $3\,\mathrm{A}$ in; it leaves down the $2\,\Omega$ and the $4\,\Omega$: $3=\dfrac{p}{2}+\dfrac{p+6}{4}$, so $p=2$, $q=8\,\mathrm{V}$." show=p,q
#@ step "Currents: $1\,\mathrm{A}$ down the $2\,\Omega$, $2\,\mathrm{A}$ down the $4\,\Omega$. The other $2\,\mathrm{A}$ climbs through the battery from $p$ to $q$. (The battery's own current never goes into the bubble equation: it stays inside.)" show=eR1,eR2,eV1,eI1
```

1. Bubble (supernode): the battery fixes the difference; in = out for the bubble.

   $$q=p+6,\qquad 3=\frac{p}{2}+\frac{p+6}{4}\;\Rightarrow\;p=2\,\mathrm{V},\;q=8\,\mathrm{V}$$

**Answer:** $p=2\,\mathrm{V}$, $q=8\,\mathrm{V}$

**Example: Example 9 · A diamond: find what it depends on first (Lecture 3)**

Use the node-voltage method to find the power dissipated in the $5\,\Omega$ resistor.

```schematic
V1 0,3 -> 0,0 "$20\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$20\,\Omega$"
R3 3,3 -> 6,3 "$5\,\Omega$" i="$i_\Phi$"
R4 6,3 -> 6,0 "$10\,\Omega$"
R5 6,3 -> 9,3 "$2\,\Omega$"
E1 9,3 -> 9,0 "$8i_\Phi$"
wire 9,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" above
label 9,3 "$c$" above
ground 0,0
#@ inline
#@ straight off
#@ node s 20 "battery top: $20\,\mathrm{V}$"
#@ node a 16 "$a$: $16\,\mathrm{V}$"
#@ node b 10 "$b$: $10\,\mathrm{V}$"
#@ node c 9.6 "$c$: $9.6\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$20\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$2\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$20\,\Omega$: falls $16\,\mathrm{V}$" col=1 i="$0.8\,\mathrm{A}$" to=g2 id=eR2
#@ el R a b "$5\,\Omega$: falls $6\,\mathrm{V}$" col=2 i="$1.2\,\mathrm{A}$" to=b id=eR3
#@ el R b g3 "$10\,\Omega$: falls $10\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=g3 id=eR4
#@ el R b c "$2\,\Omega$: falls $0.4\,\mathrm{V}$" col=3 i="$0.2\,\mathrm{A}$" to=c id=eR5
#@ el E c g4 "$8i_\Phi$: $9.6\,\mathrm{V}$" col=3 i="$0.2\,\mathrm{A}$" to=g4 id=eE1
#@ step "Ground the bottom wire. The $20\,\mathrm{V}$ battery lifts its top to $20\,\mathrm{V}$."
#@ step "The diamond is a battery of $8i_\Phi$ volts from ground to $c$. It depends on $i_\Phi$, the current in the $5\,\Omega$: $i_\Phi=\dfrac{a-b}{5}$. So $c=8i_\Phi=1.6(a-b)$."
#@ step "Unknowns $a$ and $b$ (with $c=1.6(a-b)$). In = out at $a$ and at $b$ gives $a=16\,\mathrm{V}$, $b=10\,\mathrm{V}$." show=a,b
#@ step "Now the diamond: $i_\Phi=\dfrac{16-10}{5}=1.2\,\mathrm{A}$, so $c=8(1.2)=9.6\,\mathrm{V}$." show=c,eR3,eE1
#@ step "The rest: $2\,\mathrm{A}$ from the battery, $0.8$ and $1\,\mathrm{A}$ down the $20\,\Omega$ and $10\,\Omega$, $0.2\,\mathrm{A}$ from $b$ to $c$ that then falls through the diamond (it absorbs). The $5\,\Omega$ uses $1.2\times6=7.2\,\mathrm{W}$." show=eR1,eR2,eR4,eR5,eV1
```

1. Ground the bottom wire. Control first: the diamond fixes $v_c$ in terms of $a$ and $b$.

   $$i_\Phi=\frac{v_a-v_b}{5},\qquad v_c=8i_\Phi=1.6(v_a-v_b)$$
2. KCL at $a$ and $b$.

   $$\begin{aligned}&\frac{v_a-20}{2}+\frac{v_a}{20}+\frac{v_a-v_b}{5}=0\\&\frac{v_b-v_a}{5}+\frac{v_b}{10}+\frac{v_b-v_c}{2}=0\end{aligned}$$
3. Substitute $v_c$ and collect.

   $$0.75v_a-0.2v_b=10,\qquad -v_a+1.6v_b=0$$
4. Solve.

   $$v_a=16\,\mathrm{V},\quad v_b=10\,\mathrm{V},\quad i_\Phi=1.2\,\mathrm{A}$$
5. Power in the $5\,\Omega$.

   $$p_{5\Omega}=(1.2)^2(5)=7.2\,\mathrm{W}$$

**Answer:** $v_a=16\,\mathrm{V}$, $v_b=10\,\mathrm{V}$, $i_\Phi=1.2\,\mathrm{A}$; $p_{5\Omega}=7.2\,\mathrm{W}$

**Example: Example 10 · A bubble with a diamond inside (Lecture 3)**

Use a supernode around $b$ and $c$ to find the node voltages.

```schematic
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$40\,\Omega$"
R2 6,3 -> 3,3 "$5\,\Omega$" i="$i_\Phi$"
R3 6,3 -> 6,0 "$50\,\Omega$"
E1 9,3 -> 6,3 "$10i_\Phi$"
R4 9,3 -> 9,0 "$100\,\Omega$"
wire 9,3 -> 12,3
I1 12,0 -> 12,3 "$4\,\mathrm{A}$"
wire 12,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" below
label 9,3 "$c$" below
ground 0,0
#@ inline
#@ straight off
#@ node c 80 "$c$: $80\,\mathrm{V}$"
#@ node b 60 "$b$: $60\,\mathrm{V}$"
#@ node a 50 "$a$: $50\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ node g5 0 "ground: $0\,\mathrm{V}$" ground
#@ el I g c "$4\,\mathrm{A}$" col=0 i="$4\,\mathrm{A}$" to=c id=eI1
#@ el R c g2 "$100\,\Omega$: falls $80\,\mathrm{V}$" col=1 i="$0.8\,\mathrm{A}$" to=g2 id=eR4
#@ el E c b "$10i_\Phi$: $20\,\mathrm{V}$" col=2 i="$3.2\,\mathrm{A}$" to=b id=eE1
#@ el R b g3 "$50\,\Omega$: falls $60\,\mathrm{V}$" col=2 i="$1.2\,\mathrm{A}$" to=g3 id=eR3
#@ el R b a "$5\,\Omega$: falls $10\,\mathrm{V}$" col=3 i="$2\,\mathrm{A}$" to=a id=eR2
#@ el R a g4 "$40\,\Omega$: falls $50\,\mathrm{V}$" col=3 i="$1.25\,\mathrm{A}$" to=g4 id=eR1
#@ el V a g5 "$50\,\mathrm{V}$" col=4 i="$0.75\,\mathrm{A}$" to=g5 id=eV1
#@ step "Ground the bottom wire. The $50\,\mathrm{V}$ battery fixes $a=50\,\mathrm{V}$." show=a
#@ step "The diamond ($10i_\Phi$) sits between $b$ and $c$, both unknown: it locks $c=b+10i_\Phi$. It depends on $i_\Phi$, the current from $b$ to $a$ through $5\,\Omega$: $i_\Phi=\dfrac{b-50}{5}$. So $c=3b-100$."
#@ step "Bubble around $b$ and $c$. In = out for the bubble: the $4\,\mathrm{A}$ pump comes in; out go $\dfrac{b-50}{5}$, $\dfrac{b}{50}$ and $\dfrac{c}{100}$. So $b=60$, $c=80\,\mathrm{V}$." show=b,c,eE1
#@ step "Currents: $i_\Phi=2\,\mathrm{A}$ from $b$ to $a$, $1.2\,\mathrm{A}$ down the $50\,\Omega$, $0.8\,\mathrm{A}$ down the $100\,\Omega$. The other $3.2\,\mathrm{A}$ goes **down** through the diamond (it absorbs)." show=eR2,eR3,eR4,eI1
#@ step "At $a$: $2\,\mathrm{A}$ arrives, the $40\,\Omega$ takes $1.25\,\mathrm{A}$, so $0.75\,\mathrm{A}$ falls into the $50\,\mathrm{V}$ battery (it absorbs). Only the pump climbs: $4\times80=320\,\mathrm{W}$." show=eR1,eV1
```

1. Ground the bottom wire. The grounded source fixes $v_a$; the control uses the leftward arrow.

   $$v_a=50\,\mathrm{V},\qquad i_\Phi=\frac{v_b-50}{5}$$
2. The rod: the diamond fixes $v_c-v_b$.

   $$v_c-v_b=10i_\Phi=2(v_b-50)\;\Rightarrow\;v_c=3v_b-100$$
3. KCL around the rod: only currents crossing its boundary.

   $$\frac{v_b-50}{5}+\frac{v_b}{50}+\frac{v_c}{100}=4$$
4. Substitute and solve.

   $$0.25v_b=15\;\Rightarrow\;v_b=60\,\mathrm{V},\quad v_c=80\,\mathrm{V},\quad i_\Phi=2\,\mathrm{A}$$

**Answer:** $v_a=50\,\mathrm{V}$, $v_b=60\,\mathrm{V}$, $v_c=80\,\mathrm{V}$, $i_\Phi=2\,\mathrm{A}$

> **Warning:** **Bubble traps.** The two wires in a bubble are **not** equal: they differ by the battery's $V$. The battery's own current never appears in the bubble's in = out. And a diamond's control arrow decides the sign: $\dfrac{b-a}{R}$ is not $\dfrac{a-b}{R}$.

**Problem: Try it 1 · How much does the pump take? (Textbook P4.6)** (introductory)

Use the node-voltage method to find how much power the $2\,\mathrm{A}$ source extracts from the circuit.

```schematic
I1 0,3 -> 0,0 "$2\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$4\,\Omega$"
R2 3,3 -> 6,3 "$2\,\Omega$"
V1 6,3 -> 6,0 "$55\,\mathrm{V}$"
R3 3,0 -> 6,0 "$3\,\Omega$"
wire 0,0 -> 3,0
label 3,3 "$a$" above
label 6,0 "$d$" below
ground 0,0
#@ spoiler
#@ straight off
#@ node c 55 "battery top: $55\,\mathrm{V}$"
#@ node a 41 "$a$: $41\,\mathrm{V}$"
#@ node z0 21 "bottom-left: $21\,\mathrm{V}$"
#@ node g 0 "$d$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$d$: $0\,\mathrm{V}$" ground
#@ el I a z0 "$2\,\mathrm{A}$" col=0 i="$2\,\mathrm{A}$" to=z0 id=eI1
#@ el R a z0 "$4\,\Omega$: falls $20\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=z0 id=eR1
#@ el R z0 g "$3\,\Omega$: falls $21\,\mathrm{V}$" col=2 i="$7\,\mathrm{A}$" to=g id=eR3
#@ el R a c "$2\,\Omega$: falls $14\,\mathrm{V}$" col=3 i="$7\,\mathrm{A}$" to=a id=eR2
#@ el V c g2 "$55\,\mathrm{V}$" col=4 i="$7\,\mathrm{A}$" to=c id=eV1
#@ step "Ground $d$, the lowest wire (the $55\,\mathrm{V}$ battery's $-$ end). Answers are still read from the bottom-left wire."
#@ step "The right side is one path: $a$ → $2\,\Omega$ → battery → $3\,\Omega$ → bottom-left. Its current toward $a$ is $\dfrac{55-a}{5}$ (the battery climbs $55$, the slides fall $5\,\Omega$ worth)."
#@ step "In = out at $a$ (from the bottom-left wire): $\dfrac{55-a}{5}=\dfrac{a}{4}+2$, so $a=20\,\mathrm{V}$." show=a
#@ step "So $7\,\mathrm{A}$ climbs the battery and slides into $a$; $5\,\mathrm{A}$ goes down the $4\,\Omega$ and $2\,\mathrm{A}$ down through the pump." show=c,z0,eR1,eR2,eR3,eV1
#@ step "The pump carries $2\,\mathrm{A}$ **downhill** by $20\,\mathrm{V}$: it extracts $40\,\mathrm{W}$." show=eI1
```

<details><summary>Solution</summary>

1. One unknown, $a$. The right branch: battery and $2+3\,\Omega$ in series.

   $$\frac{55-v_a}{5}=\frac{v_a}{4}+2\;\Rightarrow\;v_a=20\,\mathrm{V}$$
2. The pump carries its current from $a$ down to the bottom wire.

   $$p=(20)(2)=40\,\mathrm{W}\text{ absorbed}$$

**Answer:** The $2\,\mathrm{A}$ source extracts (absorbs) $40\,\mathrm{W}$.

</details>

**Problem: Try it 2 · Find v_o, then every power (Textbook P4.8 and P4.9)** (introductory)

**(a)** Use the node-voltage method to find $v_o$. **(b)** Find the power developed by the $5\,\mathrm{A}$ source and by the $180\,\mathrm{V}$ source, and check the balance.

```schematic
V1 0,2 -> 0,0 "$180\,\mathrm{V}$"
R1 0,4 -> 0,2 "$12\,\Omega$"
R2 0,4 -> 3,4 "$5\,\Omega$"
R3 3,4 -> 3,0 "$2\,\Omega$" v="$v_o$"
wire 3,4 -> 6,4
I1 6,4 -> 6,0 "$5\,\mathrm{A}$"
wire 0,0 -> 6,0
label 0,4 "$t$" left
ground 0,0
#@ spoiler
#@ straight off
#@ node s 180 "battery top: $180\,\mathrm{V}$"
#@ node t 60 "$t$: $60\,\mathrm{V}$"
#@ node o 10 "$v_o$: $10\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$180\,\mathrm{V}$" col=0 i="$10\,\mathrm{A}$" to=s id=eV1
#@ el R t s "$12\,\Omega$: falls $120\,\mathrm{V}$" col=1 i="$10\,\mathrm{A}$" to=t id=eR1
#@ el R t o "$5\,\Omega$: falls $50\,\mathrm{V}$" col=1 i="$10\,\mathrm{A}$" to=o id=eR2
#@ el R o g2 "$2\,\Omega$: falls $10\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=g2 id=eR3 plus=o v="$v_o$"
#@ el I o g3 "$5\,\mathrm{A}$" col=2 i="$5\,\mathrm{A}$" to=g3 id=eI1
#@ step "Ground the bottom wire. The battery lifts its top to $180\,\mathrm{V}$."
#@ step "The $12\,\Omega$ and $5\,\Omega$ are one path ($17\,\Omega$) from $180\,\mathrm{V}$ to $v_o$. In = out at $v_o$: $\dfrac{180-v_o}{17}=\dfrac{v_o}{2}+5$, so $v_o=10\,\mathrm{V}$." show=o,t
#@ step "Currents: $10\,\mathrm{A}$ down the $12\,\Omega$ and $5\,\Omega$, $5\,\mathrm{A}$ down the $2\,\Omega$, $5\,\mathrm{A}$ down through the pump." show=eR1,eR2,eR3,eI1,eV1
#@ step "Power: the battery lifts $10\,\mathrm{A}$ by $180\,\mathrm{V}$: $1800\,\mathrm{W}$. The pump carries $5\,\mathrm{A}$ **down** $10\,\mathrm{V}$: it absorbs $50\,\mathrm{W}$ (develops $-50\,\mathrm{W}$). Slides: $1200+500+50=1750$ ✓"
```

<details><summary>Solution</summary>

1. In = out at $v_o$.

   $$\frac{180-v_o}{12+5}=\frac{v_o}{2}+5\;\Rightarrow\;v_o=10\,\mathrm{V}$$
2. Powers.

   $$\begin{aligned}p_{180}&=180(10)=1800\,\mathrm{W}\text{ developed}\\p_{5\mathrm{A}}&=-(10)(5)=-50\,\mathrm{W}\text{ developed}\end{aligned}$$

**Answer:** **(a)** $v_o=10\,\mathrm{V}$. **(b)** $180\,\mathrm{V}$: $1800\,\mathrm{W}$; $5\,\mathrm{A}$: $-50\,\mathrm{W}$ (it absorbs $50\,\mathrm{W}$). Total $1750\,\mathrm{W}$ developed = dissipated.

</details>

**Problem: Try it 3 · One wire above both batteries (Assessment AP 4.13)** (introductory)

Use the node-voltage method to find $v_1$ and the power delivered by the $2\,\mathrm{A}$ current source.

```schematic
V1 0,3 -> 0,0 "$20\,\mathrm{V}$"
R1 0,3 -> 3,3 "$15\,\Omega$"
I1 3,0 -> 3,3 "$2\,\mathrm{A}$"
R2 3,3 -> 6,3 "$10\,\Omega$"
V2 6,3 -> 6,0 "$25\,\mathrm{V}$"
wire 6,0 -> 0,0
label 3,3 "$v_1$" above
ground 0,0
#@ spoiler
#@ straight off
#@ node n1 35 "$v_1$: $35\,\mathrm{V}$"
#@ node r 25 "right top: $25\,\mathrm{V}$"
#@ node s 20 "left top: $20\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el I g n1 "$2\,\mathrm{A}$" col=0 i="$2\,\mathrm{A}$" to=n1 id=eI1
#@ el R s n1 "$15\,\Omega$: falls $15\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=s id=eR1
#@ el V s g2 "$20\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=g2 id=eV1
#@ el R n1 r "$10\,\Omega$: falls $10\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=r id=eR2
#@ el V r g3 "$25\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=g3 id=eV2
#@ step "Ground the bottom wire. Left battery top: $20\,\mathrm{V}$. Right battery top: $25\,\mathrm{V}$."
#@ step "One unknown, $v_1$. In = out: $2=\dfrac{v_1-20}{15}+\dfrac{v_1-25}{10}$, so $v_1=35\,\mathrm{V}$." show=n1
#@ step "$v_1$ is above both batteries, so $1\,\mathrm{A}$ slides away on each side and falls **into** both batteries (both absorb)." show=eR1,eR2,eV1,eV2
#@ step "The pump lifts $2\,\mathrm{A}$ by $35\,\mathrm{V}$: it delivers $70\,\mathrm{W}=20+25+15+10$." show=eI1
```

<details><summary>Solution</summary>

1. Ground the bottom wire. KCL at $v_1$ (currents out); the $2\,\mathrm{A}$ comes in.

   $$\frac{v_1-20}{15}+\frac{v_1-25}{10}=2$$
2. Multiply by 30.

   $$2v_1-40+3v_1-75=60\;\Rightarrow\;v_1=35\,\mathrm{V}$$
3. The source lifts $2\,\mathrm{A}$ from $0$ to $35\,\mathrm{V}$.

   $$p_{2\mathrm{A}}=(35)(2)=70\,\mathrm{W}\text{ delivered}$$

**Answer:** $v_1=35\,\mathrm{V}$; the $2\,\mathrm{A}$ source delivers $70\,\mathrm{W}$.

</details>

**Problem: Try it 4 · Two pumps, no battery (Textbook P4.13)** (introductory)

Use the node-voltage method to find $v_1$ and $v_2$.

```schematic
I1 0,3 -> 0,0 "$2.4\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$125\,\Omega$" v="$v_1$"
R2 3,3 -> 6,3 "$25\,\Omega$"
R3 6,3 -> 6,0 "$250\,\Omega$"
wire 6,3 -> 9,3
R4 9,3 -> 9,0 "$375\,\Omega$" v="$v_2$"
wire 9,3 -> 12,3
I2 12,0 -> 12,3 "$3.2\,\mathrm{A}$"
wire 12,0 -> 0,0
label 3,3 "1" above
label 6,3 "2" above
ground 0,0
#@ spoiler
#@ straight off
#@ node n2 90 "$v_2$: $90\,\mathrm{V}$"
#@ node n1 25 "$v_1$: $25\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ node g5 0 "ground: $0\,\mathrm{V}$" ground
#@ el I g n2 "$3.2\,\mathrm{A}$" col=0 i="$3.2\,\mathrm{A}$" to=n2 id=eI2
#@ el R n2 g2 "$375\,\Omega$: falls $90\,\mathrm{V}$" col=1 i="$0.24\,\mathrm{A}$" to=g2 id=eR4 plus=n2 v="$v_2$"
#@ el R n2 g3 "$250\,\Omega$: falls $90\,\mathrm{V}$" col=2 i="$0.36\,\mathrm{A}$" to=g3 id=eR3
#@ el R n1 n2 "$25\,\Omega$: falls $65\,\mathrm{V}$" col=3 i="$2.6\,\mathrm{A}$" to=n1 id=eR2
#@ el R n1 g4 "$125\,\Omega$: falls $25\,\mathrm{V}$" col=4 i="$0.2\,\mathrm{A}$" to=g4 id=eR1 plus=n1 v="$v_1$"
#@ el I n1 g5 "$2.4\,\mathrm{A}$" col=5 i="$2.4\,\mathrm{A}$" to=g5 id=eI1
#@ step "Ground the bottom wire. No battery: $v_1$ and $v_2$ are both unknown."
#@ step "In = out at each. Node 1: $\dfrac{v_1}{125}+\dfrac{v_1-v_2}{25}+2.4=0$. Node 2: $\dfrac{v_2}{250}+\dfrac{v_2}{375}+\dfrac{v_2-v_1}{25}=3.2$."
#@ step "Solve: $v_1=25\,\mathrm{V}$, $v_2=90\,\mathrm{V}$." show=n1,n2
#@ step "$2.6\,\mathrm{A}$ slides from node 2 to node 1; $0.2\,\mathrm{A}$ goes down the $125\,\Omega$ and $2.4\,\mathrm{A}$ down through the left pump (it absorbs). Only the $3.2\,\mathrm{A}$ pump climbs." show=eR1,eR2,eR3,eR4,eI1,eI2
```

<details><summary>Solution</summary>

1. Ground the bottom wire. KCL at node 1 (out = in; the $2.4\,\mathrm{A}$ leaves).

   $$\frac{v_1}{125}+\frac{v_1-v_2}{25}=-2.4$$
2. KCL at node 2 (the $3.2\,\mathrm{A}$ comes in).

   $$\frac{v_2}{250}+\frac{v_2}{375}+\frac{v_2-v_1}{25}=3.2$$
3. Clear fractions (×125 and ×750).

   $$6v_1-5v_2=-300,\qquad -30v_1+35v_2=2400$$
4. Add 5× the first to the second.

   $$10v_2=900\;\Rightarrow\;v_2=90\,\mathrm{V},\quad v_1=25\,\mathrm{V}$$

**Answer:** $v_1=25\,\mathrm{V}$, $v_2=90\,\mathrm{V}$

</details>

**Problem: Try it 5 · The top wire lands at the average (Textbook P4.16)** (introductory)

**(a)** Show that $v_o$ is the average of the source voltages. **(b)** Find $v_o$ if $v_1=150\,\mathrm{V}$, $v_2=200\,\mathrm{V}$ and $v_3=-50\,\mathrm{V}$.

```schematic
V1 0,2 -> 0,0 "$v_1$"
R1 0,4 -> 0,2 "$R$"
V2 3,2 -> 3,0 "$v_2$"
R2 3,4 -> 3,2 "$R$"
V3 6,2 -> 6,0 "$v_3$"
R3 6,4 -> 6,2 "$R$"
wire 0,4 -> 8,4
wire 0,0 -> 8,0
terminal 8,4 "$+$" right
terminal 8,0 "$-$" right
label 8,2 "$v_o$" right
ground 0,0
#@ spoiler
#@ straight off
#@ node p2 250 "$v_2$ top: $250\,\mathrm{V}$"
#@ node p1 200 "$v_1$ top: $200\,\mathrm{V}$"
#@ node o 150 "$v_o$: $150\,\mathrm{V}$"
#@ node z0 50 "bottom: $50\,\mathrm{V}$"
#@ node g 0 "$v_3$ top: $0\,\mathrm{V}$" ground
#@ node g2 0 "$v_3$ top: $0\,\mathrm{V}$" ground
#@ el V p2 z0 "$200\,\mathrm{V}$" col=0 i="$10\,\mathrm{A}$" to=p2 id=eV2
#@ el V p1 z0 "$150\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=p1 id=eV1
#@ el V g z0 "$-50\,\mathrm{V}$" col=1 i="$15\,\mathrm{A}$" to=z0 id=eV3
#@ el R o p1 "$10\,\Omega$: falls $50\,\mathrm{V}$" col=2 i="$5\,\mathrm{A}$" to=o id=eR1
#@ el R o p2 "$10\,\Omega$: falls $100\,\mathrm{V}$" col=3 i="$10\,\mathrm{A}$" to=o id=eR2
#@ el R o g2 "$10\,\Omega$: falls $150\,\mathrm{V}$" col=3 i="$15\,\mathrm{A}$" to=g2 id=eR3
#@ step "Ground the lowest wire, the top of $v_3$ ($-50\,\mathrm{V}$). Answers are still read from the bottom wire."
#@ step "In = out at the top wire, all slides equal: $\dfrac{v_1-v_o}{R}+\dfrac{v_2-v_o}{R}+\dfrac{v_3-v_o}{R}=0$, so $v_o=\dfrac{v_1+v_2+v_3}{3}$."
#@ step "$v_o=\dfrac{150+200-50}{3}=100\,\mathrm{V}$: the top wire settles at the **average** height of the three battery tops." show=o
#@ step "Drawn with $R=10\,\Omega$: $5$ and $10\,\mathrm{A}$ slide in from $v_1$ and $v_2$; $15\,\mathrm{A}$ slides down into $v_3$ (that battery absorbs)." show=eR1,eR2,eR3,eV1,eV2,eV3
#@ note "Any $R$ gives the same $v_o$; only the currents change."
```

<details><summary>Solution</summary>

1. In = out at the top wire.

   $$\sum_k\frac{v_k-v_o}{R}=0\;\Rightarrow\;v_o=\frac{v_1+v_2+\cdots+v_n}{n}$$
2. Numbers.

   $$v_o=\frac{150+200-50}{3}=100\,\mathrm{V}$$

**Answer:** $v_o$ is the average; with these values $v_o=100\,\mathrm{V}$.

</details>

**Problem: Try it 6 · Three unknown heights (Textbook P4.11)** (intermediate)

**(a)** Use the node-voltage method to find the branch currents $i_a$ to $i_f$. **(b)** Find the total power developed.

```schematic
V1 0,3 -> 0,0 "$80\,\mathrm{V}$"
R1 0,3 -> 3,3 "$800\,\Omega$" i="$i_b$"
R2 3,3 -> 6,3 "$500\,\Omega$" i="$i_c$"
R3 6,3 -> 9,3 "$2\,\mathrm{k\Omega}$" i="$i_d$"
wire 3,3 -> 3,5
R4 3,5 -> 9,5 "$1\,\mathrm{k\Omega}$" i="$i_a$"
wire 9,5 -> 9,3
R5 6,3 -> 6,0 "$3\,\mathrm{k\Omega}$" i="$i_e$"
R6 9,3 -> 9,0 "$250\,\Omega$" i="$i_f$"
wire 0,0 -> 9,0
label 3,3 "$p$" below
label 6,3 "$q$" above
label 9,3 "$r$" right
ground 0,0
#@ spoiler
#@ straight off
#@ node s 80 "battery top: $80\,\mathrm{V}$"
#@ node p 40 "$p$: $40\,\mathrm{V}$"
#@ node q 30 "$q$: $30\,\mathrm{V}$"
#@ node r 10 "$r$: $10\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$80\,\mathrm{V}$" col=0 i="$50\,\mathrm{mA}$" to=s id=eV1
#@ el R s p "$800\,\Omega$: falls $40\,\mathrm{V}$" col=1 i="$50\,\mathrm{mA}$" to=p id=eR1
#@ el R p q "$500\,\Omega$: falls $10\,\mathrm{V}$" col=2 i="$20\,\mathrm{mA}$" to=q id=eR2
#@ el R q g2 "$3\,\mathrm{k\Omega}$: falls $30\,\mathrm{V}$" col=2 i="$10\,\mathrm{mA}$" to=g2 id=eR5
#@ el R q r "$2\,\mathrm{k\Omega}$: falls $20\,\mathrm{V}$" col=3 i="$10\,\mathrm{mA}$" to=r id=eR3
#@ el R r g3 "$250\,\Omega$: falls $10\,\mathrm{V}$" col=3 i="$40\,\mathrm{mA}$" to=g3 id=eR6
#@ el R p r "$1\,\mathrm{k\Omega}$: falls $30\,\mathrm{V}$" col=4 i="$30\,\mathrm{mA}$" to=r id=eR4
#@ step "Ground the bottom wire. The battery lifts its top to $80\,\mathrm{V}$."
#@ step "Three unknowns: $p$, $q$, $r$. In = out at each (mA, kΩ). $p$: $\dfrac{80-p}{0.8}=\dfrac{p-q}{0.5}+\dfrac{p-r}{1}$. $q$: $\dfrac{p-q}{0.5}=\dfrac{q}{3}+\dfrac{q-r}{2}$. $r$: $\dfrac{p-r}{1}+\dfrac{q-r}{2}=\dfrac{r}{0.25}$."
#@ step "Solve: $p=40$, $q=30$, $r=10\,\mathrm{V}$." show=p,q,r
#@ step "Currents = fall ÷ R: $i_b=50$, $i_c=20$, $i_d=10$, $i_a=30$, $i_e=10$, $i_f=40\,\mathrm{mA}$." show=eR1,eR2,eR3,eR4,eR5,eR6,eV1
#@ step "Power: the battery lifts $50\,\mathrm{mA}$ by $80\,\mathrm{V}$: $4\,\mathrm{W}$, all used by the slides."
```

<details><summary>Solution</summary>

1. In = out at $p$, $q$, $r$ (mA, kΩ).

   $$\begin{aligned}&\tfrac{80-p}{0.8}=\tfrac{p-q}{0.5}+\tfrac{p-r}{1}\\&\tfrac{p-q}{0.5}=\tfrac{q}{3}+\tfrac{q-r}{2}\\&\tfrac{p-r}{1}+\tfrac{q-r}{2}=\tfrac{r}{0.25}\end{aligned}$$
2. Solve.

   $$p=40,\quad q=30,\quad r=10\,\mathrm{V}$$
3. Currents and power.

   $$\begin{aligned}&i_a=30,\;i_b=50,\;i_c=20,\;i_d=10,\;i_e=10,\;i_f=40\,\mathrm{mA}\\&p=80(0.05)=4\,\mathrm{W}\end{aligned}$$

**Answer:** $i_a=30$, $i_b=50$, $i_c=20$, $i_d=10$, $i_e=10$, $i_f=40\,\mathrm{mA}$; $4\,\mathrm{W}$ developed.

</details>

**Problem: Try it 7 · A pump lifts a wire above the battery (Textbook P4.25)** (intermediate)

Use the node-voltage method to find $v_o$.

```schematic
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
R1 0,3 -> 3,3 "$80\,\Omega$"
R2 3,3 -> 3,0 "$50\,\Omega$"
R3 3,3 -> 6,3 "$40\,\Omega$"
I1 6,0 -> 6,3 "$750\,\mathrm{mA}$"
wire 6,3 -> 9,3
R4 9,3 -> 9,0 "$200\,\Omega$"
wire 0,3 -> 0,5
R5 6,5 -> 0,5 "$800\,\Omega$" v="$v_o$"
wire 6,5 -> 6,3
wire 0,0 -> 9,0
label 3,3 "$m$" below
label 6,3 "$r$" below
ground 0,0
#@ spoiler
#@ straight off
#@ node r 53.2 "$r$: $53.2\,\mathrm{V}$"
#@ node s 50 "battery top: $50\,\mathrm{V}$"
#@ node m 34 "$m$: $34\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$50\,\mathrm{V}$" col=0 i="$0.196\,\mathrm{A}$" to=s id=eV1
#@ el R r s "$800\,\Omega$: falls $3.2\,\mathrm{V}$" col=1 i="$0.004\,\mathrm{A}$" to=s id=eR5 plus=r v="$v_o$"
#@ el R s m "$80\,\Omega$: falls $16\,\mathrm{V}$" col=2 i="$0.2\,\mathrm{A}$" to=m id=eR1
#@ el R m g2 "$50\,\Omega$: falls $34\,\mathrm{V}$" col=2 i="$0.68\,\mathrm{A}$" to=g2 id=eR2
#@ el R m r "$40\,\Omega$: falls $19.2\,\mathrm{V}$" col=3 i="$0.48\,\mathrm{A}$" to=m id=eR3
#@ el I g3 r "$0.75\,\mathrm{A}$" col=4 i="$0.75\,\mathrm{A}$" to=r id=eI1
#@ el R r g4 "$200\,\Omega$: falls $53.2\,\mathrm{V}$" col=5 i="$0.266\,\mathrm{A}$" to=g4 id=eR4
#@ step "Ground the bottom wire. The battery lifts its top to $50\,\mathrm{V}$."
#@ step "Unknowns $m$ and $r$. In = out at $m$: $\dfrac{50-m}{80}+\dfrac{r-m}{40}=\dfrac{m}{50}$. At $r$: $0.75=\dfrac{r-m}{40}+\dfrac{r}{200}+\dfrac{r-50}{800}$."
#@ step "Solve: $m=34\,\mathrm{V}$, $r=53.2\,\mathrm{V}$. The pump lifted $r$ above the battery." show=m,r
#@ step "$v_o$ is $r$ measured from the $800\,\Omega$'s left end (the battery top): $v_o=53.2-50=3.2\,\mathrm{V}$. Only $4\,\mathrm{mA}$ trickles back through it." show=eR1,eR2,eR3,eR4,eR5,eV1,eI1
```

<details><summary>Solution</summary>

1. In = out at $m$ and $r$.

   $$\begin{aligned}&\tfrac{50-m}{80}+\tfrac{r-m}{40}=\tfrac{m}{50}\\&0.75=\tfrac{r-m}{40}+\tfrac{r}{200}+\tfrac{r-50}{800}\end{aligned}$$
2. Solve and subtract.

   $$m=34,\quad r=53.2\,\mathrm{V},\qquad v_o=r-50=3.2\,\mathrm{V}$$

**Answer:** $v_o=3.2\,\mathrm{V}$

</details>

**Problem: Try it 8 · A diamond between two unknown wires (Textbook P4.27)** (advanced)

Use the node-voltage method to find $v$.

```schematic
I1 0,0 -> 0,3 "$4.8\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$7.5\,\Omega$" i="$i_x$"
R2 3,3 -> 6,3 "$2.5\,\Omega$"
R3 6,3 -> 6,0 "$10\,\Omega$" v="$v$"
E1 9,3 -> 6,3 "$i_x$"
R4 9,3 -> 9,0 "$2.5\,\Omega$"
R5 9,3 -> 12,3 "$1\,\Omega$"
V1 12,3 -> 12,0 "$12\,\mathrm{V}$"
wire 12,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" above
label 9,3 "$c$" above
ground 0,0
#@ spoiler
#@ straight off
#@ node a 15 "$a$: $15\,\mathrm{V}$"
#@ node d 12 "12 V top: $12\,\mathrm{V}$"
#@ node c 10 "$c$: $10\,\mathrm{V}$"
#@ node b 8 "$b$ ($v$): $8\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ node g5 0 "ground: $0\,\mathrm{V}$" ground
#@ el I g a "$4.8\,\mathrm{A}$" col=0 i="$4.8\,\mathrm{A}$" to=a id=eI1
#@ el R a g2 "$7.5\,\Omega$: falls $15\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=eR1
#@ el R a b "$2.5\,\Omega$: falls $7\,\mathrm{V}$" col=2 i="$2.8\,\mathrm{A}$" to=b id=eR2
#@ el R b g3 "$10\,\Omega$: falls $8\,\mathrm{V}$" col=2 i="$0.8\,\mathrm{A}$" to=g3 id=eR3 plus=b v="$v$"
#@ el E c b "$i_x$: $2\,\mathrm{V}$" col=3 i="$2\,\mathrm{A}$" to=c id=eE1
#@ el R c g4 "$2.5\,\Omega$: falls $10\,\mathrm{V}$" col=4 i="$4\,\mathrm{A}$" to=g4 id=eR4
#@ el R c d "$1\,\Omega$: falls $2\,\mathrm{V}$" col=5 i="$2\,\mathrm{A}$" to=c id=eR5
#@ el V d g5 "$12\,\mathrm{V}$" col=6 i="$2\,\mathrm{A}$" to=d id=eV1
#@ step "Ground the bottom wire. The $12\,\mathrm{V}$ battery lifts its top to $12\,\mathrm{V}$."
#@ step "The diamond sits between $b$ and $c$: it locks $c=v+i_x$ (it is $1\,\Omega\times i_x$ volts). It depends on $i_x=\dfrac{a}{7.5}$, the current down the $7.5\,\Omega$."
#@ step "In = out at $a$: $4.8=\dfrac{a}{7.5}+\dfrac{a-v}{2.5}$. Bubble around $b$ and $c$: $\dfrac{a-v}{2.5}+\dfrac{12-c}{1}=\dfrac{v}{10}+\dfrac{c}{2.5}$. Solve: $a=15$, $v=8$, $c=10\,\mathrm{V}$." show=a,b,c,eE1
#@ step "Currents: $i_x=2\,\mathrm{A}$, $2.8\,\mathrm{A}$ from $a$ to $b$, $0.8\,\mathrm{A}$ down the $10\,\Omega$, $4\,\mathrm{A}$ down the $2.5\,\Omega$ at $c$, $2\,\mathrm{A}$ into $c$ from the $12\,\mathrm{V}$ side." show=eR1,eR2,eR3,eR4,eR5,eV1,eI1
```

<details><summary>Solution</summary>

1. Ground the bottom wire. $b$ and $c$ form a supernode (the diamond joins them). Control: $i_x$ runs down the $7.5\,\Omega$.

   $$i_x=\frac{v_a}{7.5},\qquad v_c-v=(1\,\Omega)\,i_x$$
2. KCL at $a$ (the $4.8\,\mathrm{A}$ comes in).

   $$\frac{v_a}{7.5}+\frac{v_a-v}{2.5}=4.8\;\Rightarrow\;v_a=9+0.75v$$
3. So the rod is

   $$v_c=v+\frac{v_a}{7.5}=1.1v+1.2$$
4. KCL around the rod.

   $$\frac{v-v_a}{2.5}+\frac{v}{10}+\frac{v_c}{2.5}+\frac{v_c-12}{1}=0$$
5. Substitute and solve.

   $$1.74v-13.92=0\;\Rightarrow\;v=8\,\mathrm{V},\quad v_a=15\,\mathrm{V},\quad v_c=10\,\mathrm{V}$$

**Answer:** $v=8\,\mathrm{V}$ (with $v_a=15\,\mathrm{V}$, $v_c=10\,\mathrm{V}$, $i_x=2\,\mathrm{A}$)

</details>

**Problem: Try it 9 · A diamond hanging from a battery (Assessment AP 4.6)** (advanced)

Use the node-voltage method to find $v_1$ and $i_\phi$.

```schematic
V1 0,3 -> 0,0 "$60\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$24\,\Omega$"
R3 6,3 -> 3,3 "$3\,\Omega$" i="$i_\phi$"
R4 6,3 -> 6,0 "$3\,\Omega$"
wire 0,3 -> 0,5
E1 6,5 -> 0,5 "$6i_\phi$"
wire 6,5 -> 6,3
wire 6,0 -> 0,0
label 3,3 "$v_1$" above
ground 0,0
#@ spoiler
#@ straight off
#@ node s 60 "battery top: $60\,\mathrm{V}$"
#@ node n1 48 "$v_1$: $48\,\mathrm{V}$"
#@ node r 36 "right wire: $36\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$60\,\mathrm{V}$" col=0 i="$14\,\mathrm{A}$" to=s id=eV1
#@ el R s n1 "$2\,\Omega$: falls $12\,\mathrm{V}$" col=1 i="$6\,\mathrm{A}$" to=n1 id=eR1
#@ el R n1 g2 "$24\,\Omega$: falls $48\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=eR2
#@ el R r n1 "$3\,\Omega$: falls $12\,\mathrm{V}$" col=2 i="$4\,\mathrm{A}$" to=r id=eR3
#@ el E r s "$6i_\phi$: $-24\,\mathrm{V}$" col=3 i="$8\,\mathrm{A}$" to=r id=eE1
#@ el R r g3 "$3\,\Omega$: falls $36\,\mathrm{V}$" col=3 i="$12\,\mathrm{A}$" to=g3 id=eR4
#@ step "Ground the bottom wire. The $60\,\mathrm{V}$ battery lifts the left wire to $60\,\mathrm{V}$."
#@ step "The diamond hangs from that wire: the right wire is $6i_\phi$ above it (below it if $i_\phi$ is negative). $i_\phi$ is the current from the right wire to $v_1$ through $3\,\Omega$."
#@ step "In = out at $v_1$, with the right wire at $60+6i_\phi$ and $i_\phi=\dfrac{60+6i_\phi-v_1}{3}$: $i_\phi=-4\,\mathrm{A}$, $v_1=48\,\mathrm{V}$, right wire $36\,\mathrm{V}$." show=n1,r,eE1
#@ step "Negative $i_\phi$: $4\,\mathrm{A}$ really flows from $v_1$ to the right wire. The diamond steps **down** $24\,\mathrm{V}$ and $8\,\mathrm{A}$ falls through it (it absorbs $192\,\mathrm{W}$)." show=eR1,eR2,eR3,eR4,eV1
```

<details><summary>Solution</summary>

1. Ground the bottom wire. The right node is the $60\,\mathrm{V}$ node plus the diamond's step.

   $$v_r=60+6i_\phi$$
2. KCL at $v_1$.

   $$\frac{v_1-60}{2}+\frac{v_1}{24}+\frac{v_1-(60+6i_\phi)}{3}=0$$
3. Control: $i_\phi$ flows from the right node to $v_1$.

   $$i_\phi=\frac{60+6i_\phi-v_1}{3}\;\Rightarrow\;v_1=60+3i_\phi$$
4. Substitute and solve.

   $$i_\phi=-4\,\mathrm{A},\qquad v_1=48\,\mathrm{V}$$

**Answer:** $v_1=48\,\mathrm{V}$, $i_\phi=-4\,\mathrm{A}$

</details>

## Topic 2: Mesh currents are loop walks

> **Tip:** **How it looks in heights.**
> 
> - Give each window of the circuit a **loop current** (clockwise). Walk around each window: **climbs = falls**.
> - A resistor shared by two windows carries the **difference** of their loop currents.
> - A pump on a window's **outside edge** gives that loop current for free. A pump **between** two windows: walk around both windows as one big loop, skipping the pump (a *supermesh*), and add *difference of the two loop currents = pump current*.
> - Loop currents are bookkeeping. Turn them into real currents, then place the heights by walking down the slides.

**Example: Example 11 · One window**

Find the loop current and the height of $x$.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$"
wire 3,0 -> 0,0
label 3,3 "$x$" above
ground 0,0
#@ inline
#@ straight off
#@ node s 12 "battery top: $12\,\mathrm{V}$"
#@ node x 8 "$x$: $8\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$12\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=s id=eV1
#@ el R s x "$2\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=x id=eR1
#@ el R x g2 "$4\,\Omega$: falls $8\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=eR2
#@ step "Ground the bottom wire. One window, one loop current $I$ (clockwise)."
#@ step "Walk around: climb $12\,\mathrm{V}$ through the battery, fall $2I$ and $4I$ through the slides. Climbs = falls: $12=6I$, so $I=2\,\mathrm{A}$." show=eR1,eR2,eV1
#@ step "Place heights by walking down: $x=12-(2)(2)=8\,\mathrm{V}$. That is the whole mesh method: one loop walk per window." show=x
```

1. Loop walk.

   $$12=2I+4I\;\Rightarrow\;I=2\,\mathrm{A},\qquad x=4I=8\,\mathrm{V}$$

**Answer:** $I=2\,\mathrm{A}$, $x=8\,\mathrm{V}$

**Example: Example 12 · Two windows (same answer as node voltages)**

Find the loop currents and the height of $x$.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$"
R3 3,3 -> 6,3 "$2\,\Omega$"
V2 6,3 -> 6,0 "$6\,\mathrm{V}$"
wire 6,0 -> 0,0
label 3,3 "$x$" above
ground 0,0
#@ inline
#@ straight off
#@ node s 12 "left top: $12\,\mathrm{V}$"
#@ node x 7.2 "$x$: $7.2\,\mathrm{V}$"
#@ node r 6 "right top: $6\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$12\,\mathrm{V}$" col=0 i="$2.4\,\mathrm{A}$" to=s id=eV1
#@ el R s x "$2\,\Omega$: falls $4.8\,\mathrm{V}$" col=1 i="$2.4\,\mathrm{A}$" to=x id=eR1
#@ el R x g2 "$4\,\Omega$: falls $7.2\,\mathrm{V}$" col=1 i="$1.8\,\mathrm{A}$" to=g2 id=eR2
#@ el R x r "$2\,\Omega$: falls $1.2\,\mathrm{V}$" col=2 i="$0.6\,\mathrm{A}$" to=r id=eR3
#@ el V r g3 "$6\,\mathrm{V}$" col=2 i="$0.6\,\mathrm{A}$" to=g3 id=eV2
#@ step "Ground the bottom wire. Battery tops: $12\,\mathrm{V}$ (left) and $6\,\mathrm{V}$ (right)."
#@ step "Loop currents $I_1$ (left window) and $I_2$ (right), both clockwise. The middle $4\,\Omega$ is shared: it carries $I_1-I_2$."
#@ step "Left walk: $12=2I_1+4(I_1-I_2)$. Right walk: $0=4(I_2-I_1)+2I_2+6$ (walking down through the $6\,\mathrm{V}$ battery is a fall). So $I_1=2.4$, $I_2=0.6\,\mathrm{A}$."
#@ step "Real currents: $2.4\,\mathrm{A}$ in, $1.8\,\mathrm{A}$ down the middle, $0.6\,\mathrm{A}$ into the $6\,\mathrm{V}$ battery. Height: $x=(1.8)(4)=7.2\,\mathrm{V}$. In = out at $x$ (Topic 1) gives the same $7.2\,\mathrm{V}$." show=x,eR1,eR2,eR3,eV1,eV2
```

1. Two loop walks.

   $$6I_1-4I_2=12,\qquad -4I_1+6I_2=-6\;\Rightarrow\;I_1=2.4\,\mathrm{A},\;I_2=0.6\,\mathrm{A}$$
2. Height.

   $$x=4(I_1-I_2)=7.2\,\mathrm{V}$$

**Answer:** $I_1=2.4\,\mathrm{A}$, $I_2=0.6\,\mathrm{A}$, $x=7.2\,\mathrm{V}$

**Example: Example 13 · A pump on the outside edge**

Find both loop currents and the heights of $m$ and $r$.

```schematic
V1 0,3 -> 0,0 "$20\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
R2 3,3 -> 3,0 "$6\,\Omega$"
R3 3,3 -> 6,3 "$3\,\Omega$"
I1 6,3 -> 6,0 "$2\,\mathrm{A}$"
wire 6,0 -> 0,0
label 3,3 "$m$" above
label 6,3 "$r$" above
ground 0,0
#@ inline
#@ straight off
#@ node s 20 "battery top: $20\,\mathrm{V}$"
#@ node m 7.2 "$m$: $7.2\,\mathrm{V}$"
#@ node r 1.2 "$r$: $1.2\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$20\,\mathrm{V}$" col=0 i="$3.2\,\mathrm{A}$" to=s id=eV1
#@ el R s m "$4\,\Omega$: falls $12.8\,\mathrm{V}$" col=1 i="$3.2\,\mathrm{A}$" to=m id=eR1
#@ el R m g2 "$6\,\Omega$: falls $7.2\,\mathrm{V}$" col=1 i="$1.2\,\mathrm{A}$" to=g2 id=eR2
#@ el R m r "$3\,\Omega$: falls $6\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=r id=eR3
#@ el I r g3 "$2\,\mathrm{A}$" col=2 i="$2\,\mathrm{A}$" to=g3 id=eI1
#@ step "Ground the bottom wire. The battery lifts the left top to $20\,\mathrm{V}$."
#@ step "The $2\,\mathrm{A}$ pump is on the right window's outside edge, pointing the same way as the clockwise loop. So $I_2=2\,\mathrm{A}$: no equation needed." show=eI1
#@ step "Only the left walk is left: $20=4I_1+6(I_1-2)$, so $I_1=3.2\,\mathrm{A}$." show=eR1
#@ step "Heights: $m=20-(3.2)(4)=7.2\,\mathrm{V}$; the $6\,\Omega$ carries $1.2\,\mathrm{A}$ down ($7.2\,\mathrm{V}$ ✓); $r=7.2-(2)(3)=1.2\,\mathrm{V}$." show=m,r,eR2,eR3,eV1
#@ step "The pump carries $2\,\mathrm{A}$ **down** from $1.2\,\mathrm{V}$ to $0$: it absorbs $2.4\,\mathrm{W}$."
```

1. The pump fixes the right loop.

   $$I_2=2\,\mathrm{A}$$
2. Left loop walk.

   $$20=4I_1+6(I_1-2)\;\Rightarrow\;I_1=3.2\,\mathrm{A}$$
3. Heights.

   $$m=6(3.2-2)=7.2\,\mathrm{V},\qquad r=7.2-3(2)=1.2\,\mathrm{V}$$

**Answer:** $I_1=3.2\,\mathrm{A}$, $I_2=2\,\mathrm{A}$; $m=7.2\,\mathrm{V}$, $r=1.2\,\mathrm{V}$

**Example: Example 14 · Three windows (Lecture 3)**

Use the mesh-current method to find **(a)** the power of each voltage source and **(b)** $v_o$.

```schematic
V1 0,3 -> 0,0 "$40\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$8\,\Omega$" v="$v_o$"
R3 3,3 -> 6,3 "$6\,\Omega$"
R4 6,3 -> 6,0 "$6\,\Omega$"
R5 6,3 -> 9,3 "$4\,\Omega$"
V2 9,3 -> 9,0 "$20\,\mathrm{V}$"
wire 9,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" above
ground 0,0
#@ inline
#@ straight off
#@ node s 40 "40 V top: $40\,\mathrm{V}$"
#@ node a 28.8 "$a$: $28.8\,\mathrm{V}$"
#@ node c 20 "20 V top: $20\,\mathrm{V}$"
#@ node b 16.8 "$b$: $16.8\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$40\,\mathrm{V}$" col=0 i="$5.6\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$2\,\Omega$: falls $11.2\,\mathrm{V}$" col=1 i="$5.6\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$8\,\Omega$: falls $28.8\,\mathrm{V}$" col=1 i="$3.6\,\mathrm{A}$" to=g2 id=eR2 plus=a v="$v_o$"
#@ el R a b "$6\,\Omega$: falls $12\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=b id=eR3
#@ el R b g3 "$6\,\Omega$: falls $16.8\,\mathrm{V}$" col=2 i="$2.8\,\mathrm{A}$" to=g3 id=eR4
#@ el R b c "$4\,\Omega$: falls $3.2\,\mathrm{V}$" col=3 i="$0.8\,\mathrm{A}$" to=b id=eR5
#@ el V c g4 "$20\,\mathrm{V}$" col=4 i="$0.8\,\mathrm{A}$" to=c id=eV2
#@ step "Ground the bottom wire. Battery tops: $40\,\mathrm{V}$ and $20\,\mathrm{V}$."
#@ step "Three clockwise loop currents. One walk per window: $10I_1-8I_2=40$, $-8I_1+20I_2-6I_3=0$, $-6I_2+10I_3=-20$."
#@ step "Solve: $I_1=5.6$, $I_2=2$, $I_3=-0.8\,\mathrm{A}$. Real currents: $5.6\,\mathrm{A}$ in the $2\,\Omega$, $3.6\,\mathrm{A}$ down the $8\,\Omega$, $2\,\mathrm{A}$ across, $2.8\,\mathrm{A}$ down the right $6\,\Omega$, $0.8\,\mathrm{A}$ leftward in the $4\,\Omega$." show=eR1,eR2,eR3,eR4,eR5,eV1,eV2
#@ step "Walk down from $40\,\mathrm{V}$: $a=40-(5.6)(2)=28.8\,\mathrm{V}=v_o$, $b=28.8-(2)(6)=16.8\,\mathrm{V}$. From the right: $20-(0.8)(4)=16.8$ ✓" show=a,b
#@ step "Both batteries climb: they deliver $224\,\mathrm{W}$ and $16\,\mathrm{W}$."
```

1. KVL around each mesh, clockwise. Shared resistors carry differences; walking down through the $20\,\mathrm{V}$ source is a fall.

   $$\begin{aligned}&-40+2I_1+8(I_1-I_2)=0\\&8(I_2-I_1)+6I_2+6(I_2-I_3)=0\\&6(I_3-I_2)+4I_3+20=0\end{aligned}$$
2. Collect.

   $$\begin{aligned}10I_1-8I_2&=40\\-8I_1+20I_2-6I_3&=0\\-6I_2+10I_3&=-20\end{aligned}$$
3. Solve.

   $$I_1=5.6\,\mathrm{A},\quad I_2=2\,\mathrm{A},\quad I_3=-0.8\,\mathrm{A}$$
4. **(b)** The $8\,\Omega$ carries $I_1-I_2$.

   $$v_o=8(5.6-2)=28.8\,\mathrm{V}$$
5. **(a)** Absorbed power uses the current entering $+$. Negative = delivering.

   $$p_{40\mathrm{V}}=-40(5.6)=-224\,\mathrm{W},\qquad p_{20\mathrm{V}}=20(-0.8)=-16\,\mathrm{W}$$

**Answer:** **(a)** The $40\,\mathrm{V}$ source delivers $224\,\mathrm{W}$; the $20\,\mathrm{V}$ source delivers $16\,\mathrm{W}$. **(b)** $v_o=28.8\,\mathrm{V}$

**Example: Example 15 · A pump between two windows: walk around both (Assessment AP 4.12)**

Use the mesh-current method to find the power dissipated in the $1\,\Omega$ resistor. Mesh $a$ is lower-left, $b$ the top, $c$ lower-right (all clockwise).

```schematic
V1 0,3 -> 0,0 "$10\,\mathrm{V}$"
I1 0,3 -> 3,3 "$2\,\mathrm{A}$"
wire 0,3 -> 0,6
R1 0,6 -> 6,6 "$2\,\Omega$"
wire 6,6 -> 6,3
R2 3,3 -> 6,3 "$2\,\Omega$"
R3 3,3 -> 3,0 "$2\,\Omega$"
V2 6,0 -> 6,3 "$6\,\mathrm{V}$"
R4 6,0 -> 3,0 "$1\,\Omega$"
wire 3,0 -> 0,0
label 3,3 "$m$" above
label 6,3 "$r$" right
label 6,0 "$q$" right
ground 0,0
#@ inline
#@ straight off
#@ node s 10 "battery top: $10\,\mathrm{V}$"
#@ node q 6 "$q$: $6\,\mathrm{V}$"
#@ node m 2 "$m$: $2\,\mathrm{V}$"
#@ node r 0 "$r$ = ground: $0\,\mathrm{V}$"
#@ node g 0 "$r$ = ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "$r$ = ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "$r$ = ground: $0\,\mathrm{V}$" ground
#@ el V s g "$10\,\mathrm{V}$" col=0 i="$7\,\mathrm{A}$" to=s id=eV1
#@ el R s r "$2\,\Omega$: falls $10\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=r id=eR1
#@ el I s m "$2\,\mathrm{A}$" col=2 i="$2\,\mathrm{A}$" to=m id=eI1
#@ el R m g2 "$2\,\Omega$: falls $2\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=g2 id=eR3
#@ el R m r "$2\,\Omega$: falls $2\,\mathrm{V}$" col=3 i="$1\,\mathrm{A}$" to=r id=eR2
#@ el V q r "$6\,\mathrm{V}$" col=4 i="$6\,\mathrm{A}$" to=q id=eV2
#@ el R q g3 "$1\,\Omega$: falls $6\,\mathrm{V}$" col=5 i="$6\,\mathrm{A}$" to=g3 id=eR4
#@ step "Ground the bottom wire. The $10\,\mathrm{V}$ battery lifts its top to $10\,\mathrm{V}$."
#@ step "The $2\,\mathrm{A}$ pump sits between windows $a$ and $b$: $I_a-I_b=2$. Its height change is unknown, so walk around $a$ and $b$ together, skipping it: $-10+2I_b+2(I_b-I_c)+2(I_a-I_c)=0$."
#@ step "Window $c$: $-6+I_c+2(I_c-I_a)+2(I_c-I_b)=0$. Solve: $I_a=7$, $I_b=5$, $I_c=6\,\mathrm{A}$."
#@ step "Real currents → heights: $5\,\mathrm{A}$ down the top $2\,\Omega$ to $r$ ($0\,\mathrm{V}$); $m=2\,\mathrm{V}$; $q=6\,\mathrm{V}$ above the $1\,\Omega$, which carries $6\,\mathrm{A}$: $36\,\mathrm{W}$." show=m,q,r,eR1,eR2,eR3,eR4,eV1,eV2
#@ step "The pump carries $2\,\mathrm{A}$ **down** from $10\,\mathrm{V}$ to $2\,\mathrm{V}$: it absorbs $16\,\mathrm{W}$." show=eI1
```

1. The $2\,\mathrm{A}$ source is shared by meshes $a$ and $b$.

   $$I_a-I_b=2$$
2. KVL around the supermesh (skip the source branch).

   $$-10+2I_b+2(I_b-I_c)+2(I_a-I_c)=0$$
3. KVL around mesh $c$.

   $$-6+I_c+2(I_c-I_a)+2(I_c-I_b)=0$$
4. Solve the three equations.

   $$I_a=7\,\mathrm{A},\quad I_b=5\,\mathrm{A},\quad I_c=6\,\mathrm{A}$$
5. The $1\,\Omega$ is only in mesh $c$.

   $$p_{1\Omega}=I_c^2(1)=36\,\mathrm{W}$$

**Answer:** $I_a=7\,\mathrm{A}$, $I_b=5\,\mathrm{A}$, $I_c=6\,\mathrm{A}$; $p_{1\Omega}=36\,\mathrm{W}$

**Example: Example 16 · A diamond in a window (Lecture 3)**

Use the mesh-current method to find the power dissipated in the $4\,\Omega$ resistor. Mesh $a$ is lower-left, $b$ the top triangle, $c$ lower-right (all clockwise).

```schematic
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$"
R2 3,3 -> 6,3 "$4\,\Omega$"
R3 3,3 -> 3,0 "$20\,\Omega$" i="$i_\phi$"
E1 6,3 -> 6,0 "$15i_\phi$"
wire 0,3 -> 0,5
R4 0,5 -> 6,5 "$1\,\Omega$"
wire 6,5 -> 6,3
wire 6,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$b$" right
ground 0,0
#@ inline
#@ straight off
#@ node s 50 "battery top: $50\,\mathrm{V}$"
#@ node a 32 "$a$: $32\,\mathrm{V}$"
#@ node b 24 "$b$: $24\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$50\,\mathrm{V}$" col=0 i="$29.6\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$5\,\Omega$: falls $18\,\mathrm{V}$" col=1 i="$3.6\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$20\,\Omega$: falls $32\,\mathrm{V}$" col=1 i="$1.6\,\mathrm{A}$" to=g2 id=eR3
#@ el R a b "$4\,\Omega$: falls $8\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=b id=eR2
#@ el E b g3 "$15i_\phi$: $24\,\mathrm{V}$" col=2 i="$28\,\mathrm{A}$" to=g3 id=eE1
#@ el R s b "$1\,\Omega$: falls $26\,\mathrm{V}$" col=3 i="$26\,\mathrm{A}$" to=b id=eR4
#@ step "Ground the bottom wire. The battery lifts its top to $50\,\mathrm{V}$."
#@ step "The diamond is a battery of $15i_\phi$. It depends on $i_\phi$, the current down the $20\,\Omega$: $i_\phi=I_a-I_c$ (two windows share it)."
#@ step "Three loop walks with that control: $I_a=29.6$, $I_b=26$, $I_c=28\,\mathrm{A}$, so $i_\phi=1.6\,\mathrm{A}$."
#@ step "Heights: $a=20i_\phi=32\,\mathrm{V}$, the diamond's top $b=15i_\phi=24\,\mathrm{V}$. The $4\,\Omega$ falls $8\,\mathrm{V}$ with $2\,\mathrm{A}$: $16\,\mathrm{W}$." show=a,b,eR1,eR2,eR3,eR4,eV1,eE1
```

1. Control first: both lower meshes cross the $20\,\Omega$.

   $$i_\phi=I_a-I_c$$
2. Loop walks.

   $$\begin{aligned}&-50+5(I_a-I_b)+20(I_a-I_c)=0\\&I_b+4(I_b-I_c)+5(I_b-I_a)=0\\&15i_\phi+20(I_c-I_a)+4(I_c-I_b)=0\end{aligned}$$
3. Substitute the control and collect.

   $$\begin{aligned}25I_a-5I_b-20I_c&=50\\-5I_a+10I_b-4I_c&=0\\-5I_a-4I_b+9I_c&=0\end{aligned}$$
4. Solve.

   $$I_a=29.6\,\mathrm{A},\quad I_b=26\,\mathrm{A},\quad I_c=28\,\mathrm{A},\quad i_\phi=1.6\,\mathrm{A}$$
5. The $4\,\Omega$ carries $I_c-I_b$.

   $$p_{4\Omega}=4(28-26)^2=16\,\mathrm{W}$$

**Answer:** $i_\phi=1.6\,\mathrm{A}$; $p_{4\Omega}=16\,\mathrm{W}$

**Example: Example 17 · Count the unknowns before you start (Lecture 3)**

Count the nodes, essential nodes, branches, essential branches and meshes.

```schematic
V1 0,6 -> 0,3 "$v_1$"
V2 0,3 -> 0,0 "$v_2$"
R1 0,6 -> 4,6 "$R_1$"
R5 4,6 -> 4,3 "$R_5$"
R2 0,3 -> 2,3 "$R_2$"
R3 2,3 -> 4,3 "$R_3$"
R6 4,3 -> 4,0 "$R_6$"
R4 0,0 -> 4,0 "$R_4$"
wire 4,6 -> 9,6
wire 4,0 -> 9,0
R7 6.5,6 -> 6.5,0 "$R_7$"
I1 9,0 -> 9,6 "$I$"
label 0,6 "$a$" left
label 4,6 "$b$" above
label 0,3 "$c$" left
label 2,3 "$d$" above
label 4,3 "$e$" right
label 0,0 "$f$" left
label 4,0 "$g$" below
```

1. Nodes $a$–$g$; ten elements, so ten branches.

   $$n=7,\qquad b=10$$
2. Essential nodes meet three or more elements: $b$, $c$, $e$, $g$. ($a$, $d$, $f$ only join two.)

   $$n_e=4$$
3. Essential branches: $c$–$a$–$b$, $c$–$f$–$g$, $c$–$d$–$e$, $b$–$e$, $e$–$g$, and the two $b$–$g$ paths ($R_7$ and $I$).

   $$b_e=7$$
4. Meshes, checked both ways.

   $$M=10-7+1=7-4+1=4$$

**Answer:** $7$ nodes, $4$ essential nodes, $10$ branches, $7$ essential branches, $4$ meshes. Node-voltage would need $4-1=3$ unknown heights. **So:** node voltages need $n_e-1$ equations, mesh currents need $b_e-n_e+1$.

> **Warning:** **Loop-walk traps.** Through a battery from $-$ to $+$ is a **climb**; $+$ to $-$ is a **fall**. A shared resistor carries a **difference** of loop currents. A pump's height change is unknown: never write $R\times I$ for it (that is why you walk around it).

**Problem: Try it 10 · Count everything (Textbook P4.1)** (introductory)

Find the number of **(a)** branches, **(b)** branches with unknown current, **(c)** essential branches, **(d)** essential branches with unknown current, **(e)** nodes, **(f)** essential nodes, **(g)** meshes.

```schematic
V1 0,4 -> 0,0 "$18\,\mathrm{V}$"
wire 0,4 -> 0,7
R1 0,7 -> 10,7 "$R_1$"
wire 10,7 -> 10,4
R2 0,6 -> 3,6 "$R_2$" i_rev="$i_\Delta$"
R3 0,4 -> 3,4 "$R_3$"
wire 3,6 -> 3,4
G1 3,6 -> 10,6 "$2v_\Delta$"
R6 3,4 -> 3,0 "$R_6$" v="$v_\Delta$"
R4 3,4 -> 6,4 "$R_4$"
R5 6,4 -> 10,4 "$R_5$"
E1 6,4 -> 6,0 "$25i_\Delta$"
R7 10,4 -> 10,0 "$R_7$"
wire 10,4 -> 13,4
I1 13,0 -> 13,4 "$5\,\mathrm{mA}$"
wire 13,0 -> 0,0
label 0,4 "$a$" left
label 3,6 "$b$" above
label 6,4 "$c$" above
label 10,7 "$d$" right
label 13,0 "$e$" right
```

<details><summary>Solution</summary>

1. Branches: seven resistors and four sources.

   $$b=11$$
2. Only the $5\,\mathrm{mA}$ source has a known current; the diamond $2v_\Delta$ depends on an unknown, so it does not count as known.

   $$b_{\text{unknown}}=10$$
3. Nodes: $a$ (top-left wire), $b$, $c$, $d$ and the bottom wire $e$. Each joins at least three elements.

   $$n=n_e=5$$
4. Every branch runs between essential nodes, so every branch is essential.

   $$b_e=11,\quad b_{e,\text{unknown}}=10$$
5. Meshes.

   $$M=b-n+1=11-5+1=7$$

**Answer:** **(a)** $11$ **(b)** $10$ **(c)** $11$ **(d)** $10$ **(e)** $5$ **(f)** $5$ **(g)** $7$

</details>

**Problem: Try it 11 · A pump on the outside edge (Assessment AP 4.10)** (intermediate)

Use the mesh-current method to find the power dissipated in the $2\,\Omega$ resistor.

```schematic
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
R1 0,3 -> 3,3 "$3\,\Omega$"
R2 0,0 -> 3,0 "$6\,\Omega$"
R3 3,3 -> 3,0 "$2\,\Omega$"
R4 3,3 -> 6,3 "$8\,\Omega$"
R5 3,0 -> 6,0 "$4\,\Omega$"
R6 6,3 -> 6,0 "$5\,\Omega$"
wire 6,3 -> 9,3
I1 9,0 -> 9,3 "$16\,\mathrm{A}$"
wire 9,0 -> 6,0
ground 0,0
#@ spoiler
#@ straight off
#@ node r 60 "top right: $60\,\mathrm{V}$"
#@ node s 34 "battery top: $34\,\mathrm{V}$"
#@ node m 28 "top middle: $28\,\mathrm{V}$"
#@ node q 16 "bottom middle: $16\,\mathrm{V}$"
#@ node z0 4 "bottom-left: $4\,\mathrm{V}$"
#@ node g 0 "bottom right: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom right: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom right: $0\,\mathrm{V}$" ground
#@ el V s z0 "$30\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=s id=eV1
#@ el R s m "$3\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=m id=eR1
#@ el R m q "$2\,\Omega$: falls $12\,\mathrm{V}$" col=1 i="$6\,\mathrm{A}$" to=q id=eR3
#@ el R z0 q "$6\,\Omega$: falls $12\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=z0 id=eR2
#@ el R m r "$8\,\Omega$: falls $32\,\mathrm{V}$" col=2 i="$4\,\mathrm{A}$" to=m id=eR4
#@ el R q g "$4\,\Omega$: falls $16\,\mathrm{V}$" col=2 i="$4\,\mathrm{A}$" to=g id=eR5
#@ el R r g2 "$5\,\Omega$: falls $60\,\mathrm{V}$" col=3 i="$12\,\mathrm{A}$" to=g2 id=eR6
#@ el I g3 r "$16\,\mathrm{A}$" col=4 i="$16\,\mathrm{A}$" to=r id=eI1
#@ step "Ground the bottom-right wire, the lowest. Heights are measured from it (the bottom-left wire sits $4\,\mathrm{V}$ up)."
#@ step "The $16\,\mathrm{A}$ pump is on mesh 3's outside edge, pointing **against** clockwise: $I_3=-16\,\mathrm{A}$." show=eI1
#@ step "Walk meshes 1 and 2: $11I_1-2I_2=30$ and $-2I_1+19I_2=-80$, so $I_1=2$, $I_2=-4\,\mathrm{A}$."
#@ step "The $2\,\Omega$ carries $I_1-I_2=6\,\mathrm{A}$: $6^2\times2=72\,\mathrm{W}$." show=eR3
#@ step "All real currents → heights. The pump lifts $16\,\mathrm{A}$ by $60\,\mathrm{V}$: the big climb in this circuit." show=s,m,q,r,eR1,eR2,eR4,eR5,eR6,eV1
```

<details><summary>Solution</summary>

1. The perimeter source fixes mesh 3: clockwise $I_3$ opposes its upward arrow.

   $$I_3=-16\,\mathrm{A}$$
2. KVL in mesh 1.

   $$-30+3I_1+2(I_1-I_2)+6I_1=0\;\Rightarrow\;11I_1-2I_2=30$$
3. KVL in mesh 2.

   $$8I_2+5(I_2-I_3)+4I_2+2(I_2-I_1)=0\;\Rightarrow\;-2I_1+19I_2=-80$$
4. Solve.

   $$I_1=2\,\mathrm{A},\qquad I_2=-4\,\mathrm{A}$$
5. The $2\,\Omega$ carries $I_1-I_2$ downward.

   $$p_{2\Omega}=(6)^2(2)=72\,\mathrm{W}$$

**Answer:** $p_{2\Omega}=72\,\mathrm{W}$

</details>

**Problem: Try it 12 · Flip one battery (Textbook P4.37)** (intermediate)

**(a)** Use the mesh-current method to find $i_a$, $i_b$ and $i_c$. **(b)** Repeat with the polarity of the $64\,\mathrm{V}$ source reversed.

```schematic
V1 0,3 -> 0,0 "$40\,\mathrm{V}$"
R1 0,3 -> 3,3 "$3\,\Omega$" i="$i_a$"
R2 0,0 -> 3,0 "$2\,\Omega$"
R3 3,3 -> 3,0 "$45\,\Omega$" i="$i_b$"
R4 6,3 -> 3,3 "$4\,\Omega$" i="$i_c$"
R5 3,0 -> 6,0 "$1.5\,\Omega$"
V2 6,0 -> 6,3 "$64\,\mathrm{V}$"
ground 0,0
#@ spoiler
#@ view "As drawn"
#@ straight off
#@ node s 69.4 "battery top: $69.4\,\mathrm{V}$"
#@ node p 64 "bottom right: $64\,\mathrm{V}$"
#@ node q 49 "bottom middle: $49\,\mathrm{V}$"
#@ node m 40 "top middle: $40\,\mathrm{V}$"
#@ node z0 29.4 "bottom-left: $29.4\,\mathrm{V}$"
#@ node g 0 "top right: $0\,\mathrm{V}$" ground
#@ node g2 0 "top right: $0\,\mathrm{V}$" ground
#@ el V s z0 "$40\,\mathrm{V}$" col=0 i="$9.8\,\mathrm{A}$" to=s id=eV1
#@ el R s m "$3\,\Omega$: falls $29.4\,\mathrm{V}$" col=1 i="$9.8\,\mathrm{A}$" to=m id=eR1
#@ el R g m "$4\,\Omega$: falls $40\,\mathrm{V}$" col=1 i="$10\,\mathrm{A}$" to=g id=eR4
#@ el R q p "$1.5\,\Omega$: falls $15\,\mathrm{V}$" col=2 i="$10\,\mathrm{A}$" to=q id=eR5
#@ el R m q "$45\,\Omega$: falls $9\,\mathrm{V}$" col=2 i="$0.2\,\mathrm{A}$" to=m id=eR3
#@ el R z0 q "$2\,\Omega$: falls $19.6\,\mathrm{V}$" col=3 i="$9.8\,\mathrm{A}$" to=z0 id=eR2
#@ el V p g2 "$64\,\mathrm{V}$" col=4 i="$10\,\mathrm{A}$" to=p id=eV2
#@ step "Ground the lowest wire, the $64\,\mathrm{V}$ battery's $-$ end. Answers don't change."
#@ step "Loop currents $I_L$, $I_R$ (clockwise): $i_a=I_L$, $i_b=I_L-I_R$, $i_c=-I_R$. Walks: $50I_L-45I_R=40$ and $-45I_L+50.5I_R=64$, so $I_L=9.8$, $I_R=10\,\mathrm{A}$."
#@ step "So $i_a=9.8\,\mathrm{A}$, $i_b=-0.2\,\mathrm{A}$ ($0.2\,\mathrm{A}$ goes **up** the $45\,\Omega$), $i_c=-10\,\mathrm{A}$." show=eR1,eR2,eR3,eR4,eR5,eV1,eV2
#@ view "64 V flipped"
#@ straight off
#@ node r 64 "top right: $64\,\mathrm{V}$"
#@ node m 52.8 "top middle: $52.8\,\mathrm{V}$"
#@ node s 47.64 "battery top: $47.64\,\mathrm{V}$"
#@ node z0 7.64 "bottom-left: $7.64\,\mathrm{V}$"
#@ node q 4.2 "bottom middle: $4.2\,\mathrm{V}$"
#@ node g 0 "bottom right: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom right: $0\,\mathrm{V}$" ground
#@ el V r g "$64\,\mathrm{V}$" col=0 i="$2.8\,\mathrm{A}$" to=r id=eV2
#@ el R r m "$4\,\Omega$: falls $11.2\,\mathrm{V}$" col=1 i="$2.8\,\mathrm{A}$" to=m id=eR4
#@ el R s m "$3\,\Omega$: falls $5.16\,\mathrm{V}$" col=1 i="$1.72\,\mathrm{A}$" to=s id=eR1
#@ el V s z0 "$40\,\mathrm{V}$" col=1 i="$1.72\,\mathrm{A}$" to=z0 id=eV1
#@ el R z0 q "$2\,\Omega$: falls $3.44\,\mathrm{V}$" col=1 i="$1.72\,\mathrm{A}$" to=q id=eR2
#@ el R q g2 "$1.5\,\Omega$: falls $4.2\,\mathrm{V}$" col=1 i="$2.8\,\mathrm{A}$" to=g2 id=eR5
#@ el R m q "$45\,\Omega$: falls $48.6\,\mathrm{V}$" col=2 i="$1.08\,\mathrm{A}$" to=q id=eR3
#@ step "Ground the lowest wire again. Only the $64\,\mathrm{V}$ walk sign changes: $-45I_L+50.5I_R=-64$."
#@ step "$I_L=-1.72$, $I_R=-2.8\,\mathrm{A}$: $i_a=-1.72$, $i_b=1.08$, $i_c=2.8\,\mathrm{A}$." show=eR1,eR2,eR3,eR4,eR5,eV1,eV2
```

<details><summary>Solution</summary>

1. Clockwise mesh currents $I_L$, $I_R$. From the arrows: $i_a=I_L$, $i_b=I_L-I_R$, $i_c=-I_R$ (it points left).
2. Left mesh.

   $$-40+(3+2)I_L+45(I_L-I_R)=0\;\Rightarrow\;50I_L-45I_R=40$$
3. **(a)** Right mesh: clockwise through the $64\,\mathrm{V}$ source is a climb.

   $$45(I_R-I_L)+5.5I_R-64=0\;\Rightarrow\;-45I_L+50.5I_R=64$$
4. Solve.

   $$I_R=10\,\mathrm{A},\quad I_L=9.8\,\mathrm{A}$$
5. **(b)** Only the source sign flips.

   $$-45I_L+50.5I_R=-64\;\Rightarrow\;I_R=-2.8\,\mathrm{A},\quad I_L=-1.72\,\mathrm{A}$$

**Answer:** **(a)** $i_a=9.8\,\mathrm{A}$, $i_b=-0.2\,\mathrm{A}$, $i_c=-10\,\mathrm{A}$. **(b)** $i_a=-1.72\,\mathrm{A}$, $i_b=1.08\,\mathrm{A}$, $i_c=2.8\,\mathrm{A}$.

</details>

**Problem: Try it 13 · Three batteries, three windows (Textbook P4.36)** (intermediate)

**(a)** Use the mesh-current method to find the total power developed. **(b)** Check that it equals the total power dissipated.

```schematic
V1 0,3 -> 0,0 "$110\,\mathrm{V}$"
R1 0,3 -> 4,3 "$10\,\Omega$"
R2 4,3 -> 8,3 "$12\,\Omega$"
V2 8,3 -> 8,0 "$70\,\mathrm{V}$"
wire 0,3 -> 0,5
R3 0,5 -> 8,5 "$6\,\Omega$"
wire 8,5 -> 8,3
R4 4,3 -> 4,1.8 "$3\,\Omega$"
V3 4,0 -> 4,1.8 "$12\,\mathrm{V}$"
R5 0,0 -> 4,0 "$4\,\Omega$"
R6 4,0 -> 8,0 "$2\,\Omega$"
label 0,3 "$a$" left
label 4,3 "$m$" above
label 8,3 "$b$" right
label 0,0 "$l$" left
label 8,0 "$r$" right
ground 4,0
#@ spoiler
#@ straight off
#@ node a 110 "$a$: $110\,\mathrm{V}$"
#@ node b 98 "$b$: $98\,\mathrm{V}$"
#@ node m 50 "$m$: $50\,\mathrm{V}$"
#@ node z0 32 "bottom middle: $32\,\mathrm{V}$"
#@ node r 28 "$r$: $28\,\mathrm{V}$"
#@ node n 20 "12 V top: $20\,\mathrm{V}$"
#@ node g 0 "$l$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$l$: $0\,\mathrm{V}$" ground
#@ el V a g "$110\,\mathrm{V}$" col=0 i="$8\,\mathrm{A}$" to=a id=eV1
#@ el R a b "$6\,\Omega$: falls $12\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=b id=eR3
#@ el V b r "$70\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=b id=eV2
#@ el R m b "$12\,\Omega$: falls $48\,\mathrm{V}$" col=2 i="$4\,\mathrm{A}$" to=m id=eR2
#@ el R z0 r "$2\,\Omega$: falls $4\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=r id=eR6
#@ el R a m "$10\,\Omega$: falls $60\,\mathrm{V}$" col=3 i="$6\,\mathrm{A}$" to=m id=eR1
#@ el R m n "$3\,\Omega$: falls $30\,\mathrm{V}$" col=3 i="$10\,\mathrm{A}$" to=n id=eR4
#@ el V z0 n "$12\,\mathrm{V}$" col=4 i="$10\,\mathrm{A}$" to=z0 id=eV3
#@ el R g2 z0 "$4\,\Omega$: falls $32\,\mathrm{V}$" col=5 i="$8\,\mathrm{A}$" to=g2 id=eR5
#@ step "Ground $l$, the lowest wire (the $110\,\mathrm{V}$ battery's $-$ end). Heights are measured from $l$."
#@ step "Clockwise loops: $i_1$ lower left, $i_2$ lower right, $i_3$ top. Walks: $17i_1-3i_2-10i_3=122$, $-3i_1+17i_2-12i_3=-82$, $-10i_1-12i_2+28i_3=0$."
#@ step "Solve: $i_1=8$, $i_2=-2$, $i_3=2\,\mathrm{A}$. Real currents: $6\,\mathrm{A}$ in the $10\,\Omega$, $4\,\mathrm{A}$ from $b$ to $m$, $2\,\mathrm{A}$ in the $6\,\Omega$, $10\,\mathrm{A}$ down the $3\,\Omega$ and up through the $12\,\mathrm{V}$ battery, $8\,\mathrm{A}$ in the $4\,\Omega$, $2\,\mathrm{A}$ in the $2\,\Omega$." show=eR1,eR2,eR3,eR4,eR5,eR6
#@ step "Heights by walking down the slides." show=a,b,m,n,r,z0
#@ step "All three batteries climb: $880+140+120=1140\,\mathrm{W}$ developed = $1140\,\mathrm{W}$ in the six slides." show=eV1,eV2,eV3
```

<details><summary>Solution</summary>

1. Loop walks (clockwise; $-\to+$ through a battery is a climb).

   $$\begin{aligned}17i_1-3i_2-10i_3&=122\\-3i_1+17i_2-12i_3&=-82\\-10i_1-12i_2+28i_3&=0\end{aligned}$$
2. Solve.

   $$i_1=8\,\mathrm{A},\quad i_2=-2\,\mathrm{A},\quad i_3=2\,\mathrm{A}$$
3. Developed power.

   $$110(8)+70(2)+12(10)=880+140+120=1140\,\mathrm{W}$$
4. Dissipated.

   $$360+192+24+300+256+8=1140\,\mathrm{W}$$

**Answer:** $1140\,\mathrm{W}$ developed $=1140\,\mathrm{W}$ dissipated.

</details>

**Problem: Try it 14 · A diamond controlled by a shared resistor (Textbook P4.42)** (intermediate)

Use the mesh-current method to find the power dissipated in the $10\,\Omega$ resistor.

```schematic
V1 0,3 -> 0,0 "$60\,\mathrm{V}$"
R1 0,3 -> 4,3 "$4\,\Omega$"
R2 4,3 -> 4,0 "$10\,\Omega$" v="$v_\Delta$"
R3 4,3 -> 8,3 "$2.5\,\Omega$"
E1 8,0 -> 8,3 "$\tfrac{v_\Delta}{2}$"
R4 0,0 -> 4,0 "$2\,\Omega$"
R5 4,0 -> 8,0 "$20\,\Omega$"
label 4,3 "$m$" above
label 0,0 "$l$" left
label 8,0 "$r$" right
ground 4,0
#@ spoiler
#@ straight off
#@ node s 60 "battery top: $60\,\mathrm{V}$"
#@ node r 50 "$r$: $50\,\mathrm{V}$"
#@ node m 40 "$m$: $40\,\mathrm{V}$"
#@ node t 35 "diamond $-$: $35\,\mathrm{V}$"
#@ node z0 10 "bottom middle: $10\,\mathrm{V}$"
#@ node g 0 "$l$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$l$: $0\,\mathrm{V}$" ground
#@ el V s g "$60\,\mathrm{V}$" col=0 i="$5\,\mathrm{A}$" to=s id=eV1
#@ el R s m "$4\,\Omega$: falls $20\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=m id=eR1
#@ el R m z0 "$10\,\Omega$: falls $30\,\mathrm{V}$" col=1 i="$3\,\mathrm{A}$" to=z0 id=eR2 plus=m v="$v_\Delta$"
#@ el R g2 z0 "$2\,\Omega$: falls $10\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=g2 id=eR4
#@ el R m t "$2.5\,\Omega$: falls $5\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=t id=eR3
#@ el E r t "$\tfrac{v_\Delta}{2}$: $15\,\mathrm{V}$" col=3 i="$2\,\mathrm{A}$" to=r id=eE1
#@ el R z0 r "$20\,\Omega$: falls $40\,\mathrm{V}$" col=4 i="$2\,\mathrm{A}$" to=z0 id=eR5
#@ step "Ground $l$, the lowest wire. Heights are measured from $l$."
#@ step "The diamond is a battery of $\dfrac{v_\Delta}{2}$ ($+$ at the bottom). It depends on $v_\Delta$, across the shared $10\,\Omega$: $v_\Delta=10(i_1-i_2)$."
#@ step "Walk both windows: left $60=4i_1+10(i_1-i_2)+2i_1$; right $2.5i_2-\dfrac{v_\Delta}{2}+20i_2+10(i_2-i_1)=0$. So $i_1=5$, $i_2=2\,\mathrm{A}$, $v_\Delta=30\,\mathrm{V}$." show=eE1
#@ step "The $10\,\Omega$ carries $3\,\mathrm{A}$ and falls $30\,\mathrm{V}$: $90\,\mathrm{W}$." show=m,eR2
#@ step "The rest: the diamond lifts $2\,\mathrm{A}$ by $15\,\mathrm{V}$ (gives $30\,\mathrm{W}$); the battery gives $300\,\mathrm{W}$." show=t,r,eR1,eR3,eR4,eR5,eV1
```

<details><summary>Solution</summary>

1. Control.

   $$v_\Delta=10(i_1-i_2)$$
2. Loop walks.

   $$\begin{aligned}60&=4i_1+10(i_1-i_2)+2i_1\\0&=2.5i_2-\tfrac{v_\Delta}{2}+20i_2+10(i_2-i_1)\end{aligned}$$
3. Solve.

   $$i_1=5\,\mathrm{A},\quad i_2=2\,\mathrm{A},\quad v_\Delta=30\,\mathrm{V},\qquad p_{10\Omega}=\frac{30^2}{10}=90\,\mathrm{W}$$

**Answer:** $p_{10\,\Omega}=90\,\mathrm{W}$

</details>

## Practice set

Exam-style, mixing both topics. Try each for 10–15 minutes before opening the solution, then check your picture against the height view.

**Problem: P4.30 · Where should ground go?** (intermediate)

**(a)** Use the node-voltage method with node $a$ as the reference to find $v_o$ and the power delivered by the $0.5\,\mathrm{A}$ source. **(b)** Repeat with node $b$ as the reference. **(c)** Which reference is better, and why?

```schematic
I1 0,0 -> 0,3 "$0.5\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$40\,\Omega$"
V1 6,3 -> 3,3 "$12\,\mathrm{V}$"
R2 6,3 -> 6,0 "$100\,\Omega$" v="$v_o$"
R3 6,3 -> 9,3 "$150\,\Omega$"
R4 9,3 -> 9,0 "$50\,\Omega$"
wire 9,0 -> 0,0
label 3,3 "b" above
label 3,0 "a" below
#@ spoiler
#@ straight off
#@ node c 20 "$c$: $20\,\mathrm{V}$"
#@ node b 8 "$b$: $8\,\mathrm{V}$"
#@ node d 5 "$d$: $5\,\mathrm{V}$"
#@ node g 0 "$a$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$a$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$a$: $0\,\mathrm{V}$" ground
#@ node g4 0 "$a$: $0\,\mathrm{V}$" ground
#@ el I g b "$0.5\,\mathrm{A}$" col=0 i="$0.5\,\mathrm{A}$" to=b id=eI1
#@ el V c b "$12\,\mathrm{V}$" col=1 i="$0.3\,\mathrm{A}$" to=c id=eV1
#@ el R b g2 "$40\,\Omega$: falls $8\,\mathrm{V}$" col=1 i="$0.2\,\mathrm{A}$" to=g2 id=eR1
#@ el R c g3 "$100\,\Omega$: falls $20\,\mathrm{V}$" col=2 i="$0.2\,\mathrm{A}$" to=g3 id=eR2 plus=c v="$v_o$"
#@ el R c d "$150\,\Omega$: falls $15\,\mathrm{V}$" col=3 i="$0.1\,\mathrm{A}$" to=d id=eR3
#@ el R d g4 "$50\,\Omega$: falls $5\,\mathrm{V}$" col=3 i="$0.1\,\mathrm{A}$" to=g4 id=eR4
#@ step "Ground $a$ (the bottom wire)."
#@ step "The $12\,\mathrm{V}$ battery joins $b$ and $c$, both unknown: $c=b+12$. Bubble around them: the $0.5\,\mathrm{A}$ pump comes in; out go $\dfrac{b}{40}$, $\dfrac{c}{100}$ and $\dfrac{c}{200}$. So $b=8$, $c=20\,\mathrm{V}=v_o$." show=b,c
#@ step "Currents: $0.2\,\mathrm{A}$, $0.2\,\mathrm{A}$, and $0.1\,\mathrm{A}$ through $150+50\,\Omega$ ($d=5\,\mathrm{V}$). The pump lifts $0.5\,\mathrm{A}$ by $8\,\mathrm{V}$: $4\,\mathrm{W}$." show=d,eR1,eR2,eR3,eR4,eV1,eI1
#@ step "(b) Grounding $b$ instead just shifts every height down $8\,\mathrm{V}$: $v_o=c-a$ is still $20\,\mathrm{V}$. (c) $b$ is better: the battery then gives $c=12\,\mathrm{V}$ directly, so one plain in = out is enough."
```

<details><summary>Solution</summary>

1. **(a)** Reference $a$: $b$ and $c$ form a supernode with $v_c=v_b+12$. KCL around it (the $0.5\,\mathrm{A}$ comes in).

   $$\frac{v_b}{40}+\frac{v_b+12}{100}+\frac{v_b+12}{200}=0.5$$
2. Multiply by 200 and solve.

   $$8v_b+36=100\;\Rightarrow\;v_b=8\,\mathrm{V},\quad v_o=v_c=20\,\mathrm{V}$$
3. The source lifts $0.5\,\mathrm{A}$ from $a$ to $b$.

   $$p=(8)(0.5)=4\,\mathrm{W}\text{ delivered}$$
4. **(b)** Reference $b$: the source fixes $v_c=12\,\mathrm{V}$. One KCL, at $a$ (the $0.5\,\mathrm{A}$ leaves $a$).

   $$\frac{v_a}{40}+\frac{v_a-12}{100}+\frac{v_a-12}{200}+0.5=0\;\Rightarrow\;v_a=-8\,\mathrm{V}$$
5. Same answers.

   $$v_o=v_c-v_a=20\,\mathrm{V},\qquad p=(0-(-8))(0.5)=4\,\mathrm{W}$$
6. **(c)** Reference $b$ is better: the voltage source then fixes a node directly, so one plain KCL replaces the supernode.

**Answer:** **(a)** $v_o=20\,\mathrm{V}$; the source delivers $4\,\mathrm{W}$. **(b)** Same: $v_o=20\,\mathrm{V}$, $4\,\mathrm{W}$ (with $v_a=-8\,\mathrm{V}$). **(c)** $b$: the $12\,\mathrm{V}$ source then fixes $v_c$, leaving one equation.

</details>

**Problem: P4.24 · Wires below ground** (intermediate)

**(a)** Use the node-voltage method to find $i_1$, $i_2$ and $i_3$. **(b)** Check by showing the power dissipated equals the power developed.

```schematic
V1 0,3 -> 0,0 "$20\,\mathrm{V}$"
R1 0,3 -> 3,3 "$25\,\mathrm{k\Omega}$" i="$i_1$"
R2 3,3 -> 3,0 "$250\,\Omega$" i="$i_2$"
I1 3,3 -> 6,3 "$11\,\mathrm{mA}$"
R3 6,3 -> 6,0 "$1\,\mathrm{k\Omega}$"
wire 6,3 -> 9,3
V2 9,0 -> 9,3 "$10\,\mathrm{V}$" i_rev="$i_3$"
wire 3,3 -> 3,5
R4 3,5 -> 9,5 "$500\,\Omega$"
wire 9,5 -> 9,3
wire 9,0 -> 0,0
label 3,5 "$a$" left
label 6,3 "$b$" above
ground 0,0
#@ spoiler
#@ straight off
#@ node s 30 "battery top: $30\,\mathrm{V}$"
#@ node z0 10 "bottom wire: $10\,\mathrm{V}$"
#@ node a 5 "$a$: $5\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g4 0 "$b$: $0\,\mathrm{V}$" ground
#@ el R s a "$25\,\mathrm{k\Omega}$: falls $25\,\mathrm{V}$" col=0 i="$1\,\mathrm{mA}$" to=a id=eR1
#@ el V s z0 "$20\,\mathrm{V}$" col=1 i="$1\,\mathrm{mA}$" to=s id=eV1
#@ el R a z0 "$250\,\Omega$: falls $5\,\mathrm{V}$" col=1 i="$20\,\mathrm{mA}$" to=a id=eR2
#@ el I a g "$11\,\mathrm{mA}$" col=1 i="$11\,\mathrm{mA}$" to=g id=eI1
#@ el R a g2 "$500\,\Omega$: falls $5\,\mathrm{V}$" col=2 i="$10\,\mathrm{mA}$" to=g2 id=eR4
#@ el R g3 z0 "$1\,\mathrm{k\Omega}$: falls $10\,\mathrm{V}$" col=3 i="$10\,\mathrm{mA}$" to=g3 id=eR3
#@ el V z0 g4 "$10\,\mathrm{V}$" col=4 i="$31\,\mathrm{mA}$" to=z0 id=eV2
#@ step "Ground $b$, the lowest wire: the $10\,\mathrm{V}$ battery hangs it $10\,\mathrm{V}$ below the bottom wire. The question's voltages are from the bottom wire."
#@ step "One unknown, $a$. In = out at $a$ (mA, kΩ, from the bottom wire): $\dfrac{20-a}{25}=\dfrac{a}{0.25}+11+\dfrac{a+10}{0.5}$, so $a=-5\,\mathrm{V}$." show=a
#@ step "Currents: $i_1=1\,\mathrm{mA}$; $20\,\mathrm{mA}$ slides **up** the $250\,\Omega$ to $a$ ($i_2=-20$); $i_3=31\,\mathrm{mA}$ through the $10\,\mathrm{V}$ battery." show=eR1,eR2,eR3,eR4,eV1,eV2
#@ step "The pump carries $11\,\mathrm{mA}$ **down** from $a$ to $b$: it absorbs $55\,\mathrm{mW}$. The batteries give $20+310=330\,\mathrm{mW}$." show=eI1
```

<details><summary>Solution</summary>

1. Ground the bottom wire. The $10\,\mathrm{V}$ source has its $+$ at ground, so $v_b=-10\,\mathrm{V}$. KCL at $a$ (currents out, in mA and kΩ).

   $$\frac{v_a-20}{25}+\frac{v_a}{0.25}+11+\frac{v_a+10}{0.5}=0$$
2. Multiply by 25.

   $$v_a-20+100v_a+275+50v_a+500=0\;\Rightarrow\;v_a=-5\,\mathrm{V}$$
3. Branch currents in their arrow directions.

   $$i_1=\frac{20-(-5)}{25}=1\,\mathrm{mA},\qquad i_2=\frac{-5}{0.25}=-20\,\mathrm{mA}$$
4. KCL at $b$: in from the source ($11$), the $500\,\Omega$ ($10$) and the $1\,\mathrm{k\Omega}$ ($10$); out down through the $10\,\mathrm{V}$ source.

   $$i_3=11+\frac{-5+10}{0.5}+\frac{0+10}{1}=31\,\mathrm{mA}$$
5. **(b)** Developed: both voltage sources. Dissipated: the resistors plus the $11\,\mathrm{mA}$ source (which absorbs).

   $$20(1)+10(31)=330\,\mathrm{mW}=25+100+50+100+55$$

**Answer:** **(a)** $i_1=1\,\mathrm{mA}$, $i_2=-20\,\mathrm{mA}$, $i_3=31\,\mathrm{mA}$. **(b)** $330\,\mathrm{mW}$ developed $=330\,\mathrm{mW}$ absorbed.

</details>

**Problem: P4.18 · A diamond that gives power** (intermediate)

Use the node-voltage method to find the power delivered by the dependent voltage source.

```schematic
V1 0,3 -> 0,0 "$80\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$"
R2 3,3 -> 3,0 "$50\,\Omega$" i="$i_\sigma$"
R3 3,3 -> 6,3 "$10\,\Omega$"
E1 6,0 -> 6,3 "$75i_\sigma$"
R4 3,0 -> 6,0 "$15\,\Omega$"
wire 3,0 -> 0,0
label 3,3 "$a$" above
label 6,3 "$c$" right
label 6,0 "$d$" right
ground 0,0
#@ spoiler
#@ straight off
#@ node s 80 "battery top: $80\,\mathrm{V}$"
#@ node d 75 "$d$: $75\,\mathrm{V}$"
#@ node a 50 "$a$: $50\,\mathrm{V}$"
#@ node c 0 "$c$ = ground: $0\,\mathrm{V}$"
#@ node g 0 "$c$ = ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "$c$ = ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "$c$ = ground: $0\,\mathrm{V}$" ground
#@ el V s g "$80\,\mathrm{V}$" col=0 i="$6\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$5\,\Omega$: falls $30\,\mathrm{V}$" col=1 i="$6\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$50\,\Omega$: falls $50\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=g2 id=eR2
#@ el R a c "$10\,\Omega$: falls $50\,\mathrm{V}$" col=2 i="$5\,\mathrm{A}$" to=c id=eR3
#@ el E d c "$75i_\sigma$: $75\,\mathrm{V}$" col=3 i="$5\,\mathrm{A}$" to=d id=eE1
#@ el R g3 d "$15\,\Omega$: falls $75\,\mathrm{V}$" col=4 i="$5\,\mathrm{A}$" to=g3 id=eR4
#@ step "Ground the bottom-left wire. The battery lifts its top to $80\,\mathrm{V}$."
#@ step "The diamond locks $d=c+75i_\sigma$, with $i_\sigma=\dfrac{a}{50}$ (the current down the $50\,\Omega$)."
#@ step "In = out at $a$, and for the bubble around $c$ and $d$: $a=50$, $c=0$, $d=75\,\mathrm{V}$, $i_\sigma=1\,\mathrm{A}$." show=a,c,d
#@ step "$5\,\mathrm{A}$ slides from $a$ to $c$, **climbs** $75\,\mathrm{V}$ through the diamond, then falls down the $15\,\Omega$. Climbing means it gives $5\times75=375\,\mathrm{W}$." show=eR1,eR2,eR3,eR4,eV1,eE1
```

<details><summary>Solution</summary>

1. Ground the bottom-left wire. Name $a$, the diamond's $-$ end $c$ and $+$ end $d$. Control and rod.

   $$i_\sigma=\frac{v_a}{50},\qquad v_d-v_c=75i_\sigma=1.5v_a$$
2. KCL at $a$, times 50.

   $$10(v_a-80)+v_a+5(v_a-v_c)=0\;\Rightarrow\;16v_a-5v_c=800$$
3. KCL around the rod: in through the $10\,\Omega$, out through the $15\,\Omega$.

   $$\frac{v_a-v_c}{10}=\frac{v_d}{15}=\frac{v_c+1.5v_a}{15}\;\Rightarrow\;v_c=0$$
4. So

   $$v_a=50\,\mathrm{V},\quad i_\sigma=1\,\mathrm{A},\quad v_d=75\,\mathrm{V},\quad i=\frac{50-0}{10}=5\,\mathrm{A}$$
5. The $5\,\mathrm{A}$ enters the diamond's $-$ end and leaves its $+$ end: it climbs.

   $$p=(75)(5)=375\,\mathrm{W}\text{ delivered}$$

**Answer:** The dependent source delivers $375\,\mathrm{W}$ ($i_\sigma=1\,\mathrm{A}$, $75\,\mathrm{V}$ step, $5\,\mathrm{A}$).

</details>

**Problem: P4.49 · A battery that gets charged** (intermediate)

Use the mesh-current method to find the total power dissipated in the circuit.

```schematic
V1 0,3 -> 0,0 "$18\,\mathrm{V}$"
R1 0,3 -> 3,3 "$3\,\Omega$"
R2 3,3 -> 6,3 "$9\,\Omega$"
I1 3,0 -> 3,3 "$3\,\mathrm{A}$"
V2 6,0 -> 6,3 "$15\,\mathrm{V}$"
R3 0,0 -> 3,0 "$2\,\Omega$"
R4 3,0 -> 6,0 "$6\,\Omega$"
label 3,3 "$m$" above
label 3,0 "$q$" below
ground 0,0
#@ spoiler
#@ straight off
#@ node m 21.6 "$m$: $21.6\,\mathrm{V}$"
#@ node s 19.8 "battery top: $19.8\,\mathrm{V}$"
#@ node p 15 "bottom right: $15\,\mathrm{V}$"
#@ node z0 1.8 "bottom-left: $1.8\,\mathrm{V}$"
#@ node q 0.6 "$q$: $0.6\,\mathrm{V}$"
#@ node g 0 "top right: $0\,\mathrm{V}$" ground
#@ node g2 0 "top right: $0\,\mathrm{V}$" ground
#@ el R s m "$3\,\Omega$: falls $1.8\,\mathrm{V}$" col=0 i="$0.6\,\mathrm{A}$" to=s id=eR1
#@ el V s z0 "$18\,\mathrm{V}$" col=0 i="$0.6\,\mathrm{A}$" to=z0 id=eV1
#@ el R z0 q "$2\,\Omega$: falls $1.2\,\mathrm{V}$" col=0 i="$0.6\,\mathrm{A}$" to=q id=eR3
#@ el I q m "$3\,\mathrm{A}$" col=1 i="$3\,\mathrm{A}$" to=m id=eI1
#@ el R q p "$6\,\Omega$: falls $14.4\,\mathrm{V}$" col=2 i="$2.4\,\mathrm{A}$" to=q id=eR4
#@ el V p g "$15\,\mathrm{V}$" col=3 i="$2.4\,\mathrm{A}$" to=p id=eV2
#@ el R m g2 "$9\,\Omega$: falls $21.6\,\mathrm{V}$" col=4 i="$2.4\,\mathrm{A}$" to=g2 id=eR2
#@ step "Ground the lowest wire (top right). Heights are measured from it."
#@ step "The $3\,\mathrm{A}$ pump is shared: $I_b-I_a=3$. Walk around the outside, skipping it: $5I_a+15I_b=33$. So $I_a=-0.6$, $I_b=2.4\,\mathrm{A}$."
#@ step "Real currents → heights. The slides use $88.2\,\mathrm{W}$." show=s,m,p,q,z0,eR1,eR2,eR3,eR4
#@ step "$0.6\,\mathrm{A}$ falls **into** the $18\,\mathrm{V}$ battery: it absorbs $10.8\,\mathrm{W}$. The pump ($63\,\mathrm{W}$) and the $15\,\mathrm{V}$ battery ($36\,\mathrm{W}$) climb." show=eV1,eV2,eI1
```

<details><summary>Solution</summary>

1. Clockwise $I_a$ (left) and $I_b$ (right). The shared $3\,\mathrm{A}$ source points up; $I_b$ goes up through it and $I_a$ down.

   $$I_b-I_a=3$$
2. Supermesh KVL around the outside (the $15\,\mathrm{V}$ source is walked $-\to+$: a climb).

   $$-18+3I_a+9I_b-15+6I_b+2I_a=0\;\Rightarrow\;5I_a+15I_b=33$$
3. Solve.

   $$I_a=-0.6\,\mathrm{A},\qquad I_b=2.4\,\mathrm{A}$$
4. Resistor powers.

   $$(0.6)^2(3+2)+(2.4)^2(9+6)=1.8+86.4=88.2\,\mathrm{W}$$
5. Check: developed $63+36=99\,\mathrm{W}$; absorbed $88.2\,\mathrm{W}$ plus $10.8\,\mathrm{W}$ in the $18\,\mathrm{V}$ source.

**Answer:** $88.2\,\mathrm{W}$ dissipated in the resistors (and the $18\,\mathrm{V}$ source absorbs another $10.8\,\mathrm{W}$).

</details>

**Problem: Tutorial · A bridge by node voltages** (advanced)

Find $i_o$, $i_1$, $i_2$ and the power delivered by the current source. (The tutorial uses a Y–Δ swap; solve it with node voltages.)

```schematic
I1 0,0 -> 0,3 "$1\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$240\,\Omega$"
R2 3,3 -> 6,3 "$20\,\Omega$"
R3 6,3 -> 6,0 "$100\,\Omega$" i="$i_2$"
R4 6,3 -> 9,3 "$50\,\Omega$"
R5 9,3 -> 9,0 "$600\,\Omega$" i="$i_o$"
wire 3,3 -> 3,5
R6 3,5 -> 9,5 "$320\,\Omega$" i="$i_1$"
wire 9,5 -> 9,3
wire 9,0 -> 0,0
label 3,5 "$a$" left
label 6,3 "$b$" above
label 9,3 "$c$" right
ground 0,0
#@ spoiler
#@ straight off
#@ node a 72.96 "$a$: $72.96\,\mathrm{V}$"
#@ node b 60 "$b$: $60\,\mathrm{V}$"
#@ node c 57.6 "$c$: $57.6\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ el I g a "$1\,\mathrm{A}$" col=0 i="$1\,\mathrm{A}$" to=a id=eI1
#@ el R a g2 "$240\,\Omega$: falls $72.96\,\mathrm{V}$" col=1 i="$0.304\,\mathrm{A}$" to=g2 id=eR1
#@ el R a b "$20\,\Omega$: falls $12.96\,\mathrm{V}$" col=2 i="$0.648\,\mathrm{A}$" to=b id=eR2
#@ el R b g3 "$100\,\Omega$: falls $60\,\mathrm{V}$" col=2 i="$0.6\,\mathrm{A}$" to=g3 id=eR3
#@ el R b c "$50\,\Omega$: falls $2.4\,\mathrm{V}$" col=3 i="$0.048\,\mathrm{A}$" to=c id=eR4
#@ el R c g4 "$600\,\Omega$: falls $57.6\,\mathrm{V}$" col=3 i="$0.096\,\mathrm{A}$" to=g4 id=eR5
#@ el R a c "$320\,\Omega$: falls $15.36\,\mathrm{V}$" col=4 i="$0.048\,\mathrm{A}$" to=c id=eR6
#@ step "Ground the bottom wire. The $1\,\mathrm{A}$ pump pushes into $a$."
#@ step "Three unknowns $a$, $b$, $c$: one in = out each. Solve: $a=72.96$, $b=60$, $c=57.6\,\mathrm{V}$." show=a,b,c
#@ step "Currents = fall ÷ R: $i_o=\dfrac{57.6}{600}=0.096\,\mathrm{A}$, $i_1=0.048\,\mathrm{A}$, $i_2=\dfrac{60}{100}=0.6\,\mathrm{A}$." show=eR1,eR2,eR3,eR4,eR5,eR6
#@ step "The pump lifts $1\,\mathrm{A}$ by $72.96\,\mathrm{V}$: $72.96\,\mathrm{W}$." show=eI1
```

<details><summary>Solution</summary>

1. Ground the bottom wire; KCL at $a$, $b$, $c$.

   $$\begin{aligned}&\frac{v_a}{240}+\frac{v_a-v_b}{20}+\frac{v_a-v_c}{320}=1\\&\frac{v_b}{100}+\frac{v_b-v_a}{20}+\frac{v_b-v_c}{50}=0\\&\frac{v_c}{600}+\frac{v_c-v_b}{50}+\frac{v_c-v_a}{320}=0\end{aligned}$$
2. The second gives $v_b$ as a weighted average; substitute into the third.

   $$v_b=\tfrac58v_a+\tfrac14v_c,\qquad v_c=\tfrac{15}{19}v_a,\qquad v_b=\tfrac{125}{152}v_a$$
3. Substitute into the first.

   $$v_a=72.96\,\mathrm{V},\quad v_b=60\,\mathrm{V},\quad v_c=57.6\,\mathrm{V}$$
4. Currents and source power.

   $$i_o=\frac{57.6}{600}=0.096\,\mathrm{A},\quad i_1=0.048\,\mathrm{A},\quad i_2=0.6\,\mathrm{A},\quad p=72.96\,\mathrm{W}$$

**Answer:** $i_o=0.096\,\mathrm{A}$, $i_1=0.048\,\mathrm{A}$, $i_2=0.6\,\mathrm{A}$; the source delivers $72.96\,\mathrm{W}$.

</details>

**Problem: Lecture 3 p.22 · A shared pump** (advanced)

Use the mesh-current method to find the clockwise mesh currents $i_a$ (lower left), $i_b$ (top), $i_c$ (lower right) and the voltage $v$ across the current source.

```schematic
wire 0,3 -> 0,6
R1 0,6 -> 8,6 "$10\,\Omega$"
wire 8,6 -> 8,3
R2 0,3 -> 4,3 "$3\,\Omega$"
R3 4,3 -> 8,3 "$2\,\Omega$"
I1 4,0 -> 4,3 "$5\,\mathrm{A}$" v_rev="$v$"
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
V2 8,3 -> 8,0 "$50\,\mathrm{V}$"
R4 0,0 -> 4,0 "$6\,\Omega$"
R5 4,0 -> 8,0 "$4\,\Omega$"
label 4,3 "$m$" above
label 4,0 "$q$" below
label 8,3 "$r$" right
label 8,0 "$p$" right
ground 0,0
#@ spoiler
#@ straight off
#@ node l 100 "battery top: $100\,\mathrm{V}$"
#@ node m 98.5 "$m$: $98.5\,\mathrm{V}$"
#@ node r 87.5 "$r$: $87.5\,\mathrm{V}$"
#@ node p 37.5 "$p$: $37.5\,\mathrm{V}$"
#@ node q 10.5 "$q$: $10.5\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ el V l g "$100\,\mathrm{V}$" col=0 i="$1.75\,\mathrm{A}$" to=l id=eV1
#@ el R l m "$3\,\Omega$: falls $1.5\,\mathrm{V}$" col=1 i="$0.5\,\mathrm{A}$" to=m id=eR2
#@ el R m r "$2\,\Omega$: falls $11\,\mathrm{V}$" col=1 i="$5.5\,\mathrm{A}$" to=r id=eR3
#@ el V r p "$50\,\mathrm{V}$" col=1 i="$6.75\,\mathrm{A}$" to=p id=eV2
#@ el R q p "$4\,\Omega$: falls $27\,\mathrm{V}$" col=1 i="$6.75\,\mathrm{A}$" to=q id=eR5
#@ el R g2 q "$6\,\Omega$: falls $10.5\,\mathrm{V}$" col=1 i="$1.75\,\mathrm{A}$" to=g2 id=eR4
#@ el I q m "$5\,\mathrm{A}$" col=2 i="$5\,\mathrm{A}$" to=m id=eI1 plus=m v="$v$"
#@ el R l r "$10\,\Omega$: falls $12.5\,\mathrm{V}$" col=3 i="$1.25\,\mathrm{A}$" to=r id=eR1
#@ step "Ground the bottom wire. The $100\,\mathrm{V}$ battery lifts its top to $100\,\mathrm{V}$."
#@ step "The $5\,\mathrm{A}$ pump is shared by windows $a$ and $c$: $i_c-i_a=5$. Walk around $a$ and $c$ together (skip the pump), and around $b$: $i_a=1.75$, $i_b=1.25$, $i_c=6.75\,\mathrm{A}$."
#@ step "Heights: $m=100-3(0.5)=98.5\,\mathrm{V}$, $q=6(1.75)=10.5\,\mathrm{V}$. The pump spans them: $v=88\,\mathrm{V}$." show=m,q
#@ step "$6.75\,\mathrm{A}$ falls through the $50\,\mathrm{V}$ battery ($r=87.5$ down to $p=37.5$): it absorbs. The pump lifts $5\,\mathrm{A}$ by $88\,\mathrm{V}$: $440\,\mathrm{W}$." show=r,p,eR1,eR2,eR3,eR4,eR5,eV1,eV2,eI1
```

<details><summary>Solution</summary>

1. The shared source points up; $i_c$ goes up through it, $i_a$ down.

   $$i_c-i_a=5$$
2. Top mesh.

   $$10i_b+2(i_b-i_c)+3(i_b-i_a)=0\;\Rightarrow\;15i_b-3i_a-2i_c=0$$
3. Supermesh around the bottom two meshes, skipping the source.

   $$\begin{aligned}&-100+3(i_a-i_b)+2(i_c-i_b)+50+4i_c+6i_a=0\\&\Rightarrow\;9i_a-5i_b+6i_c=50\end{aligned}$$
4. Substitute $i_c=i_a+5$: $i_a=3i_b-2$ from the top mesh, then $15i_a-5i_b=20$.

   $$i_b=1.25\,\mathrm{A},\quad i_a=1.75\,\mathrm{A},\quad i_c=6.75\,\mathrm{A}$$
5. Heights at the source's ends.

   $$v=\big(100-3(0.5)\big)-6(1.75)=98.5-10.5=88\,\mathrm{V}$$

**Answer:** $i_a=1.75\,\mathrm{A}$, $i_b=1.25\,\mathrm{A}$, $i_c=6.75\,\mathrm{A}$; $v=88\,\mathrm{V}$

</details>

**Problem: P4.41 · A diamond in three windows** (advanced)

Use the mesh-current method to find the power developed in the dependent voltage source. Mesh 1 is lower left, mesh 2 the top, mesh 3 lower right (all clockwise).

```schematic
V1 0,4 -> 0,0 "$25\,\mathrm{V}$"
R1 0,4 -> 3,4 "$2\,\Omega$"
R2 3,4 -> 6,4 "$3\,\Omega$" v="$v_\phi$"
R3 3,4 -> 3,2 "$5\,\Omega$"
V2 3,2 -> 3,0 "$10\,\mathrm{V}$"
R4 6,4 -> 6,0 "$1\,\Omega$"
wire 6,0 -> 0,0
wire 0,4 -> 0,6
E1 3,6 -> 0,6 "$-3v_\phi$"
R5 3,6 -> 6,6 "$14\,\Omega$"
wire 6,6 -> 6,4
label 3,4 "$m$" above
ground 0,0
#@ spoiler
#@ straight off
#@ node s 36 "battery top: $36\,\mathrm{V}$"
#@ node m 26 "$m$: $26\,\mathrm{V}$"
#@ node n 21 "10 V top: $21\,\mathrm{V}$"
#@ node r 14 "right wire: $14\,\mathrm{V}$"
#@ node z0 11 "bottom: $11\,\mathrm{V}$"
#@ node g 0 "diamond $+$: $0\,\mathrm{V}$" ground
#@ node g2 0 "diamond $+$: $0\,\mathrm{V}$" ground
#@ el V s z0 "$25\,\mathrm{V}$" col=0 i="$4\,\mathrm{A}$" to=s id=eV1
#@ el R s m "$2\,\Omega$: falls $10\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=m id=eR1
#@ el R m n "$5\,\Omega$: falls $5\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=n id=eR3
#@ el V n z0 "$10\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=z0 id=eV2
#@ el R m r "$3\,\Omega$: falls $12\,\mathrm{V}$" col=2 i="$4\,\mathrm{A}$" to=r id=eR2 plus=m v="$v_\phi$"
#@ el R r z0 "$1\,\Omega$: falls $3\,\mathrm{V}$" col=2 i="$3\,\mathrm{A}$" to=z0 id=eR4
#@ el R g r "$14\,\Omega$: falls $14\,\mathrm{V}$" col=3 i="$1\,\mathrm{A}$" to=g id=eR5
#@ el E g2 s "$-3v_\phi$: $-36\,\mathrm{V}$" col=4 i="$1\,\mathrm{A}$" to=s id=eE1
#@ step "Ground the lowest wire, the diamond's $+$ end. Heights are measured from it."
#@ step "The diamond depends on $v_\phi=3(i_3-i_2)$. Walk the three windows: $i_1=4$, $i_2=-1$, $i_3=3\,\mathrm{A}$, $v_\phi=12\,\mathrm{V}$."
#@ step "The diamond is a battery of $-3v_\phi=-36\,\mathrm{V}$: its $+$ end sits $36\,\mathrm{V}$ **below** its $-$ end." show=eE1
#@ step "$1\,\mathrm{A}$ falls down the $14\,\Omega$ to the diamond, then climbs $36\,\mathrm{V}$ through it: it delivers $36\,\mathrm{W}$." show=s,m,n,r,z0,eR1,eR2,eR3,eR4,eR5,eV1,eV2
```

<details><summary>Solution</summary>

1. Control first: $v_\phi$ is across the $3\,\Omega$ shared by meshes 2 and 3.

   $$v_\phi=3(i_3-i_2)$$
2. Loop walks.

   $$\begin{aligned}&-25+2(i_1-i_2)+5(i_1-i_3)+10=0\\&3v_\phi+14i_2+3(i_2-i_3)+2(i_2-i_1)=0\\&i_3-10+5(i_3-i_1)+3(i_3-i_2)=0\end{aligned}$$
3. Solve with the control.

   $$i_1=4\,\mathrm{A},\quad i_2=-1\,\mathrm{A},\quad i_3=3\,\mathrm{A},\quad v_\phi=12\,\mathrm{V}$$
4. The diamond carries $i_2$; absorbed power with current entering $-$ means delivering.

   $$p=-(-3v_\phi)\,i_2=3(12)(-1)=-36\,\mathrm{W}$$

**Answer:** The dependent source delivers $36\,\mathrm{W}$ (absorbs $-36\,\mathrm{W}$).

</details>

## Cheat sheet

| Idea | In heights | Write |
|---|---|---|
| Node voltage | height of a wire above ground | $v_k$ |
| In = out (KCL) | what slides in = what slides out | $\sum\dfrac{v_k-v_j}{R}=$ pump current in |
| Battery from ground | a height for free | $v_k=V$ |
| Battery between two unknown wires | a locked pair: one bubble | $v_p-v_q=V$, in = out for the bubble |
| Diamond | a source whose size is set elsewhere | write its control in your letters first |
| Loop walk (KVL) | around a window: climbs = falls | $\sum$ climbs $=\sum$ falls |
| Shared resistor | carries the difference | $I_1-I_2$ |
| Pump on an outside edge | gives that loop current | $I=\pm I_s$ |
| Pump between two windows | walk around both, skip the pump | $I_a-I_b=I_s$ |
| How many equations | unknown heights / windows | node: $n_e-1$; mesh: $b_e-n_e+1$ |
| Power | current × height change | climb gives, fall uses |
