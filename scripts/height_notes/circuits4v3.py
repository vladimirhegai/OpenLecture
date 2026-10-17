"""New Week 4 circuits for the v3 rewrite; merged into circuits45.C on import."""
from circuits45 import C, add

add('swap2', r'''
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
''', [('I', 'I1', '0', 'p', 2), ('R', 'R1', 'p', '0', 6), ('R', 'R2', 'p', 'q', 4), ('R', 'R3', 'q', 't', 2),
      ('V', 'V1', 't', '0', 24)])


def p458_net(vdc):
    return [('V', 'V1', 'a', 'l', 230), ('R', 'R1', 'a', 'm', 5), ('R', 'R2', 'm', 'b', 15), ('R', 'R3', 'a', 'b', 30),
            ('R', 'R4', 'm', 'k', 10), ('V', 'V2', 'k', '0', 115), ('V', 'V3', 'b', 'r', vdc), ('R', 'R5', 'l', '0', 20),
            ('R', 'R6', '0', 'r', 25)]


add('p458', r'''
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
''', p458_net(0))

add('p461', r'''
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
''', [('V', 'V1', 'l', 's', 100), ('R', 'R1', 's', 'p', 20e3), ('R', 'R2', 'p', 'l', 80e3), ('R', 'R3', 'p', 'q', 3e3),
      ('I', 'I1', '0', 'q', 12e-3), ('R', 'R4', 'q', '0', 60e3), ('R', 'R5', 'q', 'r', 5e3), ('R', 'R6', 'r', '0', 10e3),
      ('R', 'R7', 'l', '0', 1e3)])

add('p462', r'''
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
''', [('I', 'I1', 'a', '0', 2.5e-3), ('R', 'R1', 'a', '0', 8e3), ('R', 'R2', 'a', 'b', 24e3), ('R', 'R3', 'b', '0', 80e3),
      ('R', 'R4', 'b', 'c', 15e3), ('V', 'V1', 'c', 'd', 40), ('R', 'R5', 'd', '0', 5e3), ('I', 'I2', '0', 'd', 12e-3)])

add('p466', r'''
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
''', [('V', 'V1', 's', '0', 72), ('R', 'R1', 's', 'm', 5), ('R', 'R2', 'm', 'a', 8), ('R', 'R3', 'm', '0', 20),
      ('R', 'R4', 's', 'a', 12)])

add('p467', r'''
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
''', [('I', 'I1', '0', 'n', 0.01), ('R', 'R1', 'n', '0', 10e3), ('V', 'V1', 'n', '0', 30), ('R', 'R2', 'n', 'a', 15e3),
      ('I', 'I2', 'a', '0', 3e-3), ('R', 'R3', 'a', '0', 5e3)])

add('p470', r'''
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
''', [('V', 'V1', 's', '0', 120), ('R', 'R1', 's', 'l', 900), ('R', 'R2', 'l', '0', 600), ('R', 'R3', 's', 'r', 1204),
      ('R', 'R4', 'r', '0', 800), ('R', 'RG', 'l', 'r', 30)])

add('p477', r'''
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
''', [('V', 'V1', 's', '0', 17.4), ('R', 'R1', 's', 'p', 40), ('R', 'R2', 'p', '0', 15), ('I', 'I1', 'p', 'a', 0.1),
      ('R', 'R3', 's', 'a', 26), ('R', 'R4', 'a', 'b', 10), ('R', 'R5', '0', 'b', 4)])


def p456_net(idc):
    return [('V', 'V1', 's', '0', 420), ('R', 'R1', 's', 'p', 7.2), ('R', 'R2', 'p', '0', 20), ('R', 'R3', 'p', 'q', 15),
            ('I', 'I1', 'q', 'p', 15), ('R', 'R4', 'q', 'm', 50), ('I', 'I2', 'q', 'm', idc), ('R', 'R5', '0', 'm', 40)]


add('p456', r'''
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
''', p456_net(0))
