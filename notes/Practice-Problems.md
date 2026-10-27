# Practice Problems

## Kirchhoff's laws and Ohm's law (meters, bridges, Δ–Y)

### Problem 1 · Walk back from one known current

*Textbook P2.20*

The current $i_a$ is $2\,\mathrm{mA}$. Find **(a)** $i_o$, **(b)** $i_g$ and **(c)** the power delivered by the current source.

```schematic
I1 0,0 -> 0,3 "$i_g$"
R1 2,3 -> 2,0 "$2\,\mathrm{k\Omega}$" i="$i_o$"
R2 2,3 -> 5,3 "$1\,\mathrm{k\Omega}$" i="$i_a$"
R3 5,3 -> 5,0 "$4\,\mathrm{k\Omega}$" flip
R4 5,0 -> 2,0 "$3\,\mathrm{k\Omega}$"
wire 0,3 -> 2,3
wire 2,0 -> 0,0
label 2,3 "$a$" above
label 5,3 "$b$" above
label 5,0 "$c$" right
label 0,0 "$d$" left
```

### Problem 2 · Split currents and check power

*Tutorial 1, P2.19*

Find $i_1$, $i_2$ and $v_o$, and check that the power balances.

```schematic
I1 0,0 -> 0,3 "$1.5\,\mathrm{A}$" v_rev="$v_o$"
wire 0,3 -> 4,3
wire 8,0 -> 0,0
R1 4,3 -> 4,0 "$100\,\Omega$" i="$i_1$"
R2 4,3 -> 8,3 "$150\,\Omega$" i="$i_2$"
R3 8,3 -> 8,0 "$250\,\Omega$"
```

### Problem 3 · Two circuits joined by one wire

*Tutorial 1, P2.35*

Find $i_o$ (the current in the wire joining the two networks), $i_1$ and $i_2$.

```schematic
V1 0,3 -> 0,0 "$18\,\mathrm{V}$"
R1 0,3 -> 3,3 "$12\,\Omega$"
R2 3,3 -> 3,0 "$6\,\Omega$" v="$v_\Delta$"
wire 3,0 -> 0,0
wire 3,0 -> 5,0
label 4,0 "$\leftarrow i_o$" below
G1 5,3 -> 5,0 "$\dfrac{v_\Delta}{2}$"
wire 5,3 -> 10,3
wire 5,0 -> 10,0
R3 7.5,3 -> 7.5,0 "$10\,\Omega$" i="$i_1$"
R4 10,3 -> 10,0 "$5\,\Omega$" i="$i_2$"
```

### Problem 4 · Balanced bridge and resistor ratings

*Assessment Problem 3.7*

The bridge is balanced (no galvanometer current). Find $R_x$, and check whether any resistor exceeds a $250\,\mathrm{mW}$ rating.

```schematic
V1 0,4 -> 0,0 "$5\,\mathrm{V}$"
wire 0,4 -> 6,4
wire 6,0 -> 0,0
R1 3,4 -> 3,2 "$100\,\Omega$"
R3 3,2 -> 3,0 "$150\,\Omega$"
R2 6,4 -> 6,2 "$1\,\mathrm{k\Omega}$"
R4 6,2 -> 6,0 "$R_x$"
AM1 3,2 -> 6,2 "galvanometer"
```

### Problem 5 · A triangle with no series or parallel pairs

*Textbook P3.58*

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
wire 0,0 -> 4,0
wire 4,0 -> 8,0
```

## Nodal, mesh and source transformation

### Problem 6 · A bridge fed by a current source

*Tutorial 4, Problem 4*

Find $i_o$, $i_1$, $i_2$ and the power delivered by the current source.

```schematic
I1 0,0 -> 0,3 "$1\,\mathrm{A}$"
R1 3,3 -> 3,0 "$240\,\Omega$"
R2 3,3 -> 6,3 "$20\,\Omega$"
R3 6,3 -> 6,0 "$100\,\Omega$" i="$i_2$"
R4 6,3 -> 9,3 "$50\,\Omega$"
R5 9,3 -> 9,0 "$600\,\Omega$" i="$i_o$"
R6 3,5 -> 9,5 "$320\,\Omega$" i="$i_1$"
wire 0,3 -> 3,3
wire 3,3 -> 3,5
wire 9,5 -> 9,3
wire 9,0 -> 0,0
label 3,5 "$a$" left
label 6,3 "$b$" above
label 9,3 "$c$" right
ground 0,0
```

### Problem 7 · Power in the middle resistor

*Assessment Problem 4.10*

Find the power dissipated in the $2\,\Omega$ resistor.

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
```

### Problem 8 · A current source between two windows

*Assessment Problem 4.12*

Find the power dissipated in the $1\,\Omega$ resistor.

```schematic
V1 0,2 -> 0,0 "$10\,\mathrm{V}$"
I1 0,2 -> 3,2 "$2\,\mathrm{A}$"
wire 0,2 -> 0,4
R1 0,4 -> 6,4 "$2\,\Omega$"
wire 6,4 -> 6,2
R2 3,2 -> 6,2 "$2\,\Omega$"
R3 3,2 -> 3,0 "$2\,\Omega$"
V2 6,0 -> 6,2 "$6\,\mathrm{V}$"
R4 6,0 -> 3,0 "$1\,\Omega$"
wire 3,0 -> 0,0
label 3,2 "$m$" above
label 6,2 "$r$" right
label 6,0 "$q$" right
ground 0,0
```

### Problem 9 · A dependent source watches the shared branch

*Textbook P4.47*

Find **(a)** $i_\Delta$; **(b)** the power delivered by the independent current source; **(c)** the power delivered by the dependent voltage source.

```schematic
I1 0,0 -> 0,3 "$8\,\mathrm{mA}$"
R1 0,3 -> 3.5,3 "$980\,\Omega$"
R2 3.5,3 -> 3.5,0 "$3.3\,\mathrm{k\Omega}$" i_rev="$i_\Delta$"
R3 3.5,3 -> 7.5,3 "$1.8\,\mathrm{k\Omega}$"
E1 7.5,3 -> 7.5,0 "$200i_\Delta$"
R4 7.5,0 -> 3.5,0 "$4.7\,\mathrm{k\Omega}$"
wire 3.5,0 -> 0,0
label 0,3 "$s$" above
label 3.5,3 "$a$" above
ground 0,0
```

### Problem 10 · A voltage source that floats between two nodes

*Textbook P4.27*

Find $v$.

```schematic
I1 0,0 -> 0,3 "$4.8\,\mathrm{A}$"
R1 2.5,3 -> 2.5,0 "$7.5\,\Omega$" i="$i_x$"
R2 2.5,3 -> 5,3 "$2.5\,\Omega$"
R3 5,3 -> 5,0 "$10\,\Omega$" v="$v$"
E1 7.5,3 -> 5,3 "$i_x$"
R4 7.5,3 -> 7.5,0 "$2.5\,\Omega$"
R5 7.5,3 -> 10,3 "$1\,\Omega$"
V1 10,3 -> 10,0 "$12\,\mathrm{V}$"
wire 0,3 -> 2.5,3
wire 10,0 -> 0,0
label 2.5,3 "$a$" above
label 5,3 "$b$" above
label 7.5,3 "$c$" above
ground 0,0
```

### Problem 11 · Two current sources at the ends

*Textbook P4.62*

**(a)** Make a series of source transformations to find $v_o$.

**(b)** Check your answer with the mesh-current method.

```schematic
I1 0,3 -> 0,0 "$2.5\,\mathrm{mA}$"
wire 0,3 -> 2,3
R1 2,3 -> 2,0 "$8\,\mathrm{k\Omega}$"
R2 2,3 -> 4.5,3 "$24\,\mathrm{k\Omega}$" v="$v_o$"
R3 4.5,3 -> 4.5,0 "$80\,\mathrm{k\Omega}$"
R4 4.5,3 -> 7,3 "$15\,\mathrm{k\Omega}$"
V1 7,3 -> 9.5,3 "$40\,\mathrm{V}$"
R5 9.5,3 -> 9.5,0 "$5\,\mathrm{k\Omega}$"
wire 9.5,3 -> 11.5,3
I2 11.5,0 -> 11.5,3 "$12\,\mathrm{mA}$"
wire 0,0 -> 11.5,0
label 2,3 "$a$" above
label 4.5,3 "$b$" above
label 7,3 "$c$" above
label 9.5,3 "$d$" above
ground 7,0
```

### Problem 12 · Shrink it for one voltage, then go back for the powers

*Textbook P4.63*

**(a)** Find $v_o$. **(b)** Find the power developed by the $340\,\mathrm{V}$ source and **(c)** by the $5\,\mathrm{A}$ source. **(d)** Check the power balance.

```schematic
I1 0,0 -> 0,3 "$5\,\mathrm{A}$"
R1 0,3 -> 2.5,3 "$8\,\Omega$"
R2 2.5,3 -> 2.5,0 "$20\,\Omega$"
V1 2.5,3 -> 5,3 "$340\,\mathrm{V}$"
wire 2.5,3 -> 2.5,5
R3 2.5,5 -> 5,5 "$80\,\Omega$"
wire 5,5 -> 5,3
R4 5,3 -> 7.5,3 "$5\,\Omega$"
wire 7.5,3 -> 9.5,3
R5 9.5,3 -> 9.5,0 "$45\,\Omega$"
wire 0,0 -> 2.5,0
R6 2.5,0 -> 7.5,0 "$10\,\Omega$"
wire 7.5,0 -> 9.5,0
gap 7.5,3 -> 7.5,0 v="$v_o$"
label 2.5,3 "$q$" above
label 5,3 "$r$" below
label 7.5,0 "$m$" below
ground 0,0
```

## Thévenin and Norton

### Problem 13 · Thévenin: one equivalent, any load

*Tutorial 4, Problem 3.2*

a) Find the no-load value of $v_o$.

b) Find $v_o$ when $R_L=150\,\mathrm{k\Omega}$.

c) How much power is dissipated in the $25\,\mathrm{k\Omega}$ resistor if the load terminals are accidentally short-circuited?

d) What is the maximum power dissipated in the $75\,\mathrm{k\Omega}$ resistor?

```schematic
V1 0,3 -> 0,0 "$200\,\mathrm{V}$"
R1 0,3 -> 3,3 "$25\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$75\,\mathrm{k\Omega}$"
wire 3,3 -> 5,3
wire 0,0 -> 5,0
terminal 5,3
terminal 5,0
wire 5,3 -> 7,3
R3 7,3 -> 7,0 "$R_L$"
wire 5,0 -> 7,0
gap 5,3 -> 5,0 v="$v_o$"
```

### Problem 14 · Thévenin

*Practice problem (from your list)*

Find $V_o$ using Thévenin's theorem.

```schematic
R1 0,3 -> 0,0 "$2\,\mathrm{k\Omega}$"
V1 0,3 -> 3,3 "$6\,\mathrm{V}$"
R2 3,3 -> 3,0 "$4\,\mathrm{k\Omega}$"
V2 6,3 -> 3,3 "$12\,\mathrm{V}$"
R3 6,3 -> 6,0 "$2\,\mathrm{k\Omega}$"
wire 6,3 -> 8,3
wire 0,0 -> 8,0
terminal 8,3
terminal 8,0
gap 8,3 -> 8,0 v="$V_o$"
```

### Problem 15 · Thévenin: two meshes, then a walk

*Assessment Problem 4.16*

Find the Thévenin equivalent circuit with respect to the terminals $a$, $b$.

```schematic
V1 0,2.5 -> 0,0 "$72\,\mathrm{V}$"
R1 0,2.5 -> 3,2.5 "$5\,\Omega$"
R2 3,2.5 -> 3,0 "$20\,\Omega$"
R3 3,2.5 -> 6,2.5 "$8\,\Omega$"
wire 0,2.5 -> 0,4.5 -> 1.5,4.5
R4 1.5,4.5 -> 4.5,4.5 "$12\,\Omega$"
wire 4.5,4.5 -> 6,4.5 -> 6,2.5
wire 6,2.5 -> 7.5,2.5
wire 0,0 -> 7.5,0
terminal 7.5,2.5
terminal 7.5,0
label 7.5,2.5 "$a$" right
label 7.5,0 "$b$" right
```

### Problem 16 · Thévenin by source transformations, then a voltmeter

*Assessment Problem 4.18*

A voltmeter with an internal resistance of $100\,\mathrm{k\Omega}$ is used to measure $v_{AB}$.

Use source transformations to find the Thévenin equivalent at $A$, $B$, then find the voltmeter reading.

```schematic
V1 0,0 -> 0,3 "$36\,\mathrm{V}$"
R1 0,3 -> 3.5,3 "$12\,\mathrm{k\Omega}$"
I1 3.5,0 -> 3.5,3 "$18\,\mathrm{mA}$" flip
wire 3.5,3 -> 6,3
R2 6,3 -> 6,0 "$60\,\mathrm{k\Omega}$" flip
R3 6,3 -> 9,3 "$15\,\mathrm{k\Omega}$"
wire 0,0 -> 9,0
terminal 9,3
terminal 9,0
label 9,3 "$A$" above
label 9,0 "$B$" below
gap 9,3 -> 9,0 v="$v_{AB}$"
```

### Problem 17 · Thévenin: a dependent source needs a test source

*Assessment Problem 4.20*

Find the Thévenin equivalent at $a$–$b$. The dependent source is controlled by $i_\Delta$, the current down the $40\,\Omega$.

```schematic
R1 0,3 -> 0,0 "$60\,\Omega$"
wire 0,3 -> 2,3
I1 2,0 -> 2,3 "$4\,\mathrm{A}$"
R2 2,3 -> 4,3 "$20\,\Omega$"
E1 4,3 -> 6,3 "$160i_\Delta$"
R3 6,3 -> 6,0 "$80\,\Omega$"
R4 9,3 -> 9,0 "$40\,\Omega$" i="$i_\Delta$"
wire 6,3 -> 9,3
wire 9,3 -> 10.5,3
wire 0,0 -> 10.5,0
terminal 10.5,3 "$a$" right
terminal 10.5,0 "$b$" right
ground 6,0
```

### Problem 18 · Norton: a shorted internal branch

*Textbook P4.64*

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
```

### Problem 19 · Norton: a negative Norton current

*Textbook P4.67*

Find the Norton equivalent at $a$–$b$.

```schematic
I1 0,0 -> 0,3 "$10\,\mathrm{mA}$"
R1 2,3 -> 2,0 "$10\,\mathrm{k\Omega}$"
V1 4,3 -> 4,0 "$30\,\mathrm{V}$"
wire 0,3 -> 4,3
R2 4,3 -> 7,3 "$15\,\mathrm{k\Omega}$"
I2 7,3 -> 7,0 "$3\,\mathrm{mA}$"
R3 9,3 -> 9,0 "$5\,\mathrm{k\Omega}$" flip
wire 7,3 -> 12,3
terminal 12,3 "$a$" right
terminal 12,0 "$b$" right
wire 0,0 -> 12,0
ground 0,0
```

### Problem 20 · Norton: a dependent source stays on

*Textbook Assessment Problem 4.19*

Find the Norton equivalent circuit with respect to the terminals $a$, $b$.

```schematic
V1 0,3 -> 0,0 "$280\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\mathrm{k\Omega}$" i="$i_\Delta$"
R2 3,3 -> 3,0 "$2\,\mathrm{k\Omega}$"
R3 3,3 -> 6,3 "$2\,\mathrm{k\Omega}$"
wire 3,3 -> 3,5.2
F1 3,5.2 -> 6,5.2 "$0.2i_\Delta$"
wire 6,5.2 -> 6,3
R4 6,3 -> 6,0 "$5.6\,\mathrm{k\Omega}$"
wire 6,3 -> 8,3
terminal 8,3 "$a$" right
wire 0,0 -> 8,0
terminal 8,0 "$b$" right
```

## Maximum power transfer and superposition

### Problem 21 · Matched load and efficiency

*Assessment Problem 4.19 (Textbook P4.75, P4.83)*

Find **(a)** $V_{\mathrm{Th}}$; **(b)** $R_{\mathrm{Th}}$ using a test source; **(c)** the Norton equivalent; **(d)** the adjustable load $R_o$ for maximum power, and that power; **(e)** the percentage of the total developed power delivered to that load.

```schematic
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
wire 0,3 -> 0,5
G1 3,5 -> 0,5 "$3i_x$"
wire 3,5 -> 3,3
wire 3,3 -> 5,3
I1 5,3 -> 5,0 "$4\,\mathrm{A}$"
wire 5,3 -> 7,3
R2 7,3 -> 7,0 "$8\,\Omega$" i="$i_x$"
wire 7,3 -> 9,3
terminal 9,3 "$a$" right
terminal 9,0 "$b$" right
ground 0,0
wire 0,0 -> 9,0
```

### Problem 22 · Max power: efficiency with a dependent source

*Assessment Problem 4.21 (Textbook P4.85, P4.86)*

$R_o$ is set for maximum power; $v_\phi$ is the voltage across the $4\,\Omega$ in series with the $20\,\mathrm{V}$ source. **(a)** Find $R_o$. **(b)** Find $p_{\max}$. **(c)** What percentage of the power developed reaches $R_o$?

```schematic
V1 0,4 -> 0,0 "$100\,\mathrm{V}$"
R1 0,4 -> 3,4 "$4\,\Omega$"
R2 3,4 -> 6,4 "$4\,\Omega$"
R3 3,4 -> 3,2 "$4\,\Omega$" v="$v_\phi$"
V2 3,2 -> 3,0 "$20\,\mathrm{V}$"
wire 0,4 -> 0,6
E1 3,6 -> 0,6 "$v_\phi$"
R4 3,6 -> 6,6 "$4\,\Omega$"
wire 6,6 -> 6,4
wire 6,4 -> 8,4
wire 0,0 -> 8,0
label 3,4 "$c$" below
label 3,6 "$t$" above
label 8,4 "$a$" above
ground 0,0
RO 8,4 -> 8,0 "$R_o$"
```

### Problem 23 · Max power: a current-controlled source stays on

*Textbook P4.91*

Find **(a)** $R_L$ for maximum power transfer and **(b)** the maximum power. The source on the left has $+$ at its bottom; $i_\beta$ points right through the $6\,\Omega$.

```schematic
V1 0,0 -> 0,4 "$480\,\mathrm{V}$"
R1 0,4 -> 4,4 "$6\,\Omega$" i="$i_\beta$"
R3 6,4 -> 8,4 "$8\,\Omega$"
E1 8,0 -> 8,4 "$20i_\beta$"
R4 0,0 -> 4,0 "$4\,\Omega$"
R5 6,0 -> 8,0 "$2\,\Omega$"
wire 0,4 -> 0,6
R6 0,6 -> 8,6 "$4\,\Omega$"
wire 8,6 -> 8,4
wire 4,4 -> 6,4
wire 4,0 -> 6,0
label 0,4 "$a$" left
label 4,4 "$p$" above
ground 4,0
R2 4,4 -> 4,0 "$40\,\Omega$"
RL 5,4 -> 5,0 "$R_L$"
```

### Problem 24 · Superposition with three sources

*Textbook P4.94*

Use superposition to find $i_o$.

```schematic
I1 0,0 -> 0,4 "$6\,\mathrm{A}$"
wire 0,4 -> 2,4
R1 2,4 -> 2,0 "$20\,\Omega$"
R2 2,4 -> 4.5,4 "$1\,\Omega$" i="$i_o$"
I2 4.5,4 -> 4.5,0 "$10\,\mathrm{A}$"
wire 4.5,4 -> 10.5,4
R3 6.5,4 -> 6.5,0 "$60\,\Omega$"
R4 8.5,4 -> 8.5,2 "$5\,\Omega$"
V1 8.5,2 -> 8.5,0 "$75\,\mathrm{V}$"
R5 10.5,4 -> 10.5,0 "$30\,\Omega$"
wire 0,0 -> 10.5,0
label 1.1,4 "$p$" above
label 4.5,4 "$q$" above
label 8.5,2 "$k$" right
ground 0,0
```

### Problem 25 · Superposition: add a source to a solved circuit

*Textbook P4.96*

Before the $5\,\mathrm{mA}$ source is attached between $a$ and $b$, $i_o=3.5\,\mathrm{mA}$. **(a)** Use superposition to find $i_o$ after it is attached. **(b)** Check with all three sources on.

```schematic
V1 0,3 -> 0,0 "$8\,\mathrm{V}$"
R1 3,3 -> 3,0 "$5\,\mathrm{k\Omega}$"
R2 3,3 -> 6,3 "$2\,\mathrm{k\Omega}$"
R3 6,3 -> 6,0 "$6\,\mathrm{k\Omega}$" i="$i_o$"
I1 9,0 -> 9,3 "$10\,\mathrm{mA}$" flip
wire 3,3 -> 3,5
I2 6,5 -> 3,5 "$5\,\mathrm{mA}$"
wire 6,5 -> 6,3
wire 0,3 -> 3,3
wire 6,3 -> 9,3
wire 0,0 -> 9,0
label 3,3 "$a$" below
label 6,3 "$b$" below
ground 0,0
```

### Problem 26 · Superposition: the dependent source stays on

*Textbook P4.98*

Use superposition to find $v_o$.

```schematic
V1 0,3 -> 0,0 "$25\,\mathrm{V}$"
R1 4,3 -> 0,3 "$4\,\mathrm{k\Omega}$" i="$i_\phi$"
I1 4,3 -> 4,0 "$5\,\mathrm{mA}$"
R2 8,3 -> 8,0 "$20\,\mathrm{k\Omega}$" v="$v_o$"
wire 0,3 -> 0,5
G1 0,5 -> 8,5 "$2.2i_\phi$"
wire 8,5 -> 8,3
wire 4,3 -> 8,3
wire 0,0 -> 8,0
label 4,3 "$n$" above
ground 0,0
```

## Midterm Practice

### Problem 27 · Q1: Thévenin and maximum power

*ELEC 221 Midterm, Fall 2025, Question 1 (Fig. P1)*

**(a)** Find the Thévenin equivalent circuit seen by $R_L$. **(b)** Find the $R_L$ that receives the maximum power. **(c)** With this $R_L$, find the maximum power delivered to $R_L$.

*$R_L$ is drawn straight here instead of diagonal: it still goes from the top-right node $a$ down to the bottom wire $b$.*

```schematic
V1 0,3 -> 0,0 "$5\,\mathrm{V}$"
R2A 0,3 -> 3,3 "$2\,\Omega$"
wire 0,3 -> 0,5
R4 0,5 -> 6,5 "$4\,\Omega$"
wire 6,5 -> 6,3
I1 3,0 -> 3,3 "$3\,\mathrm{A}$"
R2B 3,3 -> 6,3 "$2\,\Omega$"
RL 6,3 -> 6,0 "$R_L=12\,\Omega$" v="$V_L$"
wire 6,3 -> 9,3
R1 9,3 -> 9,0 "$1\,\Omega$"
R5 9,0 -> 6,0 "$5\,\Omega$"
wire 0,0 -> 6,0
label 7,3 "$a$" above
label 6,0 "$b$" below
ground 0,0
```

### Problem 28 · Q2: Superposition, add a source

*ELEC 221 Midterm, Fall 2025, Question 2 (Fig. P2)*

In the circuit of Question 1, the voltage across $R_L=12\,\Omega$ is $V_L$. A voltage source $v_x=3\,\mathrm{V}$ is added in series with the $4\,\Omega$, as shown. How much does $V_L$ change? *Hint: use superposition.*

```schematic
V1 0,3 -> 0,0 "$5\,\mathrm{V}$"
R2A 0,3 -> 3,3 "$2\,\Omega$"
wire 0,3 -> 0,5
R4 0,5 -> 3,5 "$4\,\Omega$"
VX 6,5 -> 3,5 "$v_x=3\,\mathrm{V}$"
wire 6,5 -> 6,3
I1 3,0 -> 3,3 "$3\,\mathrm{A}$"
R2B 3,3 -> 6,3 "$2\,\Omega$"
RL 6,3 -> 6,0 "$R_L=12\,\Omega$" v="$V_L$"
wire 6,3 -> 9,3
R1 9,3 -> 9,0 "$1\,\Omega$"
R5 9,0 -> 6,0 "$5\,\Omega$"
wire 0,0 -> 6,0
label 7,3 "$a$" above
label 6,0 "$b$" below
ground 0,0
```

### Problem 29 · Q3: Series and parallel back and forth

*ELEC 221 Midterm, Fall 2025, Question 3 (Fig. P3)*

Find $I_x$ and $V_x$.

*The current source's value is cut off on the posted exam, so we use $9\,\mathrm{A}$ here.*

```schematic
I1 0,0 -> 0,4 "$9\,\mathrm{A}$"
wire 0,4 -> 2,4
R2 2,4 -> 2,0 "$2\,\Omega$"
R1 2,4 -> 5,4 "$1\,\Omega$" v="$V_x$"
R4 5,4 -> 5,2 "$4\,\Omega$"
wire 4,2 -> 6,2
R3 4,2 -> 4,0 "$3\,\Omega$" i="$I_x$"
R6 6,2 -> 6,0 "$6\,\Omega$"
R12A 5,4 -> 8,4 "$1.2\,\Omega$"
R8 8,4 -> 8,0 "$8\,\Omega$"
wire 8,4 -> 10,4
R12 10,4 -> 10,0 "$12\,\Omega$"
wire 0,0 -> 10,0
ground 0,0
```

### Problem 30 · Q4: Dependent source, equations then solve

*ELEC 221 Midterm, Fall 2025, Question 4*

**(a)** Write (but do not solve) the set of simultaneous equations needed to solve the circuit, using either the node-voltage or the mesh-current method. **(b)** Solve for $i_\Delta$ any way you choose.

```schematic
E1 0,3 -> 0,0 "$5i_\Delta$"
wire 0,3 -> 0,5
RT 6,5 -> 0,5 "$10\,\Omega$" i="$i_\Delta$"
wire 6,5 -> 6,3
RA 0,3 -> 3,3 "$10\,\Omega$"
RB 3,3 -> 6,3 "$10\,\Omega$"
I1 3,0 -> 3,3 "$2\,\mathrm{A}$"
R30 6,3 -> 6,0 "$30\,\Omega$"
wire 0,0 -> 6,0
ground 0,0
```
