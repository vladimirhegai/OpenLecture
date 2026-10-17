# Week 1: Complex Numbers and Your First Differential Equation

> **Info:** **Week 1 in one sentence:** complex numbers are points on a flat plane that you can write two ways ($a+jb$ or $c\,e^{j\theta}$), and a circuit with an inductor gives you your first differential equation, whose answer is a decaying exponential.
> 
> **By the end you can:**
> 
> - switch any complex number between rectangular form $a+jb$ and polar form $c\,e^{j\theta}$ (with the right angle in every quadrant);
> - add, subtract, multiply, divide, and take powers and roots of complex numbers;
> - use Euler's identity $e^{j\theta}=\cos\theta+j\sin\theta$ (including to prove trig identities);
> - write the differential equation of an RL circuit after a switch opens, solve it, and use the time constant $\tau=L/R$.

> **Tip:** **Why complex numbers in a differential-equations course?** In Week 5 you will solve equations like $y''+2y'+5y=0$ by solving $s^2+2s+5=0$, and the roots are $s=-1\pm j2$, complex numbers. Those roots turn into decaying oscillations (the ringing of an RLC circuit). Everything in Topics 1–2 is the toolkit for that.

## Topic 1: Complex numbers: one point, two ways to write it

Engineers write $j$ for $\sqrt{-1}$ (so $j^2=-1$; $i$ is already taken by current). A complex number $z=a+jb$ is really just a **point on a plane**: go $a$ to the right along the horizontal *real axis* (Re) and $b$ up along the vertical *imaginary axis* (Im). $a=\mathrm{Re}\{z\}$ is the *real part* and $b=\mathrm{Im}\{z\}$ is the *imaginary part*; both are ordinary real numbers.

You can describe the same point a second way: **how far** it is from the origin ($c=|z|$, the *magnitude*, never negative) and **which direction** it points ($\theta=\angle z$, the *angle*, measured counter-clockwise from the positive real axis). That is *polar form*, written $z=c\,e^{j\theta}$ or, in angle notation, $z=c\angle\theta$. Rectangular form is best for adding; polar form is best for multiplying. Converting between them is the core skill of this week.

> **Tip:** **The method: converting**
> 
> **Rectangular → polar** ($a+jb\;\to\;c\angle\theta$):
> 
> 1. **Sketch the point** $(a,b)$ so you know its quadrant.
> 2. Magnitude: $c=\sqrt{a^2+b^2}$.
> 3. Reference angle: $\theta_{\text{ref}}=\arctan\left|\dfrac{b}{a}\right|$ (an angle between $0^\circ$ and $90^\circ$).
> 4. Put it in the right quadrant with the table below.
> 
> **Polar → rectangular** ($c\angle\theta\;\to\;a+jb$): $a=c\cos\theta$, $b=c\sin\theta$. No quadrant thinking needed: the signs of $\cos$ and $\sin$ take care of it.
> 
> **Casio 991 check:** `Pol(a, b)` returns $c$ and $\theta$ (between $-180^\circ$ and $180^\circ$) with the quadrant already handled; `Rec(c, θ)` goes back. Make sure the calculator is in degree mode when you use degrees.

$$\begin{gathered}z=a+jb=c\,e^{j\theta}=c\angle\theta, \\ c=\sqrt{a^2+b^2},\quad \tan\theta=\frac{b}{a}, \\ a=c\cos\theta,\quad b=c\sin\theta\end{gathered}$$

| Where the point is | Signs | Angle $\theta$ (from the reference angle) | Example |
|---|---|---|---|
| 1st quadrant (up-right) | $a>0,\ b>0$ | $\theta=\theta_{\text{ref}}$ | $3+j4$: $53.13^\circ$ |
| 2nd quadrant (up-left) | $a<0,\ b>0$ | $\theta=180^\circ-\theta_{\text{ref}}$ | $-3+j4$: $126.87^\circ$ |
| 3rd quadrant (down-left) | $a<0,\ b<0$ | $\theta=180^\circ+\theta_{\text{ref}}$ (same as $-(180^\circ-\theta_{\text{ref}})$) | $-3-j4$: $233.13^\circ=-126.87^\circ$ |
| 4th quadrant (down-right) | $a>0,\ b<0$ | $\theta=-\theta_{\text{ref}}$ (same as $360^\circ-\theta_{\text{ref}}$) | $3-j4$: $-53.13^\circ$ |
| On an axis |  | $1=1\angle0^\circ$, $j=1\angle90^\circ$, $-1=1\angle180^\circ$, $-j=1\angle-90^\circ$ |  |

![Four points, four quadrants. Every arrow has length $c=5$; only the angle changes. The angle is always measured counter-clockwise from the positive real axis (orange arc for $-3+j4$).](/figures/elec231/w1_plane.svg)

*Four points, four quadrants. Every arrow has length $c=5$; only the angle changes. The angle is always measured counter-clockwise from the positive real axis (orange arc for $-3+j4$).*

**Euler's identity** is the bridge between the two forms. It says that $e^{j\theta}$ is the point at angle $\theta$ on the circle of radius 1:

$$\begin{gathered}e^{j\theta}=\cos\theta+j\sin\theta \\ \Longrightarrow \\ c\,e^{j\theta}=c\cos\theta+j\,c\sin\theta=a+jb\end{gathered}$$

Multiplying by $c$ just stretches that unit point out to distance $c$, which is why $a=c\cos\theta$ and $b=c\sin\theta$. Two consequences you will use a lot: $|e^{j\theta}|=\sqrt{\cos^2\theta+\sin^2\theta}=1$ (it always has length 1), and $e^{j\theta}$ only moves *around* a circle, so it can never grow or shrink.

**Example: Example 1 · A first-quadrant point**

Write $z=3+j4$ in polar form.

1. Sketch it: 3 to the right, 4 up. Both parts are positive, so the point is in the 1st quadrant.
2. The magnitude is the distance from the origin, by Pythagoras.

   $$c=\sqrt{3^2+4^2}=\sqrt{25}=5$$
3. In the 1st quadrant the angle is just the arctangent of (up ÷ right).

   $$\theta=\arctan\frac{4}{3}=53.13^\circ$$
4. Write the answer both ways.

   $$z=5\angle53.13^\circ=5\,e^{j53.13^\circ}$$

**Answer:** $z=5\angle 53.13^\circ$

**Example: Example 2 · The quadrant trap**

Write $z=-3+j4$ in polar form.

1. Sketch it: 3 to the **left**, 4 up. That is the 2nd quadrant.
2. The magnitude doesn't care about signs.

   $$c=\sqrt{(-3)^2+4^2}=5$$
3. A calculator's $\arctan(4/(-3))$ gives $-53.13^\circ$, which points down-right: wrong quadrant! Instead take the reference angle (the angle to the nearest horizontal axis) using sizes only.

   $$\theta_{\text{ref}}=\arctan\frac{4}{3}=53.13^\circ$$
4. In the 2nd quadrant the angle is measured from the positive real axis, so it is $180^\circ$ minus the reference angle.

   $$\theta=180^\circ-53.13^\circ=126.87^\circ$$
5. Check with `Pol(-3, 4)` on the calculator: it gives $5$ and $126.87^\circ$. ✓

   $$z=5\angle126.87^\circ$$

**Answer:** $z=5\angle126.87^\circ$ (not $-53.13^\circ$)

**Example: Example 3 · Third quadrant**

Write $z=-1-j$ in polar form.

1. Sketch: 1 left and 1 down, the 3rd quadrant.
2. The magnitude is the distance from the origin, by Pythagoras (the minus signs disappear when squared).

   $$c=\sqrt{(-1)^2+(-1)^2}=\sqrt2\approx1.414$$
3. The reference angle uses the sizes only (ignore the signs): the angle between the arrow and the horizontal axis.

   $$\theta_{\text{ref}}=\arctan\frac11=45^\circ$$
4. 3rd quadrant: go past $180^\circ$ by the reference angle. Going clockwise instead gives the equivalent negative angle; both are correct.

   $$\theta=180^\circ+45^\circ=225^\circ\quad(\text{same as }-135^\circ)$$

**Answer:** $z=\sqrt2\angle225^\circ=\sqrt2\angle-135^\circ$

**Example: Example 4 · Polar back to rectangular**

Write (a) $z=10\,e^{j150^\circ}$ and (b) $w=2\,e^{-j\pi/3}$ in rectangular form.

1. Use $a=c\cos\theta$ and $b=c\sin\theta$. For (a), $c=10$ and $\theta=150^\circ$.

   $$\begin{gathered}a=10\cos150^\circ=10(-0.866)=-8.66, \\ b=10\sin150^\circ=10(0.5)=5\end{gathered}$$
2. So (a) is in the 2nd quadrant, as $150^\circ$ should be.

   $$z=-8.66+j5$$
3. For (b) the angle is in **radians**: $\pi/3=60^\circ$, and the minus sign means clockwise. Set the calculator to radians, or convert to degrees first.

   $$\begin{gathered}a=2\cos(-60^\circ)=2(0.5)=1, \\ b=2\sin(-60^\circ)=2(-0.866)=-1.732\end{gathered}$$
4. So (b) is in the 4th quadrant.

   $$w=1-j1.732$$

**Answer:** (a) $-8.66+j5$  (b) $1-j1.732$

**Example: Example 5 · Trig identities for free from Euler (Lecture 1)**

Use $e^{jA}e^{jB}=e^{j(A+B)}$ to find formulas for $\cos(A+B)$ and $\sin(A+B)$.

1. Exponents add when you multiply, so the left and right sides are equal. Write each exponential with Euler's identity.

   $$(\cos A+j\sin A)(\cos B+j\sin B)=\cos(A+B)+j\sin(A+B)$$
2. Multiply out the left side like ordinary brackets, remembering $j\cdot j=j^2=-1$.

   $$\cos A\cos B+j\cos A\sin B+j\sin A\cos B+j^2\sin A\sin B$$
3. Group the real terms (no $j$) and the imaginary terms (with $j$).

   $$=(\cos A\cos B-\sin A\sin B)+j(\sin A\cos B+\cos A\sin B)$$
4. Two complex numbers are equal only if their real parts match **and** their imaginary parts match. Match them.

   $$\begin{gathered}\cos(A+B)=\cos A\cos B-\sin A\sin B, \\ \sin(A+B)=\sin A\cos B+\cos A\sin B\end{gathered}$$

**Answer:** $\cos(A+B)=\cos A\cos B-\sin A\sin B$, $\sin(A+B)=\sin A\cos B+\cos A\sin B$

> **Warning:** **Common mistakes**
> 
> - Trusting $\arctan(b/a)$ blindly. It only gives the right angle in the 1st and 4th quadrants. Always sketch the point first.
> - Calculator in the wrong mode: $\cos(150)$ in radian mode is not $\cos150^\circ$.
> - A negative magnitude. $c$ is a distance, so it is always $\ge0$; a minus sign belongs in the angle ($-5=5\angle180^\circ$).
> - Forgetting that $\theta$ and $\theta\pm360^\circ$ are the same direction ($225^\circ=-135^\circ$). Either is a correct answer.

**Problem: Try it 1 · Quick conversion** (introductory)

Write $z=1+j\sqrt3$ in polar form.

<details><summary>Solution</summary>

1. 1 right and $\sqrt3\approx1.73$ up: 1st quadrant.
2. The magnitude is the distance from the origin, by Pythagoras.

   $$c=\sqrt{1^2+(\sqrt3)^2}=\sqrt{4}=2$$
3. In the 1st quadrant the angle is just $\arctan(\text{up}\div\text{right})$; $\arctan\sqrt3=60^\circ$ is a standard angle.

   $$\theta=\arctan\frac{\sqrt3}{1}=60^\circ$$

**Answer:** $z=2\angle60^\circ=2e^{j\pi/3}$

</details>

**Problem: Try it 2 · Down and to the left** (introductory)

Write $z=-5-j12$ in polar form.

<details><summary>Solution</summary>

1. 5 left and 12 down: 3rd quadrant.
2. The magnitude, by Pythagoras (the signs disappear when squared).

   $$c=\sqrt{(-5)^2+(-12)^2}=\sqrt{169}=13$$
3. The reference angle uses the sizes only: up/down size 12, left/right size 5.

   $$\theta_{\text{ref}}=\arctan\frac{12}{5}=67.38^\circ$$
4. In the 3rd quadrant go past $180^\circ$ by the reference angle. Subtracting $360^\circ$ gives the same direction measured clockwise.

   $$\theta=180^\circ+67.38^\circ=247.38^\circ\;(=-112.62^\circ)$$

**Answer:** $z=13\angle247.38^\circ=13\angle-112.62^\circ$

</details>

**Problem: Try it 3 · Fourth quadrant** (introductory)

Write $z=4-j4$ in polar form.

<details><summary>Solution</summary>

1. 4 right and 4 down: 4th quadrant.
2. The magnitude, by Pythagoras.

   $$c=\sqrt{4^2+(-4)^2}=\sqrt{32}=4\sqrt2\approx5.657$$
3. Reference angle $45^\circ$; in the 4th quadrant measure it clockwise.

   $$\theta=-45^\circ$$

**Answer:** $z=5.657\angle-45^\circ$

</details>

**Problem: Try it 4 · Polar to rectangular** (introductory)

Write $z=6\,e^{j240^\circ}$ in rectangular form.

<details><summary>Solution</summary>

1. Use $a=c\cos\theta$, $b=c\sin\theta$.

   $$\begin{gathered}a=6\cos240^\circ=6(-0.5)=-3, \\ b=6\sin240^\circ=6(-0.866)=-5.196\end{gathered}$$
2. $240^\circ$ is in the 3rd quadrant, and both parts are negative. ✓

   $$z=-3-j5.196$$

**Answer:** $z=-3-j5.196$

</details>

**Problem: Try it 5 · Points on the axes** (introductory)

Write in polar form: (a) $-7$ (b) $j2$ (c) $-j7$.

<details><summary>Solution</summary>

1. (a) 7 to the left on the real axis: distance 7, pointing at $180^\circ$.

   $$-7=7\angle180^\circ$$
2. (b) 2 straight up: $90^\circ$.

   $$j2=2\angle90^\circ$$
3. (c) 7 straight down: $-90^\circ$ (or $270^\circ$).

   $$-j7=7\angle-90^\circ$$

**Answer:** (a) $7\angle180^\circ$ (b) $2\angle90^\circ$ (c) $7\angle-90^\circ$

</details>

**Problem: Try it 6 · Another identity from Euler** (intermediate)

Use $e^{jA}e^{-jB}=e^{j(A-B)}$ to find $\cos(A-B)$ and $\sin(A-B)$.

<details><summary>Solution</summary>

1. $e^{-jB}=\cos(-B)+j\sin(-B)=\cos B-j\sin B$ (cosine is even, sine is odd).

   $$(\cos A+j\sin A)(\cos B-j\sin B)=\cos(A-B)+j\sin(A-B)$$
2. Multiply out, using $j\cdot(-j)=-j^2=+1$.

   $$=(\cos A\cos B+\sin A\sin B)+j(\sin A\cos B-\cos A\sin B)$$
3. Match real and imaginary parts.

   $$\begin{gathered}\cos(A-B)=\cos A\cos B+\sin A\sin B, \\ \sin(A-B)=\sin A\cos B-\cos A\sin B\end{gathered}$$

**Answer:** $\cos(A-B)=\cos A\cos B+\sin A\sin B$, $\sin(A-B)=\sin A\cos B-\cos A\sin B$

</details>

## Topic 2: Complex arithmetic: add, multiply, divide, powers and roots

Each operation is easy in one form and messy in the other, so the whole trick is **pick the right form first**:

- **Adding and subtracting** works like adding arrows tip-to-tail: add the real parts and add the imaginary parts. Use **rectangular** form.
- **Multiplying** multiplies the lengths and **adds the angles** (it stretches and rotates). Dividing divides the lengths and subtracts the angles. Use **polar** form.
- **Powers** repeat a multiplication: raise the length to the power and multiply the angle (*de Moivre's theorem*).
- **Roots**: a $k$-th root has **$k$ different answers**, all the same length, spread evenly around a circle, $360^\circ/k$ apart.

The **complex conjugate** $z^*$ flips the sign of the imaginary part (a mirror image across the real axis). Its superpower: $z\,z^*=a^2+b^2$ is a plain real number, which is how you divide in rectangular form.

> **Tip:** **The method: which form for which job**
> 
> 1. $+$ or $-$: rectangular. $(a_1+jb_1)\pm(a_2+jb_2)=(a_1\pm a_2)+j(b_1\pm b_2)$.
> 2. $\times$ or $\div$: polar (multiply/divide the lengths, add/subtract the angles). In rectangular form you can also multiply out the brackets with $j^2=-1$, and divide by multiplying top and bottom by the conjugate of the bottom.
> 3. Power $z^k$: polar, $c^k\angle k\theta$.
> 4. Roots $z^{1/k}$: polar. Length $c^{1/k}$; first angle $\theta/k$; add $360^\circ/k$ to get each of the other $k-1$ roots.

$$\begin{gathered}z_1z_2=c_1c_2\,e^{j(\theta_1+\theta_2)}, \\ \frac{z_1}{z_2}=\frac{c_1}{c_2}\,e^{j(\theta_1-\theta_2)}, \\ z^k=c^k\,e^{jk\theta}\end{gathered}$$

$$\begin{gathered}z^{1/k}=c^{1/k}\,e^{j\theta/k}\,x_\ell,\quad x_\ell=e^{j\,360^\circ\ell/k}\;(\ell=0,1,\dots,k-1), \\ (a+jb)^*=a-jb,\quad z\,z^*=a^2+b^2\end{gathered}$$

The $x_\ell$ are the *$k$-th roots of 1*: the $k$ points on the unit circle that land on 1 when raised to the $k$-th power (for $k=4$: $1,\ j,\ -1,\ -j$). Multiplying by them is what spaces the roots $360^\circ/k$ apart. Also handy from the conjugate: $z+z^*=2\,\mathrm{Re}\{z\}$ and $z-z^*=j\,2\,\mathrm{Im}\{z\}$.

**Example: Example 6 · Adding and subtracting**

$z_1=3+j4$, $z_2=1-j6$. Find $z_1+z_2$ and $z_1-z_2$.

1. Add real parts with real parts and imaginary with imaginary.

   $$z_1+z_2=(3+1)+j(4-6)=4-j2$$
2. Subtracting: be careful to subtract **both** parts of $z_2$.

   $$z_1-z_2=(3-1)+j(4-(-6))=2+j10$$

**Answer:** $z_1+z_2=4-j2$, $z_1-z_2=2+j10$

**Example: Example 7 · Multiplying in rectangular form**

Find $(2+j3)(4-j)$.

1. Expand the brackets term by term (FOIL), exactly like $(x+y)(u+v)$.

   $$2\cdot4+2(-j)+j3\cdot4+j3(-j)=8-j2+j12-j^2\,3$$
2. Replace $j^2$ with $-1$, so $-j^2\,3=+3$.

   $$=8+3+j(12-2)$$
3. Collect the real numbers ($8+3$) and the $j$ terms ($12-2$).

   $$=11+j10$$

**Answer:** $11+j10$

**Example: Example 8 · Dividing in rectangular form (Lecture Example 1.1)**

Find $\dfrac{80+j18}{8+j10}$.

1. To get rid of $j$ in the bottom, multiply top and bottom by the conjugate of the bottom, $8-j10$. This doesn't change the value (it's multiplying by 1).

   $$\frac{80+j18}{8+j10}\cdot\frac{8-j10}{8-j10}$$
2. The bottom becomes a real number: $z\,z^*=a^2+b^2$.

   $$(8+j10)(8-j10)=64+100=164$$
3. Multiply out the top with $j^2=-1$.

   $$(80+j18)(8-j10)=640-j800+j144-j^2\,180=820-j656$$
4. Divide each part by 164.

   $$\frac{820-j656}{164}=5-j4$$

**Answer:** $5-j4$

**Example: Example 9 · Multiplying and dividing in polar form**

Find $(6\angle40^\circ)(2\angle-70^\circ)$ and $\dfrac{6\angle40^\circ}{2\angle-70^\circ}$.

1. Multiplying: multiply the lengths, **add** the angles.

   $$(6)(2)\angle(40^\circ+(-70^\circ))=12\angle-30^\circ$$
2. Dividing: divide the lengths, **subtract** the angles (top minus bottom).

   $$\frac{6}{2}\angle(40^\circ-(-70^\circ))=3\angle110^\circ$$

**Answer:** $12\angle-30^\circ$ and $3\angle110^\circ$

**Example: Example 10 · A big power: de Moivre's theorem**

Find $(1+j)^8$.

1. Multiplying $1+j$ by itself 8 times is painful. In polar form it's one step. First convert: 1 right, 1 up.

   $$1+j=\sqrt2\angle45^\circ$$
2. Raise the length to the 8th power and multiply the angle by 8.

   $$(\sqrt2)^8\angle(8\times45^\circ)=16\angle360^\circ$$
3. $360^\circ$ is a full turn, the same direction as $0^\circ$: pointing along the positive real axis.

   $$16\angle360^\circ=16$$

**Answer:** $(1+j)^8=16$

**Example: Example 11 · All four fourth roots (Lecture Example 1.2)**

Find all fourth roots of $z=81\,e^{j60^\circ}$.

1. Here $c=81$, $\theta=60^\circ$ and $k=4$. The length of every root is the 4th root of 81.

   $$81^{1/4}=3$$
2. The first root's angle is the angle divided by 4.

   $$\frac{60^\circ}{4}=15^\circ\quad\Rightarrow\quad 3\,e^{j15^\circ}$$
3. The other three are spaced $360^\circ/4=90^\circ$ apart (that's multiplying by the fourth roots of 1: $1, j, -1, -j$).

   $$3e^{j15^\circ},\quad 3e^{j105^\circ},\quad 3e^{j195^\circ},\quad 3e^{j285^\circ}$$
4. Check one: $(3e^{j105^\circ})^4=81\,e^{j420^\circ}=81\,e^{j60^\circ}$ because $420^\circ-360^\circ=60^\circ$. ✓

**Answer:** $3e^{j15^\circ},\ 3e^{j105^\circ},\ 3e^{j195^\circ},\ 3e^{j285^\circ}$

![The four fourth roots of $81e^{j60^\circ}$ sit on a circle of radius 3, starting at $15^\circ$ and spaced $90^\circ$ apart. Every $k$-th root problem looks like this: $k$ equally spaced points on one circle.](/figures/elec231/w1_roots.svg)

*The four fourth roots of $81e^{j60^\circ}$ sit on a circle of radius 3, starting at $15^\circ$ and spaced $90^\circ$ apart. Every $k$-th root problem looks like this: $k$ equally spaced points on one circle.*

> **Info:** **Algebra reminder: the quadratic formula** $as^2+bs+c=0\;\Rightarrow\;s=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$. When $b^2-4ac$ is negative, take the square root of the positive number and attach a $j$: $\sqrt{-16}=\sqrt{16}\,\sqrt{-1}=j4$.

**Example: Example 12 · Why we need all this: complex roots of a quadratic**

Solve $s^2+2s+5=0$. (In Week 5 this equation comes from the ODE $y''+2y'+5y=0$.)

1. Use the quadratic formula with $a=1$, $b=2$, $c=5$.

   $$s=\frac{-2\pm\sqrt{4-20}}{2}=\frac{-2\pm\sqrt{-16}}{2}$$
2. The number under the root is negative, so the roots are complex: $\sqrt{-16}=\sqrt{16}\,\sqrt{-1}=j4$.

   $$s=\frac{-2\pm j4}{2}=-1\pm j2$$
3. The roots always come as a **conjugate pair** ($-1+j2$ and $-1-j2$) when the equation has real coefficients.

**Answer:** $s=-1\pm j2$

> **Warning:** **Common mistakes**
> 
> - Adding in polar form: $5\angle0^\circ+5\angle90^\circ$ is **not** $10\angle90^\circ$. Convert to rectangular first ($5+j5$).
> - Forgetting $j^2=-1$ when expanding brackets (a sign error on the real part).
> - Roots: giving only one answer. A $k$-th root has $k$ answers, $360^\circ/k$ apart, and the first angle is $\theta/k$ (divide the angle too!).
> - The conjugate in polar form flips the **angle**: $(c\,e^{j\theta})^*=c\,e^{-j\theta}$.

**Problem: Try it 7 · Subtract and multiply** (introductory)

$z_1=5-j2$, $z_2=-3+j7$. Find $z_1-z_2$ and $z_1z_2$.

<details><summary>Solution</summary>

1. Subtract real from real and imaginary from imaginary; subtracting $-3$ adds 3, and subtracting $j7$ takes 7 off the imaginary part.

   $$z_1-z_2=(5+3)+j(-2-7)=8-j9$$
2. Expand the brackets term by term: $5(-3)$, $5(j7)$, $(-j2)(-3)$ and $(-j2)(j7)$.

   $$(5-j2)(-3+j7)=-15+j35+j6-j^2\,14$$
3. Replace $j^2$ by $-1$, so $-j^2\,14=+14$, then collect real and imaginary parts.

   $$=-15+14+j41=-1+j41$$

**Answer:** $z_1-z_2=8-j9$, $z_1z_2=-1+j41$

</details>

**Problem: Try it 8 · Divide with the conjugate** (introductory)

Find $\dfrac{10+j5}{3-j4}$ in rectangular form.

<details><summary>Solution</summary>

1. Multiply top and bottom by $3+j4$, the conjugate of the bottom.

   $$\frac{(10+j5)(3+j4)}{(3-j4)(3+j4)}$$
2. Bottom: $3^2+4^2=25$. Top: expand with $j^2=-1$.

   $$(10+j5)(3+j4)=30+j40+j15+j^2\,20=10+j55$$
3. Divide both the real and the imaginary part by 25.

   $$\frac{10+j55}{25}=0.4+j2.2$$

**Answer:** $0.4+j2.2$

</details>

**Problem: Try it 9 · Powers of j** (introductory)

Simplify (a) $\dfrac1j$ (b) $j^3$ (c) $j^{10}$.

<details><summary>Solution</summary>

1. (a) Multiply top and bottom by $-j$: the bottom becomes $j(-j)=-j^2=1$.

   $$\frac1j=\frac{-j}{1}=-j$$
2. (b) $j^3=j^2\cdot j$.

   $$j^3=(-1)j=-j$$
3. (c) The powers of $j$ repeat every 4 ($j, -1, -j, 1$). $10=8+2$, so $j^{10}=j^2$.

   $$j^{10}=(j^4)^2j^2=1\cdot(-1)=-1$$

**Answer:** (a) $-j$ (b) $-j$ (c) $-1$

</details>

**Problem: Try it 10 · A sixth power** (intermediate)

Find $(1-j\sqrt3)^6$.

<details><summary>Solution</summary>

1. Convert: 1 right, $\sqrt3$ down (4th quadrant).

   $$1-j\sqrt3=2\angle-60^\circ$$
2. de Moivre: length to the 6th, angle times 6.

   $$2^6\angle(6\times-60^\circ)=64\angle-360^\circ$$
3. $-360^\circ$ is a full turn, pointing along the positive real axis.

   $$=64$$

**Answer:** $64$

</details>

**Problem: Try it 11 · Cube roots** (intermediate)

Find all three cube roots of $j8$, in polar and rectangular form.

<details><summary>Solution</summary>

1. Write $j8$ in polar form: 8 straight up.

   $$j8=8\angle90^\circ$$
2. Length $8^{1/3}=2$; first angle $90^\circ/3=30^\circ$; spacing $360^\circ/3=120^\circ$.

   $$2\angle30^\circ,\quad 2\angle150^\circ,\quad 2\angle270^\circ$$
3. Convert each with $a=c\cos\theta$, $b=c\sin\theta$.

   $$\sqrt3+j,\quad -\sqrt3+j,\quad -j2$$

**Answer:** $2\angle30^\circ=\sqrt3+j$, $2\angle150^\circ=-\sqrt3+j$, $2\angle270^\circ=-j2$

</details>

**Problem: Try it 12 · Conjugate facts** (introductory)

For $z=3-j4$ find $z^*$, $zz^*$, $z+z^*$ and $z-z^*$.

<details><summary>Solution</summary>

1. The conjugate flips the sign of the imaginary part (mirror image across the real axis).

   $$z^*=3+j4$$
2. A number times its conjugate is $a^2+b^2$ (the $j$ terms cancel), with $a=3$, $b=-4$.

   $$zz^*=3^2+(-4)^2=25$$
3. $z+z^*=2\,\mathrm{Re}\{z\}$ and $z-z^*=j\,2\,\mathrm{Im}\{z\}$ with $\mathrm{Im}\{z\}=-4$.

   $$z+z^*=6,\qquad z-z^*=-j8$$

**Answer:** $z^*=3+j4$, $zz^*=25$, $z+z^*=6$, $z-z^*=-j8$

</details>

**Problem: Try it 13 · Complex roots of a quadratic** (introductory)

Solve $s^2+4s+13=0$.

<details><summary>Solution</summary>

1. Quadratic formula with $a=1$, $b=4$, $c=13$.

   $$s=\frac{-4\pm\sqrt{16-52}}{2}=\frac{-4\pm\sqrt{-36}}{2}$$
2. The number under the root is negative: $\sqrt{-36}=\sqrt{36}\,\sqrt{-1}=j6$. Then divide both parts by 2.

   $$s=\frac{-4\pm j6}{2}=-2\pm j3$$

**Answer:** $s=-2\pm j3$

</details>

## Topic 3: Your first differential equation: the RL natural response

A **differential equation** is an equation that involves an unknown *function* and its *derivatives*. Solving it means finding the whole function, e.g. the current $i(t)$ at every time $t$.

Inductors create them because an inductor's voltage depends on how fast its current changes: $v_L=L\dfrac{di}{dt}$ ($L$ is the *inductance* in henries). Two facts from the lecture that you will use all term:

- **An inductor's current cannot jump:** $i(0^-)=i(0^+)$ (just before and just after a switch moves).
- **In DC steady state an inductor acts like a short circuit** (a plain wire): nothing changes, so $\dfrac{di}{dt}=0$ and $v_L=0$.

In the circuit below the switch has been closed for a long time, so the inductor is a short and carries all of $I_s$. At $t=0$ the switch opens. The inductor's current can't stop instantly, so it keeps flowing round the loop through $R$, and $R$ slowly burns the energy off. Kirchhoff's voltage law (KVL) around that loop says the voltages add to zero:

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

$$L\frac{di}{dt}+Ri=0\quad\Longleftrightarrow\quad \frac{di}{dt}=-\frac{R}{L}\,i$$

Read it in words: *the current shrinks at a rate proportional to how big it is.* Big current → fast drop; small current → slow drop. The only function that behaves like that is a **decaying exponential**:

$$\begin{gathered}i(t)=i(0)\,e^{-t/\tau}, \\ \tau=\frac{L}{R}\quad(\text{the time constant, in seconds})\end{gathered}$$

$\tau$ (tau) is the *time constant*. After one $\tau$ the current is $e^{-1}\approx0.37$ of its start (it has lost 63%); after $5\tau$ it is under 1%, which engineers call "done". A bigger $L$ (more stored energy) or a smaller $R$ (less resistance to burn it) makes $\tau$ longer.

![Every RL (and RC) natural response has this one shape. Measure time in time constants: after $1\tau$ 37% is left, after $5\tau$ less than 1%.](/figures/elec231/w1_tau.svg)

*Every RL (and RC) natural response has this one shape. Measure time in time constants: after $1\tau$ 37% is left, after $5\tau$ less than 1%.*

> **Tip:** **The method: RL natural response**
> 
> 1. **Before the switch** ($t<0$, settled): replace $L$ by a wire and find the inductor current $i(0^-)$.
> 2. **The jump rule:** $i(0^+)=i(0^-)$. Call it $I_0$.
> 3. **After the switch:** find the resistance $R$ the inductor sees (only what is still connected to it).
> 4. Write KVL: $L\dfrac{di}{dt}+Ri=0$. The solution is $i(t)=I_0e^{-t/\tau}$ with $\tau=L/R$.
> 5. Get anything else from $i$: e.g. the resistor voltage $v=Ri$ (sign from the drawn $+/-$ and current arrow).

> **Info:** **Calculus reminder** (you need these four facts to solve the equation yourself):
> 
> - $\dfrac{d}{dt}e^{at}=a\,e^{at}$: the derivative of an exponential is the same exponential times the number in front of $t$.
> - $\displaystyle\int\frac{dx}{x}=\ln|x|+C$.
> - $\ln A-\ln B=\ln\dfrac AB$.
> - $\ln A=B$ means $A=e^B$ (take $e$ to the power of both sides).

**Example: Example 13 · Solve the simplest ODE: dy/dt + y = 0**

Solve $\dfrac{dy}{dt}+y=0$ with $y(0)=y_0$, then check the answer.

1. Move $y$ to the other side so the derivative is alone.

   $$\frac{dy}{dt}=-y$$
2. **Separate the variables**: get everything with $y$ on the left and everything with $t$ on the right (divide by $y$, multiply by $dt$).

   $$\frac{dy}{y}=-dt$$
3. Integrate both sides. On the left use $\int dx/x=\ln|x|$; only one $+C$ is needed.

   $$\ln|y|=-t+C$$
4. Undo the logarithm by raising $e$ to both sides: $|y|=e^{-t+C}=e^C e^{-t}$. Dropping the absolute value allows either sign, so $y=\pm e^{C}e^{-t}$; call the constant $A=\pm e^{C}$ (it can be positive or negative).

   $$y=A\,e^{-t}$$
5. Use the initial condition: at $t=0$, $e^0=1$, so $A=y_0$.

   $$y(t)=y_0\,e^{-t}$$
6. **Check** by putting it back into the equation: $\dfrac{dy}{dt}=-y_0e^{-t}$, and adding $y=y_0e^{-t}$ gives 0. ✓

   $$\frac{dy}{dt}+y=-y_0e^{-t}+y_0e^{-t}=0$$

**Answer:** $y(t)=y_0\,e^{-t}$

**Example: Example 14 · Where the e comes from (lecture outline)**

Without calculus: why does $\dfrac{dy}{dt}+y=0$ give $y=y_0e^{-t}$? Use a tiny time step $\Delta$.

1. Replace the derivative by a slope over a tiny step $\Delta$: (value now − value a moment ago) ÷ $\Delta$.

   $$\frac{y(t)-y(t-\Delta)}{\Delta}+y(t)\approx0$$
2. Multiply by $\Delta$ and rearrange. Each step the value gets divided by $(1+\Delta)$.

   $$y(t)\,(1+\Delta)=y(t-\Delta)$$
3. Repeat from $t=0$: after $k=t/\Delta$ steps you have divided by $(1+\Delta)$ $k$ times.

   $$y(t)=y(0)\,(1+\Delta)^{-t/\Delta}$$
4. As the steps get tiny, $(1+\Delta)^{1/\Delta}$ approaches the number $e\approx2.718$ (that is one definition of $e$).

   $$y(t)=y(0)\Big[(1+\Delta)^{1/\Delta}\Big]^{-t}\;\to\;y(0)\,e^{-t}$$

**Answer:** Shrinking by the same small fraction every instant is exactly what $e^{-t}$ does.

**Example: Example 15 · The general RL loop (Lecture 1)**

Solve $L\dfrac{di}{dt}+Ri=0$ with $i(0)=I_s$.

1. Divide by $L$ and separate: currents on the left, time on the right.

   $$\frac{di}{i}=-\frac{R}{L}\,dt$$
2. Integrate from the start (time $0$, current $i(0)$) to a general time $t$ (current $i(t)$). Definite integrals mean no $+C$. ($x$ and $s$ are just placeholder names for current and time inside the integrals, so they don't clash with the limits.)

   $$\int_{i(0)}^{i(t)}\frac{dx}{x}=-\frac{R}{L}\int_0^t ds$$
3. Evaluate both sides and combine the logs.

   $$\ln i(t)-\ln i(0)=\ln\frac{i(t)}{i(0)}=-\frac{R}{L}\,t$$
4. Exponentiate both sides and multiply by $i(0)=I_s$.

   $$\begin{gathered}i(t)=I_s\,e^{-(R/L)t}=I_s\,e^{-t/\tau}, \\ \tau=\frac{L}{R}\end{gathered}$$

**Answer:** $i(t)=I_s\,e^{-t/\tau}$ with $\tau=L/R$

**Example: Example 16 · Pre-tutorial 1: numbers in the RL loop**

In the circuit above, $L=8\,\mathrm{mH}$, $R=4\,\Omega$ and $I_s=4\,\mathrm{A}$. Find $i(t)$ for $t\ge0$, sketch it, and find $v(t)$.

1. Before the switch opens, the inductor is a short, so it carries the whole source current. The current can't jump.

   $$i(0^+)=i(0^-)=I_s=4\,\mathrm{A}$$
2. After the switch opens, the inductor only sees $R=4\,\Omega$ ($R_0$ and the source are cut off). Convert mH to H.

   $$\tau=\frac{L}{R}=\frac{8\times10^{-3}}{4}=2\times10^{-3}\,\mathrm{s}=2\,\mathrm{ms}$$
3. $1/\tau=500\,\mathrm{s^{-1}}$, so $e^{-t/\tau}=e^{-500t}$.

   $$i(t)=4\,e^{-500t}\,\mathrm{A},\quad t\ge0$$
4. The current goes up through $L$ and comes down through $R$ from $+$ to $-$, so $v=Ri$.

   $$v(t)=4\cdot4e^{-500t}=16\,e^{-500t}\,\mathrm{V}$$
5. Sketch points: starts at 4 A, is $4(0.37)=1.47\,\mathrm{A}$ at $t=2\,\mathrm{ms}$, and is essentially 0 after $5\tau=10\,\mathrm{ms}$ (see the plot).

**Answer:** $\tau=2\,\mathrm{ms}$, $i(t)=4e^{-500t}\,\mathrm{A}$, $v(t)=16e^{-500t}\,\mathrm{V}$

**Example: Example 17 · How long until it is small?**

An RL loop has $L=0.5\,\mathrm{H}$, $R=100\,\Omega$ and $i(0)=10\,\mathrm{A}$. When is $i=1\,\mathrm{A}$?

1. Compute $\tau=L/R$, then write the natural response $i=i(0)e^{-t/\tau}$; note $1/\tau=1/0.005=200\,\mathrm{s^{-1}}$.

   $$\begin{gathered}\tau=\frac{0.5}{100}=0.005\,\mathrm{s}=5\,\mathrm{ms}, \\ i(t)=10e^{-t/0.005}=10e^{-200t}\,\mathrm{A}\end{gathered}$$
2. Set $i=1$ and isolate the exponential.

   $$10e^{-200t}=1\;\Rightarrow\;e^{-200t}=0.1$$
3. Take $\ln$ of both sides ($\ln e^{x}=x$).

   $$-200t=\ln0.1=-2.303$$
4. Solve. A neat shortcut: the time to fall to a fraction $f$ is $\tau\ln(1/f)$.

   $$t=\frac{2.303}{200}=11.5\,\mathrm{ms}=\tau\ln10$$

**Answer:** $t=\tau\ln10\approx11.5\,\mathrm{ms}$

> **Warning:** **Common mistakes**
> 
> - $\tau=L/R$, not $R/L$. Check units: henries ÷ ohms = seconds.
> - Using a resistor that is no longer connected after the switch moves (here $R_0$). $R$ is what the inductor sees **after** switching.
> - Mixing ms and s: convert $L$ in mH to H first, then $\tau$ comes out in seconds.
> - Forgetting to check the answer: put $i(t)$ back into $L\,di/dt+Ri$ and you must get 0, and $i(0)$ must match.

**Problem: Try it 14 · Solve and check** (introductory)

Solve $\dfrac{dy}{dt}=-3y$ with $y(0)=5$, and check your answer.

<details><summary>Solution</summary>

1. Separate the variables: divide both sides by $y$ and multiply by $dt$, so $y$ is on the left and $t$ on the right.

   $$\frac{dy}{y}=-3\,dt$$
2. Integrate both sides ($\int dy/y=\ln|y|$, $\int -3\,dt=-3t$), add one constant, then raise $e$ to both sides; the constant $A=\pm e^{C}$ can have either sign.

   $$\ln|y|=-3t+C\;\Rightarrow\;|y|=e^{C}e^{-3t}\;\Rightarrow\;y=Ae^{-3t}$$
3. Use the initial condition: at $t=0$, $e^0=1$, so $y(0)=A=5$.

   $$y(t)=5e^{-3t}$$
4. Check: $\dfrac{dy}{dt}=-15e^{-3t}=-3(5e^{-3t})=-3y$ ✓ and $y(0)=5$ ✓.

**Answer:** $y(t)=5e^{-3t}$

</details>

**Problem: Try it 15 · An RL loop with numbers** (introductory)

An RL loop has $L=2\,\mathrm{H}$, $R=10\,\Omega$ and $i(0)=3\,\mathrm{A}$. Find $\tau$, $i(t)$ and $i(0.2\,\mathrm{s})$.

<details><summary>Solution</summary>

1. The time constant of an RL loop is $\tau=L/R$.

   $$\tau=\frac{2}{10}=0.2\,\mathrm{s}$$
2. The natural response starts at $i(0)=3\,\mathrm{A}$ and decays with that $\tau$; $1/0.2=5$.

   $$i(t)=3e^{-t/0.2}=3e^{-5t}\,\mathrm{A}$$
3. At $t=0.2\,\mathrm{s}=\tau$: 37% of the start.

   $$i(0.2)=3e^{-1}=1.10\,\mathrm{A}$$

**Answer:** $\tau=0.2\,\mathrm{s}$, $i(t)=3e^{-5t}\,\mathrm{A}$, $i(0.2)=1.10\,\mathrm{A}$

</details>

**Problem: Try it 16 · Work backwards** (introductory)

A measured inductor current is $i(t)=6e^{-250t}\,\mathrm{A}$ and the resistor is $R=50\,\Omega$. Find $i(0)$, $\tau$ and $L$.

<details><summary>Solution</summary>

1. At $t=0$ the exponential is 1.

   $$i(0)=6\,\mathrm{A}$$
2. The exponent is $-t/\tau$, so $1/\tau=250$.

   $$\tau=\frac{1}{250}=4\,\mathrm{ms}$$
3. Rearrange $\tau=L/R$ to get $L=\tau R$ (time in seconds: $4\,\mathrm{ms}=0.004\,\mathrm{s}$).

   $$L=(0.004)(50)=0.2\,\mathrm{H}$$

**Answer:** $i(0)=6\,\mathrm{A}$, $\tau=4\,\mathrm{ms}$, $L=0.2\,\mathrm{H}$

</details>

**Problem: Try it 17 · How many time constants?** (introductory)

How many time constants does it take an RL current to fall to 1% of its starting value?

<details><summary>Solution</summary>

1. 1% of the start means the factor $e^{-t/\tau}$ has dropped to $0.01$ (the starting value cancels).

   $$I_0e^{-t/\tau}=0.01\,I_0\;\Rightarrow\;e^{-t/\tau}=0.01$$
2. Take $\ln$ of both sides; $\ln(e^x)=x$ brings the exponent down.

   $$-\frac{t}{\tau}=\ln0.01=-4.605$$
3. So about $4.6\tau$, which is why "$5\tau$" is used as the rule of thumb for "finished".

   $$t=4.6\,\tau$$

**Answer:** $t=\tau\ln100\approx4.6\,\tau$

</details>

**Problem: Try it 18 · The full switching problem** (intermediate)

In the lecture circuit (switch closed for a long time, opens at $t=0$): $I_s=2\,\mathrm{A}$, $R_0=10\,\Omega$, $L=40\,\mathrm{mH}$, $R=20\,\Omega$. Find $i(t)$ and $v(t)$ for $t\ge0$.

<details><summary>Solution</summary>

1. Before: the inductor is a short, which also shorts out $R_0$ and $R$, so it carries all of $I_s$.

   $$i(0^-)=2\,\mathrm{A}=i(0^+)$$
2. After: only $R=20\,\Omega$ is connected to $L$; $R_0$ plays no part.

   $$\tau=\frac{0.04}{20}=2\,\mathrm{ms}$$
3. The natural response starts at $2\,\mathrm{A}$; $1/\tau=1/0.002=500\,\mathrm{s^{-1}}$.

   $$i(t)=2e^{-500t}\,\mathrm{A}$$
4. The current flows down through $R$ from $+$ to $-$, so Ohm's law gives $v=Ri$.

   $$v(t)=20\,i=40e^{-500t}\,\mathrm{V}$$

**Answer:** $i(t)=2e^{-500t}\,\mathrm{A}$, $v(t)=40e^{-500t}\,\mathrm{V}$

</details>

**Problem: Try it 19 · Write the ODE yourself** (intermediate)

A $0.1\,\mathrm{H}$ inductor carrying $2\,\mathrm{A}$ is suddenly connected across a $5\,\Omega$ resistor at $t=0$. Write the differential equation for $i(t)$ and solve it by separating variables.

<details><summary>Solution</summary>

1. KVL around the loop: the inductor voltage $L\,di/dt$ plus the resistor voltage $Ri$ add to zero. Divide by $0.1$.

   $$0.1\frac{di}{dt}+5i=0\;\Rightarrow\;\frac{di}{dt}=-50i$$
2. Separate ($i$ left, $t$ right), integrate both sides, and raise $e$ to both sides; $A=\pm e^{C}$ is a constant of either sign.

   $$\frac{di}{i}=-50\,dt\;\Rightarrow\;\ln|i|=-50t+C\;\Rightarrow\;i=Ae^{-50t}$$
3. Initial condition $i(0)=2$ gives $A=2$. (Check: $\tau=L/R=0.02\,\mathrm{s}=1/50$ ✓)

   $$i(t)=2e^{-50t}\,\mathrm{A}$$

**Answer:** $0.1\,\dfrac{di}{dt}+5i=0$, $i(t)=2e^{-50t}\,\mathrm{A}$

</details>

## Mixed practice (exam style)

Mixed topics, like the midterm. Try each one before opening the solution.

**Problem: Practice 1 · Multiply and divide two ways** (intermediate)

$z_1=2+j2$ and $z_2=1-j\sqrt3$.

1. Write both in polar form.
2. Find $z_1z_2$ and $z_1/z_2$ in polar and rectangular form.

<details><summary>Solution</summary>

1. Convert. $z_1$: 1st quadrant. $z_2$: 1 right, $\sqrt3$ down, 4th quadrant.

   $$z_1=2\sqrt2\angle45^\circ,\qquad z_2=2\angle-60^\circ$$
2. Product: multiply lengths, add angles.

   $$z_1z_2=4\sqrt2\angle-15^\circ=5.657(\cos15^\circ-j\sin15^\circ)=5.464-j1.464$$
3. Quotient: divide lengths, subtract angles.

   $$\frac{z_1}{z_2}=\sqrt2\angle105^\circ=1.414(\cos105^\circ+j\sin105^\circ)=-0.366+j1.366$$

**Answer:** $z_1z_2=5.657\angle-15^\circ=5.464-j1.464$; $z_1/z_2=1.414\angle105^\circ=-0.366+j1.366$

</details>

**Problem: Practice 2 · Solve a cubic** (intermediate)

Find all solutions of $z^3=-27$.

<details><summary>Solution</summary>

1. Write $-27$ in polar form: 27 to the left.

   $$-27=27\angle180^\circ$$
2. Length $27^{1/3}=3$; first angle $180^\circ/3=60^\circ$; spacing $120^\circ$.

   $$3\angle60^\circ,\quad3\angle180^\circ,\quad3\angle300^\circ$$
3. Convert each with $a=3\cos\theta$, $b=3\sin\theta$ ($\cos60^\circ=0.5$, $\sin60^\circ=0.866$).

   $$1.5+j2.598,\qquad -3,\qquad 1.5-j2.598$$

**Answer:** $z=3\angle60^\circ,\ 3\angle180^\circ=-3,\ 3\angle300^\circ$, i.e. $1.5\pm j2.598$ and $-3$

</details>

**Problem: Practice 3 · Double-angle formulas** (intermediate)

Use $e^{j2\theta}=(e^{j\theta})^2$ to show $\cos2\theta=\cos^2\theta-\sin^2\theta$ and $\sin2\theta=2\sin\theta\cos\theta$.

<details><summary>Solution</summary>

1. Write both sides with Euler.

   $$\cos2\theta+j\sin2\theta=(\cos\theta+j\sin\theta)^2$$
2. Square the right side with $j^2=-1$.

   $$=\cos^2\theta+j2\sin\theta\cos\theta-\sin^2\theta$$
3. Match real and imaginary parts.

   $$\begin{gathered}\cos2\theta=\cos^2\theta-\sin^2\theta, \\ \sin2\theta=2\sin\theta\cos\theta\end{gathered}$$

**Answer:** Shown by matching real and imaginary parts.

</details>

**Problem: Practice 4 · RL with every question asked** (intermediate)

In the lecture RL circuit, $I_s=5\,\mathrm{A}$, $L=20\,\mathrm{mH}$ and $R=8\,\Omega$ (the switch opens at $t=0$).

1. Find $\tau$, $i(t)$ and $v(t)=Ri$.
2. Find $i$ at $t=5\,\mathrm{ms}$.
3. When is $i=1\,\mathrm{A}$?

<details><summary>Solution</summary>

1. $i(0^+)=i(0^-)=I_s=5\,\mathrm{A}$ (inductor was a short).

   $$\tau=\frac{0.02}{8}=2.5\,\mathrm{ms}$$
2. Write the natural response with $1/\tau=1/0.0025=400\,\mathrm{s^{-1}}$; the resistor voltage is $v=Ri$.

   $$\begin{gathered}i(t)=5e^{-400t}\,\mathrm{A}, \\ v(t)=8i=40e^{-400t}\,\mathrm{V}\end{gathered}$$
3. Put $t=0.005\,\mathrm{s}$ in (that is $2\tau$, so the exponent is $-2$).

   $$i(0.005)=5e^{-400(0.005)}=5e^{-2}=0.677\,\mathrm{A}$$
4. Set $5e^{-400t}=1$: divide by 5 to isolate the exponential, take $\ln$ of both sides ($\ln\tfrac15=-\ln5$), then divide by $-400$.

   $$e^{-400t}=\tfrac15\;\Rightarrow\;-400t=-\ln5\;\Rightarrow\;t=\frac{\ln5}{400}=4.02\,\mathrm{ms}$$

**Answer:** $\tau=2.5\,\mathrm{ms}$, $i=5e^{-400t}\,\mathrm{A}$, $v=40e^{-400t}\,\mathrm{V}$; $i(5\,\mathrm{ms})=0.677\,\mathrm{A}$; $t=4.02\,\mathrm{ms}$

</details>

**Problem: Practice 5 · Euler warm-up** (introductory)

Evaluate (a) $e^{j\pi}+1$ (b) $|e^{j3}|$ (c) $\mathrm{Re}\{4e^{j\pi/6}\}$.

<details><summary>Solution</summary>

1. (a) $e^{j\pi}=\cos\pi+j\sin\pi=-1$.

   $$e^{j\pi}+1=0$$
2. (b) Every $e^{j\theta}$ has length 1, whatever $\theta$ is.

   $$|e^{j3}|=1$$
3. (c) The real part is $c\cos\theta$ with $\theta=\pi/6=30^\circ$.

   $$4\cos30^\circ=3.464$$

**Answer:** (a) $0$ (b) $1$ (c) $3.464$

</details>

**Problem: Practice 6 · A messy expression** (intermediate)

Find $\dfrac{(3+j4)^2}{1-j}$ in rectangular form.

<details><summary>Solution</summary>

1. Square the top first.

   $$(3+j4)^2=9+j24+j^2\,16=-7+j24$$
2. Divide by $1-j$: multiply top and bottom by $1+j$; the bottom becomes $1+1=2$.

   $$\frac{(-7+j24)(1+j)}{2}=\frac{-7-j7+j24+j^2\,24}{2}$$
3. Simplify with $j^2=-1$.

   $$=\frac{-31+j17}{2}=-15.5+j8.5$$

**Answer:** $-15.5+j8.5$

</details>

**Problem: Practice 7 · Roots in polar form** (introductory)

Solve $s^2+6s+25=0$ and write both roots in polar form.

<details><summary>Solution</summary>

1. Quadratic formula with $a=1$, $b=6$, $c=25$; the number under the root is negative.

   $$s=\frac{-6\pm\sqrt{36-100}}{2}=\frac{-6\pm\sqrt{-64}}{2}$$
2. $\sqrt{-64}=\sqrt{64}\,\sqrt{-1}=j8$; divide both parts by 2.

   $$s=\frac{-6\pm j8}{2}=-3\pm j4$$
3. $-3+j4$ is in the 2nd quadrant: length 5, reference angle $53.13^\circ$.

   $$-3+j4=5\angle126.87^\circ$$
4. The other root is the conjugate: same length, angle with the opposite sign (mirror image across the real axis).

   $$-3-j4=5\angle-126.87^\circ$$

**Answer:** $s=-3\pm j4=5\angle\pm126.87^\circ$

</details>

**Problem: Practice 8 · Read the time constant from data** (intermediate)

In an RL loop with $R=10\,\Omega$, the current is $2\,\mathrm{A}$ at $t=0$ and $0.736\,\mathrm{A}$ at $t=1\,\mathrm{ms}$. Find $\tau$ and $L$.

<details><summary>Solution</summary>

1. $0.736/2=0.368=e^{-1}$, so 1 ms is exactly one time constant.

   $$e^{-0.001/\tau}=0.368\;\Rightarrow\;\tau=1\,\mathrm{ms}$$
2. Rearrange $\tau=L/R$ to $L=\tau R$.

   $$L=(0.001)(10)=10\,\mathrm{H}\times10^{-3}=10\,\mathrm{mH}$$

**Answer:** $\tau=1\,\mathrm{ms}$, $L=10\,\mathrm{mH}$

</details>

## Summary

| Problem type | How to recognise it | What to do |
|---|---|---|
| Rectangular → polar | given $a+jb$, asked for $c\angle\theta$ or $ce^{j\theta}$ | sketch; $c=\sqrt{a^2+b^2}$; reference angle; fix the quadrant |
| Polar → rectangular | given $c\angle\theta$ or $ce^{j\theta}$ | $a=c\cos\theta$, $b=c\sin\theta$ |
| Add / subtract | $z_1\pm z_2$ | rectangular: add the parts |
| Multiply / divide | $z_1z_2$, $z_1/z_2$ | polar: multiply/divide lengths, add/subtract angles (or expand with $j^2=-1$; divide using the conjugate) |
| Power | $z^k$ | polar: $c^k\angle k\theta$ |
| Roots | $z^{1/k}$ or "solve $z^k=w$" | $k$ answers: length $c^{1/k}$, angles $\theta/k+360^\circ\ell/k$ |
| Trig identity | "use Euler to show…" | write both sides with $e^{j\theta}=\cos\theta+j\sin\theta$, expand, match real and imaginary parts |
| RL natural response | switch disconnects the source; an inductor is left with a resistor | $i(0^+)=i(0^-)$ (L = short before); $\tau=L/R$; $i=I_0e^{-t/\tau}$ |

| Formula | Meaning |
|---|---|
| $e^{j\theta}=\cos\theta+j\sin\theta$ | Euler's identity: the unit-circle point at angle $\theta$ |
| $z\,z^*=a^2+b^2=c^2$ | a number times its conjugate is real |
| $L\dfrac{di}{dt}+Ri=0$ | KVL for the source-free RL loop |
| $i(t)=I_0e^{-t/\tau},\ \tau=L/R$ | 37% left after $\tau$, under 1% after $5\tau$ |
| time to fall to fraction $f$ | $t=\tau\ln(1/f)$ |
