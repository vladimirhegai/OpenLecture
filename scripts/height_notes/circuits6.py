"""Week 6 circuits: drawings plus one netlist per snapshot.

Snapshot rules (the height method for C and L):
  DC settled: a capacitor is a gap ('I', name, a, b, 0); an inductor is a wire ('V', name, a, b, 0).
  Just after switching: a capacitor holds its voltage ('V', name, +, -, v_C); an inductor holds its current
  ('I', name, a, b, i_L) with i_L measured a->b.
Switches: closed = ('V', S, a, b, 0); open = ('I', S, a, b, 0).
"""
from circuits45 import C, add

# ---------------------------------------------------------------- Topic 1: settled circuits
add('dc1', r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
L1 3,3 -> 6,3 "$0.5\,\mathrm{H}$" i="$i_L$"
R2 6,3 -> 6,0 "$4\,\Omega$"
wire 6,3 -> 9,3
C1 9,3 -> 9,0 "$100\,\mu\mathrm{F}$" v="$v_C$"
wire 0,0 -> 9,0
label 3,3 "$a$" above
label 6,3 "$b$" above
ground 0,0
''', [('V', 'V1', 's', '0', 12), ('R', 'R1', 's', 'a', 2), ('V', 'L1', 'a', 'b', 0), ('R', 'R2', 'b', '0', 4),
      ('I', 'C1', 'b', '0', 0)])

add('dc2', r'''
I1 0,0 -> 0,3 "$5\,\mathrm{A}$"
wire 0,3 -> 6,3
C1 2,3 -> 2,0 "$10\,\mu\mathrm{F}$" v="$v_C$"
R1 4,3 -> 4,0 "$4\,\Omega$"
L1 6,3 -> 9,3 "$2\,\mathrm{mH}$" i="$i_L$"
R2 9,3 -> 9,0 "$6\,\Omega$"
wire 0,0 -> 9,0
label 4,3 "$a$" above
label 9,3 "$b$" above
ground 0,0
''', [('I', 'I1', '0', 'a', 5), ('I', 'C1', 'a', '0', 0), ('R', 'R1', 'a', '0', 4), ('V', 'L1', 'a', 'b', 0),
      ('R', 'R2', 'b', '0', 6)])

# ---------------------------------------------------------------- Topic 2: switching
add('rc1', r'''
V1 0,3 -> 0,0 "$10\,\mathrm{V}$"
S1 0,3 -> 3,3 "$t=0$" action=close
R1 3,3 -> 6,3 "$2\,\mathrm{k\Omega}$"
C1 6,3 -> 6,0 "$1\,\mu\mathrm{F}$" v="$v_C$"
wire 6,0 -> 0,0
label 6,3 "$n$" right
ground 0,0
''', [('V', 'V1', 's', '0', 10), ('I', 'S1', 's', 'p', 0), ('R', 'R1', 'p', 'n', 2000), ('I', 'C1', 'n', '0', 0)])


def rc1(vc):
    """Switch closed, capacitor holding vc."""
    return [('V', 'V1', 's', '0', 10), ('V', 'S1', 's', 'p', 0), ('R', 'R1', 'p', 'n', 2000), ('V', 'C1', 'n', '0', vc)]


add('lecrl', r'''
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
label 6,3 "$x$" above
ground 0,0
''', [('V', 'V1', 's', '0', 24), ('R', 'R1', 's', 'b', 2), ('I', 'S1', 'b', 'x', 0), ('V', 'S2', 'a', 'x', 0),
      ('V', 'L1', 'x', '0', 0), ('R', 'R2', 'a', '0', 10), ('I', 'I1', 'a', '0', 8)])


def lecrl(iL):
    """After switching (left loop only): inductor holds iL (x -> ground)."""
    return [('V', 'V1', 's', '0', 24), ('R', 'R1', 's', 'b', 2), ('V', 'S1', 'b', 'x', 0), ('I', 'L1', 'x', '0', iL)]


add('p71', r'''
V1 0,3 -> 0,0 "$120\,\mathrm{V}$"
R1 0,3 -> 3,3 "$3\,\Omega$"
R2 3,3 -> 3,0 "$30\,\Omega$"
R3 3,3 -> 6,3 "$6\,\Omega$"
S1 6,3 -> 9,3 "$t=0$" state=closed action=open
L1 9,0 -> 9,3 "$8\,\mathrm{mH}$" i="$i$"
wire 9,3 -> 12,3
R4 12,3 -> 12,0 "$2\,\Omega$"
wire 0,0 -> 3,0 -> 9,0 -> 12,0
label 3,3 "$p$" above
label 9,3 "$r$" above
ground 0,0
''', [('V', 'V1', 's', '0', 120), ('R', 'R1', 's', 'p', 3), ('R', 'R2', 'p', '0', 30), ('R', 'R3', 'p', 'q', 6),
      ('V', 'S1', 'q', 'r', 0), ('V', 'L1', '0', 'r', 0), ('R', 'R4', 'r', '0', 2)])


def p71(iL):
    """After the switch opens: only the inductor and the 2 ohm (inductor current iL measured upward, ground -> r)."""
    return [('I', 'L1', '0', 'r', iL), ('R', 'R4', 'r', '0', 2)]


add('p722', r'''
I1 0,0 -> 0,3 "$7.5\,\mathrm{mA}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$80\,\mathrm{k\Omega}$"
R2 3,3 -> 6,3 "$20\,\mathrm{k\Omega}$"
S1 6,3 -> 9,3 "$t=0$" state=closed action=open
C1 9,3 -> 9,0 "$0.4\,\mu\mathrm{F}$" v="$v(t)$"
wire 9,3 -> 12,3
R3 12,3 -> 12,0 "$50\,\mathrm{k\Omega}$"
wire 0,0 -> 3,0 -> 9,0 -> 12,0
label 3,3 "$p$" above
label 9,3 "$r$" above
ground 0,0
''', [('I', 'I1', '0', 'p', 7.5e-3), ('R', 'R1', 'p', '0', 80e3), ('R', 'R2', 'p', 'q', 20e3), ('V', 'S1', 'q', 'r', 0),
      ('I', 'C1', 'r', '0', 0), ('R', 'R3', 'r', '0', 50e3)])


def p722(vc):
    return [('V', 'C1', 'r', '0', vc), ('R', 'R3', 'r', '0', 50e3)]


add('p723', r'''
V1 0,3 -> 0,0 "$60\,\mathrm{V}$"
R1 0,3 -> 3,3 "$75\,\mathrm{k\Omega}$"
S1 3,3 -> 6,3 "$t=0$" state=closed action=open
C1 6,3 -> 6,0 "$5\,\mathrm{nF}$" v="$v_o$"
wire 6,3 -> 9,3
R2 9,3 -> 9,0 "$25\,\mathrm{k\Omega}$"
wire 0,0 -> 9,0
label 6,3 "$n$" above
ground 0,0
''', [('V', 'V1', 's', '0', 60), ('R', 'R1', 's', 'p', 75e3), ('V', 'S1', 'p', 'n', 0), ('I', 'C1', 'n', '0', 0),
      ('R', 'R2', 'n', '0', 25e3)])


def p723(vc):
    return [('V', 'C1', 'n', '0', vc), ('R', 'R2', 'n', '0', 25e3)]


add('lecrc', r'''
V1 0,3 -> 0,0 "$40\,\mathrm{V}$"
R1 0,3 -> 3,3 "$20\,\mathrm{k\Omega}$"
R2 3,3 -> 3,0 "$60\,\mathrm{k\Omega}$"
S1 3,3 -> 6,3 "$1$" state=closed action=open
C1 6,3 -> 6,0 "$0.25\,\mu\mathrm{F}$" v="$v_C$"
S2 9,3 -> 6,3 "$2$" action=close
R3 12,3 -> 9,3 "$8\,\mathrm{k\Omega}$" i="$i_o$"
R4 12,3 -> 12,0 "$160\,\mathrm{k\Omega}$"
R5 12,3 -> 15,3 "$40\,\mathrm{k\Omega}$"
V2 15,0 -> 15,3 "$75\,\mathrm{V}$"
wire 0,0 -> 3,0 -> 6,0 -> 12,0 -> 15,0
label 12,3 "$c$" above
label 6,3 "$x$" above
label 15,3 "$d$" right
ground 0,0
''', [('V', 'V1', 's', '0', 40), ('R', 'R1', 's', 'p', 20e3), ('R', 'R2', 'p', '0', 60e3), ('V', 'S1', 'p', 'x', 0),
      ('I', 'C1', 'x', '0', 0), ('I', 'S2', 'y', 'x', 0), ('R', 'R3', 'c', 'y', 8e3), ('R', 'R4', 'c', '0', 160e3),
      ('R', 'R5', 'c', 'd', 40e3), ('V', 'V2', '0', 'd', 75)])


def lecrc(vc=None):
    """Position 2 (right part only). vc=None: settled (C a gap); else C holds vc."""
    cap = ('I', 'C1', 'x', '0', 0) if vc is None else ('V', 'C1', 'x', '0', vc)
    return [cap, ('V', 'S2', 'y', 'x', 0), ('R', 'R3', 'c', 'y', 8e3), ('R', 'R4', 'c', '0', 160e3),
            ('R', 'R5', 'c', 'd', 40e3), ('V', 'V2', '0', 'd', 75)]


add('p737', r'''
I1 0,3 -> 0,0 "$40\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$4\,\Omega$"
S1 3,3 -> 6,3 "$a$" state=closed action=open
S2 8,3 -> 6,3 "$b$" action=close
R2 8,3 -> 8,1.5 "$60\,\Omega$"
V1 8,1.5 -> 8,0 "$240\,\mathrm{V}$"
wire 6,3 -> 6,5 -> 11,5 -> 11,3
R3 11,3 -> 11,0 "$20\,\Omega$" v="$v_o$"
R4 11,3 -> 14,3 "$5\,\Omega$" i="$i_o$"
L1 14,3 -> 14,0 "$10\,\mathrm{mH}$"
wire 0,0 -> 14,0
label 11,3 "$x$" above
label 14,3 "$y$" right
ground 0,0
''', [('I', 'I1', 'a', '0', 40), ('R', 'R1', 'a', '0', 4), ('V', 'S1', 'a', 'x', 0), ('I', 'S2', 'b', 'x', 0),
      ('R', 'R2', 'b', 'k', 60), ('V', 'V1', 'k', '0', 240), ('R', 'R3', 'x', '0', 20), ('R', 'R4', 'x', 'y', 5),
      ('V', 'L1', 'y', '0', 0)])


def p737(iL=None):
    """Position b (right part only). iL=None: settled (L a wire); else L holds iL (y -> ground)."""
    ind = ('V', 'L1', 'y', '0', 0) if iL is None else ('I', 'L1', 'y', '0', iL)
    return [('V', 'S2', 'b', 'x', 0), ('R', 'R2', 'b', 'k', 60), ('V', 'V1', 'k', '0', 240), ('R', 'R3', 'x', '0', 20),
            ('R', 'R4', 'x', 'y', 5), ind]
