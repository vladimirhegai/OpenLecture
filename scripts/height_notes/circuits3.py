"""New Week 3 circuits (v3 rewrite). Same tuple format as circuits.py; merged into circuits.C on import."""
from circuits import C, add

# ---- custom ladder examples
add('N1', r'''
I1 0,0 -> 0,3 "$3\,\mathrm{A}$"
wire 0,3 -> 6,3
R1 3,3 -> 3,0 "$4\,\Omega$"
R2 6,3 -> 6,0 "$12\,\Omega$"
wire 0,0 -> 6,0
label 3,3 "$x$" above
ground 0,0
''', [('I', 'I1', '0', 'x', 3), ('R', 'R1', 'x', '0', 4), ('R', 'R2', 'x', '0', 12)])

add('M1', r'''
V1 0,3 -> 0,0 "$12\,\mathrm{V}$"
R1 0,3 -> 3,3 "$2\,\Omega$"
R2 3,3 -> 3,0 "$4\,\Omega$"
wire 3,0 -> 0,0
label 3,3 "$x$" above
ground 0,0
''', [('V', 'V1', 's', '0', 12), ('R', 'R1', 's', 'x', 2), ('R', 'R2', 'x', '0', 4)])

add('M2', r'''
V1 0,3 -> 0,0 "$20\,\mathrm{V}$"
R1 0,3 -> 3,3 "$4\,\Omega$"
R2 3,3 -> 3,0 "$6\,\Omega$"
R3 3,3 -> 6,3 "$3\,\Omega$"
I1 6,3 -> 6,0 "$2\,\mathrm{A}$"
wire 6,0 -> 0,0
label 3,3 "$m$" above
label 6,3 "$r$" above
ground 0,0
''', [('V', 'V1', 's', '0', 20), ('R', 'R1', 's', 'm', 4), ('R', 'R2', 'm', '0', 6), ('R', 'R3', 'm', 'r', 3),
      ('I', 'I1', 'r', '0', 2)])

# ---- textbook, node voltages
add('p46', r'''
I1 0,3 -> 0,0 "$2\,\mathrm{A}$"
wire 0,3 -> 3,3
R1 3,3 -> 3,0 "$4\,\Omega$"
R2 3,3 -> 6,3 "$2\,\Omega$"
V1 6,3 -> 6,0 "$55\,\mathrm{V}$"
R3 3,0 -> 6,0 "$3\,\Omega$"
wire 0,0 -> 3,0
label 3,3 "$a$" above
label 6,0 "$d$" below
ground 0,0
''', [('I', 'I1', 'a', '0', 2), ('R', 'R1', 'a', '0', 4), ('R', 'R2', 'a', 'c', 2), ('V', 'V1', 'c', 'd', 55),
      ('R', 'R3', '0', 'd', 3)])

add('p48', r'''
V1 0,2 -> 0,0 "$180\,\mathrm{V}$"
R1 0,4 -> 0,2 "$12\,\Omega$"
R2 0,4 -> 3,4 "$5\,\Omega$"
R3 3,4 -> 3,0 "$2\,\Omega$" v="$v_o$"
wire 3,4 -> 6,4
I1 6,4 -> 6,0 "$5\,\mathrm{A}$"
wire 0,0 -> 6,0
label 0,4 "$t$" left
ground 0,0
''', [('V', 'V1', 's', '0', 180), ('R', 'R1', 't', 's', 12), ('R', 'R2', 't', 'o', 5), ('R', 'R3', 'o', '0', 2),
      ('I', 'I1', 'o', '0', 5)])

add('p411', r'''
V1 0,3 -> 0,0 "$80\,\mathrm{V}$"
R1 0,3 -> 3,3 "$800\,\Omega$" i="$i_b$"
R2 3,3 -> 6,3 "$500\,\Omega$" i="$i_c$"
R3 6,3 -> 9,3 "$2\,\mathrm{k\Omega}$" i="$i_d$"
wire 3,3 -> 3,5
R4 3,5 -> 9,5 "$1\,\mathrm{k\Omega}$" i="$i_a$"
wire 9,5 -> 9,3
R5 6,3 -> 6,0 "$3\,\mathrm{k\Omega}$" i="$i_e$"
R6 9,3 -> 9,0 "$250\,\Omega$" i="$i_f$"
wire 0,0 -> 9,0
label 3,3 "$p$" below
label 6,3 "$q$" above
label 9,3 "$r$" right
ground 0,0
''', [('V', 'V1', 's', '0', 80), ('R', 'R1', 's', 'p', 800), ('R', 'R2', 'p', 'q', 500), ('R', 'R3', 'q', 'r', 2000),
      ('R', 'R4', 'p', 'r', 1000), ('R', 'R5', 'q', '0', 3000), ('R', 'R6', 'r', '0', 250)])

add('p416', r'''
V1 0,2 -> 0,0 "$v_1$"
R1 0,4 -> 0,2 "$R$"
V2 3,2 -> 3,0 "$v_2$"
R2 3,4 -> 3,2 "$R$"
V3 6,2 -> 6,0 "$v_3$"
R3 6,4 -> 6,2 "$R$"
wire 0,4 -> 8,4
wire 0,0 -> 8,0
terminal 8,4 "$+$" right
terminal 8,0 "$-$" right
label 8,2 "$v_o$" right
ground 0,0
''', [('V', 'V1', 'p1', '0', 150), ('R', 'R1', 'o', 'p1', 10), ('V', 'V2', 'p2', '0', 200), ('R', 'R2', 'o', 'p2', 10),
      ('V', 'V3', 'p3', '0', -50), ('R', 'R3', 'o', 'p3', 10)])

add('p425', r'''
V1 0,3 -> 0,0 "$50\,\mathrm{V}$"
R1 0,3 -> 3,3 "$80\,\Omega$"
R2 3,3 -> 3,0 "$50\,\Omega$"
R3 3,3 -> 6,3 "$40\,\Omega$"
I1 6,0 -> 6,3 "$750\,\mathrm{mA}$"
wire 6,3 -> 9,3
R4 9,3 -> 9,0 "$200\,\Omega$"
wire 0,3 -> 0,5
R5 6,5 -> 0,5 "$800\,\Omega$" v="$v_o$"
wire 6,5 -> 6,3
wire 0,0 -> 9,0
label 3,3 "$m$" below
label 6,3 "$r$" below
ground 0,0
''', [('V', 'V1', 's', '0', 50), ('R', 'R1', 's', 'm', 80), ('R', 'R2', 'm', '0', 50), ('R', 'R3', 'm', 'r', 40),
      ('I', 'I1', '0', 'r', 0.75), ('R', 'R4', 'r', '0', 200), ('R', 'R5', 'r', 's', 800)])

# ---- textbook, mesh currents
add('p436', r'''
V1 0,3 -> 0,0 "$110\,\mathrm{V}$"
R1 0,3 -> 4,3 "$10\,\Omega$"
R2 4,3 -> 8,3 "$12\,\Omega$"
V2 8,3 -> 8,0 "$70\,\mathrm{V}$"
wire 0,3 -> 0,5
R3 0,5 -> 8,5 "$6\,\Omega$"
wire 8,5 -> 8,3
R4 4,3 -> 4,1.8 "$3\,\Omega$"
V3 4,0 -> 4,1.8 "$12\,\mathrm{V}$"
R5 0,0 -> 4,0 "$4\,\Omega$"
R6 4,0 -> 8,0 "$2\,\Omega$"
label 0,3 "$a$" left
label 4,3 "$m$" above
label 8,3 "$b$" right
label 0,0 "$l$" left
label 8,0 "$r$" right
ground 4,0
''', [('V', 'V1', 'a', 'l', 110), ('R', 'R1', 'a', 'm', 10), ('R', 'R2', 'm', 'b', 12), ('V', 'V2', 'b', 'r', 70),
      ('R', 'R3', 'a', 'b', 6), ('R', 'R4', 'm', 'n', 3), ('V', 'V3', '0', 'n', 12), ('R', 'R5', 'l', '0', 4),
      ('R', 'R6', '0', 'r', 2)])

add('p442', r'''
V1 0,3 -> 0,0 "$60\,\mathrm{V}$"
R1 0,3 -> 4,3 "$4\,\Omega$"
R2 4,3 -> 4,0 "$10\,\Omega$" v="$v_\Delta$"
R3 4,3 -> 8,3 "$2.5\,\Omega$"
E1 8,0 -> 8,3 "$\tfrac{v_\Delta}{2}$"
R4 0,0 -> 4,0 "$2\,\Omega$"
R5 4,0 -> 8,0 "$20\,\Omega$"
label 4,3 "$m$" above
label 0,0 "$l$" left
label 8,0 "$r$" right
ground 4,0
''', [('V', 'V1', 's', 'l', 60), ('R', 'R1', 's', 'm', 4), ('R', 'R2', 'm', '0', 10), ('R', 'R3', 'm', 't', 2.5),
      ('E', 'E1', 'r', 't', {'m': 0.5}, 0), ('R', 'R4', 'l', '0', 2), ('R', 'R5', '0', 'r', 20)])
