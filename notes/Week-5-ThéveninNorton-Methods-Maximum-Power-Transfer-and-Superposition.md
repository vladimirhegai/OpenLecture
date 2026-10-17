# Week 5: Thévenin/Norton Methods, Maximum Power Transfer and Superposition

> **Info:** **Week 5 in one line:** finish Thévenin (diamonds inside), then use it twice: **maximum power** (the best load sits at half the open height) and **superposition** (one source at a time, then add the heights).

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
> **New this week:** a diamond **never** turns off, and when you split a circuit into one-source pictures, **heights add but powers don't**.

**Example: Example 0 · Open, short, sources off**

Find $V_{\mathrm{Th}}$, $I_N$ and $R_{\mathrm{Th}}$ at $a$–$b$.

```schematic
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
R2 3,3 -> 3,0 "$12\,\Omega$"
wire 3,3 -> 6,3
wire 3,0 -> 6,0
terminal 6,3 "$a$" right
terminal 6,0 "$b$" right
wire 0,0 -> 3,0
ground 0,0
#@ inline
#@ view "Open"
#@ straight off
#@ node s 24 "source top: $24\,\mathrm{V}$"
#@ node a 18 "$a$: $18\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$24\,\mathrm{V}$" col=0 i="$1.5\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$4\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$1.5\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$12\,\Omega$: falls $18\,\mathrm{V}$" col=1 i="$1.5\,\mathrm{A}$" to=g2 id=eR2
#@ step "Ground $b$. The source steps up $24\,\mathrm{V}$."
#@ step "Divider: $\dfrac{24}{16}=1.5\,\mathrm{A}$; the $4\,\Omega$ falls $6\,\mathrm{V}$, so $a=18\,\mathrm{V}=V_{\mathrm{Th}}$." show=a,eR1,eR2,eV1
#@ view "Short"
#@ straight off
#@ node s 24 "source top: $24\,\mathrm{V}$"
#@ node a 0 "$a$ = $b$: $0\,\mathrm{V}$"
#@ node g 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ el V s g "$24\,\mathrm{V}$" col=0 i="$6\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$4\,\Omega$: falls $24\,\mathrm{V}$" col=1 i="$6\,\mathrm{A}$" to=a id=eR1
#@ el W a g2 "short: no step" col=1 i="$6\,\mathrm{A}$" to=g2 id=eSC
#@ step "Same ground. A wire pins $a$ to $b$. The $4\,\Omega$ falls all $24\,\mathrm{V}$: $I_N=6\,\mathrm{A}$, so $R_{\mathrm{Th}}=\dfrac{18}{6}=3\,\Omega$." show=a,eR1,eSC,eV1
#@ note "The $12\,\Omega$ sits across the short (no fall, no current), so it is left out of this tab."
#@ view "Sources off, push 1 A"
#@ straight off
#@ node a 3 "$a$: $3\,\mathrm{V}$" terminal
#@ node s 0 "source top = $b$: $0\,\mathrm{V}$"
#@ node g 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ el W s g "$24\,\mathrm{V}$ off: a wire" col=0 i="$0.75\,\mathrm{A}$" to=g id=eV1
#@ el R s a "$4\,\Omega$: falls $3\,\mathrm{V}$" col=1 i="$0.75\,\mathrm{A}$" to=s id=eR1
#@ el R a g2 "$12\,\Omega$: falls $3\,\mathrm{V}$" col=2 i="$0.25\,\mathrm{A}$" to=g2 id=eR2
#@ el I g3 a "test $1\,\mathrm{A}$" col=3 i="$1\,\mathrm{A}$" to=a id=eIT
#@ step "Same ground. Flatten the $24\,\mathrm{V}$. $1\,\mathrm{A}$ into $4\parallel12=3\,\Omega$: $a=3\,\mathrm{V}$, so $R_{\mathrm{Th}}=3\,\Omega$ ✓." show=a,eR1,eR2,eIT
```

1. Three numbers, one check.

   $$V_{\mathrm{Th}}=24\cdot\tfrac{12}{16}=18\,\mathrm{V},\quad I_N=\tfrac{24}{4}=6\,\mathrm{A},\quad R_{\mathrm{Th}}=4\parallel12=3\,\Omega=\tfrac{18}{6}$$

**Answer:** $V_{\mathrm{Th}}=18\,\mathrm{V}$, $I_N=6\,\mathrm{A}$, $R_{\mathrm{Th}}=3\,\Omega$.

> **Info:** **Signs.** $V_{\mathrm{Th}}<0$ means $a$ sits **below** $b$ when nothing is attached; then $I_N<0$ too (it flows $b\to a$) and $R_{\mathrm{Th}}=\dfrac{V_{\mathrm{Th}}}{I_N}$ stays positive.

## Topic 1: Thévenin with diamonds inside

> **Tip:** **How it looks in heights.**
> 
> - A diamond **never turns off**: keep it in every picture, with what it depends on.
> - **Push $1\,\mathrm{A}$ into $a$** (independent sources off): $a$'s height is $R_{\mathrm{Th}}$. If $a$ goes **up** when you pull current out, $R_{\mathrm{Th}}$ is negative: the diamond is giving energy.
> - No independent source at all: nothing lifts $a$, so $V_{\mathrm{Th}}=0$ and only the push finds $R_{\mathrm{Th}}$.
> - One shot: keep everything on and push $i_T$: then $a=V_{\mathrm{Th}}+R_{\mathrm{Th}}\,i_T$ (start height + slope).

$$R_{\mathrm{Th}}=\frac{v_T}{i_T}\;(\text{independent sources off}),\qquad v_T=V_{\mathrm{Th}}+R_{\mathrm{Th}}\,i_T\;(\text{all on})$$

**Example: Example 1 · A diamond lowers the climb**

Find $R_{\mathrm{Th}}$ at $a$–$b$. The diamond draws $\tfrac{v}{3}$ from $a$ to $b$.

```schematic
R1 0,3 -> 0,0 "$6\,\Omega$" v="$v$"
wire 0,3 -> 3,3
G1 3,3 -> 3,0 "$\tfrac{v}{3}$"
wire 0,0 -> 3,0
wire 3,3 -> 5,3
wire 3,0 -> 5,0
terminal 5,3 "$a$" right
terminal 5,0 "$b$" right
ground 0,0
#@ inline
#@ view "Push 1 A"
#@ straight off
#@ node a 2 "$a$: $2\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el I g a "test $1\,\mathrm{A}$" col=0 i="$1\,\mathrm{A}$" to=a id=eIT
#@ el R a g2 "$6\,\Omega$: falls $2\,\mathrm{V}$" col=1 i="$0.3333\,\mathrm{A}$" to=g2 id=eR1 plus=a v="$v$"
#@ el G a g3 "$\tfrac{v}{3}$: $0.6667\,\mathrm{A}$" col=2 i="$0.6667\,\mathrm{A}$" to=g3 id=eG1
#@ step "Ground $b$, push $1\,\mathrm{A}$ in. KCL: $1=\dfrac{a}{6}+\dfrac{a}{3}=\dfrac{a}{2}$, so $a=2\,\mathrm{V}$: $R_{\mathrm{Th}}=2\,\Omega$, not $6$." show=a,eR1,eG1
```

1. Test current.

   $$1=\frac{v}{6}+\frac{v}{3}\;\Rightarrow\;v=2\,\mathrm{V},\quad R_{\mathrm{Th}}=2\,\Omega$$

**Answer:** $R_{\mathrm{Th}}=2\,\Omega$

**Example: Example 2 · Pull current out, and a rises (Lecture 5)**

The network has only a dependent source. Find $V_{\mathrm{Th}}$ and $R_{\mathrm{Th}}$.

```schematic
E1 0,3 -> 0,0 "$12i_\Delta$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$" i="$i_\Delta$"
wire 3,3 -> 6,3
wire 3,0 -> 6,0
terminal 6,3 "$a$" right
terminal 6,0 "$b$" right
wire 0,0 -> 3,0
label 0,3 "$s$" left
ground 0,0
#@ inline
#@ view "Pull 1 A out of a"
#@ straight off
#@ node s 4 "$s$: $4\,\mathrm{V}$"
#@ node a 1.33 "$a$: $1.33\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el E s g "$12i_\Delta$: $4\,\mathrm{V}$" col=0 i="$1.333\,\mathrm{A}$" to=s id=eE1
#@ el R s a "$2\,\Omega$: falls $2.67\,\mathrm{V}$" col=1 i="$1.333\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$4\,\Omega$: falls $1.33\,\mathrm{V}$" col=1 i="$0.3333\,\mathrm{A}$" to=g2 id=eR2
#@ el I a g3 "test: pulls $1\,\mathrm{A}$ out" col=2 i="$1\,\mathrm{A}$" to=g3 id=eIT
#@ step "Ground $b$. No independent source: with nothing attached every height is $0$, so $V_{\mathrm{Th}}=0$ and $I_N=0$. Only a test source can find $R_{\mathrm{Th}}$."
#@ step "Pull $1\,\mathrm{A}$ out of $a$. Control: $i_\Delta=\dfrac{a}{4}$, so the diamond's step is $12i_\Delta=3a$." show=eIT
#@ step "KCL at $a$: in from the $2\,\Omega$, $\dfrac{3a-a}{2}=a$; out, $\dfrac{a}{4}+1$. So $a=\tfrac43\,\mathrm{V}$ and $s=4\,\mathrm{V}$." show=a,s
#@ step "A normal circuit sags when you pull current out. Here $a$ **rises**: $R_{\mathrm{Th}}=\dfrac{4/3}{-1}=-\tfrac43\,\Omega$. The diamond climbs $1.33\,\mathrm{A}$ through $4\,\mathrm{V}$: it delivers $5.33\,\mathrm{W}$." show=eE1,eR1,eR2
#@ note "A negative $R_{\mathrm{Th}}$ is a source that pushes back, not a resistor."
```

1. No independent source.

   $$V_{\mathrm{Th}}=0,\qquad I_N=0$$
2. Test current $i_T$ into $a$, control $i_\Delta=\dfrac{v_T}{4}$; KCL at $a$.

   $$i_T+\frac{12i_\Delta-v_T}{2}=i_\Delta\;\Rightarrow\;i_T=-\tfrac34v_T$$
3. Ratio.

   $$R_{\mathrm{Th}}=\frac{v_T}{i_T}=-\tfrac43\,\Omega$$

**Answer:** $V_{\mathrm{Th}}=0$, $R_{\mathrm{Th}}=-\tfrac43\,\Omega$.

**Example: Example 3 · One shot: the test source as a variable (Lecture 5)**

Keep every source on and push a test current $i_T$ into $a$. Find $v_T$ as a function of $i_T$, then read off $V_{\mathrm{Th}}$, $R_{\mathrm{Th}}$ and $I_N$.

```schematic
V1 0,3 -> 0,0 "$5\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\mathrm{k\Omega}$" i="$i$"
E1 3,3 -> 3,0 "$3v$"
G1 6,3 -> 6,0 "$20i$"
wire 6,3 -> 8,3
R2 8,3 -> 8,0 "$25\,\Omega$" v="$v$"
wire 8,3 -> 10,3
terminal 10,3 "$a$" right
terminal 10,0 "$b$" right
wire 0,0 -> 10,0
label 3,3 "$m$" above
ground 0,0
#@ inline
#@ view "Open (no test current)"
#@ straight off
#@ node s 20 "5 V top: $20\,\mathrm{V}$"
#@ node z0 15 "$b$: $15\,\mathrm{V}$"
#@ node a 10 "$a$: $10\,\mathrm{V}$" terminal
#@ node g 0 "$m$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$m$: $0\,\mathrm{V}$" ground
#@ el R s g "$2\,\mathrm{k\Omega}$: falls $20\,\mathrm{V}$" col=0 i="$10\,\mathrm{mA}$" to=g id=eR1
#@ el V s z0 "$5\,\mathrm{V}$" col=1 i="$10\,\mathrm{mA}$" to=s id=eV1
#@ el E g2 z0 "$3v$: $-15\,\mathrm{V}$" col=2 i="$10\,\mathrm{mA}$" to=z0 id=eE1
#@ el G a z0 "$20i$: $200\,\mathrm{mA}$" col=3 i="$200\,\mathrm{mA}$" to=z0 id=eG1
#@ el R a z0 "$25\,\Omega$: falls $5\,\mathrm{V}$" col=4 i="$200\,\mathrm{mA}$" to=a id=eR2 plus=a v="$v$"
#@ step "Ground $m$, the lowest node. Every answer is a height **above $b$** (the bottom wire)."
#@ step "All sources on, test current $i_T$ in. KCL at $a$: $i_T=\dfrac{v}{25}+20i$. Left loop: $5=2000i+3v$. With $v=v_T$: $v_T=100\,i_T-5$."
#@ step "With $i_T=0$, $a$ sits $5\,\mathrm{V}$ **below** $b$: $V_{\mathrm{Th}}=-5\,\mathrm{V}$. The diamond pump lifts $200\,\mathrm{mA}$ from $a$ up to $b$." show=a,eG1,eR2
#@ view "Push 0.1 A into a"
#@ straight off
#@ node m 15 "$m$: $15\,\mathrm{V}$"
#@ node a 5 "$a$ = 5 V top: $5\,\mathrm{V}$" terminal
#@ node s 5 "$a$ = 5 V top: $5\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g4 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g5 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$5\,\mathrm{V}$" col=0 i="$5\,\mathrm{mA}$" to=g id=eV1
#@ el R s m "$2\,\mathrm{k\Omega}$: falls $10\,\mathrm{V}$" col=1 i="$5\,\mathrm{mA}$" to=s id=eR1
#@ el E m g2 "$3v$: $15\,\mathrm{V}$" col=2 i="$5\,\mathrm{mA}$" to=m id=eE1
#@ el G a g3 "$20i$: $100\,\mathrm{mA}$" col=3 i="$100\,\mathrm{mA}$" to=a id=eG1
#@ el R a g4 "$25\,\Omega$: falls $5\,\mathrm{V}$" col=4 i="$200\,\mathrm{mA}$" to=g4 id=eR2 plus=a v="$v$"
#@ el I g5 a "test $100\,\mathrm{mA}$" col=5 i="$100\,\mathrm{mA}$" to=a id=eIT
#@ step "Ground $b$ (now the lowest node). Push $0.1\,\mathrm{A}$ into $a$."
#@ step "$a$ rises to $100(0.1)-5=5\,\mathrm{V}$: $10\,\mathrm{V}$ higher for $0.1\,\mathrm{A}$, so $R_{\mathrm{Th}}=100\,\Omega$. And $I_N=\dfrac{-5}{100}=-50\,\mathrm{mA}$." show=a,eIT,eR2,eG1
```

1. KCL at $a$ ($v=v_T$).

   $$v_T=25\,(i_T-20i)$$
2. Left loop.

   $$5=2000\,i+3v_T\;\Rightarrow\;i=\frac{5-3v_T}{2000}$$
3. Substitute.

   $$v_T=25\,i_T-1.25+0.75\,v_T\;\Rightarrow\;v_T=100\,i_T-5$$
4. Read off.

   $$V_{\mathrm{Th}}=-5\,\mathrm{V},\quad R_{\mathrm{Th}}=100\,\Omega,\quad I_N=\frac{-5}{100}=-50\,\mathrm{mA}$$

**Answer:** $v_T=100\,i_T-5$: $V_{\mathrm{Th}}=-5\,\mathrm{V}$, $R_{\mathrm{Th}}=100\,\Omega$, $I_N=-50\,\mathrm{mA}$.

**Problem: Try it 1 · A diamond that feeds back (Assessment AP 4.19)** (intermediate)

Find the Thévenin equivalent at $a$–$b$. **(a)** $V_{\mathrm{Th}}$ **(b)** $R_{\mathrm{Th}}$ with a test source **(c)** check with $I_N$.

```schematic
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
wire 0,3 -> 0,6
G1 3,6 -> 0,6 "$3i_x$"
wire 3,6 -> 3,3
wire 3,3 -> 5,3
I1 5,3 -> 5,0 "$4\,\mathrm{A}$"
wire 5,3 -> 7,3
R2 7,3 -> 7,0 "$8\,\Omega$" i="$i_x$"
wire 7,3 -> 9,3
terminal 9,3 "$a$" right
terminal 9,0 "$b$" right
wire 0,0 -> 9,0
ground 0,0
#@ spoiler
#@ view "Open"
#@ straight off
#@ node s 24 "source top: $24\,\mathrm{V}$"
#@ node a 8 "$a$: $8\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$24\,\mathrm{V}$" col=0 i="$5\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$2\,\Omega$: falls $16\,\mathrm{V}$" col=1 i="$8\,\mathrm{A}$" to=a id=eR1
#@ el G a s "$3i_x$: $3\,\mathrm{A}$" col=2 i="$3\,\mathrm{A}$" to=s id=eG1
#@ el I a g2 "$4\,\mathrm{A}$" col=3 i="$4\,\mathrm{A}$" to=g2 id=eI1
#@ el R a g3 "$8\,\Omega$: falls $8\,\mathrm{V}$" col=4 i="$1\,\mathrm{A}$" to=g3 id=eR2
#@ step "Ground $b$. The source fixes its top at $24\,\mathrm{V}$."
#@ step "Control: $i_x=\dfrac{a}{8}$. KCL at $a$: $\dfrac{a-24}{2}+\dfrac{3a}{8}+4+\dfrac{a}{8}=0$, so $a=8\,\mathrm{V}=V_{\mathrm{Th}}$." show=a
#@ step "$8\,\mathrm{A}$ falls into $a$; the diamond lifts $3\,\mathrm{A}$ back up (delivers), the $4\,\mathrm{A}$ pump carries its current **down** (absorbs), $1\,\mathrm{A}$ goes down the $8\,\Omega$." show=eR1,eG1,eI1,eR2,eV1
#@ view "Sources off, push 1 A"
#@ straight off
#@ node a 1 "$a$: $1\,\mathrm{V}$" terminal
#@ node s 0 "source top = $b$: $0\,\mathrm{V}$"
#@ node g 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ node g4 0 "source top = $b$: $0\,\mathrm{V}$" ground
#@ el W s g "$24\,\mathrm{V}$ off: a wire" col=0 i="$0.875\,\mathrm{A}$" to=g id=eV1
#@ el R s a "$2\,\Omega$: falls $1\,\mathrm{V}$" col=1 i="$0.5\,\mathrm{A}$" to=s id=eR1
#@ el G a s "$3i_x$: $0.375\,\mathrm{A}$" col=2 i="$0.375\,\mathrm{A}$" to=s id=eG1
#@ el S a g2 "$4\,\mathrm{A}$ off: a gap" col=3 id=eI1
#@ el R a g3 "$8\,\Omega$: falls $1\,\mathrm{V}$" col=4 i="$0.125\,\mathrm{A}$" to=g3 id=eR2
#@ el I g4 a "test $1\,\mathrm{A}$" col=5 i="$1\,\mathrm{A}$" to=a id=eIT
#@ step "Same ground. $24\,\mathrm{V}$ → wire, $4\,\mathrm{A}$ → gap. The diamond **stays on**."
#@ step "Push $1\,\mathrm{A}$ into $a$: $1=\dfrac{a}{2}+\dfrac{3a}{8}+\dfrac{a}{8}=a$. So $a=1\,\mathrm{V}$: $R_{\mathrm{Th}}=1\,\Omega$." show=a,eR1,eG1,eR2,eIT,eV1
#@ step "Check with a short: $a=b$ makes $i_x=0$ (diamond off), so $I_N=\dfrac{24}{2}-4=8\,\mathrm{A}$ and $\dfrac{8}{8}=1\,\Omega$ ✓."
```

<details><summary>Solution</summary>

1. Open, KCL at $a$ with $i_x=\dfrac{v_a}{8}$.

   $$\frac{v_a-24}{2}+\frac{3v_a}{8}+4+\frac{v_a}{8}=0\;\Rightarrow\;V_{\mathrm{Th}}=8\,\mathrm{V}$$
2. Test source, independent sources off.

   $$i_T=\frac{v_T}{2}+\frac{3v_T}{8}+\frac{v_T}{8}=v_T\;\Rightarrow\;R_{\mathrm{Th}}=1\,\Omega$$
3. Check.

   $$i_{sc}=\tfrac{24}{2}-4=8\,\mathrm{A},\qquad \tfrac{8}{8}=1\,\Omega$$

**Answer:** **(a)** $8\,\mathrm{V}$ **(b)** $1\,\Omega$ **(c)** $I_N=8\,\mathrm{A}$ ✓

</details>

**Problem: Try it 2 · No independent source (Textbook P4.80)** (intermediate)

Find the Thévenin equivalent at $a$–$b$. The dependent source is controlled by $i_\Delta$ in the $12\,\Omega$.

```schematic
E1 0,4 -> 0,0 "$10i_\Delta$"
wire 0,4 -> 0,7
R1 0,7 -> 8,7 "$6\,\Omega$"
wire 8,7 -> 8,4
R2 0,4 -> 4,4 "$10\,\Omega$"
R3 8,4 -> 4,4 "$12\,\Omega$" i="$i_\Delta$"
R4 4,4 -> 4,0 "$2.5\,\Omega$"
wire 8,4 -> 11,4
terminal 11,4 "$a$" right
terminal 11,0 "$b$" right
wire 0,0 -> 11,0
label 0,4 "$x$" left
label 4,4 "$m$" above
ground 0,0
#@ spoiler
#@ view "Push 1 A into a"
#@ straight off
#@ node a 8 "$a$: $8\,\mathrm{V}$" terminal
#@ node x 5 "$x$: $5\,\mathrm{V}$"
#@ node m 2 "$m$: $2\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el E x g "$10i_\Delta$: $5\,\mathrm{V}$" col=0 i="$0.2\,\mathrm{A}$" to=g id=eE1
#@ el R x a "$6\,\Omega$: falls $3\,\mathrm{V}$" col=1 i="$0.5\,\mathrm{A}$" to=x id=eR1
#@ el R x m "$10\,\Omega$: falls $3\,\mathrm{V}$" col=1 i="$0.3\,\mathrm{A}$" to=m id=eR2
#@ el R m g2 "$2.5\,\Omega$: falls $2\,\mathrm{V}$" col=1 i="$0.8\,\mathrm{A}$" to=g2 id=eR4
#@ el R a m "$12\,\Omega$: falls $6\,\mathrm{V}$" col=2 i="$0.5\,\mathrm{A}$" to=m id=eR3
#@ el I g3 a "test $1\,\mathrm{A}$" col=3 i="$1\,\mathrm{A}$" to=a id=eIT
#@ step "Ground $b$. No independent source, so with nothing attached every height is $0$: $V_{\mathrm{Th}}=0$."
#@ step "Push $1\,\mathrm{A}$ into $a$. Control: $i_\Delta=\dfrac{a-m}{12}$, and the diamond holds $x=10i_\Delta$." show=eIT
#@ step "KCL at $a$ and $m$: $a=8$, $m=2$, $x=5\,\mathrm{V}$ ($i_\Delta=0.5\,\mathrm{A}$)." show=a,m,x
#@ step "Currents = fall ÷ R; the diamond carries $0.2\,\mathrm{A}$ **down** (it absorbs here). $a$ sits at $8\,\mathrm{V}$ per amp: $R_{\mathrm{Th}}=8\,\Omega$." show=eE1,eR1,eR2,eR3,eR4
```

<details><summary>Solution</summary>

1. No independent source.

   $$V_{\mathrm{Th}}=0$$
2. Test voltage $v_T$ at $a$; $x=10i_\Delta$, $v_m=v_T-12i_\Delta$. KCL at $m$.

   $$i_\Delta+\frac{10i_\Delta-v_m}{10}=\frac{v_m}{2.5}\;\Rightarrow\;i_\Delta=\frac{v_T}{16}$$
3. Test current: through the $6\,\Omega$ and the $12\,\Omega$.

   $$i_T=\frac{v_T-10i_\Delta}{6}+i_\Delta=\frac{v_T}{8}\;\Rightarrow\;R_{\mathrm{Th}}=8\,\Omega$$

**Answer:** $V_{\mathrm{Th}}=0$, $R_{\mathrm{Th}}=8\,\Omega$: the terminals act like an $8\,\Omega$ resistor.

</details>

**Problem: Try it 3 · A diamond battery on the top wire (Textbook P4.74)** (intermediate)

Find the Thévenin equivalent at $a$–$b$.

```schematic
R1 0,3 -> 0,0 "$60\,\Omega$"
I1 3,0 -> 3,3 "$4\,\mathrm{A}$"
wire 0,3 -> 3,3
R2 3,3 -> 6,3 "$20\,\Omega$"
E1 6,3 -> 9,3 "$160i_\Delta$"
R3 9,3 -> 9,0 "$80\,\Omega$"
wire 9,3 -> 11,3
R4 11,3 -> 11,0 "$40\,\Omega$" i="$i_\Delta$"
wire 11,3 -> 13,3
terminal 13,3 "$a$" right
terminal 13,0 "$b$" right
wire 0,0 -> 13,0
label 3,3 "$n$" above
label 6,3 "$m$" above
ground 0,0
#@ spoiler
#@ view "Open"
#@ straight off
#@ node n 172.5 "$n$: $172.5\,\mathrm{V}$"
#@ node m 150 "$m$: $150\,\mathrm{V}$"
#@ node a 30 "$a$: $30\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g4 0 "$b$: $0\,\mathrm{V}$" ground
#@ el I g n "$4\,\mathrm{A}$" col=0 i="$4\,\mathrm{A}$" to=n id=eI1
#@ el R n g2 "$60\,\Omega$: falls $172.5\,\mathrm{V}$" col=1 i="$2.875\,\mathrm{A}$" to=g2 id=eR1
#@ el R n m "$20\,\Omega$: falls $22.5\,\mathrm{V}$" col=2 i="$1.125\,\mathrm{A}$" to=m id=eR2
#@ el E m a "$160i_\Delta$: $120\,\mathrm{V}$" col=2 i="$1.125\,\mathrm{A}$" to=a id=eE1
#@ el R a g3 "$80\,\Omega$: falls $30\,\mathrm{V}$" col=3 i="$0.375\,\mathrm{A}$" to=g3 id=eR3
#@ el R a g4 "$40\,\Omega$: falls $30\,\mathrm{V}$" col=4 i="$0.75\,\mathrm{A}$" to=g4 id=eR4
#@ step "Ground $b$. The $4\,\mathrm{A}$ pump pushes into $n$."
#@ step "The diamond is a battery of $160i_\Delta$ with $+$ at $m$, where $i_\Delta=\dfrac{a}{40}$ (the current down the $40\,\Omega$). So $m=a+4a=5a$."
#@ step "In = out at $n$: $4=\dfrac{n}{60}+\dfrac{n-m}{20}$. In = out for the bubble $\{m,a\}$: $\dfrac{n-m}{20}=\dfrac{a}{80}+\dfrac{a}{40}$. So $a=30\,\mathrm{V}=V_{\mathrm{Th}}$, $m=150$, $n=172.5\,\mathrm{V}$." show=a,m,n
#@ step "Currents: $2.875\,\mathrm{A}$ down the $60\,\Omega$; $1.125\,\mathrm{A}$ through the $20\,\Omega$ and **down** through the diamond (it absorbs); $0.375+0.75\,\mathrm{A}$ down the $80\,\Omega$ and $40\,\Omega$." show=eR1,eR2,eR3,eR4,eE1,eI1
#@ view "Sources off, push 1 A"
#@ straight off
#@ node m 50 "$m$: $50\,\mathrm{V}$"
#@ node n 37.5 "$n$: $37.5\,\mathrm{V}$"
#@ node a 10 "$a$: $10\,\mathrm{V}$" terminal
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g4 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g5 0 "$b$: $0\,\mathrm{V}$" ground
#@ el I g a "test $1\,\mathrm{A}$" col=0 i="$1\,\mathrm{A}$" to=a id=eIT
#@ el R a g2 "$80\,\Omega$: falls $10\,\mathrm{V}$" col=1 i="$0.125\,\mathrm{A}$" to=g2 id=eR3
#@ el R a g3 "$40\,\Omega$: falls $10\,\mathrm{V}$" col=2 i="$0.25\,\mathrm{A}$" to=g3 id=eR4
#@ el E m a "$160i_\Delta$: $40\,\mathrm{V}$" col=3 i="$0.625\,\mathrm{A}$" to=m id=eE1
#@ el R n m "$20\,\Omega$: falls $12.5\,\mathrm{V}$" col=4 i="$0.625\,\mathrm{A}$" to=n id=eR2
#@ el R n g4 "$60\,\Omega$: falls $37.5\,\mathrm{V}$" col=4 i="$0.625\,\mathrm{A}$" to=g4 id=eR1
#@ el S g5 n "$4\,\mathrm{A}$ off: a gap" col=5 id=eI1
#@ step "Same ground. The pump → gap. The diamond **stays on**."
#@ step "Push $1\,\mathrm{A}$ into $a$. Still $m=5a$. Paths from $a$: down the $80\,\Omega$ and $40\,\Omega$, or up through the diamond to $m$ and down $20+60\,\Omega$: $1=\dfrac{a}{80}+\dfrac{a}{40}+\dfrac{5a}{80}=\dfrac{a}{10}$."
#@ step "$a=10\,\mathrm{V}$ per amp: $R_{\mathrm{Th}}=10\,\Omega$. The diamond lifts $0.625\,\mathrm{A}$ from $a$ up to $m$ (it gives energy), which is why $a$ only climbs $10\,\mathrm{V}$." show=a,m,n,eR1,eR2,eR3,eR4,eE1,eIT
```

<details><summary>Solution</summary>

1. Control: $i_\Delta=\dfrac{v_a}{40}$, so the diamond gives $v_m=v_a+160i_\Delta=5v_a$.

   $$4=\frac{v_n}{60}+\frac{v_n-5v_a}{20},\qquad \frac{v_n-5v_a}{20}=\frac{v_a}{80}+\frac{v_a}{40}$$
2. Solve.

   $$v_a=V_{\mathrm{Th}}=30\,\mathrm{V},\qquad v_n=172.5\,\mathrm{V}$$
3. Test current, pump off.

   $$1=\frac{v_a}{80}+\frac{v_a}{40}+\frac{5v_a}{80}=\frac{v_a}{10}\;\Rightarrow\;R_{\mathrm{Th}}=10\,\Omega$$

**Answer:** $V_{\mathrm{Th}}=30\,\mathrm{V}$, $R_{\mathrm{Th}}=10\,\Omega$

</details>

**Problem: Try it 4 · Only a diamond inside (Textbook P4.81)** (intermediate)

Find the Thévenin equivalent at $a$–$b$.

```schematic
R1 0,3 -> 0,0 "$50\,\Omega$"
wire 0,3 -> 3,3
R2 3,3 -> 3,1.6 "$5\,\Omega$"
E1 3,0 -> 3,1.6 "$6.5i_x$"
R3 3,3 -> 6,3 "$10\,\Omega$"
R4 6,3 -> 6,0 "$25\,\Omega$" i="$i_x$"
R5 6,3 -> 9,3 "$12\,\Omega$"
terminal 9,3 "$a$" right
terminal 9,0 "$b$" right
wire 0,0 -> 9,0
label 3,3 "$t$" above
label 3,1.6 "$k$" right
label 6,3 "$m$" above
ground 0,0
#@ spoiler
#@ view "Push 1 A into a"
#@ straight off
#@ node a 22.08 "$a$: $22.08\,\mathrm{V}$" terminal
#@ node m 10.08 "$m$: $10.08\,\mathrm{V}$"
#@ node t 3.28 "$t$: $3.28\,\mathrm{V}$"
#@ node z0 2.08 "$b$: $2.08\,\mathrm{V}$"
#@ node g 0 "$k$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$k$: $0\,\mathrm{V}$" ground
#@ el E z0 g "$6.5i_x$: $2.08\,\mathrm{V}$" col=0 i="$0.656\,\mathrm{A}$" to=z0 id=eE1
#@ el R t g2 "$5\,\Omega$: falls $3.28\,\mathrm{V}$" col=0 i="$0.656\,\mathrm{A}$" to=g2 id=eR2
#@ el R t z0 "$50\,\Omega$: falls $1.2\,\mathrm{V}$" col=1 i="$0.024\,\mathrm{A}$" to=z0 id=eR1
#@ el R t m "$10\,\Omega$: falls $6.8\,\mathrm{V}$" col=2 i="$0.68\,\mathrm{A}$" to=t id=eR3
#@ el R m z0 "$25\,\Omega$: falls $8\,\mathrm{V}$" col=3 i="$0.32\,\mathrm{A}$" to=z0 id=eR4
#@ el R m a "$12\,\Omega$: falls $12\,\mathrm{V}$" col=4 i="$1\,\mathrm{A}$" to=m id=eR5
#@ el I z0 a "test $1\,\mathrm{A}$" col=5 i="$1\,\mathrm{A}$" to=a id=eIT
#@ step "Ground $k$, the lowest wire (the diamond's $-$ end). No independent source, so with nothing attached every height is $0$: $V_{\mathrm{Th}}=0$."
#@ step "Push $1\,\mathrm{A}$ into $a$. It slides down the $12\,\Omega$ to $m$, so $m=a-12$." show=eR5,eIT
#@ step "The diamond is a battery of $6.5i_x$ ($+$ at $b$) with $i_x=\dfrac{m}{25}$. In = out at $m$ and at $t$ (from $b$): $m=8$, $t=1.2$, $a=20\,\mathrm{V}$." show=m,t,a,z0
#@ step "$a$ sits $20\,\mathrm{V}$ above $b$ for $1\,\mathrm{A}$: $R_{\mathrm{Th}}=20\,\Omega$. With $V_{\mathrm{Th}}=0$ the terminals act like a plain $20\,\Omega$ resistor." show=eR1,eR2,eR3,eR4,eE1
```

<details><summary>Solution</summary>

1. No independent source.

   $$V_{\mathrm{Th}}=0$$
2. Test current $1\,\mathrm{A}$ into $a$; $i_x=\dfrac{v_m}{25}$, diamond: $v_k=-6.5i_x$. In = out at $m$ and $t$.

   $$\begin{aligned}1&=\tfrac{v_m}{25}+\tfrac{v_m-v_t}{10}\\\tfrac{v_m-v_t}{10}&=\tfrac{v_t}{50}+\tfrac{v_t+6.5v_m/25}{5}\end{aligned}$$
3. Solve.

   $$v_m=8\,\mathrm{V},\quad v_t=1.2\,\mathrm{V},\quad v_a=8+12=20\,\mathrm{V}\;\Rightarrow\;R_{\mathrm{Th}}=20\,\Omega$$

**Answer:** $V_{\mathrm{Th}}=0$, $R_{\mathrm{Th}}=20\,\Omega$

</details>

## Topic 2: Maximum power: half the open height

> **Tip:** **How it looks in heights.**
> 
> - A load on a Thévenin source sits at some height $h$ and gets current $\dfrac{V_{\mathrm{Th}}-h}{R_{\mathrm{Th}}}$. Its power $h\cdot\dfrac{V_{\mathrm{Th}}-h}{R_{\mathrm{Th}}}$ is biggest when $h=\dfrac{V_{\mathrm{Th}}}{2}$: the **half-height rule**. That happens when $R_L=R_{\mathrm{Th}}$.
> - Half of $V_{\mathrm{Th}}$, not half the battery.
> - Maximum power is not maximum efficiency. For efficiency, go back to the original circuit and compare the load's power with every source's climb.
> - Load fixed and a series resistor is the knob? That resistor only steals height: the best value is $0$.

$$R_L=R_{\mathrm{Th}},\qquad h=\frac{V_{\mathrm{Th}}}{2},\qquad p_{\max}=\frac{V_{\mathrm{Th}}^2}{4R_{\mathrm{Th}}}$$

**Example: Example 4 · Matched vs not**

$V_{\mathrm{Th}}=20\,\mathrm{V}$, $R_{\mathrm{Th}}=5\,\Omega$. Compare $R_L=5$, $20$ and $1.25\,\Omega$.

```schematic
V1 0,3 -> 0,0 "$V_{\mathrm{Th}}=20\,\mathrm{V}$"
R1 0,3 -> 3,3 "$R_{\mathrm{Th}}=5\,\Omega$"
wire 3,3 -> 5,3
RL 5,3 -> 5,0 "$R_L$" flip
wire 5,0 -> 0,0
terminal 3,3 "$a$" above
ground 0,0
#@ inline
#@ view "Load 5 Ω (matched)"
#@ straight off
#@ node t 20 "top: $20\,\mathrm{V}$"
#@ node a 10 "$a$: $10\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V t g "$V_{\mathrm{Th}}$: $20\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=t id=eV1
#@ el R t a "$5\,\Omega$: falls $10\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$5\,\Omega$: falls $10\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=eRL
#@ step "Ground $b$. $a$ at half height, $10\,\mathrm{V}$; $2\,\mathrm{A}$; $p=20\,\mathrm{W}$ (the most)." show=a,eRL
#@ view "Load 20 Ω"
#@ straight off
#@ node t 20 "top: $20\,\mathrm{V}$"
#@ node a 16 "$a$: $16\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V t g "$V_{\mathrm{Th}}$: $20\,\mathrm{V}$" col=0 i="$0.8\,\mathrm{A}$" to=t id=eV1
#@ el R t a "$5\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$0.8\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$20\,\Omega$: falls $16\,\mathrm{V}$" col=1 i="$0.8\,\mathrm{A}$" to=g2 id=eRL
#@ note "$a=16\,\mathrm{V}$, $0.8\,\mathrm{A}$: $12.8\,\mathrm{W}$."
#@ view "Load 1.25 Ω"
#@ straight off
#@ node t 20 "top: $20\,\mathrm{V}$"
#@ node a 4 "$a$: $4\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V t g "$V_{\mathrm{Th}}$: $20\,\mathrm{V}$" col=0 i="$3.2\,\mathrm{A}$" to=t id=eV1
#@ el R t a "$5\,\Omega$: falls $16\,\mathrm{V}$" col=1 i="$3.2\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$1.25\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$3.2\,\mathrm{A}$" to=g2 id=eRL
#@ note "$a=4\,\mathrm{V}$, $3.2\,\mathrm{A}$: also $12.8\,\mathrm{W}$. $4$ and $16$ mirror around $10$."
```

1. Power at height $h$.

   $$p=h\cdot\frac{20-h}{5}:\quad h=10\to20\,\mathrm{W},\quad h=4\text{ or }16\to12.8\,\mathrm{W}$$

**Answer:** Matched: $20\,\mathrm{W}$; the other two: $12.8\,\mathrm{W}$ each.

**Example: Example 5 · Half the open height (Lecture 5)**

$R_L$ is adjustable. **(a)** Which $R_L$ gets the most power? **(b)** How much? **(c)** What fraction of the source's power reaches $R_L$?

```schematic
V1 0,3 -> 0,0 "$360\,\mathrm{V}$"
R1 0,3 -> 3,3 "$30\,\Omega$"
R2 3,3 -> 3,0 "$150\,\Omega$"
wire 3,3 -> 6,3
R3 6,3 -> 6,0 "$R_L$"
wire 0,0 -> 6,0
label 3,3 "$a$" above
ground 0,0
#@ inline
#@ view "Open"
#@ straight off
#@ node s 360 "source top: $360\,\mathrm{V}$"
#@ node a 300 "$a$: $300\,\mathrm{V}$" terminal
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$360\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$30\,\Omega$: falls $60\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$150\,\Omega$: falls $300\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=g2 id=eR2
#@ step "Ground the bottom wire. Open: divider, $a=360\cdot\tfrac{150}{180}=300\,\mathrm{V}=V_{\mathrm{Th}}$. Sources off: $R_{\mathrm{Th}}=30\parallel150=25\,\Omega$." show=a
#@ view "Load 5 Ω"
#@ straight off
#@ node s 360 "source top: $360\,\mathrm{V}$"
#@ node a 50 "$a$: $50\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$360\,\mathrm{V}$" col=0 i="$10.33\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$30\,\Omega$: falls $310\,\mathrm{V}$" col=1 i="$10.33\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$150\,\Omega$: falls $50\,\mathrm{V}$" col=2 i="$0.3333\,\mathrm{A}$" to=g2 id=eR2
#@ el R a g3 "$5\,\Omega$: falls $50\,\mathrm{V}$" col=3 i="$10\,\mathrm{A}$" to=g3 id=eR3
#@ note "Too small: $a$ sits low ($50\,\mathrm{V}$). Load gets $50\times10=500\,\mathrm{W}$."
#@ view "Load 25 Ω (matched)"
#@ straight off
#@ node s 360 "source top: $360\,\mathrm{V}$"
#@ node a 150 "$a$: $150\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$360\,\mathrm{V}$" col=0 i="$7\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$30\,\Omega$: falls $210\,\mathrm{V}$" col=1 i="$7\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$150\,\Omega$: falls $150\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=g2 id=eR2
#@ el R a g3 "$25\,\Omega$: falls $150\,\mathrm{V}$" col=3 i="$6\,\mathrm{A}$" to=g3 id=eR3
#@ step "Same ground. Matched: $a$ sits at half the open height, $150\,\mathrm{V}$." show=a
#@ step "Load current $\dfrac{150}{25}=6\,\mathrm{A}$: $p_{\max}=(150)(6)=900\,\mathrm{W}$." show=eR3
#@ step "Source: $\dfrac{360-150}{30}=7\,\mathrm{A}$ climbs $360\,\mathrm{V}$: $2520\,\mathrm{W}$. Only $\dfrac{900}{2520}=35.7\%$ reaches the load." show=eR1,eR2,eV1
#@ view "Load 100 Ω"
#@ straight off
#@ node s 360 "source top: $360\,\mathrm{V}$"
#@ node a 240 "$a$: $240\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$360\,\mathrm{V}$" col=0 i="$4\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$30\,\Omega$: falls $120\,\mathrm{V}$" col=1 i="$4\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$150\,\Omega$: falls $240\,\mathrm{V}$" col=2 i="$1.6\,\mathrm{A}$" to=g2 id=eR2
#@ el R a g3 "$100\,\Omega$: falls $240\,\mathrm{V}$" col=3 i="$2.4\,\mathrm{A}$" to=g3 id=eR3
#@ note "Too big: $a$ sits high ($240\,\mathrm{V}$) but little current. Load gets $240\times2.4=576\,\mathrm{W}$."
```

1. Thévenin.

   $$V_{\mathrm{Th}}=360\cdot\frac{150}{180}=300\,\mathrm{V},\qquad R_{\mathrm{Th}}=30\parallel150=25\,\Omega$$
2. Match.

   $$R_L=25\,\Omega,\qquad p_{\max}=\frac{300^2}{4(25)}=900\,\mathrm{W}$$
3. Back to the original.

   $$v_a=150\,\mathrm{V},\quad i_s=\frac{360-150}{30}=7\,\mathrm{A},\quad \eta=\frac{900}{360(7)}=35.7\%$$

**Answer:** **(a)** $25\,\Omega$ **(b)** $900\,\mathrm{W}$ **(c)** $35.7\%$

**Example: Example 6 · Two sources, then match (Lecture 5)**

$R_L$ is adjustable. Find the Thévenin equivalent at $a$–$b$ ($b$ is the bottom wire), then the best $R_L$ and $p_{\max}$.

```schematic
V1 0,0 -> 0,3 "$3\,\mathrm{V}$"
I1 0,3 -> 0,6 "$2\,\mathrm{mA}$"
wire 0,6 -> 8,6
R2 0,3 -> 3,3 "$3\,\mathrm{k\Omega}$"
wire 3,3 -> 4,3
R1 4,6 -> 4,3 "$4\,\mathrm{k\Omega}$"
R3 4,3 -> 4,0 "$6\,\mathrm{k\Omega}$"
R4 8,6 -> 8,3 "$R_L$"
wire 8,3 -> 8,0
wire 0,0 -> 8,0
label 8,6 "$a$" right
label 4,3 "$m$" right
label 0,3 "$c$" left
ground 4,0
#@ inline
#@ view "Open"
#@ straight off
#@ node a 13 "$a$: $13\,\mathrm{V}$" terminal
#@ node m 5 "$m$: $5\,\mathrm{V}$"
#@ node z0 3 "$b$: $3\,\mathrm{V}$"
#@ node g 0 "$c$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$c$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$c$: $0\,\mathrm{V}$" ground
#@ el R g m "$3\,\mathrm{k\Omega}$: falls $5\,\mathrm{V}$" col=0 i="$1.667\,\mathrm{mA}$" to=g id=eR2
#@ el R a m "$4\,\mathrm{k\Omega}$: falls $8\,\mathrm{V}$" col=1 i="$2\,\mathrm{mA}$" to=m id=eR1
#@ el R m z0 "$6\,\mathrm{k\Omega}$: falls $2\,\mathrm{V}$" col=1 i="$0.3333\,\mathrm{mA}$" to=z0 id=eR3
#@ el V z0 g2 "$3\,\mathrm{V}$" col=2 i="$0.3333\,\mathrm{mA}$" to=g2 id=eV1
#@ el I g3 a "$2\,\mathrm{mA}$" col=3 i="$2\,\mathrm{mA}$" to=a id=eI1
#@ step "Ground $c$, the lowest node: the $3\,\mathrm{V}$ source hangs it below $b$. Read every answer as a height **above $b$**."
#@ step "The pump forces $2\,\mathrm{mA}$ through $R_1$: it falls $8\,\mathrm{V}$." show=eI1,eR1
#@ step "Lower mesh: $i_2=\dfrac{3(2)-3}{3+6}=\tfrac13\,\mathrm{mA}$ down $R_3$, so $m$ is $2\,\mathrm{V}$ above $b$ and $a$ is $10\,\mathrm{V}$ above: $V_{\mathrm{Th}}=10\,\mathrm{V}$." show=m,a,eR2,eR3,eV1
#@ step "Sources off: pump → gap, $3\,\mathrm{V}$ → wire, so $R_{\mathrm{Th}}=4+(3\parallel6)=6\,\mathrm{k\Omega}$."
#@ view "Matched: 6 kΩ"
#@ straight off
#@ node a 8 "$a$: $8\,\mathrm{V}$"
#@ node m 3.33 "$m$: $3.33\,\mathrm{V}$"
#@ node z0 3 "$b$: $3\,\mathrm{V}$"
#@ node g 0 "$c$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$c$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$c$: $0\,\mathrm{V}$" ground
#@ el R g m "$3\,\mathrm{k\Omega}$: falls $3.33\,\mathrm{V}$" col=0 i="$1.111\,\mathrm{mA}$" to=g id=eR2
#@ el R a m "$4\,\mathrm{k\Omega}$: falls $4.67\,\mathrm{V}$" col=1 i="$1.167\,\mathrm{mA}$" to=m id=eR1
#@ el R m z0 "$6\,\mathrm{k\Omega}$: falls $0.3333\,\mathrm{V}$" col=1 i="$0.05556\,\mathrm{mA}$" to=z0 id=eR3
#@ el R a z0 "$6\,\mathrm{k\Omega}$: falls $5\,\mathrm{V}$" col=2 i="$0.8333\,\mathrm{mA}$" to=z0 id=eR4
#@ el V z0 g2 "$3\,\mathrm{V}$" col=2 i="$0.8889\,\mathrm{mA}$" to=g2 id=eV1
#@ el I g3 a "$2\,\mathrm{mA}$" col=3 i="$2\,\mathrm{mA}$" to=a id=eI1
#@ step "Same ground. Matched: $a$ sits $5\,\mathrm{V}$ above $b$, half of $V_{\mathrm{Th}}$." show=a
#@ step "The load carries $\dfrac{5}{6}\,\mathrm{mA}$: $p_{\max}=\dfrac{10^2}{4(6000)}=4.17\,\mathrm{mW}$." show=eR4
```

1. Pump fixes mesh 1; KVL on the lower mesh (kΩ, mA).

   $$3+3(i_2-2)+6i_2=0\;\Rightarrow\;i_2=\tfrac13\,\mathrm{mA}$$
2. Open height of $a$.

   $$V_{\mathrm{Th}}=4(2)+6(\tfrac13)=10\,\mathrm{V}$$
3. Sources off.

   $$R_{\mathrm{Th}}=4+(3\parallel6)=6\,\mathrm{k\Omega}$$
4. Match.

   $$R_L=6\,\mathrm{k\Omega},\qquad p_{\max}=\frac{10^2}{4(6000)}=4.17\,\mathrm{mW}$$

**Answer:** $V_{\mathrm{Th}}=10\,\mathrm{V}$, $R_{\mathrm{Th}}=6\,\mathrm{k\Omega}$; $R_L=6\,\mathrm{k\Omega}$ gets $4.17\,\mathrm{mW}$.

**Problem: Try it 5 · The matching trap (Textbook P4.84)** (introductory)

**(a)** Which $R_o$ gives the most power in the $6\,\Omega$? (Hint: hasty conclusions could be hazardous to your career.) **(b)** What is that power?

```schematic
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
R1 0,3 -> 3,3 "$R_o$"
R2 3,3 -> 3,0 "$6\,\Omega$"
wire 0,0 -> 3,0
label 3,3 "$a$" above
ground 0,0
#@ spoiler
#@ view "6 Ω (the trap)"
#@ straight off
#@ node s 30 "source top: $30\,\mathrm{V}$"
#@ node a 15 "$a$: $15\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$30\,\mathrm{V}$" col=0 i="$2.5\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$R_o=6\,\Omega$: falls $15\,\mathrm{V}$" col=1 i="$2.5\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$6\,\Omega$: falls $15\,\mathrm{V}$" col=1 i="$2.5\,\mathrm{A}$" to=g2 id=eR2
#@ step "Ground the bottom wire. Matching says $R_o=6\,\Omega$: $a$ sits at $15\,\mathrm{V}$, $p_6=\dfrac{15^2}{6}=37.5\,\mathrm{W}$." show=a,eR1,eR2
#@ view "0 Ω"
#@ straight off
#@ node s 30 "source top = $a$: $30\,\mathrm{V}$"
#@ node a 30 "source top = $a$: $30\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ el V s g "$30\,\mathrm{V}$" col=0 i="$5\,\mathrm{A}$" to=s id=eV1
#@ el W s a "$R_o=0$: no step" col=1 i="$5\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$6\,\Omega$: falls $30\,\mathrm{V}$" col=2 i="$5\,\mathrm{A}$" to=g2 id=eR2
#@ step "Same ground. But here the **load is fixed** and $R_o$ is the knob. $R_o$ only steals height, so set it to $0$: $a$ sits at the full $30\,\mathrm{V}$." show=a
#@ step "$p_6=\dfrac{30^2}{6}=150\,\mathrm{W}$, four times the trap." show=eR2,eR1
```

<details><summary>Solution</summary>

1. Write the load power directly.

   $$p_6=\Big(\frac{30}{R_o+6}\Big)^2(6)$$
2. It falls as $R_o$ grows: pick the smallest.

   $$R_o=0,\qquad p_{\max}=\frac{30^2}{6}=150\,\mathrm{W}$$

**Answer:** **(a)** $R_o=0$ (not $6\,\Omega$) **(b)** $150\,\mathrm{W}$

</details>

**Problem: Try it 6 · Two loads, same power (Textbook P4.88)** (advanced)

$R_o$ is adjusted until it dissipates $1.5\,\mathrm{W}$. Find **both** values of $R_o$.

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$50\,\Omega$"
R2 3,3 -> 3,0 "$200\,\Omega$"
R3 3,3 -> 6,3 "$60\,\Omega$" i="$i_x$"
R4 6,3 -> 6,1.5 "$40\,\Omega$"
E1 6,0 -> 6,1.5 "$60i_x$"
wire 6,3 -> 9,3
R5 9,3 -> 9,0 "$R_o$"
wire 0,0 -> 9,0
label 3,3 "$n$" above
label 6,3 "$a$" above
label 6,1.5 "$k$" right
ground 0,0
#@ spoiler
#@ view "Open"
#@ straight off
#@ node s 160 "source top: $160\,\mathrm{V}$"
#@ node n 100 "$n$: $100\,\mathrm{V}$"
#@ node z0 60 "$b$: $60\,\mathrm{V}$"
#@ node a 40 "$a$: $40\,\mathrm{V}$" terminal
#@ node g 0 "$k$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$k$: $0\,\mathrm{V}$" ground
#@ el V s z0 "$100\,\mathrm{V}$" col=0 i="$1.2\,\mathrm{A}$" to=s id=eV1
#@ el R s n "$50\,\Omega$: falls $60\,\mathrm{V}$" col=1 i="$1.2\,\mathrm{A}$" to=n id=eR1
#@ el R n z0 "$200\,\Omega$: falls $40\,\mathrm{V}$" col=1 i="$0.2\,\mathrm{A}$" to=z0 id=eR2
#@ el E z0 g "$60i_x$: $60\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=z0 id=eE1
#@ el R n a "$60\,\Omega$: falls $60\,\mathrm{V}$" col=4 i="$1\,\mathrm{A}$" to=a id=eR3
#@ el R a g2 "$40\,\Omega$: falls $40\,\mathrm{V}$" col=4 i="$1\,\mathrm{A}$" to=g2 id=eR4
#@ step "Ground $k$, the lowest node (the diamond hangs it below $b$). Read answers as heights relative to $b$."
#@ step "Open: $i_x$ runs through $60+40\,\Omega$ into the diamond. $a=-20i_x$, $n=40i_x$; KCL at $n$: $\dfrac{100-n}{50}=\dfrac{n}{200}+i_x$, so $i_x=1\,\mathrm{A}$." show=n,eR3,eR4,eE1
#@ step "$a$ sits $20\,\mathrm{V}$ **below** $b$: $V_{\mathrm{Th}}=-20\,\mathrm{V}$. With a short, $I_N=-0.4\,\mathrm{A}$, so $R_{\mathrm{Th}}=50\,\Omega$." show=a,eR1,eR2,eV1
#@ view "16.7 Ω"
#@ straight off
#@ node s 151 "source top: $151\,\mathrm{V}$"
#@ node n 97 "$n$: $97\,\mathrm{V}$"
#@ node z0 51 "$b$: $51\,\mathrm{V}$"
#@ node a 46 "$a$: $46\,\mathrm{V}$"
#@ node g 0 "$k$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$k$: $0\,\mathrm{V}$" ground
#@ el V s z0 "$100\,\mathrm{V}$" col=0 i="$1.08\,\mathrm{A}$" to=s id=eV1
#@ el R s n "$50\,\Omega$: falls $54\,\mathrm{V}$" col=1 i="$1.08\,\mathrm{A}$" to=n id=eR1
#@ el R n z0 "$200\,\Omega$: falls $46\,\mathrm{V}$" col=1 i="$0.23\,\mathrm{A}$" to=z0 id=eR2
#@ el E z0 g "$60i_x$: $51\,\mathrm{V}$" col=2 i="$1.15\,\mathrm{A}$" to=z0 id=eE1
#@ el R n a "$60\,\Omega$: falls $51\,\mathrm{V}$" col=4 i="$0.85\,\mathrm{A}$" to=a id=eR3
#@ el R a g2 "$40\,\Omega$: falls $46\,\mathrm{V}$" col=4 i="$1.15\,\mathrm{A}$" to=g2 id=eR4
#@ el R a z0 "$16.67\,\Omega$: falls $5\,\mathrm{V}$" col=3 i="$0.3\,\mathrm{A}$" to=a id=eR5
#@ step "Same ground. Let the load's fall be $h$: $p=h\cdot\dfrac{20-h}{50}=1.5$, so $h^2-20h+75=0$: $h=5$ or $15\,\mathrm{V}$."
#@ step "$h=5\,\mathrm{V}$: current $\dfrac{20-5}{50}=0.3\,\mathrm{A}$, so $R_o=\dfrac{5}{0.3}=16.7\,\Omega$." show=a,eR5
#@ view "150 Ω"
#@ straight off
#@ node s 157 "source top: $157\,\mathrm{V}$"
#@ node n 99 "$n$: $99\,\mathrm{V}$"
#@ node z0 57 "$b$: $57\,\mathrm{V}$"
#@ node a 42 "$a$: $42\,\mathrm{V}$"
#@ node g 0 "$k$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$k$: $0\,\mathrm{V}$" ground
#@ el V s z0 "$100\,\mathrm{V}$" col=0 i="$1.16\,\mathrm{A}$" to=s id=eV1
#@ el R s n "$50\,\Omega$: falls $58\,\mathrm{V}$" col=1 i="$1.16\,\mathrm{A}$" to=n id=eR1
#@ el R n z0 "$200\,\Omega$: falls $42\,\mathrm{V}$" col=1 i="$0.21\,\mathrm{A}$" to=z0 id=eR2
#@ el E z0 g "$60i_x$: $57\,\mathrm{V}$" col=2 i="$1.05\,\mathrm{A}$" to=z0 id=eE1
#@ el R n a "$60\,\Omega$: falls $57\,\mathrm{V}$" col=4 i="$0.95\,\mathrm{A}$" to=a id=eR3
#@ el R a g2 "$40\,\Omega$: falls $42\,\mathrm{V}$" col=4 i="$1.05\,\mathrm{A}$" to=g2 id=eR4
#@ el R a z0 "$150\,\Omega$: falls $15\,\mathrm{V}$" col=3 i="$0.1\,\mathrm{A}$" to=a id=eR5
#@ step "Same ground ($k$). $h=15\,\mathrm{V}$: current $\dfrac{5}{50}=0.1\,\mathrm{A}$, so $R_o=150\,\Omega$." show=a,eR5
#@ note "The two loads fall $5$ and $15\,\mathrm{V}$: mirror images around half of $|V_{\mathrm{Th}}|=10\,\mathrm{V}$, where the power would peak ($2\,\mathrm{W}$)."
```

<details><summary>Solution</summary>

1. Open circuit ($i_x$ through $60+40\,\Omega$ and the diamond).

   $$\begin{aligned}&v_a=-20i_x,\quad v_n=40i_x,\quad \frac{100-v_n}{50}=\frac{v_n}{200}+i_x\\&\Rightarrow\;i_x=1\,\mathrm{A},\quad V_{\mathrm{Th}}=-20\,\mathrm{V}\end{aligned}$$
2. Short circuit gives $I_N=-0.4\,\mathrm{A}$.

   $$R_{\mathrm{Th}}=\frac{-20}{-0.4}=50\,\Omega$$
3. Power equation.

   $$\Big(\frac{20}{50+R_o}\Big)^2R_o=1.5\;\Rightarrow\;3R_o^2-500R_o+7500=0$$
4. Two roots.

   $$R_o=\frac{500\pm400}{6}=150\,\Omega\;\text{ or }\;16.7\,\Omega$$

**Answer:** $R_o=16.7\,\Omega$ or $R_o=150\,\Omega$.

</details>

**Problem: Try it 7 · Match the load on a diamond circuit (Textbook P4.83)** (intermediate)

$R_o$ is connected across $a$–$b$ of the circuit in Try it 1 and adjusted for maximum power. **(a)** Find $R_o$. **(b)** Find $p_{\max}$. **(c)** What percentage of the power developed reaches $R_o$?

```schematic
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
wire 0,3 -> 0,6
G1 3,6 -> 0,6 "$3i_x$"
wire 3,6 -> 3,3
wire 3,3 -> 5,3
I1 5,3 -> 5,0 "$4\,\mathrm{A}$"
wire 5,3 -> 7,3
R2 7,3 -> 7,0 "$8\,\Omega$" i="$i_x$"
wire 7,3 -> 10,3
RO 10,3 -> 10,0 "$R_o$"
wire 0,0 -> 10,0
label 7,3 "$a$" above
ground 0,0
#@ spoiler
#@ view "Matched: 1 Ω"
#@ straight off
#@ node s 24 "battery top: $24\,\mathrm{V}$"
#@ node a 4 "$a$: $4\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g4 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$24\,\mathrm{V}$" col=0 i="$8.5\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$2\,\Omega$: falls $20\,\mathrm{V}$" col=1 i="$10\,\mathrm{A}$" to=a id=eR1
#@ el G a s "$3i_x$: $1.5\,\mathrm{A}$" col=2 i="$1.5\,\mathrm{A}$" to=s id=eG1
#@ el I a g2 "$4\,\mathrm{A}$" col=3 i="$4\,\mathrm{A}$" to=g2 id=eI1
#@ el R a g3 "$8\,\Omega$: falls $4\,\mathrm{V}$" col=4 i="$0.5\,\mathrm{A}$" to=g3 id=eR2
#@ el R a g4 "$1\,\Omega$: falls $4\,\mathrm{V}$" col=5 i="$4\,\mathrm{A}$" to=g4 id=eRO
#@ step "Ground $b$. From Try it 1: $V_{\mathrm{Th}}=8\,\mathrm{V}$, $R_{\mathrm{Th}}=1\,\Omega$. So $R_o=1\,\Omega$."
#@ step "Half-height rule: $a$ sits at $4\,\mathrm{V}$. $p_{\max}=\dfrac{4^2}{1}=16\,\mathrm{W}$." show=a,eRO
#@ step "Climbs in the real circuit: the battery lifts $8.5\,\mathrm{A}$ by $24\,\mathrm{V}$ ($204\,\mathrm{W}$), the diamond $1.5\,\mathrm{A}$ by $20\,\mathrm{V}$ ($30\,\mathrm{W}$). The $4\,\mathrm{A}$ pump falls $4\,\mathrm{V}$ (it absorbs). $R_o$ gets $\dfrac{16}{234}=6.8\%$." show=eV1,eR1,eG1,eI1,eR2
```

<details><summary>Solution</summary>

1. Match.

   $$R_o=R_{\mathrm{Th}}=1\,\Omega,\qquad p_{\max}=\frac{8^2}{4(1)}=16\,\mathrm{W}$$
2. Original circuit with $R_o=1\,\Omega$ ($v_a=4\,\mathrm{V}$, $i_x=0.5\,\mathrm{A}$).

   $$p_{\text{dev}}=24(8.5)+20(1.5)=234\,\mathrm{W},\qquad \frac{16}{234}=6.84\%$$

**Answer:** **(a)** $1\,\Omega$ **(b)** $16\,\mathrm{W}$ **(c)** $6.84\%$

</details>

**Problem: Try it 8 · Maximum power, and most of it gets there (Textbook P4.87)** (advanced)

$R_o$ is adjusted for maximum power. **(a)** Find $R_o$. **(b)** Find $p_{\max}$. **(c)** What percentage of the power developed reaches $R_o$?

```schematic
V1 0,3 -> 0,0 "$100\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$" i="$i_\Delta$"
R2 3,3 -> 3,1.6 "$5\,\Omega$"
E1 3,1.6 -> 3,0 "$13i_\Delta$"
R3 3,3 -> 6,3 "$4\,\Omega$" v="$v_\Delta$"
G1 6,0 -> 6,3 "$v_\Delta$"
wire 6,3 -> 9,3
RO 9,3 -> 9,0 "$R_o$"
wire 0,0 -> 9,0
label 3,3 "$p$" above
label 3,1.6 "$k$" right
label 6,3 "$q$" above
ground 0,0
#@ spoiler
#@ view "Open"
#@ straight off
#@ node s 100 "battery top: $100\,\mathrm{V}$"
#@ node p 90 "$p$ = $q$: $90\,\mathrm{V}$"
#@ node q 90 "$p$ = $q$: $90\,\mathrm{V}$"
#@ node k 65 "diamond top: $65\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$100\,\mathrm{V}$" col=0 i="$5\,\mathrm{A}$" to=s id=eV1
#@ el E k g2 "$13i_\Delta$: $65\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=g2 id=eE1
#@ el R p k "$5\,\Omega$: falls $25\,\mathrm{V}$" col=2 i="$5\,\mathrm{A}$" to=k id=eR2
#@ el R s p "$2\,\Omega$: falls $10\,\mathrm{V}$" col=3 i="$5\,\mathrm{A}$" to=p id=eR1
#@ el R p q "$4\,\Omega$: no fall" col=4 id=eR3 plus=p v="$v_\Delta$"
#@ el G g3 q "$v_\Delta$: $0\,\mathrm{A}$" col=5 id=eG1
#@ step "Ground the bottom wire. The battery lifts its top to $100\,\mathrm{V}$."
#@ step "Open: the pump pushes $v_\Delta=p-q$ into $q$, and only the $4\,\Omega$ can take it away: $\dfrac{p-q}{4}+(p-q)=0$, so $p=q$ and the $4\,\Omega$ lies flat." show=eR3,eG1
#@ step "Left loop: $100=2i_\Delta+5i_\Delta+13i_\Delta$, so $i_\Delta=5\,\mathrm{A}$ and $p=90\,\mathrm{V}$: $V_{\mathrm{Th}}=90\,\mathrm{V}$. (A short gives $I_N=100\,\mathrm{A}$, so $R_{\mathrm{Th}}=0.9\,\Omega$.)" show=p,q,k,eR1,eR2,eE1,eV1
#@ view "Matched: 0.9 Ω"
#@ straight off
#@ node s 100 "battery top: $100\,\mathrm{V}$"
#@ node k 97.5 "diamond top: $97.5\,\mathrm{V}$"
#@ node p 85 "$p$: $85\,\mathrm{V}$"
#@ node q 45 "$q$: $45\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g4 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$100\,\mathrm{V}$" col=0 i="$7.5\,\mathrm{A}$" to=s id=eV1
#@ el E k g2 "$13i_\Delta$: $97.5\,\mathrm{V}$" col=1 i="$2.5\,\mathrm{A}$" to=k id=eE1
#@ el R p k "$5\,\Omega$: falls $12.5\,\mathrm{V}$" col=2 i="$2.5\,\mathrm{A}$" to=p id=eR2
#@ el R s p "$2\,\Omega$: falls $15\,\mathrm{V}$" col=3 i="$7.5\,\mathrm{A}$" to=p id=eR1
#@ el R p q "$4\,\Omega$: falls $40\,\mathrm{V}$" col=3 i="$10\,\mathrm{A}$" to=q id=eR3 plus=p v="$v_\Delta$"
#@ el R q g3 "$0.9\,\Omega$: falls $45\,\mathrm{V}$" col=3 i="$50\,\mathrm{A}$" to=g3 id=eRO
#@ el G g4 q "$v_\Delta$: $40\,\mathrm{A}$" col=4 i="$40\,\mathrm{A}$" to=q id=eG1
#@ step "Same ground. Matched: $q$ sits at half of $90$, $45\,\mathrm{V}$. $p_{\max}=\dfrac{45^2}{0.9}=2250\,\mathrm{W}$." show=q,eRO
#@ step "Climbs: battery $750\,\mathrm{W}$, diamond $243.75\,\mathrm{W}$, pump $40\,\mathrm{A}$ by $45\,\mathrm{V}=1800\,\mathrm{W}$. $R_o$ gets $\dfrac{2250}{2793.75}=80.5\%$: the diamond pump does most of the lifting." show=p,k,eR1,eR2,eR3,eE1,eG1,eV1
```

<details><summary>Solution</summary>

1. Open: the pump forces $v_\Delta=0$; left loop.

   $$\begin{aligned}&100=(2+5+13)\,i_\Delta\;\Rightarrow\;i_\Delta=5\,\mathrm{A}\\&V_{\mathrm{Th}}=100-2(5)=90\,\mathrm{V}\end{aligned}$$
2. Short ($q=0$): $i_{sc}=100\,\mathrm{A}$.

   $$R_{\mathrm{Th}}=\frac{90}{100}=0.9\,\Omega$$
3. Match and efficiency.

   $$p_{\max}=\frac{90^2}{4(0.9)}=2250\,\mathrm{W},\qquad \frac{2250}{750+243.75+1800}=80.5\%$$

**Answer:** **(a)** $0.9\,\Omega$ **(b)** $2250\,\mathrm{W}$ **(c)** $80.5\%$

</details>

## Topic 3: Superposition: add heights, not powers

> **Tip:** **How it looks in heights.**
> 
> - One picture per independent source: the other batteries become wires, the other pumps become gaps. **Diamonds stay on.**
> - **Add the heights** (voltages) and the currents from the pictures. **Never add powers**: power is a product, so compute it once from the sums.
> - Keep the same reference directions in every picture.
> - Worth it when each one-source picture is a simple divider; otherwise one node-voltage solve is faster.

$$y=y_1+y_2+\cdots,\qquad p=(v_1+v_2)(i_1+i_2)\neq p_1+p_2$$

**Example: Example 7 · Two pictures, one sum**

Find the height of $m$ by superposition.

```schematic
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$" flip
wire 3,3 -> 6,3
I1 6,0 -> 6,3 "$2\,\mathrm{A}$" flip
wire 6,0 -> 0,0
label 3,3 "$m$" above
ground 0,0
#@ inline
#@ view "12 V alone"
#@ straight off
#@ node t 12 "source top: $12\,\mathrm{V}$"
#@ node m 6 "$m$: $6\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ el V t g "$12\,\mathrm{V}$" col=0 i="$1.5\,\mathrm{A}$" to=t id=eV1
#@ el R t m "$4\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$1.5\,\mathrm{A}$" to=m id=eR1
#@ el R m g2 "$4\,\Omega$: falls $6\,\mathrm{V}$" col=1 i="$1.5\,\mathrm{A}$" to=g2 id=eR2
#@ step "Ground the bottom wire. Pump off: a divider, $m'=6\,\mathrm{V}$." show=m,eR1,eR2
#@ view "2 A alone"
#@ straight off
#@ node m 4 "$m$: $4\,\mathrm{V}$"
#@ node t 0 "source top = ground: $0\,\mathrm{V}$"
#@ node g 0 "source top = ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "source top = ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "source top = ground: $0\,\mathrm{V}$" ground
#@ el W t g "$12\,\mathrm{V}$ off: a wire" col=0 i="$1\,\mathrm{A}$" to=g id=eV1
#@ el R t m "$4\,\Omega$: falls $4\,\mathrm{V}$" col=1 i="$1\,\mathrm{A}$" to=t id=eR1
#@ el R m g2 "$4\,\Omega$: falls $4\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=g2 id=eR2
#@ el I g3 m "$2\,\mathrm{A}$" col=3 i="$2\,\mathrm{A}$" to=m id=eI1
#@ step "Same ground. $12\,\mathrm{V}$ → wire. $2\,\mathrm{A}$ into $4\parallel4=2\,\Omega$: $m''=4\,\mathrm{V}$." show=m,eR1,eR2
#@ view "Both: add"
#@ straight off
#@ node t 12 "source top: $12\,\mathrm{V}$"
#@ node m 10 "$m$: $10\,\mathrm{V}$"
#@ node g 0 "ground: $0\,\mathrm{V}$" ground
#@ node g2 0 "ground: $0\,\mathrm{V}$" ground
#@ node g3 0 "ground: $0\,\mathrm{V}$" ground
#@ el V t g "$12\,\mathrm{V}$" col=0 i="$0.5\,\mathrm{A}$" to=t id=eV1
#@ el R t m "$4\,\Omega$: falls $2\,\mathrm{V}$" col=1 i="$0.5\,\mathrm{A}$" to=m id=eR1
#@ el R m g2 "$4\,\Omega$: falls $10\,\mathrm{V}$" col=1 i="$2.5\,\mathrm{A}$" to=g2 id=eR2
#@ el I g3 m "$2\,\mathrm{A}$" col=2 i="$2\,\mathrm{A}$" to=m id=eI1
#@ step "Same ground. $m=6+4=10\,\mathrm{V}$. Power in the lower $4\,\Omega$: $\dfrac{10^2}{4}=25\,\mathrm{W}$, not $9+4$." show=m,eR1,eR2
```

1. Add the heights.

   $$m=6+4=10\,\mathrm{V},\qquad p_{4\Omega}=\frac{10^2}{4}=25\,\mathrm{W}\neq9+4$$

**Answer:** $m=10\,\mathrm{V}$

**Example: Example 8 · One source at a time (Lecture 5)**

Use superposition to find $v_o$ and $i_o$.

```schematic
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
R1 0,3 -> 3,3 "$6\,\Omega$"
R3 3,3 -> 3,0 "$3\,\Omega$" i="$i_o$"
R2 3,3 -> 6,3 "$2\,\Omega$"
R4 6,3 -> 6,0 "$4\,\Omega$" v="$v_o$"
wire 6,3 -> 9,3
I1 9,3 -> 9,0 "$12\,\mathrm{A}$"
wire 0,0 -> 9,0
label 0,3 "$s$" above
label 3,3 "$1$" above
label 6,3 "$2$" above
ground 0,0
#@ inline
#@ view "120 V alone"
#@ straight off
#@ node s 120 "$s$: $120\,\mathrm{V}$"
#@ node n1 30 "node 1: $30\,\mathrm{V}$"
#@ node n2 20 "node 2: $20\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V s g "$120\,\mathrm{V}$" col=0 i="$15\,\mathrm{A}$" to=s id=eV1
#@ el R s n1 "$6\,\Omega$: falls $90\,\mathrm{V}$" col=1 i="$15\,\mathrm{A}$" to=n1 id=eR1
#@ el R n1 g2 "$3\,\Omega$: falls $30\,\mathrm{V}$" col=2 i="$10\,\mathrm{A}$" to=g2 id=eR3
#@ el R n1 n2 "$2\,\Omega$: falls $10\,\mathrm{V}$" col=3 i="$5\,\mathrm{A}$" to=n2 id=eR2
#@ el R n2 g3 "$4\,\Omega$: falls $20\,\mathrm{V}$" col=3 i="$5\,\mathrm{A}$" to=g3 id=eR4 plus=n2 v="$v_o$"
#@ step "Ground the bottom wire. The $12\,\mathrm{A}$ pump is off (a gap)."
#@ step "$2+4=6\,\Omega$ beside $3\,\Omega$: $2\,\Omega$; plus $6\,\Omega$: $8\,\Omega$. So $15\,\mathrm{A}$, and node 1 sits at $30\,\mathrm{V}$." show=n1,eR1,eV1
#@ step "$i_o'=\dfrac{30}{3}=10\,\mathrm{A}$; divider on the right: $v_o'=30\cdot\tfrac46=20\,\mathrm{V}$." show=n2,eR2,eR3,eR4
#@ view "12 A alone"
#@ straight off
#@ node s 24 "$s$ = bottom: $24\,\mathrm{V}$"
#@ node z0 24 "$s$ = bottom: $24\,\mathrm{V}$"
#@ node n1 12 "node 1: $12\,\mathrm{V}$"
#@ node g 0 "node 2: $0\,\mathrm{V}$" ground
#@ node g2 0 "node 2: $0\,\mathrm{V}$" ground
#@ node g3 0 "node 2: $0\,\mathrm{V}$" ground
#@ el W s z0 "$120\,\mathrm{V}$ off: a wire" col=0 i="$2\,\mathrm{A}$" to=s id=eV1
#@ el R s n1 "$6\,\Omega$: falls $12\,\mathrm{V}$" col=0 i="$2\,\mathrm{A}$" to=n1 id=eR1
#@ el R n1 z0 "$3\,\Omega$: falls $12\,\mathrm{V}$" col=1 i="$4\,\mathrm{A}$" to=n1 id=eR3
#@ el R n1 g "$2\,\Omega$: falls $12\,\mathrm{V}$" col=2 i="$6\,\mathrm{A}$" to=g id=eR2
#@ el R g2 z0 "$4\,\Omega$: falls $24\,\mathrm{V}$" col=3 i="$6\,\mathrm{A}$" to=g2 id=eR4 plus=g2 v="$v_o$"
#@ el I g3 z0 "$12\,\mathrm{A}$" col=4 i="$12\,\mathrm{A}$" to=z0 id=eI1
#@ step "Ground node 2, the lowest: the pump drags $12\,\mathrm{A}$ out of it. The $120\,\mathrm{V}$ step flattens to a wire."
#@ step "From node 2: $4\,\Omega$ beside $2+(6\parallel3)=4\,\Omega$, so $2\,\Omega$. Node 2 sits $24\,\mathrm{V}$ below the bottom wire: $v_o''=-24\,\mathrm{V}$." show=z0,eR4,eI1
#@ step "Node 1 sits halfway: $v_1''=-12\,\mathrm{V}$, so $i_o''=\dfrac{-12}{3}=-4\,\mathrm{A}$ (it flows **up** the $3\,\Omega$)." show=n1,eR1,eR2,eR3,eV1
#@ view "Both: add"
#@ straight off
#@ node s 124 "$s$: $124\,\mathrm{V}$"
#@ node n1 22 "node 1: $22\,\mathrm{V}$"
#@ node z0 4 "bottom: $4\,\mathrm{V}$"
#@ node g 0 "node 2: $0\,\mathrm{V}$" ground
#@ node g2 0 "node 2: $0\,\mathrm{V}$" ground
#@ node g3 0 "node 2: $0\,\mathrm{V}$" ground
#@ el V s z0 "$120\,\mathrm{V}$" col=0 i="$17\,\mathrm{A}$" to=s id=eV1
#@ el R s n1 "$6\,\Omega$: falls $102\,\mathrm{V}$" col=1 i="$17\,\mathrm{A}$" to=n1 id=eR1
#@ el R n1 z0 "$3\,\Omega$: falls $18\,\mathrm{V}$" col=2 i="$6\,\mathrm{A}$" to=z0 id=eR3
#@ el R g z0 "$4\,\Omega$: falls $4\,\mathrm{V}$" col=3 i="$1\,\mathrm{A}$" to=g id=eR4 plus=g v="$v_o$"
#@ el I g2 z0 "$12\,\mathrm{A}$" col=4 i="$12\,\mathrm{A}$" to=z0 id=eI1
#@ el R n1 g3 "$2\,\Omega$: falls $22\,\mathrm{V}$" col=5 i="$11\,\mathrm{A}$" to=g3 id=eR2
#@ step "Ground node 2 again. Add the voltages: $v_o=20-24=-4\,\mathrm{V}$, $i_o=10-4=6\,\mathrm{A}$." show=z0,n1,s
#@ step "Check: the $3\,\Omega$ falls $18\,\mathrm{V}$ ($6\,\mathrm{A}$) ✓. The $4\,\Omega$ absorbs $\dfrac{4^2}{4}=4\,\mathrm{W}$, not $100+144$." show=eR1,eR2,eR3,eR4,eV1,eI1
```

1. $120\,\mathrm{V}$ alone (pump open).

   $$i_s=\frac{120}{6+(3\parallel6)}=15\,\mathrm{A},\quad v_1'=30,\quad i_o'=10\,\mathrm{A},\quad v_o'=20\,\mathrm{V}$$
2. $12\,\mathrm{A}$ alone (source shorted).

   $$v_o''=-12\,(4\parallel4)=-24\,\mathrm{V},\quad v_1''=-12,\quad i_o''=-4\,\mathrm{A}$$
3. Add.

   $$v_o=20-24=-4\,\mathrm{V},\qquad i_o=10-4=6\,\mathrm{A}$$

**Answer:** $v_o=-4\,\mathrm{V}$, $i_o=6\,\mathrm{A}$.

**Example: Example 9 · Dependent sources stay on (Lecture 5)**

Use superposition on the two independent sources to find $v_o$. The pump is $0.4v_\Delta$ (A/V) and the rod is $2i_\Delta$ (Ω).

```schematic
V1 0,3 -> 0,0 "$10\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$" i="$i_\Delta$"
R2 3,3 -> 3,0 "$20\,\Omega$" v="$v_o$"
G1 6,3 -> 3,3 "$0.4v_\Delta$"
R3 6,3 -> 6,0 "$10\,\Omega$" v="$v_\Delta$"
E1 6,0 -> 3,0 "$2i_\Delta$"
I1 9,0 -> 9,3 "$5\,\mathrm{A}$"
wire 6,3 -> 9,3
wire 6,0 -> 9,0
wire 0,0 -> 3,0
label 0,3 "$s$" above
label 3,3 "$a$" above
label 6,3 "$d$" above
label 6,0 "$c$" below
ground 3,0
#@ inline
#@ view "10 V alone"
#@ straight off
#@ node s 10 "$s$: $10\,\mathrm{V}$"
#@ node a 8 "$a$: $8\,\mathrm{V}$"
#@ node d 0.8 "$d$ = $c$: $0.8\,\mathrm{V}$"
#@ node c 0.8 "$d$ = $c$: $0.8\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V s g "$10\,\mathrm{V}$" col=0 i="$0.4\,\mathrm{A}$" to=s id=eV1
#@ el R s a "$5\,\Omega$: falls $2\,\mathrm{V}$" col=1 i="$0.4\,\mathrm{A}$" to=a id=eR1
#@ el R a g2 "$20\,\Omega$: falls $8\,\mathrm{V}$" col=1 i="$0.4\,\mathrm{A}$" to=g2 id=eR2 plus=a v="$v_o$"
#@ el G d a "$0.4v_\Delta$: $0\,\mathrm{A}$" col=2 id=eG1
#@ el R d c "$10\,\Omega$: no fall" col=3 id=eR3 plus=d v="$v_\Delta$"
#@ el E c g3 "$2i_\Delta$: $0.8\,\mathrm{V}$" col=4 id=eE1
#@ step "Ground the bottom wire. The $5\,\mathrm{A}$ pump is off (a gap); both diamonds stay on."
#@ step "KCL at $d$: nothing comes in, so $0.4v_\Delta'+\dfrac{v_\Delta'}{10}=0$: $v_\Delta'=0$. The diamond pump is off **because its control is zero**." show=eG1,eR3
#@ step "The left side is a plain divider: $v_o'=10\cdot\tfrac{20}{25}=8\,\mathrm{V}$. ($i_\Delta=0.4\,\mathrm{A}$, so the rod still lifts $c$ and $d$ to $0.8\,\mathrm{V}$.)" show=a,c,d,eR1,eR2,eE1
#@ view "5 A alone"
#@ straight off
#@ node a 22.4 "$a$: $22.4\,\mathrm{V}$"
#@ node d 10 "$d$: $10\,\mathrm{V}$"
#@ node s 6.4 "$s$ = bottom: $6.4\,\mathrm{V}$"
#@ node z0 6.4 "$s$ = bottom: $6.4\,\mathrm{V}$"
#@ node g 0 "$c$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$c$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$c$: $0\,\mathrm{V}$" ground
#@ el R s a "$5\,\Omega$: falls $16\,\mathrm{V}$" col=0 i="$3.2\,\mathrm{A}$" to=s id=eR1
#@ el W s z0 "$10\,\mathrm{V}$ off: a wire" col=0 i="$3.2\,\mathrm{A}$" to=z0 id=eV1
#@ el R a z0 "$20\,\Omega$: falls $16\,\mathrm{V}$" col=1 i="$0.8\,\mathrm{A}$" to=z0 id=eR2 plus=a v="$v_o$"
#@ el G d a "$0.4v_\Delta$: $4\,\mathrm{A}$" col=2 i="$4\,\mathrm{A}$" to=a id=eG1
#@ el R d g "$10\,\Omega$: falls $10\,\mathrm{V}$" col=3 i="$1\,\mathrm{A}$" to=g id=eR3 plus=d v="$v_\Delta$"
#@ el I g2 d "$5\,\mathrm{A}$" col=4 i="$5\,\mathrm{A}$" to=d id=eI1
#@ el E g3 z0 "$2i_\Delta$: $-6.4\,\mathrm{V}$" col=5 i="$4\,\mathrm{A}$" to=g3 id=eE1
#@ step "Ground $c$, the lowest node; $v_o$ is $a$'s height minus the bottom wire's. The $10\,\mathrm{V}$ step flattens to a wire."
#@ step "KCL at $d$: $5=0.4v_\Delta''+\dfrac{v_\Delta''}{10}$, so $v_\Delta''=10\,\mathrm{V}$ and the diamond pushes $4\,\mathrm{A}$ into $a$." show=d,eG1,eR3,eI1
#@ step "$a$ sees $5\parallel20=4\,\Omega$ down to the bottom wire: $v_o''=(4)(4)=16\,\mathrm{V}$." show=a,eR1,eR2,eV1,eE1
#@ view "Both: add"
#@ straight off
#@ node a 29.6 "$a$: $29.6\,\mathrm{V}$"
#@ node s 15.6 "$s$: $15.6\,\mathrm{V}$"
#@ node d 10 "$d$: $10\,\mathrm{V}$"
#@ node z0 5.6 "bottom: $5.6\,\mathrm{V}$"
#@ node g 0 "$c$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$c$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$c$: $0\,\mathrm{V}$" ground
#@ el R s a "$5\,\Omega$: falls $14\,\mathrm{V}$" col=0 i="$2.8\,\mathrm{A}$" to=s id=eR1
#@ el V s z0 "$10\,\mathrm{V}$" col=0 i="$2.8\,\mathrm{A}$" to=z0 id=eV1
#@ el E g z0 "$2i_\Delta$: $-5.6\,\mathrm{V}$" col=0 i="$4\,\mathrm{A}$" to=g id=eE1
#@ el R a z0 "$20\,\Omega$: falls $24\,\mathrm{V}$" col=1 i="$1.2\,\mathrm{A}$" to=z0 id=eR2 plus=a v="$v_o$"
#@ el G d a "$0.4v_\Delta$: $4\,\mathrm{A}$" col=2 i="$4\,\mathrm{A}$" to=a id=eG1
#@ el R d g2 "$10\,\Omega$: falls $10\,\mathrm{V}$" col=3 i="$1\,\mathrm{A}$" to=g2 id=eR3 plus=d v="$v_\Delta$"
#@ el I g3 d "$5\,\mathrm{A}$" col=4 i="$5\,\mathrm{A}$" to=d id=eI1
#@ step "Ground $c$. Add: $v_o=8+16=24\,\mathrm{V}$: $a$ sits $24\,\mathrm{V}$ above the bottom wire ✓." show=a,s,z0
```

1. $10\,\mathrm{V}$ alone: KCL at $d$ forces $v_\Delta'=0$; divider on the left.

   $$v_o'=10\cdot\frac{20}{25}=8\,\mathrm{V}$$
2. $5\,\mathrm{A}$ alone: KCL at $d$, then $a$.

   $$5=0.4v_\Delta''+\frac{v_\Delta''}{10}\Rightarrow v_\Delta''=10,\quad v_o''=4\,(5\parallel20)=16\,\mathrm{V}$$
3. Add.

   $$v_o=8+16=24\,\mathrm{V}$$

**Answer:** $v_o=24\,\mathrm{V}$

**Problem: Try it 9 · Three sources (Textbook P4.94)** (intermediate)

Use superposition to find $i_o$.

```schematic
I1 0,0 -> 0,4 "$6\,\mathrm{A}$"
wire 0,4 -> 2,4
R1 2,4 -> 2,0 "$20\,\Omega$"
R2 2,4 -> 5,4 "$1\,\Omega$" i="$i_o$"
I2 5,4 -> 5,0 "$10\,\mathrm{A}$"
wire 5,4 -> 11,4
R3 7,4 -> 7,0 "$60\,\Omega$"
R4 9,4 -> 9,2 "$5\,\Omega$"
V1 9,2 -> 9,0 "$75\,\mathrm{V}$"
R5 11,4 -> 11,0 "$30\,\Omega$"
wire 0,0 -> 11,0
label 2,4 "$p$" above
label 5,4 "$q$" above
label 9,2 "$k$" right
ground 0,0
#@ spoiler
#@ view "6 A alone"
#@ straight off
#@ node p 24 "$p$: $24\,\mathrm{V}$"
#@ node q 19.2 "$q$: $19.2\,\mathrm{V}$"
#@ node k 0 "$k$ = bottom: $0\,\mathrm{V}$"
#@ node g 0 "$k$ = bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "$k$ = bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "$k$ = bottom: $0\,\mathrm{V}$" ground
#@ node g4 0 "$k$ = bottom: $0\,\mathrm{V}$" ground
#@ node g5 0 "$k$ = bottom: $0\,\mathrm{V}$" ground
#@ el I g p "$6\,\mathrm{A}$" col=0 i="$6\,\mathrm{A}$" to=p id=eI1
#@ el R p g2 "$20\,\Omega$: falls $24\,\mathrm{V}$" col=1 i="$1.2\,\mathrm{A}$" to=g2 id=eR1
#@ el R p q "$1\,\Omega$: falls $4.8\,\mathrm{V}$" col=2 i="$4.8\,\mathrm{A}$" to=q id=eR2
#@ el R q g3 "$60\,\Omega$: falls $19.2\,\mathrm{V}$" col=3 i="$0.32\,\mathrm{A}$" to=g3 id=eR3
#@ el R q k "$5\,\Omega$: falls $19.2\,\mathrm{V}$" col=4 i="$3.84\,\mathrm{A}$" to=k id=eR4
#@ el W k g4 "$75\,\mathrm{V}$ off: a wire" col=4 i="$3.84\,\mathrm{A}$" to=g4 id=eV1
#@ el R q g5 "$30\,\Omega$: falls $19.2\,\mathrm{V}$" col=5 i="$0.64\,\mathrm{A}$" to=g5 id=eR5
#@ step "Ground the bottom wire. $10\,\mathrm{A}$ off (gap), $75\,\mathrm{V}$ → wire. Right side: $60\parallel5\parallel30=4\,\Omega$."
#@ step "Divider of currents: $20\,\Omega$ vs $1+4=5\,\Omega$. $i_o'=6\cdot\tfrac{20}{25}=4.8\,\mathrm{A}$." show=eR2,p,q,eR1,eR3,eR4,eR5,eV1
#@ view "10 A alone"
#@ straight off
#@ node z0 33.6 "bottom = $k$: $33.6\,\mathrm{V}$"
#@ node k 33.6 "bottom = $k$: $33.6\,\mathrm{V}$"
#@ node p 1.6 "$p$: $1.6\,\mathrm{V}$"
#@ node g 0 "$q$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$q$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$q$: $0\,\mathrm{V}$" ground
#@ node g4 0 "$q$: $0\,\mathrm{V}$" ground
#@ node g5 0 "$q$: $0\,\mathrm{V}$" ground
#@ el R p z0 "$20\,\Omega$: falls $32\,\mathrm{V}$" col=0 i="$1.6\,\mathrm{A}$" to=p id=eR1
#@ el R p g "$1\,\Omega$: falls $1.6\,\mathrm{V}$" col=0 i="$1.6\,\mathrm{A}$" to=g id=eR2
#@ el I g2 z0 "$10\,\mathrm{A}$" col=1 i="$10\,\mathrm{A}$" to=z0 id=eI2
#@ el R g3 z0 "$60\,\Omega$: falls $33.6\,\mathrm{V}$" col=2 i="$0.56\,\mathrm{A}$" to=g3 id=eR3
#@ el R g4 k "$5\,\Omega$: falls $33.6\,\mathrm{V}$" col=3 i="$6.72\,\mathrm{A}$" to=g4 id=eR4
#@ el W k z0 "$75\,\mathrm{V}$ off: a wire" col=3 i="$6.72\,\mathrm{A}$" to=k id=eV1
#@ el R g5 z0 "$30\,\Omega$: falls $33.6\,\mathrm{V}$" col=4 i="$1.12\,\mathrm{A}$" to=g5 id=eR5
#@ step "Ground $q$, the lowest: the pump drags $10\,\mathrm{A}$ out of it. Its $10\,\mathrm{A}$ comes back via $4\,\Omega$ (right) or $1+20=21\,\Omega$ (left)."
#@ step "Left share: $10\cdot\tfrac{4}{25}=1.6\,\mathrm{A}$, falling $p\to q$ through the $1\,\Omega$: $i_o''=+1.6\,\mathrm{A}$." show=eR2,p,eR1,eR3,eR4,eR5,eV1
#@ view "75 V alone"
#@ straight off
#@ node k 75 "$k$: $75\,\mathrm{V}$"
#@ node q 50.4 "$q$: $50.4\,\mathrm{V}$"
#@ node p 48 "$p$: $48\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g4 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V k g "$75\,\mathrm{V}$" col=0 i="$4.92\,\mathrm{A}$" to=k id=eV1
#@ el R q k "$5\,\Omega$: falls $24.6\,\mathrm{V}$" col=1 i="$4.92\,\mathrm{A}$" to=q id=eR4
#@ el R p q "$1\,\Omega$: falls $2.4\,\mathrm{V}$" col=1 i="$2.4\,\mathrm{A}$" to=p id=eR2
#@ el R p g2 "$20\,\Omega$: falls $48\,\mathrm{V}$" col=1 i="$2.4\,\mathrm{A}$" to=g2 id=eR1
#@ el R q g3 "$60\,\Omega$: falls $50.4\,\mathrm{V}$" col=2 i="$0.84\,\mathrm{A}$" to=g3 id=eR3
#@ el R q g4 "$30\,\Omega$: falls $50.4\,\mathrm{V}$" col=3 i="$1.68\,\mathrm{A}$" to=g4 id=eR5
#@ step "Ground the bottom wire; both pumps off. Node $q$: $\dfrac{q-75}{5}+\dfrac{q}{60}+\dfrac{q}{30}+\dfrac{q}{21}=0$, so $q=50.4\,\mathrm{V}$." show=q
#@ step "Current runs $q\to p$ through $1+20\,\Omega$: $\dfrac{50.4}{21}=2.4\,\mathrm{A}$, against $i_o$: $i_o'''=-2.4\,\mathrm{A}$." show=p,eR1,eR2,eR3,eR4,eR5
#@ view "All three: add"
#@ straight off
#@ node k 75 "$k$: $75\,\mathrm{V}$"
#@ node p 40 "$p$: $40\,\mathrm{V}$"
#@ node q 36 "$q$: $36\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g4 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g5 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g6 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V k g "$75\,\mathrm{V}$" col=0 i="$7.8\,\mathrm{A}$" to=k id=eV1
#@ el R q k "$5\,\Omega$: falls $39\,\mathrm{V}$" col=1 i="$7.8\,\mathrm{A}$" to=q id=eR4
#@ el R q g2 "$30\,\Omega$: falls $36\,\mathrm{V}$" col=1 i="$1.2\,\mathrm{A}$" to=g2 id=eR5
#@ el I g3 p "$6\,\mathrm{A}$" col=2 i="$6\,\mathrm{A}$" to=p id=eI1
#@ el R p q "$1\,\Omega$: falls $4\,\mathrm{V}$" col=3 i="$4\,\mathrm{A}$" to=q id=eR2
#@ el R q g4 "$60\,\Omega$: falls $36\,\mathrm{V}$" col=3 i="$0.6\,\mathrm{A}$" to=g4 id=eR3
#@ el R p g5 "$20\,\Omega$: falls $40\,\mathrm{V}$" col=4 i="$2\,\mathrm{A}$" to=g5 id=eR1
#@ el I q g6 "$10\,\mathrm{A}$" col=5 i="$10\,\mathrm{A}$" to=g6 id=eI2
#@ step "Ground the bottom wire. Add: $i_o=4.8+1.6-2.4=4\,\mathrm{A}$. Check: $p=40$, $q=36\,\mathrm{V}$, the $1\,\Omega$ falls $4\,\mathrm{V}$ ✓." show=p,q,eR2
```

<details><summary>Solution</summary>

1. $6\,\mathrm{A}$ alone.

   $$i_o'=6\cdot\frac{20}{20+(1+4)}=4.8\,\mathrm{A}$$
2. $10\,\mathrm{A}$ alone.

   $$i_o''=10\cdot\frac{4}{4+21}=1.6\,\mathrm{A}$$
3. $75\,\mathrm{V}$ alone.

   $$\frac{v-75}{5}+\frac{v}{60}+\frac{v}{30}+\frac{v}{21}=0\Rightarrow v=50.4,\;\;i_o'''=-\frac{50.4}{21}=-2.4\,\mathrm{A}$$
4. Add.

   $$i_o=4.8+1.6-2.4=4\,\mathrm{A}$$

**Answer:** $i_o=4\,\mathrm{A}$ ($4.8$, $1.6$, $-2.4$).

</details>

**Problem: Try it 10 · Adding one more source (Textbook P4.96)** (intermediate)

Before the $5\,\mathrm{mA}$ source is attached between $a$ and $b$, $i_o=3.5\,\mathrm{mA}$. **(a)** Use superposition to find $i_o$ after it is attached. **(b)** Check with all three sources on.

```schematic
V1 0,3 -> 0,0 "$8\,\mathrm{V}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$5\,\mathrm{k\Omega}$"
R2 3,3 -> 6,3 "$2\,\mathrm{k\Omega}$"
R3 6,3 -> 6,0 "$6\,\mathrm{k\Omega}$" i="$i_o$"
wire 6,3 -> 9,3
I1 9,0 -> 9,3 "$10\,\mathrm{mA}$"
wire 3,3 -> 3,5
I2 6,5 -> 3,5 "$5\,\mathrm{mA}$"
wire 6,5 -> 6,3
wire 0,0 -> 9,0
label 3,3 "$a$" below
label 6,3 "$b$" below
ground 0,0
#@ spoiler
#@ view "Before: 8 V and 10 mA"
#@ straight off
#@ node b 21 "$b$: $21\,\mathrm{V}$"
#@ node a 8 "$a$: $8\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g4 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V a g "$8\,\mathrm{V}$" col=0 i="$4.9\,\mathrm{mA}$" to=g id=eV1
#@ el R a g2 "$5\,\mathrm{k\Omega}$: falls $8\,\mathrm{V}$" col=1 i="$1.6\,\mathrm{mA}$" to=g2 id=eR1
#@ el R a b "$2\,\mathrm{k\Omega}$: falls $13\,\mathrm{V}$" col=2 i="$6.5\,\mathrm{mA}$" to=a id=eR2
#@ el R b g3 "$6\,\mathrm{k\Omega}$: falls $21\,\mathrm{V}$" col=3 i="$3.5\,\mathrm{mA}$" to=g3 id=eR3
#@ el I g4 b "$10\,\mathrm{mA}$" col=4 i="$10\,\mathrm{mA}$" to=b id=eI1
#@ step "Ground the bottom wire. The $8\,\mathrm{V}$ source fixes $a=8\,\mathrm{V}$."
#@ step "KCL at $b$: $\dfrac{b-8}{2}+\dfrac{b}{6}=10$, so $b=21\,\mathrm{V}$ and $i_o=\dfrac{21}{6}=3.5\,\mathrm{mA}$ ✓ (given)." show=b,eR2,eR3,eI1
#@ view "5 mA alone"
#@ straight off
#@ node a 7.5 "$a$ = bottom: $7.5\,\mathrm{V}$"
#@ node z0 7.5 "$a$ = bottom: $7.5\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el I g a "$5\,\mathrm{mA}$" col=0 i="$5\,\mathrm{mA}$" to=a id=eI2
#@ el R a g2 "$2\,\mathrm{k\Omega}$: falls $7.5\,\mathrm{V}$" col=1 i="$3.75\,\mathrm{mA}$" to=g2 id=eR2
#@ el W a z0 "$8\,\mathrm{V}$ off: a wire" col=1 i="$1.25\,\mathrm{mA}$" to=z0 id=eV1
#@ el R g3 z0 "$6\,\mathrm{k\Omega}$: falls $7.5\,\mathrm{V}$" col=2 i="$1.25\,\mathrm{mA}$" to=g3 id=eR3
#@ step "Ground $b$, the lowest: the new pump moves $5\,\mathrm{mA}$ from $b$ to $a$."
#@ step "From $b$ the pump sees $2\parallel6=1.5\,\mathrm{k\Omega}$: $b$ sits $7.5\,\mathrm{V}$ below the bottom wire, so $i_o''=-\dfrac{7.5}{6}=-1.25\,\mathrm{mA}$." show=a,z0,eR2,eR3,eV1
#@ note "$8\,\mathrm{V}$ → wire, so the $5\,\mathrm{k\Omega}$ has no fall (left out); $10\,\mathrm{mA}$ → gap."
#@ view "All three"
#@ straight off
#@ node b 13.5 "$b$: $13.5\,\mathrm{V}$"
#@ node a 8 "$a$: $8\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g4 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V a g "$8\,\mathrm{V}$" col=0 i="$6.15\,\mathrm{mA}$" to=g id=eV1
#@ el R a g2 "$5\,\mathrm{k\Omega}$: falls $8\,\mathrm{V}$" col=1 i="$1.6\,\mathrm{mA}$" to=g2 id=eR1
#@ el R a b "$2\,\mathrm{k\Omega}$: falls $5.5\,\mathrm{V}$" col=2 i="$2.75\,\mathrm{mA}$" to=a id=eR2
#@ el I b a "$5\,\mathrm{mA}$" col=3 i="$5\,\mathrm{mA}$" to=a id=eI2
#@ el R b g3 "$6\,\mathrm{k\Omega}$: falls $13.5\,\mathrm{V}$" col=4 i="$2.25\,\mathrm{mA}$" to=g3 id=eR3
#@ el I g4 b "$10\,\mathrm{mA}$" col=5 i="$10\,\mathrm{mA}$" to=b id=eI1
#@ step "Ground the bottom wire. Add: $i_o=3.5-1.25=2.25\,\mathrm{mA}$. Check: $b=13.5\,\mathrm{V}$, $\dfrac{13.5}{6}=2.25\,\mathrm{mA}$ ✓. The new pump carries its current **down** from $b$ to $a$: it absorbs." show=b,eR3,eR2,eI2
```

<details><summary>Solution</summary>

1. The new source alone ($8\,\mathrm{V}$ shorted, $10\,\mathrm{mA}$ open).

   $$i_o''=-5\cdot\frac{2}{2+6}=-1.25\,\mathrm{mA}$$
2. Add to the old answer.

   $$i_o=3.5-1.25=2.25\,\mathrm{mA}$$
3. Check: KCL at $b$ with all three.

   $$\frac{v_b-8}{2}+\frac{v_b}{6}+5=10\;\Rightarrow\;v_b=13.5\,\mathrm{V},\;\;i_o=2.25\,\mathrm{mA}$$

**Answer:** $i_o=2.25\,\mathrm{mA}$

</details>

**Problem: Try it 11 · A battery and a pump (Textbook P4.95)** (intermediate)

Use superposition to find $i_o$ and $v_o$.

```schematic
V1 0,3 -> 0,0 "$180\,\mathrm{V}$" i_rev="$i_o$"
R1 0,3 -> 3,3 "$30\,\Omega$"
R2 3,3 -> 3,0 "$60\,\Omega$"
I1 6,3 -> 3,3 "$7.5\,\mathrm{A}$"
R3 6,3 -> 6,0 "$80\,\Omega$" v="$v_o$"
R4 6,3 -> 9,3 "$20\,\Omega$"
R5 9,3 -> 9,0 "$25\,\Omega$"
wire 0,3 -> 0,5
R6 0,5 -> 9,5 "$40\,\Omega$"
wire 9,5 -> 9,3
wire 0,0 -> 9,0
label 3,3 "$p$" below
label 6,3 "$q$" below
label 9,3 "$r$" right
ground 0,0
#@ spoiler
#@ view "180 V alone"
#@ straight off
#@ node s 180 "$s$: $180\,\mathrm{V}$"
#@ node p 120 "$p$: $120\,\mathrm{V}$"
#@ node r 60 "$r$: $60\,\mathrm{V}$"
#@ node q 48 "$q$: $48\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g4 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V s g "$180\,\mathrm{V}$" col=0 i="$5\,\mathrm{A}$" to=s id=eV1
#@ el R s p "$30\,\Omega$: falls $60\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=p id=eR1
#@ el R p g2 "$60\,\Omega$: falls $120\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=g2 id=eR2
#@ el R s r "$40\,\Omega$: falls $120\,\mathrm{V}$" col=2 i="$3\,\mathrm{A}$" to=r id=eR6
#@ el R q r "$20\,\Omega$: falls $12\,\mathrm{V}$" col=3 i="$0.6\,\mathrm{A}$" to=q id=eR4
#@ el R q g3 "$80\,\Omega$: falls $48\,\mathrm{V}$" col=3 i="$0.6\,\mathrm{A}$" to=g3 id=eR3 plus=q v="$v_o$"
#@ el R r g4 "$25\,\Omega$: falls $60\,\mathrm{V}$" col=4 i="$2.4\,\mathrm{A}$" to=g4 id=eR5
#@ step "Ground the bottom wire. The $7.5\,\mathrm{A}$ pump is off (a gap, left out). The battery lifts $s$ to $180\,\mathrm{V}$."
#@ step "In = out at $q$ and $r$ (and $p$ is a plain divider, $120\,\mathrm{V}$): $q=48$, $r=60\,\mathrm{V}$. So $v_o'=48\,\mathrm{V}$ and the battery sends $i_o'=5\,\mathrm{A}$." show=p,q,r,eR1,eR2,eR3,eR4,eR5,eR6,eV1
#@ view "7.5 A alone"
#@ straight off
#@ node p 334 "$p$: $334\,\mathrm{V}$"
#@ node s 184 "$s$ = bottom: $184\,\mathrm{V}$"
#@ node z0 184 "$s$ = bottom: $184\,\mathrm{V}$"
#@ node r 104 "$r$: $104\,\mathrm{V}$"
#@ node g 0 "$q$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$q$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$q$: $0\,\mathrm{V}$" ground
#@ el I g p "$7.5\,\mathrm{A}$" col=0 i="$7.5\,\mathrm{A}$" to=p id=eI1
#@ el R s p "$30\,\Omega$: falls $150\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=s id=eR1
#@ el W s z0 "$180\,\mathrm{V}$ off: a wire" col=1 i="$3\,\mathrm{A}$" to=z0 id=eV1
#@ el R p z0 "$60\,\Omega$: falls $150\,\mathrm{V}$" col=2 i="$2.5\,\mathrm{A}$" to=z0 id=eR2
#@ el R s r "$40\,\Omega$: falls $80\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=r id=eR6
#@ el R r z0 "$25\,\Omega$: falls $80\,\mathrm{V}$" col=3 i="$3.2\,\mathrm{A}$" to=r id=eR5
#@ el R g2 r "$20\,\Omega$: falls $104\,\mathrm{V}$" col=3 i="$5.2\,\mathrm{A}$" to=g2 id=eR4
#@ el R g3 z0 "$80\,\Omega$: falls $184\,\mathrm{V}$" col=4 i="$2.3\,\mathrm{A}$" to=g3 id=eR3 plus=g3 v="$v_o$"
#@ step "Ground $q$, the lowest wire: the pump pulls its $7.5\,\mathrm{A}$ out of $q$. The battery → wire."
#@ step "In = out (from the bottom wire): $q=-184$, $p=150$, $r=-80\,\mathrm{V}$. So $v_o''=-184\,\mathrm{V}$, and $3\,\mathrm{A}$ flows **down** through the battery's spot: $i_o''=-3\,\mathrm{A}$." show=p,r,s,eR1,eR2,eR3,eR4,eR5,eR6,eV1,eI1
#@ view "Both: add"
#@ straight off
#@ node p 406 "$p$: $406\,\mathrm{V}$"
#@ node s 316 "$s$: $316\,\mathrm{V}$"
#@ node z0 136 "bottom: $136\,\mathrm{V}$"
#@ node r 116 "$r$: $116\,\mathrm{V}$"
#@ node g 0 "$q$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$q$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$q$: $0\,\mathrm{V}$" ground
#@ el I g p "$7.5\,\mathrm{A}$" col=0 i="$7.5\,\mathrm{A}$" to=p id=eI1
#@ el R s p "$30\,\Omega$: falls $90\,\mathrm{V}$" col=1 i="$3\,\mathrm{A}$" to=s id=eR1
#@ el V s z0 "$180\,\mathrm{V}$" col=1 i="$2\,\mathrm{A}$" to=s id=eV1
#@ el R r z0 "$25\,\Omega$: falls $20\,\mathrm{V}$" col=1 i="$0.8\,\mathrm{A}$" to=r id=eR5
#@ el R g2 r "$20\,\Omega$: falls $116\,\mathrm{V}$" col=1 i="$5.8\,\mathrm{A}$" to=g2 id=eR4
#@ el R s r "$40\,\Omega$: falls $200\,\mathrm{V}$" col=2 i="$5\,\mathrm{A}$" to=r id=eR6
#@ el R p z0 "$60\,\Omega$: falls $270\,\mathrm{V}$" col=3 i="$4.5\,\mathrm{A}$" to=z0 id=eR2
#@ el R g3 z0 "$80\,\Omega$: falls $136\,\mathrm{V}$" col=4 i="$1.7\,\mathrm{A}$" to=g3 id=eR3 plus=g3 v="$v_o$"
#@ step "Ground $q$ again. Add: $v_o=48-184=-136\,\mathrm{V}$, $i_o=5-3=2\,\mathrm{A}$ (climbing through the battery)." show=eV1,z0
```

<details><summary>Solution</summary>

1. $180\,\mathrm{V}$ alone (pump open): node equations at $q$ and $r$.

   $$v_o'=48\,\mathrm{V},\qquad i_o'=5\,\mathrm{A}$$
2. $7.5\,\mathrm{A}$ alone (battery shorted).

   $$v_o''=-184\,\mathrm{V},\qquad i_o''=-3\,\mathrm{A}$$
3. Add.

   $$v_o=48-184=-136\,\mathrm{V},\qquad i_o=5-3=2\,\mathrm{A}$$

**Answer:** $i_o=2\,\mathrm{A}$, $v_o=-136\,\mathrm{V}$

</details>

## Practice set

Exam-style, mixing all three topics. Try each for 10–15 minutes before opening the solution, then check your picture against the height view.

**Problem: Textbook P4.93 · A hidden balanced bridge** (advanced)

Use superposition to find $i_o$, the current in the $45\,\mathrm{V}$ source.

```schematic
V1 0,5 -> 0,2 "$45\,\mathrm{V}$" i_rev="$i_o$"
wire 0,5 -> 1,5
R1 1,5 -> 4,5 "$5\,\Omega$"
R2 4,5 -> 7,5 "$10\,\Omega$"
wire 7,5 -> 8,5
V2 8,5 -> 8,2 "$10\,\mathrm{V}$"
R3 4,5 -> 4,2 "$40\,\Omega$"
wire 0,2 -> 1,2
R4 1,2 -> 4,2 "$15\,\Omega$"
R5 4,2 -> 7,2 "$30\,\Omega$"
wire 7,2 -> 8,2
wire 0,2 -> 0,0 -> 3,0
I1 5,0 -> 3,0 "$8\,\mathrm{A}$"
wire 5,0 -> 8,0 -> 8,2
label 1,5 "$p$" above
label 4,5 "$m$" above
label 7,5 "$n$" above
label 4,2 "$k$" below
label 8,2 "$r$" right
ground 0,0
#@ spoiler
#@ view "45 V alone"
#@ straight off
#@ node p 45 "$p$: $45\,\mathrm{V}$"
#@ node m 39.37 "$m$: $39.37\,\mathrm{V}$"
#@ node n 33.75 "$n$ = $r$: $33.75\,\mathrm{V}$"
#@ node r 33.75 "$n$ = $r$: $33.75\,\mathrm{V}$"
#@ node k 16.88 "$k$: $16.88\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V p g "$45\,\mathrm{V}$" col=0 i="$1.125\,\mathrm{A}$" to=p id=eV1
#@ el R p m "$5\,\Omega$: falls $5.63\,\mathrm{V}$" col=1 i="$1.125\,\mathrm{A}$" to=m id=eR1
#@ el R m n "$10\,\Omega$: falls $5.62\,\mathrm{V}$" col=1 i="$0.5625\,\mathrm{A}$" to=n id=eR2
#@ el W n r "$10\,\mathrm{V}$ off: a wire" col=2 i="$0.5625\,\mathrm{A}$" to=r id=eV2
#@ el R k r "$30\,\Omega$: falls $16.88\,\mathrm{V}$" col=4 i="$0.5625\,\mathrm{A}$" to=k id=eR5
#@ el R g2 k "$15\,\Omega$: falls $16.88\,\mathrm{V}$" col=4 i="$1.125\,\mathrm{A}$" to=g2 id=eR4
#@ el R m k "$40\,\Omega$: falls $22.5\,\mathrm{V}$" col=5 i="$0.5625\,\mathrm{A}$" to=k id=eR3
#@ step "Ground the bottom-left wire. $10\,\mathrm{V}$ → wire, $8\,\mathrm{A}$ → gap."
#@ step "$10+30=40\,\Omega$ beside $40\,\Omega$: $20\,\Omega$; plus $5+15$: $40\,\Omega$. So $i_o'=\dfrac{45}{40}=1.125\,\mathrm{A}$." show=m,n,r,k,eV1,eR1,eR2,eR3,eR4,eR5,eV2
#@ view "10 V alone"
#@ straight off
#@ node n 10 "$n$: $10\,\mathrm{V}$"
#@ node m 8.12 "$m$: $8.12\,\mathrm{V}$"
#@ node p 7.5 "$p$ = bottom: $7.5\,\mathrm{V}$"
#@ node z0 7.5 "$p$ = bottom: $7.5\,\mathrm{V}$"
#@ node k 5.62 "$k$: $5.62\,\mathrm{V}$"
#@ node g 0 "$r$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$r$: $0\,\mathrm{V}$" ground
#@ el V n g "$10\,\mathrm{V}$" col=0 i="$0.1875\,\mathrm{A}$" to=n id=eV2
#@ el R m n "$10\,\Omega$: falls $1.88\,\mathrm{V}$" col=1 i="$0.1875\,\mathrm{A}$" to=m id=eR2
#@ el R p m "$5\,\Omega$: falls $0.625\,\mathrm{V}$" col=1 i="$0.125\,\mathrm{A}$" to=p id=eR1
#@ el W p z0 "$45\,\mathrm{V}$ off: a wire" col=2 i="$0.125\,\mathrm{A}$" to=z0 id=eV1
#@ el R z0 k "$15\,\Omega$: falls $1.88\,\mathrm{V}$" col=4 i="$0.125\,\mathrm{A}$" to=k id=eR4
#@ el R k g2 "$30\,\Omega$: falls $5.62\,\mathrm{V}$" col=4 i="$0.1875\,\mathrm{A}$" to=g2 id=eR5
#@ el R m k "$40\,\Omega$: falls $2.5\,\mathrm{V}$" col=5 i="$0.0625\,\mathrm{A}$" to=k id=eR3
#@ step "Ground $r$, the lowest. $45\,\mathrm{V}$ → wire, $8\,\mathrm{A}$ → gap."
#@ step "The $10\,\mathrm{V}$ source sees $10+\big(40\parallel(5+15)\big)+30=53.3\,\Omega$: $0.1875\,\mathrm{A}$. Its share through the $5\,\Omega$, $0.125\,\mathrm{A}$, flows **down** the shorted $45\,\mathrm{V}$ spot: $i_o''=-0.125\,\mathrm{A}$." show=m,k,p,eV2,eR1,eR2,eR3,eR4,eR5,eV1
#@ view "8 A alone"
#@ straight off
#@ node p 90 "$p$ = bottom: $90\,\mathrm{V}$"
#@ node z0 90 "$p$ = bottom: $90\,\mathrm{V}$"
#@ node m 60 "$m$ = $k$: $60\,\mathrm{V}$"
#@ node k 60 "$m$ = $k$: $60\,\mathrm{V}$"
#@ node n 0 "$n$ = $r$: $0\,\mathrm{V}$"
#@ node g 0 "$n$ = $r$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$n$ = $r$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$n$ = $r$: $0\,\mathrm{V}$" ground
#@ el R p m "$5\,\Omega$: falls $30\,\mathrm{V}$" col=1 i="$6\,\mathrm{A}$" to=m id=eR1
#@ el R m n "$10\,\Omega$: falls $60\,\mathrm{V}$" col=1 i="$6\,\mathrm{A}$" to=n id=eR2
#@ el R z0 k "$15\,\Omega$: falls $30\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=k id=eR4
#@ el R k g "$30\,\Omega$: falls $60\,\mathrm{V}$" col=2 i="$2\,\mathrm{A}$" to=g id=eR5
#@ el W p z0 "$45\,\mathrm{V}$ off: a wire" col=1 i="$6\,\mathrm{A}$" to=p id=eV1
#@ el R m k "$40\,\Omega$: no fall" col=1 id=eR3
#@ el W n g2 "$10\,\mathrm{V}$ off: a wire" col=1 i="$6\,\mathrm{A}$" to=g2 id=eV2
#@ el I g3 z0 "$8\,\mathrm{A}$" col=3 i="$8\,\mathrm{A}$" to=z0 id=eI1
#@ step "Ground $r$ (and $n$: the $10\,\mathrm{V}$ is now a wire). Both voltage sources flatten."
#@ step "Bridge check: $\dfrac{10}{5}=\dfrac{30}{15}$, so $m$ and $k$ sit at **one height**: the $40\,\Omega$ lies flat, no current." show=m,k,eR3
#@ step "The $8\,\mathrm{A}$ splits: $5+10=15\,\Omega$ vs $15+30=45\,\Omega$: $6\,\mathrm{A}$ and $2\,\mathrm{A}$. The $6\,\mathrm{A}$ comes up through the $45\,\mathrm{V}$ spot: $i_o'''=6\,\mathrm{A}$." show=p,eR1,eR2,eR4,eR5,eV1,eV2
#@ view "All three: add"
#@ straight off
#@ node p 108.75 "$p$: $108.75\,\mathrm{V}$"
#@ node m 73.75 "$m$: $73.75\,\mathrm{V}$"
#@ node z0 63.75 "bottom: $63.75\,\mathrm{V}$"
#@ node k 48.75 "$k$: $48.75\,\mathrm{V}$"
#@ node n 10 "$n$: $10\,\mathrm{V}$"
#@ node g 0 "$r$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$r$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$r$: $0\,\mathrm{V}$" ground
#@ el V p z0 "$45\,\mathrm{V}$" col=0 i="$7\,\mathrm{A}$" to=p id=eV1
#@ el I g z0 "$8\,\mathrm{A}$" col=1 i="$8\,\mathrm{A}$" to=z0 id=eI1
#@ el R z0 k "$15\,\Omega$: falls $15\,\mathrm{V}$" col=2 i="$1\,\mathrm{A}$" to=k id=eR4
#@ el R k g2 "$30\,\Omega$: falls $48.75\,\mathrm{V}$" col=2 i="$1.625\,\mathrm{A}$" to=g2 id=eR5
#@ el R m k "$40\,\Omega$: falls $25\,\mathrm{V}$" col=3 i="$0.625\,\mathrm{A}$" to=k id=eR3
#@ el R p m "$5\,\Omega$: falls $35\,\mathrm{V}$" col=4 i="$7\,\mathrm{A}$" to=m id=eR1
#@ el R m n "$10\,\Omega$: falls $63.75\,\mathrm{V}$" col=4 i="$6.375\,\mathrm{A}$" to=n id=eR2
#@ el V n g3 "$10\,\mathrm{V}$" col=4 i="$6.375\,\mathrm{A}$" to=g3 id=eV2
#@ step "Ground $r$ again (the lowest). Add: $i_o=1.125-0.125+6=7\,\mathrm{A}$, climbing through the $45\,\mathrm{V}$ source." show=eV1
```

<details><summary>Solution</summary>

1. $45\,\mathrm{V}$ alone.

   $$i_o'=\frac{45}{5+(40\parallel40)+15}=1.125\,\mathrm{A}$$
2. $10\,\mathrm{V}$ alone.

   $$i_{10}=\frac{10}{53.33}=0.1875\,\mathrm{A},\quad i_o''=-0.1875\cdot\frac{40}{60}=-0.125\,\mathrm{A}$$
3. $8\,\mathrm{A}$ alone: balanced bridge ($\tfrac{10}{5}=\tfrac{30}{15}$), no current in the $40\,\Omega$.

   $$i_o'''=8\cdot\frac{45}{15+45}=6\,\mathrm{A}$$
4. Add.

   $$i_o=1.125-0.125+6=7\,\mathrm{A}$$

**Answer:** $i_o=7\,\mathrm{A}$ ($1.125$, $-0.125$, $6$).

</details>

**Problem: Assessment AP 4.21 + P4.86 · Matched, and how efficient?** (advanced)

$R_o$ is set for maximum power; $v_\phi$ is the voltage across the $4\,\Omega$ in series with the $20\,\mathrm{V}$ source. **(a)** Find $R_o$. **(b)** Find $p_{\max}$. **(c)** (P4.86) What percentage of the power developed reaches $R_o$?

```schematic
V1 0,4 -> 0,0 "$100\,\mathrm{V}$"
R1 0,4 -> 3,4 "$4\,\Omega$"
R2 3,4 -> 6,4 "$4\,\Omega$"
R3 3,4 -> 3,2 "$4\,\Omega$" v="$v_\phi$"
V2 3,2 -> 3,0 "$20\,\mathrm{V}$"
wire 0,4 -> 0,7
E1 3,7 -> 0,7 "$v_\phi$"
R4 3,7 -> 6,7 "$4\,\Omega$"
wire 6,7 -> 6,4
wire 6,4 -> 8,4
R5 8,4 -> 8,0 "$R_o$"
wire 0,0 -> 8,0
label 3,4 "$c$" above
label 3,7 "$t$" above
label 3,2 "$d$" right
label 8,4 "$a$" above
ground 0,0
#@ spoiler
#@ view "Open"
#@ straight off
#@ node t 160 "diamond +: $160\,\mathrm{V}$"
#@ node a 120 "$a$: $120\,\mathrm{V}$" terminal
#@ node s 100 "100 V top: $100\,\mathrm{V}$"
#@ node c 80 "$c$: $80\,\mathrm{V}$"
#@ node d 20 "20 V top: $20\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$100\,\mathrm{V}$" col=0 i="$15\,\mathrm{A}$" to=s id=eV1
#@ el E t s "$v_\phi$: $60\,\mathrm{V}$" col=0 i="$10\,\mathrm{A}$" to=t id=eE1
#@ el R s c "$4\,\Omega$: falls $20\,\mathrm{V}$" col=1 i="$5\,\mathrm{A}$" to=c id=eR1
#@ el R t a "$4\,\Omega$: falls $40\,\mathrm{V}$" col=2 i="$10\,\mathrm{A}$" to=a id=eR4
#@ el R c a "$4\,\Omega$: falls $40\,\mathrm{V}$" col=2 i="$10\,\mathrm{A}$" to=c id=eR2
#@ el R c d "$4\,\Omega$: falls $60\,\mathrm{V}$" col=3 i="$15\,\mathrm{A}$" to=d id=eR3 plus=c v="$v_\phi$"
#@ el V d g2 "$20\,\mathrm{V}$" col=3 i="$15\,\mathrm{A}$" to=g2 id=eV2
#@ step "Ground $b$. The source fixes $100\,\mathrm{V}$; the rod $v_\phi=c-20$ puts the diamond's top at $80+c$."
#@ step "Open: KCL at $a$ gives $a=40+c$; KCL at $c$ gives $c=80$. So $a=120\,\mathrm{V}=V_{\mathrm{Th}}$." show=c,a,t
#@ step "Currents = fall ÷ R. The $20\,\mathrm{V}$ source carries $15\,\mathrm{A}$ **down**: it absorbs." show=eR1,eR2,eR3,eR4,eV1,eV2,eE1
#@ view "Short"
#@ straight off
#@ node t 120 "diamond +: $120\,\mathrm{V}$"
#@ node s 100 "100 V top: $100\,\mathrm{V}$"
#@ node c 40 "$c$: $40\,\mathrm{V}$"
#@ node d 20 "20 V top: $20\,\mathrm{V}$"
#@ node a 0 "$a$ = $b$: $0\,\mathrm{V}$"
#@ node g 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$a$ = $b$: $0\,\mathrm{V}$" ground
#@ el V s g "$100\,\mathrm{V}$" col=0 i="$45\,\mathrm{A}$" to=s id=eV1
#@ el E t s "$v_\phi$: $20\,\mathrm{V}$" col=0 i="$30\,\mathrm{A}$" to=t id=eE1
#@ el R s c "$4\,\Omega$: falls $60\,\mathrm{V}$" col=1 i="$15\,\mathrm{A}$" to=c id=eR1
#@ el R c a "$4\,\Omega$: falls $40\,\mathrm{V}$" col=2 i="$10\,\mathrm{A}$" to=a id=eR2
#@ el R c d "$4\,\Omega$: falls $20\,\mathrm{V}$" col=3 i="$5\,\mathrm{A}$" to=d id=eR3 plus=c v="$v_\phi$"
#@ el V d g2 "$20\,\mathrm{V}$" col=3 i="$5\,\mathrm{A}$" to=g2 id=eV2
#@ el R t a "$4\,\Omega$: falls $120\,\mathrm{V}$" col=4 i="$30\,\mathrm{A}$" to=a id=eR4
#@ el W a g3 "short: no step" col=4 i="$40\,\mathrm{A}$" to=g3 id=eSC
#@ step "Same ground; $a$ pinned to $b$. KCL at $c$: $c=40\,\mathrm{V}$, so the diamond's top is $120\,\mathrm{V}$." show=c,t
#@ step "Into the short: $\dfrac{120}{4}+\dfrac{40}{4}=40\,\mathrm{A}=I_N$. So $R_{\mathrm{Th}}=\dfrac{120}{40}=3\,\Omega$." show=eR4,eR2,eSC,eR1,eR3,eV1,eV2,eE1
#@ view "Matched: 3 Ω"
#@ straight off
#@ node t 140 "diamond +: $140\,\mathrm{V}$"
#@ node s 100 "100 V top: $100\,\mathrm{V}$"
#@ node a 60 "$a$ = $c$: $60\,\mathrm{V}$"
#@ node c 60 "$a$ = $c$: $60\,\mathrm{V}$"
#@ node d 20 "20 V top: $20\,\mathrm{V}$"
#@ node g 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g2 0 "$b$: $0\,\mathrm{V}$" ground
#@ node g3 0 "$b$: $0\,\mathrm{V}$" ground
#@ el V s g "$100\,\mathrm{V}$" col=0 i="$30\,\mathrm{A}$" to=s id=eV1
#@ el E t s "$v_\phi$: $40\,\mathrm{V}$" col=0 i="$20\,\mathrm{A}$" to=t id=eE1
#@ el R s c "$4\,\Omega$: falls $40\,\mathrm{V}$" col=1 i="$10\,\mathrm{A}$" to=c id=eR1
#@ el R c d "$4\,\Omega$: falls $40\,\mathrm{V}$" col=1 i="$10\,\mathrm{A}$" to=d id=eR3 plus=c v="$v_\phi$"
#@ el V d g2 "$20\,\mathrm{V}$" col=1 i="$10\,\mathrm{A}$" to=g2 id=eV2
#@ el R c a "$4\,\Omega$: no fall" col=1 id=eR2
#@ el R t a "$4\,\Omega$: falls $80\,\mathrm{V}$" col=2 i="$20\,\mathrm{A}$" to=a id=eR4
#@ el R a g3 "$3\,\Omega$: falls $60\,\mathrm{V}$" col=2 i="$20\,\mathrm{A}$" to=g3 id=eR5
#@ step "Same ground. Matched: $a$ sits at half the open height, $60\,\mathrm{V}$. $p_{\max}=\dfrac{60^2}{3}=1200\,\mathrm{W}$." show=a,eR5
#@ step "Note $c$ is also $60\,\mathrm{V}$: the $4\,\Omega$ between $c$ and $a$ lies flat." show=c,t,eR2
#@ step "Climbs: the $100\,\mathrm{V}$ source lifts $30\,\mathrm{A}$ ($3000\,\mathrm{W}$), the diamond $20\,\mathrm{A}$ through $40\,\mathrm{V}$ ($800\,\mathrm{W}$). The $20\,\mathrm{V}$ source absorbs $200\,\mathrm{W}$. Load share: $\dfrac{1200}{3800}=31.6\%$." show=eR1,eR3,eR4,eV1,eV2,eE1
```

<details><summary>Solution</summary>

1. Open: $v_\phi=v_c-20$, diamond top $=80+v_c$; KCL at $a$, then $c$.

   $$v_a=40+v_c,\qquad v_c=80\;\Rightarrow\;V_{\mathrm{Th}}=120\,\mathrm{V}$$
2. Short: KCL at $c$.

   $$v_c=40\,\mathrm{V},\qquad I_N=\frac{120}{4}+\frac{40}{4}=40\,\mathrm{A}$$
3. Match.

   $$R_o=R_{\mathrm{Th}}=\frac{120}{40}=3\,\Omega,\qquad p_{\max}=\frac{120^2}{4(3)}=1200\,\mathrm{W}$$
4. Back to the original with $R_o=3\,\Omega$.

   $$\eta=\frac{1200}{100(30)+40(20)}=\frac{1200}{3800}=31.6\%$$

**Answer:** **(a)** $3\,\Omega$ **(b)** $1200\,\mathrm{W}$ **(c)** $31.6\%$

</details>

**Problem: Textbook P4.98 · Superposition with a diamond that stays on** (intermediate)

Use superposition to find $v_o$.

```schematic
V1 0,3 -> 0,0 "$25\,\mathrm{V}$"
R1 4,3 -> 0,3 "$4\,\mathrm{k\Omega}$" i="$i_\phi$"
I1 4,3 -> 4,0 "$5\,\mathrm{mA}$"
wire 4,3 -> 8,3
R2 8,3 -> 8,0 "$20\,\mathrm{k\Omega}$" v="$v_o$"
wire 0,3 -> 0,5
G1 0,5 -> 8,5 "$2.2i_\phi$"
wire 8,5 -> 8,3
wire 0,0 -> 8,0
label 4,3 "$n$" above
ground 0,0
#@ spoiler
#@ view "25 V alone"
#@ straight off
#@ node n 30 "$n$: $30\,\mathrm{V}$"
#@ node s 25 "$s$: $25\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V s g "$25\,\mathrm{V}$" col=0 i="$1.5\,\mathrm{mA}$" to=s id=eV1
#@ el G s n "$2.2i_\phi$: $2.75\,\mathrm{mA}$" col=1 i="$2.75\,\mathrm{mA}$" to=n id=eG1
#@ el R n s "$4\,\mathrm{k\Omega}$: falls $5\,\mathrm{V}$" col=2 i="$1.25\,\mathrm{mA}$" to=s id=eR1
#@ el R n g2 "$20\,\mathrm{k\Omega}$: falls $30\,\mathrm{V}$" col=3 i="$1.5\,\mathrm{mA}$" to=g2 id=eR2 plus=n v="$v_o$"
#@ step "Ground the bottom wire. The $5\,\mathrm{mA}$ pump is off (a gap, left out). The battery lifts $s$ to $25\,\mathrm{V}$. The diamond stays on."
#@ step "The diamond pumps $2.2i_\phi$ from $s$ to $n$, with $i_\phi=\dfrac{n-25}{4}\,\mathrm{mA}$. In = out at $n$ (mA, kΩ): $2.2\dfrac{n-25}{4}=\dfrac{n-25}{4}+\dfrac{n}{20}$, so $n=30\,\mathrm{V}$: $v_o'=30\,\mathrm{V}$." show=n,eG1,eR1,eR2,eV1
#@ view "5 mA alone"
#@ straight off
#@ node n 20 "$n$: $20\,\mathrm{V}$"
#@ node s 0 "$s$ = bottom: $0\,\mathrm{V}$"
#@ node g 0 "$s$ = bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "$s$ = bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "$s$ = bottom: $0\,\mathrm{V}$" ground
#@ el W g s "$25\,\mathrm{V}$ off: a wire" col=0 i="$6\,\mathrm{mA}$" to=s id=eV1
#@ el G s n "$2.2i_\phi$: $11\,\mathrm{mA}$" col=1 i="$11\,\mathrm{mA}$" to=n id=eG1
#@ el R n s "$4\,\mathrm{k\Omega}$: falls $20\,\mathrm{V}$" col=2 i="$5\,\mathrm{mA}$" to=s id=eR1
#@ el I n g2 "$5\,\mathrm{mA}$" col=3 i="$5\,\mathrm{mA}$" to=g2 id=eI1
#@ el R n g3 "$20\,\mathrm{k\Omega}$: falls $20\,\mathrm{V}$" col=4 i="$1\,\mathrm{mA}$" to=g3 id=eR2 plus=n v="$v_o$"
#@ step "Same ground. The battery → wire ($s=0$). The diamond stays on."
#@ step "In = out at $n$: $2.2\dfrac{n}{4}=\dfrac{n}{4}+5+\dfrac{n}{20}$, so $n=20\,\mathrm{V}$: $v_o''=20\,\mathrm{V}$. The diamond lifts $11\,\mathrm{mA}$; $5\,\mathrm{mA}$ falls back through the $4\,\mathrm{k\Omega}$ and $5\,\mathrm{mA}$ down through the pump." show=n,eG1,eR1,eR2,eI1,eV1
#@ view "Both: add"
#@ straight off
#@ node n 50 "$n$: $50\,\mathrm{V}$"
#@ node s 25 "$s$: $25\,\mathrm{V}$"
#@ node g 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g2 0 "bottom: $0\,\mathrm{V}$" ground
#@ node g3 0 "bottom: $0\,\mathrm{V}$" ground
#@ el V s g "$25\,\mathrm{V}$" col=0 i="$7.5\,\mathrm{mA}$" to=s id=eV1
#@ el G s n "$2.2i_\phi$: $13.75\,\mathrm{mA}$" col=1 i="$13.75\,\mathrm{mA}$" to=n id=eG1
#@ el R n s "$4\,\mathrm{k\Omega}$: falls $25\,\mathrm{V}$" col=2 i="$6.25\,\mathrm{mA}$" to=s id=eR1
#@ el I n g2 "$5\,\mathrm{mA}$" col=3 i="$5\,\mathrm{mA}$" to=g2 id=eI1
#@ el R n g3 "$20\,\mathrm{k\Omega}$: falls $50\,\mathrm{V}$" col=4 i="$2.5\,\mathrm{mA}$" to=g3 id=eR2 plus=n v="$v_o$"
#@ step "Same ground. Add: $v_o=30+20=50\,\mathrm{V}$ ✓" show=n
```

<details><summary>Solution</summary>

1. $25\,\mathrm{V}$ alone, $i_\phi=\dfrac{v_o-25}{4}$ (mA, kΩ).

   $$2.2\,\frac{v_o-25}{4}=\frac{v_o-25}{4}+\frac{v_o}{20}\;\Rightarrow\;v_o'=30\,\mathrm{V}$$
2. $5\,\mathrm{mA}$ alone, $i_\phi=\dfrac{v_o}{4}$.

   $$2.2\,\frac{v_o}{4}=\frac{v_o}{4}+5+\frac{v_o}{20}\;\Rightarrow\;v_o''=20\,\mathrm{V}$$
3. Add.

   $$v_o=30+20=50\,\mathrm{V}$$

**Answer:** $v_o=50\,\mathrm{V}$

</details>

## Cheat sheet

| Idea | In heights | Write |
|---|---|---|
| Thévenin with diamonds | push $1\,\mathrm{A}$ into $a$ (independent sources off) | $R_{\mathrm{Th}}=\dfrac{v_T}{i_T}$ |
| One-shot test source | start height + slope | $v_T=V_{\mathrm{Th}}+R_{\mathrm{Th}}i_T$ |
| No independent source | nothing lifts $a$ | $V_{\mathrm{Th}}=I_N=0$ |
| Maximum power | load at half the open height | $R_L=R_{\mathrm{Th}}$, $p_{\max}=\dfrac{V_{\mathrm{Th}}^2}{4R_{\mathrm{Th}}}$ |
| Efficiency | load power ÷ all the climbs (original circuit) | $\eta=\dfrac{p_L}{\sum p_{\text{dev}}}$ |
| Superposition | one picture per source; add heights | $y=y_1+y_2+\cdots$, $p\neq p_1+p_2$ |
