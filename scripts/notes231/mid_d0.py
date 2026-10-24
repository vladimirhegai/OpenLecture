"""Topic D opening: the circuit facts and the switching recipe shared by D1 (first order) and D2 (RLC)."""
import sympy as sp

from midlib import TAGS, link, t, zero


def build(D):
    D.H('Topic D: Circuits → ODE → solution', cites=D.cite('W2', 1, 2) + D.cite('W1', 6))
    TAGS(D, (2, 3), (5, 3))
    D.P(r'Every circuit question in this course is the same job: a switch moves (or a source changes) at $t=0$, and you need $v(t)$ or $i(t)$ afterwards.')
    D.P('The circuit hands you two things:')
    D.L([r'**the ODE**, from KVL or KCL after the switch;',
         r'**the starting values**, from the circuit before the switch.'])
    D.P('Then Topic B solves the ODE, exactly as before.')

    D.P('**The element facts.** Everything in this topic comes from these three rows:')
    D.T(['Element', 'Law', 'In DC steady state', 'At the switching instant'], [
        ['Capacitor $C$', r'$i=C\dfrac{dv}{dt}$', r'**open circuit** ($i=0$)', r'$v_C$ **cannot jump**: $v_C(0^+)=v_C(0^-)$'],
        ['Inductor $L$', r'$v=L\dfrac{di}{dt}$', r'**short circuit** ($v=0$)', r'$i_L$ **cannot jump**: $i_L(0^+)=i_L(0^-)$'],
        ['Resistor $R$', r'$v=iR$', '—', 'its current and voltage **can** jump'],
    ], cites=D.cite('W2', 1, 2))
    D.L([r'**DC steady state** = “the switch has been there **for a long time**”: nothing changes any more, so every $\frac{d}{dt}$ is 0.',
         r'$0^-$ = just before the switch moves; $0^+$ = just after.'])
    D.P(r'So always solve for the quantity that **can’t jump**: $v_C$ in a capacitor circuit, $i_L$ in an inductor circuit. '
        r'Get everything else (resistor currents, $i_C$, $v_L$) from it afterwards.')

    D.P('**What each element looks like at the three moments you need:**')
    D.T(['', r'$t=0^-$ (old DC state)', r'$t=0^+$ (just after)', r'$t\to\infty$ (new DC state)'], [
        ['Capacitor', r'open circuit, holding $V_0$', r'a **voltage source** $V_0$', 'open circuit again'],
        ['Inductor', r'short circuit, carrying $I_0$', r'a **current source** $I_0$', 'short circuit again'],
        ['Resistor', 'Ohm’s law', 'Ohm’s law (may jump)', 'Ohm’s law'],
    ])
    D.GRAPH(r'''
    title "A capacitor charging from $0\,\mathrm{V}$: its voltage is continuous, its current jumps"
    x -1 5 label="$t/\tau$"
    y -0.2 1.2 label="fraction of final value"
    curve "if(x<0, 0, 1-exp(-x))" label="$v_C$: starts at 0, no jump" color=1
    curve "if(x<0, 0, exp(-x))" label="$i_C$: 0 before, jumps at $t=0$" color=2
    vline "0" label="switch closes" color=0
    caption "Pre-tutorial 2 in picture form. Before the switch closes no current flows. Just after, $v_C$ is still 0, so all of the source current goes into the capacitor: $i_C$ jumps, $v_C$ doesn’t."
    ''')

    D.P('**The switching recipe** (every circuit problem):')
    D.L([r'**Before ($t<0$):** the switch has been in its old position for a long time, so the circuit is in DC steady state. '
         r'Replace $C$ by an open circuit and $L$ by a short. Find $v_C(0^-)$ or $i_L(0^-)$.',
         r'**Just after ($t=0^+$):** carry them over: $v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$. To find anything else at $0^+$, '
         r'redraw the **new** circuit with $C$ as a voltage source $v_C(0^+)$ and $L$ as a current source $i_L(0^+)$, then use KVL/KCL.',
         r'**After ($t>0$):** in the new circuit, write KCL at a node or KVL around the loop. Replace $i_C$ by $C\frac{dv}{dt}$ and $v_L$ by $L\frac{di}{dt}$. That is the ODE.',
         r'**Solve:** one $L$ or $C$ → first order → ' + link('B2', 'b2') + ' (or the ' + link('D1', 'd1') + ' formula). '
         r'An $L$ and a $C$ → second order → ' + link('B5', 'b5') + ' (no source) or ' + link('B6', 'b6') + ' (constant source), see ' + link('D2', 'd2') + '. '
         'The values from step 2 are the conditions.',
         r'**Check ($t\to\infty$):** DC steady state again ($C$ open, $L$ short). Your answer must approach this final value.'],
        ordered=True)
    D.CO('warning', r'**Before and after are two different circuits.** Draw both. Use the old one only for step 1; write the ODE (step 3) from the new one, '
         r'with only the parts still connected.')
    D.CO('warning', r'**Signs come from the drawn arrow.** If the reference arrow for $i_L$ points against the real current, the starting value is **negative**. '
         r'Find the real direction first, then compare it with the arrow.')
    D.CO('info', r'**Bonus (skip-safe): why $v_C$ and $i_L$ can’t jump.** If $v_C$ jumped, $\frac{dv}{dt}$ would be infinite, so $i=C\frac{dv}{dt}$ would be infinite: '
         r'no real circuit supplies that. The same with $v=L\frac{di}{dt}$ for an inductor current. The stored energy $\frac12Cv^2$ or $\frac12Li^2$ cannot change instantly.')


def verify():
    zero(sp.diff(1 - sp.exp(-t), t) - sp.exp(-t))
