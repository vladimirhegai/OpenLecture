"""Topic D opening: the circuit facts and the switching recipe shared by D1 (first order) and D2 (RLC).

Layout (REWRITE_PLAN.md). Every circuit solution in D1, D2 and Topic E uses the recipe's step words:
Before, Carry across, After, then Plug in (D1) or Pick + Plug in (D2), Check.
"""
import sympy as sp

from midlib import CARD, TAGS, link, t, zero


def build(D):
    D.H('Topic D: Circuits → ODE → solution', cites=D.cite('W2', 1, 2) + D.cite('W1', 6))
    TAGS(D, (2, 3), (5, 3))
    D.P(r'**Use this when** a switch flips at $t=0$ and you need $v(t)$ or $i(t)$ after it.')
    D.P(r'**The move: solve for the thing that can’t jump**, $v_C$ (capacitor voltage) or $i_L$ (inductor current).')
    D.L([r'Its **starting value** comes from the circuit **before** the switch.',
         r'Its **ODE** comes from the circuit **after** the switch (KVL or KCL).',
         r'Then solve the ODE with ' + link('Topic B', 'topic-b') + r'. Get anything else ($i_C$, $v_R$, …) from it at the end.'])

    D.P('**The three rules, one per element:**')
    D.T(['Element', 'Law', 'After a long time', 'At the switch'], [
        ['Capacitor $C$', r'$i=C\dfrac{dv}{dt}$', r'a **gap**', r'$v_C$ **can’t jump**'],
        ['Inductor $L$', r'$v=L\dfrac{di}{dt}$', r'a **wire**', r'$i_L$ **can’t jump**'],
        ['Resistor $R$', r'$v=iR$', '—', 'can jump'],
    ], cites=D.cite('W2', 1, 2))
    CARD(D, r'After a long time: $\;C$ = gap, $\;L$ = wire',
         [(r'Nothing changes any more, so every $\frac{d}{dt}$ is $0$.', (r'i_C=C\cdot0=0\quad\text{(gap)}', r'v_L=L\cdot0=0\quad\text{(wire)}')),
          (r'Example: $12\,\mathrm{V}$ source, a resistor and a capacitor in one loop, left alone. No current flows, so the resistor has $0\,\mathrm{V}$:',
           r'v_C=12\,\mathrm{V}')])
    CARD(D, r'At the switch: $\;v_C(0^+)=v_C(0^-)$, $\;i_L(0^+)=i_L(0^-)$',
         [(r'$0^-$ = just before, $0^+$ = just after. The value carries straight across.', r'v_C(0^-)=12\,\mathrm{V}\quad\Longrightarrow\quad v_C(0^+)=12\,\mathrm{V}'),
          (r'So for that instant a capacitor acts like a **battery** of its old voltage, and an inductor like a **current source** of its old current.',
           r'C\ \to\ \text{voltage source }V_0,\qquad L\ \to\ \text{current source }I_0')])
    D.P('**Steps** (every circuit problem, D1 and D2):')
    D.L([r'**Before** ($t<0$): the old circuit, sitting for a long time. $C$ = gap, $L$ = wire. Find $v_C(0^-)$ or $i_L(0^-)$.',
         r'**Carry across** to $t=0^+$: $v_C(0^+)=v_C(0^-)$, $i_L(0^+)=i_L(0^-)$. Need another value at $0^+$? Redraw the **new** circuit with $C$ as a battery (or $L$ as a current source) and use KVL/KCL.',
         r'**After** ($t>0$): in the new circuit, find what you need: the final value and $\tau$ (' + link('D1', 'd1') + r'), or $\alpha$ and $\omega_0$ (' + link('D2', 'd2') + ').',
         r'**Plug in** to the formula (' + link('D1', 'd1') + r'), or **pick** the case and **plug in** the starting values (' + link('D2', 'd2') + ').',
         r'**Check** $t\to\infty$: $C$ = gap, $L$ = wire again. Your answer must head there.'], ordered=True)
    D.P(r'**Short example:** a $V_s$, $R$, $C$ loop. KVL after the switch, with $i=C\frac{dv_C}{dt}$:')
    D.EQ(r'V_s=Ri+v_C\quad\Longrightarrow\quad RC\,\dfrac{dv_C}{dt}+v_C=V_s')
    D.P(r'One $C$ or one $L$ → first order → ' + link('D1', 'd1') + r'. An $L$ **and** a $C$ → second order → ' + link('D2', 'd2') + '.')
    D.CO('warning', r'**Before and after are two different circuits.** Draw both. The old one is only for the starting value. '
         r'Write the ODE from the new one, with only the parts still connected.')
    D.CO('warning', r'**The sign comes from the drawn arrow.** Find which way the current really flows, then compare with the arrow. '
         r'Opposite? The value is **negative**. Example: $3\,\mathrm{A}$ really flows down, the $i_L$ arrow points up → $i_L(0)=-3\,\mathrm{A}$.')


def verify():
    zero(sp.diff(1 - sp.exp(-t), t) - sp.exp(-t))
