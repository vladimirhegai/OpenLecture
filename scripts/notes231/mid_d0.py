"""Topic D opening: the circuit facts and the switching recipe shared by D1 (first order) and D2 (RLC)."""
import sympy as sp

from midlib import TAGS, link, t, zero


def build(D):
    D.H('Topic D: Circuits → ODE → solution', cites=D.cite('W2', 1, 2) + D.cite('W1', 6))
    TAGS(D, (2, 3), (5, 3))
    D.P(r'**What does a circuit question want?** Always the same thing: a switch flips at $t=0$, and you need $v(t)$ or $i(t)$ after it.')
    D.P('The circuit gives you two things:')
    D.L([r'**the ODE**: write KVL or KCL for the circuit **after** the switch;',
         r'**the starting value**: read it off the circuit **before** the switch.'])
    D.P('Then you solve that ODE with ' + link('Topic B', 'topic-b') + ', like any other ODE.')

    D.P('**The three rules you need, one per element:**')
    D.T(['Element', 'Law', 'After a long time (DC)', 'When the switch flips'], [
        ['Capacitor $C$', r'$i=C\dfrac{dv}{dt}$', r'a **gap** (open circuit)', r'$v_C$ **can’t jump**'],
        ['Inductor $L$', r'$v=L\dfrac{di}{dt}$', r'a **wire** (short circuit)', r'$i_L$ **can’t jump**'],
        ['Resistor $R$', r'$v=iR$', '—', 'its $v$ and $i$ **can** jump'],
    ], cites=D.cite('W2', 1, 2))
    D.P(r'**After a long time** (called **DC steady state**): nothing changes any more, so every $\frac{d}{dt}$ is 0.')
    D.L([r'**Capacitor:** $i=C\cdot0=0$. No current gets through, so it acts like a gap.',
         r'**Inductor:** $v=L\cdot0=0$. No voltage across it, so it acts like a plain wire.'])
    D.P(r'Example: a $12\,\mathrm{V}$ source, a resistor and a capacitor in one loop, left alone for a long time. '
        r'No current flows, so the resistor has 0 V and the capacitor holds all $12\,\mathrm{V}$.')
    D.P(r'**When the switch flips:** $0^-$ = just before, $0^+$ = just after. “Can’t jump” means:')
    D.EQ(r'v_C(0^+)=v_C(0^-),\qquad i_L(0^+)=i_L(0^-)')
    D.P(r'Example: if the capacitor holds $12\,\mathrm{V}$ just before the switch flips, it still holds $12\,\mathrm{V}$ just after. '
        r'Why: a jump would need an infinite current (see the Bonus at the end of this section).')
    D.P(r'**So which quantity do you solve for?** The one that can’t jump ($v_C$ or $i_L$), because its starting value carries straight across the switch. '
        r'Get the rest from it afterwards, e.g. $i_C=C\frac{dv_C}{dt}$.')

    D.P('**What each element looks like at the three moments you need:**')
    D.T(['', r'$t=0^-$ (old DC state)', r'$t=0^+$ (just after)', r'$t\to\infty$ (new DC state)'], [
        ['Capacitor', r'gap, holding $V_0$', r'a **voltage source** $V_0$', 'gap again'],
        ['Inductor', r'wire, carrying $I_0$', r'a **current source** $I_0$', 'wire again'],
        ['Resistor', 'Ohm’s law', 'Ohm’s law (may jump)', 'Ohm’s law'],
    ])
    D.L([r'**Capacitor at $0^+$:** it still holds its old voltage $V_0$, so for that instant it acts like a battery. Example: charged to $12\,\mathrm{V}$ → a $12\,\mathrm{V}$ source.',
         r'**Inductor at $0^+$:** it keeps pushing its old current $I_0$, so it acts like a current source. Example: carrying $4\,\mathrm{A}$ → a $4\,\mathrm{A}$ source.'])
    D.GRAPH(r'''
    title "A capacitor charging from $0\,\mathrm{V}$: its voltage doesn’t jump, its current does"
    x -1 5 label="$t/\tau$"
    y -0.2 1.2 label="scaled so the biggest value is 1"
    curve "if(x<0, 0, 1-exp(-x))" label="$v_C$: starts at 0, no jump" color=1
    curve "if(x<0, 0, exp(-x))" label="$i_C$: 0 before, jumps at $t=0$" color=2
    vline "0" label="switch closes" color=0
    caption "This is Pre-tutorial 2 (a problem in D1). Before the switch closes, no current goes into the capacitor. Just after, $v_C$ is still 0, so the resistor beside it gets no current and all of the source current goes into the capacitor. $i_C$ jumps; $v_C$ doesn’t."
    ''')

    D.P('**The switching recipe.** Every circuit problem, in five steps:')
    D.L([r'**Before ($t<0$):** the switch sat in its old spot for a long time, so use the DC rules: $C$ = gap, $L$ = wire. Find $v_C(0^-)$ or $i_L(0^-)$. '
         r'Example: a capacitor that sat across a $12\,\mathrm{V}$ source → $v_C(0^-)=12\,\mathrm{V}$.',
         r'**Just after ($t=0^+$):** carry the value across: $v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$. '
         r'Need something else at $0^+$, like a resistor current? Draw the **new** circuit with $C$ as a voltage source $v_C(0^+)$ (or $L$ as a current source $i_L(0^+)$), then use KVL/KCL.',
         r'**After ($t>0$):** in the new circuit, write KVL around a loop or KCL at a node. Swap $i_C$ for $C\frac{dv}{dt}$ and $v_L$ for $L\frac{di}{dt}$. That’s the ODE. '
         r'Example: a loop of $V_s$, $R$, $C$: $\;V_s=Ri+v_C$ with $i=C\frac{dv_C}{dt}$, so $RC\frac{dv_C}{dt}+v_C=V_s$.',
         r'**Solve:** one $L$ or one $C$ → first order → the ' + link('D1', 'd1') + ' formula (it’s a ' + link('B2', 'b2') + ' equation). '
         r'An $L$ and a $C$ → second order → ' + link('D2', 'd2') + ' (solved with ' + link('B5', 'b5') + ' or ' + link('B6', 'b6') + '). '
         'Your values from step 2 are the starting conditions.',
         r'**Check ($t\to\infty$):** use the DC rules again ($C$ = gap, $L$ = wire). Your answer must head to this final value. '
         r'Example: in the $V_s$, $R$, $C$ loop, no current flows in the end, so $v_C\to V_s$.'],
        ordered=True)
    D.CO('warning', r'**Before and after are two different circuits.** Draw both. Use the old one only for the starting value (step 1). '
         r'Write the ODE (step 3) from the new one, with only the parts still connected.')
    D.CO('warning', r'**The sign comes from the drawn arrow.** First find which way the current really flows, then compare with the arrow. '
         r'If they point opposite ways, the value is **negative**. Example: $3\,\mathrm{A}$ really flows down, the $i_L$ arrow points up → $i_L(0)=-3\,\mathrm{A}$.')
    D.CO('info', r'**Bonus (skip-safe): why $v_C$ and $i_L$ can’t jump.** If $v_C$ jumped, its slope $\frac{dv}{dt}$ would be infinite at that instant. '
         r'Then $i=C\frac{dv}{dt}$ would be an infinite current, and no real circuit can supply that. '
         r'Same for an inductor: a jump in $i_L$ would need an infinite voltage $v=L\frac{di}{dt}$. '
         r'Another way to see it: the stored energy, $\frac12Cv^2$ or $\frac12Li^2$, can’t change in zero time.')


def verify():
    zero(sp.diff(1 - sp.exp(-t), t) - sp.exp(-t))
