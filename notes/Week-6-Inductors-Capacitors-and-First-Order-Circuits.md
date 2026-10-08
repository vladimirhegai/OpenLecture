# Week 6: Inductors, Capacitors and First-Order Circuits

## Overview

> **Info:** Week 6 introduces the two energy-storage elements: the inductor, whose voltage depends on how fast its current changes, and the capacitor, whose current depends on how fast its voltage changes. We then combine them in series and parallel and begin first-order circuits, where a single equivalent $L$ or $C$ discharges or charges through a resistance with time constant $\tau$.

- Use $v = L\,\dfrac{di}{dt}$ and $i = C\,\dfrac{dv}{dt}$ (and their integral forms) with correct reference directions.
- Compute instantaneous power and stored energy $w = \tfrac{1}{2}Li^2$ and $w = \tfrac{1}{2}Cv^2$, and say when an element stores or delivers energy.
- Explain why inductor current and capacitor voltage cannot change instantaneously, and treat $L$ as a short and $C$ as an open at DC.
- Reduce series and parallel inductors and capacitors to one equivalent element, including its initial condition.
- Find the natural response of RL and RC circuits and interpret the time constant $\tau$.
- Find the step response of RL and RC circuits with the form $x(\infty) + [x(0^+) - x(\infty)]e^{-\frac{t}{\tau}}$.

## Topic 1: Inductors

An inductor is a coil of wire. A changing current through it produces a changing magnetic flux, and that changing flux induces a voltage across its terminals. Its parameter is the inductance $L$, measured in henries (H). With the passive sign convention, the reference current enters the terminal marked $+$. The formulas here assume ideal linear elements with constant positive inductance and capacitance; combined inductors have no mutual magnetic coupling.

```schematic
terminal 0,3
L1 0,3 -> 0,0 "$L$" i="$i$" v="$v$"
terminal 0,0
```

$$v = L\,\frac{di}{dt}$$

Here $v$ is the terminal voltage in volts, $i$ is the inductor current in amperes, and $L$ is the inductance in henries. If the reference current enters the $-$ terminal instead, the relation becomes $v = -L\,\dfrac{di}{dt}$. A constant current gives $\dfrac{di}{dt} = 0$, so $v = 0$.

$$i(t) = \frac{1}{L}\int_{t_0}^{t} v(\tau)\,d\tau + i(t_0)$$

This integral form gives the current from the voltage. $\tau$ is a dummy integration variable, $t_0$ is the reference instant (often $0$), and $i(t_0)$ is the initial inductor current at $t_0$.

**Power and energy stored in an inductor**

1. Start from the power absorbed with the passive sign convention, and substitute the inductor law.

   $$p = vi = \left(L\,\frac{di}{dt}\right) i$$
2. Power is the rate of change of stored energy, so multiply both sides by $dt$.

   $$\frac{dw}{dt} = Li\,\frac{di}{dt} \;\Rightarrow\; dw = L\,i\,di$$
3. Integrate from zero energy at zero current to energy $w$ at current $i$.

   $$w = \int_0^{i} L\,x\,dx = \tfrac{1}{2}Li^2$$

$$p = Li\,\frac{di}{dt}, \qquad w = \tfrac{1}{2}Li^2$$

$p$ is the instantaneous power in watts. When $p > 0$ the inductor is storing energy, and when $p < 0$ it is returning stored energy to the circuit. $w$ is the stored magnetic energy in joules. It depends only on the present current, never on its sign or history.

- **DC behaviour:** with a constant current, $v = 0$, so an inductor in DC steady state acts as a **short circuit**.
- **Continuity:** inductor current is continuous when the applied voltage has no impulse. A finite voltage cannot produce an instantaneous current jump. In practice, suddenly opening an inductive circuit can cause a large voltage and arcing across the switch.
- **No dissipation:** an ideal inductor stores and returns energy but never converts it to heat.

**Example: Lecture example: inductor driven by $i = 10te^{-5t}$**

The independent current source produces $i = 0$ for $t < 0$ and $i = 10te^{-5t}\,\mathrm{A}$ for $t \ge 0$. The inductor is $100\,\mathrm{mH}$.

```schematic
I1 0,0 -> 0,3 "$i(t)$"
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$100\,\mathrm{mH}$" v="$v$" i="$i$"
wire 3,0 -> 0,0
ground 0,0
```

1. Sketch $i(t)$ and find when it is maximum.
2. Find $v(t)$ across the inductor.
3. Are $v$ and $i$ maximum at the same time? Which one changes abruptly?
4. Find $p(t)$ and $w(t)$, and state when the inductor stores or delivers energy.

1. The current is zero at $t=0$, rises, then decays. Set its derivative to zero to find the peak.

   $$\frac{di}{dt} = 10e^{-5t}(1-5t) = 0 \;\Rightarrow\; t = 0.2\,\mathrm{s},\quad i_{\max} = 2e^{-1} \approx 0.736\,\mathrm{A}$$
2. Apply $v = L\,\dfrac{di}{dt}$ with $L = 0.1\,\mathrm{H}$. For $t<0$ the current is constant at zero, so $v = 0$.

   $$v = 0.1 \cdot 10(1-5t)e^{-5t} = (1-5t)e^{-5t}\,\mathrm{V},\quad t>0$$
3. The voltage is largest at $t=0^+$ and crosses zero exactly when the current peaks, so the maxima do not coincide.

   $$v(0^-) = 0,\; v(0^+) = 1\,\mathrm{V};\qquad v(0.2) = 0$$
4. The current is continuous ($i(0)=0$), but the voltage jumps from $0$ to $1\,\mathrm{V}$ at $t=0$. That jump is allowed for an inductor.

   $$i(0^-) = i(0^+) = 0$$
5. Multiply $v$ and $i$ to get the power.

   $$p = vi = 10t(1-5t)e^{-10t}\,\mathrm{W}$$
6. Find the stored energy from $\tfrac12 Li^2$. Its maximum occurs where $i$ is maximum.

   $$w = \tfrac{1}{2}(0.1)(10te^{-5t})^2 = 5t^2e^{-10t}\,\mathrm{J},\quad w(0.2) = 0.2e^{-2} \approx 27.1\,\mathrm{mJ}$$
7. The sign of $p$ follows the sign of $(1-5t)$, which tells us when energy flows in or out.

   $$p>0 \text{ for } 0<t<0.2\,\mathrm{s}\;(\text{storing}),\qquad p<0 \text{ for } t>0.2\,\mathrm{s}\;(\text{delivering})$$

**Answer:** (a) $i$ peaks at $t = 0.2\,\mathrm{s}$ with $i_{\max} = 2e^{-1} \approx 0.736\,\mathrm{A}$, then decays toward zero.
(b) $v = (1-5t)e^{-5t}\,\mathrm{V}$ for $t>0$, and $0$ for $t<0$.
(c) No. $v$ is maximum ($1\,\mathrm{V}$) at $t=0^+$, while $i$ is maximum at $0.2\,\mathrm{s}$, where $v=0$. The voltage changes abruptly at $t=0$; the current does not.
(d) $p = 10t(1-5t)e^{-10t}\,\mathrm{W}$ and $w = 5t^2e^{-10t}\,\mathrm{J}$, with $w_{\max} \approx 27.1\,\mathrm{mJ}$ at $0.2\,\mathrm{s}$. The inductor stores energy for $0<t<0.2\,\mathrm{s}$ and delivers it for $t>0.2\,\mathrm{s}$.

> **Warning:** Check the reference directions before writing $v = L\,\dfrac{di}{dt}$. If the reference current enters the $-$ terminal (for example an upward current arrow with $+$ at the top), use $v = -L\,\dfrac{di}{dt}$, and likewise $i = -\tfrac{1}{L}\int v\,d\tau + i(t_0)$. Also remember that an inductor *voltage* can jump; only its *current* must be continuous.

> **Tip:** Stored energy $\tfrac12 Li^2$ is largest when $|i|$ is largest. At a differentiable interior maximum with nonzero current, $\dfrac{di}{dt}=0$ and hence $v=0$. Check endpoints and limiting values too; a monotone transient can reach its largest energy at an endpoint or as $t\to\infty$.

## Topic 2: Capacitors

A capacitor is two conductors separated by an insulator (dielectric). No charge actually crosses the dielectric, but a changing voltage moves charge onto one plate and off the other, which appears at the terminals as a current (the displacement current). Its parameter is the capacitance $C$, measured in farads (F), and it stores energy in its electric field.

```schematic
terminal 0,3
C1 0,3 -> 0,0 "$C$" i="$i$" v="$v$"
terminal 0,0
```

$$i = C\,\frac{dv}{dt}$$

$i$ is the capacitor current in amperes entering the $+$ terminal, $v$ is the capacitor voltage in volts, and $C$ is the capacitance in farads. A constant voltage gives $i = 0$.

$$v(t) = \frac{1}{C}\int_{t_0}^{t} i(\tau)\,d\tau + v(t_0)$$

This integral form gives the voltage from the current. $v(t_0)$ is the initial capacitor voltage at the reference instant $t_0$, and $\tau$ is the dummy integration variable.

**Energy stored in a capacitor**

1. Substitute $i = C\,\dfrac{dv}{dt}$ into $p = vi$.

   $$p = vi = Cv\,\frac{dv}{dt}$$
2. Write the power as the rate of change of energy.

   $$dw = C\,v\,dv$$
3. Integrate from an uncharged capacitor ($v=0$, $w=0$).

   $$w = \int_0^{v} C\,x\,dx = \tfrac{1}{2}Cv^2$$

$$p = Cv\,\frac{dv}{dt}, \qquad w = \tfrac{1}{2}Cv^2$$

$p$ is instantaneous absorbed power in watts. When $p>0$ stored energy increases; when $p<0$ the capacitor returns energy. With the passive sign convention, use the product $vi$, not the sign of current alone. Stored energy $w=\tfrac12 Cv^2$ is nonnegative and depends on the present voltage for an ideal constant capacitor.

| Property | Inductor | Capacitor |
|---|---|---|
| Defining law | $v = L\,\dfrac{di}{dt}$ | $i = C\,\dfrac{dv}{dt}$ |
| Integral form | $i = \dfrac{1}{L}\int v\,d\tau + i(t_0)$ | $v = \dfrac{1}{C}\int i\,d\tau + v(t_0)$ |
| Stored energy | $\tfrac12 Li^2$ (magnetic field) | $\tfrac12 Cv^2$ (electric field) |
| DC steady state | Short circuit | Open circuit |
| Cannot jump with finite inputs | Current $i_L$ (finite voltage) | Voltage $v_C$ (finite current) |
| Can jump | Voltage $v_L$ | Current $i_C$ |
| Dual quantities | $L$, $i$, flux $\lambda$ | $C$, $v$, charge $q$ |

The two elements are **duals**: swap $L \leftrightarrow C$ and $v \leftrightarrow i$ (and flux $\leftrightarrow$ charge) in any inductor result to get the matching capacitor result. Learn one set of results carefully and derive the other by duality.

> **Warning:** Only $v_C$ is guaranteed continuous. The capacitor current can jump, and can even change sign, at a switching instant, so $i_C(0^-) = i_C(0^+)$ is generally **false**. Always carry $v_C$ (or $i_L$) across $t = 0$, then recompute every other quantity at $0^+$.

> **Tip:** If the circuit has settled under DC conditions before switching, replace each capacitor with an open circuit and each inductor with a short circuit. Solve for $v_C(0^-)$ and $i_L(0^-)$. With no impulse at switching, those values carry over to $t=0^+$. If the circuit has not settled, use the given state or its earlier transient instead of assuming DC steady state.

## Topic 3: Series and parallel combinations

Inductors combine like resistors, and capacitors combine like conductances (series capacitors combine reciprocally). The new ingredient compared with resistors is the **initial condition**: the equivalent element must also carry the correct initial current or voltage.

**Series and parallel inductors**

1. In series, every inductor carries the same current $i$, so each voltage is $L_k\,\dfrac{di}{dt}$.

   $$v_k = L_k\,\frac{di}{dt}$$
2. KVL adds the voltages.

   $$v = \sum_k v_k = \left(\sum_k L_k\right)\frac{di}{dt} \;\Rightarrow\; L_{eq} = \sum_k L_k$$
3. In parallel, every inductor has the same voltage $v$, so each current is the integral of $v$ plus that inductor's own initial current.

   $$i_k = \frac{1}{L_k}\int_{t_0}^{t} v\,d\tau + i_k(t_0)$$
4. KCL adds the currents, giving a reciprocal sum and a summed initial current.

   $$i = \left(\sum_k \frac{1}{L_k}\right)\int_{t_0}^{t} v\,d\tau + \sum_k i_k(t_0) \;\Rightarrow\; \frac{1}{L_{eq}} = \sum_k \frac{1}{L_k},\; i(t_0) = \sum_k i_k(t_0)$$

$$\text{Series } C:\; \frac{1}{C_{eq}} = \sum_k \frac{1}{C_k},\; v(t_0) = \sum_k v_k(t_0) \qquad \text{Parallel } C:\; C_{eq} = \sum_k C_k$$

These are the duals of the inductor results. $C_k$ are the individual capacitances, $v_k(t_0)$ are their initial voltages (with polarities measured in the same direction around the series path), and $v(t_0)$ is the initial voltage of the series equivalent. Parallel capacitors share one voltage, so they must start with equal initial voltages.

| Combination | Equivalent | Initial condition of the equivalent |
|---|---|---|
| Series $L$ | $L_{eq} = L_1 + L_2 + \dots + L_n$ | Same current $i(t_0)$ in every inductor |
| Parallel $L$ | $\dfrac{1}{L_{eq}} = \dfrac{1}{L_1} + \dots + \dfrac{1}{L_n}$ | $i(t_0) = \sum_k i_k(t_0)$ |
| Series $C$ | $\dfrac{1}{C_{eq}} = \dfrac{1}{C_1} + \dots + \dfrac{1}{C_n}$ | $v(t_0) = \sum_k v_k(t_0)$ |
| Parallel $C$ | $C_{eq} = C_1 + C_2 + \dots + C_n$ | Same voltage $v(t_0)$ on every capacitor |

**Example: Lecture example: three inductors in series**

A current source drives three inductors in series. The slide gives $i_S=\sin t$ for $t\ge0$ and zero for $t<0$, without current units. Assume amperes and time in seconds for the numerical answer below.

```schematic
I1 0,0 -> 0,3 "$i_S=\sin t$" v="$v_S$" v_rev
L1 0,3 -> 3,3 "$1\,\mathrm{mH}$"
L2 3,3 -> 3,0 "$3\,\mathrm{mH}$"
L3 3,0 -> 0,0 "$4\,\mathrm{mH}$"
ground 0,0
```

1. Find the equivalent inductance $L_{eq}$.
2. Find the source voltage $v_S(t)$.

1. The three inductors carry the same current, so they are in series and their inductances add.

   $$L_{eq} = 1 + 3 + 4 = 8\,\mathrm{mH}$$
2. The source current enters the $+$ terminal of the equivalent inductor, so $v_S = L_{eq}\,\dfrac{di_S}{dt}$.

   $$v_S = (8\times10^{-3})\frac{d}{dt}(\sin t) = 8\cos t\,\mathrm{mV}$$
3. Check: each inductor's share of the voltage is proportional to its inductance.

   $$v_{L1} = \cos t,\; v_{L2} = 3\cos t,\; v_{L3} = 4\cos t\;(\mathrm{mV}),\quad \text{sum} = 8\cos t\,\mathrm{mV}$$

**Answer:** (a) $L_{eq}=8\,\mathrm{mH}$. (b) Assuming $i_S=\sin t\,\mathrm{A}$, $v_S=8\cos t\,\mathrm{mV}$ for $t\ge0$, and $v_S=0$ for $t<0$. The slide prints $8\cos t$ without voltage units.

**Example: Lecture example: three inductors in parallel with initial currents**

A source $v_S = 9\cos t$ is connected across three parallel inductors with initial currents $i_{L1}(0) = i_{L2}(0) = 2\,\mathrm{mA}$ and $i_{L3}(0) = 4\,\mathrm{mA}$.

```schematic
V1 0,3 -> 0,0 "$v_S=9\cos t$" i="$i_S$" i_rev
wire 0,3 -> 3,3
L1 3,3 -> 3,0 "$12\,\mathrm{mH}$" i="$i_{L1}$"
wire 3,3 -> 6,3
L2 6,3 -> 6,0 "$12\,\mathrm{mH}$" i="$i_{L2}$"
wire 6,3 -> 9,3
L3 9,3 -> 9,0 "$6\,\mathrm{mH}$" i="$i_{L3}$"
wire 9,0 -> 6,0 -> 3,0 -> 0,0
ground 0,0
```

1. Find $L_{eq}$ and its initial current $i_S(0)$.
2. Find the source current $i_S(t)$. The slide omits the voltage units. For a numerical SI answer below, explicitly assume $v_S(t)=9\cos t\,\mathrm{V}$ and $t$ in seconds; a different voltage unit changes the result.

1. Add the reciprocals for parallel inductors.

   $$\frac{1}{L_{eq}} = \frac{1}{12} + \frac{1}{12} + \frac{1}{6} = \frac{4}{12} \;\Rightarrow\; L_{eq} = 3\,\mathrm{mH}$$
2. The equivalent's initial current is the sum of the branch initial currents (all in the same downward reference).

   $$i_S(0) = 2 + 2 + 4 = 8\,\mathrm{mA}$$
3. Use henries, volts and amperes under the stated voltage assumption.

   $$i_S(t)=\frac{1}{0.003}\int_0^t9\cos\tau\,d\tau+0.008=3000\sin t+0.008\;\mathrm{A}$$
4. Check each downward branch current in amperes; their sum gives the source current.

   $$i_{L1}=i_{L2}=750\sin t+0.002,\quad i_{L3}=1500\sin t+0.004,\quad i_S=3000\sin t+0.008\;\mathrm{A}$$

**Answer:** (a) $L_{eq}=3\,\mathrm{mH}$ and $i_S(0)=8\,\mathrm{mA}$. (b) Assuming the source is in volts, $i_S(t)=3000\sin t+0.008\,\mathrm{A}$. The slide prints $3\sin t+8$ without current units; it cannot be accepted as an SI answer. The expression $(3\sin t+8)\,\mathrm{mA}$ would require $v_S=9\cos t\,\mu\mathrm{V}$, a unit not given on the slide.

**Example: Lecture example: three capacitors in series**

A source $v_s = 3\sin 2t\,\mathrm{V}$ drives three series capacitors. The $1\,\mu\mathrm{F}$ capacitor starts with $v_{C1}(0) = 10\,\mathrm{V}$.

```schematic
V1 0,3 -> 0,0 "$v_s=3\sin 2t$" i="$i_s$" i_rev
C1 0,3 -> 3,3 "$1\,\mu\mathrm{F}$" v="$v_{C1}$"
C2 3,3 -> 3,0 "$2\,\mu\mathrm{F}$"
C3 3,0 -> 0,0 "$2\,\mu\mathrm{F}$"
ground 0,0
```

1. Find $C_{eq}$.
2. Find $i_s(t)$.
3. Find $v_{C1}(t)$.

1. Series capacitors combine reciprocally.

   $$\frac{1}{C_{eq}} = \frac{1}{1} + \frac{1}{2} + \frac{1}{2} = 2\;\mu\mathrm{F}^{-1} \;\Rightarrow\; C_{eq} = 0.5\,\mu\mathrm{F}$$
2. The source sees one equivalent capacitor, so $i_s = C_{eq}\,\dfrac{dv_s}{dt}$.

   $$i_s = (0.5\times10^{-6})(6\cos 2t) = 3\cos 2t\,\mu\mathrm{A}$$
3. The same current flows through $C_1$ into its $+$ terminal. Integrate it and add $C_1$'s own initial voltage.

   $$v_{C1}(t) = \frac{1}{1\times10^{-6}}\int_0^{t} 3\times10^{-6}\cos 2\tau\,d\tau + 10 = 10 + 1.5\sin 2t\,\mathrm{V}$$

**Answer:** (a) $C_{eq} = 0.5\,\mu\mathrm{F}$.
(b) $i_s = 3\cos 2t\,\mu\mathrm{A}$.
(c) $v_{C1} = 10 + 1.5\sin 2t\,\mathrm{V}$.

> **Warning:** Do not split a series-capacitor voltage in proportion to $\dfrac{1}{C_k}$ when the capacitors start with different voltages. Integrate the common current through each capacitor and add that capacitor's own initial voltage, as in the example above. Similarly, parallel inductors with unequal initial currents can end up with current circulating between them, and the energy in that circulating current stays trapped (see P6.25 below).

> **Tip:** Memory aid: $L$ behaves like $R$ (series adds), and $C$ behaves like $G = \dfrac{1}{R}$ (parallel adds). The initial condition always follows the quantity that is *shared*: a common current in series $L$, a common voltage in parallel $C$; the other quantities simply add.

## Topic 4: First-order RL and RC circuits

The first-order circuits treated here reduce to one equivalent ideal $L$ or $C$ connected to a linear resistive network that admits a finite Thévenin or Norton equivalent. The resulting equation has one independent state. Natural response comes from initial stored energy with independent inputs zero; step response follows a change in a DC input. Stable exponential decay below assumes a positive equivalent resistance. Other first-order configurations are outside this lecture treatment.

```schematic
L1 0,3 -> 0,0 "$L$" i="$i$" i_rev v="$v$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$R$" i="$i$"
wire 3,0 -> 0,0
ground 0,0
```

**Natural response of an RL circuit**

1. KVL around the loop. The current $i$ flows down through $R$ and up through $L$ (opposite to the passive sign convention for $L$), so $v = Ri = -L\,\dfrac{di}{dt}$.

   $$L\,\frac{di}{dt} + Ri = 0$$
2. Separate the variables.

   $$\frac{di}{i} = -\frac{R}{L}\,dt$$
3. Integrate from $0^+$ to $t$.

   $$\ln\frac{i(t)}{i(0^+)} = -\frac{R}{L}\,t$$
4. Inductor current is continuous, so $i(0^+) = i(0^-) = I_0$.

   $$i(t) = I_0\,e^{-(R/L)t},\quad t \ge 0$$
5. The resistor voltage follows from Ohm's law. It exists only from $t = 0^+$ because it may jump at $t = 0$.

   $$v(t) = RI_0\,e^{-(R/L)t},\quad t \ge 0^+$$
6. Integrating $p_R = i^2R$ shows that all of the initially stored energy is eventually dissipated in $R$.

   $$w_R(t) = \tfrac12 LI_0^2\left(1 - e^{-2t/\tau}\right) \to \tfrac12 LI_0^2$$

$$i(t) = I_0\,e^{-t/\tau}, \qquad \tau = \frac{L}{R}$$

$I_0$ is the initial inductor current, $R$ is the equivalent (Thévenin) resistance seen by the inductor, and $\tau$ is the time constant in seconds ($\mathrm{H}/\Omega = \mathrm{s}$). After one time constant the response has fallen to $e^{-1} \approx 36.8\%$ of its initial value.

| Elapsed time | $e^{-\frac{t}{\tau}}$ | Fraction of the total change completed |
|---|---|---|
| $\tau$ | $0.368$ | $63.2\%$ |
| $2\tau$ | $0.135$ | $86.5\%$ |
| $3\tau$ | $0.0498$ | $95.0\%$ |
| $5\tau$ | $0.0067$ | $99.3\%$ (treat as steady state) |

In the RC natural response, a capacitor initially at $V_0$ discharges through $R>0$. Its voltage is continuous. Define resistor current from the positive-voltage node through $R$: $i_R(0^+)=\dfrac{V_0}{R}$. Capacitor current entering its positive terminal is $i_C=-i_R$, so $i_C(0^+)=-\dfrac{V_0}{R}$. For the lecture circuit settled before switching, both currents were zero just before the discharge connection.

$$v(t) = V_0\,e^{-t/\tau},\quad \tau = RC; \qquad w(t) = w(0)\,e^{-2t/\tau}$$

$V_0$ is the initial capacitor voltage, $R$ is the resistance seen by the capacitor, and $\tau = RC$ is in seconds. The stored energy decays twice as fast as the voltage or current, because it is proportional to their square.

```schematic
V1 0,3 -> 0,0 "$V_s$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$R$" i="$i$"
L1 6,3 -> 6,0 "$L$" v="$v$"
wire 6,0 -> 0,0
ground 0,0
```

**Step response of an RL circuit**

1. KVL for $t > 0$ with the switch closed.

   $$V_s = Ri + L\,\frac{di}{dt}$$
2. Rearrange so the variables can be separated.

   $$\frac{di}{i - V_s/R} = -\frac{R}{L}\,dt$$
3. Integrate from $i(0^+) = I_0$ to $i(t)$.

   $$\ln\frac{i(t) - V_s/R}{I_0 - V_s/R} = -\frac{R}{L}\,t$$
4. Solve for the current: a final value plus a decaying transient.

   $$i(t) = \frac{V_s}{R} + \left(I_0 - \frac{V_s}{R}\right)e^{-(R/L)t}$$
5. Differentiate to get the inductor voltage.

   $$v(t) = L\,\frac{di}{dt} = (V_s - RI_0)\,e^{-(R/L)t}$$

$$i(t) = \frac{V_s}{R} + \left(I_0 - \frac{V_s}{R}\right)e^{-t/\tau}, \qquad v(t) = (V_s - RI_0)\,e^{-t/\tau}$$

$V_s$ is the DC source (Thévenin) voltage, $\dfrac{V_s}{R}$ is the final current once the inductor becomes a short, $I_0$ is the initial inductor current, and $\tau = \dfrac{L}{R}$. If $I_0 = 0$, the voltage starts at $V_s$ and decays to zero.

$$v_C(t) = RI_s + (V_0 - RI_s)\,e^{-t/RC}$$

This is the RC step response for a DC current source $I_s$ in parallel with $R$ and $C$ (the Norton form). $RI_s$ is the final capacitor voltage once $C$ becomes an open circuit, $V_0$ is the initial capacitor voltage, and $\tau = RC$.

$$x(t)=x(\infty)+[x(t_0^+)-x(\infty)]e^{-(t-t_0)/\tau},\qquad t\ge t_0$$

This form applies to the stable first-order natural and DC step responses discussed here. $x$ is a circuit voltage or current, $x(t_0^+)$ is its value just after switching at $t_0$, and $x(\infty)$ is its final DC value. For positive $R_{Th}$, $\tau=\dfrac{L}{R_{Th}}$ or $R_{Th}C$. A source-free response whose measured output tends to zero has $x(\infty)=0$.

1. Before switching: treat $L$ as a short and $C$ as an open, and find $i_L(0^-)$ or $v_C(0^-)$.
2. Carry it across: $i_L(0^+) = i_L(0^-)$ and $v_C(0^+) = v_C(0^-)$.
3. After switching: find the final value $x(\infty)$ with $L$ shorted or $C$ open.
4. Zero the independent sources, find $R_{Th}$ seen by $L$ or $C$, then $\tau = \dfrac{L}{R_{Th}}$ or $R_{Th}C$.
5. Substitute into the general form, then differentiate if you need $v_L = L\,\dfrac{di_L}{dt}$ or $i_C = C\,\dfrac{dv_C}{dt}$.

**Example: Lecture example: RL step response after a switch moves from a to b**

The switch has been in position $a$ for a long time and moves to position $b$ at $t = 0$. It is drawn here as two switches that operate together: $a$ opens and $b$ closes.

```schematic
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$" v="$v_R$"
S1 3,3 -> 6,3 "$t=0$" action=close
S2 9,3 -> 6,3 "$t=0$" state=closed action=open
L1 6,3 -> 6,0 "$200\,\mathrm{mH}$" i="$i$" v="$v$"
R2 9,3 -> 9,0 "$10\,\Omega$"
wire 9,3 -> 12,3
I1 12,3 -> 12,0 "$8\,\mathrm{A}$"
wire 0,0 -> 6,0 -> 9,0 -> 12,0
label 3,3 "$b$" above
label 9,3 "$a$" above
ground 0,0
```

1. Find $i(t)$ for $t \ge 0$.
2. Find $v(0^+)$.
3. Does the result make sense?
4. At what time does $v$ fall to $24\,\mathrm{V}$?
5. Sketch $i(t)$ and $v(t)$.

1. For $t < 0$ the inductor (a short at DC) sits across the $10\,\Omega$ resistor and the $8\,\mathrm{A}$ source. All of the source current goes through the short. The source pushes $8\,\mathrm{A}$ down through itself, so the current flows *up* through the inductor, against the reference $i$. A DC operating-point solve confirms this.

   $$i(0^-) = -8\,\mathrm{A} = i(0^+)$$
2. For $t > 0$ the inductor is connected through $2\,\Omega$ to the $24\,\mathrm{V}$ source. At steady state it is a short again.

   $$i(\infty) = \frac{24}{2} = 12\,\mathrm{A}$$
3. The resistance seen by the inductor with the source zeroed is $2\,\Omega$.

   $$\tau = \frac{L}{R} = \frac{0.2}{2} = 0.1\,\mathrm{s}$$
4. Substitute into the general first-order form.

   $$i(t) = 12 + (-8 - 12)e^{-10t} = 12 - 20e^{-10t}\,\mathrm{A},\quad t \ge 0$$
5. Differentiate to get the inductor voltage.

   $$v(t) = 0.2\,\frac{di}{dt} = 0.2(200e^{-10t}) = 40e^{-10t}\,\mathrm{V},\quad v(0^+) = 40\,\mathrm{V}$$
6. Check with KVL at $0^+$. It agrees, and the voltage jumps from $0$ to $40\,\mathrm{V}$ while the current stays continuous, which is allowed for an inductor.

   $$v(0^+) = 24 - 2\,i(0^+) = 24 + 16 = 40\,\mathrm{V}$$
7. Solve for the time when $v = 24\,\mathrm{V}$.

   $$40e^{-10t} = 24 \;\Rightarrow\; t = \frac{\ln(5/3)}{10} \approx 51.1\,\mathrm{ms}$$

**Answer:** (a) $i(t) = 12 - 20e^{-10t}\,\mathrm{A}$ for $t \ge 0$.
(b) $v(0^+) = 40\,\mathrm{V}$.
(c) Yes. The inductor current is continuous at $-8\,\mathrm{A}$, and KVL gives $24 - 2(-8) = 40\,\mathrm{V}$.
(d) $t = 0.1\ln(\dfrac{5}{3}) \approx 51.1\,\mathrm{ms}$.
(e) $i$ rises from $-8\,\mathrm{A}$ toward $12\,\mathrm{A}$, and $v = 40e^{-10t}\,\mathrm{V}$ decays from $40\,\mathrm{V}$ to $0$, both with $\tau = 100\,\mathrm{ms}$.

> **Warning:** Lecture slide 62 writes the RL time constant as $\tau \equiv \dfrac{R}{L}$. That is a typo: the correct value is $\tau = \dfrac{L}{R}$. Check the units: $\mathrm{H}/\Omega = (\mathrm{V\,s/A})/(\mathrm{V/A}) = \mathrm{s}$, whereas $\dfrac{R}{L}$ has units of $\mathrm{s}^{-1}$. The exponent is $-\dfrac{Rt}{L} = -\dfrac{t}{\tau}$, so it is $\dfrac{R}{L}$ that multiplies $t$.

> **Tip:** Always find $\tau$ from the resistance seen by the energy-storage element *after* switching, with independent sources zeroed (voltage sources shorted, current sources opened). Using a resistance from the pre-switch circuit is one of the most common exam mistakes.

## Practice problems

These problems run from single-element calculations to complete switched first-order circuits. Five come from the Nilsson textbook (Chapters 6 and 7) and the last is the unsolved RC example from the lecture slides. Try each one before opening the steps.

**Problem: Textbook P6.15 · Capacitor voltage, power and energy** (introductory)

Both the voltage and current in a $0.6\,\mu\mathrm{F}$ capacitor are zero for $t < 0$ and $i = 3\cos 50{,}000t\,\mathrm{A}$ for $t \ge 0$. The passive sign convention is used.

1. Find the capacitor voltage $v(t)$.
2. Find the power $p(t)$ and its maximum value.
3. Find the maximum energy stored.

<details><summary>Solution</summary>

1. The problem gives $v(0^-)=0$. With finite capacitor current, voltage is continuous, so $v(0^+)=0$. Integrate the current and include this given initial voltage; zero current alone would not imply an uncharged capacitor.

   $$v(t)=v(0^+)+\frac{1}{0.6\times10^{-6}}\int_0^{t} 3\cos(5\times10^{4}\tau)\,d\tau = \frac{3}{(0.6\times10^{-6})(5\times10^{4})}\sin 50{,}000t$$
2. Simplify the coefficient.

   $$v(t) = 100\sin 50{,}000t\,\mathrm{V}$$
3. Multiply $v$ and $i$, and use $2\sin\theta\cos\theta = \sin 2\theta$.

   $$p = (100\sin\theta)(3\cos\theta) = 150\sin 100{,}000t\,\mathrm{W},\quad p_{\max} = 150\,\mathrm{W}$$
4. The energy is greatest when $|v|$ is greatest, i.e. at $100\,\mathrm{V}$.

   $$w_{\max} = \tfrac12(0.6\times10^{-6})(100)^2 = 3\,\mathrm{mJ}$$

**Answer:** (a) $v = 100\sin 50{,}000t\,\mathrm{V}$.
(b) $p = 150\sin 100{,}000t\,\mathrm{W}$, with $p_{\max} = 150\,\mathrm{W}$.
(c) $w_{\max} = 3\,\mathrm{mJ}$.

</details>

**Problem: Textbook P6.2 · Inductor voltage, power and energy** (introductory)

The current in a $4\,\mathrm{mH}$ inductor with zero initial current is $i = 8e^{-300t} - 8e^{-1200t}\,\mathrm{A}$ for $t \ge 0$. The passive sign convention is used.

1. Find the initial voltage across the inductor.
2. At what time $t > 0$ is the voltage zero?
3. Find the expression for the power $p(t)$.
4. At what time is the power maximum, and what is that maximum?
5. At what time is the stored energy maximum, and what is that maximum?

<details><summary>Solution</summary>

1. Differentiate the current and multiply by $L = 0.004\,\mathrm{H}$.

   $$v = 0.004\left(-2400e^{-300t} + 9600e^{-1200t}\right) = -9.6e^{-300t} + 38.4e^{-1200t}\,\mathrm{V}$$
2. Evaluate at $t = 0$.

   $$v(0) = -9.6 + 38.4 = 28.8\,\mathrm{V}$$
3. Set $v = 0$ and solve.

   $$38.4e^{-1200t} = 9.6e^{-300t} \Rightarrow e^{900t} = 4 \Rightarrow t = \frac{\ln 4}{900} \approx 1.540\,\mathrm{ms}$$
4. Multiply $v$ and $i$ and collect the exponentials.

   $$p = vi = -76.8e^{-600t} + 384e^{-1500t} - 307.2e^{-2400t}\,\mathrm{W}$$
5. Set $\dfrac{dp}{dt} = 0$, divide by $46{,}080e^{-600t}$ and substitute $y = e^{-900t}$. Take the root that gives a positive maximum.

   $$16y^2 - 12.5y + 1 = 0 \Rightarrow y = \frac{12.5 + \sqrt{92.25}}{32} = 0.6908 \Rightarrow t = \frac{-\ln y}{900} \approx 411\,\mu\mathrm{s}$$
6. Evaluate $p$ at that instant.

   $$p_{\max} = p(411\,\mu\mathrm{s}) \approx 32.7\,\mathrm{W}$$
7. The energy is maximum when $i$ is maximum, which is when $v = 0$, at $t \approx 1.540\,\mathrm{ms}$.

   $$i = 8\left(e^{-0.4621} - e^{-1.8484}\right) \approx 3.780\,\mathrm{A},\quad w_{\max} = \tfrac12(0.004)(3.780)^2 \approx 28.6\,\mathrm{mJ}$$

**Answer:** (a) $v(0) = 28.8\,\mathrm{V}$.
(b) $t = \dfrac{\ln 4}{900} \approx 1.54\,\mathrm{ms}$.
(c) $p = -76.8e^{-600t} + 384e^{-1500t} - 307.2e^{-2400t}\,\mathrm{W}$.
(d) $p_{\max} \approx 32.7\,\mathrm{W}$ at $t \approx 411\,\mu\mathrm{s}$.
(e) $w_{\max} \approx 28.6\,\mathrm{mJ}$ at $t \approx 1.54\,\mathrm{ms}$.

</details>

**Problem: Textbook P6.25 · Parallel inductors and trapped energy** (intermediate)

The two parallel inductors are connected across the terminals of a black box when the switch opens at $t = 0$. For $t > 0$ the resulting voltage is $v = -1800e^{-20t}\,\mathrm{V}$. The initial currents are $i_1(0) = 4\,\mathrm{A}$ and $i_2(0) = -16\,\mathrm{A}$.

```schematic
L1 0,0 -> 0,3 "$10\,\mathrm{H}$" i="$i_1(t)$"
L2 3,0 -> 3,3 "$30\,\mathrm{H}$" i="$i_2(t)$"
wire 0,3 -> 3,3 -> 6,3 -> 9,3
wire 0,0 -> 3,0 -> 6,0 -> 9,0
S1 6,3 -> 6,0 "$t=0$" state=closed action=open
X1 9,3 -> 9,0 "Black box" i="$i(t)$" v="$v$"
ground 0,0
```

1. Replace the inductors with one equivalent inductor and find $i(t)$.
2. Find $i_1(t)$.
3. Find $i_2(t)$.
4. How much energy is delivered to the black box for $0 \le t < \infty$?
5. How much energy was initially stored in the inductors?
6. How much energy is trapped in the ideal inductors?
7. Show that $i_1$ and $i_2$ agree with the answer to part 6.

<details><summary>Solution</summary>

1. Combine the parallel inductors. Once the switch opens, all of the inductor current flows into the box, so $i(0^+) = i_1(0) + i_2(0)$.

   $$L_{eq} = \frac{10 \cdot 30}{40} = 7.5\,\mathrm{H},\qquad i(0^+) = 4 - 16 = -12\,\mathrm{A}$$
2. The upward inductor current enters the $-$ terminal of $v$, so the integral relation carries a minus sign.

   $$i(t) = -\frac{1}{7.5}\int_0^{t} (-1800e^{-20\tau})\,d\tau - 12 = 12(1 - e^{-20t}) - 12 = -12e^{-20t}\,\mathrm{A}$$
3. Apply the same relation to each inductor with its own initial current.

   $$i_1 = \frac{1800}{10}\cdot\frac{1 - e^{-20t}}{20} + 4 = 13 - 9e^{-20t}\,\mathrm{A}$$
4. Repeat for $i_2$.

   $$i_2 = \frac{1800}{30}\cdot\frac{1 - e^{-20t}}{20} - 16 = -13 - 3e^{-20t}\,\mathrm{A}$$
5. Integrate the power delivered to the box; $i$ enters the box's $+$ terminal.

   $$w_{box} = \int_0^{\infty} (-1800e^{-20t})(-12e^{-20t})\,dt = \frac{21{,}600}{40} = 540\,\mathrm{J}$$
6. Find the initial stored energy from the initial currents.

   $$w(0) = \tfrac12(10)(4)^2 + \tfrac12(30)(16)^2 = 80 + 3840 = 3920\,\mathrm{J}$$
7. Whatever energy was not delivered to the box stays trapped in the loop formed by the two inductors.

   $$w_{trapped} = 3920 - 540 = 3380\,\mathrm{J}$$
8. Check with the final currents $i_1(\infty) = 13\,\mathrm{A}$ and $i_2(\infty) = -13\,\mathrm{A}$, which circulate around the inductor loop.

   $$\tfrac12(10)(13)^2 + \tfrac12(30)(13)^2 = 845 + 2535 = 3380\,\mathrm{J}$$

**Answer:** (a) $L_{eq} = 7.5\,\mathrm{H}$ and $i(t) = -12e^{-20t}\,\mathrm{A}$.
(b) $i_1 = 13 - 9e^{-20t}\,\mathrm{A}$.
(c) $i_2 = -13 - 3e^{-20t}\,\mathrm{A}$.
(d) $540\,\mathrm{J}$.
(e) $3920\,\mathrm{J}$.
(f) $3380\,\mathrm{J}$.
(g) $845 + 2535 = 3380\,\mathrm{J}$, which matches.

</details>

**Problem: Textbook P7.1 · RL natural response** (intermediate)

The switch has been closed for a long time and opens at $t = 0$.

```schematic
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
R1 0,3 -> 3,3 "$3\,\Omega$"
R2 3,3 -> 3,0 "$30\,\Omega$"
R3 3,3 -> 6,3 "$6\,\Omega$"
S1 6,3 -> 9,3 "$t=0$" state=closed action=open
L1 9,0 -> 9,3 "$8\,\mathrm{mH}$" i="$i$"
wire 9,3 -> 12,3
R4 12,3 -> 12,0 "$2\,\Omega$"
wire 0,0 -> 3,0 -> 9,0 -> 12,0
ground 0,0
```

1. Calculate the initial value of $i$.
2. Calculate the initial energy stored in the inductor.
3. What is the time constant for $t > 0$?
4. Find $i(t)$ for $t \ge 0$.
5. What percentage of the initial energy has been dissipated in the $2\,\Omega$ resistor $5\,\mathrm{ms}$ after the switch opens?

<details><summary>Solution</summary>

1. Before $t = 0$ the inductor is a short, which also shorts out the $2\,\Omega$ resistor. The source therefore sees $3\,\Omega$ in series with $30\,\Omega \parallel 6\,\Omega$.

   $$30 \parallel 6 = 5\,\Omega,\quad i_{src} = \frac{120}{3 + 5} = 15\,\mathrm{A},\quad v_{30} = 75\,\mathrm{V}$$
2. The $6\,\Omega$ branch carries $\dfrac{75}{6} = 12.5\,\mathrm{A}$ down through the inductor. The reference $i$ points up, so $i$ is negative. A DC operating-point solve confirms the $12.5\,\mathrm{A}$.

   $$i(0^-) = i(0^+) = -12.5\,\mathrm{A}$$
3. Compute the stored energy.

   $$w(0) = \tfrac12(8\times10^{-3})(12.5)^2 = 0.625\,\mathrm{J}$$
4. After the switch opens, the inductor sees only the $2\,\Omega$ resistor.

   $$\tau = \frac{L}{R} = \frac{8\times10^{-3}}{2} = 4\,\mathrm{ms}$$
5. This is a natural response, so it decays to zero.

   $$i(t) = -12.5e^{-250t}\,\mathrm{A},\quad t \ge 0$$
6. The energy remaining decays as $e^{-\frac{2t}{\tau}}$; the rest has been dissipated in the $2\,\Omega$ resistor.

   $$\frac{w_{diss}}{w(0)} = 1 - e^{-2(5)/4} = 1 - e^{-2.5} \approx 0.918$$

**Answer:** (a) $i(0) = -12.5\,\mathrm{A}$.
(b) $w(0) = 0.625\,\mathrm{J}$.
(c) $\tau = 4\,\mathrm{ms}$.
(d) $i(t) = -12.5e^{-250t}\,\mathrm{A}$ for $t \ge 0$.
(e) About $91.8\%$.

</details>

**Problem: Textbook P7.22 · RC natural response** (intermediate)

The switch has been closed for a long time and opens at $t = 0$.

```schematic
I1 0,0 -> 0,3 "$7.5\,\mathrm{mA}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$80\,\mathrm{k}\Omega$"
R2 3,3 -> 6,3 "$20\,\mathrm{k}\Omega$"
S1 6,3 -> 9,3 "$t=0$" state=closed action=open
C1 9,3 -> 9,0 "$0.4\,\mu\mathrm{F}$" v="$v(t)$"
wire 9,3 -> 12,3
R3 12,3 -> 12,0 "$50\,\mathrm{k}\Omega$"
wire 0,0 -> 3,0 -> 9,0 -> 12,0
ground 0,0
```

1. Find the initial value of $v(t)$.
2. Find the time constant for $t > 0$.
3. Find $v(t)$ after the switch opens.
4. Find the initial energy stored in the capacitor.
5. How long does it take to dissipate $75\%$ of the initially stored energy?

<details><summary>Solution</summary>

1. Before $t = 0$ the capacitor is an open circuit. The $7.5\,\mathrm{mA}$ splits between $80\,\mathrm{k}\Omega$ and the $20 + 50 = 70\,\mathrm{k}\Omega$ path by current division. A DC operating-point solve gives the same $200\,\mathrm{V}$.

   $$i_{70k} = 7.5\cdot\frac{80}{80 + 70} = 4\,\mathrm{mA},\quad v(0) = (4\,\mathrm{mA})(50\,\mathrm{k}\Omega) = 200\,\mathrm{V}$$
2. After the switch opens, the capacitor discharges through the $50\,\mathrm{k}\Omega$ resistor alone.

   $$\tau = RC = (50\times10^{3})(0.4\times10^{-6}) = 20\,\mathrm{ms}$$
3. This is a natural response.

   $$v(t) = 200e^{-50t}\,\mathrm{V},\quad t \ge 0$$
4. Compute the initial energy.

   $$w(0) = \tfrac12(0.4\times10^{-6})(200)^2 = 8\,\mathrm{mJ}$$
5. The remaining energy is $w(0)e^{-\frac{2t}{\tau}}$. Dissipating $75\%$ leaves $25\%$.

   $$e^{-100t} = 0.25 \Rightarrow t = \frac{\ln 4}{100} \approx 13.86\,\mathrm{ms}$$

**Answer:** (a) $v(0) = 200\,\mathrm{V}$.
(b) $\tau = 20\,\mathrm{ms}$.
(c) $v(t) = 200e^{-50t}\,\mathrm{V}$ for $t \ge 0$.
(d) $w(0) = 8\,\mathrm{mJ}$.
(e) $t \approx 13.86\,\mathrm{ms}$.

</details>

**Problem: Lecture 6 example · RC step response with a two-position switch** (advanced)

The switch has been in position 1 for a long time and moves to position 2 at $t = 0$. It is drawn as two switches that operate together: 1 opens and 2 closes. The $75\,\mathrm{V}$ source has its $+$ terminal at the reference node.

```schematic
V1 0,3 -> 0,0 "$40\,\mathrm{V}$"
R1 0,3 -> 3,3 "$20\,\mathrm{k}\Omega$"
R2 3,3 -> 3,0 "$60\,\mathrm{k}\Omega$"
S1 3,3 -> 6,3 "$1$" state=closed action=open
C1 6,3 -> 6,0 "$0.25\,\mu\mathrm{F}$" v="$v_C$"
S2 9,3 -> 6,3 "$2$" action=close
R3 12,3 -> 9,3 "$8\,\mathrm{k}\Omega$" i="$i_o$"
R4 12,3 -> 12,0 "$160\,\mathrm{k}\Omega$"
R5 12,3 -> 15,3 "$40\,\mathrm{k}\Omega$"
V2 15,0 -> 15,3 "$75\,\mathrm{V}$"
wire 0,0 -> 3,0 -> 6,0 -> 12,0 -> 15,0
label 12,3 "$c$" above
ground 0,0
```

1. Find $v_C(t)$ for $t \ge 0$.
2. Find $i_o(t)$ for $t \ge 0^+$.

<details><summary>Solution</summary>

1. In position 1 the capacitor is an open circuit at DC and sits across the $60\,\mathrm{k}\Omega$ resistor of a voltage divider (confirmed by a DC solve).

   $$v_C(0^-) = 40\cdot\frac{60}{20 + 60} = 30\,\mathrm{V} = v_C(0^+)$$
2. In position 2, find the Thévenin equivalent seen by the capacitor. Node $c$ is a divider of the $-75\,\mathrm{V}$ node through $40\,\mathrm{k}\Omega$ and $160\,\mathrm{k}\Omega$, and no current flows in the $8\,\mathrm{k}\Omega$ at steady state.

   $$V_{Th} = -75\cdot\frac{160}{40 + 160} = -60\,\mathrm{V} = v_C(\infty)$$
3. Zero the $75\,\mathrm{V}$ source (short it) to find the resistance seen by the capacitor.

   $$R_{Th} = 8 + (160 \parallel 40) = 8 + 32 = 40\,\mathrm{k}\Omega$$
4. Compute the time constant.

   $$\tau = R_{Th}C = (40\times10^{3})(0.25\times10^{-6}) = 10\,\mathrm{ms}$$
5. Substitute into the general step-response form.

   $$v_C(t) = -60 + [30 - (-60)]e^{-100t} = -60 + 90e^{-100t}\,\mathrm{V},\quad t \ge 0$$
6. $i_o$ flows through the $8\,\mathrm{k}\Omega$ toward the capacitor, so it enters the capacitor's $+$ terminal and $i_o = C\,\dfrac{dv_C}{dt}$.

   $$i_o = (0.25\times10^{-6})(-9000e^{-100t}) = -2.25e^{-100t}\,\mathrm{mA},\quad t \ge 0^+$$
7. Check at $0^+$ with the Thévenin circuit.

   $$i_o(0^+) = \frac{V_{Th} - v_C(0^+)}{R_{Th}} = \frac{-60 - 30}{40\,\mathrm{k}\Omega} = -2.25\,\mathrm{mA}$$

**Answer:** (a) $v_C(t) = -60 + 90e^{-100t}\,\mathrm{V}$ for $t \ge 0$.
(b) $i_o(t) = -2.25e^{-100t}\,\mathrm{mA}$ for $t \ge 0^+$.

</details>

## Summary

- Inductors respond to *changes in current* ($v = L\,\dfrac{di}{dt}$); capacitors respond to *changes in voltage* ($i = C\,\dfrac{dv}{dt}$). The two are duals.
- With finite applied voltage and current, inductor current and capacitor voltage are continuous. Inductor voltage and capacitor current may jump at switching.
- In DC steady state an inductor is a short and a capacitor is an open circuit. Use this to find $i_L(0^-)$ and $v_C(0^-)$. This initial-state shortcut requires the circuit to have settled before switching.
- Stored energy is $\tfrac12 Li^2$ or $\tfrac12 Cv^2$. Ideal $L$ and $C$ store and return energy but never dissipate it.
- Inductors combine like resistors and capacitors like conductances, and the equivalent must also carry the correct initial condition.
- For the stable circuits here with positive equivalent resistance, natural responses decay as $e^{-\frac{t}{\tau}}$ with $\tau=\dfrac{L}{R}$ or $RC$. After $5\tau$, less than $1\%$ of the initial distance from the final value remains.
- The stable first-order natural and DC step responses here have the form $x(\infty)+[x(0^+)-x(\infty)]e^{-\frac{t}{\tau}}$, with $\tau$ found from the equivalent resistance after switching.

### Formula sheet

| Result | Formula | Use when |
|---|---|---|
| Inductor law | $v = L\,\dfrac{di}{dt}$ | Current is known and you need the voltage (passive sign convention) |
| Inductor current | $i(t) = \dfrac{1}{L}\displaystyle\int_{t_0}^{t} v\,d\tau + i(t_0)$ | Voltage is known and you need the current |
| Capacitor law | $i = C\,\dfrac{dv}{dt}$ | Voltage is known and you need the current |
| Capacitor voltage | $v(t) = \dfrac{1}{C}\displaystyle\int_{t_0}^{t} i\,d\tau + v(t_0)$ | Current is known and you need the voltage |
| Stored energy | $w_L = \tfrac12 Li^2,\; w_C = \tfrac12 Cv^2$ | Energy at an instant, maximum energy, or energy balance |
| Power | $p_L=vi=Li\,\dfrac{di}{dt}$; $p_C=vi=Cv\,\dfrac{dv}{dt}$ (passive references) | Deciding whether the element stores ($p>0$) or delivers ($p<0$) |
| Series / parallel $L$ | $L_{eq} = \sum L_k$; $\dfrac{1}{L_{eq}} = \sum\dfrac{1}{L_k}$, $i(t_0) = \sum i_k(t_0)$ | Reducing several inductors to one |
| Series / parallel $C$ | $\dfrac{1}{C_{eq}} = \sum\dfrac{1}{C_k}$, $v(t_0) = \sum v_k(t_0)$; $C_{eq} = \sum C_k$ | Reducing several capacitors to one |
| Time constant | $\tau = \dfrac{L}{R_{Th}}$ or $\tau = R_{Th}C$ | Stable first-order circuits with positive equivalent resistance |
| Natural response | $x(t) = x(0^+)\,e^{-\frac{t}{\tau}}$ | Stored energy decays with no source acting |
| General response | $x(t)=x(\infty)+[x(t_0^+)-x(\infty)]e^{-\frac{t-t_0}{\tau}}$ | Stable first-order DC response after switching at $t_0$ |
| Energy decay | $w(t) = w(0)\,e^{-\frac{2t}{\tau}}$ | Fraction of stored energy remaining or dissipated |
