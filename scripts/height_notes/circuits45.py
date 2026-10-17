"""Week 4 and Week 5 circuits: drawing (schematic language) + netlist for mna.py.

Netlist element names match the drawing's element names; node '0' is the drawing's ground node.
Tuples: ('R',n,a,b,ohms) ('V',n,p,m,volts) ('I',n,a,b,amps: arrow a->b) ('E',n,p,m,{node:k},const) ('G',n,a,b,{node:k}).
Extra elements used only by height-view tabs (shorts, loads, test sources) are added in the builders.
"""

C = {}


def add(key, sch, net):
    C[key] = {'sch': sch.strip('\n'), 'net': net}


# ============================================================ Week 4
add('w4S', r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$" flip
wire 3,3 -> 6,3
I1 6,0 -> 6,3 "$1\,\mathrm{A}$" flip
wire 6,0 -> 0,0
label 3,3 "$x$" above
ground 0,0
''', [('V', 'V1', 't', '0', 12), ('R', 'R1', 't', 'x', 4), ('R', 'R2', 'x', '0', 4), ('I', 'I1', '0', 'x', 1)])

# Topic 1: lecture example, power in the 300 ohm resistor
add('lec300', r'''
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
''', [('V', 'V1', 's', '0', 256), ('R', 'R1', 's', 'a', 150), ('R', 'R2', 'a', '0', 200), ('R', 'R3', 'a', 'b', 100),
      ('E', 'E1', 'b', '0', {'c': 50 / 300, 'a': -50 / 300}, 0), ('R', 'R4', 'b', 'c', 250), ('R', 'R5', 'c', '0', 400),
      ('R', 'R6', 'c', 'd', 500), ('V', 'V2', '0', 'd', 128), ('R', 'R7', 'c', 'a', 300)])

add('p454', r'''
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
''', [('I', 'I1', '0', 't', 4), ('R', 'R1', 't', 'l', 8), ('R', 'R3', 'l', '0', 1), ('R', 'R2', 't', 'r', 2),
      ('R', 'R4', 'r', '0', 4), ('R', 'R5', 'l', 'r', 10)])

# Topic 2: source transformation, voltage form with a load (current form is a view-only net)
add('stx', r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
wire 3,3 -> 5,3
R2 5,3 -> 5,0 "$2\,\Omega$" flip
wire 5,0 -> 0,0
terminal 3,3 "$a$" above
ground 0,0
''', [('V', 'V1', 's', '0', 12), ('R', 'R1', 's', 'a', 4), ('R', 'R2', 'a', '0', 2)])

add('lec250', r'''
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
''', [('V', 'V1', 's', '0', 250), ('R', 'R2', 's', '0', 125), ('R', 'R1', 's', 'b', 25), ('R', 'R4', 'b', '0', 100),
      ('I', 'I1', 'b', 'd', 8), ('R', 'R3', 'd', '0', 10), ('R', 'R5', 'b', 'e', 5), ('R', 'R6', 'e', '0', 15)])

add('p459', r'''
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
''', [('I', 'I1', 'a', '0', 0.006), ('R', 'R1', 'a', '0', 2300), ('R', 'R2', 'b', 'a', 2700), ('R', 'R3', 'b', '0', 1000),
      ('I', 'I2', '0', 'b', 0.0042)])

add('lecp9', r'''
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
''', [('V', 'V1', 's', '0', 6), ('R', 'R1', 's', 'c', 4), ('R', 'R2', 'c', '0', 30), ('R', 'R3', 'c', 'd', 6),
      ('R', 'R4', 'd', 'f', 20), ('R', 'R5', 'd', 'e', 5), ('V', 'V2', 'e', 'f', 40), ('R', 'R6', '0', 'f', 10)])

# Topic 3: the Thévenin picture itself, then the lecture example
add('thpic', r'''
V1 0,3 -> 0,0 "$V_{\mathrm{Th}}=32\,\mathrm{V}$"
R1 0,3 -> 3,3 "$R_{\mathrm{Th}}=8\,\Omega$"
wire 3,3 -> 5,3
RL 5,3 -> 5,0 "$R_L$" flip
wire 5,0 -> 0,0
terminal 3,3 "$a$" above
terminal 3,0 "$b$" below
ground 0,0
''', [('V', 'V1', 't', '0', 32), ('R', 'R1', 't', 'a', 8), ('R', 'RL', 'a', '0', 24)])

add('lecth', r'''
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
''', [('V', 'V1', 's', '0', 25), ('R', 'R1', 's', 'n', 5), ('R', 'R2', 'n', '0', 20), ('I', 'I1', '0', 'n', 3),
      ('R', 'R3', 'n', 'a', 4)])

add('p465', r'''
V1 0,4 -> 0,0 "$80\,\mathrm{V}$"
R1 0,4 -> 4,4 "$10\,\Omega$"
R2 4,4 -> 4,0 "$30\,\Omega$"
R3 4,4 -> 8,4 "$2.5\,\Omega$"
terminal 8,4 "$a$" right
terminal 8,0 "$b$" right
label 4,4 "$m$" above
wire 0,0 -> 8,0
ground 0,0
''', [('V', 'V1', 's', '0', 80), ('R', 'R1', 's', 'm', 10), ('R', 'R2', 'm', '0', 30), ('R', 'R3', 'm', 'a', 2.5)])

add('p464', r'''
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
''', [('I', 'I1', 'q', 'p', 15), ('R', 'R1', 'p', 'q', 8), ('R', 'R2', 'p', 'a', 2), ('R', 'R3', 'a', '0', 12),
      ('R', 'R4', 'q', '0', 10)])

# P4.69: the network is a box; the load is the only drawn element besides it
add('p469', r'''
X1 0,3 -> 0,0 "network"
wire 0,3 -> 3,3
wire 0,0 -> 3,0
RL 3,3 -> 3,0 "$R_L$" flip
terminal 3,3 "$a$" above
terminal 3,0 "$b$" below
ground 0,0
''', [])

# Practice
add('p463', r'''
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
''', [('I', 'I1', '0', 'p', 5), ('R', 'R1', 'p', 'q', 8), ('R', 'R2', 'q', '0', 20), ('V', 'V1', 'q', 'r', 340),
      ('R', 'R3', 'q', 'r', 80), ('R', 'R4', 'r', 's', 5), ('R', 'R5', 's', 'm', 45), ('R', 'R6', '0', 'm', 10)])

add('p460', r'''
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
''', [('I', 'I1', '0', 'p', 4), ('R', 'R1', 'p', '0', 5), ('R', 'R2', 'p', 'q', 4), ('R', 'R3', 'q', 'r', 1),
      ('I', 'I2', 'r', 'q', 10), ('R', 'R4', 'r', 'k', 40), ('V', 'V1', 'k', '0', 10), ('R', 'R5', 'r', '0', 2)])

add('p468', r'''
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
''', [('V', 'V1', 's', '0', 300), ('R', 'R1', 's', 'm', 40), ('R', 'R2', 'm', '0', 8), ('R', 'R3', 'm', 'a', 10),
      ('R', 'R4', 's', 'a', 150), ('I', 'I1', 'a', 's', 3)])

add('p473', r'''
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
''', [('R', 'R1', 'p', 's', 10e3), ('V', 'V1', 's', '0', 30), ('R', 'R2', 'p', '0', 40e3), ('R', 'R3', 'p', 'q', 4e3),
      ('I', 'I1', '0', 'q', 8e-3), ('R', 'R4', 'q', 'a', 3e3), ('R', 'R5', 'a', '0', 10e3)])

# Week 4 summary visuals
add('w4A', r'''
V1 0,3 -> 0,0 "$9\,\mathrm{V}$"
R1 0,3 -> 3,3 "$3\,\Omega$"
wire 3,3 -> 5,3
R2 5,3 -> 5,0 "$6\,\Omega$" flip
wire 5,0 -> 0,0
terminal 3,3 "$a$" above
ground 0,0
''', [('V', 'V1', 's', '0', 9), ('R', 'R1', 's', 'a', 3), ('R', 'R2', 'a', '0', 6)])

add('w4C', r'''
V1 0,3 -> 0,0 "$18\,\mathrm{V}$"
R1 0,3 -> 3,3 "$6\,\Omega$"
R2 3,3 -> 3,0 "$3\,\Omega$"
wire 3,3 -> 6,3
wire 3,0 -> 6,0
terminal 6,3 "$a$" right
terminal 6,0 "$b$" right
wire 0,0 -> 3,0
ground 0,0
''', [('V', 'V1', 's', '0', 18), ('R', 'R1', 's', 'a', 6), ('R', 'R2', 'a', '0', 3)])

# ============================================================ Week 5
# Start here: same 18 V / 6 / 3 divider as the W4 summary (V_Th 6 V, R_Th 2 ohm)

# Topic 1: dependent sources only (lecture), R_Th negative
add('lecneg', r'''
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
''', [('E', 'E1', 's', '0', {'a': 3}, 0), ('R', 'R1', 's', 'a', 2), ('R', 'R2', 'a', '0', 4)])

# Topic 1: Method 4 (lecture), all sources on plus a test source
add('lecm4', r'''
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
''', [('V', 'V1', 's', '0', 5), ('R', 'R1', 's', 'm', 2000), ('E', 'E1', 'm', '0', {'a': 3}, 0),
      ('G', 'G1', 'a', '0', {'s': 20 / 2000, 'm': -20 / 2000}), ('R', 'R2', 'a', '0', 25)])

add('ap419', r'''
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
''', [('V', 'V1', 's', '0', 24), ('R', 'R1', 's', 'a', 2), ('G', 'G1', 'a', 's', {'a': 3 / 8}),
      ('I', 'I1', 'a', '0', 4), ('R', 'R2', 'a', '0', 8)])

add('p480', r'''
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
''', [('E', 'E1', 'x', '0', {'a': 10 / 12, 'm': -10 / 12}, 0), ('R', 'R1', 'x', 'a', 6), ('R', 'R2', 'x', 'm', 10),
      ('R', 'R3', 'a', 'm', 12), ('R', 'R4', 'm', '0', 2.5)])

# Topic 2: maximum power
add('lec360', r'''
V1 0,3 -> 0,0 "$360\,\mathrm{V}$"
R1 0,3 -> 3,3 "$30\,\Omega$"
R2 3,3 -> 3,0 "$150\,\Omega$"
wire 3,3 -> 6,3
R3 6,3 -> 6,0 "$R_L$"
wire 0,0 -> 6,0
label 3,3 "$a$" above
ground 0,0
''', [('V', 'V1', 's', '0', 360), ('R', 'R1', 's', 'a', 30), ('R', 'R2', 'a', '0', 150)])

add('lecmp', r'''
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
''', [('V', 'V1', '0', 'c', 3), ('I', 'I1', 'c', 'a', 0.002), ('R', 'R2', 'c', 'm', 3000), ('R', 'R1', 'a', 'm', 4000),
      ('R', 'R3', 'm', '0', 6000)])

add('p484', r'''
V1 0,3 -> 0,0 "$30\,\mathrm{V}$"
R1 0,3 -> 3,3 "$R_o$"
R2 3,3 -> 3,0 "$6\,\Omega$"
wire 0,0 -> 3,0
label 3,3 "$a$" above
ground 0,0
''', [])

add('p488', r'''
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
''', [('V', 'V1', 's', '0', 100), ('R', 'R1', 's', 'n', 50), ('R', 'R2', 'n', '0', 200), ('R', 'R3', 'n', 'a', 60),
      ('R', 'R4', 'a', 'k', 40), ('E', 'E1', '0', 'k', {'n': 1, 'a': -1}, 0)])

add('ap421', r'''
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
''', [('V', 'V1', 's', '0', 100), ('R', 'R1', 's', 'c', 4), ('R', 'R2', 'c', 'a', 4), ('R', 'R3', 'c', 'd', 4),
      ('V', 'V2', 'd', '0', 20), ('E', 'E1', 't', 's', {'c': 1, 'd': -1}, 0), ('R', 'R4', 't', 'a', 4)])

# Topic 3: superposition
add('lecsup', r'''
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
''', [('V', 'V1', 's', '0', 120), ('R', 'R1', 's', 'n1', 6), ('R', 'R3', 'n1', '0', 3), ('R', 'R2', 'n1', 'n2', 2),
      ('R', 'R4', 'n2', '0', 4), ('I', 'I1', 'n2', '0', 12)])

add('lecsupd', r'''
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
''', [('V', 'V1', 's', '0', 10), ('R', 'R1', 's', 'a', 5), ('R', 'R2', 'a', '0', 20),
      ('G', 'G1', 'd', 'a', {'d': 0.4, 'c': -0.4}), ('R', 'R3', 'd', 'c', 10),
      ('E', 'E1', 'c', '0', {'s': 2 / 5, 'a': -2 / 5}, 0), ('I', 'I1', 'c', 'd', 5)])

add('p494', r'''
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
''', [('I', 'I1', '0', 'p', 6), ('R', 'R1', 'p', '0', 20), ('R', 'R2', 'p', 'q', 1), ('I', 'I2', 'q', '0', 10),
      ('R', 'R3', 'q', '0', 60), ('R', 'R4', 'q', 'k', 5), ('V', 'V1', 'k', '0', 75), ('R', 'R5', 'q', '0', 30)])

add('p496', r'''
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
''', [('V', 'V1', 'a', '0', 8), ('R', 'R1', 'a', '0', 5000), ('R', 'R2', 'a', 'b', 2000), ('R', 'R3', 'b', '0', 6000),
      ('I', 'I1', '0', 'b', 0.010), ('I', 'I2', 'b', 'a', 0.005)])

# Practice
add('ap416', r'''
V1 0,3 -> 0,0 "$72\,\mathrm{V}$"
R1 0,3 -> 3,3 "$5\,\Omega$"
R2 3,3 -> 3,0 "$20\,\Omega$"
R3 3,3 -> 6,3 "$8\,\Omega$"
wire 0,3 -> 0,6 -> 2,6
R4 2,6 -> 5,6 "$12\,\Omega$"
wire 5,6 -> 6,6 -> 6,3
wire 6,3 -> 8,3
wire 0,0 -> 8,0
terminal 8,3 "$a$" right
terminal 8,0 "$b$" right
label 3,3 "$v_1$" below
ground 0,0
''', [('V', 'V1', 's', '0', 72), ('R', 'R1', 's', 'n', 5), ('R', 'R2', 'n', '0', 20), ('R', 'R3', 'n', 'a', 8),
      ('R', 'R4', 's', 'a', 12)])

add('p493', r'''
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
''', [('V', 'V1', 'p', '0', 45), ('R', 'R1', 'p', 'm', 5), ('R', 'R2', 'm', 'n', 10), ('V', 'V2', 'n', 'r', 10),
      ('R', 'R3', 'm', 'k', 40), ('R', 'R4', '0', 'k', 15), ('R', 'R5', 'k', 'r', 30), ('I', 'I1', 'r', '0', 8)])

# Week 5 start here: V_Th 18 V, R_Th 3 ohm, I_N 6 A
add('w5S', r'''
V1 0,3 -> 0,0 "$24\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
R2 3,3 -> 3,0 "$12\,\Omega$"
wire 3,3 -> 6,3
wire 3,0 -> 6,0
terminal 6,3 "$a$" right
terminal 6,0 "$b$" right
wire 0,0 -> 3,0
ground 0,0
''', [('V', 'V1', 's', '0', 24), ('R', 'R1', 's', 'a', 4), ('R', 'R2', 'a', '0', 12)])

# Week 5 summary visuals
add('w5A', r'''
R1 0,3 -> 0,0 "$6\,\Omega$" v="$v$"
wire 0,3 -> 3,3
G1 3,3 -> 3,0 "$\tfrac{v}{3}$"
wire 0,0 -> 3,0
wire 3,3 -> 5,3
wire 3,0 -> 5,0
terminal 5,3 "$a$" right
terminal 5,0 "$b$" right
ground 0,0
''', [('R', 'R1', 'a', '0', 6), ('G', 'G1', 'a', '0', {'a': 1 / 3})])

add('w5B', r'''
V1 0,3 -> 0,0 "$V_{\mathrm{Th}}=20\,\mathrm{V}$"
R1 0,3 -> 3,3 "$R_{\mathrm{Th}}=5\,\Omega$"
wire 3,3 -> 5,3
RL 5,3 -> 5,0 "$R_L$" flip
wire 5,0 -> 0,0
terminal 3,3 "$a$" above
ground 0,0
''', [('V', 'V1', 't', '0', 20), ('R', 'R1', 't', 'a', 5), ('R', 'RL', 'a', '0', 5)])

add('w5C', r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$" flip
wire 3,3 -> 6,3
I1 6,0 -> 6,3 "$2\,\mathrm{A}$" flip
wire 6,0 -> 0,0
label 3,3 "$m$" above
ground 0,0
''', [('V', 'V1', 't', '0', 12), ('R', 'R1', 't', 'm', 4), ('R', 'R2', 'm', '0', 4), ('I', 'I1', '0', 'm', 2)])
