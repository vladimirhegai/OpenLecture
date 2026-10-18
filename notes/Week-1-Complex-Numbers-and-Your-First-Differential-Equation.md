# Week 1: Complex Numbers and Your First Differential Equation

## Topic 1: Complex numbers: one point, two ways to write it

$j=\sqrt{-1}$, so $j^2=-1$. (Engineers write $j$ because $i$ means current.)

A complex number $z$ is a **point on a plane**. You can describe that point two ways.

**Rectangular form** $z=a+jb$: how far across, how far up.
- $a=\mathrm{Re}\{z\}$: the **real part** (across)
- $b=\mathrm{Im}\{z\}$: the **imaginary part** (up)

**Polar form** $z=c\angle\theta$: how long, which direction.
- $c=|z|$: the **magnitude** (length of the arrow, never negative)
- $\theta=\angle z$: the **angle** (counter-clockwise from the positive real axis)

$$z=a+jb=c\,e^{j\theta}=c\angle\theta$$

| Convert | How |
|---|---|
| $a+jb\ \to\ c\angle\theta$ | $c=\sqrt{a^2+b^2}$, $\ \theta=\arctan\dfrac{b}{a}$, **then add $180^\circ$ if $a<0$** |
| $c\angle\theta\ \to\ a+jb$ | $a=c\cos\theta$, $\ b=c\sin\theta$ |

```graph
title "Drag $z$: both forms update"
x -5 5 label="Re"
y -4 4 label="Im"
equal
drag Z 3 4 label="$z$" snap=0.5
arrow "Z_x" "Z_y" color=1
segment "Z_x" "0" "Z_x" "Z_y" dash color=0
segment "0" "Z_y" "Z_x" "Z_y" dash color=0
circle "0" "0" "1" dash color=0
readout "$a=$" "Z_x"
readout "$b=$" "Z_y"
readout "$c=$" "hypot(Z_x,Z_y)"
readout "$\theta=$" "deg(atan2(Z_y,Z_x))" unit="°"
readout "$\arctan(b/a)=$" "deg(atan(Z_y/Z_x))" unit="°"
caption "Drag $z$ into the left half: $\arctan(b/a)$ is now off by $180^\circ$ from the true angle $\theta$."
```

**Euler's identity** connects the two forms:

$$e^{j\theta}=\cos\theta+j\sin\theta\quad\Rightarrow\quad c\,e^{j\theta}=\underbrace{c\cos\theta}_{a}+j\,\underbrace{c\sin\theta}_{b}$$

- $e^{j\theta}$ is the point at angle $\theta$ on the **unit circle** (the dashed circle above): its length is $\sqrt{\cos^2\theta+\sin^2\theta}=1$.
- Multiplying by $c$ stretches it out to length $c$. That's where $a=c\cos\theta$ and $b=c\sin\theta$ come from.

**Example: Example 1 · Left half of the plane: the arctan trap**

Write $z=-3+j4$ in polar form.

1. The length uses Pythagoras; signs don't matter.

   $$c=\sqrt{(-3)^2+4^2}=5$$
2. The calculator gives $\arctan\frac{4}{-3}=-53.13^\circ$, which points down-right. But $z$ is up-left ($a<0$).

   $$\arctan\frac{4}{-3}=-53.13^\circ\quad\text{(wrong side)}$$
3. $a<0$, so add $180^\circ$. (`Pol(-3,4)` on a Casio does this for you.)

   $$\theta=-53.13^\circ+180^\circ=126.87^\circ$$

**Answer:** $z=5\angle126.87^\circ=5e^{j126.87^\circ}$

**Example: Example 2 · Polar back to rectangular**

Write $z=10\angle{-150^\circ}$ as $a+jb$.

1. No quadrant thinking needed: the signs of $\cos$ and $\sin$ handle it.

   $$a=10\cos(-150^\circ)=-8.66$$
2. Same for the imaginary part.

   $$b=10\sin(-150^\circ)=-5$$

**Answer:** $z=-8.66-j5$ (down-left, as $-150^\circ$ says)

**Example: Example 3 · Trig identities for free (lecture)**

Use $e^{jA}e^{jB}=e^{j(A+B)}$ to get the formulas for $\cos(A+B)$ and $\sin(A+B)$.

1. ```steps
$$ e^{jA}\,e^{jB}=e^{j(A+B)} $$
Exponents add when you multiply.
$$ \hl{(\cos A+j\sin A)(\cos B+j\sin B)}=\hl{\cos(A+B)+j\sin(A+B)} $$
Write every exponential with Euler's identity.
$$ \cos A\cos B+j\cos A\sin B+j\sin A\cos B+\hl{j^2}\sin A\sin B $$
Expand the left side like ordinary brackets.
$$ \hl{(\cos A\cos B-\sin A\sin B)}+j\hl{(\sin A\cos B+\cos A\sin B)} $$
$j^2=-1$; group the terms without $j$ and with $j$.
$$ \cos(A+B)=\cos A\cos B-\sin A\sin B $$
Two complex numbers are equal only if their real parts match…
$$ \sin(A+B)=\sin A\cos B+\cos A\sin B $$
…and their imaginary parts match.
```

**Answer:** $\cos(A+B)=\cos A\cos B-\sin A\sin B$, $\ \sin(A+B)=\sin A\cos B+\cos A\sin B$

**Problem: Try it 1 · Euler on the axes** (introductory)

Without a calculator, find $e^{j\pi}$, $e^{j\pi/2}$ and $e^{-j\pi/2}$. (Angles in radians: $\pi=180^\circ$.)

<details><summary>Solution</summary>

1. $e^{j\theta}$ is the point at angle $\theta$ on the unit circle. $\pi$ is $180^\circ$: straight left.

   $$e^{j\pi}=\cos\pi+j\sin\pi=-1$$
2. $\pi/2$ is $90^\circ$: straight up.

   $$e^{j\pi/2}=\cos\tfrac{\pi}{2}+j\sin\tfrac{\pi}{2}=j$$
3. $-\pi/2$ is $90^\circ$ clockwise: straight down.

   $$e^{-j\pi/2}=-j$$

**Answer:** $e^{j\pi}=-1$, $\ e^{j\pi/2}=j$, $\ e^{-j\pi/2}=-j$

</details>

## Topic 2: Complex arithmetic

Each operation is easy in one form and messy in the other:

| Operation | Use | Rule |
|---|---|---|
| Add, subtract | rectangular | add the real parts and the imaginary parts separately |
| Multiply | polar | lengths multiply, angles add: $c_1e^{j\theta_1}\cdot c_2e^{j\theta_2}=c_1c_2\,e^{j(\theta_1+\theta_2)}$ |
| Divide | polar | lengths divide, angles subtract: $\dfrac{c_1e^{j\theta_1}}{c_2e^{j\theta_2}}=\dfrac{c_1}{c_2}e^{j(\theta_1-\theta_2)}$ |
| Divide | rectangular | multiply top and bottom by the conjugate of the bottom |
| Power $z^k$ | polar | $c^k\,e^{jk\theta}$ (de Moivre's theorem) |
| $k$-th roots | polar | $c^{1/k}\,e^{j(\theta+360^\circ\ell)/k}$ for $\ell=0,1,\dots,k-1$: $k$ answers |

**Conjugate** $z^*$: flip the sign of the imaginary part.
- $z^*=a-jb=c\,e^{-j\theta}$ (mirror image across the real axis)
- $z\,z^*=a^2+b^2=c^2$, always a **real** number. That is what makes rectangular division work.

```graph
title "Multiplying: lengths multiply, angles add"
x -4 4 label="Re"
y -3 3 label="Im"
equal
drag Z 1.5 0.5 label="$z$" color=1 snap=0.25
drag W 0.5 1.5 label="$w$" color=3 snap=0.25
arrow "Z_x" "Z_y" color=1
arrow "W_x" "W_y" color=3
arrow "Z_x*W_x-Z_y*W_y" "Z_x*W_y+Z_y*W_x" color=2 label="$zw$"
circle "0" "0" "1" dash color=0
readout "$|z|\,|w|=$" "hypot(Z_x,Z_y)*hypot(W_x,W_y)"
readout "$|zw|=$" "hypot(Z_x*W_x-Z_y*W_y,Z_x*W_y+Z_y*W_x)"
readout "$\angle z+\angle w=$" "deg(atan2(Z_y,Z_x))+deg(atan2(W_y,W_x))" unit="°"
readout "$\angle zw=$" "deg(atan2(Z_x*W_y+Z_y*W_x,Z_x*W_x-Z_y*W_y))" unit="°"
caption "Put $w$ on the dashed unit circle: then $zw$ is just $z$ rotated."
```

**Example: Example 4 · Dividing in rectangular form (lecture Example 1.1)**

Find $\dfrac{80+j18}{8+j10}$.

1. ```steps
$$ \dfrac{80+j18}{8+j10} $$
The $j$ in the bottom is the problem.
$$ \dfrac{80+j18}{8+j10}\cdot\hl{\dfrac{8-j10}{8-j10}} $$
Multiply top and bottom by the conjugate of the bottom (that is multiplying by 1).
$$ =\dfrac{(80+j18)(8-j10)}{\hl{64+100}} $$
Bottom: $zz^*=a^2+b^2$, a real number.
$$ =\dfrac{\hl{640+180}+j(\hl{144-800})}{164} $$
Top: expand, with $j\cdot j=-1$ turning $-j^2180$ into $+180$.
$$ =\dfrac{820-j656}{164}=\hl{5-j4} $$
Divide each part by 164.
```

**Answer:** $5-j4$

**Example: Example 5 · A big power: de Moivre**

Find $(1+j)^8$.

1. Multiplying out 8 brackets is painful; in polar form it's one step. $1+j$ is 1 right and 1 up.

   $$1+j=\sqrt2\angle45^\circ$$
2. Raise the length to the 8th power and multiply the angle by 8.

   $$(\sqrt2)^8\angle(8\times45^\circ)=16\angle360^\circ$$
3. $360^\circ$ is a full turn: pointing along the positive real axis.

   $$16\angle360^\circ=16$$

**Answer:** $(1+j)^8=16$

**Example: Example 6 · All four fourth roots (lecture Example 1.2)**

Find all fourth roots of $z=81e^{j60^\circ}$.

1. Every root has length $81^{1/4}$.

   $$81^{1/4}=3$$
2. The first root has a quarter of the angle.

   $$\tfrac{60^\circ}{4}=15^\circ\ \Rightarrow\ 3e^{j15^\circ}$$
3. The other three are spaced $\tfrac{360^\circ}{4}=90^\circ$ apart round the same circle.

   $$3e^{j15^\circ},\ 3e^{j105^\circ},\ 3e^{j195^\circ},\ 3e^{j285^\circ}$$
4. Check one: $(3e^{j105^\circ})^4=81e^{j420^\circ}$, and $420^\circ-360^\circ=60^\circ$ ✓

**Answer:** $3e^{j15^\circ},\ 3e^{j105^\circ},\ 3e^{j195^\circ},\ 3e^{j285^\circ}$

```graph
title "The $k$ roots of $z=c\angle\theta$ sit evenly on one circle"
x -4.6 4.6 label="Re"
y -4.6 4.6 label="Im"
equal
slider k 3 6 4 step=1 label="$k$"
slider c 1 81 81 step=1 label="$c$"
slider th 0 360 60 step=5 label="$\theta$ (°)"
point "if(k>0,c^(1/k)*cos(rad((th+360*0)/k)),sqrt(-1))" "if(k>0,c^(1/k)*sin(rad((th+360*0)/k)),sqrt(-1))" color=2
point "if(k>1,c^(1/k)*cos(rad((th+360*1)/k)),sqrt(-1))" "if(k>1,c^(1/k)*sin(rad((th+360*1)/k)),sqrt(-1))" color=1
point "if(k>2,c^(1/k)*cos(rad((th+360*2)/k)),sqrt(-1))" "if(k>2,c^(1/k)*sin(rad((th+360*2)/k)),sqrt(-1))" color=1
point "if(k>3,c^(1/k)*cos(rad((th+360*3)/k)),sqrt(-1))" "if(k>3,c^(1/k)*sin(rad((th+360*3)/k)),sqrt(-1))" color=1
point "if(k>4,c^(1/k)*cos(rad((th+360*4)/k)),sqrt(-1))" "if(k>4,c^(1/k)*sin(rad((th+360*4)/k)),sqrt(-1))" color=1
point "if(k>5,c^(1/k)*cos(rad((th+360*5)/k)),sqrt(-1))" "if(k>5,c^(1/k)*sin(rad((th+360*5)/k)),sqrt(-1))" color=1
circle "0" "0" "c^(1/k)" dash color=0
readout "radius $c^{1/k}=$" "c^(1/k)"
readout "first angle $\theta/k=$" "th/k" unit="°"
readout "spacing $360^\circ/k=$" "360/k" unit="°"
caption "Orange is the first root ($\ell=0$). Set $k=4$, $c=81$, $\theta=60^\circ$ for the lecture example."
```

**Example: Example 7 · Square root of a negative: complex roots of a quadratic**

Solve $s^2+2s+5=0$.

1. Quadratic formula with $a=1$, $b=2$, $c=5$.

   $$s=\frac{-2\pm\sqrt{4-20}}{2}=\frac{-2\pm\sqrt{-16}}{2}$$
2. $\sqrt{-16}=\sqrt{16}\,\sqrt{-1}=j4$.

   $$s=\frac{-2\pm j4}{2}=-1\pm j2$$

**Answer:** $s=-1\pm j2$ (a conjugate pair)

**Problem: Try it 2 · Cube roots of a negative number** (intermediate)

Find all three cube roots of $-8$. Give each in polar and rectangular form.

<details><summary>Solution</summary>

1. $-8$ points straight left: length 8, angle $180^\circ$.

   $$-8=8\angle180^\circ$$
2. Root length $8^{1/3}=2$; first angle $\tfrac{180^\circ}{3}=60^\circ$; spacing $\tfrac{360^\circ}{3}=120^\circ$.

   $$2\angle60^\circ,\quad 2\angle180^\circ,\quad 2\angle300^\circ$$
3. Convert with $a=c\cos\theta$, $b=c\sin\theta$.

   $$1+j1.732,\quad -2,\quad 1-j1.732$$

**Answer:** $2\angle60^\circ=1+j\sqrt3$, $\ 2\angle180^\circ=-2$, $\ 2\angle300^\circ=1-j\sqrt3$

</details>

**Problem: Try it 3 · A high power of j** (introductory)

Simplify $j^{27}$.

<details><summary>Solution</summary>

1. $j$ is length 1 at $90^\circ$, so $j^{27}$ is length 1 at $27\times90^\circ$.

   $$j^{27}=1\angle2430^\circ$$
2. Remove whole turns: $2430^\circ-6\times360^\circ=270^\circ$, which points straight down.

   $$1\angle270^\circ=-j$$

**Answer:** $j^{27}=-j$

</details>

## Topic 3: Your first differential equation: the RL natural response

```schematic
I1 0,3 -> 0,0 "$I_s$"
wire 0,3 -> 3,3
R0 3,3 -> 3,0 "$R_0$"
S1 3,3 -> 6,3 "$t=0$" state=closed action=open
L1 6,0 -> 6,3 "$L$" i="$i$"
wire 6,3 -> 9,3
R1 9,3 -> 9,0 "$R$" v="$v$"
wire 0,0 -> 9,0
ground 0,0
```

- **Before $t=0$:** the inductor has been in DC a long time, so it acts like a wire and carries all of $I_s$.
- **At $t=0$:** the switch opens. An inductor's current **can't jump**, so $i(0)=I_s$.
- **After:** only the $L$–$R$ loop is left. KVL around it gives the equation below.

That equation is a **differential equation**: the unknown is a *function* $i(t)$, and the equation involves its rate of change $\frac{di}{dt}$.

```steps
title "Solving the RL loop (lecture)"
$$ L\dfrac{di}{dt}+Ri=0 $$
KVL around the loop: the inductor voltage is $L\frac{di}{dt}$, the resistor voltage $Ri$.
$$ \dfrac{di}{\hl{i}}=\hl{-\dfrac{R}{L}\,dt} $$
Divide by $L$ and by $i$, multiply by $dt$: all $i$ on the left, all $t$ on the right.
$$ \hl{\int_{i(0)}^{i(t)}}\dfrac{dx}{x}=-\dfrac{R}{L}\hl{\int_0^t}ds $$
Integrate from the start ($0$, $i(0)$) to any time $t$. $x$ and $s$ are placeholder names.
$$ \hl{\ln i(t)-\ln i(0)}=-\dfrac{R}{L}\,t $$
$\int\frac{dx}{x}=\ln x$, and $\int ds=s$.
$$ \hl{\ln\dfrac{i(t)}{i(0)}}=-\dfrac{R}{L}\,t $$
$\ln A-\ln B=\ln\frac{A}{B}$.
$$ \dfrac{i(t)}{i(0)}=\hl{e^{-(R/L)t}} $$
Undo $\ln$ by raising $e$ to both sides.
$$ i(t)=\hl{I_s}\,e^{-t/\tau},\qquad \hl{\tau=\dfrac{L}{R}} $$
Multiply by $i(0)=I_s$. $\tau$ (tau) is the **time constant**, in seconds.
```

```graph
title "$i(t)=I_se^{-t/\tau}$: change $\tau$ and $I_s$"
x 0 6 label="$t$ (s)"
y 0 5 label="$i$ (A)"
slider tau 0.2 3 1 step=0.05 label="$\tau$" animate
slider I 0.5 4.5 4 step=0.1 label="$I_s$"
curve "I*exp(-t/tau)" label="$I_se^{-t/\tau}$"
vline "tau" label="$t=\tau$"
point "tau" "I*exp(-1)" color=2
vline "5*tau" color=0
readout "$i(\tau)=$" "I*exp(-1)"
readout "$i(\tau)/I_s=$" "exp(-1)"
caption "After one $\tau$, $37\%$ is left; after $5\tau$ (grey line), under $1\%$."
```

```steps
title "Where the $e$ comes from (lecture's outline)"
$$ \dfrac{dy}{dt}+y=0,\qquad y(0)=y_0 $$
The simplest version of the RL equation.
$$ \hl{\dfrac{y(t)-y(t-\Delta)}{\Delta}}+y(t)\approx0 $$
Replace the derivative by a slope over a tiny time step $\Delta$.
$$ y(t)\,\hl{(1+\Delta)}=y(t-\Delta) $$
Multiply by $\Delta$ and rearrange: every step divides $y$ by $(1+\Delta)$.
$$ y(t)=y(0)\,(1+\Delta)^{\hl{-t/\Delta}} $$
Going from $0$ to $t$ takes $t/\Delta$ steps.
$$ y(t)=y(0)\,\Big[\hl{(1+\Delta)^{1/\Delta}}\Big]^{-t} $$
Regroup the exponent.
$$ y(t)=y(0)\,\hl{e}^{-t} $$
As $\Delta\to0$, $(1+\Delta)^{1/\Delta}\to e\approx2.718$. That is one definition of $e$.
```

**Example: Example 8 · Pre-tutorial 1: numbers in the RL loop**

In the circuit above, $L=8\,\mathrm{mH}$, $R=4\,\Omega$ and $I_s=4\,\mathrm{A}$. Find $i(t)$ and $v(t)$ for $t\ge0$, and sketch $i(t)$.

1. The current can't jump, so it starts at $I_s$.

   $$i(0)=4\,\mathrm{A}$$
2. Time constant (convert mH to H).

   $$\tau=\frac{L}{R}=\frac{8\times10^{-3}}{4}=2\,\mathrm{ms},\quad \frac1\tau=500\,\mathrm{s^{-1}}$$
3. Put both into $i(t)=I_se^{-t/\tau}$.

   $$i(t)=4e^{-500t}\,\mathrm{A}$$
4. The current comes down through $R$ from $+$ to $-$, so $v=Ri$.

   $$v(t)=4\cdot4e^{-500t}=16e^{-500t}\,\mathrm{V}$$

**Answer:** $\tau=2\,\mathrm{ms}$, $i(t)=4e^{-500t}\,\mathrm{A}$, $v(t)=16e^{-500t}\,\mathrm{V}$

```graph
title "Sketch: $i(t)=4e^{-500t}$ A"
x 0 10 label="$t$ (ms)"
y 0 4.5 label="$i$ (A)"
curve "4*exp(-t/2)" label="$i(t)$"
vline "2" label="$t=\tau=2$ ms"
point "2" "4*exp(-1)" color=2
text "2.3" "1.95" "$1.47$ A"
caption "Starts at 4 A, is at $37\%$ (1.47 A) after one $\tau$, gone by $5\tau=10$ ms."
```

**Example: Example 9 · How long until it is small?**

An RL loop has $L=0.5\,\mathrm{H}$, $R=100\,\Omega$ and $i(0)=10\,\mathrm{A}$. When is $i=1\,\mathrm{A}$?

1. Time constant and response.

   $$\begin{gathered}\tau=\frac{0.5}{100}=5\,\mathrm{ms}, \\ i(t)=10e^{-t/\tau}\end{gathered}$$
2. Set $i=1$ and isolate the exponential.

   $$e^{-t/\tau}=0.1$$
3. Take $\ln$ of both sides ($\ln e^x=x$).

   $$-\frac{t}{\tau}=\ln0.1=-2.303$$
4. Multiply by $-\tau$.

   $$t=2.303\,\tau=11.5\,\mathrm{ms}$$

**Answer:** $t=\tau\ln10=11.5\,\mathrm{ms}$

**Problem: Try it 4 · Check a solution by substituting it** (introductory)

Show that $i(t)=I_se^{-t/\tau}$ with $\tau=\dfrac{L}{R}$ really satisfies $L\dfrac{di}{dt}+Ri=0$.

<details><summary>Solution</summary>

1. Differentiate: $\frac{d}{dt}e^{-t/\tau}=-\frac1\tau e^{-t/\tau}$ (chain rule).

   $$\frac{di}{dt}=-\frac{I_s}{\tau}e^{-t/\tau}=-\frac{R}{L}I_se^{-t/\tau}$$
2. Substitute both pieces into the left side.

   $$L\Big(-\frac{R}{L}I_se^{-t/\tau}\Big)+R\,I_se^{-t/\tau}=-RI_se^{-t/\tau}+RI_se^{-t/\tau}=0\ \checkmark$$

**Answer:** It gives $0$ for every $t$, so it is a solution.

</details>

**Problem: Try it 5 · Work backwards from a measurement** (intermediate)

In an RL loop with $R=20\,\Omega$, the current halves every $3\,\mathrm{ms}$. Find $L$.

<details><summary>Solution</summary>

1. Halving in $3\,\mathrm{ms}$ means $e^{-0.003/\tau}=\tfrac12$.

   $$\frac{0.003}{\tau}=\ln2\ \Rightarrow\ \tau=\frac{0.003}{0.693}=4.33\,\mathrm{ms}$$
2. $\tau=L/R$, so $L=R\tau$.

   $$L=20\times0.00433=0.0866\,\mathrm{H}$$

**Answer:** $L\approx86.6\,\mathrm{mH}$

</details>
