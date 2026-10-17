# Week 2: Kirchhoff’s Laws and Resistive Circuit Techniques

## Overview

> **Info:** Week 2 is about **solving whole resistor circuits**. Two laws do all the work (KCL and KVL); everything else this week is a shortcut that saves algebra: series/parallel, dividers, meters, bridges and Δ–Y.

### Topic map

| # | Topic | Key result | In heights |
|---|---|---|---|
| 1 | KCL and KVL | current in = out; loop sum $=0$ | currents balance; one height per node |
| 2 | Dependent sources | value = gain × control | find the control on the picture first |
| 3 | Series and parallel | $R_1+R_2$; $\;R_1R_2/(R_1+R_2)$ | stacked in a column vs side by side |
| 4 | Voltage and current dividers | $v_2=v\,\dfrac{R_2}{R_1+R_2}$ | the midpoint's place on the slope |
| 5 | Meters and the Wheatstone bridge | $R_x=R_2R_3/R_1$ | balanced = both midpoints level |
| 6 | Delta–wye (Δ–Y) | arm = product ÷ sum | corner heights don't change |

> **Tip:** **How to use this note.** Shaky on Week 1? Read **Start here** first: five rules are all you need. Each topic: short rules → worked example → **Try it** (answer on paper before opening). Every circuit has a **Height view** with a **Walk me through it**. Stuck? The **Summary** at the end is a visual crash course that maps every practice problem to what you need.

## Start here: the only Week 1 you need

> **Tip:** **Week 1 not clicking yet? That's fine.** Week 2 only needs these five rules. Learn them from the picture below; using them on Week 2 circuits is often what makes Week 1 click.

| # | Rule | Picture it as |
|---|---|---|
| 1 | **Voltage is height.** Pick one node as ground ($0\,\mathrm{V}$); every other node has a height. A voltage between two points = their height difference. | floors of a building |
| 2 | **Voltage source** = a fixed step: its $+$ end is exactly that many volts higher. Any current can go through it. | an escalator of fixed height |
| 3 | **Current source** = a fixed current in its arrow's direction. Its step can be anything. | a pump |
| 4 | **Resistor:** current always goes **downhill** through it, and it drops $i\times R$. So $i=\dfrac{\text{drop}}{R}$. | a slide |
| 5 | **Power = current × height.** Current falling through something → it **absorbs**. Climbing through it → it **delivers**. | water wheel vs pump |

**Example: S1 · All five rules in one circuit**

Find the current, the height of the middle node $m$, and who delivers or absorbs how much power.

```schematic
V1 0,3 -> 0,0 "$10\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$3\,\Omega$" flip
wire 3,0 -> 0,0
label 3,3 "$m$" above
#@ inline
#@ straight off
#@ node top 10 "top: $10\,\mathrm{V}$"
#@ node m 6 "$m$: $6\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$ (ground)" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$ (ground)" ground
#@ el V top g "$10\,\mathrm{V}$: lifts" col=0 i="$2\,\mathrm{A}$" to=top id=es
#@ el R top m "$2\,\Omega$: drops $4\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=m id=e2
#@ el R m g2 "$3\,\Omega$: drops $6\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=e3
#@ step "Rule 1: ground the bottom wire. Rule 2: the source's + end is $10\,\mathrm{V}$ up, so the top wire is at $10\,\mathrm{V}$." show=top
#@ step "Rule 4: one path, one current $i$, sliding down both resistors. The drops must add up to the whole $10\,\mathrm{V}$: $2i+3i=10$, so $i=2\,\mathrm{A}$." show=es,e2,e3
#@ step "Walk down from the top: the $2\,\Omega$ drops $(2)(2)=4\,\mathrm{V}$, so $m$ is at $6\,\mathrm{V}$. The $3\,\Omega$ drops the last $6\,\mathrm{V}$ to ground." show=m
#@ step "Rule 5: the source lifts $2\,\mathrm{A}$ up $10\,\mathrm{V}$ (delivers $20\,\mathrm{W}$); the resistors absorb $(4)(2)=8\,\mathrm{W}$ and $(6)(2)=12\,\mathrm{W}$."
```

1. Ground the bottom wire (rule 1). The source puts the top wire at $10\,\mathrm{V}$ (rule 2).
2. One path, so one current. It slides down both resistors, and the drops must add up to the full $10\,\mathrm{V}$ (rule 4).

   $$2i+3i=10\;\Rightarrow\;i=2\,\mathrm{A}$$
3. Walk down from the top to place $m$.

   $$V_m=10-(2)(2)=6\,\mathrm{V}$$
4. Power = current × height (rule 5).

   $$\underbrace{(10)(2)=20\,\mathrm{W}}_{\text{source delivers}}=\underbrace{(4)(2)}_{2\,\Omega}+\underbrace{(6)(2)}_{3\,\Omega}\ \text{absorbed}$$

**Answer:** $i=2\,\mathrm{A}$, $V_m=6\,\mathrm{V}$. The source delivers $20\,\mathrm{W}$; the resistors absorb $8\,\mathrm{W}$ and $12\,\mathrm{W}$.

> **Info:** **Signs, in two lines.** If a labelled voltage's $+$ sits on the **low** end, that voltage is negative. If a current comes out negative, it just flows **opposite** its arrow. That's the whole sign convention.

## Topic 1: Kirchhoff's current and voltage laws

- **Node:** a whole connected wire. It has **one** height (voltage).
- **KCL:** at every node, current in = current out. Nothing piles up.
- **KVL:** around any closed loop, the rises equal the drops (climbs = falls). It's the same as \"every node has one height\".
- **The move you'll use most:** ground one node, call an unknown node's height $x$, write each resistor current as $\dfrac{\text{high}-\text{low}}{R}$, then KCL at that node.
- Current arrows are guesses. A negative answer just means the current flows the other way; keep the arrow.

$$\text{KCL: }\sum i_{\text{in}}=\sum i_{\text{out}}\qquad\qquad \text{KVL: }\sum_{\text{loop}}\Delta v=0$$

**Example: Split currents and check power (Tutorial P2.19)**

Find $i_1$, $i_2$ and $v_o$, and check that the power balances.

```schematic
I1 0,0 -> 0,3 "$1.5\,\mathrm{A}$" v_rev="$v_o$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$100\,\Omega$" i="$i_1$"
R2 3,3 -> 6,3 "$150\,\Omega$" i="$i_2$"
R3 6,3 -> 6,0 "$250\,\Omega$"
wire 6,0 -> 0,0
#@ node a 120 "top: $120\,\mathrm{V}$"
#@ node m 75 "between $150$ and $250\,\Omega$: $75\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el I g a "$1.5\,\mathrm{A}$" col=0 i="$1.5\,\mathrm{A}$" to=a id=es plus=a v="$v_o$" rail
#@ el R a g2 "$100\,\Omega$: falls $120\,\mathrm{V}$" col=1 i="$1.2\,\mathrm{A}$" to=g2 id=e1
#@ el R a m "$150\,\Omega$: falls $45\,\mathrm{V}$" col=2 i="$0.3\,\mathrm{A}$" to=m id=e2
#@ el R m g3 "$250\,\Omega$: falls $75\,\mathrm{V}$" col=2 i="$0.3\,\mathrm{A}$" to=g3 id=e3
#@ step "Ground the bottom wire. The current source lifts $1.5\,\mathrm{A}$ to the top node, but a current source fixes a current, not a height: the top's height is still unknown."
#@ step "Both branches hang from the top level down to ground, so they fall the **same** height: $100i_1=(150+250)i_2$. The $400\,\Omega$ path needs four times the fall per amp, so it gets a quarter of the current: $i_1=4i_2$."
#@ step "KCL at the top: $i_1+i_2=1.5\,\mathrm{A}$, so $i_2=0.3\,\mathrm{A}$ and $i_1=1.2\,\mathrm{A}$." show=e1,e2,e3
#@ step "Now place the heights. The $100\,\Omega$ falls $(1.2)(100)=120\,\mathrm{V}$, so the top is at $120\,\mathrm{V}=v_o$. On the right, the $150\,\Omega$ falls $45\,\mathrm{V}$ to $75\,\mathrm{V}$ and the $250\,\Omega$ falls the last $75\,\mathrm{V}$." show=a,m,es
#@ step "Power = current × height change. The source lifts $1.5\,\mathrm{A}$ through $120\,\mathrm{V}$: $180\,\mathrm{W}$. The falls absorb $(120)(1.2)+(45)(0.3)+(75)(0.3)=144+13.5+22.5=180\,\mathrm{W}$."
#@ note "Straight line view: the current source is drawn as the supply rail at $120\,\mathrm{V}$; the stream splits $1.2\,\mathrm{A}$ / $0.3\,\mathrm{A}$ right away."
```

1. Ground the bottom wire; call the top node $a$. The $1.5\,\mathrm{A}$ source pushes current into $a$, and it leaves by two paths: the $100\,\Omega$ straight down, and the $150+250\,\Omega$ path.

   $$\text{KCL at }a:\quad i_1+i_2=1.5\,\mathrm{A}$$
2. Both paths fall from $a$ to ground, so they fall the **same height** (KVL).

   $$100i_1=(150+250)i_2\;\Rightarrow\;i_1=4i_2$$
3. Substitute, then read the height of $a$.

   $$5i_2=1.5\;\Rightarrow\;i_2=0.3\,\mathrm{A},\quad i_1=1.2\,\mathrm{A},\quad v_o=100(1.2)=120\,\mathrm{V}$$
4. Check: the source lifts $1.5\,\mathrm{A}$ up $120\,\mathrm{V}$; the resistors absorb $i^2R$.

   $$(120)(1.5)=180\,\mathrm{W}=144+13.5+22.5$$

**Answer:** $i_1=1.2\,\mathrm{A}$, $i_2=0.3\,\mathrm{A}$, $v_o=120\,\mathrm{V}$; $180\,\mathrm{W}$ delivered $=180\,\mathrm{W}$ absorbed.

**Problem: Try it 1 · One unknown height (Textbook P2.17)** (introductory)

Find $i_a$, $i_b$ and $v_b$, the power dissipated in each resistor, and the power delivered by the $80\,\mathrm{V}$ source.

```schematic
V1 0,3 -> 0,0 "$80\,\mathrm{V}$"
R1 0,3 -> 3,3 "$10\,\Omega$"
R2 3,3 -> 3,0 "$10\,\Omega$" i="$i_a$"
wire 3,3 -> 6,3
R3 6,3 -> 6,0 "$15\,\Omega$" i="$i_b$" v="$v_b$"
wire 6,0 -> 0,0
label 3,3 "$x$" above
#@ spoiler
#@ node t 80 "top: $80\,\mathrm{V}$"
#@ node x 30 "$x$: $30\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$80\,\mathrm{V}$" col=0 i="$5\,\mathrm{A}$" to=t id=es
#@ el R t x "$10\,\Omega$: falls $50\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=x id=e1
#@ el R x g2 "$10\,\Omega$: falls $30\,\mathrm{V}$" col=1 i="$3\,\mathrm{A}$" to=g2 id=ea
#@ el R x g3 "$15\,\Omega$: falls $30\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=g3 id=eb plus=x v="$v_b$"
#@ step "Ground the bottom; the source holds the top at $80\,\mathrm{V}$. Call the split node's height $v_x$."
#@ step "Charge falls from $80$ to $v_x$ through the series $10\,\Omega$, then splits down two slopes that both fall $v_x$. KCL at $x$: $\dfrac{80-v_x}{10}=\dfrac{v_x}{10}+\dfrac{v_x}{15}$, so $v_x=30\,\mathrm{V}$." show=x
#@ step "Both right-hand resistors fall $30\,\mathrm{V}$: $i_a=3\,\mathrm{A}$, $i_b=2\,\mathrm{A}$ and $v_b=30\,\mathrm{V}$. The series $10\,\Omega$ falls $50\,\mathrm{V}$ with $5\,\mathrm{A}$." show=ea,eb,e1,es
#@ step "Power = current × fall: $(50)(5)=250$, $(30)(3)=90$ and $(30)(2)=60\,\mathrm{W}$. The source lifts $5\,\mathrm{A}$ through $80\,\mathrm{V}$: $400\,\mathrm{W}$."
```

<details><summary>Solution</summary>

1. Ground the bottom wire. The top-left is at $80\,\mathrm{V}$; call the middle node's height $v_x$. KCL at $x$: what comes through the series $10\,\Omega$ leaves through the other two.

   $$\frac{80-v_x}{10}=\frac{v_x}{10}+\frac{v_x}{15}$$
2. Multiply by 30 and solve.

   $$240-3v_x=3v_x+2v_x\;\Rightarrow\;v_x=30\,\mathrm{V}$$
3. Both right-hand resistors fall $30\,\mathrm{V}$.

   $$i_a=\frac{30}{10}=3\,\mathrm{A},\quad i_b=\frac{30}{15}=2\,\mathrm{A},\quad v_b=30\,\mathrm{V}$$
4. Powers, and the check: the source lifts $3+2=5\,\mathrm{A}$ up $80\,\mathrm{V}$.

   $$\begin{aligned}&5^2(10)=250\,\mathrm{W},\quad 3^2(10)=90\,\mathrm{W},\quad 2^2(15)=60\,\mathrm{W}\\&(80)(5)=400\,\mathrm{W}=250+90+60\end{aligned}$$

**Answer:** **(a)** $i_a=3\,\mathrm{A}$ **(b)** $i_b=2\,\mathrm{A}$ **(c)** $v_b=30\,\mathrm{V}$ **(d)** $250\,\mathrm{W}$, $90\,\mathrm{W}$, $60\,\mathrm{W}$ **(e)** $400\,\mathrm{W}$

</details>

**Problem: Try it 2 · A current source pulls the middle down (Textbook P2.21)** (introductory)

Find $v_o$ using KCL and Ohm's law, then check that the power balances.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$2\,\mathrm{k\Omega}$" v="$v_o$" flip
wire 3,3 -> 6,3
I1 6,3 -> 6,0 "$2.5\,\mathrm{mA}$" flip
wire 6,0 -> 0,0
#@ spoiler
#@ node t 100 "top: $100\,\mathrm{V}$"
#@ node o 25 "middle: $25\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$100\,\mathrm{V}$" col=0 i="$15\,\mathrm{mA}$" to=t id=es
#@ el R t o "$5\,\mathrm{k\Omega}$: falls $75\,\mathrm{V}$" col=1 i="$15\,\mathrm{mA}$" to=o id=e5
#@ el R o g2 "$2\,\mathrm{k\Omega}$: falls $25\,\mathrm{V}$" col=1 i="$12.5\,\mathrm{mA}$" to=g2 id=e2 plus=o v="$v_o$"
#@ el I o g3 "$2.5\,\mathrm{mA}$" col=2 i="$2.5\,\mathrm{mA}$" to=g3 id=ei
#@ step "Ground the bottom; the source holds the top at $100\,\mathrm{V}$. Call the middle height $v_o$."
#@ step "KCL at the middle: what falls in through the $5\,\mathrm{k\Omega}$ leaves down the $2\,\mathrm{k\Omega}$ and the current source. In mA and kΩ: $\dfrac{100-v_o}{5}=\dfrac{v_o}{2}+2.5$, so $v_o=25\,\mathrm{V}$." show=o
#@ step "Currents: the $5\,\mathrm{k\Omega}$ falls $75\,\mathrm{V}$ ($15\,\mathrm{mA}$), the $2\,\mathrm{k\Omega}$ falls $25\,\mathrm{V}$ ($12.5\,\mathrm{mA}$), and the current source sinks the other $2.5\,\mathrm{mA}$." show=e5,e2,ei,es
#@ step "Power: the source lifts $15\,\mathrm{mA}$ through $100\,\mathrm{V}$ ($1.5\,\mathrm{W}$). The falls absorb $1.125+0.3125+0.0625=1.5\,\mathrm{W}$; the current source absorbs because its current falls from $25\,\mathrm{V}$ to 0."
```

<details><summary>Solution</summary>

1. Convert: ground the bottom, the top is at $100\,\mathrm{V}$, the middle at unknown height $v_o$. KCL at the middle (mA and kΩ):

   $$\frac{100-v_o}{5}=\frac{v_o}{2}+2.5\;\Rightarrow\;200-2v_o=5v_o+25\;\Rightarrow\;v_o=25\,\mathrm{V}$$
2. Read the currents as fall ÷ R.

   $$\begin{aligned}&i_{5\mathrm{k}}=\frac{75}{5}=15\,\mathrm{mA},\\&i_{2\mathrm{k}}=\frac{25}{2}=12.5\,\mathrm{mA},\quad 12.5+2.5=15\ \checkmark\end{aligned}$$
3. Power: the source's climb equals the sum of the falls. The current source's current falls from 25 V to 0, so it absorbs.

   $$(100)(15)=1500\,\mathrm{mW}=1125+312.5+62.5$$

**Answer:** $v_o=25\,\mathrm{V}$; the $100\,\mathrm{V}$ source delivers $1.5\,\mathrm{W}$, absorbed as $1.125+0.3125+0.0625\,\mathrm{W}$.

</details>

## Topic 2: Dependent sources

- A **dependent source** (diamond) is a source whose value is set by a voltage or current somewhere else: its **control**.
- It still obeys KCL and KVL like any source. You just get one extra equation: value = gain × control.
- **Recipe:** (1) find the control and its arrow or $+/-$; (2) write the source's value in terms of it; (3) KCL/KVL as usual; (4) solve; (5) check the control law.
- Gain units: V/V and A/A have none; V/A is $\Omega$; A/V is S.
- **In heights:** a dependent voltage source is a step whose size you read from its control; a dependent current source fixes a current. Either can deliver or absorb.

**Example: A current-controlled current source (Lecture 2)**

Find $i_\Delta$, $i_o$ and $v_o$.

```schematic
V1 0,3 -> 0,0 "$500\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$" i="$i_\Delta$"
R2 3,3 -> 3,0 "$20\,\Omega$" i="$i_o$" v="$v_o$"
wire 3,3 -> 6,3
G1 6,0 -> 6,3 "$5i_\Delta$"
wire 6,0 -> 0,0
label 3,3 "$b$" above
#@ node t 500 "top: $500\,\mathrm{V}$"
#@ node b 480 "$b$: $480\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$500\,\mathrm{V}$" col=0 i="$4\,\mathrm{A}$" to=t id=es
#@ el R t b "$5\,\Omega$: falls $20\,\mathrm{V}$" col=1 i="$4\,\mathrm{A}$" to=b id=e5
#@ el R b g2 "$20\,\Omega$: falls $480\,\mathrm{V}$" col=1 i="$24\,\mathrm{A}$" to=g2 id=e20 plus=b v="$v_o$"
#@ el G g3 b "$5i_\Delta=20\,\mathrm{A}$" col=2 i="$20\,\mathrm{A}$" to=b id=ed
#@ step "Ground the bottom wire. The $500\,\mathrm{V}$ source puts the top at $500\,\mathrm{V}$." show=t
#@ step "Call the controlling current (through the $5\,\Omega$) $i_\Delta$. The diamond pumps another $5i_\Delta$ up into $b$, so by KCL $i_o=i_\Delta+5i_\Delta=6i_\Delta$ falls through the $20\,\Omega$."
#@ step "Walk down from the top: the $5\,\Omega$ falls $5i_\Delta$ and the $20\,\Omega$ falls $20(6i_\Delta)=120i_\Delta$. Together they use up the whole $500\,\mathrm{V}$: $125i_\Delta=500$, so $i_\Delta=4\,\mathrm{A}$." show=es,e5
#@ step "So $b$ sits only $20\,\mathrm{V}$ below the top, at $480\,\mathrm{V}=v_o$. The $20\,\Omega$ carries $24\,\mathrm{A}$ down, and the diamond lifts $20\,\mathrm{A}$ from 0 up to $480\,\mathrm{V}$." show=b,e20,ed
#@ step "Power: the diamond climbs $480\,\mathrm{V}$ with $20\,\mathrm{A}$ and delivers $9600\,\mathrm{W}$; the source delivers $2000\,\mathrm{W}$. The falls absorb $(20)(4)+(480)(24)=80+11\,520\,\mathrm{W}$. A dependent source can be the main supplier."
```

1. Control first: $i_\Delta$ is the current through the $5\,\Omega$. The diamond pushes $5i_\Delta$ up into node $b$. KCL at $b$:

   $$i_o=i_\Delta+5i_\Delta=6i_\Delta$$
2. Write everything in terms of $i_\Delta$.

   $$v_o=20\,i_o=120\,i_\Delta$$
3. KVL around the left loop: climb $500$, fall $5i_\Delta$, fall $v_o$.

   $$500-5i_\Delta-120i_\Delta=0\;\Rightarrow\;i_\Delta=4\,\mathrm{A}$$
4. Back-substitute; the diamond carries $5(4)=20\,\mathrm{A}$.

   $$i_o=24\,\mathrm{A},\qquad v_o=480\,\mathrm{V}$$
5. Check: the $500\,\mathrm{V}$ source lifts $4\,\mathrm{A}$ up $500\,\mathrm{V}$, the diamond lifts $20\,\mathrm{A}$ up to $b$ ($480\,\mathrm{V}$), and the resistors absorb what they deliver.

   $$\underbrace{(500)(4)+(480)(20)}_{2000+9600}=\underbrace{(4)^2(5)+(24)^2(20)}_{80+11\,520}$$

**Answer:** $i_\Delta=4\,\mathrm{A}$, $i_o=24\,\mathrm{A}$, $v_o=480\,\mathrm{V}$

**Problem: Try it 3 · Two circuits joined by one wire (Tutorial P2.35)** (intermediate)

Find $i_o$ (the current in the wire joining the two networks), $i_1$ and $i_2$.

```schematic
V1 0,3 -> 0,0 "$18\,\mathrm{V}$"
R1 0,3 -> 3,3 "$12\,\Omega$"
R2 3,3 -> 3,0 "$6\,\Omega$" v="$v_\Delta$"
wire 3,0 -> 0,0
wire 3,0 -> 6,0
label 4.5,0 "$\leftarrow i_o$" below
G1 6,3 -> 6,0 "$\dfrac{v_\Delta}{2}$"
wire 6,3 -> 12,3
wire 6,0 -> 12,0
R3 9,3 -> 9,0 "$10\,\Omega$" i="$i_1$"
R4 12,3 -> 12,0 "$5\,\Omega$" i="$i_2$"
#@ spoiler
#@ node t 18 "left top: $18\,\mathrm{V}$"
#@ node m 6 "left middle: $6\,\mathrm{V}$"
#@ node g 0 "shared bottom wire: $0\,\mathrm{V}$" ground
#@ node g2 0 "shared bottom wire: $0\,\mathrm{V}$" ground
#@ node g3 0 "shared bottom wire: $0\,\mathrm{V}$" ground
#@ node g4 0 "shared bottom wire: $0\,\mathrm{V}$" ground
#@ node g5 0 "shared bottom wire: $0\,\mathrm{V}$" ground
#@ node c -10 "right top: $-10\,\mathrm{V}$"
#@ el V t g "$18\,\mathrm{V}$" col=0 i="$1\,\mathrm{A}$" to=t id=es
#@ el R t m "$12\,\Omega$: falls $12\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=m id=e12
#@ el R m g2 "$6\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=g2 id=e6 plus=m v="$v_\Delta$"
#@ el G c g3 "$v_\Delta/2$" col=2 i="$3\,\mathrm{A}$" to=g3 id=eG
#@ el R g4 c "$10\,\Omega$: falls $10\,\mathrm{V}$" col=3 i="$1\,\mathrm{A}$" to=c id=e10
#@ el R g5 c "$5\,\Omega$: falls $10\,\mathrm{V}$" col=4 i="$2\,\mathrm{A}$" to=c id=e5
#@ step "Ground the shared bottom wire. The left network is one loop: $\dfrac{18}{12+6}=1\,\mathrm{A}$, and the $6\,\Omega$ falls $6\,\mathrm{V}$, so $v_\Delta=6\,\mathrm{V}$." show=m,e12,e6,es
#@ step "The single wire between the networks can't carry a net current (nothing could come back), so $i_o=0$. All it does is put both bottoms at the same height."
#@ step "The diamond pulls $\dfrac{v_\Delta}{2}=3\,\mathrm{A}$ down out of the right top node. The resistors must refill that node from the bottom wire, and current only falls through a resistor, so the right top node must sit **below** ground." show=eG
#@ step "Both resistors fall the same height from ground down to that node and share the $3\,\mathrm{A}$ by conductance: $1\,\mathrm{A}$ through the $10\,\Omega$, $2\,\mathrm{A}$ through the $5\,\Omega$. The fall is $(1)(10)=10\,\mathrm{V}$, so the node is at $-10\,\mathrm{V}$. Against their downward arrows: $i_1=-1\,\mathrm{A}$, $i_2=-2\,\mathrm{A}$." show=c,e10,e5
```

<details><summary>Solution</summary>

1. The two halves touch through **one** wire only. Current that leaves the left half on it would need a second wire to come back (KCL around the whole left half), so none flows.

   $$i_o=0$$
2. So the left loop is on its own: one current through $12+6\,\Omega$.

   $$i=\frac{18}{18}=1\,\mathrm{A},\qquad v_\Delta=6(1)=6\,\mathrm{V}$$
3. Control → value: the diamond pushes $\dfrac{v_\Delta}{2}=3\,\mathrm{A}$ down. KCL at the right top node:

   $$i_1+i_2+3=0$$
4. Both right resistors span the same two nodes (same height difference).

   $$10i_1=5i_2\;\Rightarrow\;i_2=2i_1\;\Rightarrow\;3i_1=-3$$
5. Negative: both currents really flow **up**, against their arrows.

   $$i_1=-1\,\mathrm{A},\qquad i_2=-2\,\mathrm{A}$$

**Answer:** $i_o=0$, $i_1=-1\,\mathrm{A}$, $i_2=-2\,\mathrm{A}$

</details>

## Topic 3: Series and parallel resistance

|  | Series | Parallel |
|---|---|---|
| How to spot it | one path, nothing branches off between them | both ends on the **same two nodes** |
| They share | the same **current** | the same **voltage** |
| Combine | $R=R_1+R_2+\dots$ | $\dfrac1R=\dfrac1{R_1}+\dfrac1{R_2}+\dots$; two: $\dfrac{R_1R_2}{R_1+R_2}$ |
| In heights | stacked in one column; the falls add | side by side between the same two levels |
| Sanity check | bigger than the biggest | smaller than the smallest |

- **Reduce:** start at the far end from the source, combine one pair at a time, redraw.
- **Then go back** (\"un-reduce\"): find the source current, then the height at each split, then each branch current = fall ÷ $R$.
- Trap: two resistors sharing a node are **not** in series if a third element also touches that node.

**Example: Reduce, then work back to each branch (Lecture 2)**

Find the equivalent resistance seen by the source, then $i_s$, $i_1$ and $i_2$.

```schematic
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$" i="$i_s$"
R2 3,3 -> 3,0 "$18\,\Omega$" i="$i_1$"
R3 3,3 -> 6,3 "$3\,\Omega$"
R4 6,3 -> 6,0 "$6\,\Omega$" i="$i_2$"
wire 6,0 -> 0,0
label 3,3 "$x$" above
label 6,3 "$a$" above
#@ node t 120 "top: $120\,\mathrm{V}$"
#@ node x 72 "$x$: $72\,\mathrm{V}$"
#@ node a 48 "$a$: $48\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$120\,\mathrm{V}$" col=0 i="$12\,\mathrm{A}$" to=t id=es
#@ el R t x "$4\,\Omega$: falls $48\,\mathrm{V}$" col=1 i="$12\,\mathrm{A}$" to=x id=e4
#@ el R x g2 "$18\,\Omega$: falls $72\,\mathrm{V}$" col=1 i="$4\,\mathrm{A}$" to=g2 id=e18
#@ el R x a "$3\,\Omega$: falls $24\,\mathrm{V}$" col=2 i="$8\,\mathrm{A}$" to=a id=e3
#@ el R a g3 "$6\,\Omega$: falls $48\,\mathrm{V}$" col=2 i="$8\,\mathrm{A}$" to=g3 id=e6
#@ step "Ground the bottom; the source holds the top at $120\,\mathrm{V}$. The reduction ($R_{\mathrm{in}}=10\,\Omega$) tells you how much current the source lifts: $i_s=12\,\mathrm{A}$." show=es
#@ step "The $4\,\Omega$ falls $(12)(4)=48\,\mathrm{V}$, so the split node $x$ sits at $72\,\mathrm{V}$." show=e4,x
#@ step "From $x$ both branches fall the same $72\,\mathrm{V}$ to ground: the $18\,\Omega$ carries $i_1=\dfrac{72}{18}=4\,\mathrm{A}$, the $3+6=9\,\Omega$ path carries $i_2=\dfrac{72}{9}=8\,\mathrm{A}$." show=e18,e3,e6
#@ step "On the right path the $3\,\Omega$ falls $24\,\mathrm{V}$ to $a=48\,\mathrm{V}$ and the $6\,\Omega$ falls the last $48\,\mathrm{V}$. KCL at $x$: $4+8=12$." show=a
#@ step "Power: the source lifts $12\,\mathrm{A}$ through $120\,\mathrm{V}$ ($1440\,\mathrm{W}$); the falls absorb $576+288+192+384=1440\,\mathrm{W}$."
```

1. Far end first: node $a$ joins only the $3\,\Omega$ and $6\,\Omega$, so they're in series.

   $$3+6=9\,\Omega$$
2. That $9\,\Omega$ path and the $18\,\Omega$ both hang from $x$ to ground: parallel. Then add the $4\,\Omega$.

   $$18\parallel9=\frac{18\cdot9}{27}=6\,\Omega,\qquad R_{\mathrm{in}}=4+6=10\,\Omega$$
3. Source current, then the height of $x$.

   $$i_s=\frac{120}{10}=12\,\mathrm{A},\qquad V_x=120-(12)(4)=72\,\mathrm{V}$$
4. Each branch falls $72\,\mathrm{V}$: current = fall ÷ R. Check KCL.

   $$i_1=\frac{72}{18}=4\,\mathrm{A},\quad i_2=\frac{72}{9}=8\,\mathrm{A},\quad 4+8=12\ \checkmark$$

**Answer:** $R_{eq}=10\,\Omega$, $i_s=12\,\mathrm{A}$, $i_1=4\,\mathrm{A}$, $i_2=8\,\mathrm{A}$

**Problem: Try it 4 · Reduce, then restore (Assessment AP 3.1)** (intermediate)

Find:

1. the voltage $v$;
2. the power delivered by the current source;
3. the power dissipated in the $10\,\Omega$ resistor.

```schematic
I1 0,0 -> 0,3 "$5\,\mathrm{A}$" v_rev="$v$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$30\,\Omega$"
R2 3,3 -> 6,3 "$7.2\,\Omega$"
R3 6,3 -> 6,0 "$64\,\Omega$"
R4 6,3 -> 9,3 "$6\,\Omega$"
R5 9,3 -> 9,0 "$10\,\Omega$"
wire 9,0 -> 0,0
#@ spoiler
#@ node t 60 "top: $60\,\mathrm{V}$"
#@ node b 38.4 "$b$: $38.4\,\mathrm{V}$"
#@ node m 24 "between $6$ and $10\,\Omega$: $24\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g4 0 "bottom: $0\,\mathrm{V}$" ground
#@ el I g t "$5\,\mathrm{A}$" col=0 i="$5\,\mathrm{A}$" to=t id=es plus=t v="$v$" rail
#@ el R t g2 "$30\,\Omega$: falls $60\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=e30
#@ el R t b "$7.2\,\Omega$: falls $21.6\,\mathrm{V}$" col=2 i="$3\,\mathrm{A}$" to=b id=e72
#@ el R b g3 "$64\,\Omega$: falls $38.4\,\mathrm{V}$" col=2 i="$0.6\,\mathrm{A}$" to=g3 id=e64
#@ el R b m "$6\,\Omega$: falls $14.4\,\mathrm{V}$" col=3 i="$2.4\,\mathrm{A}$" to=m id=e6
#@ el R m g4 "$10\,\Omega$: falls $24\,\mathrm{V}$" col=3 i="$2.4\,\mathrm{A}$" to=g4 id=e10
#@ step "Ground the bottom wire. Reduce from the far end to see how high the source must lift: $R_{\mathrm{in}}=12\,\Omega$, so the top sits at $v=(5)(12)=60\,\mathrm{V}$." show=t
#@ step "The $30\,\Omega$ falls the full $60\,\mathrm{V}$: $2\,\mathrm{A}$. The other $3\,\mathrm{A}$ falls $21.6\,\mathrm{V}$ through the $7.2\,\Omega$ to $b=38.4\,\mathrm{V}$." show=e30,e72,b
#@ step "At $b$ the stream splits again: the $64\,\Omega$ takes $\dfrac{38.4}{64}=0.6\,\mathrm{A}$, the $6+10=16\,\Omega$ path takes $\dfrac{38.4}{16}=2.4\,\mathrm{A}$. The $6\,\Omega$ falls $14.4\,\mathrm{V}$ to $24\,\mathrm{V}$." show=e64,e6,e10,m
#@ step "The source lifts $5\,\mathrm{A}$ through $60\,\mathrm{V}$: it delivers $300\,\mathrm{W}$. The $10\,\Omega$ absorbs $(24)(2.4)=57.6\,\mathrm{W}$." show=es
```

<details><summary>Solution</summary>

1. Reduce from the far end.

   $$\begin{aligned}&6+10=16,\qquad 16\parallel64=12.8\\&12.8+7.2=20,\qquad 20\parallel30=12\,\Omega\end{aligned}$$
2. The source sees $12\,\Omega$, so its height is $v$; it lifts $5\,\mathrm{A}$ up $v$.

   $$v=(5)(12)=60\,\mathrm{V},\qquad p=(60)(5)=300\,\mathrm{W}\text{ delivered}$$
3. Restore: the $30\,\Omega$ falls $60\,\mathrm{V}$; the rest goes through $7.2\,\Omega$; walk down to the next node.

   $$i_{30}=2\,\mathrm{A},\quad i_{7.2}=3\,\mathrm{A},\quad V_b=60-(3)(7.2)=38.4\,\mathrm{V}$$
4. The $6+10\,\Omega$ path falls $38.4\,\mathrm{V}$.

   $$i_{10}=\frac{38.4}{16}=2.4\,\mathrm{A},\qquad p_{10}=10(2.4)^2=57.6\,\mathrm{W}$$

**Answer:** **(1)** $v=60\,\mathrm{V}$ **(2)** $300\,\mathrm{W}$ delivered **(3)** $57.6\,\mathrm{W}$

</details>

## Topic 4: Voltage and current dividers

|  | Voltage divider (series) | Current divider (parallel) |
|---|---|---|
| Formula | $v_2=v\,\dfrac{R_2}{R_1+R_2}$ | $i_1=i\,\dfrac{R_2}{R_1+R_2}$ (the **other** resistor on top) |
| Who gets more | the **bigger** resistor gets more voltage | the **smaller** resistor gets more current |
| In heights | one slope; the midpoint sits $\dfrac{R_2}{R_1+R_2}$ of the way up | same fall for both; current $\propto 1/R$ |

- **Loaded divider:** a load $R_L$ on the output is in parallel with $R_2$. Replace $R_2$ by $R_2\parallel R_L$: the output **sags**. Barely matters if $R_L\gg R_2$.
- **Nested split:** divide the current that actually enters that branch, not the source current.
- **Tolerance worst case:** biggest output = $R_2$ at max and $R_1$ at min; smallest output = the opposite.

$$v_o=v_s\,\frac{R_2\parallel R_L}{R_1+R_2\parallel R_L}\qquad(\text{loaded})$$

**Example: Worst-case divider tolerance (Lecture 2)**

Both resistors have a $\pm10\%$ tolerance. Find the nominal, maximum and minimum no-load output $v_o$.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$25\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$100\,\mathrm{k\Omega}$"
wire 3,3 -> 5,3
wire 3,0 -> 5,0
wire 3,0 -> 0,0
terminal 5,3
terminal 5,0
gap 5,3 -> 5,0 v="$v_o$"
#@ view "Nominal"
#@ node t 100 "top: $100\,\mathrm{V}$"
#@ node m 80 "midpoint: $80\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$100\,\mathrm{V}$" col=0 i="$0.8\,\mathrm{mA}$" to=t id=es
#@ el R t m "$25\,\mathrm{k\Omega}$: falls $20\,\mathrm{V}$" col=1 i="$0.8\,\mathrm{mA}$" to=m id=e1
#@ el R m g2 "$100\,\mathrm{k\Omega}$: falls $80\,\mathrm{V}$" col=1 i="$0.8\,\mathrm{mA}$" to=g2 id=e2 plus=m v="$v_o$"
#@ step "Ground the bottom wire; the top is at $100\,\mathrm{V}$. No load, so one current flows through both resistors: $\dfrac{100}{125\,\mathrm{k\Omega}}=0.8\,\mathrm{mA}$." show=es
#@ step "The fall is shared in proportion to resistance: the $25\,\mathrm{k\Omega}$ takes $20\,\mathrm{V}$, the $100\,\mathrm{k\Omega}$ takes $80\,\mathrm{V}$. The midpoint sits $\dfrac{100}{125}$ of the way up: $v_o=80\,\mathrm{V}$." show=m,e1,e2
#@ note "Compare the tabs: shrinking the top slope or stretching the bottom one raises the midpoint."
#@ view "Highest output"
#@ node t 100 "top: $100\,\mathrm{V}$"
#@ node m 83.02 "midpoint: $83.02\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$100\,\mathrm{V}$" col=0 i="$0.755\,\mathrm{mA}$" to=t
#@ el R t m "$22.5\,\mathrm{k\Omega}$: falls $16.98\,\mathrm{V}$" col=1 i="$0.755\,\mathrm{mA}$" to=m
#@ el R m g2 "$110\,\mathrm{k\Omega}$: falls $83.02\,\mathrm{V}$" col=1 i="$0.755\,\mathrm{mA}$" to=g2 plus=m v="$v_o$"
#@ note "Top resistor at its minimum, bottom at its maximum: the bottom takes the biggest share of the fall, $\dfrac{110}{132.5}$."
#@ view "Lowest output"
#@ node t 100 "top: $100\,\mathrm{V}$"
#@ node m 76.60 "midpoint: $76.60\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$100\,\mathrm{V}$" col=0 i="$0.851\,\mathrm{mA}$" to=t
#@ el R t m "$27.5\,\mathrm{k\Omega}$: falls $23.40\,\mathrm{V}$" col=1 i="$0.851\,\mathrm{mA}$" to=m
#@ el R m g2 "$90\,\mathrm{k\Omega}$: falls $76.60\,\mathrm{V}$" col=1 i="$0.851\,\mathrm{mA}$" to=g2 plus=m v="$v_o$"
#@ note "Top resistor at its maximum, bottom at its minimum: the midpoint drops to $\dfrac{90}{117.5}$ of the way up."
```

1. Nominal output.

   $$v_{o}=100\cdot\frac{100}{25+100}=80\,\mathrm{V}$$
2. Biggest output: make $R_2$ as big and $R_1$ as small as allowed ($\pm10\%$).

   $$v_{o,\max}=100\cdot\frac{110}{22.5+110}\approx83.02\,\mathrm{V}$$
3. Smallest output: the opposite.

   $$v_{o,\min}=100\cdot\frac{90}{27.5+90}\approx76.60\,\mathrm{V}$$

**Answer:** $v_o=80\,\mathrm{V}$ nominal; $76.60\,\mathrm{V}\le v_o\le83.02\,\mathrm{V}$

**Example: Two current divisions in a row (Lecture 2)**

Find the power dissipated in the $6\,\Omega$ resistor.

```schematic
I1 0,0 -> 0,3 "$10\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$16\,\Omega$"
R2 3,3 -> 6,3 "$1.6\,\Omega$" i="$i_B$"
R3 6,3 -> 6,0 "$4\,\Omega$"
wire 6,3 -> 9,3
R4 9,3 -> 9,0 "$6\,\Omega$" i="$i_6$"
wire 9,0 -> 0,0
#@ node t 32 "top: $32\,\mathrm{V}$"
#@ node c 19.2 "after the $1.6\,\Omega$: $19.2\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g4 0 "bottom: $0\,\mathrm{V}$" ground
#@ el I g t "$10\,\mathrm{A}$" col=0 i="$10\,\mathrm{A}$" to=t id=es rail
#@ el R t g2 "$16\,\Omega$: falls $32\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=e16
#@ el R t c "$1.6\,\Omega$: falls $12.8\,\mathrm{V}$" col=2 i="$8\,\mathrm{A}$" to=c id=eB
#@ el R c g3 "$4\,\Omega$: falls $19.2\,\mathrm{V}$" col=2 i="$4.8\,\mathrm{A}$" to=g3 id=e4
#@ el R c g4 "$6\,\Omega$: falls $19.2\,\mathrm{V}$" col=3 i="$3.2\,\mathrm{A}$" to=g4 id=e6
#@ step "Ground the bottom. The $10\,\mathrm{A}$ source fixes the current it lifts, not the top's height." show=t
#@ step "First split, at the top: the $16\,\Omega$ branch and the $1.6+(4\parallel6)=4\,\Omega$ branch fall the same height, so the $4\,\Omega$ branch takes $\dfrac{16}{16+4}$ of the current: $i_B=8\,\mathrm{A}$, leaving $2\,\mathrm{A}$ for the $16\,\Omega$." show=e16,eB
#@ step "So the top is at $(2)(16)=32\,\mathrm{V}$, and the $1.6\,\Omega$ falls $(8)(1.6)=12.8\,\mathrm{V}$ to $19.2\,\mathrm{V}$." show=t,c,es
#@ step "Second split: the $4\,\Omega$ and the $6\,\Omega$ both fall $19.2\,\mathrm{V}$, so they carry $\dfrac{19.2}{4}=4.8\,\mathrm{A}$ and $i_6=\dfrac{19.2}{6}=3.2\,\mathrm{A}$ ($4.8+3.2=8$)." show=e4,e6
#@ step "Power in the $6\,\Omega$: current × fall $=(3.2)(19.2)=61.44\,\mathrm{W}$."
```

1. The $4\,\Omega$ and $6\,\Omega$ are parallel; that pair is in series with $1.6\,\Omega$.

   $$4\parallel6=2.4\,\Omega,\qquad 1.6+2.4=4\,\Omega$$
2. First split: $10\,\mathrm{A}$ between the $16\,\Omega$ and that $4\,\Omega$ branch (other resistor on top).

   $$i_B=10\cdot\frac{16}{16+4}=8\,\mathrm{A}$$
3. Second split: divide the **branch** current $8\,\mathrm{A}$, not the source's $10\,\mathrm{A}$.

   $$i_6=8\cdot\frac{4}{4+6}=3.2\,\mathrm{A}$$
4. Power.

   $$p_6=6(3.2)^2=61.44\,\mathrm{W}$$

**Answer:** $i_6=3.2\,\mathrm{A}$, $p_{6\Omega}=61.44\,\mathrm{W}$

**Problem: Try it 5 · Two dividers, one rail (Textbook P3.29)** (introductory)

**(a)** Find $v_x$ using voltage division. **(b)** Replace the $18\,\mathrm{V}$ source with a general $V_s$ ($+$ at the top) and find $v_x$ as a function of $V_s$.

```schematic
V1 0,4 -> 0,0 "$18\,\mathrm{V}$"
wire 0,4 -> 6,4
R1 3,4 -> 3,2 "$2\,\mathrm{k\Omega}$" flip
R2 3,2 -> 3,0 "$6\,\mathrm{k\Omega}$" flip
R3 6,4 -> 6,2 "$9\,\mathrm{k\Omega}$" flip
R4 6,2 -> 6,0 "$3\,\mathrm{k\Omega}$" flip
gap 3,2 -> 6,2 v="$v_x$"
wire 6,0 -> 0,0
#@ spoiler
#@ node t 18 "top: $18\,\mathrm{V}$"
#@ node L 13.5 "left midpoint: $13.5\,\mathrm{V}$"
#@ node R 4.5 "right midpoint: $4.5\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$18\,\mathrm{V}$" col=0 i="$3.75\,\mathrm{mA}$" to=t id=es
#@ el R t L "$2\,\mathrm{k\Omega}$: falls $4.5\,\mathrm{V}$" col=1 i="$2.25\,\mathrm{mA}$" to=L id=e2
#@ el R L g2 "$6\,\mathrm{k\Omega}$: falls $13.5\,\mathrm{V}$" col=1 i="$2.25\,\mathrm{mA}$" to=g2 id=e6
#@ el R t R "$9\,\mathrm{k\Omega}$: falls $13.5\,\mathrm{V}$" col=2 i="$1.5\,\mathrm{mA}$" to=R id=e9
#@ el R R g3 "$3\,\mathrm{k\Omega}$: falls $4.5\,\mathrm{V}$" col=2 i="$1.5\,\mathrm{mA}$" to=g3 id=e3
#@ step "Ground the bottom; the source holds the top at $18\,\mathrm{V}$. Two separate slopes hang from that rail: $2+6\,\mathrm{k\Omega}$ on the left, $9+3\,\mathrm{k\Omega}$ on the right."
#@ step "Left divider: its midpoint sits $\dfrac{6}{8}$ of the way up, at $13.5\,\mathrm{V}$." show=L,e2,e6
#@ step "Right divider: its midpoint sits $\dfrac{3}{12}$ of the way up, at $4.5\,\mathrm{V}$." show=R,e9,e3
#@ step "$v_x$ is + on the left, so it is the left height minus the right height: $13.5-4.5=9\,\mathrm{V}$. For a general $V_s$ both heights scale with it: $v_x=V_s\left(\tfrac{6}{8}-\tfrac{3}{12}\right)=\tfrac12V_s$." show=es
#@ note "Like a Wheatstone bridge without the detector: $v_x$ is the height difference between the two midpoints."
```

<details><summary>Solution</summary>

1. Convert: one rail at $18\,\mathrm{V}$, two separate slopes to ground. Each midpoint sits at its own divider fraction of the way up.

   $$\begin{aligned}&V_L=18\cdot\frac{6}{2+6}=13.5\,\mathrm{V},\\&V_R=18\cdot\frac{3}{9+3}=4.5\,\mathrm{V}\end{aligned}$$
2. **(a)** $v_x$ is $+$ at the left midpoint.

   $$v_x=V_L-V_R=13.5-4.5=9\,\mathrm{V}$$
3. **(b)** Every height scales with the rail.

   $$v_x=V_s\left(\frac{6}{8}-\frac{3}{12}\right)=0.5\,V_s$$

**Answer:** **(a)** $v_x=9\,\mathrm{V}$. **(b)** $v_x=\dfrac{V_s}{2}$.

</details>

**Problem: Try it 6 · Three branches share one height (Textbook P3.19)** (introductory)

Find the power dissipated in the $1.2\,\mathrm{k}\Omega$ resistor.

```schematic
I1 0,0 -> 0,3 "$320\,\mathrm{mA}$"
wire 0,3 -> 9,3
R1 3,3 -> 3,0 "$800\,\Omega$"
R2 6,3 -> 6,0 "$2.4\,\mathrm{k\Omega}$"
R3 9,3 -> 9,0 "$1.2\,\mathrm{k\Omega}$"
wire 9,0 -> 0,0
#@ spoiler
#@ node t 128 "top: $128\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g4 0 "bottom: $0\,\mathrm{V}$" ground
#@ el I g t "$320\,\mathrm{mA}$" col=0 i="$320\,\mathrm{mA}$" to=t id=es rail
#@ el R t g2 "$800\,\Omega$" col=1 i="$160\,\mathrm{mA}$" to=g2 id=e1
#@ el R t g3 "$2.4\,\mathrm{k\Omega}$" col=2 i="$53.3\,\mathrm{mA}$" to=g3 id=e2
#@ el R t g4 "$1.2\,\mathrm{k\Omega}$" col=3 i="$106.7\,\mathrm{mA}$" to=g4 id=e3
#@ step "All three resistors hang from the same top level to ground, so they share one fall $v$, and the source's $320\,\mathrm{mA}$ splits among them."
#@ step "Side by side they make $R_{\mathrm{eq}}=400\,\Omega$, so the top sits at $(0.32)(400)=128\,\mathrm{V}$." show=t
#@ step "Each current is fall ÷ $R$: $160$, $53.3$ and $106.7\,\mathrm{mA}$ (they add to $320$). The $1.2\,\mathrm{k\Omega}$ absorbs $(128)(0.1067)=\dfrac{128^2}{1200}=13.65\,\mathrm{W}$." show=e1,e2,e3,es
```

<details><summary>Solution</summary>

1. All three resistors span the same two wires, so they share one height $v$. Find it from the total current.

   $$\begin{aligned}R_{\mathrm{eq}}&=\left(\frac{1}{800}+\frac{1}{2400}+\frac{1}{1200}\right)^{-1}=400\,\Omega\\ v&=(0.32)(400)=128\,\mathrm{V}\end{aligned}$$
2. Power from the height: $v^2/R$.

   $$p_{1.2\mathrm{k}}=\frac{128^2}{1200}\approx13.65\,\mathrm{W}$$

**Answer:** $p_{1.2\,\mathrm{k}\Omega}=\dfrac{1024}{75}\approx13.65\,\mathrm{W}$

</details>

**Problem: Try it 7 · Find the load from the sag (Textbook P3.12)** (intermediate)

With no load, $v_o=25\,\mathrm{V}$. When the load $R_L$ is connected across $a$–$b$, $v_o$ drops to $15\,\mathrm{V}$. Find $R_L$.

```schematic
V1 0,3 -> 0,0 "$75\,\mathrm{V}$"
R1 0,3 -> 3,3 "$100\,\Omega$"
R2 3,3 -> 3,0 "$R_2$" v="$v_o$" flip
wire 3,3 -> 5,3
wire 3,0 -> 5,0
wire 3,0 -> 0,0
terminal 5,3 "a" right
terminal 5,0 "b" right
terminal 8,3
R3 8,3 -> 8,0 "$R_L$"
terminal 8,0
#@ spoiler
#@ view "No load"
#@ node t 75 "top: $75\,\mathrm{V}$"
#@ node m 25 "$a$: $25\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V t g "$75\,\mathrm{V}$" col=0 i="$0.5\,\mathrm{A}$" to=t id=es
#@ el R t m "$100\,\Omega$: falls $50\,\mathrm{V}$" col=1 i="$0.5\,\mathrm{A}$" to=m id=e1
#@ el R m g2 "$R_2=50\,\Omega$" col=1 i="$0.5\,\mathrm{A}$" to=g2 id=e2 plus=m v="$v_o$"
#@ step "Ground $b$ (the bottom wire); the top is at $75\,\mathrm{V}$. Unloaded, the midpoint sits at the given $25\,\mathrm{V}$, so the $100\,\Omega$ falls $50\,\mathrm{V}$: $0.5\,\mathrm{A}$ flows down the whole chain." show=e1,es
#@ step "$R_2$ falls the remaining $25\,\mathrm{V}$ with that same $0.5\,\mathrm{A}$: $R_2=\dfrac{25}{0.5}=50\,\Omega$." show=e2
#@ view "Load connected"
#@ node t 75 "top: $75\,\mathrm{V}$"
#@ node m 15 "$a$: $15\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V t g "$75\,\mathrm{V}$" col=0 i="$0.6\,\mathrm{A}$" to=t id=es
#@ el R t m "$100\,\Omega$: falls $60\,\mathrm{V}$" col=1 i="$0.6\,\mathrm{A}$" to=m id=e1
#@ el R m g2 "$R_2=50\,\Omega$" col=1 i="$0.3\,\mathrm{A}$" to=g2 id=e2 plus=m v="$v_o$"
#@ el R m g3 "$R_L=50\,\Omega$" col=2 i="$0.3\,\mathrm{A}$" to=g3 id=eL
#@ step "Same ground ($b$). With the load the midpoint sags to the given $15\,\mathrm{V}$, so the $100\,\Omega$ falls $60\,\mathrm{V}$: $0.6\,\mathrm{A}$." show=e1,es
#@ step "At the midpoint the stream splits. $R_2=50\,\Omega$ falls $15\,\mathrm{V}$ and takes $0.3\,\mathrm{A}$, so the load gets the other $0.3\,\mathrm{A}$ for the same $15\,\mathrm{V}$ fall: $R_L=\dfrac{15}{0.3}=50\,\Omega$." show=e2,eL
```

<details><summary>Solution</summary>

1. No load: an ordinary divider gives $R_2$.

   $$25=\frac{75R_2}{100+R_2}\;\Rightarrow\;R_2=50\,\Omega$$
2. With the load, the bottom resistance becomes $R_p=R_2\parallel R_L$ and the midpoint sags to $15\,\mathrm{V}$.

   $$15=\frac{75R_p}{100+R_p}\;\Rightarrow\;R_p=25\,\Omega$$
3. Undo the parallel.

   $$\frac{1}{R_L}=\frac{1}{25}-\frac{1}{50}\;\Rightarrow\;R_L=50\,\Omega$$

**Answer:** $R_L=50\,\Omega$ (with $R_2=50\,\Omega$)

</details>

## Topic 5: Meters and the Wheatstone bridge

|  | Ammeter | Voltmeter |
|---|---|---|
| Connect it | **in series** (current flows through it) | **across** the two points (in parallel) |
| Ideal | a wire ($0\,\Omega$): no step | a gap ($\infty\,\Omega$): draws nothing |
| Real | a small resistance: steals a little of the fall | a big resistance: drags the node it touches down |
| Rule | its $R$ should be $\le\dfrac1{10}$ of the smallest $R$ in the circuit | its $R$ should be much bigger than what it's across |

```schematic
V1 0,3 -> 0,0 "$v_s$"
R1 0,3 -> 3,3 "$R_1$"
AM1 3,3 -> 6,3
R2 6,3 -> 6,0 "$R_2$"
wire 6,3 -> 9,3
VM1 9,3 -> 9,0
wire 9,0 -> 0,0
```

- **Analog meter (d'Arsonval movement):** full scale at $I_m$ and $V_m$, so $R_m=V_m/I_m$.
- **Make an ammeter:** put a shunt $R_A$ **in parallel**; it carries the extra current: $R_A=\dfrac{V_m}{I_{FS}-I_m}$.
- **Make a voltmeter:** put $R_v$ **in series**; the full-scale voltage drives $I_m$: $R_v=\dfrac{V_{FS}}{I_m}-R_m$.
- **Before predicting a reading,** put the meter's resistance into the circuit and solve again.

**Example: Designing an ammeter and a voltmeter (Lecture 2)**

A d'Arsonval movement ($R_m$) reads full scale at $50\,\mathrm{mV}$ and $1\,\mathrm{mA}$.

1. Find the shunt $R_A$ for a $10\,\mathrm{mA}$ full-scale ammeter (left).
2. Find the series resistor $R_v$ for a $150\,\mathrm{V}$ full-scale voltmeter (right).

```schematic
terminal 0,3 "$u$" left
terminal 0,0 left
wire 0,3 -> 4,3
wire 0,0 -> 4,0
R1 2,3 -> 2,0 "$R_m$"
R2 4,3 -> 4,0 "$R_A$"
terminal 7,3 "$u$" left
terminal 7,0 left
R3 7,3 -> 10,3 "$R_v$"
R4 10,3 -> 10,0 "$R_m$"
wire 10,0 -> 7,0
```

1. Movement resistance.

   $$R_m=\frac{0.050}{0.001}=50\,\Omega$$
2. Ammeter: the movement takes $1\,\mathrm{mA}$, so the shunt takes the other $9\,\mathrm{mA}$ at the same $50\,\mathrm{mV}$.

   $$R_A=\frac{0.050}{0.009}=\frac{50}{9}\approx5.556\,\Omega$$
3. The whole ammeter is $R_m\parallel R_A$: that's what it adds to a circuit.

   $$50\parallel\frac{50}{9}=5\,\Omega$$
4. Voltmeter: $150\,\mathrm{V}$ must drive $1\,\mathrm{mA}$ through $R_v+R_m$.

   $$150=0.001(R_v+50)\;\Rightarrow\;R_v=149.95\,\mathrm{k\Omega}\quad(\text{total }150\,\mathrm{k\Omega})$$

**Answer:** $R_A=\dfrac{50}{9}\approx5.556\,\Omega$ (ammeter resistance $5\,\Omega$); $R_v=149.95\,\mathrm{k}\Omega$ (voltmeter resistance $150\,\mathrm{k}\Omega$)

**Problem: Try it 8 · A voltmeter drags the node down (Assessment AP 3.6)** (intermediate)

Find $v$ before the meter is connected. Then find the reading of the $150\,\mathrm{V}$ voltmeter designed above (internal resistance $150\,\mathrm{k}\Omega$).

```schematic
V1 0,3 -> 0,0 "$60\,\mathrm{V}$"
R1 0,3 -> 3,3 "$15\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$75\,\mathrm{k\Omega}$" v="$v$"
wire 3,3 -> 6,3
VM1 6,3 -> 6,0
wire 6,0 -> 0,0
#@ view "Before the meter"
#@ node t 60 "top: $60\,\mathrm{V}$"
#@ node m 50 "midpoint: $50\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$60\,\mathrm{V}$" col=0 i="$0.667\,\mathrm{mA}$" to=t
#@ el R t m "$15\,\mathrm{k\Omega}$: falls $10\,\mathrm{V}$" col=1 i="$0.667\,\mathrm{mA}$" to=m
#@ el R m g2 "$75\,\mathrm{k\Omega}$: falls $50\,\mathrm{V}$" col=1 i="$0.667\,\mathrm{mA}$" to=g2 plus=m v="$v$"
#@ note "Unloaded divider: the midpoint sits $\dfrac{75}{90}$ of the way up, at $50\,\mathrm{V}$."
#@ view "Meter connected"
#@ node t 60 "top: $60\,\mathrm{V}$"
#@ node m 46.15 "midpoint: $46.15\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$60\,\mathrm{V}$" col=0 i="$0.923\,\mathrm{mA}$" to=t id=es
#@ el R t m "$15\,\mathrm{k\Omega}$: falls $13.85\,\mathrm{V}$" col=1 i="$0.923\,\mathrm{mA}$" to=m id=e15
#@ el R m g2 "$75\,\mathrm{k\Omega}$: falls $46.15\,\mathrm{V}$" col=1 i="$0.615\,\mathrm{mA}$" to=g2 id=e75 plus=m v="$v$"
#@ el R m g3 "voltmeter $150\,\mathrm{k\Omega}$" col=2 i="$0.308\,\mathrm{mA}$" to=g3 id=evm
#@ step "A real voltmeter is a $150\,\mathrm{k\Omega}$ path from the midpoint to ground, side by side with the $75\,\mathrm{k\Omega}$: together they make $75\parallel150=50\,\mathrm{k\Omega}$."
#@ step "Now the bottom of the divider is $50\,\mathrm{k\Omega}$, so the midpoint sits $\dfrac{50}{65}$ of the way up: $46.15\,\mathrm{V}$. The meter pulled the height it is measuring down by almost $4\,\mathrm{V}$." show=m
#@ step "More current flows ($\dfrac{60}{65\,\mathrm{k\Omega}}=0.923\,\mathrm{mA}$), so the $15\,\mathrm{k\Omega}$ falls more ($13.85\,\mathrm{V}$); at the midpoint the stream splits $0.615\,\mathrm{mA}$ / $0.308\,\mathrm{mA}$." show=es,e15,e75,evm
```

<details><summary>Solution</summary>

1. Before the meter: an unloaded divider.

   $$v=60\cdot\frac{75}{15+75}=50\,\mathrm{V}$$
2. The $150\,\mathrm{k\Omega}$ voltmeter is a second path down, in parallel with the $75\,\mathrm{k\Omega}$.

   $$75\parallel150=50\,\mathrm{k\Omega}$$
3. Divide again with the new bottom resistance.

   $$v_{\text{read}}=60\cdot\frac{50}{15+50}\approx46.15\,\mathrm{V}$$

**Answer:** $v=50\,\mathrm{V}$; the voltmeter reads $46.15\,\mathrm{V}$.

</details>

**Problem: Try it 9 · What does the ammeter read? (Assessment AP 3.5)** (intermediate)

1. Find the current $i$ in the circuit without a meter.
2. The analog ammeter designed in Lecture 2 ($5\,\Omega$ terminal resistance) is inserted as shown. What does it read?

```schematic
V1 0,3 -> 0,0 "$1\,\mathrm{V}$"
AM1 0,3 -> 3,3
R1 3,3 -> 3,0 "$100\,\Omega$" i="$i$"
wire 3,0 -> 0,0
#@ spoiler
#@ view "Without a meter"
#@ node t 1 "top: $1\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$1\,\mathrm{V}$" col=0 i="$10\,\mathrm{mA}$" to=t
#@ el R t g2 "$100\,\Omega$: falls $1\,\mathrm{V}$" col=1 i="$10\,\mathrm{mA}$" to=g2
#@ note "An ideal ammeter is a wire (no step), so the resistor falls the full $1\,\mathrm{V}$: $10\,\mathrm{mA}$."
#@ view "With the 5 Ω ammeter"
#@ node t 1 "top: $1\,\mathrm{V}$"
#@ node m 0.952 "after the meter: $0.952\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$1\,\mathrm{V}$" col=0 i="$9.524\,\mathrm{mA}$" to=t id=es
#@ el R t m "ammeter $5\,\Omega$: falls $0.048\,\mathrm{V}$" col=1 i="$9.524\,\mathrm{mA}$" to=m id=eA
#@ el R m g2 "$100\,\Omega$: falls $0.952\,\mathrm{V}$" col=1 i="$9.524\,\mathrm{mA}$" to=g2 id=eR
#@ step "Ground the bottom wire; the top is at $1\,\mathrm{V}$. The real ammeter is a $5\,\Omega$ slope in the path it measures: $105\,\Omega$ in all, so the current, which is what the meter reads, is $\dfrac{1}{105}=9.524\,\mathrm{mA}$." show=es,eA,eR
#@ step "The meter steals a $(9.524\,\mathrm{mA})(5\,\Omega)=0.048\,\mathrm{V}$ step, so the resistor gets only $0.952\,\mathrm{V}$ instead of $1\,\mathrm{V}$: about $5\%$ less current." show=m
```

<details><summary>Solution</summary>

1. Without the meter.

   $$i=\frac{1}{100}=10\,\mathrm{mA}$$
2. The meter designed above is a $5\,\Omega$ resistor in series.

   $$i_{\text{read}}=\frac{1}{100+5}\approx9.524\,\mathrm{mA}$$
3. About $5\%$ low: the meter's own small slope takes part of the $1\,\mathrm{V}$.

**Answer:** **(1)** $i=10\,\mathrm{mA}$ **(2)** the ammeter reads $9.524\,\mathrm{mA}$

</details>

### The Wheatstone bridge

- Two dividers hang from the same supply; a detector (galvanometer) connects their midpoints.
- **Balanced** = no detector current = both midpoints at the **same height**.
- At balance, each side is a plain divider, so the ratios match: $R_1R_x=R_2R_3$ ($R_1$ above $R_3$ on the left, $R_2$ above $R_x$ on the right).
- **Not balanced:** the midpoints sit at different heights, and the detector carries current from the higher one to the lower one. An ideal detector (no step) forces them level instead: the four arms become two side-by-side pairs, one pair above the shared midpoint and one below (Try it 10).

$$R_x=\frac{R_2R_3}{R_1}$$

**Example: Balanced bridge and resistor ratings (Assessment AP 3.7)**

The bridge is balanced (no galvanometer current). Find $R_x$, and check whether any resistor exceeds a $250\,\mathrm{mW}$ rating.

```schematic
V1 0,6 -> 0,0 "$5\,\mathrm{V}$"
wire 0,6 -> 6,6
R1 3,6 -> 3,3 "$100\,\Omega$"
R3 3,3 -> 3,0 "$150\,\Omega$"
R2 6,6 -> 6,3 "$1\,\mathrm{k\Omega}$"
R4 6,3 -> 6,0 "$R_x$"
AM1 3,3 -> 6,3 "galvanometer"
wire 6,0 -> 0,0
#@ node t 5 "top: $5\,\mathrm{V}$"
#@ node b 3 "left midpoint: $3\,\mathrm{V}$"
#@ node c 3 "right midpoint: $3\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$5\,\mathrm{V}$" col=0 i="$22\,\mathrm{mA}$" to=t id=es
#@ el R t b "$100\,\Omega$: falls $2\,\mathrm{V}$" col=1 i="$20\,\mathrm{mA}$" to=b id=e1
#@ el R b g2 "$150\,\Omega$: falls $3\,\mathrm{V}$" col=1 i="$20\,\mathrm{mA}$" to=g2 id=e3
#@ el X b c "galvanometer: level, no current" col=1 id=eg
#@ el R t c "$1\,\mathrm{k\Omega}$: falls $2\,\mathrm{V}$" col=2 i="$2\,\mathrm{mA}$" to=c id=e2
#@ el R c g3 "$R_x$: falls $3\,\mathrm{V}$" col=2 i="$2\,\mathrm{mA}$" to=g3 id=ex
#@ step "Ground the bottom; the source holds the top at $5\,\mathrm{V}$. Balanced means no galvanometer current, so the two sides are separate dividers hanging from the same $5\,\mathrm{V}$ rail."
#@ step "Left side: one current, $\dfrac{5}{100+150}=20\,\mathrm{mA}$. The $100\,\Omega$ falls $2\,\mathrm{V}$, so the left midpoint sits at $3\,\mathrm{V}$." show=e1,e3,b
#@ step "No current through the galvanometer means no height difference across it: the right midpoint is also at $3\,\mathrm{V}$. So the $1\,\mathrm{k\Omega}$ falls $2\,\mathrm{V}$ ($2\,\mathrm{mA}$) and $R_x$ falls $3\,\mathrm{V}$ with the same $2\,\mathrm{mA}$: $R_x=\dfrac{3}{0.002}=1.5\,\mathrm{k\Omega}$." show=c,eg,e2,ex
#@ step "Ratings: power = current × fall. The largest is the $150\,\Omega$: $(20\,\mathrm{mA})(3\,\mathrm{V})=60\,\mathrm{mW}<250\,\mathrm{mW}$." show=es
#@ note "Balance in one picture: the detector lies flat because both sides divide the same rail in the same ratio."
```

1. Balance formula.

   $$R_x=\frac{(1000)(150)}{100}=1500\,\Omega$$
2. No detector current, so each side is one series path with its own current.

   $$i_{\text{left}}=\frac{5}{250}=20\,\mathrm{mA},\qquad i_{\text{right}}=\frac{5}{2500}=2\,\mathrm{mA}$$
3. Each resistor's power, $i^2R$.

   $$\begin{aligned}&100(0.02)^2=40\,\mathrm{mW},\quad 150(0.02)^2=60\,\mathrm{mW}\\&1000(0.002)^2=4\,\mathrm{mW},\quad 1500(0.002)^2=6\,\mathrm{mW}\end{aligned}$$
4. The largest is $60\,\mathrm{mW}<250\,\mathrm{mW}$. Both midpoints sit at $3\,\mathrm{V}$ (level, as balance requires).

**Answer:** $R_x=1.5\,\mathrm{k}\Omega$; the largest dissipation is $60\,\mathrm{mW}$, so every resistor is within its rating.

**Problem: Try it 10 · An unbalanced bridge (Textbook P3.53)** (intermediate)

The bridge below is **not** balanced, and the voltage drop across the detector is negligible. Find the detector current $i_d$.

```schematic
V1 0,6 -> 0,0 "$50\,\mathrm{V}$"
wire 0,6 -> 6,6
R1 3,6 -> 3,3 "$15\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$9\,\mathrm{k\Omega}$"
R3 6,6 -> 6,3 "$3\,\mathrm{k\Omega}$" flip
R4 6,3 -> 6,0 "$45\,\mathrm{k\Omega}$" flip
AM1 3,3 -> 6,3 "detector" i="$i_d$"
wire 6,0 -> 0,0
ground 0,0
#@ spoiler
#@ node t 50 "top: $50\,\mathrm{V}$"
#@ node L 37.5 "midpoints: $37.5\,\mathrm{V}$"
#@ node R 37.5 "midpoints: $37.5\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$50\,\mathrm{V}$" col=0 i="$5\,\mathrm{mA}$" to=t id=es
#@ el R t L "$15\,\mathrm{k\Omega}$: falls $12.5\,\mathrm{V}$" col=1 i="$0.833\,\mathrm{mA}$" to=L id=e15
#@ el R L g2 "$9\,\mathrm{k\Omega}$: falls $37.5\,\mathrm{V}$" col=1 i="$4.167\,\mathrm{mA}$" to=g2 id=e9
#@ el W L R "detector: no step" col=1 i="$3.33\,\mathrm{mA}$" to=L id=ed
#@ el R t R "$3\,\mathrm{k\Omega}$: falls $12.5\,\mathrm{V}$" col=2 i="$4.167\,\mathrm{mA}$" to=R id=e3
#@ el R R g3 "$45\,\mathrm{k\Omega}$: falls $37.5\,\mathrm{V}$" col=2 i="$0.833\,\mathrm{mA}$" to=g3 id=e45
#@ step "Ground the bottom wire; the source holds the top at $50\,\mathrm{V}$. The detector has no step, so it forces both midpoints to **one** height. Call it $m$."
#@ step "That changes the shape: the $15\,\mathrm{k\Omega}$ and $3\,\mathrm{k\Omega}$ both fall from the top to $m$ (side by side: $2.5\,\mathrm{k\Omega}$), and the $9\,\mathrm{k\Omega}$ and $45\,\mathrm{k\Omega}$ both fall from $m$ to ground ($7.5\,\mathrm{k\Omega}$). So $m$ sits $\dfrac{7.5}{10}$ of the way up: $37.5\,\mathrm{V}$." show=L,R
#@ step "Each resistor's current is its fall ÷ R. Left: $\dfrac{12.5}{15}=0.833\,\mathrm{mA}$ in, $\dfrac{37.5}{9}=4.167\,\mathrm{mA}$ out. Right: $\dfrac{12.5}{3}=4.167\,\mathrm{mA}$ in, $\dfrac{37.5}{45}=0.833\,\mathrm{mA}$ out." show=e15,e9,e3,e45,es
#@ step "The detector is flat, so its current can't be read from a fall: only KCL gives it. The left midpoint is short $4.167-0.833=3.33\,\mathrm{mA}$, and the right one has exactly that much spare. So $3.33\,\mathrm{mA}$ crosses from right to left, against the $i_d$ arrow: $i_d=-3.33\,\mathrm{mA}$." show=ed
#@ step "Power check: the source lifts $5\,\mathrm{mA}$ through $50\,\mathrm{V}$ ($250\,\mathrm{mW}$); the falls absorb $10.4+156.3+52.1+31.3=250\,\mathrm{mW}$. The detector absorbs nothing: it has no fall."
#@ note "An ideal detector keeps the two midpoints level even when the bridge is unbalanced; the imbalance shows up as current through it instead."
```

<details><summary>Solution</summary>

1. The detector has (almost) no drop, so both midpoints are at the same height $v_m$. Now the $15$ and $3\,\mathrm{k\Omega}$ sit side by side above that node, and the $9$ and $45\,\mathrm{k\Omega}$ side by side below it.

   $$15\parallel3=\frac{(15)(3)}{18}=2.5\,\mathrm{k\Omega},\qquad 9\parallel45=\frac{(9)(45)}{54}=7.5\,\mathrm{k\Omega}$$
2. Divide the $50\,\mathrm{V}$.

   $$v_m=50\cdot\frac{7.5}{2.5+7.5}=37.5\,\mathrm{V}$$
3. Currents on the left side, as fall ÷ R (mA and kΩ).

   $$i_{15}=\frac{50-37.5}{15}=0.833\,\mathrm{mA},\qquad i_9=\frac{37.5}{9}=4.167\,\mathrm{mA}$$
4. KCL at the left midpoint: $i_d$ leaves it (arrow to the right).

   $$i_{15}=i_9+i_d\;\Rightarrow\;i_d=0.833-4.167=-3.33\,\mathrm{mA}$$

**Answer:** $i_d=-\dfrac{10}{3}\approx-3.33\,\mathrm{mA}$: $3.33\,\mathrm{mA}$ flows through the detector from right to left.

</details>

**Problem: Try it 11 · A bridge that drifts off balance (Textbook P3.66)** (advanced)

The bridge is balanced when $\Delta R=0$. The output $v_o$ is $+$ at the left midpoint.

```schematic
V1 0,6 -> 0,0 "$v_{\mathrm{in}}$"
wire 0,6 -> 6,6
R1 3,6 -> 3,3 "$R_o+\Delta R$"
R2 3,3 -> 3,0 "$R_4$"
R3 6,6 -> 6,3 "$R_2$" flip
R4 6,3 -> 6,0 "$R_3$" flip
gap 3,3 -> 6,3 v="$v_o$"
wire 6,0 -> 0,0
ground 0,0
#@ spoiler
#@ view "Balanced: ΔR = 0"
#@ node t 10 "top: $10\,\mathrm{V}$"
#@ node L 2.5 "midpoints: $2.5\,\mathrm{V}$"
#@ node R 2.5 "midpoints: $2.5\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$10\,\mathrm{V}$" col=0 i="$12.5\,\mathrm{mA}$" to=t id=es
#@ el R t L "$R_o$: $3\,\mathrm{k\Omega}$, falls $7.5\,\mathrm{V}$" col=1 i="$2.5\,\mathrm{mA}$" to=L id=e1
#@ el R L g2 "$R_4$: falls $2.5\,\mathrm{V}$" col=1 i="$2.5\,\mathrm{mA}$" to=g2 id=e4
#@ el S L R "gap: level" col=1 plus=L v="$v_o$" id=eo
#@ el R t R "$R_2$: falls $7.5\,\mathrm{V}$" col=2 i="$10\,\mathrm{mA}$" to=R id=e2
#@ el R R g3 "$R_3$: falls $2.5\,\mathrm{V}$" col=2 i="$10\,\mathrm{mA}$" to=g3 id=e3
#@ step "Ground the bottom wire; the top is at $10\,\mathrm{V}$ (part b). The right divider is fully known: its midpoint sits $\dfrac{250}{1000}$ of the way up, at $2.5\,\mathrm{V}$." show=R,e2,e3
#@ step "Balanced means the two midpoints are level, so the left one is at $2.5\,\mathrm{V}$ too. Then $R_4$ takes a quarter of the fall and $R_o$ three quarters: $R_o=3R_4=3\,\mathrm{k\Omega}$." show=L,e1,e4,eo,es
#@ view "Off balance: ΔR = 60 Ω"
#@ node t 10 "top: $10\,\mathrm{V}$"
#@ node R 2.5 "right midpoint: $2.5\,\mathrm{V}$"
#@ node L 2.4631 "left midpoint: $2.463\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$10\,\mathrm{V}$" col=0 i="$12.46\,\mathrm{mA}$" to=t id=es
#@ el R t L "$3060\,\Omega$: falls $7.537\,\mathrm{V}$" col=1 i="$2.463\,\mathrm{mA}$" to=L id=e1
#@ el R L g2 "$R_4$: falls $2.463\,\mathrm{V}$" col=1 i="$2.463\,\mathrm{mA}$" to=g2 id=e4
#@ el S L R "gap: $36.95\,\mathrm{mV}$" col=2 plus=L v="$v_o$" id=eo
#@ el R t R "$R_2$: falls $7.5\,\mathrm{V}$" col=3 i="$10\,\mathrm{mA}$" to=R id=e2
#@ el R R g3 "$R_3$: falls $2.5\,\mathrm{V}$" col=3 i="$10\,\mathrm{mA}$" to=g3 id=e3
#@ step "Same ground (the bottom wire). The right divider doesn't change: its midpoint stays at $2.5\,\mathrm{V}$." show=R,e2,e3
#@ step "$\Delta R=0.02(3000)=60\,\Omega$ makes the left chain $1.5\%$ longer ($\dfrac{60}{4000}$), so about $1.5\%$ less current flows down it. The left midpoint is $R_4\times$ that current, so it sags by about $1.5\%$ of $2.5\,\mathrm{V}$: $37.5\,\mathrm{mV}$. That is the estimate in part (b)." show=e1,es
#@ step "Exactly: the left midpoint sits at $10\cdot\dfrac{1000}{4060}=2.463\,\mathrm{V}$." show=L,e4
#@ step "$v_o$ is $+$ on the left, so it is left height minus right height: $2.463-2.5=-36.95\,\mathrm{mV}$. Negative: the left midpoint is the lower one." show=eo
#@ note "The two midpoints are only $37\,\mathrm{mV}$ apart; the picture spreads the levels so you can see which is higher."
```

**(a)** Show that if $\Delta R\ll R_o$, the bridge output is approximately $v_o\approx\dfrac{-\Delta R\,R_4}{(R_o+R_4)^2}\,v_{\mathrm{in}}$.

**(b)** Given $R_2=750\,\Omega$, $R_3=250\,\Omega$, $R_4=1\,\mathrm{k\Omega}$ and $v_{\mathrm{in}}=10\,\mathrm{V}$, what is the approximate output if $\Delta R$ is $2\%$ of $R_o$?

**(c)** Find the actual value of $v_o$ in part (b).

<details><summary>Solution</summary>

1. Ground the bottom. Each midpoint's height is a divider of $v_{\mathrm{in}}$, and $v_o$ is the left height minus the right height.

   $$\begin{aligned}v_L&=v_{\mathrm{in}}\frac{R_4}{R_o+\Delta R+R_4}\\ v_R&=v_{\mathrm{in}}\frac{R_3}{R_2+R_3}\end{aligned}$$
2. Balanced at $\Delta R=0$ means the midpoints are level, so $v_R$ equals the left height with $\Delta R=0$.

   $$v_o=v_{\mathrm{in}}R_4\left[\frac{1}{R_o+\Delta R+R_4}-\frac{1}{R_o+R_4}\right]$$
3. Combine the fractions.

   $$v_o=\frac{-\Delta R\,R_4\,v_{\mathrm{in}}}{(R_o+\Delta R+R_4)(R_o+R_4)}$$
4. **(a)** If $\Delta R\ll R_o$, drop the $\Delta R$ in the first factor.

   $$v_o\approx\frac{-\Delta R\,R_4}{(R_o+R_4)^2}\,v_{\mathrm{in}}$$
5. **(b)** Balance gives $R_o$; then $\Delta R=0.02R_o$.

   $$\begin{aligned}&R_o=\frac{R_2R_4}{R_3}=\frac{(750)(1000)}{250}=3\,\mathrm{k\Omega},\quad \Delta R=60\,\Omega\\&v_o\approx\frac{-(60)(1000)(10)}{(4000)^2}=-37.5\,\mathrm{mV}\end{aligned}$$
6. **(c)** The exact heights.

   $$\begin{aligned}&v_L=10\cdot\frac{1000}{4060}=2.4631\,\mathrm{V},\quad v_R=2.5\,\mathrm{V}\\&v_o=2.4631-2.5=-36.95\,\mathrm{mV}\end{aligned}$$

**Answer:** **(a)** $v_o=\dfrac{-\Delta R\,R_4\,v_{\mathrm{in}}}{(R_o+\Delta R+R_4)(R_o+R_4)}\approx\dfrac{-\Delta R\,R_4}{(R_o+R_4)^2}\,v_{\mathrm{in}}$ **(b)** $R_o=3\,\mathrm{k\Omega}$, $v_o\approx-37.5\,\mathrm{mV}$ **(c)** $v_o=-36.95\,\mathrm{mV}$

</details>

## Topic 6: Delta–wye (Δ–Y) transformations

- **When:** a bridge, where nothing is in series or parallel.
- A **Δ** (triangle) and a **Y** (three arms meeting at a new center $n$) can act the same at their three corners. Swap one for the other, then reduce normally.
- **Δ → Y:** each arm = (product of the two Δ resistors **touching that corner**) ÷ (sum of all three).
- **Y → Δ** (rarer): each Δ resistor = (sum of the pairwise arm products) ÷ (the arm **opposite** it).
- Check: three equal resistors $R$ in Δ become three arms of $R/3$.
- **In heights:** the corners keep their heights; only the inside changes. To get an original resistor's current, go back to the original circuit.

```schematic
R1 2,6 -> 0,2 "$R_c$"
R2 2,6 -> 4,2 "$R_b$" flip
R3 0,2 -> 4,2 "$R_a$"
label 2,6 "$a$" above
label 0,2 "$b$" left
label 4,2 "$c$" right
R4 10,6 -> 10,4 "$R_1$"
R5 10,4 -> 8,2 "$R_2$"
R6 10,4 -> 12,2 "$R_3$" flip
label 10,6 "$a$" above
label 8,2 "$b$" left
label 12,2 "$c$" right
label 10,4 "$n$" right
```

$$R_1=\frac{R_bR_c}{S},\quad R_2=\frac{R_cR_a}{S},\quad R_3=\frac{R_aR_b}{S},\qquad S=R_a+R_b+R_c$$

**Example: Simplify a bridge with a delta-to-wye transformation (Lecture 2)**

Find the current and the power supplied by the $40\,\mathrm{V}$ source.

```schematic
V1 0,6 -> 0,0 "$40\,\mathrm{V}$" i_rev="$i_s$" flip
R1 0,6 -> 5,6 "$5\,\Omega$"
R2 5,6 -> 3,3 "$100\,\Omega$"
R3 5,6 -> 7,3 "$125\,\Omega$"
R4 3,3 -> 7,3 "$25\,\Omega$"
R5 3,3 -> 5,0 "$40\,\Omega$" flip
R6 7,3 -> 5,0 "$37.5\,\Omega$"
wire 5,0 -> 0,0
label 5,6 "$a$" above
label 3,3 "$b$" left
label 7,3 "$c$" right
#@ view "After Δ→Y"
#@ node t 40 "source +: $40\,\mathrm{V}$"
#@ node a 37.5 "$a$: $37.5\,\mathrm{V}$"
#@ node n 12.5 "center $n$: $12.5\,\mathrm{V}$"
#@ node b 10 "$b$: $10\,\mathrm{V}$"
#@ node c 9.375 "$c$: $9.375\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$40\,\mathrm{V}$" col=0 i="$0.5\,\mathrm{A}$" to=t id=es
#@ el R t a "$5\,\Omega$: falls $2.5\,\mathrm{V}$" col=1 i="$0.5\,\mathrm{A}$" to=a id=e5
#@ el R a n "$R_1=50\,\Omega$: falls $25\,\mathrm{V}$" col=1 i="$0.5\,\mathrm{A}$" to=n id=e50
#@ el R n b "$R_2=10\,\Omega$" col=1 i="$0.25\,\mathrm{A}$" to=b id=e10
#@ el R b g2 "$40\,\Omega$: falls $10\,\mathrm{V}$" col=1 i="$0.25\,\mathrm{A}$" to=g2 id=e40
#@ el R n c "$R_3=12.5\,\Omega$" col=2 i="$0.25\,\mathrm{A}$" to=c id=e125
#@ el R c g3 "$37.5\,\Omega$: falls $9.375\,\mathrm{V}$" col=2 i="$0.25\,\mathrm{A}$" to=g3 id=e375
#@ step "Ground the bottom; the source holds its + end at $40\,\mathrm{V}$. After the swap the circuit is one path down to the new center $n$, then two equal $50\,\Omega$ paths: $R_{\mathrm{in}}=5+50+25=80\,\Omega$, so the source lifts $i_s=0.5\,\mathrm{A}$ ($20\,\mathrm{W}$)." show=es
#@ step "Walk down: the $5\,\Omega$ falls $2.5\,\mathrm{V}$ ($a=37.5\,\mathrm{V}$) and $R_1$ falls $25\,\mathrm{V}$ ($n=12.5\,\mathrm{V}$)." show=e5,a,e50,n
#@ step "The two equal paths split $0.25\,\mathrm{A}$ each: $b=(0.25)(40)=10\,\mathrm{V}$ and $c=(0.25)(37.5)=9.375\,\mathrm{V}$." show=e10,e40,e125,e375,b,c
#@ note "The swap keeps the heights of $a$, $b$ and $c$. Open the other tab to see the original resistors with these same heights."
#@ view "Back to the original bridge"
#@ node t 40 "source +: $40\,\mathrm{V}$"
#@ node a 37.5 "$a$: $37.5\,\mathrm{V}$"
#@ node b 10 "$b$: $10\,\mathrm{V}$"
#@ node c 9.375 "$c$: $9.375\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$40\,\mathrm{V}$" col=0 i="$0.5\,\mathrm{A}$" to=t
#@ el R t a "$5\,\Omega$" col=1 i="$0.5\,\mathrm{A}$" to=a
#@ el R a b "$100\,\Omega$: falls $27.5\,\mathrm{V}$" col=1 i="$0.275\,\mathrm{A}$" to=b id=e100
#@ el R b g2 "$40\,\Omega$" col=1 i="$0.25\,\mathrm{A}$" to=g2
#@ el R b c "$25\,\Omega$: falls $0.625\,\mathrm{V}$" col=2 i="$25\,\mathrm{mA}$" to=c id=e25
#@ el R a c "$125\,\Omega$: falls $28.125\,\mathrm{V}$" col=3 i="$0.225\,\mathrm{A}$" to=c id=e125
#@ el R c g3 "$37.5\,\Omega$" col=3 i="$0.25\,\mathrm{A}$" to=g3
#@ step "Same ground (the bottom wire). Δ→Y keeps the heights of the three terminals, so copy $a=37.5$, $b=10$ and $c=9.375\,\mathrm{V}$ from the other tab."
#@ step "Each original resistor's current is its fall over its resistance: the $100\,\Omega$ carries $\dfrac{27.5}{100}=0.275\,\mathrm{A}$, the $125\,\Omega$ carries $\dfrac{28.125}{125}=0.225\,\mathrm{A}$." show=e100,e125
#@ step "The bridge resistor is nearly level: $b$ is only $0.625\,\mathrm{V}$ above $c$, so the $25\,\Omega$ carries just $25\,\mathrm{mA}$ from $b$ to $c$. KCL at $b$: $0.275$ in, $0.025+0.25$ out." show=e25
```

1. Take the upper triangle $a$-$b$-$c$ (resistors $100$, $125$, $25\,\Omega$).

   $$S=100+125+25=250\,\Omega$$
2. Arm at each corner = product of the two touching it ÷ $S$.

   $$\begin{aligned}R_{an}&=\frac{100\cdot125}{250}=50\,\Omega\\ R_{bn}&=\frac{100\cdot25}{250}=10\,\Omega\\ R_{cn}&=\frac{125\cdot25}{250}=12.5\,\Omega\end{aligned}$$
3. Now each path from $n$ to ground is a plain series pair, and the two paths are parallel.

   $$(10+40)\parallel(12.5+37.5)=50\parallel50=25\,\Omega$$
4. Add the rest in series, then Ohm's law.

   $$\begin{aligned}R_{\mathrm{in}}&=5+50+25=80\,\Omega\\ i_s&=\frac{40}{80}=0.5\,\mathrm{A}\\ p&=(40)(0.5)=20\,\mathrm{W}\end{aligned}$$

**Answer:** $i_s=0.5\,\mathrm{A}$; the source supplies $20\,\mathrm{W}$.

**Problem: Try it 12 · Δ–Y, then find a voltage (Textbook P3.58)** (advanced)

Use a delta-to-wye transformation to find $v$.

```schematic
I1 0,0 -> 0,3 "$2\,\mathrm{A}$" v_rev="$v$"
wire 0,3 -> 0,5
R1 0,5 -> 8,5 "$28\,\Omega$"
wire 8,5 -> 8,3
R2 0,3 -> 4,3 "$20\,\Omega$"
R3 4,3 -> 8,3 "$10\,\Omega$"
R4 4,3 -> 4,0 "$5\,\Omega$"
R5 8,3 -> 8,0 "$105\,\Omega$"
wire 8,0 -> 0,0
#@ spoiler
#@ node a 35 "$a$: $35\,\mathrm{V}$"
#@ node c 15 "$c$: $15\,\mathrm{V}$"
#@ node b 9.2857 "$b$: $9.29\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el I g a "$2\,\mathrm{A}$" col=0 i="$2\,\mathrm{A}$" to=a id=es plus=a v="$v$" rail
#@ el R a c "$28\,\Omega$: falls $20\,\mathrm{V}$" col=1 i="$0.714\,\mathrm{A}$" to=c id=e28
#@ el R c g3 "$105\,\Omega$: falls $15\,\mathrm{V}$" col=1 i="$0.143\,\mathrm{A}$" to=g3 id=e105
#@ el R c b "$10\,\Omega$: falls $5.71\,\mathrm{V}$" col=2 i="$0.571\,\mathrm{A}$" to=b id=e10
#@ el R a b "$20\,\Omega$: falls $25.71\,\mathrm{V}$" col=3 i="$1.286\,\mathrm{A}$" to=b id=e20
#@ el R b g2 "$5\,\Omega$: falls $9.29\,\mathrm{V}$" col=3 i="$1.857\,\mathrm{A}$" to=g2 id=e5
#@ step "Ground the bottom wire. The Δ→Y reduction gives $R_{\mathrm{in}}=17.5\,\Omega$, so the source lifts $2\,\mathrm{A}$ to $v=(2)(17.5)=35\,\mathrm{V}$." show=a
#@ step "In the transformed circuit the $2\,\mathrm{A}$ splits $\dfrac{13}{7}\,\mathrm{A}$ through the $b$ path and $\dfrac{1}{7}\,\mathrm{A}$ through the $c$ path, which puts $b$ at $\dfrac{13}{7}(5)=\dfrac{65}{7}\approx9.29\,\mathrm{V}$ and $c$ at $\dfrac{1}{7}(105)=15\,\mathrm{V}$. The swap keeps these terminal heights." show=b,c
#@ step "Back in the original, each resistor's current is fall ÷ $R$. The picture shows a surprise: $c$ ($15\,\mathrm{V}$) sits **above** $b$, so the $10\,\Omega$ carries $\dfrac{4}{7}\approx0.571\,\mathrm{A}$ from $c$ to $b$." show=e28,e105,e10,e20,e5,es
#@ step "KCL check at $b$: in $\dfrac{9}{7}+\dfrac{4}{7}=\dfrac{13}{7}\,\mathrm{A}$; out through the $5\,\Omega$: $\dfrac{65/7}{5}=\dfrac{13}{7}\,\mathrm{A}$."
```

<details><summary>Solution</summary>

1. The triangle $20$, $10$, $28\,\Omega$ has no series or parallel pairs. Convert it ($S=58\,\Omega$); each arm = product of the two touching that corner ÷ 58.

   $$\begin{aligned}R_{an}&=\frac{20\cdot28}{58}=\frac{280}{29}\approx9.655\,\Omega\\ R_{bn}&=\frac{20\cdot10}{58}=\frac{100}{29}\approx3.448\,\Omega\\ R_{cn}&=\frac{28\cdot10}{58}=\frac{140}{29}\approx4.828\,\Omega\end{aligned}$$
2. Two paths from $n$ to ground (through $b$ and through $c$), side by side.

   $$\begin{aligned}&\left(\tfrac{100}{29}+5\right)\parallel\left(\tfrac{140}{29}+105\right)\\&=8.448\parallel109.83\approx7.845\,\Omega\end{aligned}$$
3. Add the arm at $a$, then the source's height.

   $$R_{\mathrm{in}}=9.655+7.845=17.5\,\Omega,\qquad v=(2)(17.5)=35\,\mathrm{V}$$

**Answer:** $v=35\,\mathrm{V}$

</details>

**Problem: Try it 13 · Pick the triangle with easy numbers (Textbook P3.60)** (advanced)

Find **(a)** $i_1$, **(b)** $v$, **(c)** $i_2$ and **(d)** the power supplied by the voltage source.

```schematic
V1 0,4 -> 0,0 "$750\,\mathrm{V}$"
R1 0,4 -> 3,4 "$5\,\Omega$"
wire 3,6 -> 3,2
R2 3,6 -> 6,6 "$24\,\Omega$" i="$i_1$"
R3 3,2 -> 6,2 "$14\,\Omega$"
R4 6,6 -> 6,2 "$60\,\Omega$" v="$v$"
R5 6,6 -> 9,6 "$120\,\Omega$"
R6 6,2 -> 9,2 "$20\,\Omega$" i="$i_2$"
wire 9,6 -> 9,2
wire 9,4 -> 11,4
R7 11,4 -> 11,0 "$43\,\Omega$"
wire 11,0 -> 0,0
label 3,6 "$a$" above
label 6,6 "$b$" above
label 6,2 "$c$" below
label 9,6 "$d$" above
ground 0,0
#@ spoiler
#@ view "After Δ→Y"
#@ node s 750 "source +: $750\,\mathrm{V}$"
#@ node a 700 "$a$: $700\,\mathrm{V}$"
#@ node b 640 "$b$: $640\,\mathrm{V}$"
#@ node c 595 "$c$: $595\,\mathrm{V}$"
#@ node n 550 "center $n$: $550\,\mathrm{V}$"
#@ node d 430 "$d$: $430\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V s g "$750\,\mathrm{V}$" col=0 i="$10\,\mathrm{A}$" to=s id=es
#@ el R s a "$5\,\Omega$: falls $50\,\mathrm{V}$" col=1 i="$10\,\mathrm{A}$" to=a id=e5
#@ el R a c "$14\,\Omega$: falls $105\,\mathrm{V}$" col=1 i="$7.5\,\mathrm{A}$" to=c id=e14
#@ el R c n "$R_c=6\,\Omega$: falls $45\,\mathrm{V}$" col=1 i="$7.5\,\mathrm{A}$" to=n id=ec
#@ el R n d "$R_d=12\,\Omega$: falls $120\,\mathrm{V}$" col=1 i="$10\,\mathrm{A}$" to=d id=ed
#@ el R d g2 "$43\,\Omega$: falls $430\,\mathrm{V}$" col=1 i="$10\,\mathrm{A}$" to=g2 id=e43
#@ el R a b "$24\,\Omega$: falls $60\,\mathrm{V}$" col=2 i="$2.5\,\mathrm{A}$" to=b id=e24
#@ el R b n "$R_b=36\,\Omega$: falls $90\,\mathrm{V}$" col=2 i="$2.5\,\mathrm{A}$" to=n id=eb
#@ step "Ground the bottom wire; the source's + end is at $750\,\mathrm{V}$. Pick the triangle $b$–$c$–$d$ ($60$, $120$, $20\,\Omega$, sum $200$): its arms come out whole, $R_b=\dfrac{(60)(120)}{200}=36$, $R_c=\dfrac{(60)(20)}{200}=6$, $R_d=\dfrac{(120)(20)}{200}=12\,\Omega$."
#@ step "Now it reduces: $(24+36)\parallel(14+6)=60\parallel20=15\,\Omega$, so $R_{\mathrm{in}}=5+15+12+43=75\,\Omega$ and the source lifts $\dfrac{750}{75}=10\,\mathrm{A}$." show=es
#@ step "Walk down the single stream: the $5\,\Omega$ falls $50\,\mathrm{V}$, so $a=700\,\mathrm{V}$. From the bottom up: the $43\,\Omega$ falls $430\,\mathrm{V}$ ($d=430$), and $R_d$ falls $120\,\mathrm{V}$ above that ($n=550\,\mathrm{V}$)." show=e5,a,e43,d,ed,n
#@ step "Between $a$ ($700$) and $n$ ($550$) both paths fall $150\,\mathrm{V}$: $\dfrac{150}{60}=2.5\,\mathrm{A}$ and $\dfrac{150}{20}=7.5\,\mathrm{A}$. Walk down each: $b=700-(2.5)(24)=640\,\mathrm{V}$, $c=700-(7.5)(14)=595\,\mathrm{V}$." show=e24,eb,e14,ec,b,c
#@ note "The swap keeps the heights of $b$, $c$ and $d$; the other tab puts the original triangle back between them."
#@ view "Back to the original"
#@ node s 750 "source +: $750\,\mathrm{V}$"
#@ node a 700 "$a$: $700\,\mathrm{V}$"
#@ node b 640 "$b$: $640\,\mathrm{V}$"
#@ node c 595 "$c$: $595\,\mathrm{V}$"
#@ node d 430 "$d$: $430\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V s g "$750\,\mathrm{V}$" col=0 i="$10\,\mathrm{A}$" to=s
#@ el R s a "$5\,\Omega$" col=1 i="$10\,\mathrm{A}$" to=a
#@ el R a c "$14\,\Omega$" col=1 i="$7.5\,\mathrm{A}$" to=c id=e14
#@ el R c d "$20\,\Omega$: falls $165\,\mathrm{V}$" col=1 i="$8.25\,\mathrm{A}$" to=d id=e20
#@ el R d g2 "$43\,\Omega$" col=1 i="$10\,\mathrm{A}$" to=g2
#@ el R a b "$24\,\Omega$: falls $60\,\mathrm{V}$" col=2 i="$2.5\,\mathrm{A}$" to=b id=e24
#@ el R b c "$60\,\Omega$: falls $45\,\mathrm{V}$" col=2 i="$0.75\,\mathrm{A}$" to=c id=e60 plus=b v="$v$"
#@ el R b d "$120\,\Omega$: falls $210\,\mathrm{V}$" col=3 i="$1.75\,\mathrm{A}$" to=d id=e120
#@ step "Same ground (the bottom wire). Δ→Y keeps the heights of $b$, $c$ and $d$, so copy them from the other tab: $640$, $595$ and $430\,\mathrm{V}$ (and $a=700\,\mathrm{V}$)."
#@ step "Read the answers as falls between real nodes: $i_1=\dfrac{700-640}{24}=2.5\,\mathrm{A}$, $v=640-595=45\,\mathrm{V}$, $i_2=\dfrac{595-430}{20}=8.25\,\mathrm{A}$." show=e24,e60,e20
#@ step "KCL check at $b$: $2.5\,\mathrm{A}$ in; out $0.75\,\mathrm{A}$ down the $60\,\Omega$ and $\dfrac{210}{120}=1.75\,\mathrm{A}$ through the $120\,\Omega$. At $c$: $7.5+0.75=8.25\,\mathrm{A}$ in and out." show=e120
#@ step "Power: the source lifts $10\,\mathrm{A}$ through $750\,\mathrm{V}$, supplying $7500\,\mathrm{W}$."
```

<details><summary>Solution</summary>

1. Nothing is in series or parallel. Of the two triangles, $b$–$c$–$d$ ($60$, $120$, $20\,\Omega$) has the friendly sum $200\,\Omega$; convert it. Arm at each corner = product of the two touching it ÷ 200.

   $$\begin{aligned}&R_b=\frac{(60)(120)}{200}=36\,\Omega,\quad R_c=\frac{(60)(20)}{200}=6\,\Omega\\&R_d=\frac{(120)(20)}{200}=12\,\Omega\end{aligned}$$
2. Two paths from $a$ to the new center $n$, side by side, then everything in series.

   $$\begin{aligned}&(24+36)\parallel(14+6)=60\parallel20=15\,\Omega\\&R_{\mathrm{in}}=5+15+12+43=75\,\Omega,\quad i=\frac{750}{75}=10\,\mathrm{A}\end{aligned}$$
3. Heights along the single stream.

   $$\begin{aligned}&v_a=750-(10)(5)=700\,\mathrm{V},\quad v_n=700-(10)(15)=550\,\mathrm{V}\\&v_d=(10)(43)=430\,\mathrm{V}\end{aligned}$$
4. Split the $10\,\mathrm{A}$ between the two paths (each falls $150\,\mathrm{V}$), then place $b$ and $c$. They are original nodes, so their heights carry over.

   $$\begin{aligned}&i_1=\frac{150}{60}=2.5\,\mathrm{A},\quad i_{14}=\frac{150}{20}=7.5\,\mathrm{A}\\&v_b=700-(2.5)(24)=640\,\mathrm{V},\quad v_c=700-(7.5)(14)=595\,\mathrm{V}\end{aligned}$$
5. Back in the original circuit, $v$ and $i_2$ are falls between real nodes.

   $$v=640-595=45\,\mathrm{V},\qquad i_2=\frac{595-430}{20}=8.25\,\mathrm{A}$$
6. Power supplied by the source.

   $$p=(750)(10)=7500\,\mathrm{W}$$

**Answer:** **(a)** $i_1=2.5\,\mathrm{A}$ **(b)** $v=45\,\mathrm{V}$ **(c)** $i_2=8.25\,\mathrm{A}$ **(d)** $7500\,\mathrm{W}$

</details>

## Practice problems

Exam-style, each mixing topics. Give each a real try (10–15 minutes) before opening the solution.

**Problem: Textbook P3.20 · Two paths back to the source** (intermediate)

Find **(a)** $i_o$ and $v_o$, **(b)** the power dissipated in the $12\,\Omega$ resistor and **(c)** the power developed by the current source.

```schematic
R1 0,3 -> 0,0 "$40\,\Omega$" v="$v_o$"
R2 0,3 -> 3,3 "$10\,\Omega$"
R3 0,0 -> 3,0 "$20\,\Omega$"
I1 3,0 -> 3,3 "$12\,\mathrm{A}$" flip
R4 3,3 -> 6,3 "$12\,\Omega$"
R5 6,3 -> 6,0 "$20\,\Omega$" i="$i_o$" flip
wire 6,3 -> 9,3
R6 9,3 -> 9,0 "$180\,\Omega$" flip
wire 9,0 -> 3,0
#@ spoiler
#@ node t 252 "source top: $252\,\mathrm{V}$"
#@ node p 216 "top of the $40\,\Omega$: $216\,\mathrm{V}$"
#@ node r 151.2 "after the $12\,\Omega$: $151.2\,\mathrm{V}$"
#@ node q 72 "bottom of the $40\,\Omega$: $72\,\mathrm{V}$"
#@ node g 0 "source bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "source bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "source bottom: $0\,\mathrm{V}$" ground
#@ node g4 0 "source bottom: $0\,\mathrm{V}$" ground
#@ el I g t "$12\,\mathrm{A}$" col=0 i="$12\,\mathrm{A}$" to=t id=es rail
#@ el R t p "$10\,\Omega$: falls $36\,\mathrm{V}$" col=1 i="$3.6\,\mathrm{A}$" to=p id=e10
#@ el R p q "$40\,\Omega$: falls $144\,\mathrm{V}$" col=1 i="$3.6\,\mathrm{A}$" to=q id=e40 plus=p v="$v_o$"
#@ el R q g2 "$20\,\Omega$: falls $72\,\mathrm{V}$" col=1 i="$3.6\,\mathrm{A}$" to=g2 id=e20a
#@ el R t r "$12\,\Omega$: falls $100.8\,\mathrm{V}$" col=2 i="$8.4\,\mathrm{A}$" to=r id=e12
#@ el R r g3 "$20\,\Omega$: falls $151.2\,\mathrm{V}$" col=2 i="$7.56\,\mathrm{A}$" to=g3 id=e20b
#@ el R r g4 "$180\,\Omega$: falls $151.2\,\mathrm{V}$" col=3 i="$0.84\,\mathrm{A}$" to=g4 id=e180
#@ step "Ground the bottom of the current source. Two paths fall from its top back to its bottom: left $10+40+20=70\,\Omega$, right $12+(20\parallel180)=12+18=30\,\Omega$."
#@ step "Both paths fall the same total height, so they split the $12\,\mathrm{A}$ by conductance: left $12\cdot\dfrac{30}{100}=3.6\,\mathrm{A}$, right $8.4\,\mathrm{A}$. The top is at $(3.6)(70)=252\,\mathrm{V}$." show=t,es,e10,e40,e20a,e12
#@ step "Left path: the $10\,\Omega$ falls $36\,\mathrm{V}$ (to $216$), the $40\,\Omega$ falls $144\,\mathrm{V}$ (to $72$), so $v_o=144\,\mathrm{V}$; the $20\,\Omega$ falls the last $72\,\mathrm{V}$." show=p,q
#@ step "Right path: the $12\,\Omega$ falls $(8.4)(12)=100.8\,\mathrm{V}$ to $151.2\,\mathrm{V}$. The $20\,\Omega$ takes $i_o=\dfrac{151.2}{20}=7.56\,\mathrm{A}$, the $180\,\Omega$ the other $0.84\,\mathrm{A}$." show=r,e20b,e180
#@ step "Power: the $12\,\Omega$ absorbs $(100.8)(8.4)=846.72\,\mathrm{W}$; the source lifts $12\,\mathrm{A}$ through $252\,\mathrm{V}$: $3024\,\mathrm{W}$ developed."
```

<details><summary>Solution</summary>

1. Convert: ground the source's bottom. Two paths fall from its top back down: $70\,\Omega$ on the left, $12+(20\parallel180)=30\,\Omega$ on the right. They share one total fall, so they split the current by conductance.

   $$\begin{aligned}&i_{\text{left}}=12\cdot\frac{30}{70+30}=3.6\,\mathrm{A},\\&i_{\text{right}}=8.4\,\mathrm{A},\quad V_{\text{top}}=(3.6)(70)=252\,\mathrm{V}\end{aligned}$$
2. **(a)** The $40\,\Omega$ falls $v_o$; the right junction sits below the top by the $12\,\Omega$'s fall.

   $$\begin{aligned}&v_o=(3.6)(40)=144\,\mathrm{V},\quad V_r=252-(8.4)(12)=151.2\,\mathrm{V},\\&i_o=\frac{151.2}{20}=7.56\,\mathrm{A}\end{aligned}$$
3. **(b)–(c)** Power = current × fall.

   $$\begin{aligned}&p_{12}=(8.4)(100.8)=846.72\,\mathrm{W},\\&p_{\text{source}}=(252)(12)=3024\,\mathrm{W}\end{aligned}$$

**Answer:** **(a)** $i_o=7.56\,\mathrm{A}$, $v_o=144\,\mathrm{V}$. **(b)** $846.72\,\mathrm{W}$. **(c)** $3024\,\mathrm{W}$.

</details>

**Problem: Textbook P3.14 · A loaded divider, then a buffer** (intermediate)

**(a)** The divider on the left is loaded by the divider on the right (connected at $a$). Find $v_o$.

```schematic
V1 0,3 -> 0,0 "$380\,\mathrm{V}$"
R1 0,3 -> 3,3 "$75\,\mathrm{k\Omega}$" i="$i$"
R2 3,3 -> 3,0 "$25\,\mathrm{k\Omega}$" flip
R3 3,3 -> 6,3 "$40\,\mathrm{k\Omega}$"
R4 6,3 -> 6,0 "$60\,\mathrm{k\Omega}$" v="$v_o$" flip
wire 6,0 -> 0,0
label 3,3 "$a$" above
#@ spoiler
#@ node t 380 "top: $380\,\mathrm{V}$"
#@ node a 80 "$a$: $80\,\mathrm{V}$"
#@ node o 48 "output: $48\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$380\,\mathrm{V}$" col=0 i="$4\,\mathrm{mA}$" to=t id=es
#@ el R t a "$75\,\mathrm{k\Omega}$: falls $300\,\mathrm{V}$" col=1 i="$4\,\mathrm{mA}$" to=a id=e75
#@ el R a g2 "$25\,\mathrm{k\Omega}$: falls $80\,\mathrm{V}$" col=1 i="$3.2\,\mathrm{mA}$" to=g2 id=e25
#@ el R a o "$40\,\mathrm{k\Omega}$: falls $32\,\mathrm{V}$" col=2 i="$0.8\,\mathrm{mA}$" to=o id=e40
#@ el R o g3 "$60\,\mathrm{k\Omega}$: falls $48\,\mathrm{V}$" col=2 i="$0.8\,\mathrm{mA}$" to=g3 id=e60 plus=o v="$v_o$"
#@ step "Ground the bottom; the top is at $380\,\mathrm{V}$. Below $a$ there are two ways down: the $25\,\mathrm{k\Omega}$ and the $40+60=100\,\mathrm{k\Omega}$ path, together $25\parallel100=20\,\mathrm{k\Omega}$."
#@ step "So $a$ sits $\dfrac{20}{75+20}$ of the way up: $80\,\mathrm{V}$. Unloaded it would have been $95\,\mathrm{V}$: the second divider makes it sag $15\,\mathrm{V}$." show=a,e75,es
#@ step "The right divider hangs from $a$: its midpoint sits $\dfrac{60}{100}$ of the way up from 0 to $80$: $v_o=48\,\mathrm{V}$." show=o,e25,e40,e60
```

**(b)** Now the right divider is driven by a current-controlled voltage source $25\,000\,i$ instead of being wired to $a$. Find $v_o$. **(c)** What does the dependent source do for the $380\,\mathrm{V}$ divider?

```schematic
V1 0,3 -> 0,0 "$380\,\mathrm{V}$"
R1 0,3 -> 3,3 "$75\,\mathrm{k\Omega}$" i="$i$"
R2 3,3 -> 3,0 "$25\,\mathrm{k\Omega}$" flip
E1 6,3 -> 6,0 "$25\,000\,i$"
R3 6,3 -> 9,3 "$40\,\mathrm{k\Omega}$"
R4 9,3 -> 9,0 "$60\,\mathrm{k\Omega}$" v="$v_o$" flip
wire 9,0 -> 0,0
label 3,3 "$a$" above
#@ spoiler
#@ node t 380 "top: $380\,\mathrm{V}$"
#@ node a 95 "$a$, and the copy: $95\,\mathrm{V}$"
#@ node e 95 "$a$, and the copy: $95\,\mathrm{V}$"
#@ node o 57 "output: $57\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g4 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$380\,\mathrm{V}$" col=0 i="$3.8\,\mathrm{mA}$" to=t id=es
#@ el R t a "$75\,\mathrm{k\Omega}$: falls $285\,\mathrm{V}$" col=1 i="$3.8\,\mathrm{mA}$" to=a id=e75
#@ el R a g2 "$25\,\mathrm{k\Omega}$: falls $95\,\mathrm{V}$" col=1 i="$3.8\,\mathrm{mA}$" to=g2 id=e25
#@ el E e g3 "$25\,000\,i=95\,\mathrm{V}$" col=2 i="$0.95\,\mathrm{mA}$" to=e id=eE
#@ el R e o "$40\,\mathrm{k\Omega}$: falls $38\,\mathrm{V}$" col=3 i="$0.95\,\mathrm{mA}$" to=o id=e40
#@ el R o g4 "$60\,\mathrm{k\Omega}$: falls $57\,\mathrm{V}$" col=3 i="$0.95\,\mathrm{mA}$" to=g4 id=e60 plus=o v="$v_o$"
#@ step "Ground the bottom wire, as in part (a). Now nothing is attached to $a$: the left divider is unloaded, one current $\dfrac{380}{100\,\mathrm{k\Omega}}=3.8\,\mathrm{mA}$, and $a$ sits at its no-load height $95\,\mathrm{V}$." show=a,e75,e25,es
#@ step "The dependent source copies that height: its step is $25\,000\,i=(25\,000)(0.0038)=95\,\mathrm{V}$, the same as the $25\,\mathrm{k\Omega}$'s fall. It supplies the right divider's current itself." show=e,eE
#@ step "The right divider falls from $95\,\mathrm{V}$: its midpoint sits $\dfrac{60}{100}$ of the way up, so $v_o=57\,\mathrm{V}$." show=o,e40,e60
#@ note "The source is a **buffer**: it reproduces the $95\,\mathrm{V}$ height on the right without drawing any current from the left divider, so the left divider no longer sags."
```

<details><summary>Solution</summary>

1. **(a)** Below $a$ the $25\,\mathrm{k\Omega}$ and the $40+60\,\mathrm{k\Omega}$ path are side by side: $20\,\mathrm{k\Omega}$. Divide the rail, then divide again.

   $$\begin{aligned}&V_a=380\cdot\frac{20}{75+20}=80\,\mathrm{V},\\&v_o=80\cdot\frac{60}{100}=48\,\mathrm{V}\end{aligned}$$
2. **(b)** Unloaded, the left divider sets $i$ and $a$; the dependent source copies $a$'s height.

   $$\begin{aligned}&i=\frac{380}{100\,\mathrm{k\Omega}}=3.8\,\mathrm{mA},\quad 25\,000\,i=95\,\mathrm{V},\\&v_o=95\cdot\frac{60}{100}=57\,\mathrm{V}\end{aligned}$$
3. **(c)** The dependent source draws no current from the $380\,\mathrm{V}$ divider, so that divider stays at its no-load output ($95\,\mathrm{V}$ at $a$). It isolates the load: a buffer.

**Answer:** **(a)** $v_o=48\,\mathrm{V}$. **(b)** $v_o=57\,\mathrm{V}$. **(c)** It isolates the second divider, so the $380\,\mathrm{V}$ divider is no longer loaded ($a$ stays at $95\,\mathrm{V}$).

</details>

**Problem: Textbook P3.41 · How wrong is the ammeter?** (intermediate)

The ammeter in the circuit has a resistance of $0.5\,\Omega$. What is the percentage error in its reading, $\left(\dfrac{\text{measured}}{\text{true}}-1\right)\times100$?

```schematic
V1 0,3 -> 0,0 "$180\,\mathrm{V}$"
R1 0,3 -> 3,3 "$10\,\Omega$"
R2 3,3 -> 3,0 "$60\,\Omega$" flip
R3 3,3 -> 6,3 "$30\,\Omega$"
AM1 6,3 -> 6,0 "ammeter"
wire 6,0 -> 0,0
#@ spoiler
#@ view "Ideal ammeter (true value)"
#@ node t 180 "top: $180\,\mathrm{V}$"
#@ node n 120 "junction: $120\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$180\,\mathrm{V}$" col=0 i="$6\,\mathrm{A}$" to=t
#@ el R t n "$10\,\Omega$: falls $60\,\mathrm{V}$" col=1 i="$6\,\mathrm{A}$" to=n
#@ el R n g2 "$60\,\Omega$: falls $120\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2
#@ el R n g3 "$30\,\Omega$ (ideal ammeter: no step)" col=2 i="$4\,\mathrm{A}$" to=g3
#@ note "True value: $10+(60\parallel30)=30\,\Omega$, so $6\,\mathrm{A}$; the junction sits at $120\,\mathrm{V}$ and the measured branch carries $\dfrac{120}{30}=4\,\mathrm{A}$."
#@ view "Real 0.5 Ω ammeter"
#@ node t 180 "top: $180\,\mathrm{V}$"
#@ node n 120.44 "junction: $120.44\,\mathrm{V}$"
#@ node m 1.97 "between $30\,\Omega$ and meter: $1.97\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V t g "$180\,\mathrm{V}$" col=0 i="$5.956\,\mathrm{A}$" to=t id=es
#@ el R t n "$10\,\Omega$: falls $59.56\,\mathrm{V}$" col=1 i="$5.956\,\mathrm{A}$" to=n id=e10
#@ el R n g2 "$60\,\Omega$" col=1 i="$2.007\,\mathrm{A}$" to=g2 id=e60
#@ el R n m "$30\,\Omega$: falls $118.46\,\mathrm{V}$" col=2 i="$3.949\,\mathrm{A}$" to=m id=e30
#@ el R m g3 "ammeter $0.5\,\Omega$: falls $1.97\,\mathrm{V}$" col=2 i="$3.949\,\mathrm{A}$" to=g3 id=eA
#@ step "Ground the bottom wire; the top is at $180\,\mathrm{V}$. The real ammeter is a $0.5\,\Omega$ slope in the branch it measures: $30.5\,\Omega$ beside $60\,\Omega$ is $20.22\,\Omega$, plus $10\,\Omega$ is $30.22\,\Omega$. The source now lifts $\dfrac{180}{30.22}=5.956\,\mathrm{A}$." show=es
#@ step "The $10\,\Omega$ falls $59.56\,\mathrm{V}$, leaving the junction at $120.44\,\mathrm{V}$ (it was $120$)." show=n,e10,e60
#@ step "The measured branch falls those $120.44\,\mathrm{V}$ through $30.5\,\Omega$: $3.949\,\mathrm{A}$, which is what the meter reads. The meter itself steals a $1.97\,\mathrm{V}$ step." show=m,e30,eA
#@ step "Error: $\left(\dfrac{3.949}{4}-1\right)\times100=-1.28\%$."
```

<details><summary>Solution</summary>

1. True value (ideal ammeter, no step): $10+(60\parallel30)=30\,\Omega$, so $6\,\mathrm{A}$ and the junction sits at $120\,\mathrm{V}$.

   $$i_{\text{true}}=\frac{120}{30}=4\,\mathrm{A}$$
2. With the meter, the branch is $30.5\,\Omega$: recompute the junction height.

   $$\begin{aligned}&R=10+\frac{60(30.5)}{90.5}=30.22\,\Omega,\quad i=5.956\,\mathrm{A},\\&V_n=180-59.56=120.44\,\mathrm{V},\\&i_{\text{meas}}=\frac{120.44}{30.5}=3.949\,\mathrm{A}\end{aligned}$$
3. Percentage error.

   $$\left(\frac{3.949}{4}-1\right)\times100=-1.28\%$$

**Answer:** About $-1.28\%$ (it reads $3.949\,\mathrm{A}$ instead of $4\,\mathrm{A}$).

</details>

**Problem: Textbook P3.18 · Design three output voltages** (intermediate)

Choose $R_1$, $R_2$ and $R_3$ so that the unloaded divider draws $30\,\mathrm{W}$ from the $30\,\mathrm{V}$ source and, measured from the common terminal, $v_1=15\,\mathrm{V}$, $v_2=5\,\mathrm{V}$ and $v_3=-15\,\mathrm{V}$.

```schematic
V1 0,6 -> 0,0 "$30\,\mathrm{V}$"
wire 0,6 -> 3,6
R1 3,6 -> 3,4 "$R_1$" flip
R2 3,4 -> 3,2 "$R_2$" flip
R3 3,2 -> 3,0 "$R_3$" flip
wire 0,0 -> 3,0
wire 3,6 -> 6,6
wire 3,4 -> 6,4
wire 3,2 -> 6,2
wire 3,0 -> 6,0
terminal 6,6 "$v_1$" right
terminal 6,4 "$v_2$" right
terminal 6,2 "Common" right
terminal 6,0 "$v_3$" right
#@ spoiler
#@ node t 15 "$v_1$: $15\,\mathrm{V}$"
#@ node m 5 "$v_2$: $5\,\mathrm{V}$"
#@ node c 0 "common: $0\,\mathrm{V}$" ground
#@ node b -15 "$v_3$: $-15\,\mathrm{V}$"
#@ el V t b "$30\,\mathrm{V}$" col=0 i="$1\,\mathrm{A}$" to=t id=es
#@ el R t m "$R_1=10\,\Omega$: falls $10\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=m id=e1
#@ el R m c "$R_2=5\,\Omega$: falls $5\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=c id=e2
#@ el R c b "$R_3=15\,\Omega$: falls $15\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=b id=e3
#@ step "Ground the **common** terminal: it is the reference, even though it sits in the middle of the chain. The outputs are heights: $v_1$ at $+15$, $v_2$ at $+5$, $v_3$ at $-15\,\mathrm{V}$. The source spans $15-(-15)=30\,\mathrm{V}$, as it must."
#@ step "The power sets the current: $30\,\mathrm{W}=(30\,\mathrm{V})\,i$, so $1\,\mathrm{A}$ flows down the whole chain." show=es
#@ step "Each resistor's value is its fall ÷ the current: $R_1=\dfrac{15-5}{1}=10\,\Omega$, $R_2=\dfrac{5-0}{1}=5\,\Omega$, $R_3=\dfrac{0-(-15)}{1}=15\,\Omega$." show=e1,e2,e3
```

<details><summary>Solution</summary>

1. Convert: the common terminal is ground, so the required voltages are heights: +15, +5, 0 and −15 V from top to bottom.
2. The power fixes the current through the unloaded chain.

   $$i=\frac{P}{V}=\frac{30\,\mathrm{W}}{30\,\mathrm{V}}=1\,\mathrm{A}$$
3. Each resistor is fall ÷ current.

   $$\begin{aligned}&R_1=\frac{15-5}{1}=10\,\Omega,\quad R_2=\frac{5-0}{1}=5\,\Omega,\\&R_3=\frac{0-(-15)}{1}=15\,\Omega\end{aligned}$$

**Answer:** $R_1=10\,\Omega$, $R_2=5\,\Omega$, $R_3=15\,\Omega$.

</details>

**Challenge set: unusual circuits.** Three harder textbook problems picked to stretch the height method: a source in the middle of the network, resistors that carry no current, and a staircase of dependent sources. Sketch the heights before you write any equation.

**Problem: Textbook P3.7(b) · A current source in the middle** (advanced)

The $50\,\mathrm{mA}$ source sits in the middle of the network, between $e$ and $b$.

```schematic
R1 0,6 -> 4,6 "$250\,\Omega$"
R2 4,6 -> 8,6 "$900\,\Omega$"
R3 0,6 -> 0,0 "$750\,\Omega$"
R4 8,6 -> 8,0 "$500\,\Omega$" flip
R5 0,0 -> 4,0 "$250\,\Omega$"
R6 4,0 -> 8,0 "$300\,\Omega$"
R7 4,6 -> 0,0 "$1\,\mathrm{k\Omega}$"
R8 4,0 -> 8,6 "$2.4\,\mathrm{k\Omega}$" flip
I1 4,0 -> 4,6 "$50\,\mathrm{mA}$"
label 0,6 "$a$" above
label 4,6 "$b$" above
label 8,6 "$c$" above
label 0,0 "$d$" below
label 4,0 "$e$" below
label 8,0 "$f$" below
#@ spoiler
#@ node b 25 "$b$: $25\,\mathrm{V}$"
#@ node a 20.833 "$a$: $20.83\,\mathrm{V}$"
#@ node c 10 "$c$: $10\,\mathrm{V}$"
#@ node d 8.333 "$d$: $8.33\,\mathrm{V}$"
#@ node f 3.75 "$f$: $3.75\,\mathrm{V}$"
#@ node g 0 "$e$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$e$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$e$: $0\,\mathrm{V}$" ground
#@ node g4 0 "$e$: $0\,\mathrm{V}$" ground
#@ el I g b "$50\,\mathrm{mA}$" col=0 i="$50\,\mathrm{mA}$" to=b id=es rail
#@ el R b a "$250\,\Omega$: falls $4.17\,\mathrm{V}$" col=1 i="$16.7\,\mathrm{mA}$" to=a id=eA
#@ el R a d "$750\,\Omega$: falls $12.5\,\mathrm{V}$" col=1 i="$16.7\,\mathrm{mA}$" to=d id=eB
#@ el R d g2 "$250\,\Omega$: falls $8.33\,\mathrm{V}$" col=1 i="$33.3\,\mathrm{mA}$" to=g2 id=eC
#@ el R b d "$1\,\mathrm{k\Omega}$: falls $16.7\,\mathrm{V}$" col=2 i="$16.7\,\mathrm{mA}$" to=d id=eD
#@ el R b c "$900\,\Omega$: falls $15\,\mathrm{V}$" col=3 i="$16.7\,\mathrm{mA}$" to=c id=eE
#@ el R c f "$500\,\Omega$: falls $6.25\,\mathrm{V}$" col=3 i="$12.5\,\mathrm{mA}$" to=f id=eF
#@ el R f g3 "$300\,\Omega$: falls $3.75\,\mathrm{V}$" col=3 i="$12.5\,\mathrm{mA}$" to=g3 id=eG
#@ el R c g4 "$2.4\,\mathrm{k\Omega}$: falls $10\,\mathrm{V}$" col=4 i="$4.17\,\mathrm{mA}$" to=g4 id=eH
#@ step "Ground $e$, the bottom of the source: everything else hangs above it. The source fixes the $50\,\mathrm{mA}$ it pushes into $b$, not $b$'s height."
#@ step "Left of the source, $b$ reaches $d$ two ways: the $1\,\mathrm{k\Omega}$ straight across, or $250+750=1\,\mathrm{k\Omega}$ round the corner. Side by side that is $500\,\Omega$, then the bottom $250\,\Omega$ to $e$: $750\,\Omega$. Right of it, $c$ reaches $e$ by the $2.4\,\mathrm{k\Omega}$ or by $500+300=800\,\Omega$: $600\,\Omega$, plus the $900\,\Omega$ on top: $1500\,\Omega$."
#@ step "Both sides fall from $b$ to $e$, so they are side by side: $750\parallel1500=500\,\Omega$. The source lifts its $50\,\mathrm{mA}$ to $b=(0.05)(500)=25\,\mathrm{V}$." show=b
#@ step "The left side carries $\dfrac{25}{750}=33.3\,\mathrm{mA}$. The bottom $250\,\Omega$ falls $8.33\,\mathrm{V}$, so $d=8.33\,\mathrm{V}$. Above $d$ the two equal $1\,\mathrm{k\Omega}$ paths take $16.7\,\mathrm{mA}$ each; on the corner path the $250\,\Omega$ falls $4.17\,\mathrm{V}$ to $a=20.83\,\mathrm{V}$." show=d,a,eA,eB,eC,eD
#@ step "The right side carries $\dfrac{25}{1500}=16.7\,\mathrm{mA}$; the $900\,\Omega$ falls $15\,\mathrm{V}$ to $c=10\,\mathrm{V}$. From $c$: $\dfrac{10}{2400}=4.17\,\mathrm{mA}$ straight down and $\dfrac{10}{800}=12.5\,\mathrm{mA}$ round the corner, where the $500\,\Omega$ falls $6.25\,\mathrm{V}$ to $f=3.75\,\mathrm{V}$." show=c,f,eE,eF,eG,eH
#@ step "Power: the source lifts $50\,\mathrm{mA}$ through $25\,\mathrm{V}$ and delivers $1.25\,\mathrm{W}$; the eight falls add up to the same $1.25\,\mathrm{W}$." show=es
#@ note "Every node sits between $0$ and $25\,\mathrm{V}$: with one source and only resistors, nothing can rise above the source's top or sink below its bottom."
```

**(a)** Find the equivalent resistance seen by the source.

**(b)** Find the power delivered by the source.

<details><summary>Solution</summary>

1. The source joins $b$ to $e$. On the left, $b$ reaches $d$ by the $1\,\mathrm{k\Omega}$ or by $250+750$, then the bottom $250\,\Omega$ leads to $e$. On the right, the $900\,\Omega$ leads to $c$, and $c$ reaches $e$ by the $2.4\,\mathrm{k\Omega}$ or by $500+300$.

   $$\begin{aligned}&\text{left: }1000\parallel(250+750)+250=750\,\Omega\\&\text{right: }900+2400\parallel(500+300)=1500\,\Omega\end{aligned}$$
2. **(a)** Both sides connect $b$ to $e$, so they are in parallel.

   $$R_{\mathrm{eq}}=750\parallel1500=500\,\Omega$$
3. **(b)** The height the source lifts its current to, then power = current × height.

   $$v_b=(0.05)(500)=25\,\mathrm{V},\qquad p=(25)(0.05)=1.25\,\mathrm{W}$$

**Answer:** **(a)** $R_{\mathrm{eq}}=500\,\Omega$ **(b)** $1.25\,\mathrm{W}$ delivered

</details>

**Problem: Textbook P3.30 · Two resistors that lie flat** (advanced)

Find $v_o$ using voltage and/or current division. Nothing is connected across the gap.

```schematic
I1 0,0 -> 0,6 "$50\,\mathrm{mA}$"
wire 0,6 -> 9,6
wire 0,0 -> 9,0
R1 2,6 -> 2,3 "$20\,\mathrm{k\Omega}$"
R2 2,3 -> 2,0 "$40\,\mathrm{k\Omega}$"
R3 9,6 -> 9,3 "$24\,\mathrm{k\Omega}$" flip
R4 9,3 -> 9,0 "$16\,\mathrm{k\Omega}$" flip
R5 2,3 -> 4,3 "$8\,\mathrm{k\Omega}$"
terminal 4,3
terminal 6,3
gap 6,3 -> 4,3 v="$v_o$"
R6 6,3 -> 9,3 "$3\,\mathrm{k\Omega}$"
ground 0,0
#@ spoiler
#@ node t 1200 "top: $1200\,\mathrm{V}$"
#@ node p 800 "left midpoint: $800\,\mathrm{V}$"
#@ node x 800 "left midpoint: $800\,\mathrm{V}$"
#@ node q 480 "right midpoint: $480\,\mathrm{V}$"
#@ node y 480 "right midpoint: $480\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el I g t "$50\,\mathrm{mA}$" col=0 i="$50\,\mathrm{mA}$" to=t id=es rail
#@ el R t p "$20\,\mathrm{k\Omega}$: falls $400\,\mathrm{V}$" col=1 i="$20\,\mathrm{mA}$" to=p id=e20
#@ el R p g2 "$40\,\mathrm{k\Omega}$: falls $800\,\mathrm{V}$" col=1 i="$20\,\mathrm{mA}$" to=g2 id=e40
#@ el R p x "$8\,\mathrm{k\Omega}$: flat" col=2 id=e8
#@ el S x y "gap: $320\,\mathrm{V}$" col=3 plus=y v="$v_o$" id=eo
#@ el R y q "$3\,\mathrm{k\Omega}$: flat" col=4 id=e3
#@ el R t q "$24\,\mathrm{k\Omega}$: falls $720\,\mathrm{V}$" col=5 i="$30\,\mathrm{mA}$" to=q id=e24
#@ el R q g3 "$16\,\mathrm{k\Omega}$: falls $480\,\mathrm{V}$" col=5 i="$30\,\mathrm{mA}$" to=g3 id=e16
#@ step "Ground the bottom wire. The source fixes the $50\,\mathrm{mA}$ it pushes into the top, not the top's height."
#@ step "Nothing can flow across the gap, so the $8\,\mathrm{k\Omega}$ and $3\,\mathrm{k\Omega}$ carry no current: they have **no fall**. Each end of the gap sits at the height of the midpoint it hangs from." show=e8,e3
#@ step "That leaves two dividers side by side under the top: $20+40=60\,\mathrm{k\Omega}$ and $24+16=40\,\mathrm{k\Omega}$. They fall the same height, so the $50\,\mathrm{mA}$ splits $20\,\mathrm{mA}$ / $30\,\mathrm{mA}$ (the $40\,\mathrm{k\Omega}$ side gets more), and the top sits at $(20\,\mathrm{mA})(60\,\mathrm{k\Omega})=1200\,\mathrm{V}$." show=t,es,e20,e40,e24,e16
#@ step "Place the midpoints: left $(20\,\mathrm{mA})(40\,\mathrm{k\Omega})=800\,\mathrm{V}$, right $(30\,\mathrm{mA})(16\,\mathrm{k\Omega})=480\,\mathrm{V}$. The gap ends copy them." show=p,x,q,y
#@ step "$v_o$ is $+$ on the right: $v_o=480-800=-320\,\mathrm{V}$. The gap takes all of the $320\,\mathrm{V}$ step between the two midpoints." show=eo
#@ step "Power check: the source lifts $50\,\mathrm{mA}$ through $1200\,\mathrm{V}$ ($60\,\mathrm{W}$); the falls absorb $8+16+21.6+14.4=60\,\mathrm{W}$. The flat resistors absorb nothing."
#@ note "A resistor with no current lies flat: it can't change a height. So an open gap reads the height difference of whatever it hangs from."
```

<details><summary>Solution</summary>

1. No current can cross the gap, so the $8\,\mathrm{k\Omega}$ and $3\,\mathrm{k\Omega}$ carry none and drop nothing: each gap end is at its midpoint\'s voltage. What is left is two dividers in parallel across the source.

   $$20+40=60\,\mathrm{k\Omega},\qquad 24+16=40\,\mathrm{k\Omega}$$
2. Current division of the $50\,\mathrm{mA}$ (the other resistance on top).

   $$i_{\text{left}}=50\cdot\frac{40}{60+40}=20\,\mathrm{mA},\qquad i_{\text{right}}=30\,\mathrm{mA}$$
3. Midpoint voltages (mA × kΩ = V).

   $$v_{\text{left}}=(20)(40)=800\,\mathrm{V},\qquad v_{\text{right}}=(30)(16)=480\,\mathrm{V}$$
4. $v_o$ is $+$ on the right.

   $$v_o=480-800=-320\,\mathrm{V}$$

**Answer:** $v_o=-320\,\mathrm{V}$

</details>

**Problem: Textbook P2.36 · A staircase of dependent sources** (advanced)

Call the top nodes $a$, $b$, $c$, $d$ from left to right ($a$ is the top of the $50\,\mathrm{V}$ source, $d$ the top of the $20\,\mathrm{V}$ source).

```schematic
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
E1 3,3 -> 0,3 "$20i_\sigma$"
R1 3,3 -> 3,0 "$18\,\Omega$" i="$i_\Delta$"
E2 3,3 -> 6,3 "$5i_\sigma$"
R2 6,3 -> 6,0 "$40\,\Omega$" i="$i_\sigma$" v="$v_o$"
G1 6,3 -> 9,3 "$8i_\Delta$"
V2 9,3 -> 9,0 "$20\,\mathrm{V}$"
wire 9,0 -> 0,0
ground 0,0
#@ spoiler
#@ node b 90 "$b$: $90\,\mathrm{V}$"
#@ node c 80 "$c$: $80\,\mathrm{V}$"
#@ node a 50 "$a$: $50\,\mathrm{V}$"
#@ node d 20 "$d$: $20\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g4 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V a g "$50\,\mathrm{V}$" col=0 i="$47\,\mathrm{A}$" to=a id=es
#@ el E b a "$20i_\sigma$: $40\,\mathrm{V}$" col=0 i="$47\,\mathrm{A}$" to=b id=eE1
#@ el R b g2 "$18\,\Omega$: falls $90\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=g2 id=e18
#@ el E b c "$5i_\sigma$: $10\,\mathrm{V}$" col=2 i="$42\,\mathrm{A}$" to=c id=eE2
#@ el R c g3 "$40\,\Omega$: falls $80\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=g3 id=e40 plus=c v="$v_o$"
#@ el G c d "$8i_\Delta$: $40\,\mathrm{A}$" col=3 i="$40\,\mathrm{A}$" to=d id=eG
#@ el V d g4 "$20\,\mathrm{V}$" col=3 i="$40\,\mathrm{A}$" to=g4 id=eV2
#@ step "Ground the bottom wire. The two independent sources are fixed steps: $a$ (top of the $50\,\mathrm{V}$) is at $50\,\mathrm{V}$ and $d$ (top of the $20\,\mathrm{V}$) at $20\,\mathrm{V}$."
#@ step "The two diamonds are steps too, but their size depends on $i_\sigma=\dfrac{c}{40}$, the current down the $40\,\Omega$. Climb from $a$: up $20i_\sigma$ to $b$, then down $5i_\sigma$ to $c$ (its $+$ is on the $b$ side). So $c=50+15i_\sigma$."
#@ step "Close the loop: $40i_\sigma=50+15i_\sigma$, so $i_\sigma=2\,\mathrm{A}$. The steps are $40\,\mathrm{V}$ and $10\,\mathrm{V}$: $b=90\,\mathrm{V}$ and $c=80\,\mathrm{V}=v_o$. Node $b$ sits **above** both independent sources: dependent sources can lift a node that high." show=b,c,e40
#@ step "$i_\Delta$ is $b$'s fall over $18\,\Omega$: $\dfrac{90}{18}=5\,\mathrm{A}$. So the right diamond drives $8i_\Delta=40\,\mathrm{A}$ from $c$ ($80\,\mathrm{V}$) down to $d$ ($20\,\mathrm{V}$)." show=e18,eG
#@ step "KCL fills in the rest: the $40\,\mathrm{A}$ carries on down through the $20\,\mathrm{V}$ source; $c$ needs $2+40=42\,\mathrm{A}$ through the $5i_\sigma$ step; $b$ needs $5+42=47\,\mathrm{A}$, which climbs through the $50\,\mathrm{V}$ source and the $20i_\sigma$ step." show=eV2,eE2,eE1,es
#@ step "Power = current × height change. Climbs deliver: $(47)(50)=2350$ and $(47)(40)=1880\,\mathrm{W}$. Falls absorb: $5i_\sigma$ $(42)(10)=420$, $8i_\Delta$ $(40)(60)=2400$, $20\,\mathrm{V}$ source $(40)(20)=800$, resistors $450+160$. Both total $4230\,\mathrm{W}$."
#@ note "Three of the five sources absorb: current falls through them. Only the arrow colour tells you who delivers."
```

**(a)** Calculate $i_\Delta$ and $v_o$.

**(b)** Show that the power developed equals the power absorbed.

<details><summary>Solution</summary>

1. Ground the bottom. The independent sources fix $v_a=50\,\mathrm{V}$ and $v_d=20\,\mathrm{V}$. The control $i_\sigma$ is the current down the $40\,\Omega$.

   $$i_\sigma=\frac{v_c}{40}$$
2. Walk from $a$ to $c$ through the two diamonds: up $20i_\sigma$ ($+$ on the $b$ side), then down $5i_\sigma$ ($+$ on the $b$ side too).

   $$v_c=50+20i_\sigma-5i_\sigma=50+15i_\sigma$$
3. Combine with the control.

   $$40i_\sigma=50+15i_\sigma\;\Rightarrow\;i_\sigma=2\,\mathrm{A},\quad v_o=v_c=80\,\mathrm{V}$$
4. Node $b$, then $i_\Delta$.

   $$v_b=50+20(2)=90\,\mathrm{V},\qquad i_\Delta=\frac{90}{18}=5\,\mathrm{A}$$
5. KCL for the source currents: $8i_\Delta=40\,\mathrm{A}$ goes from $c$ to $d$ and on down the $20\,\mathrm{V}$ source.

   $$\begin{aligned}&i_{5i_\sigma}=2+40=42\,\mathrm{A}\ (b\to c)\\&i_{50\,\mathrm{V}}=i_{20i_\sigma}=5+42=47\,\mathrm{A}\end{aligned}$$
6. **(b)** Power = current × step: climbing delivers, falling absorbs. Only the $50\,\mathrm{V}$ source and the $20i_\sigma$ source climb.

   $$\begin{aligned}\text{developed}&=(47)(50)+(47)(40)=4230\,\mathrm{W}\\ \text{absorbed}&=420+2400+800+450+160=4230\,\mathrm{W}\end{aligned}$$

**Answer:** **(a)** $i_\Delta=5\,\mathrm{A}$, $v_o=80\,\mathrm{V}$ **(b)** $4230\,\mathrm{W}$ developed (the $50\,\mathrm{V}$ source and the $20i_\sigma$ source) $=4230\,\mathrm{W}$ absorbed

</details>

## Summary: Week 2 in one read

> **Tip:** Same picture as Week 1: **voltage is height**, sources lift, resistors are slides. Week 2 adds one habit: **give every node a height, then make the currents balance.** Each part below is one idea, one picture (drawn under the circuit) and one example. The table at the end says which part each practice problem needs.

### A · KCL and KVL: one height per node, currents balance

- Ground a node. Every other node gets a height; an unknown one gets a name like $x$.
- Each resistor current $=\dfrac{\text{high}-\text{low}}{R}$, flowing downhill.
- KCL at the unknown node (in = out) gives one equation. Solve it, then read everything off the heights.

**Example: A1 · Find the middle height (like P2.21)**

Find the height of $x$, every current, and check the power.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$3\,\Omega$" flip
wire 3,3 -> 6,3
I1 6,3 -> 6,0 "$1\,\mathrm{A}$" flip
wire 6,0 -> 0,0
label 3,3 "$x$" above
#@ inline
#@ node top 12 "top: $12\,\mathrm{V}$"
#@ node x 6 "$x$: $6\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V top g "$12\,\mathrm{V}$" col=0 i="$3\,\mathrm{A}$" to=top id=es
#@ el R top x "$2\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$3\,\mathrm{A}$" to=x id=e2
#@ el R x g2 "$3\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=e3
#@ el I x g3 "$1\,\mathrm{A}$" col=2 i="$1\,\mathrm{A}$" to=g3 id=ei
#@ step "Ground the bottom wire. The source puts the top at $12\,\mathrm{V}$; call the middle height $x$." show=top
#@ step "KCL at $x$: $\dfrac{12-x}{2}$ comes in; $\dfrac{x}{3}$ and $1\,\mathrm{A}$ go out. Solving gives $x=6\,\mathrm{V}$." show=x,ei
#@ step "Currents = fall ÷ R: $\dfrac{6}{2}=3\,\mathrm{A}$ in, $\dfrac{6}{3}=2\,\mathrm{A}$ down the $3\,\Omega$, $1\,\mathrm{A}$ down the source." show=e2,e3,es
#@ step "Power: the source lifts $3\,\mathrm{A}$ up $12\,\mathrm{V}$ ($36\,\mathrm{W}$); the falls absorb $18+12+6=36\,\mathrm{W}$."
```

1. Ground the bottom; the top is at $12\,\mathrm{V}$. KCL at $x$ (in = out), then multiply by 6.

   $$\frac{12-x}{2}=\frac{x}{3}+1\;\Rightarrow\;36-3x=2x+6\;\Rightarrow\;x=6\,\mathrm{V}$$
2. Currents = fall ÷ R.

   $$i_{2\Omega}=\frac{6}{2}=3\,\mathrm{A},\qquad i_{3\Omega}=\frac{6}{3}=2\,\mathrm{A},\qquad 2+1=3\ \checkmark$$
3. Power check: current × height.

   $$(12)(3)=36\,\mathrm{W}=\underbrace{(6)(3)}_{2\,\Omega}+\underbrace{(6)(2)}_{3\,\Omega}+\underbrace{(6)(1)}_{\text{1 A source}}$$

**Answer:** $x=6\,\mathrm{V}$; $3\,\mathrm{A}$ in, splitting $2\,\mathrm{A}$ and $1\,\mathrm{A}$; $36\,\mathrm{W}$ delivered and absorbed.

### B · Dependent sources: control first

- Find the control (with its sign), compute the source's value, then treat it as a normal source.
- A dependent **voltage** source can copy a height into another circuit **without drawing current** from the first one. That's a buffer.

**Example: B1 · A buffer copies a height (like P3.14)**

The diamond is a voltage source of $4000\,i$ volts ($i$ in amperes, $+$ on top). Find $v_o$.

```schematic
V1 0,3 -> 0,0 "$20\,\mathrm{V}$"
R1 0,3 -> 3,3 "$6\,\mathrm{k\Omega}$" i="$i$"
R2 3,3 -> 3,0 "$4\,\mathrm{k\Omega}$" flip
E1 6,3 -> 6,0 "$4000\,i$"
R3 6,3 -> 9,3 "$1\,\mathrm{k\Omega}$"
R4 9,3 -> 9,0 "$3\,\mathrm{k\Omega}$" v="$v_o$" flip
wire 9,0 -> 0,0
label 3,3 "$a$" above
#@ inline
#@ straight off
#@ node top 20 "top: $20\,\mathrm{V}$"
#@ node a 8 "$a$: $8\,\mathrm{V}$"
#@ node e 8 "diamond top: $8\,\mathrm{V}$"
#@ node o 6 "$v_o$: $6\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ node g2 0 "$0\,\mathrm{V}$" ground
#@ node g3 0 "$0\,\mathrm{V}$" ground
#@ node g4 0 "$0\,\mathrm{V}$" ground
#@ el V top g "$20\,\mathrm{V}$" col=0 i="$2\,\mathrm{mA}$" to=top id=es
#@ el R top a "$6\,\mathrm{k\Omega}$" col=1 i="$2\,\mathrm{mA}$" to=a id=e6
#@ el R a g2 "$4\,\mathrm{k\Omega}$" col=1 i="$2\,\mathrm{mA}$" to=g2 id=e4
#@ el E e g3 "$4000i=8\,\mathrm{V}$" col=2 i="$2\,\mathrm{mA}$" to=e id=ee
#@ el R e o "$1\,\mathrm{k\Omega}$" col=3 i="$2\,\mathrm{mA}$" to=o id=e1
#@ el R o g4 "$3\,\mathrm{k\Omega}$" col=3 i="$2\,\mathrm{mA}$" to=g4 id=e3 plus=o v="$v_o$"
#@ step "Ground the bottom wire. The left circuit is a plain divider: nothing else draws current from it, so $i=\dfrac{20}{10\,\mathrm{k\Omega}}=2\,\mathrm{mA}$ and $a$ sits at $8\,\mathrm{V}$." show=top,es,e6,e4,a
#@ step "Control → value: $4000\,i=4000(0.002)=8\,\mathrm{V}$. The diamond copies $a$'s height into the right circuit." show=ee,e
#@ step "The right circuit is another divider from $8\,\mathrm{V}$: $v_o=8\cdot\dfrac{3}{4}=6\,\mathrm{V}$." show=e1,e3,o
```

1. Left side: nothing draws current from $a$, so it's a plain divider.

   $$i=\frac{20}{6+4}=2\,\mathrm{mA},\qquad V_a=(2)(4)=8\,\mathrm{V}$$
2. Control → value.

   $$4000\,i=4000(0.002)=8\,\mathrm{V}$$
3. Right side: a divider from $8\,\mathrm{V}$.

   $$v_o=8\cdot\frac{3}{1+3}=6\,\mathrm{V}$$

**Answer:** $v_o=6\,\mathrm{V}$. Wired straight to $a$ instead, the right divider would load $a$ and pull it below $8\,\mathrm{V}$.

### C · Series and parallel: reduce, then go back

- Series = one path (same current, resistances add). Parallel = same two nodes (same height difference).
- **Reduce** from the far end → source current → **height at each split** → branch current = fall ÷ $R$.

**Example: C1 · Reduce and restore (like P3.20 and AP 3.1)**

Find every current and the heights of $x$ and $y$.

```schematic
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$6\,\Omega$" flip
R3 3,3 -> 6,3 "$1\,\Omega$"
R4 6,3 -> 6,0 "$2\,\Omega$" flip
wire 6,0 -> 0,0
label 3,3 "$x$" above
label 6,3 "$y$" above
#@ inline
#@ node top 30 "top: $30\,\mathrm{V}$"
#@ node x 15 "$x$: $15\,\mathrm{V}$"
#@ node y 10 "$y$: $10\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ node g2 0 "$0\,\mathrm{V}$" ground
#@ node g3 0 "$0\,\mathrm{V}$" ground
#@ el V top g "$30\,\mathrm{V}$" col=0 i="$7.5\,\mathrm{A}$" to=top id=es
#@ el R top x "$2\,\Omega$: falls $15\,\mathrm{V}$" col=1 i="$7.5\,\mathrm{A}$" to=x id=e2
#@ el R x g2 "$6\,\Omega$: falls $15\,\mathrm{V}$" col=1 i="$2.5\,\mathrm{A}$" to=g2 id=e6
#@ el R x y "$1\,\Omega$: falls $5\,\mathrm{V}$" col=2 i="$5\,\mathrm{A}$" to=y id=e1
#@ el R y g3 "$2\,\Omega$: falls $10\,\mathrm{V}$" col=2 i="$5\,\mathrm{A}$" to=g3 id=e2b
#@ step "Ground the bottom wire; the top is at $30\,\mathrm{V}$. Reduce: $1+2=3\,\Omega$ (series), $6\parallel3=2\,\Omega$, plus $2\,\Omega$: $4\,\Omega$ total, so $7.5\,\mathrm{A}$ leaves the source." show=top,es,e2
#@ step "Go back: the first $2\,\Omega$ falls $(7.5)(2)=15\,\mathrm{V}$, so $x$ is at $15\,\mathrm{V}$." show=x
#@ step "Both branches fall $15\,\mathrm{V}$ from $x$: $\dfrac{15}{6}=2.5\,\mathrm{A}$ and $\dfrac{15}{3}=5\,\mathrm{A}$. The $1\,\Omega$ falls $5\,\mathrm{V}$, so $y$ is at $10\,\mathrm{V}$." show=e6,e1,e2b,y
```

1. Reduce from the far end.

   $$1+2=3\,\Omega,\qquad 6\parallel3=2\,\Omega,\qquad R_{\mathrm{in}}=2+2=4\,\Omega$$
2. Source current, then the height of the split.

   $$i=\frac{30}{4}=7.5\,\mathrm{A},\qquad V_x=30-(7.5)(2)=15\,\mathrm{V}$$
3. Branch currents = fall ÷ R; then walk down the right branch.

   $$\frac{15}{6}=2.5\,\mathrm{A},\quad\frac{15}{3}=5\,\mathrm{A},\quad V_y=15-(5)(1)=10\,\mathrm{V}$$

**Answer:** $7.5\,\mathrm{A}$ from the source, splitting $2.5\,\mathrm{A}$ (down the $6\,\Omega$) and $5\,\mathrm{A}$ (through $1\,\Omega$ and $2\,\Omega$). $V_x=15\,\mathrm{V}$, $V_y=10\,\mathrm{V}$.

### D · Dividers and loading

- Voltage divider: the midpoint sits $\dfrac{R_2}{R_1+R_2}$ of the way up. Current divider: same fall, so current $\propto\dfrac1R$.
- A load is a **second path down** from the midpoint, so the midpoint **sags**: use $R_2\parallel R_L$ in place of $R_2$.
- Designing a divider: place the required heights, get the current (from the power, $i=P/V$), then each $R=\text{fall}\div i$.

**Example: D1 · A load makes the midpoint sag (like P3.12 and P3.14)**

Find the output with no load, then with the $8\,\mathrm{k\Omega}$ load connected.

```schematic
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
R1 0,3 -> 3,3 "$8\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$8\,\mathrm{k\Omega}$" flip
wire 3,3 -> 6,3
R3 6,3 -> 6,0 "$R_L=8\,\mathrm{k\Omega}$" flip
wire 6,0 -> 0,0
label 3,3 "$o$" above
#@ inline
#@ view "With the load: $8\,\mathrm{V}$"
#@ node top 24 "top: $24\,\mathrm{V}$"
#@ node o 8 "$o$: $8\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ node g2 0 "$0\,\mathrm{V}$" ground
#@ node g3 0 "$0\,\mathrm{V}$" ground
#@ el V top g "$24\,\mathrm{V}$" col=0 i="$2\,\mathrm{mA}$" to=top id=es
#@ el R top o "$R_1$: falls $16\,\mathrm{V}$" col=1 i="$2\,\mathrm{mA}$" to=o id=e1
#@ el R o g2 "$R_2$: falls $8\,\mathrm{V}$" col=1 i="$1\,\mathrm{mA}$" to=g2 id=e2
#@ el R o g3 "$R_L$: falls $8\,\mathrm{V}$" col=2 i="$1\,\mathrm{mA}$" to=g3 id=eL
#@ step "Ground the bottom; the top is at $24\,\mathrm{V}$. Below $o$ there are now two paths down: $8\parallel8=4\,\mathrm{k\Omega}$." show=top
#@ step "Divide: $o$ sits $\dfrac{4}{8+4}$ of the way up: $8\,\mathrm{V}$. The top resistor falls $16\,\mathrm{V}$ with $2\,\mathrm{mA}$, which splits $1\,\mathrm{mA}$ + $1\,\mathrm{mA}$." show=o,es,e1,e2,eL
#@ view "No load: $12\,\mathrm{V}$"
#@ node top 24 "top: $24\,\mathrm{V}$"
#@ node o 12 "$o$: $12\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ node g2 0 "$0\,\mathrm{V}$" ground
#@ el V top g "$24\,\mathrm{V}$" col=0 i="$1.5\,\mathrm{mA}$" to=top id=es
#@ el R top o "$R_1$: falls $12\,\mathrm{V}$" col=1 i="$1.5\,\mathrm{mA}$" to=o id=e1
#@ el R o g2 "$R_2$: falls $12\,\mathrm{V}$" col=1 i="$1.5\,\mathrm{mA}$" to=g2 id=e2
#@ step "Same ground. Without the load, equal resistors split the $24\,\mathrm{V}$ in half: $o$ is at $12\,\mathrm{V}$." show=o,e1,e2,es
```

1. No load: equal resistors, so the midpoint is halfway up.

   $$v_o=24\cdot\frac{8}{8+8}=12\,\mathrm{V}$$
2. With the load: the bottom becomes $8\parallel8=4\,\mathrm{k\Omega}$.

   $$v_o=24\cdot\frac{4}{8+4}=8\,\mathrm{V}$$

**Answer:** $12\,\mathrm{V}$ unloaded; it sags to $8\,\mathrm{V}$ with the load, because the load is a second path down from the midpoint.

### E · Meters and the balanced bridge

- A real **ammeter** is a small resistor in series; a real **voltmeter** is a big resistor across. Put it in the circuit and solve again; that's what it reads.
- **Bridge balanced** = detector carries no current = both midpoints at the same height. Then $R_x=\dfrac{R_2R_3}{R_1}$.
- **Bridge not balanced:** an ideal detector pins both midpoints level, so the bridge becomes two side-by-side pairs in series; the detector current comes from KCL, not from a fall.

**Example: E1 · Balance a bridge (like AP 3.7)**

Find $R_x$ for balance, and both midpoint heights.

```schematic
V1 0,6 -> 0,0 "$10\,\mathrm{V}$"
wire 0,6 -> 6,6
R1 3,6 -> 3,3 "$R_1=2\,\mathrm{k\Omega}$"
R3 3,3 -> 3,0 "$R_3=3\,\mathrm{k\Omega}$"
R2 6,6 -> 6,3 "$R_2=4\,\mathrm{k\Omega}$" flip
R4 6,3 -> 6,0 "$R_x$" flip
AM1 3,3 -> 6,3 "detector"
wire 6,0 -> 0,0
#@ inline
#@ straight off
#@ node top 10 "top: $10\,\mathrm{V}$"
#@ node b 6 "left middle: $6\,\mathrm{V}$"
#@ node c 6 "right middle: $6\,\mathrm{V}$"
#@ node g 0 "$0\,\mathrm{V}$" ground
#@ node g2 0 "$0\,\mathrm{V}$" ground
#@ node g3 0 "$0\,\mathrm{V}$" ground
#@ el V top g "$10\,\mathrm{V}$" col=0 i="$3\,\mathrm{mA}$" to=top id=es
#@ el R top b "$R_1$" col=1 i="$2\,\mathrm{mA}$" to=b id=e1
#@ el R b g2 "$R_3$" col=1 i="$2\,\mathrm{mA}$" to=g2 id=e3
#@ el W b c "detector: flat, no current" col=1 id=ed
#@ el R top c "$R_2$" col=2 i="$1\,\mathrm{mA}$" to=c id=e2
#@ el R c g3 "$R_x=6\,\mathrm{k\Omega}$" col=2 i="$1\,\mathrm{mA}$" to=g3 id=ex
#@ step "Ground the bottom; the top is at $10\,\mathrm{V}$. The left side is a divider: its middle sits $\dfrac{3}{5}$ of the way up, at $6\,\mathrm{V}$." show=top,b,e1,e3
#@ step "Balance means the detector lies flat: the right middle must also be at $6\,\mathrm{V}$, so $R_x$ must take the same $\dfrac35$ share: $R_x=6\,\mathrm{k\Omega}$." show=c,ed,e2,ex,es
```

1. Balance formula (or: make both sides split the same way).

   $$R_x=\frac{R_2R_3}{R_1}=\frac{(4)(3)}{2}=6\,\mathrm{k\Omega}$$
2. Both midpoints sit $\tfrac35$ of the way up.

   $$V_b=10\cdot\frac{3}{2+3}=6\,\mathrm{V},\qquad V_c=10\cdot\frac{6}{4+6}=6\,\mathrm{V}\ \checkmark$$

**Answer:** $R_x=6\,\mathrm{k\Omega}$; both midpoints are at $6\,\mathrm{V}$, so the detector reads zero.

### F · Δ–Y in three lines

- Use it only when nothing is in series or parallel (a bridge).
- Arm at a corner = (product of the two Δ resistors touching that corner) ÷ (sum of all three). Equal $R$'s give $R/3$.
- Two triangles to choose from? Take the one whose sum makes the arms come out simple (P3.60: $60+120+20=200$).
- Then reduce normally. For an original resistor's current, go back to the original circuit.

### Which part do I need? (practice problem map)

| Practice problem | Use | First move |
|---|---|---|
| P3.20 · Two paths back to the source | C | The source's current splits into two paths with the same total fall: current divider, then walk down each path. |
| P3.14 · A loaded divider, then a buffer | D, B | (a) $25\,\mathrm{k\Omega}\parallel(40+60)\,\mathrm{k\Omega}$ below $a$, divide twice. (b) control → value, then a divider. |
| P3.41 · How wrong is the ammeter? | E, C | Solve once with a $0\,\Omega$ ammeter, once with $0.5\,\Omega$; compare. |
| P3.18 · Design three output voltages | D | Common terminal = ground; place the heights; $i=P/V$; each $R=$ fall ÷ $i$. |
| P3.7(b) · A current source in the middle | C | Ground the source's bottom $e$. Each side falls from $b$ to $e$, so the two sides are in parallel. |
| P3.30 · Two resistors that lie flat | D | No current crosses the gap, so the $8$ and $3\,\mathrm{k\Omega}$ lie flat; current-divide, then subtract the midpoint heights. |
| P2.36 · A staircase of dependent sources | A, B | Walk from $a$ up and down the diamond steps to get $v_c$; close it with $i_\sigma=\dfrac{v_c}{40}$. |

> **Warning:** **Traps.** (1) Two resistors sharing a node aren't in series if a third thing touches it. (2) Divide the current that enters *that* branch. (3) Unloaded divider formula with a load attached is wrong: combine $R_2\parallel R_L$ first. (4) A real meter changes the circuit: include its resistance. (5) Dependent source: control first, with its sign.

### Formula sheet

| Result | Formula | In heights |
|---|---|---|
| KCL | $\sum i_{\text{in}}=\sum i_{\text{out}}$ | currents balance at every level |
| KVL | $\sum_{\text{loop}}\Delta v=0$ | one height per node; climbs = falls |
| Series | $R=R_1+R_2+\dots$ | one column; falls add |
| Parallel | $R_1\parallel R_2=\dfrac{R_1R_2}{R_1+R_2}$ | side by side; same fall |
| Voltage divider | $v_2=v\,\dfrac{R_2}{R_1+R_2}$ | midpoint's share of the slope |
| Current divider | $i_1=i\,\dfrac{R_2}{R_1+R_2}$ | same fall; current $\propto1/R$ |
| Loaded divider | replace $R_2$ by $R_2\parallel R_L$ | the midpoint sags |
| Ammeter shunt | $R_A=\dfrac{V_m}{I_{FS}-I_m}$, $R_m=\dfrac{V_m}{I_m}$ | a small slope in series |
| Voltmeter series R | $R_v=\dfrac{V_{FS}}{I_m}-R_m$ | a big second path down |
| Balanced bridge | $R_x=\dfrac{R_2R_3}{R_1}$ | both midpoints level |
| Δ → Y | arm $=\dfrac{\text{product of the two touching}}{R_a+R_b+R_c}$ | corner heights unchanged |
| Y → Δ | $R=\dfrac{R_1R_2+R_2R_3+R_3R_1}{\text{opposite arm}}$ | corner heights unchanged |
