# Week 4: Method Choice, Source Transformations and Thévenin–Norton Equivalents

> **Info:** **Week 4 in one line:** shortcuts. **Pick** the method with fewer equations, **swap** sources to simplify, and **shrink** a whole circuit to two numbers ($V_{\mathrm{Th}}$, $R_{\mathrm{Th}}$) that a load can see.

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
> **New this week:** a source swap or a Thévenin equivalent keeps the heights **at the terminals** and redraws the inside. Never read inside powers from the redrawn circuit.

**Example: Example 0 · One unknown height**

Find the height of $x$ and the power of each source.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$" flip
wire 3,3 -> 6,3
I1 6,0 -> 6,3 "$1\,\mathrm{A}$" flip
wire 6,0 -> 0,0
label 3,3 "$x$" above
ground 0,0
#@ inline
#@ straight off
#@ node t 12 "top: $12\,\mathrm{V}$"
#@ node x 8 "$x$: $8\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V t g "$12\,\mathrm{V}$" col=0 i="$1\,\mathrm{A}$" to=t id=eV1
#@ el R t x "$4\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=x id=eR1
#@ el R x g2 "$4\,\Omega$: falls $8\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=eR2
#@ el I g3 x "$1\,\mathrm{A}$" col=2 i="$1\,\mathrm{A}$" to=x id=eI1
#@ step "Ground the bottom wire. The source puts the top at $12\,\mathrm{V}$."
#@ step "The pump pushes $1\,\mathrm{A}$ into $x$. KCL at $x$: $\dfrac{12-x}{4}+1=\dfrac{x}{4}$, so $x=8\,\mathrm{V}$." show=x
#@ step "Currents = fall ÷ R: $1\,\mathrm{A}$ through the top $4\,\Omega$, $2\,\mathrm{A}$ down the other." show=eR1,eR2,eV1
#@ step "Power: the source lifts $1\,\mathrm{A}$ by $12\,\mathrm{V}$ ($12\,\mathrm{W}$), the pump $1\,\mathrm{A}$ by $8\,\mathrm{V}$ ($8\,\mathrm{W}$). Falls: $4+16=20\,\mathrm{W}$."
```

1. KCL at $x$.

   $$\frac{12-x}{4}+1=\frac{x}{4}\;\Rightarrow\;x=8\,\mathrm{V}$$
2. Power: climbs = falls.

   $$(12)(1)+(8)(1)=20\,\mathrm{W}=(4)(1)+(8)(2)$$

**Answer:** $x=8\,\mathrm{V}$; the source delivers $12\,\mathrm{W}$, the pump $8\,\mathrm{W}$.

## Topic 1: Shortcuts: pick the method, swap sources

> **Tip:** **How it looks in heights.**
> 
> - **Pick the method:** node voltages need one equation per unknown height (batteries from ground give heights for free); meshes need one per window (edge pumps give loop currents for free). Take the smaller count.
> - **Swap:** a battery $V$ in series with $R$ is the same, seen from outside, as a pump $\dfrac{V}{R}$ in parallel with the same $R$ (arrow toward the $+$ end).
> - Same terminal height for **every** load; the inside is different, so go back to the original for powers.
> - A resistor across a battery, or in series with a pump, changes no other height: drop it while you solve (it still uses power).

**Example: Example 1 · Which method? Power in the 300 Ω (Lecture 4)**

Decide which method needs fewer equations, then find the power in the $300\,\Omega$ resistor.

```schematic
V1 0,4 -> 0,0 "$256\,\mathrm{V}$"
R1 0,4 -> 3,4 "$150\,\Omega$"
R2 3,4 -> 3,0 "$200\,\Omega$"
R3 3,4 -> 6,4 "$100\,\Omega$"
E1 6,4 -> 6,0 "$50i_\Delta$"
R4 6,4 -> 9,4 "$250\,\Omega$"
R5 9,4 -> 9,0 "$400\,\Omega$"
R6 9,4 -> 12,4 "$500\,\Omega$"
V2 12,0 -> 12,4 "$128\,\mathrm{V}$"
wire 3,4 -> 3,6
wire 9,4 -> 9,6
R7 9,6 -> 3,6 "$300\,\Omega$" i="$i_\Delta$"
wire 0,0 -> 12,0
label 3,4 "$a$" below
label 6,4 "$b$" above
label 9,4 "$c$" below
label 12,4 "$d$" right
ground 0,0
#@ inline
#@ straight off
#@ node s 384 "256 V top: $384\,\mathrm{V}$"
#@ node a 190.5 "$a$: $190.5\,\mathrm{V}$"
#@ node z0 128 "bottom wire: $128\,\mathrm{V}$"
#@ node c 120 "$c$: $120\,\mathrm{V}$"
#@ node b 116.25 "$b$: $116.25\,\mathrm{V}$"
#@ node g 0 "$d$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$d$: $0\,\mathrm{V}$" ground
#@ el V s z0 "$256\,\mathrm{V}$" col=0 i="$1.29\,\mathrm{A}$" to=s id=eV1
#@ el V z0 g "$128\,\mathrm{V}$" col=0 i="$0.24\,\mathrm{A}$" to=z0 id=eV2
#@ el R s a "$150\,\Omega$: falls $193.5\,\mathrm{V}$" col=1 i="$1.29\,\mathrm{A}$" to=a id=eR1
#@ el R c a "$300\,\Omega$: falls $70.5\,\mathrm{V}$" col=1 i="$0.235\,\mathrm{A}$" to=c id=eR7
#@ el R c g2 "$500\,\Omega$: falls $120\,\mathrm{V}$" col=1 i="$0.24\,\mathrm{A}$" to=g2 id=eR6
#@ el R a z0 "$200\,\Omega$: falls $62.5\,\mathrm{V}$" col=2 i="$0.3125\,\mathrm{A}$" to=z0 id=eR2
#@ el R c z0 "$400\,\Omega$: falls $8\,\mathrm{V}$" col=2 i="$0.02\,\mathrm{A}$" to=c id=eR5
#@ el R b c "$250\,\Omega$: falls $3.75\,\mathrm{V}$" col=2 i="$0.015\,\mathrm{A}$" to=b id=eR4
#@ el E b z0 "$50i_\Delta$: $-11.75\,\mathrm{V}$" col=3 i="$0.7575\,\mathrm{A}$" to=z0 id=eE1
#@ el R a b "$100\,\Omega$: falls $74.25\,\mathrm{V}$" col=4 i="$0.7425\,\mathrm{A}$" to=b id=eR3
#@ step "Ground node $d$, the lowest point: the $128\,\mathrm{V}$ source has its $+$ on the bottom wire, so $d$ hangs below it. The text's voltages are measured from the bottom wire; here every height is $128\,\mathrm{V}$ more."
#@ step "Fixed heights: the bottom wire is one $128\,\mathrm{V}$ step above $d$; the $256\,\mathrm{V}$ source's top is $384\,\mathrm{V}$." show=z0,s
#@ step "Unknowns: $a$ and $c$ ($b$ hangs from the bottom wire by the dependent step). KCL at both with $v_b=50i_\Delta=\dfrac{v_c-v_a}{6}$: $v_a=62.5$, $v_c=-8\,\mathrm{V}$ (heights $190.5$ and $120$)." show=a,c
#@ step "Control: $i_\Delta=\dfrac{v_c-v_a}{300}=-0.235\,\mathrm{A}$, so the real current runs $a\to c$. The dependent step $50i_\Delta=-11.75\,\mathrm{V}$ puts $b$ **below** the bottom wire." show=b,eE1,eR7
#@ step "Every other current = fall ÷ R." show=eR1,eR2,eR3,eR4,eR5,eR6,eV1,eV2
#@ step "Answer: the $300\,\Omega$ falls $70.5\,\mathrm{V}$ carrying $0.235\,\mathrm{A}$: $p=16.57\,\mathrm{W}$."
```

1. Mesh: $4$ essential nodes, $8$ essential branches, no current source.

   $$N_{\text{mesh}}=8-4+1=5$$
2. Node: ground the bottom wire. Both sources fix heights ($256$, $-128$); $b$ is set by the dependent source. Only $a$ and $c$ are unknown.

   $$N_{\text{node}}=2$$
3. KCL at $a$ and $c$ (×600 and ×6000), with $6v_b=v_c-v_a$.

   $$\begin{aligned}16v_a-3v_c&=1024\\-16v_a+67v_c&=-1536\end{aligned}$$
4. Add, then back-substitute.

   $$v_c=-8\,\mathrm{V},\qquad v_a=62.5\,\mathrm{V}$$
5. Control and power.

   $$i_\Delta=\frac{-8-62.5}{300}=-0.235\,\mathrm{A},\qquad p=i_\Delta^2(300)=16.57\,\mathrm{W}$$

**Answer:** Node-voltage (2 equations vs 5). $p_{300\,\Omega}\approx16.57\,\mathrm{W}$.

$$i_s=\frac{v_s}{R},\qquad v_s=R\,i_s$$

```schematic
V1 0,3 -> 0,0 "$v_s$"
R1 0,3 -> 3,3 "$R$"
wire 0,0 -> 3,0
terminal 3,3 "$a$" right
terminal 3,0 "$b$" right
I1 6,0 -> 6,3 "$i_s=\tfrac{v_s}{R}$"
wire 6,3 -> 8,3
R2 8,3 -> 8,0 "$R$"
wire 6,0 -> 8,0
wire 8,3 -> 10,3
wire 8,0 -> 10,0
terminal 10,3 "$a$" right
terminal 10,0 "$b$" right
```

**Example: Example 2 · Same load, two forms**

Attach a $2\,\Omega$ load to $12\,\mathrm{V}$ + $4\,\Omega$, then to its swap, $3\,\mathrm{A}$ ∥ $4\,\Omega$. Compare the height of $a$ and the source powers.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
wire 3,3 -> 5,3
R2 5,3 -> 5,0 "$2\,\Omega$" flip
wire 5,0 -> 0,0
terminal 3,3 "$a$" above
ground 0,0
#@ inline
#@ view "Voltage form"
#@ straight off
#@ node s 12 "source top: $12\,\mathrm{V}$"
#@ node a 4 "$a$: $4\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$12\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$4\,\Omega$: falls $8\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$2\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=eR2
#@ step "Ground $b$. The source steps up $12\,\mathrm{V}$."
#@ step "One loop: $\dfrac{12}{4+2}=2\,\mathrm{A}$. The $4\,\Omega$ falls $8\,\mathrm{V}$, so $a$ sits at $4\,\mathrm{V}$." show=a,eR1,eR2,eV1
#@ step "The source lifts $2\,\mathrm{A}$ by $12\,\mathrm{V}$: $24\,\mathrm{W}$."
#@ view "Current form: 3 A ∥ 4 Ω"
#@ straight off
#@ node a 4 "$a$: $4\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el I g a "$3\,\mathrm{A}$" col=0 i="$3\,\mathrm{A}$" to=a id=eIs
#@ el R a g2 "$4\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=g2 id=eRp
#@ el R a g3 "$2\,\Omega$: falls $4\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=g3 id=eR2
#@ step "Same ground. $i_s=\dfrac{12}{4}=3\,\mathrm{A}$ is pumped into $a$."
#@ step "Two paths down, side by side: $4\parallel2=\tfrac43\,\Omega$. So $a=(3)(\tfrac43)=4\,\mathrm{V}$: **the same height**." show=a,eRp,eR2
#@ step "But this pump lifts $3\,\mathrm{A}$ by $4\,\mathrm{V}$: only $12\,\mathrm{W}$. Inside powers differ."
#@ note "Terminal heights match; inside powers do not. Go back to the original circuit for any source's power."
```

1. Voltage form.

   $$i=\frac{12}{6}=2\,\mathrm{A},\quad v_a=(2)(2)=4\,\mathrm{V},\quad p_s=24\,\mathrm{W}$$
2. Current form.

   $$v_a=3\,(4\parallel2)=4\,\mathrm{V},\quad p_s=(3)(4)=12\,\mathrm{W}$$

**Answer:** $a$ sits at $4\,\mathrm{V}$ in both; the sources deliver $24\,\mathrm{W}$ and $12\,\mathrm{W}$.

**Example: Example 3 · Two swaps make one loop**

Find the heights of $p$ and $q$ and the power of each source.

```schematic
I1 0,0 -> 0,3 "$2\,\mathrm{A}$"
wire 0,3 -> 2,3
R1 2,3 -> 2,0 "$6\,\Omega$"
R2 2,3 -> 5,3 "$4\,\Omega$"
R3 5,3 -> 8,3 "$2\,\Omega$"
V1 8,3 -> 8,0 "$24\,\mathrm{V}$"
wire 0,0 -> 8,0
label 2,3 "$p$" above
label 5,3 "$q$" above
ground 0,0
#@ inline
#@ straight off
#@ node t 24 "battery top: $24\,\mathrm{V}$"
#@ node q 22 "$q$: $22\,\mathrm{V}$"
#@ node p 18 "$p$: $18\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el I g p "$2\,\mathrm{A}$" col=0 i="$2\,\mathrm{A}$" to=p id=eI1
#@ el R p g2 "$6\,\Omega$: falls $18\,\mathrm{V}$" col=1 i="$3\,\mathrm{A}$" to=g2 id=eR1
#@ el R p q "$4\,\Omega$: falls $4\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=p id=eR2
#@ el R q t "$2\,\Omega$: falls $2\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=q id=eR3
#@ el V t g3 "$24\,\mathrm{V}$" col=3 i="$1\,\mathrm{A}$" to=t id=eV1
#@ step "Ground the bottom wire. The $24\,\mathrm{V}$ battery lifts its top to $24\,\mathrm{V}$."
#@ step "Swap the $2\,\mathrm{A}$ pump and its $6\,\Omega$ for a $12\,\mathrm{V}$ battery behind $6\,\Omega$ ($2\times6=12$, $+$ on top). Now it is one loop: $24\,\mathrm{V}$ pushing one way, $12\,\mathrm{V}$ the other, through $6+4+2=12\,\Omega$."
#@ step "Loop current $=\dfrac{24-12}{12}=1\,\mathrm{A}$, flowing right to left through the $2\,\Omega$ and $4\,\Omega$." show=eR2,eR3,eV1
#@ step "Walk down from $24\,\mathrm{V}$: $q=24-2=22\,\mathrm{V}$, $p=22-4=18\,\mathrm{V}$." show=q,p
#@ step "Back in the real circuit: $\dfrac{18}{6}=3\,\mathrm{A}$ goes down the $6\,\Omega$ = $1\,\mathrm{A}$ from the right + $2\,\mathrm{A}$ from the pump ✓. The pump lifts $2\,\mathrm{A}$ by $18\,\mathrm{V}$ ($36\,\mathrm{W}$), the battery gives $24\,\mathrm{W}$." show=eR1,eI1
```

1. Swap the pump.

   $$2\,\mathrm{A}\parallel6\,\Omega\;\to\;12\,\mathrm{V}+6\,\Omega$$
2. One loop.

   $$\begin{aligned}&i=\frac{24-12}{6+4+2}=1\,\mathrm{A}\\&q=24-2(1)=22\,\mathrm{V},\quad p=22-4(1)=18\,\mathrm{V}\end{aligned}$$
3. Powers (original circuit).

   $$p_{2\mathrm{A}}=2(18)=36\,\mathrm{W},\qquad p_{24\mathrm{V}}=24(1)=24\,\mathrm{W}$$

**Answer:** $p=18\,\mathrm{V}$, $q=22\,\mathrm{V}$; the pump gives $36\,\mathrm{W}$, the battery $24\,\mathrm{W}$.

**Example: Example 4 · Swap, solve, go back (Lecture 4)**

Use source transformations to find $v_o$. Then find the power developed by the $250\,\mathrm{V}$ source and by the $8\,\mathrm{A}$ source.

```schematic
V1 0,4 -> 0,0 "$250\,\mathrm{V}$"
R2 3,4 -> 3,0 "$125\,\Omega$"
R1 3,4 -> 7,4 "$25\,\Omega$"
R4 7,4 -> 7,0 "$100\,\Omega$" v="$v_o$"
wire 0,4 -> 3,4
wire 7,4 -> 10,4
I1 10,4 -> 10,2 "$8\,\mathrm{A}$"
R3 10,2 -> 10,0 "$10\,\Omega$"
R5 10,4 -> 13,4 "$5\,\Omega$"
R6 13,4 -> 13,0 "$15\,\Omega$"
wire 0,0 -> 13,0
label 7,4 "$b$" above
label 10,2 "$d$" right
label 13,4 "$e$" above
ground 0,0
#@ inline
#@ view "1 · After the swaps"
#@ straight off
#@ node b 20 "$b$: $20\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ node g5 0 "ground: $0\,\mathrm{V}$" ground
#@ el I g b "$\tfrac{250}{25}=10\,\mathrm{A}$" col=0 i="$10\,\mathrm{A}$" to=b id=eIs
#@ el R b g2 "$25\,\Omega$: falls $20\,\mathrm{V}$" col=1 i="$0.8\,\mathrm{A}$" to=g2 id=eR1
#@ el R b g3 "$100\,\Omega$: falls $20\,\mathrm{V}$" col=2 i="$0.2\,\mathrm{A}$" to=g3 id=eR4
#@ el R b g4 "$5+15\,\Omega$: falls $20\,\mathrm{V}$" col=3 i="$1\,\mathrm{A}$" to=g4 id=eR56
#@ el I b g5 "$8\,\mathrm{A}$" col=4 i="$8\,\mathrm{A}$" to=g5 id=eI1
#@ step "Ground the bottom wire. Drop the $125\,\Omega$ (across the $250\,\mathrm{V}$ source) and the $10\,\Omega$ (in series with the $8\,\mathrm{A}$ pump): neither moves $b$."
#@ step "Swap $250\,\mathrm{V}$ + $25\,\Omega$ for a $10\,\mathrm{A}$ pump with $25\,\Omega$ beside it. Net into $b$: $10-8=2\,\mathrm{A}$." show=eIs,eI1
#@ step "Three paths down from $b$: $25\parallel100\parallel20=10\,\Omega$. So $b=(2)(10)=20\,\mathrm{V}=v_o$." show=b,eR1,eR4,eR56
#@ view "2 · Back to the original"
#@ straight off
#@ node s 250 "source top: $250\,\mathrm{V}$"
#@ node d 80 "$d$: $80\,\mathrm{V}$"
#@ node b 20 "$b$: $20\,\mathrm{V}$"
#@ node e 15 "$e$: $15\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ node g5 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$250\,\mathrm{V}$" col=0 i="$11.2\,\mathrm{A}$" to=s id=eV1
#@ el R s g2 "$125\,\Omega$: falls $250\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=eR2
#@ el R s b "$25\,\Omega$: falls $230\,\mathrm{V}$" col=2 i="$9.2\,\mathrm{A}$" to=b id=eR1
#@ el R b g3 "$100\,\Omega$: falls $20\,\mathrm{V}$" col=2 i="$0.2\,\mathrm{A}$" to=g3 id=eR4 plus=b v="$v_o$"
#@ el R b e "$5\,\Omega$: falls $5\,\mathrm{V}$" col=3 i="$1\,\mathrm{A}$" to=e id=eR5
#@ el R e g4 "$15\,\Omega$: falls $15\,\mathrm{V}$" col=3 i="$1\,\mathrm{A}$" to=g4 id=eR6
#@ el I b d "$8\,\mathrm{A}$" col=4 i="$8\,\mathrm{A}$" to=d id=eI1
#@ el R d g5 "$10\,\Omega$: falls $80\,\mathrm{V}$" col=5 i="$8\,\mathrm{A}$" to=g5 id=eR3
#@ step "Same ground. Copy $b=20\,\mathrm{V}$ from tab 1; the source fixes the top at $250\,\mathrm{V}$."
#@ step "Currents = fall ÷ R: $\dfrac{230}{25}=9.2\,\mathrm{A}$, $\dfrac{250}{125}=2\,\mathrm{A}$, $0.2\,\mathrm{A}$ down the $100\,\Omega$, $1\,\mathrm{A}$ through $5+15\,\Omega$." show=e,eR1,eR2,eR4,eR5,eR6
#@ step "The pump's $8\,\mathrm{A}$ falls through the $10\,\Omega$, so $d=80\,\mathrm{V}$. The pump lifts $8\,\mathrm{A}$ from $20$ to $80\,\mathrm{V}$: it **delivers** $480\,\mathrm{W}$." show=d,eR3,eI1
#@ step "The source lifts $9.2+2=11.2\,\mathrm{A}$ by $250\,\mathrm{V}$: $2800\,\mathrm{W}$. Check: the falls absorb $2116+500+4+5+15+640=3280\,\mathrm{W}$." show=eV1
```

1. Drop the $125\,\Omega$ and the $10\,\Omega$; swap the $250\,\mathrm{V}$ + $25\,\Omega$.

   $$i_s=\frac{250}{25}=10\,\mathrm{A}$$
2. One node: net $2\,\mathrm{A}$ into $25\parallel100\parallel20=10\,\Omega$.

   $$v_o=(10-8)(10)=20\,\mathrm{V}$$
3. Back to the original for the $250\,\mathrm{V}$ source.

   $$p=250\Big(\frac{250-20}{25}+\frac{250}{125}\Big)=250(11.2)=2800\,\mathrm{W}$$
4. The $8\,\mathrm{A}$ source: $d=(8)(10)=80\,\mathrm{V}$.

   $$p=(80-20)(8)=480\,\mathrm{W}\text{ developed}$$

**Answer:** $v_o=20\,\mathrm{V}$; the $250\,\mathrm{V}$ source develops $2800\,\mathrm{W}$, the $8\,\mathrm{A}$ source $480\,\mathrm{W}$.

**Problem: Try it 1 · Node or mesh for a bridge? (Textbook P4.54)** (intermediate)

**(a)** Which method would you use to find the power in the $10\,\Omega$ resistor, and why? **(b)** Find that power. **(c)** Find the power delivered by the $4\,\mathrm{A}$ source.

```schematic
I1 0,0 -> 0,6 "$4\,\mathrm{A}$"
wire 0,6 -> 9,6
R1 3,6 -> 3,3 "$8\,\Omega$"
R3 3,3 -> 3,0 "$1\,\Omega$"
R2 9,6 -> 9,3 "$2\,\Omega$"
R4 9,3 -> 9,0 "$4\,\Omega$"
R5 3,3 -> 9,3 "$10\,\Omega$" i="$i_{10}$"
wire 0,0 -> 9,0
label 3,3 "$l$" left
label 9,3 "$r$" right
label 6,6 "$t$" above
ground 0,0
#@ spoiler
#@ straight off
#@ node t 13.2 "$t$: $13.2\,\mathrm{V}$"
#@ node r 8 "$r$: $8\,\mathrm{V}$"
#@ node l 2 "$l$: $2\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el I g t "$4\,\mathrm{A}$" col=0 i="$4\,\mathrm{A}$" to=t id=eI1
#@ el R t r "$2\,\Omega$: falls $5.2\,\mathrm{V}$" col=1 i="$2.6\,\mathrm{A}$" to=r id=eR2
#@ el R r g2 "$4\,\Omega$: falls $8\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=eR4
#@ el R l r "$10\,\Omega$: falls $6\,\mathrm{V}$" col=2 i="$0.6\,\mathrm{A}$" to=l id=eR5
#@ el R t l "$8\,\Omega$: falls $11.2\,\mathrm{V}$" col=3 i="$1.4\,\mathrm{A}$" to=l id=eR1
#@ el R l g3 "$1\,\Omega$: falls $2\,\mathrm{V}$" col=3 i="$2\,\mathrm{A}$" to=g3 id=eR3
#@ step "Ground the bottom wire. The pump pushes $4\,\mathrm{A}$ up into the top node $t$."
#@ step "Mesh walks (the pump fixes mesh 1 at $4\,\mathrm{A}$): $i_2=2.6$, $i_3=2\,\mathrm{A}$. Branch currents: $1.4\,\mathrm{A}$ down the $8\,\Omega$, $2.6$ down the $2\,\Omega$, $2$ down the $1\,\Omega$ and the $4\,\Omega$." show=eR1,eR2,eR3,eR4
#@ step "Heights, walking up from ground: $l=(2)(1)=2$, $r=(2)(4)=8$, $t=8+(2.6)(2)=13.2\,\mathrm{V}$." show=l,r,t
#@ step "The $10\,\Omega$ joins $r$ ($8$) and $l$ ($2$): it falls $6\,\mathrm{V}$, so $0.6\,\mathrm{A}$ flows $r\to l$, against $i_{10}$. $p=(6)(0.6)=3.6\,\mathrm{W}$." show=eR5
#@ step "The pump lifts $4\,\mathrm{A}$ through $13.2\,\mathrm{V}$: it delivers $52.8\,\mathrm{W}$."
```

<details><summary>Solution</summary>

1. Node: $3$ unknown heights. Mesh: $3$ meshes, but the pump fixes one.

   $$N_{\text{node}}=3,\qquad N_{\text{mesh}}=2$$
2. Upper and lower triangles, clockwise.

   $$\begin{aligned}20i_2-10i_3&=32\\-10i_2+15i_3&=4\end{aligned}\;\Rightarrow\;i_2=2.6\,\mathrm{A},\;i_3=2\,\mathrm{A}$$
3. The $10\,\Omega$ carries the difference.

   $$i_{10}=i_3-i_2=-0.6\,\mathrm{A},\qquad p=(0.6)^2(10)=3.6\,\mathrm{W}$$
4. Pump voltage = falls down the left side.

   $$v=8(1.4)+1(2)=13.2\,\mathrm{V},\qquad p=(4)(13.2)=52.8\,\mathrm{W}$$

**Answer:** **(a)** Mesh (2 equations vs 3). **(b)** $3.6\,\mathrm{W}$. **(c)** $52.8\,\mathrm{W}$ delivered.

</details>

**Problem: Try it 2 · Find the battery that silences a resistor (Textbook P4.58)** (intermediate)

The variable battery $v_{dc}$ is adjusted so that $i_o=0$. **(a)** Node or mesh? **(b)** Find $v_{dc}$. **(c)** Check the power balance.

```schematic
V1 0,3 -> 0,0 "$230\,\mathrm{V}$"
R1 0,3 -> 4,3 "$5\,\Omega$"
R2 4,3 -> 8,3 "$15\,\Omega$"
wire 0,3 -> 0,5
R3 0,5 -> 8,5 "$30\,\Omega$" i="$i_o$"
wire 8,5 -> 8,3
R4 4,3 -> 4,1.8 "$10\,\Omega$"
V2 4,1.8 -> 4,0 "$115\,\mathrm{V}$"
V3 8,3 -> 8,0 "$v_{dc}$"
R5 0,0 -> 4,0 "$20\,\Omega$"
R6 4,0 -> 8,0 "$25\,\Omega$"
label 0,3 "$a$" left
label 4,3 "$m$" above
label 8,3 "$b$" right
ground 4,0
#@ spoiler
#@ straight off
#@ node a 230 "$a$ = $b$: $230\,\mathrm{V}$"
#@ node b 230 "$a$ = $b$: $230\,\mathrm{V}$"
#@ node m 215 "$m$: $215\,\mathrm{V}$"
#@ node k 175 "115 V top: $175\,\mathrm{V}$"
#@ node z0 60 "bottom middle: $60\,\mathrm{V}$"
#@ node r 35 "$r$: $35\,\mathrm{V}$"
#@ node g 0 "$l$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$l$: $0\,\mathrm{V}$" ground
#@ el V a g "$230\,\mathrm{V}$" col=0 i="$3\,\mathrm{A}$" to=a id=eV1
#@ el R a m "$5\,\Omega$: falls $15\,\mathrm{V}$" col=1 i="$3\,\mathrm{A}$" to=m id=eR1
#@ el R m k "$10\,\Omega$: falls $40\,\mathrm{V}$" col=1 i="$4\,\mathrm{A}$" to=k id=eR4
#@ el V k z0 "$115\,\mathrm{V}$" col=1 i="$4\,\mathrm{A}$" to=z0 id=eV2
#@ el R g2 z0 "$20\,\Omega$: falls $60\,\mathrm{V}$" col=1 i="$3\,\mathrm{A}$" to=g2 id=eR5
#@ el R a b "$30\,\Omega$: no fall" col=2 id=eR3
#@ el R m b "$15\,\Omega$: falls $15\,\mathrm{V}$" col=3 i="$1\,\mathrm{A}$" to=m id=eR2
#@ el V b r "$195\,\mathrm{V}$" col=4 i="$1\,\mathrm{A}$" to=b id=eV3
#@ el R z0 r "$25\,\Omega$: falls $25\,\mathrm{V}$" col=4 i="$1\,\mathrm{A}$" to=r id=eR6
#@ step "Ground $l$, the lowest wire. Heights here are measured from $l$."
#@ step "The key fact: $i_o=0$ means the $30\,\Omega$ has **no fall**, so its two ends $a$ and $b$ sit at the **same height**." show=eR3
#@ step "So the $5\,\Omega$ and the $15\,\Omega$ both fall from that height down to $m$: the $5\,\Omega$ carries $3\times$ the current of the $15\,\Omega$. In = out at $m$ and around the left loop give $3\,\mathrm{A}$ and $1\,\mathrm{A}$; $4\,\mathrm{A}$ goes down the $10\,\Omega$ into the $115\,\mathrm{V}$ battery (it absorbs)." show=m,k,eR1,eR2,eR4,eR5,eV1,eV2
#@ step "The $1\,\mathrm{A}$ through the $15\,\Omega$ comes up the right side: $1\,\mathrm{A}$ through the $25\,\Omega$ and up through $v_{dc}$. Height difference across it: $v_{dc}=195\,\mathrm{V}$." show=r,z0,eR6,eV3
#@ step "Power: $230\,\mathrm{V}$ gives $690\,\mathrm{W}$, $v_{dc}$ gives $195\,\mathrm{W}$; slides $425\,\mathrm{W}$ + the $115\,\mathrm{V}$ battery $460\,\mathrm{W}$ = $885\,\mathrm{W}$ ✓"
```

<details><summary>Solution</summary>

1. (a) Node voltages: the condition $i_o=0$ is a statement about heights, $v_a=v_b$. Ground the bottom-middle wire.

   $$v_a=v_b,\qquad v_l=v_a-230$$
2. In = out at $m$, and the left battery loop (no current in the $30\,\Omega$).

   $$\begin{aligned}(v_a-v_m)\big(\tfrac15+\tfrac1{15}\big)&=\tfrac{v_m-115}{10}\\\tfrac{v_a-v_m}{5}&=\tfrac{230-v_a}{20}\end{aligned}\;\Rightarrow\;v_a=170,\;v_m=155\,\mathrm{V}$$
3. (b) The $1\,\mathrm{A}$ in the $15\,\Omega$ flows through the $25\,\Omega$ and $v_{dc}$.

   $$v_r=-25\,\mathrm{V},\qquad v_{dc}=v_b-v_r=195\,\mathrm{V}$$
4. (c) Power balance.

   $$230(3)+195(1)=885\,\mathrm{W}=45+15+160+180+25+460$$

**Answer:** **(a)** Node voltages. **(b)** $v_{dc}=195\,\mathrm{V}$. **(c)** $885\,\mathrm{W}$ developed $=885\,\mathrm{W}$ absorbed.

</details>

**Problem: Try it 3 · Two pumps become one loop (Textbook P4.59)** (intermediate)

**(a)** Use source transformations to find $i_o$. **(b)** Check with the node-voltage method.

```schematic
I1 0,4 -> 0,0 "$6\,\mathrm{mA}$"
wire 0,4 -> 3,4
R1 3,4 -> 3,0 "$2.3\,\mathrm{k\Omega}$"
R2 7,4 -> 3,4 "$2.7\,\mathrm{k\Omega}$" i="$i_o$"
R3 7,4 -> 7,0 "$1\,\mathrm{k\Omega}$"
wire 7,4 -> 10,4
I2 10,0 -> 10,4 "$4.2\,\mathrm{mA}$"
wire 0,0 -> 10,0
label 3,4 "$a$" above
label 7,4 "$b$" above
ground 0,0
#@ spoiler
#@ straight off
#@ node b 8.1 "$b$: $8.1\,\mathrm{V}$"
#@ node z0 6.9 "bottom wire: $6.9\,\mathrm{V}$"
#@ node g 0 "$a$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$a$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$a$: $0\,\mathrm{V}$" ground
#@ el I g z0 "$6\,\mathrm{mA}$" col=0 i="$6\,\mathrm{mA}$" to=z0 id=eI1
#@ el R g2 z0 "$2.3\,\mathrm{k\Omega}$: falls $6.9\,\mathrm{V}$" col=1 i="$3\,\mathrm{mA}$" to=g2 id=eR1
#@ el R b g3 "$2.7\,\mathrm{k\Omega}$: falls $8.1\,\mathrm{V}$" col=2 i="$3\,\mathrm{mA}$" to=g3 id=eR2
#@ el R b z0 "$1\,\mathrm{k\Omega}$: falls $1.2\,\mathrm{V}$" col=3 i="$1.2\,\mathrm{mA}$" to=z0 id=eR3
#@ el I z0 b "$4.2\,\mathrm{mA}$" col=4 i="$4.2\,\mathrm{mA}$" to=b id=eI2
#@ step "Ground node $a$, the lowest point: the $6\,\mathrm{mA}$ pump pulls current out of $a$ and drags it down. Moving ground changes no voltage difference."
#@ step "Swap each pump with its parallel resistor: $(6)(2.3)=13.8\,\mathrm{V}$ and $(4.2)(1)=4.2\,\mathrm{V}$. One loop: $i_o=\dfrac{13.8+4.2}{2.3+2.7+1}=3\,\mathrm{mA}$." show=eR2
#@ step "Place heights: the $2.7\,\mathrm{k\Omega}$ falls $(3)(2.7)=8.1\,\mathrm{V}$ from $b$ to $a$. The $2.3\,\mathrm{k\Omega}$ carries $6-3=3\,\mathrm{mA}$ from the bottom wire down to $a$: $6.9\,\mathrm{V}$." show=b,z0,eR1,eR3
#@ step "In the drawing's voltages (bottom wire $=0$): $v_a=-6.9$, $v_b=1.2\,\mathrm{V}$. Both pumps climb: they deliver $41.4$ and $5.04\,\mathrm{mW}$."
```

<details><summary>Solution</summary>

1. Swap both pumps (mA, kΩ, V).

   $$6\times2.3=13.8\,\mathrm{V},\qquad 4.2\times1=4.2\,\mathrm{V}$$
2. One series loop.

   $$i_o=\frac{13.8+4.2}{2.3+2.7+1}=3\,\mathrm{mA}$$
3. Node check (currents out).

   $$\begin{aligned}\tfrac{v_a}{2.3}+\tfrac{v_a-v_b}{2.7}+6&=0\\\tfrac{v_b}{1}+\tfrac{v_b-v_a}{2.7}&=4.2\end{aligned}\;\Rightarrow\;v_a=-6.9,\;v_b=1.2$$
4. Same current.

   $$i_o=\frac{1.2-(-6.9)}{2.7}=3\,\mathrm{mA}$$

**Answer:** $i_o=3\,\mathrm{mA}$ (both ways).

</details>

**Problem: Try it 4 · Is the 6 V source delivering? (Lecture 4)** (intermediate)

Find the power of the $6\,\mathrm{V}$ source. Is it absorbed or delivered?

```schematic
V1 0,4 -> 0,0 "$6\,\mathrm{V}$"
R1 0,4 -> 4,4 "$4\,\Omega$"
R2 4,4 -> 4,0 "$30\,\Omega$"
R3 4,4 -> 8,4 "$6\,\Omega$"
R4 8,4 -> 8,0 "$20\,\Omega$"
R5 8,4 -> 12,4 "$5\,\Omega$"
V2 12,4 -> 12,0 "$40\,\mathrm{V}$"
wire 0,0 -> 4,0
R6 4,0 -> 8,0 "$10\,\Omega$"
wire 8,0 -> 12,0
label 4,4 "$c$" above
label 8,4 "$d$" above
label 8,0 "$f$" below
ground 0,0
#@ spoiler
#@ straight off
#@ node e 40 "40 V top: $40\,\mathrm{V}$"
#@ node d 27.46 "$d$: $27.46\,\mathrm{V}$"
#@ node c 20.65 "$c$: $20.65\,\mathrm{V}$"
#@ node s 17.35 "6 V top: $17.35\,\mathrm{V}$"
#@ node z0 11.35 "bottom-left: $11.35\,\mathrm{V}$"
#@ node g 0 "$f$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$f$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$f$: $0\,\mathrm{V}$" ground
#@ el V e g "$40\,\mathrm{V}$" col=0 i="$2.508\,\mathrm{A}$" to=e id=eV2
#@ el R d e "$5\,\Omega$: falls $12.54\,\mathrm{V}$" col=1 i="$2.508\,\mathrm{A}$" to=d id=eR5
#@ el R d g2 "$20\,\Omega$: falls $27.46\,\mathrm{V}$" col=1 i="$1.373\,\mathrm{A}$" to=g2 id=eR4
#@ el R c d "$6\,\Omega$: falls $6.81\,\mathrm{V}$" col=2 i="$1.135\,\mathrm{A}$" to=c id=eR3
#@ el R c z0 "$30\,\Omega$: falls $9.3\,\mathrm{V}$" col=2 i="$0.31\,\mathrm{A}$" to=z0 id=eR2
#@ el R z0 g3 "$10\,\Omega$: falls $11.35\,\mathrm{V}$" col=2 i="$1.135\,\mathrm{A}$" to=g3 id=eR6
#@ el R s c "$4\,\Omega$: falls $3.3\,\mathrm{V}$" col=3 i="$0.825\,\mathrm{A}$" to=s id=eR1
#@ el V s z0 "$6\,\mathrm{V}$" col=3 i="$0.825\,\mathrm{A}$" to=z0 id=eV1
#@ step "Ground $f$, the lowest node (bottom-right wire). The text's voltages are measured from the bottom-left wire."
#@ step "Swaps, right to left: $40\,\mathrm{V}$ + $5\,\Omega$ → $8\,\mathrm{A}$ ∥ $5\,\Omega$; with the $20\,\Omega$ → $8\,\mathrm{A}$ ∥ $4\,\Omega$ → $32\,\mathrm{V}$ + $4\,\Omega$; plus $6+10\,\Omega$ → $1.6\,\mathrm{A}$ ∥ $20\,\Omega$. Left: $6\,\mathrm{V}$ + $4\,\Omega$ → $1.5\,\mathrm{A}$ ∥ $4\,\Omega$."
#@ step "Node $c$: $(1.5+1.6)(4\parallel20\parallel30)=9.3\,\mathrm{V}$ above the bottom-left wire, which is $3.3\,\mathrm{V}$ **above** the $6\,\mathrm{V}$ source's top." show=c
#@ step "So current falls from $c$ **into** the source's $+$ end: $\dfrac{3.3}{4}=0.825\,\mathrm{A}$, then down through it. The source **absorbs** $(6)(0.825)=4.95\,\mathrm{W}$." show=eR1,eV1
#@ step "The rest, in the original circuit: currents = fall ÷ R. Only the $40\,\mathrm{V}$ source climbs: it delivers $100.3\,\mathrm{W}$." show=d,eR2,eR3,eR4,eR5,eR6,eV2
```

<details><summary>Solution</summary>

1. Right side: three swaps.

   $$\tfrac{40}{5}=8\,\mathrm{A};\;\;5\parallel20=4\,\Omega;\;\;8\times4=32\,\mathrm{V};\;\;\tfrac{32}{6+4+10}=1.6\,\mathrm{A}$$
2. Left side.

   $$\tfrac{6}{4}=1.5\,\mathrm{A}$$
3. One node: both pumps into $4\parallel20\parallel30=3\,\Omega$.

   $$v_c=(1.5+1.6)(3)=9.3\,\mathrm{V}$$
4. Back to the original.

   $$i=\frac{6-9.3}{4}=-0.825\,\mathrm{A}\;\Rightarrow\;p=(6)(0.825)=4.95\,\mathrm{W}\text{ absorbed}$$

**Answer:** The $6\,\mathrm{V}$ source **absorbs** $4.95\,\mathrm{W}$.

</details>

**Problem: Try it 5 · A pump across a resistor (Textbook P4.60)** (intermediate)

**(a)** Use source transformations to find $i_o$. **(b)** Check with the mesh-current method.

```schematic
I1 0,0 -> 0,4 "$4\,\mathrm{A}$"
wire 0,4 -> 3,4
R1 3,4 -> 3,0 "$5\,\Omega$"
R2 3,4 -> 6,4 "$4\,\Omega$"
R3 6,4 -> 9,4 "$1\,\Omega$"
wire 6,4 -> 6,6
I2 9,6 -> 6,6 "$10\,\mathrm{A}$"
wire 9,6 -> 9,4
R4 9,4 -> 9,2 "$40\,\Omega$"
V1 9,2 -> 9,0 "$10\,\mathrm{V}$"
wire 9,4 -> 12,4
R5 12,4 -> 12,0 "$2\,\Omega$" i="$i_o$"
wire 0,0 -> 12,0
label 3,4 "$p$" above
label 6,4 "$q$" below
label 9,4 "$r$" below
ground 0,0
#@ spoiler
#@ straight off
#@ node p 16 "$p$: $16\,\mathrm{V}$"
#@ node q 12.8 "$q$: $12.8\,\mathrm{V}$"
#@ node k 10 "10 V top: $10\,\mathrm{V}$"
#@ node r 2 "$r$: $2\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ node g4 0 "ground: $0\,\mathrm{V}$" ground
#@ el I g p "$4\,\mathrm{A}$" col=0 i="$4\,\mathrm{A}$" to=p id=eI1
#@ el R p g2 "$5\,\Omega$: falls $16\,\mathrm{V}$" col=1 i="$3.2\,\mathrm{A}$" to=g2 id=eR1
#@ el R p q "$4\,\Omega$: falls $3.2\,\mathrm{V}$" col=2 i="$0.8\,\mathrm{A}$" to=q id=eR2
#@ el R q r "$1\,\Omega$: falls $10.8\,\mathrm{V}$" col=2 i="$10.8\,\mathrm{A}$" to=r id=eR3
#@ el R r g3 "$2\,\Omega$: falls $2\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=g3 id=eR5
#@ el I r q "$10\,\mathrm{A}$" col=3 i="$10\,\mathrm{A}$" to=q id=eI2
#@ el V k g4 "$10\,\mathrm{V}$" col=4 i="$0.2\,\mathrm{A}$" to=k id=eV1
#@ el R r k "$40\,\Omega$: falls $8\,\mathrm{V}$" col=5 i="$0.2\,\mathrm{A}$" to=r id=eR4
#@ step "Ground the bottom wire. The $10\,\mathrm{V}$ source fixes its top at $10\,\mathrm{V}$."
#@ step "Swaps: $4\,\mathrm{A}$ ∥ $5\,\Omega$ → $20\,\mathrm{V}$ + $5\,\Omega$; $10\,\mathrm{A}$ ∥ $1\,\Omega$ → $10\,\mathrm{V}$ + $1\,\Omega$ ($+$ toward $q$). Seen from $r$, the left side is $20-10=10\,\mathrm{V}$ behind $5+4+1=10\,\Omega$."
#@ step "Averaging at $r$: $\dfrac{10/10+10/40+0/2}{1/10+1/40+1/2}=2\,\mathrm{V}$. So $i_o=\dfrac{2}{2}=1\,\mathrm{A}$." show=r,eR5
#@ step "Back in the original: $p=16$, $q=12.8\,\mathrm{V}$. The $10\,\mathrm{A}$ pump lifts current from $r$ up to $q$; $10.8\,\mathrm{A}$ falls back through the $1\,\Omega$." show=p,q,eR1,eR2,eR3,eR4,eI1,eI2,eV1
```

<details><summary>Solution</summary>

1. Swap both pumps.

   $$4\times5=20\,\mathrm{V},\qquad 10\times1=10\,\mathrm{V}$$
2. Node $r$ with three branches: $10\,\mathrm{V}$ behind $10\,\Omega$, $10\,\mathrm{V}$ behind $40\,\Omega$, $2\,\Omega$ to ground.

   $$\frac{v_r-10}{10}+\frac{v_r-10}{40}+\frac{v_r}{2}=0\;\Rightarrow\;v_r=2\,\mathrm{V}$$
3. Answer.

   $$i_o=\frac{2}{2}=1\,\mathrm{A}$$

**Answer:** $i_o=1\,\mathrm{A}$.

</details>

**Problem: Try it 6 · A battery hung upside down (Textbook P4.61)** (intermediate)

**(a)** Use source transformations to find $i_o$. **(b)** Work back to find the power developed by the $100\,\mathrm{V}$ source.

```schematic
V1 0,0 -> 0,3 "$100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$20\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$80\,\mathrm{k\Omega}$"
R3 3,3 -> 6,3 "$3\,\mathrm{k\Omega}$"
I1 6,0 -> 6,3 "$12\,\mathrm{mA}$"
wire 6,3 -> 9,3
R4 9,3 -> 9,0 "$60\,\mathrm{k\Omega}$"
R5 9,3 -> 12,3 "$5\,\mathrm{k\Omega}$"
R6 12,3 -> 12,0 "$10\,\mathrm{k\Omega}$" i="$i_o$"
wire 0,0 -> 3,0
R7 3,0 -> 6,0 "$1\,\mathrm{k\Omega}$"
wire 6,0 -> 12,0
label 3,3 "$p$" above
label 6,3 "$q$" above
label 12,3 "$r$" above
label 3,0 "$l$" below
ground 6,0
#@ spoiler
#@ straight off
#@ node q 153 "$q$: $153\,\mathrm{V}$"
#@ node r 133 "$r$: $133\,\mathrm{V}$"
#@ node p 132 "$p$: $132\,\mathrm{V}$"
#@ node l 100 "$l$: $100\,\mathrm{V}$"
#@ node z0 93 "bottom right: $93\,\mathrm{V}$"
#@ node g 0 "battery $-$: $0\,\mathrm{V}$" ground
#@ node g2 0 "battery $-$: $0\,\mathrm{V}$" ground
#@ el R g p "$20\,\mathrm{k\Omega}$: falls $132\,\mathrm{V}$" col=0 i="$6.6\,\mathrm{mA}$" to=g id=eR1
#@ el V l g2 "$100\,\mathrm{V}$" col=1 i="$6.6\,\mathrm{mA}$" to=l id=eV1
#@ el R p q "$3\,\mathrm{k\Omega}$: falls $21\,\mathrm{V}$" col=2 i="$7\,\mathrm{mA}$" to=p id=eR3
#@ el R p l "$80\,\mathrm{k\Omega}$: falls $32\,\mathrm{V}$" col=2 i="$0.4\,\mathrm{mA}$" to=l id=eR2
#@ el R l z0 "$1\,\mathrm{k\Omega}$: falls $7\,\mathrm{V}$" col=2 i="$7\,\mathrm{mA}$" to=z0 id=eR7
#@ el I z0 q "$12\,\mathrm{mA}$" col=3 i="$12\,\mathrm{mA}$" to=q id=eI1
#@ el R q z0 "$60\,\mathrm{k\Omega}$: falls $60\,\mathrm{V}$" col=4 i="$1\,\mathrm{mA}$" to=z0 id=eR4
#@ el R q r "$5\,\mathrm{k\Omega}$: falls $20\,\mathrm{V}$" col=5 i="$4\,\mathrm{mA}$" to=r id=eR5
#@ el R r z0 "$10\,\mathrm{k\Omega}$: falls $40\,\mathrm{V}$" col=5 i="$4\,\mathrm{mA}$" to=z0 id=eR6
#@ step "Ground the lowest wire: the battery's $-$ end, on top. Heights are from there; the question's voltages are from the bottom-right wire."
#@ step "Swap from the left (kΩ, mA): the battery and $20\,\mathrm{k\Omega}$ become a $5\,\mathrm{mA}$ pump; beside the $80\,\mathrm{k\Omega}$ that is $16\,\mathrm{k\Omega}$; swap back and add the $3$ and $1\,\mathrm{k\Omega}$: the whole left side is $80\,\mathrm{V}$ behind $20\,\mathrm{k\Omega}$, pulling $q$ toward $-80\,\mathrm{V}$."
#@ step "In = out at $q$ (from the bottom-right wire): $\dfrac{q+80}{20}+\dfrac{q}{60}+\dfrac{q}{15}=12$, so $q=60\,\mathrm{V}$ and $i_o=\dfrac{60}{15}=4\,\mathrm{mA}$." show=q,r,eR4,eR5,eR6,eI1
#@ step "Back in the original: $7\,\mathrm{mA}$ leaves $q$ to the left; $6.6\,\mathrm{mA}$ of it goes through the battery from $-$ to $+$, so it **climbs** $100\,\mathrm{V}$: $660\,\mathrm{mW}$ developed." show=p,l,z0,eR1,eR2,eR3,eR7,eV1
```

<details><summary>Solution</summary>

1. Left side, swapped down to one source (kΩ, mA, V measured from the bottom-right wire).

   $$\tfrac{100}{20}=5\,\mathrm{mA};\;\;20\parallel80=16;\;\;5(16)=80\,\mathrm{V};\;\;16+3+1=20\,\mathrm{k\Omega}$$
2. In = out at $q$.

   $$\frac{q+80}{20}+\frac{q}{60}+\frac{q}{15}=12\;\Rightarrow\;q=60\,\mathrm{V},\qquad i_o=\frac{60}{5+10}=4\,\mathrm{mA}$$
3. Back to the original for the battery.

   $$p_{100\mathrm{V}}=100(6.6\,\mathrm{mA})=660\,\mathrm{mW}\text{ developed}$$

**Answer:** **(a)** $i_o=4\,\mathrm{mA}$. **(b)** The $100\,\mathrm{V}$ source develops $660\,\mathrm{mW}$.

</details>

**Problem: Try it 7 · Swaps on both ends (Textbook P4.62)** (intermediate)

**(a)** Make a series of source transformations to find $v_o$. **(b)** Check with the mesh-current method.

```schematic
I1 0,3 -> 0,0 "$2.5\,\mathrm{mA}$"
wire 0,3 -> 2,3
R1 2,3 -> 2,0 "$8\,\mathrm{k\Omega}$"
R2 2,3 -> 5,3 "$24\,\mathrm{k\Omega}$" v="$v_o$"
R3 5,3 -> 5,0 "$80\,\mathrm{k\Omega}$"
R4 5,3 -> 8,3 "$15\,\mathrm{k\Omega}$"
V1 8,3 -> 11,3 "$40\,\mathrm{V}$"
R5 11,3 -> 11,0 "$5\,\mathrm{k\Omega}$"
wire 11,3 -> 13,3
I2 13,0 -> 13,3 "$12\,\mathrm{mA}$"
wire 0,0 -> 13,0
label 2,3 "$a$" above
label 5,3 "$b$" above
label 8,3 "$c$" below
label 11,3 "$d$" below
ground 0,0
#@ spoiler
#@ straight off
#@ node c 90 "$c$: $90\,\mathrm{V}$"
#@ node b 50 "$b$ = $d$: $50\,\mathrm{V}$"
#@ node d 50 "$b$ = $d$: $50\,\mathrm{V}$"
#@ node z0 3.33 "bottom wire: $3.33\,\mathrm{V}$"
#@ node g 0 "$a$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$a$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$a$: $0\,\mathrm{V}$" ground
#@ el R g b "$24\,\mathrm{k\Omega}$: falls $50\,\mathrm{V}$" col=0 i="$2.083\,\mathrm{mA}$" to=g id=eR2 plus=g v="$v_o$"
#@ el I g2 z0 "$2.5\,\mathrm{mA}$" col=1 i="$2.5\,\mathrm{mA}$" to=z0 id=eI1
#@ el R g3 z0 "$8\,\mathrm{k\Omega}$: falls $3.33\,\mathrm{V}$" col=2 i="$0.4167\,\mathrm{mA}$" to=g3 id=eR1
#@ el R b c "$15\,\mathrm{k\Omega}$: falls $40\,\mathrm{V}$" col=3 i="$2.667\,\mathrm{mA}$" to=b id=eR4
#@ el R b z0 "$80\,\mathrm{k\Omega}$: falls $46.67\,\mathrm{V}$" col=3 i="$0.5833\,\mathrm{mA}$" to=z0 id=eR3
#@ el V c d "$40\,\mathrm{V}$" col=4 i="$2.667\,\mathrm{mA}$" to=c id=eV1
#@ el R d z0 "$5\,\mathrm{k\Omega}$: falls $46.67\,\mathrm{V}$" col=4 i="$9.333\,\mathrm{mA}$" to=z0 id=eR5
#@ el I z0 d "$12\,\mathrm{mA}$" col=5 i="$12\,\mathrm{mA}$" to=d id=eI2
#@ step "Ground $a$, the lowest wire: the $2.5\,\mathrm{mA}$ pump drags it below the bottom wire."
#@ step "Swaps (kΩ, mA): $2.5\,\mathrm{mA}\parallel8\,\mathrm{k\Omega}$ → $20\,\mathrm{V}$ behind $8\,\mathrm{k\Omega}$, pulling down; $12\,\mathrm{mA}\parallel5\,\mathrm{k\Omega}$ → $60\,\mathrm{V}$ behind $5\,\mathrm{k\Omega}$; add the $40\,\mathrm{V}$ battery and $15\,\mathrm{k\Omega}$: the right side is $100\,\mathrm{V}$ behind $20\,\mathrm{k\Omega}$."
#@ step "In = out at $b$ (from the bottom wire): $\dfrac{b-100}{20}+\dfrac{b+20}{32}+\dfrac{b}{80}=0$, so $b=46.67\,\mathrm{V}$." show=b,c,d
#@ step "The $24\,\mathrm{k\Omega}$ carries $\dfrac{46.67+20}{32}=2.08\,\mathrm{mA}$ from $b$ to $a$ and falls $50\,\mathrm{V}$. Its $+$ end ($a$) is the **lower** one: $v_o=-50\,\mathrm{V}$." show=z0,eR1,eR2,eR3,eR4,eR5,eV1,eI1,eI2
```

<details><summary>Solution</summary>

1. Swap both pumps (kΩ, mA, V).

   $$\begin{aligned}&2.5(8)=20\,\mathrm{V},\qquad 12(5)=60\,\mathrm{V}\\&\text{right side: }60+40=100\,\mathrm{V}\text{ behind }20\,\mathrm{k\Omega}\end{aligned}$$
2. In = out at $b$ (the left side is $-20\,\mathrm{V}$ behind $8+24=32\,\mathrm{k\Omega}$).

   $$\frac{v_b-100}{20}+\frac{v_b+20}{32}+\frac{v_b}{80}=0\;\Rightarrow\;v_b=46.67\,\mathrm{V}$$
3. The $24\,\mathrm{k\Omega}$.

   $$i=\frac{46.67+20}{32}=2.083\,\mathrm{mA},\qquad v_o=-24(2.083)=-50\,\mathrm{V}$$

**Answer:** $v_o=-50\,\mathrm{V}$

</details>

## Topic 2: Thévenin and Norton

> **Tip:** **How it looks in heights.**
> 
> - Seen from $a$–$b$, any circuit is **one battery $V_{\mathrm{Th}}$ behind one slide $R_{\mathrm{Th}}$**. Ground $b$.
> - **Open** (nothing attached): $a$ sits at $V_{\mathrm{Th}}$. **Short** ($a$ wired to $b$): the current that flows is $I_N$.
> - **Sources off** (battery → wire, pump → gap), push $1\,\mathrm{A}$ into $a$: $a$'s height is $R_{\mathrm{Th}}$. Or use $R_{\mathrm{Th}}=\dfrac{V_{\mathrm{Th}}}{I_N}$.
> - A load drawing $i$ makes $a$ **sag**: $v_{ab}=V_{\mathrm{Th}}-R_{\mathrm{Th}}\,i$. Norton is the swap of Thévenin: $I_N$ in parallel with $R_{\mathrm{Th}}$.

$$V_{\mathrm{Th}}=v_{oc},\qquad I_N=i_{sc},\qquad R_{\mathrm{Th}}=\frac{V_{\mathrm{Th}}}{I_N},\qquad v_{ab}=V_{\mathrm{Th}}-R_{\mathrm{Th}}\,i$$

**Example: Example 5 · The terminal sags**

A Thévenin source, $32\,\mathrm{V}$ behind $8\,\Omega$. Find $v_{ab}$ open, with a $24\,\Omega$ load, and the current with $a$ shorted to $b$.

```schematic
V1 0,3 -> 0,0 "$V_{\mathrm{Th}}=32\,\mathrm{V}$"
R1 0,3 -> 3,3 "$R_{\mathrm{Th}}=8\,\Omega$"
wire 3,3 -> 5,3
RL 5,3 -> 5,0 "$R_L$" flip
wire 5,0 -> 0,0
terminal 3,3 "$a$" above
terminal 3,0 "$b$" below
ground 0,0
#@ inline
#@ view "Open"
#@ straight off
#@ node t 32 "top = $a$: $32\,\mathrm{V}$"
#@ node a 32 "top = $a$: $32\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V t g "$V_{\mathrm{Th}}$: $32\,\mathrm{V}$" col=0 id=eV1
#@ el R t a "$R_{\mathrm{Th}}$: no fall" col=1 id=eR1
#@ step "Ground $b$. The step lifts the top to $32\,\mathrm{V}$."
#@ step "Nothing attached, no current, so $R_{\mathrm{Th}}$ has **no fall**: $a$ sits at $V_{\mathrm{Th}}=32\,\mathrm{V}$." show=a
#@ view "24 Ω load"
#@ straight off
#@ node t 32 "top: $32\,\mathrm{V}$"
#@ node a 24 "$a$: $24\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V t g "$V_{\mathrm{Th}}$: $32\,\mathrm{V}$" col=0 i="$1\,\mathrm{A}$" to=t id=eV1
#@ el R t a "$R_{\mathrm{Th}}$: falls $8\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$24\,\Omega$: falls $24\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=g2 id=eRL
#@ step "Same ground. The load draws $\dfrac{32}{8+24}=1\,\mathrm{A}$." show=eRL,eV1
#@ step "$R_{\mathrm{Th}}$ falls $(1)(8)=8\,\mathrm{V}$: $a$ **sags** to $32-8=24\,\mathrm{V}$." show=a,eR1
#@ view "Short"
#@ straight off
#@ node t 32 "top: $32\,\mathrm{V}$"
#@ node a 0 "$a$ = $b$: $0\,\mathrm{V}$" terminal
#@ node g 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ el V t g "$V_{\mathrm{Th}}$: $32\,\mathrm{V}$" col=0 i="$4\,\mathrm{A}$" to=t id=eV1
#@ el R t a "$R_{\mathrm{Th}}$: falls $32\,\mathrm{V}$" col=1 i="$4\,\mathrm{A}$" to=a id=eR1
#@ el W a g2 "short: no step" col=1 i="$4\,\mathrm{A}$" to=g2 id=eSC
#@ step "Same ground. A wire pins $a$ to $b$." show=a
#@ step "$R_{\mathrm{Th}}$ now falls the whole $32\,\mathrm{V}$: $I_N=\dfrac{32}{8}=4\,\mathrm{A}$." show=eR1,eSC,eV1
#@ note "Sag per amp $=R_{\mathrm{Th}}$: $8\,\mathrm{V}$ per amp, until $a$ hits $b$ at $4\,\mathrm{A}$."
```

1. Open, loaded, shorted.

   $$v_{oc}=32\,\mathrm{V},\qquad v_{ab}=32-8(1)=24\,\mathrm{V},\qquad i_{sc}=\frac{32}{8}=4\,\mathrm{A}$$

**Answer:** $32\,\mathrm{V}$ open, $24\,\mathrm{V}$ with the load, $I_N=4\,\mathrm{A}$.

**Example: Example 6 · All three tabs**

Find $V_{\mathrm{Th}}$, $I_N$ and $R_{\mathrm{Th}}$ at $a$–$b$.

```schematic
V1 0,3 -> 0,0 "$18\,\mathrm{V}$"
R1 0,3 -> 3,3 "$6\,\Omega$"
R2 3,3 -> 3,0 "$3\,\Omega$"
wire 3,3 -> 6,3
wire 3,0 -> 6,0
terminal 6,3 "$a$" right
terminal 6,0 "$b$" right
wire 0,0 -> 3,0
ground 0,0
#@ inline
#@ view "Open"
#@ straight off
#@ node s 18 "source top: $18\,\mathrm{V}$"
#@ node a 6 "$a$: $6\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$18\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$6\,\Omega$: falls $12\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$3\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=eR2
#@ step "Ground $b$. Divider: $2\,\mathrm{A}$; the $6\,\Omega$ falls $12\,\mathrm{V}$, so $a=6\,\mathrm{V}=V_{\mathrm{Th}}$." show=a,eR1,eR2
#@ view "Short"
#@ straight off
#@ node s 18 "source top: $18\,\mathrm{V}$"
#@ node a 0 "$a$ = $b$: $0\,\mathrm{V}$"
#@ node g 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ el V s g "$18\,\mathrm{V}$" col=0 i="$3\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$6\,\Omega$: falls $18\,\mathrm{V}$" col=1 i="$3\,\mathrm{A}$" to=a id=eR1
#@ el W a g2 "short: no step" col=1 i="$3\,\mathrm{A}$" to=g2 id=eSC
#@ step "Same ground. A wire pins $a$ to $b$: the $3\,\Omega$ has no fall; the $6\,\Omega$ falls $18\,\mathrm{V}$: $I_N=3\,\mathrm{A}$." show=a,eR1,eSC
#@ note "The $3\,\Omega$ sits across the short (no fall, no current), so it is left out of this tab."
#@ view "Sources off, push 1 A"
#@ straight off
#@ node a 2 "$a$: $2\,\mathrm{V}$" terminal
#@ node s 0 "source top = $b$: $0\,\mathrm{V}$"
#@ node g 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ el W s g "$18\,\mathrm{V}$ off: a wire" col=0 i="$0.3333\,\mathrm{A}$" to=g id=eV1
#@ el R s a "$6\,\Omega$: falls $2\,\mathrm{V}$" col=1 i="$0.3333\,\mathrm{A}$" to=s id=eR1
#@ el R a g2 "$3\,\Omega$: falls $2\,\mathrm{V}$" col=2 i="$0.6667\,\mathrm{A}$" to=g2 id=eR2
#@ el I g3 a "test $1\,\mathrm{A}$" col=3 i="$1\,\mathrm{A}$" to=a id=eIT
#@ step "Same ground. Flatten the $18\,\mathrm{V}$. $1\,\mathrm{A}$ into $6\parallel3=2\,\Omega$: $a=2\,\mathrm{V}$, so $R_{\mathrm{Th}}=2\,\Omega=\dfrac{6}{3}$." show=a,eR1,eR2,eIT
```

1. Three numbers, one check.

   $$V_{\mathrm{Th}}=6\,\mathrm{V},\quad I_N=3\,\mathrm{A},\quad R_{\mathrm{Th}}=6\parallel3=2\,\Omega=\frac{6}{3}$$

**Answer:** $V_{\mathrm{Th}}=6\,\mathrm{V}$, $I_N=3\,\mathrm{A}$, $R_{\mathrm{Th}}=2\,\Omega$.

**Example: Example 7 · Open, short, sources off (Lecture 4)**

Find the Thévenin and Norton equivalents at $a$–$b$.

```schematic
V1 0,4 -> 0,0 "$25\,\mathrm{V}$"
R1 0,4 -> 4,4 "$5\,\Omega$"
R2 4,4 -> 4,0 "$20\,\Omega$"
wire 4,4 -> 7,4
I1 7,0 -> 7,4 "$3\,\mathrm{A}$"
R3 7,4 -> 11,4 "$4\,\Omega$"
terminal 11,4 "$a$" right
terminal 11,0 "$b$" right
gap 11,4 -> 11,0 v="$v_{ab}$"
label 4,4 "$v_1$" above
wire 0,0 -> 11,0
ground 0,0
#@ inline
#@ view "Open"
#@ straight off
#@ node n 32 "$v_1$ = $a$: $32\,\mathrm{V}$"
#@ node a 32 "$v_1$ = $a$: $32\,\mathrm{V}$" terminal
#@ node s 25 "source top: $25\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$25\,\mathrm{V}$" col=0 i="$1.4\,\mathrm{A}$" to=g id=eV1
#@ el R s n "$5\,\Omega$: falls $7\,\mathrm{V}$" col=1 i="$1.4\,\mathrm{A}$" to=s id=eR1
#@ el R n g2 "$20\,\Omega$: falls $32\,\mathrm{V}$" col=2 i="$1.6\,\mathrm{A}$" to=g2 id=eR2
#@ el I g3 n "$3\,\mathrm{A}$" col=3 i="$3\,\mathrm{A}$" to=n id=eI1
#@ el R n a "$4\,\Omega$: no fall" col=3 id=eR3
#@ step "Ground $b$ (the bottom wire). The source fixes its top at $25\,\mathrm{V}$."
#@ step "Open terminal: no current in the $4\,\Omega$, so it lies flat and $a=v_1$. KCL at $v_1$: $\dfrac{v_1-25}{5}+\dfrac{v_1}{20}=3$, so $v_1=32\,\mathrm{V}=V_{\mathrm{Th}}$." show=n,a
#@ step "The pump lifted $v_1$ **above** the $25\,\mathrm{V}$ source, so $1.4\,\mathrm{A}$ falls back **into** the source." show=eR1,eR2,eV1
#@ view "Short"
#@ straight off
#@ node s 25 "source top: $25\,\mathrm{V}$"
#@ node n 16 "$v_1$: $16\,\mathrm{V}$"
#@ node a 0 "$a$ = $b$: $0\,\mathrm{V}$"
#@ node g 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ node g4 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ el V s g "$25\,\mathrm{V}$" col=0 i="$1.8\,\mathrm{A}$" to=s id=eV1
#@ el R s n "$5\,\Omega$: falls $9\,\mathrm{V}$" col=1 i="$1.8\,\mathrm{A}$" to=n id=eR1
#@ el R n g2 "$20\,\Omega$: falls $16\,\mathrm{V}$" col=2 i="$0.8\,\mathrm{A}$" to=g2 id=eR2
#@ el I g3 n "$3\,\mathrm{A}$" col=3 i="$3\,\mathrm{A}$" to=n id=eI1
#@ el R n a "$4\,\Omega$: falls $16\,\mathrm{V}$" col=4 i="$4\,\mathrm{A}$" to=a id=eR3
#@ el W a g4 "short: no step" col=4 i="$4\,\mathrm{A}$" to=g4 id=eSC
#@ step "Same ground. A wire pins $a$ to $b$, so the $4\,\Omega$ is a new path down."
#@ step "KCL at $v_1$: $\dfrac{v_1-25}{5}+\dfrac{v_1}{20}+\dfrac{v_1}{4}=3$, so $v_1=16\,\mathrm{V}$." show=n
#@ step "The $4\,\Omega$ falls $16\,\mathrm{V}$: $I_N=4\,\mathrm{A}$. So $R_{\mathrm{Th}}=\dfrac{32}{4}=8\,\Omega$." show=eR3,eSC,eR1,eR2,eV1
#@ view "Sources off, push 1 A"
#@ straight off
#@ node a 8 "$a$: $8\,\mathrm{V}$" terminal
#@ node n 4 "$v_1$: $4\,\mathrm{V}$"
#@ node s 0 "source top = $b$: $0\,\mathrm{V}$"
#@ node g 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g4 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ el W s g "$25\,\mathrm{V}$ off: a wire" col=0 i="$0.8\,\mathrm{A}$" to=g id=eV1
#@ el R s n "$5\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$0.8\,\mathrm{A}$" to=s id=eR1
#@ el R n g2 "$20\,\Omega$: falls $4\,\mathrm{V}$" col=2 i="$0.2\,\mathrm{A}$" to=g2 id=eR2
#@ el S g3 n "$3\,\mathrm{A}$ off: a gap" col=3 id=eI1
#@ el R n a "$4\,\Omega$: falls $4\,\mathrm{V}$" col=4 i="$1\,\mathrm{A}$" to=n id=eR3
#@ el I g4 a "test $1\,\mathrm{A}$" col=5 i="$1\,\mathrm{A}$" to=a id=eIT
#@ step "Same ground. Sources off: the $25\,\mathrm{V}$ step flattens to a wire (its top comes down to $0$), the $3\,\mathrm{A}$ pump becomes a gap."
#@ step "Push $1\,\mathrm{A}$ into $a$. It falls $4\,\mathrm{V}$ through the $4\,\Omega$, then $4\,\mathrm{V}$ through $5\parallel20=4\,\Omega$." show=n,eR3,eR1,eR2,eV1
#@ step "$a$ climbed $8\,\mathrm{V}$ for $1\,\mathrm{A}$: $R_{\mathrm{Th}}=8\,\Omega$, the same as $\dfrac{32}{4}$." show=a,eIT
```

1. Open: no current in the $4\,\Omega$; KCL at $v_1$.

   $$\frac{v_1-25}{5}+\frac{v_1}{20}=3\;\Rightarrow\;V_{\mathrm{Th}}=v_1=32\,\mathrm{V}$$
2. Short: the $4\,\Omega$ joins $v_1$ to $b$.

   $$\frac{v_1-25}{5}+\frac{v_1}{20}+\frac{v_1}{4}=3\;\Rightarrow\;v_1=16,\;\;I_N=\frac{16}{4}=4\,\mathrm{A}$$
3. Two ways to get the resistance.

   $$R_{\mathrm{Th}}=\frac{32}{4}=8\,\Omega=(5\parallel20)+4$$

**Answer:** Thévenin: $32\,\mathrm{V}$ in series with $8\,\Omega$. Norton: $4\,\mathrm{A}$ (toward $a$) ∥ $8\,\Omega$.

**Problem: Try it 8 · A loaded divider (Textbook P4.65)** (introductory)

Find the Thévenin equivalent at $a$–$b$.

```schematic
V1 0,4 -> 0,0 "$80\,\mathrm{V}$"
R1 0,4 -> 4,4 "$10\,\Omega$"
R2 4,4 -> 4,0 "$30\,\Omega$"
R3 4,4 -> 8,4 "$2.5\,\Omega$"
terminal 8,4 "$a$" right
terminal 8,0 "$b$" right
label 4,4 "$m$" above
wire 0,0 -> 8,0
ground 0,0
#@ spoiler
#@ view "Open"
#@ straight off
#@ node s 80 "source top: $80\,\mathrm{V}$"
#@ node m 60 "$m$ = $a$: $60\,\mathrm{V}$"
#@ node a 60 "$m$ = $a$: $60\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$80\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=s id=eV1
#@ el R s m "$10\,\Omega$: falls $20\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=m id=eR1
#@ el R m g2 "$30\,\Omega$: falls $60\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=eR2
#@ el R m a "$2.5\,\Omega$: no fall" col=2 id=eR3
#@ step "Ground $b$. The source fixes its top at $80\,\mathrm{V}$."
#@ step "Open: no current in the $2.5\,\Omega$ (flat), so $a=m$. A plain divider: $2\,\mathrm{A}$, the $10\,\Omega$ falls $20\,\mathrm{V}$, so $a=60\,\mathrm{V}=V_{\mathrm{Th}}$." show=m,a,eR1,eR2,eV1
#@ view "Sources off, push 1 A"
#@ straight off
#@ node a 10 "$a$: $10\,\mathrm{V}$" terminal
#@ node m 7.5 "$m$: $7.5\,\mathrm{V}$"
#@ node s 0 "source top = $b$: $0\,\mathrm{V}$"
#@ node g 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ el W s g "$80\,\mathrm{V}$ off: a wire" col=0 i="$0.75\,\mathrm{A}$" to=g id=eV1
#@ el R s m "$10\,\Omega$: falls $7.5\,\mathrm{V}$" col=1 i="$0.75\,\mathrm{A}$" to=s id=eR1
#@ el R m g2 "$30\,\Omega$: falls $7.5\,\mathrm{V}$" col=2 i="$0.25\,\mathrm{A}$" to=g2 id=eR2
#@ el R m a "$2.5\,\Omega$: falls $2.5\,\mathrm{V}$" col=3 i="$1\,\mathrm{A}$" to=m id=eR3
#@ el I g3 a "test $1\,\mathrm{A}$" col=4 i="$1\,\mathrm{A}$" to=a id=eIT
#@ step "Same ground. The $80\,\mathrm{V}$ step flattens to a wire."
#@ step "Push $1\,\mathrm{A}$ into $a$: it falls $2.5\,\mathrm{V}$, then $7.5\,\mathrm{V}$ through $10\parallel30=7.5\,\Omega$." show=m,eR3,eR1,eR2,eV1
#@ step "$a$ sits at $10\,\mathrm{V}$ per amp: $R_{\mathrm{Th}}=10\,\Omega$." show=a,eIT
```

<details><summary>Solution</summary>

1. Open: divider.

   $$V_{\mathrm{Th}}=80\cdot\frac{30}{10+30}=60\,\mathrm{V}$$
2. Sources off.

   $$R_{\mathrm{Th}}=(10\parallel30)+2.5=10\,\Omega$$
3. Check with the short-circuit current.

   $$i_{sc}=\frac{80}{10+(30\parallel2.5)}\cdot\frac{30}{32.5}=6\,\mathrm{A}=\frac{60}{10}$$

**Answer:** $V_{\mathrm{Th}}=60\,\mathrm{V}$, $R_{\mathrm{Th}}=10\,\Omega$.

</details>

**Problem: Try it 9 · Norton by a short (Textbook P4.64)** (intermediate)

Find the Norton equivalent at $a$–$b$.

```schematic
I1 0,0 -> 0,4 "$15\,\mathrm{A}$"
wire 0,4 -> 3,4
R1 3,4 -> 3,0 "$8\,\Omega$"
R2 3,4 -> 6,4 "$2\,\Omega$"
R3 6,4 -> 6,0 "$12\,\Omega$"
wire 6,4 -> 9,4
terminal 9,4 "$a$" right
wire 0,0 -> 3,0
R4 3,0 -> 6,0 "$10\,\Omega$"
wire 6,0 -> 9,0
terminal 9,0 "$b$" right
label 3,4 "$p$" above
label 3,0 "$q$" below
ground 6,0
#@ spoiler
#@ view "Short"
#@ straight off
#@ node p 72 "$p$: $72\,\mathrm{V}$"
#@ node a 60 "$a$, $b$ (shorted): $60\,\mathrm{V}$"
#@ node z0 60 "$a$, $b$ (shorted): $60\,\mathrm{V}$"
#@ node g 0 "$q$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$q$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$q$: $0\,\mathrm{V}$" ground
#@ el I g p "$15\,\mathrm{A}$" col=0 i="$15\,\mathrm{A}$" to=p id=eI1
#@ el R p g2 "$8\,\Omega$: falls $72\,\mathrm{V}$" col=1 i="$9\,\mathrm{A}$" to=g2 id=eR1
#@ el R p a "$2\,\Omega$: falls $12\,\mathrm{V}$" col=2 i="$6\,\mathrm{A}$" to=a id=eR2
#@ el W a z0 "short: no step" col=3 i="$6\,\mathrm{A}$" to=z0 id=eSC
#@ el R g3 z0 "$10\,\Omega$: falls $60\,\mathrm{V}$" col=4 i="$6\,\mathrm{A}$" to=g3 id=eR4
#@ step "Ground $q$, the lowest node: the pump pulls its $15\,\mathrm{A}$ out of $q$."
#@ step "A wire across $a$–$b$ shorts the $12\,\Omega$ (no fall). The $15\,\mathrm{A}$ splits: $8\,\Omega$, or $2+10=12\,\Omega$. The $12\,\Omega$ path gets $\dfrac{8}{20}(15)=6\,\mathrm{A}$, through the short: $I_N=6\,\mathrm{A}$." show=eR2,eSC,eR4,eR1
#@ step "Heights: $p=(9)(8)=72\,\mathrm{V}$; the $2\,\Omega$ falls $12\,\mathrm{V}$ to $a$, the $10\,\Omega$ falls $60\,\mathrm{V}$ to $q$." show=p,a,z0
#@ note "The $12\,\Omega$ has both ends on the short (no fall, no current), so it is left out of this tab."
#@ view "Sources off, push 1 A"
#@ straight off
#@ node a 7.5 "$a$: $7.5\,\mathrm{V}$" terminal
#@ node p 6.75 "$p$: $6.75\,\mathrm{V}$"
#@ node q 3.75 "$q$: $3.75\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el I g a "test $1\,\mathrm{A}$" col=0 i="$1\,\mathrm{A}$" to=a id=eIT
#@ el R a g2 "$12\,\Omega$: falls $7.5\,\mathrm{V}$" col=1 i="$0.625\,\mathrm{A}$" to=g2 id=eR3
#@ el R p a "$2\,\Omega$: falls $0.75\,\mathrm{V}$" col=2 i="$0.375\,\mathrm{A}$" to=p id=eR2
#@ el R p q "$8\,\Omega$: falls $3\,\mathrm{V}$" col=2 i="$0.375\,\mathrm{A}$" to=q id=eR1
#@ el R q g3 "$10\,\Omega$: falls $3.75\,\mathrm{V}$" col=2 i="$0.375\,\mathrm{A}$" to=g3 id=eR4
#@ el S q p "$15\,\mathrm{A}$ off: a gap" col=3 id=eI1
#@ step "Ground $b$ (nothing dips below it now). The pump becomes a gap."
#@ step "Push $1\,\mathrm{A}$ into $a$. Two ways down: the $12\,\Omega$, or $2+8+10=20\,\Omega$. $12\parallel20=7.5\,\Omega$, so $a$ climbs $7.5\,\mathrm{V}$: $R_N=7.5\,\Omega$." show=a,p,q,eR1,eR2,eR3,eR4,eIT
#@ view "Open (check)"
#@ straight off
#@ node p 90 "$p$: $90\,\mathrm{V}$"
#@ node a 82.5 "$a$: $82.5\,\mathrm{V}$" terminal
#@ node z0 37.5 "$b$: $37.5\,\mathrm{V}$"
#@ node g 0 "$q$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$q$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$q$: $0\,\mathrm{V}$" ground
#@ el I g p "$15\,\mathrm{A}$" col=0 i="$15\,\mathrm{A}$" to=p id=eI1
#@ el R p g2 "$8\,\Omega$: falls $90\,\mathrm{V}$" col=1 i="$11.25\,\mathrm{A}$" to=g2 id=eR1
#@ el R p a "$2\,\Omega$: falls $7.5\,\mathrm{V}$" col=2 i="$3.75\,\mathrm{A}$" to=a id=eR2
#@ el R a z0 "$12\,\Omega$: falls $45\,\mathrm{V}$" col=2 i="$3.75\,\mathrm{A}$" to=z0 id=eR3
#@ el R g3 z0 "$10\,\Omega$: falls $37.5\,\mathrm{V}$" col=2 i="$3.75\,\mathrm{A}$" to=g3 id=eR4
#@ step "Ground $q$ again (lowest)."
#@ step "Open: $15\,\mathrm{A}$ splits $8$ vs $2+12+10=24\,\Omega$, so $3.75\,\mathrm{A}$ goes through the $12\,\Omega$: $v_{ab}=45\,\mathrm{V}=(6)(7.5)$ ✓." show=a,z0,p,eR1,eR2,eR3,eR4
```

<details><summary>Solution</summary>

1. Short: current divider between $8\,\Omega$ and $2+10\,\Omega$.

   $$I_N=15\cdot\frac{8}{8+12}=6\,\mathrm{A}$$
2. Pump off (a gap).

   $$R_N=12\parallel(2+8+10)=7.5\,\Omega$$
3. Check.

   $$v_{oc}=I_NR_N=45\,\mathrm{V}=(3.75)(12)$$

**Answer:** $I_N=6\,\mathrm{A}$ (toward $a$) ∥ $R_N=7.5\,\Omega$.

</details>

**Problem: Try it 10 · Norton with a bypass (Textbook P4.66)** (intermediate)

Find the Norton equivalent at $a$–$b$.

```schematic
V1 0,3 -> 0,0 "$72\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$"
R2 3,3 -> 6,3 "$8\,\Omega$"
R3 3,3 -> 3,0 "$20\,\Omega$"
wire 0,3 -> 0,5
R4 0,5 -> 6,5 "$12\,\Omega$"
wire 6,5 -> 6,3
wire 6,3 -> 8,3
terminal 8,3 "$a$" right
terminal 8,0 "$b$" right
wire 0,0 -> 8,0
label 3,3 "$m$" above
ground 0,0
#@ spoiler
#@ view "Short"
#@ straight off
#@ node s 72 "battery top: $72\,\mathrm{V}$"
#@ node m 38.4 "$m$: $38.4\,\mathrm{V}$"
#@ node a 0 "$a$ = $b$: $0\,\mathrm{V}$"
#@ node g 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ el V s g "$72\,\mathrm{V}$" col=0 i="$12.72\,\mathrm{A}$" to=s id=eV1
#@ el R s m "$5\,\Omega$: falls $33.6\,\mathrm{V}$" col=1 i="$6.72\,\mathrm{A}$" to=m id=eR1
#@ el R m g2 "$20\,\Omega$: falls $38.4\,\mathrm{V}$" col=2 i="$1.92\,\mathrm{A}$" to=g2 id=eR3
#@ el R m a "$8\,\Omega$: falls $38.4\,\mathrm{V}$" col=3 i="$4.8\,\mathrm{A}$" to=a id=eR2
#@ el R s a "$12\,\Omega$: falls $72\,\mathrm{V}$" col=4 i="$6\,\mathrm{A}$" to=a id=eR4
#@ el W a g3 "short: no step" col=4 i="$10.8\,\mathrm{A}$" to=g3 id=eSC
#@ step "Ground $b$. The battery lifts its top to $72\,\mathrm{V}$. A wire pins $a$ to $b$."
#@ step "Now $m$ is the only unknown. In = out at $m$: $\dfrac{72-m}{5}=\dfrac{m}{20}+\dfrac{m}{8}$, so $m=38.4\,\mathrm{V}$." show=m
#@ step "Into the short: $\dfrac{72}{12}+\dfrac{38.4}{8}=6+4.8=10.8\,\mathrm{A}=I_N$." show=eR2,eR4,eSC,eR1,eR3,eV1
#@ view "Sources off, push 1 A"
#@ straight off
#@ node a 6 "$a$: $6\,\mathrm{V}$" terminal
#@ node m 2 "$m$: $2\,\mathrm{V}$"
#@ node s 0 "battery top = $b$: $0\,\mathrm{V}$"
#@ node g 0 "battery top = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "battery top = $b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "battery top = $b$: $0\,\mathrm{V}$" ground
#@ el R s a "$12\,\Omega$: falls $6\,\mathrm{V}$" col=0 i="$0.5\,\mathrm{A}$" to=s id=eR4
#@ el W s g "$72\,\mathrm{V}$ off: a wire" col=0 i="$0.9\,\mathrm{A}$" to=g id=eV1
#@ el R m a "$8\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$0.5\,\mathrm{A}$" to=m id=eR2
#@ el R s m "$5\,\Omega$: falls $2\,\mathrm{V}$" col=2 i="$0.4\,\mathrm{A}$" to=s id=eR1
#@ el R m g2 "$20\,\Omega$: falls $2\,\mathrm{V}$" col=3 i="$0.1\,\mathrm{A}$" to=g2 id=eR3
#@ el I g3 a "test $1\,\mathrm{A}$" col=4 i="$1\,\mathrm{A}$" to=a id=eIT
#@ step "Same ground. Battery → wire. Push $1\,\mathrm{A}$ into $a$: $12\,\Omega$ straight down, or $8+(5\parallel20)=12\,\Omega$. Half each." show=eR1,eR2,eR3,eR4,eV1
#@ step "$a=(0.5)(12)=6\,\mathrm{V}$: $R_N=6\,\Omega$. (Check: open height $=I_NR_N=64.8\,\mathrm{V}$.)" show=a,m,eIT
```

<details><summary>Solution</summary>

1. Short: in = out at $m$.

   $$\begin{aligned}&\frac{72-v_m}{5}=\frac{v_m}{20}+\frac{v_m}{8}\;\Rightarrow\;v_m=38.4\,\mathrm{V}\\&I_N=\frac{72}{12}+\frac{38.4}{8}=10.8\,\mathrm{A}\end{aligned}$$
2. Sources off.

   $$R_N=12\parallel\big(8+(5\parallel20)\big)=12\parallel12=6\,\Omega$$

**Answer:** $I_N=10.8\,\mathrm{A}$ (toward $a$) in parallel with $R_N=6\,\Omega$.

</details>

**Problem: Try it 11 · Norton when a battery fixes a wire (Textbook P4.67)** (intermediate)

Find the Norton equivalent at $a$–$b$.

```schematic
I1 0,0 -> 0,3 "$10\,\mathrm{mA}$"
R1 2,3 -> 2,0 "$10\,\mathrm{k\Omega}$"
V1 4,3 -> 4,0 "$30\,\mathrm{V}$"
wire 0,3 -> 4,3
R2 4,3 -> 7,3 "$15\,\mathrm{k\Omega}$"
I2 7,3 -> 7,0 "$3\,\mathrm{mA}$"
R3 9,3 -> 9,0 "$5\,\mathrm{k\Omega}$"
wire 7,3 -> 11,3
terminal 11,3 "$a$" right
terminal 11,0 "$b$" right
wire 0,0 -> 11,0
ground 0,0
#@ spoiler
#@ view "Open"
#@ straight off
#@ node n 33.75 "battery top: $33.75\,\mathrm{V}$"
#@ node z0 3.75 "$b$ (bottom): $3.75\,\mathrm{V}$"
#@ node g 0 "$a$: $0\,\mathrm{V}$" ground terminal
#@ node g2 0 "$a$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$a$: $0\,\mathrm{V}$" ground
#@ el I z0 n "$10\,\mathrm{mA}$" col=0 i="$10\,\mathrm{mA}$" to=n id=eI1
#@ el R n z0 "$10\,\mathrm{k\Omega}$: falls $30\,\mathrm{V}$" col=1 i="$3\,\mathrm{mA}$" to=z0 id=eR1
#@ el V n z0 "$30\,\mathrm{V}$" col=2 i="$4.75\,\mathrm{mA}$" to=z0 id=eV1
#@ el I g z0 "$3\,\mathrm{mA}$" col=3 i="$3\,\mathrm{mA}$" to=z0 id=eI2
#@ el R g2 z0 "$5\,\mathrm{k\Omega}$: falls $3.75\,\mathrm{V}$" col=4 i="$0.75\,\mathrm{mA}$" to=g2 id=eR3
#@ el R n g3 "$15\,\mathrm{k\Omega}$: falls $33.75\,\mathrm{V}$" col=5 i="$2.25\,\mathrm{mA}$" to=g3 id=eR2
#@ step "Ground $a$, the lowest wire: the $3\,\mathrm{mA}$ pump drags it below $b$. The $30\,\mathrm{V}$ battery fixes the top-left wire $30\,\mathrm{V}$ above $b$; the $10\,\mathrm{mA}$ pump and $10\,\mathrm{k\Omega}$ beside it change nothing at $a$–$b$."
#@ step "In = out at $a$ (from $b$): $\dfrac{30-a}{15}=3+\dfrac{a}{5}$, so $a=-3.75\,\mathrm{V}$: $V_{\mathrm{Th}}=-3.75\,\mathrm{V}$." show=z0,n,eR2,eR3,eI2
#@ step "With a short, $a$ would be pulled up to $b$: $I_N=\dfrac{V_{\mathrm{Th}}}{R_N}=-1\,\mathrm{mA}$ (tab 2 gives $R_N$). Directly: $\dfrac{30}{15}-3=-1\,\mathrm{mA}$." show=eR1,eV1,eI1
#@ view "Sources off, push 1 mA"
#@ straight off
#@ node a 3.75 "$a$: $3.75\,\mathrm{V}$" terminal
#@ node n 0 "battery top = $b$: $0\,\mathrm{V}$"
#@ node g 0 "battery top = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "battery top = $b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "battery top = $b$: $0\,\mathrm{V}$" ground
#@ node g4 0 "battery top = $b$: $0\,\mathrm{V}$" ground
#@ el W n g "$30\,\mathrm{V}$ off: a wire" col=0 i="$0.25\,\mathrm{mA}$" to=g id=eV1
#@ el R n a "$15\,\mathrm{k\Omega}$: falls $3.75\,\mathrm{V}$" col=1 i="$0.25\,\mathrm{mA}$" to=n id=eR2
#@ el S a g2 "$3\,\mathrm{mA}$ off: a gap" col=2 id=eI2
#@ el R a g3 "$5\,\mathrm{k\Omega}$: falls $3.75\,\mathrm{V}$" col=3 i="$0.75\,\mathrm{mA}$" to=g3 id=eR3
#@ el I g4 a "test $1\,\mathrm{mA}$" col=4 i="$1\,\mathrm{mA}$" to=a id=eIT
#@ step "Same ground. Battery → wire, pumps → gaps. Push $1\,\mathrm{mA}$ into $a$: $15\parallel5=3.75\,\mathrm{k\Omega}$, so $a$ climbs $3.75\,\mathrm{V}$: $R_N=3.75\,\mathrm{k\Omega}$." show=a,eR2,eR3,eIT,eV1
#@ step "Check: open height $=I_NR_N=-3.75\,\mathrm{V}$, so with nothing attached $a$ sits **below** $b$."
#@ note "The $10\,\mathrm{k\Omega}$ and the $10\,\mathrm{mA}$ pump sit across the flattened battery, so they are left out."
```

<details><summary>Solution</summary>

1. Short: the battery fixes the left wire; in = out at $a$ (mA, kΩ).

   $$\frac{30}{15}-3+I_N^{\,\text{in}}=0\;\Rightarrow\;I_N=\frac{30}{15}-3=-1\,\mathrm{mA}$$
2. Sources off.

   $$R_N=15\parallel5=3.75\,\mathrm{k\Omega}$$

**Answer:** $I_N=-1\,\mathrm{mA}$ (so $1\,\mathrm{mA}$ points from $a$ to $b$ inside the source) in parallel with $R_N=3.75\,\mathrm{k\Omega}$.

</details>

**Problem: Try it 12 · Thévenin from two measurements (Textbook P4.69)** (intermediate)

A box holds an unknown linear circuit. A $15\,\mathrm{k\Omega}$ load on $a$–$b$ reads $v_{ab}=45\,\mathrm{V}$; a $5\,\mathrm{k\Omega}$ load reads $25\,\mathrm{V}$. Find the Thévenin equivalent.

```schematic
X1 0,3 -> 0,0 "network"
wire 0,3 -> 3,3
wire 0,0 -> 3,0
RL 3,3 -> 3,0 "$R_L$" flip
terminal 3,3 "$a$" above
terminal 3,0 "$b$" below
ground 0,0
#@ spoiler
#@ view "15 kΩ load"
#@ straight off
#@ node t 75 "inside: top of the step: $75\,\mathrm{V}$"
#@ node a 45 "$a$: $45\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V t g "$V_{\mathrm{Th}}$: $75\,\mathrm{V}$" col=0 i="$3\,\mathrm{mA}$" to=t id=eVT
#@ el R t a "$R_{\mathrm{Th}}$: falls $30\,\mathrm{V}$" col=1 i="$3\,\mathrm{mA}$" to=a id=eRT
#@ el R a g2 "$15\,\mathrm{k\Omega}$: falls $45\,\mathrm{V}$" col=1 i="$3\,\mathrm{mA}$" to=g2 id=eRL
#@ step "Ground $b$. The box is drawn as its answer: one step and one slope."
#@ step "The $15\,\mathrm{k\Omega}$ load sits at $45\,\mathrm{V}$, so it draws $\dfrac{45}{15}=3\,\mathrm{mA}$." show=eRL
#@ step "Tab 2: the $5\,\mathrm{k\Omega}$ draws $\dfrac{25}{5}=5\,\mathrm{mA}$. $2\,\mathrm{mA}$ more made $a$ sag $20\,\mathrm{V}$: $R_{\mathrm{Th}}=10\,\mathrm{k\Omega}$." show=eRT
#@ step "Open height: $45+(3)(10)=75\,\mathrm{V}=V_{\mathrm{Th}}$." show=t,eVT
#@ view "5 kΩ load"
#@ straight off
#@ node t 75 "inside: top of the step: $75\,\mathrm{V}$"
#@ node a 25 "$a$: $25\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V t g "$V_{\mathrm{Th}}$: $75\,\mathrm{V}$" col=0 i="$5\,\mathrm{mA}$" to=t id=eVT
#@ el R t a "$R_{\mathrm{Th}}$: falls $50\,\mathrm{V}$" col=1 i="$5\,\mathrm{mA}$" to=a id=eRT
#@ el R a g2 "$5\,\mathrm{k\Omega}$: falls $25\,\mathrm{V}$" col=1 i="$5\,\mathrm{mA}$" to=g2 id=eRL
#@ note "Same step and slope as tab 1. More current, more sag: $50\,\mathrm{V}$ lost inside, $25\,\mathrm{V}$ left at $a$."
```

<details><summary>Solution</summary>

1. Load currents.

   $$i_1=\frac{45}{15}=3\,\mathrm{mA},\qquad i_2=\frac{25}{5}=5\,\mathrm{mA}$$
2. Two points on $v=V_{\mathrm{Th}}-R_{\mathrm{Th}}i$ (kΩ, mA).

   $$\begin{aligned}45&=V_{\mathrm{Th}}-3R_{\mathrm{Th}}\\25&=V_{\mathrm{Th}}-5R_{\mathrm{Th}}\end{aligned}$$
3. Subtract.

   $$R_{\mathrm{Th}}=10\,\mathrm{k\Omega},\qquad V_{\mathrm{Th}}=75\,\mathrm{V}$$

**Answer:** $V_{\mathrm{Th}}=75\,\mathrm{V}$, $R_{\mathrm{Th}}=10\,\mathrm{k\Omega}$.

</details>

**Problem: Try it 13 · A pump that feeds back (Textbook P4.68)** (intermediate)

Find the Thévenin equivalent at $a$–$b$.

```schematic
V1 0,3 -> 0,0 "$300\,\mathrm{V}$"
R1 0,3 -> 4,3 "$40\,\Omega$"
R2 4,3 -> 4,0 "$8\,\Omega$"
R3 4,3 -> 8,3 "$10\,\Omega$"
wire 0,3 -> 0,5
R4 0,5 -> 8,5 "$150\,\Omega$"
wire 8,5 -> 8,3
wire 0,5 -> 0,7
I1 8,7 -> 0,7 "$3\,\mathrm{A}$"
wire 8,7 -> 8,5
wire 8,3 -> 10,3
terminal 10,3 "$a$" right
terminal 10,0 "$b$" right
wire 0,0 -> 10,0
label 4,3 "$m$" above
ground 0,0
#@ spoiler
#@ view "Open"
#@ straight off
#@ node s 300 "source top: $300\,\mathrm{V}$"
#@ node m 42 "$m$: $42\,\mathrm{V}$"
#@ node a 30 "$a$: $30\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$300\,\mathrm{V}$" col=0 i="$5.25\,\mathrm{A}$" to=s id=eV1
#@ el R s m "$40\,\Omega$: falls $258\,\mathrm{V}$" col=1 i="$6.45\,\mathrm{A}$" to=m id=eR1
#@ el R m g2 "$8\,\Omega$: falls $42\,\mathrm{V}$" col=1 i="$5.25\,\mathrm{A}$" to=g2 id=eR2
#@ el R m a "$10\,\Omega$: falls $12\,\mathrm{V}$" col=2 i="$1.2\,\mathrm{A}$" to=a id=eR3
#@ el R s a "$150\,\Omega$: falls $270\,\mathrm{V}$" col=3 i="$1.8\,\mathrm{A}$" to=a id=eR4
#@ el I a s "$3\,\mathrm{A}$" col=4 i="$3\,\mathrm{A}$" to=s id=eI1
#@ step "Ground $b$. The source fixes its top at $300\,\mathrm{V}$."
#@ step "Two unknown heights, $m$ and $a$. KCL: $\dfrac{m-300}{40}+\dfrac{m}{8}+\dfrac{m-a}{10}=0$ and $\dfrac{a-300}{150}+\dfrac{a-m}{10}+3=0$. So $m=42$, $a=30\,\mathrm{V}=V_{\mathrm{Th}}$." show=m,a
#@ step "$1.2+1.8=3\,\mathrm{A}$ arrive at $a$, and the pump lifts all of it back to the top: $810\,\mathrm{W}$ delivered." show=eR1,eR2,eR3,eR4,eV1,eI1
#@ view "Sources off, push 1 A"
#@ straight off
#@ node a 15 "$a$: $15\,\mathrm{V}$" terminal
#@ node m 6 "$m$: $6\,\mathrm{V}$"
#@ node s 0 "source top = $b$: $0\,\mathrm{V}$"
#@ node g 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ el I g a "test $1\,\mathrm{A}$" col=0 i="$1\,\mathrm{A}$" to=a id=eIT
#@ el R s a "$150\,\Omega$: falls $15\,\mathrm{V}$" col=1 i="$0.1\,\mathrm{A}$" to=s id=eR4
#@ el R m a "$10\,\Omega$: falls $9\,\mathrm{V}$" col=2 i="$0.9\,\mathrm{A}$" to=m id=eR3
#@ el R s m "$40\,\Omega$: falls $6\,\mathrm{V}$" col=3 i="$0.15\,\mathrm{A}$" to=s id=eR1
#@ el W s g2 "$300\,\mathrm{V}$ off: a wire" col=3 i="$0.25\,\mathrm{A}$" to=g2 id=eV1
#@ el R m g3 "$8\,\Omega$: falls $6\,\mathrm{V}$" col=4 i="$0.75\,\mathrm{A}$" to=g3 id=eR2
#@ el S a s "$3\,\mathrm{A}$ off: a gap" col=5 id=eI1
#@ step "Same ground. $300\,\mathrm{V}$ → a wire, $3\,\mathrm{A}$ → a gap."
#@ step "Push $1\,\mathrm{A}$ into $a$. Two ways down: the $150\,\Omega$, or $10\,\Omega$ then $40\parallel8=6.67\,\Omega$. $150\parallel16.67=15\,\Omega$." show=m,eR1,eR2,eR3,eR4,eV1
#@ step "$a$ sits at $15\,\mathrm{V}$: $R_{\mathrm{Th}}=15\,\Omega$." show=a,eIT
```

<details><summary>Solution</summary>

1. Open: KCL at $m$ and $a$.

   $$\begin{aligned}\tfrac{m-300}{40}+\tfrac{m}{8}+\tfrac{m-a}{10}&=0\\\tfrac{a-300}{150}+\tfrac{a-m}{10}+3&=0\end{aligned}\;\Rightarrow\;a=30\,\mathrm{V}$$
2. Sources off.

   $$R_{\mathrm{Th}}=150\parallel\big(10+(40\parallel8)\big)=150\parallel16.67=15\,\Omega$$

**Answer:** $V_{\mathrm{Th}}=30\,\mathrm{V}$, $R_{\mathrm{Th}}=15\,\Omega$.

</details>

**Problem: Try it 14 · Thévenin two ways (Textbook P4.77)** (intermediate)

**(a)** Find the Thévenin equivalent at $a$–$b$ from the open-circuit voltage and the short-circuit current. **(b)** Find $R_{\mathrm{Th}}$ by removing the sources and compare.

```schematic
V1 0,3 -> 0,0 "$17.4\,\mathrm{V}$"
R1 0,3 -> 4,3 "$40\,\Omega$"
R2 4,3 -> 4,0 "$15\,\Omega$"
I1 4,3 -> 8,3 "$100\,\mathrm{mA}$"
wire 0,3 -> 0,5
R3 0,5 -> 8,5 "$26\,\Omega$"
wire 8,5 -> 8,3
R4 8,3 -> 8,0 "$10\,\Omega$"
wire 0,0 -> 4,0
R5 4,0 -> 8,0 "$4\,\Omega$"
wire 8,3 -> 10,3
wire 8,0 -> 10,0
terminal 10,3 "$a$" right
terminal 10,0 "$b$" right
label 4,3 "$p$" above
ground 0,0
#@ spoiler
#@ view "Open"
#@ straight off
#@ node s 17.4 "$s$: $17.4\,\mathrm{V}$"
#@ node a 7 "$a$: $7\,\mathrm{V}$" terminal
#@ node p 3.65 "$p$: $3.65\,\mathrm{V}$"
#@ node b 2 "$b$: $2\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V s g "$17.4\,\mathrm{V}$" col=0 i="$0.7436\,\mathrm{A}$" to=s id=eV1
#@ el R s p "$40\,\Omega$: falls $13.75\,\mathrm{V}$" col=1 i="$0.3436\,\mathrm{A}$" to=p id=eR1
#@ el R p g2 "$15\,\Omega$: falls $3.65\,\mathrm{V}$" col=1 i="$0.2436\,\mathrm{A}$" to=g2 id=eR2
#@ el I p a "$0.1\,\mathrm{A}$" col=2 i="$0.1\,\mathrm{A}$" to=a id=eI1
#@ el R s a "$26\,\Omega$: falls $10.4\,\mathrm{V}$" col=3 i="$0.4\,\mathrm{A}$" to=a id=eR3
#@ el R a b "$10\,\Omega$: falls $5\,\mathrm{V}$" col=4 i="$0.5\,\mathrm{A}$" to=b id=eR4
#@ el R g3 b "$4\,\Omega$: falls $2\,\mathrm{V}$" col=4 i="$0.5\,\mathrm{A}$" to=g3 id=eR5
#@ step "Ground the bottom-left wire. The battery lifts its top to $17.4\,\mathrm{V}$."
#@ step "Unknowns $p$, $a$, $b$. The pump forces $0.1\,\mathrm{A}$ from $p$ to $a$. In = out at each: $p=3.65$, $a=7$, $b=2\,\mathrm{V}$." show=p,a,b
#@ step "$v_{ab}=a-b=5\,\mathrm{V}=V_{\mathrm{Th}}$. (A short across $a$–$b$ would carry $I_N=0.667\,\mathrm{A}$, so $R_{\mathrm{Th}}=\dfrac{5}{0.667}=7.5\,\Omega$.)" show=eR1,eR2,eR3,eR4,eR5,eV1,eI1
#@ view "Sources off, push 1 A"
#@ straight off
#@ node a 7.5 "$a$: $7.5\,\mathrm{V}$" terminal
#@ node s 1 "$s$ = bottom: $1\,\mathrm{V}$"
#@ node z0 1 "$s$ = bottom: $1\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el R s a "$26\,\Omega$: falls $6.5\,\mathrm{V}$" col=0 i="$0.25\,\mathrm{A}$" to=s id=eR3
#@ el W s z0 "$17.4\,\mathrm{V}$ off: a wire" col=0 i="$0.25\,\mathrm{A}$" to=z0 id=eV1
#@ el R z0 g "$4\,\Omega$: falls $1\,\mathrm{V}$" col=1 i="$0.25\,\mathrm{A}$" to=g id=eR5
#@ el R a g2 "$10\,\Omega$: falls $7.5\,\mathrm{V}$" col=2 i="$0.75\,\mathrm{A}$" to=g2 id=eR4
#@ el I g3 a "test $1\,\mathrm{A}$ from $b$ to $a$" col=3 i="$1\,\mathrm{A}$" to=a id=eIT
#@ step "Ground $b$ (the lowest here). Battery → wire, pump → gap. Push $1\,\mathrm{A}$ from $b$ into $a$."
#@ step "Two paths from $a$ back to $b$: the $10\,\Omega$, or $26+4=30\,\Omega$. $10\parallel30=7.5\,\Omega$, so $a$ climbs $7.5\,\mathrm{V}$: $R_{\mathrm{Th}}=7.5\,\Omega$, the same." show=a,eR3,eR4,eR5,eIT,eV1
#@ note "The $40\,\Omega$ and $15\,\Omega$ only reach $a$ through the pump's gap: no current, so they are left out."
```

<details><summary>Solution</summary>

1. Open: three node equations give the heights.

   $$v_p=3.65,\quad v_a=7,\quad v_b=2\,\mathrm{V}\;\Rightarrow\;V_{\mathrm{Th}}=5\,\mathrm{V}$$
2. Short circuit.

   $$i_{sc}=0.667\,\mathrm{A}\;\Rightarrow\;R_{\mathrm{Th}}=\frac{5}{0.667}=7.5\,\Omega$$
3. (b) Sources off.

   $$R_{\mathrm{Th}}=10\parallel(26+4)=7.5\,\Omega\;\checkmark$$

**Answer:** $V_{\mathrm{Th}}=5\,\mathrm{V}$, $R_{\mathrm{Th}}=7.5\,\Omega$ (both ways).

</details>

## Practice set

Exam-style, mixing both topics. Try each for 10–15 minutes before opening the solution, then check your picture against the height view.

**Problem: Textbook P4.63 · Swaps, then every power** (advanced)

**(a)** Use source transformations to find $v_o$. **(b)** Find the power developed by the $340\,\mathrm{V}$ source and **(c)** by the $5\,\mathrm{A}$ source. **(d)** Check the power balance.

```schematic
I1 0,0 -> 0,4 "$5\,\mathrm{A}$"
R1 0,4 -> 3,4 "$8\,\Omega$"
R2 3,4 -> 3,0 "$20\,\Omega$"
wire 3,4 -> 3,7
V1 3,7 -> 6,7 "$340\,\mathrm{V}$"
wire 6,7 -> 6,4
R3 3,4 -> 6,4 "$80\,\Omega$"
R4 6,4 -> 9,4 "$5\,\Omega$"
wire 9,4 -> 12,4
R5 12,4 -> 12,0 "$45\,\Omega$"
wire 0,0 -> 3,0
R6 3,0 -> 9,0 "$10\,\Omega$"
wire 9,0 -> 12,0
gap 9,4 -> 9,0 v="$v_o$"
label 3,4 "$q$" above
label 6,4 "$r$" above
label 9,0 "$m$" below
ground 0,0
#@ spoiler
#@ straight off
#@ node p 380 "pump top: $380\,\mathrm{V}$"
#@ node q 340 "$q$: $340\,\mathrm{V}$"
#@ node z0 180 "bottom-left: $180\,\mathrm{V}$"
#@ node m 150 "$m$: $150\,\mathrm{V}$"
#@ node s 15 "$v_o$ +: $15\,\mathrm{V}$"
#@ node g 0 "$r$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$r$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$r$: $0\,\mathrm{V}$" ground
#@ el V q g "$340\,\mathrm{V}$" col=0 i="$7.25\,\mathrm{A}$" to=q id=eV1
#@ el R q g2 "$80\,\Omega$: falls $340\,\mathrm{V}$" col=1 i="$4.25\,\mathrm{A}$" to=g2 id=eR3
#@ el R p q "$8\,\Omega$: falls $40\,\mathrm{V}$" col=2 i="$5\,\mathrm{A}$" to=q id=eR1
#@ el R q z0 "$20\,\Omega$: falls $160\,\mathrm{V}$" col=2 i="$8\,\mathrm{A}$" to=z0 id=eR2
#@ el R z0 m "$10\,\Omega$: falls $30\,\mathrm{V}$" col=2 i="$3\,\mathrm{A}$" to=m id=eR6
#@ el R s m "$45\,\Omega$: falls $135\,\mathrm{V}$" col=2 i="$3\,\mathrm{A}$" to=s id=eR5
#@ el R g3 s "$5\,\Omega$: falls $15\,\mathrm{V}$" col=2 i="$3\,\mathrm{A}$" to=g3 id=eR4
#@ el I z0 p "$5\,\mathrm{A}$" col=3 i="$5\,\mathrm{A}$" to=p id=eI1
#@ step "Ground $r$, the lowest node (the $340\,\mathrm{V}$ source's $-$ end). Moving ground changes no answer."
#@ step "Drop the $8\,\Omega$ (series with the pump) and the $80\,\Omega$ (across the $340\,\mathrm{V}$). Swap $5\,\mathrm{A}$ ∥ $20\,\Omega$ for $100\,\mathrm{V}$ + $20\,\Omega$. One loop: $100-340=80i$, so $i=-3\,\mathrm{A}$: $3\,\mathrm{A}$ runs counter-clockwise." show=eR4,eR5,eR6
#@ step "Climb from $r$ against that current: $5\,\Omega$ ($15\,\mathrm{V}$), $45\,\Omega$ ($135\,\mathrm{V}$) to $m=150$, $10\,\Omega$ ($30\,\mathrm{V}$) to the bottom-left wire at $180$. So $v_o=15-150=-135\,\mathrm{V}$." show=s,m,z0
#@ step "Original circuit: the $20\,\Omega$ carries $5+3=8\,\mathrm{A}$, so $q=180+160=340$ ✓. The $8\,\Omega$ adds $40\,\mathrm{V}$: the pump lifts $5\,\mathrm{A}$ through $380-180=200\,\mathrm{V}$: $1000\,\mathrm{W}$." show=p,eR1,eR2,eI1
#@ step "The $340\,\mathrm{V}$ source lifts $3+4.25=7.25\,\mathrm{A}$ (the loop plus the $80\,\Omega$'s current): $2465\,\mathrm{W}$. Total $3465\,\mathrm{W}$ = the six falls." show=eV1,eR3
```

<details><summary>Solution</summary>

1. Drop the $8\,\Omega$ and $80\,\Omega$; swap the pump.

   $$5\times20=100\,\mathrm{V}$$
2. One loop, clockwise.

   $$\begin{aligned}100-340&=(20+5+45+10)\,i\;\Rightarrow\;i=-3\,\mathrm{A}\\v_o&=45i=-135\,\mathrm{V}\end{aligned}$$
3. $340\,\mathrm{V}$ source.

   $$i=3+\tfrac{340}{80}=7.25\,\mathrm{A},\qquad p=2465\,\mathrm{W}$$
4. $5\,\mathrm{A}$ source.

   $$v=20(8)+8(5)=200\,\mathrm{V},\qquad p=1000\,\mathrm{W}$$
5. Balance.

   $$2465+1000=3465=200+1280+1445+45+405+90$$

**Answer:** **(a)** $v_o=-135\,\mathrm{V}$ **(b)** $2465\,\mathrm{W}$ **(c)** $1000\,\mathrm{W}$ **(d)** $3465\,\mathrm{W}$ both ways.

</details>

**Problem: Textbook P4.56 · Read power as a height difference** (intermediate)

The variable current source $i_{dc}$ is adjusted so that the $15\,\mathrm{A}$ source develops $3750\,\mathrm{W}$. **(a)** Node or mesh? **(b)** Find $i_{dc}$.

```schematic
V1 0,3 -> 0,0 "$420\,\mathrm{V}$"
R1 0,3 -> 3,3 "$7.2\,\Omega$"
R2 3,3 -> 3,0 "$20\,\Omega$"
R3 3,3 -> 6,3 "$15\,\Omega$"
wire 3,3 -> 3,5
I1 6,5 -> 3,5 "$15\,\mathrm{A}$"
wire 6,5 -> 6,3
R4 6,3 -> 6,0 "$50\,\Omega$"
wire 6,3 -> 9,3
I2 9,3 -> 9,0 "$i_{dc}$"
wire 0,0 -> 3,0
R5 3,0 -> 6,0 "$40\,\Omega$"
wire 6,0 -> 9,0
label 3,3 "$p$" above
label 6,3 "$q$" below
label 6,0 "$m$" below
ground 0,0
#@ spoiler
#@ straight off
#@ node s 420 "battery top: $420\,\mathrm{V}$"
#@ node p 300 "$p$: $300\,\mathrm{V}$"
#@ node m 66.67 "$m$: $66.67\,\mathrm{V}$"
#@ node q 50 "$q$: $50\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$420\,\mathrm{V}$" col=0 i="$16.67\,\mathrm{A}$" to=s id=eV1
#@ el R s p "$7.2\,\Omega$: falls $120\,\mathrm{V}$" col=1 i="$16.67\,\mathrm{A}$" to=p id=eR1
#@ el R p g2 "$20\,\Omega$: falls $300\,\mathrm{V}$" col=1 i="$15\,\mathrm{A}$" to=g2 id=eR2
#@ el I q p "$15\,\mathrm{A}$" col=2 i="$15\,\mathrm{A}$" to=p id=eI1
#@ el R p q "$15\,\Omega$: falls $250\,\mathrm{V}$" col=3 i="$16.67\,\mathrm{A}$" to=q id=eR3
#@ el I q m "$2\,\mathrm{A}$" col=4 i="$2\,\mathrm{A}$" to=m id=eI2
#@ el R q m "$50\,\Omega$: falls $16.67\,\mathrm{V}$" col=5 i="$0.3333\,\mathrm{A}$" to=q id=eR4
#@ el R g3 m "$40\,\Omega$" col=6 i="$1.667\,\mathrm{A}$" to=g3 id=eR5
#@ step "Ground the bottom wire. The battery lifts its top to $420\,\mathrm{V}$."
#@ step "The key fact: the $15\,\mathrm{A}$ pump lifts its current from $q$ up to $p$. Developing $3750\,\mathrm{W}$ means it lifts $15\,\mathrm{A}$ by $250\,\mathrm{V}$: $p-q=250\,\mathrm{V}$." show=eI1
#@ step "In = out at $p$: $\dfrac{420-p}{7.2}+15=\dfrac{p}{20}+\dfrac{250}{15}$, so $p=300$ and $q=50\,\mathrm{V}$." show=p,q,eR1,eR2,eR3,eV1
#@ step "In = out at $q$ and $m$: $m=66.67\,\mathrm{V}$ and $i_{dc}=2\,\mathrm{A}$. ($m$ is above $q$: $0.33\,\mathrm{A}$ slides back from $m$ to $q$, and the $i_{dc}$ pump lifts $2\,\mathrm{A}$ from $q$ to $m$.)" show=m,eR4,eR5,eI2
```

<details><summary>Solution</summary>

1. (a) Node voltages: the given power is a statement about the height difference across the pump.

   $$15\,(v_p-v_q)=3750\;\Rightarrow\;v_p-v_q=250\,\mathrm{V}$$
2. In = out at $p$.

   $$\frac{420-v_p}{7.2}+15=\frac{v_p}{20}+\frac{250}{15}\;\Rightarrow\;v_p=300,\;v_q=50\,\mathrm{V}$$
3. In = out at $q$ and $m$.

   $$\begin{aligned}\tfrac{250}{15}&=15+\tfrac{50-v_m}{50}+i_{dc}\\\tfrac{50-v_m}{50}+i_{dc}&=\tfrac{v_m}{40}\end{aligned}\;\Rightarrow\;v_m=66.67\,\mathrm{V},\;i_{dc}=2\,\mathrm{A}$$

**Answer:** **(a)** Node voltages. **(b)** $i_{dc}=2\,\mathrm{A}$.

</details>

**Problem: Textbook P4.73 · A voltmeter is a load** (intermediate)

A $100\,\mathrm{k\Omega}$ voltmeter measures $v_{ab}$. **(a)** What does it read? **(b)** What is the percentage error, $\dfrac{\text{measured}-\text{actual}}{\text{actual}}\times100$?

```schematic
R1 0,6 -> 0,3 "$10\,\mathrm{k\Omega}$"
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
wire 0,6 -> 3,6
R2 3,6 -> 3,0 "$40\,\mathrm{k\Omega}$"
R3 3,6 -> 6,6 "$4\,\mathrm{k\Omega}$"
I1 6,0 -> 6,6 "$8\,\mathrm{mA}$"
R4 6,6 -> 9,6 "$3\,\mathrm{k\Omega}$"
R5 9,6 -> 9,0 "$10\,\mathrm{k\Omega}$"
wire 9,6 -> 11,6
terminal 11,6 "$a$" right
terminal 11,0 "$b$" right
wire 0,0 -> 11,0
label 3,6 "$p$" above
label 6,6 "$q$" above
ground 0,0
#@ spoiler
#@ view "No meter (actual)"
#@ straight off
#@ node q 62.4 "$q$: $62.4\,\mathrm{V}$"
#@ node p 49.6 "$p$: $49.6\,\mathrm{V}$"
#@ node a 48 "$a$: $48\,\mathrm{V}$" terminal
#@ node s 30 "30 V top: $30\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g4 0 "$b$: $0\,\mathrm{V}$" ground
#@ el I g q "$8\,\mathrm{mA}$" col=0 i="$8\,\mathrm{mA}$" to=q id=eI1
#@ el R p q "$4\,\mathrm{k\Omega}$: falls $12.8\,\mathrm{V}$" col=1 i="$3.2\,\mathrm{mA}$" to=p id=eR3
#@ el R p s "$10\,\mathrm{k\Omega}$: falls $19.6\,\mathrm{V}$" col=1 i="$1.96\,\mathrm{mA}$" to=s id=eR1
#@ el V s g2 "$30\,\mathrm{V}$" col=1 i="$1.96\,\mathrm{mA}$" to=g2 id=eV1
#@ el R p g3 "$40\,\mathrm{k\Omega}$: falls $49.6\,\mathrm{V}$" col=2 i="$1.24\,\mathrm{mA}$" to=g3 id=eR2
#@ el R q a "$3\,\mathrm{k\Omega}$: falls $14.4\,\mathrm{V}$" col=3 i="$4.8\,\mathrm{mA}$" to=a id=eR4
#@ el R a g4 "$10\,\mathrm{k\Omega}$: falls $48\,\mathrm{V}$" col=3 i="$4.8\,\mathrm{mA}$" to=g4 id=eR5
#@ step "Ground $b$. The source fixes its top at $30\,\mathrm{V}$."
#@ step "Unknowns $p$ and $q$ ($a$ is a divider below $q$). KCL (mA, kΩ): $p=49.6$, $q=62.4\,\mathrm{V}$, so $a=\tfrac{10}{13}(62.4)=48\,\mathrm{V}=V_{\mathrm{Th}}$." show=p,q,a
#@ step "The pump lifts $8\,\mathrm{mA}$ to $62.4\,\mathrm{V}$. $1.96\,\mathrm{mA}$ falls back **into** the $30\,\mathrm{V}$ source." show=eR1,eR2,eR3,eR4,eR5,eV1
#@ view "100 kΩ meter attached"
#@ straight off
#@ node q 60.23 "$q$: $60.23\,\mathrm{V}$"
#@ node p 48.15 "$p$: $48.15\,\mathrm{V}$"
#@ node a 45.28 "$a$: $45.28\,\mathrm{V}$" terminal
#@ node s 30 "30 V top: $30\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g4 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g5 0 "$b$: $0\,\mathrm{V}$" ground
#@ el I g q "$8\,\mathrm{mA}$" col=0 i="$8\,\mathrm{mA}$" to=q id=eI1
#@ el R p q "$4\,\mathrm{k\Omega}$: falls $12.08\,\mathrm{V}$" col=1 i="$3.019\,\mathrm{mA}$" to=p id=eR3
#@ el R p s "$10\,\mathrm{k\Omega}$: falls $18.15\,\mathrm{V}$" col=1 i="$1.815\,\mathrm{mA}$" to=s id=eR1
#@ el V s g2 "$30\,\mathrm{V}$" col=1 i="$1.815\,\mathrm{mA}$" to=g2 id=eV1
#@ el R p g3 "$40\,\mathrm{k\Omega}$: falls $48.15\,\mathrm{V}$" col=2 i="$1.204\,\mathrm{mA}$" to=g3 id=eR2
#@ el R q a "$3\,\mathrm{k\Omega}$: falls $14.94\,\mathrm{V}$" col=3 i="$4.981\,\mathrm{mA}$" to=a id=eR4
#@ el R a g4 "$10\,\mathrm{k\Omega}$: falls $45.28\,\mathrm{V}$" col=3 i="$4.528\,\mathrm{mA}$" to=g4 id=eR5
#@ el R a g5 "meter: falls $45.28\,\mathrm{V}$" col=4 i="$0.4528\,\mathrm{mA}$" to=g5 id=eRM
#@ step "Same ground. Sources off: $10\parallel40=8$, $+4=12$, $+3=15$, $\parallel10$: $R_{\mathrm{Th}}=6\,\mathrm{k\Omega}$."
#@ step "The meter draws $\dfrac{48}{6+100}=0.453\,\mathrm{mA}$, so $a$ sags $(6)(0.453)=2.72\,\mathrm{V}$: it reads $45.28\,\mathrm{V}$." show=a,eRM
#@ step "Error: $\dfrac{45.28-48}{48}=-5.66\%$." show=p,q,eR1,eR2,eR3,eR4,eR5,eV1
```

<details><summary>Solution</summary>

1. Thévenin at $a$–$b$ (node equations, then sources off).

   $$V_{\mathrm{Th}}=48\,\mathrm{V},\qquad R_{\mathrm{Th}}=\big((10\parallel40)+4+3\big)\parallel10=6\,\mathrm{k\Omega}$$
2. The meter is a load.

   $$v_m=48\cdot\frac{100}{106}=45.28\,\mathrm{V}$$
3. Error.

   $$\frac{45.28-48}{48}\times100=-5.66\%$$

**Answer:** **(a)** $45.28\,\mathrm{V}$ **(b)** $-5.66\%$

</details>

**Problem: Textbook P4.70 · A bridge just off balance** (advanced)

The bridge is balanced when $R_3=1200\,\Omega$. With $R_3=1204\,\Omega$, how much current does the $30\,\Omega$ galvanometer detect? (Hint: find the Thévenin equivalent across the galvanometer.)

```schematic
V1 0,4 -> 0,0 "$120\,\mathrm{V}$"
wire 0,4 -> 9,4
R1 3,4 -> 3,2 "$900\,\Omega$"
R2 3,2 -> 3,0 "$600\,\Omega$"
R3 9,4 -> 9,2 "$1204\,\Omega$"
R4 9,2 -> 9,0 "$R_x=800\,\Omega$"
RG 3,2 -> 9,2 "galvanometer $30\,\Omega$"
wire 0,0 -> 9,0
label 3,2 "$l$" left
label 9,2 "$r$" right
ground 0,0
#@ spoiler
#@ view "Galvanometer removed"
#@ straight off
#@ node s 120 "battery top: $120\,\mathrm{V}$"
#@ node l 48 "$l$: $48\,\mathrm{V}$"
#@ node r 47.9042 "$r$: $47.9042\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$120\,\mathrm{V}$" col=0 i="$139.9\,\mathrm{mA}$" to=s id=eV1
#@ el R s l "$900\,\Omega$: falls $72\,\mathrm{V}$" col=1 i="$80\,\mathrm{mA}$" to=l id=eR1
#@ el R l g2 "$600\,\Omega$: falls $48\,\mathrm{V}$" col=1 i="$80\,\mathrm{mA}$" to=g2 id=eR2
#@ el R s r "$1.204\,\mathrm{k\Omega}$: falls $72.0958\,\mathrm{V}$" col=2 i="$59.88\,\mathrm{mA}$" to=r id=eR3
#@ el R r g3 "$800\,\Omega$: falls $47.9042\,\mathrm{V}$" col=2 i="$59.88\,\mathrm{mA}$" to=g3 id=eR4
#@ step "Ground the bottom wire. The battery lifts the top to $120\,\mathrm{V}$."
#@ step "With the galvanometer removed, each side is a divider: $l=120\cdot\tfrac{600}{1500}=48\,\mathrm{V}$, $r=120\cdot\tfrac{800}{2004}=47.904\,\mathrm{V}$. The midpoints are only $95.8\,\mathrm{mV}$ apart: $V_{\mathrm{Th}}=95.8\,\mathrm{mV}$." show=l,r
#@ step "Battery flattened: $R_{\mathrm{Th}}=(900\parallel600)+(1204\parallel800)=360+480.6=840.6\,\Omega$."
#@ view "Galvanometer attached"
#@ straight off
#@ node s 120 "battery top: $120\,\mathrm{V}$"
#@ node l 47.9604 "$l$: $47.9604\,\mathrm{V}$"
#@ node r 47.9571 "$r$: $47.9571\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$120\,\mathrm{V}$" col=0 i="$139.9\,\mathrm{mA}$" to=s id=eV1
#@ el R s l "$900\,\Omega$: falls $72.0396\,\mathrm{V}$" col=1 i="$80.04\,\mathrm{mA}$" to=l id=eR1
#@ el R l g2 "$600\,\Omega$: falls $47.9604\,\mathrm{V}$" col=1 i="$79.93\,\mathrm{mA}$" to=g2 id=eR2
#@ el R l r "galvanometer" col=2 i="$0.11\,\mathrm{mA}$" to=r id=eRG
#@ el R s r "$1.204\,\mathrm{k\Omega}$: falls $72.0429\,\mathrm{V}$" col=3 i="$59.84\,\mathrm{mA}$" to=r id=eR3
#@ el R r g3 "$800\,\Omega$: falls $47.9571\,\mathrm{V}$" col=3 i="$59.95\,\mathrm{mA}$" to=g3 id=eR4
#@ step "Same ground. The galvanometer is a load on the Thévenin source: $i=\dfrac{0.0958}{840.6+30}=0.110\,\mathrm{mA}$, from $l$ (higher) to $r$." show=eRG
#@ note "Levels this close are spread apart so they stay readable: the real gap is a few millivolts."
```

<details><summary>Solution</summary>

1. Thévenin across the galvanometer: two dividers.

   $$V_{\mathrm{Th}}=120\Big(\frac{600}{1500}-\frac{800}{2004}\Big)=95.8\,\mathrm{mV}$$
2. Battery flattened.

   $$R_{\mathrm{Th}}=900\parallel600+1204\parallel800=840.6\,\Omega$$
3. The galvanometer is the load.

   $$i=\frac{0.0958}{840.6+30}=110\,\mu\mathrm{A}$$

**Answer:** About $110\,\mu\mathrm{A}$, from $l$ to $r$.

</details>

## Cheat sheet

| Idea | In heights | Write |
|---|---|---|
| Node or mesh | count unknown heights vs windows | node: $(n_e-1)-$fixed; mesh: $(b_e-n_e+1)-$fixed |
| Source swap | same terminal height, different inside | $i_s=\dfrac{v_s}{R}$, $v_s=Ri_s$, arrow toward $+$ |
| Thévenin voltage | open height of $a$ | $V_{\mathrm{Th}}=v_{oc}$ |
| Norton current | current when $a$ is wired to $b$ | $I_N=i_{sc}=\dfrac{V_{\mathrm{Th}}}{R_{\mathrm{Th}}}$ |
| Thévenin resistance | height of $a$ per amp pushed in (sources off) | $R_{\mathrm{Th}}=\dfrac{v_{oc}}{i_{sc}}$ |
| Loaded terminal | the sag | $v_{ab}=V_{\mathrm{Th}}-R_{\mathrm{Th}}i=V_{\mathrm{Th}}\dfrac{R_L}{R_{\mathrm{Th}}+R_L}$ |
| Sources off | battery → wire, pump → gap | dependent sources stay on |
