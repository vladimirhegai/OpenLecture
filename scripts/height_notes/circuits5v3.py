"""New Week 5 circuits for the v3 rewrite; merged into circuits45.C on import."""
from circuits45 import C, add

add('p474', r'''
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
''', [('R', 'R1', 'n', '0', 60), ('I', 'I1', '0', 'n', 4), ('R', 'R2', 'n', 'm', 20), ('E', 'E1', 'm', 'a', {'a': 4}, 0),
      ('R', 'R3', 'a', '0', 80), ('R', 'R4', 'a', '0', 40)])

add('p481', r'''
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
''', [('R', 'R1', 't', '0', 50), ('R', 'R2', 't', 'k', 5), ('E', 'E1', '0', 'k', {'m': 6.5 / 25}, 0), ('R', 'R3', 't', 'm', 10),
      ('R', 'R4', 'm', '0', 25), ('R', 'R5', 'm', 'a', 12)])

add('p483', r'''
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
''', [('V', 'V1', 's', '0', 24), ('R', 'R1', 's', 'a', 2), ('G', 'G1', 'a', 's', {'a': 3 / 8}),
      ('I', 'I1', 'a', '0', 4), ('R', 'R2', 'a', '0', 8)])

add('p487', r'''
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
''', [('V', 'V1', 's', '0', 100), ('R', 'R1', 's', 'p', 2), ('R', 'R2', 'p', 'k', 5), ('E', 'E1', 'k', '0', {'s': 6.5, 'p': -6.5}, 0),
      ('R', 'R3', 'p', 'q', 4), ('G', 'G1', '0', 'q', {'p': 1, 'q': -1})])

add('p495', r'''
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
''', [('V', 'V1', 's', '0', 180), ('R', 'R1', 's', 'p', 30), ('R', 'R2', 'p', '0', 60), ('I', 'I1', 'q', 'p', 7.5),
      ('R', 'R3', 'q', '0', 80), ('R', 'R4', 'q', 'r', 20), ('R', 'R5', 'r', '0', 25), ('R', 'R6', 's', 'r', 40)])

add('p498', r'''
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
''', [('V', 'V1', 's', '0', 25), ('R', 'R1', 'n', 's', 4000), ('I', 'I1', 'n', '0', 5e-3), ('R', 'R2', 'n', '0', 20e3),
      ('G', 'G1', 's', 'n', {'n': 2.2 / 4000, 's': -2.2 / 4000})])
