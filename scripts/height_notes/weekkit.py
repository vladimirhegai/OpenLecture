"""Shared pieces of the v3 week layout: the height-method card at the top of every week."""


def card(D, this_week, new_rule):
    """Top of a week: one-line 'this week', the height method in a table, the two laws, and what is new this week."""
    CO = D.CO
    CO('info', this_week)
    D.H(1, 'The height method (read this first)')
    D.T(['Part', 'In the height picture', 'Rule'], [
        ['Ground', 'the floor, $0\\,\\mathrm{V}$', 'Pick one wire. The lowest one keeps the picture tidy.'],
        ['Wire (node)', 'one flat level', 'Every point on a wire is at the same height. Its voltage **is** its height.'],
        ['Battery (voltage source)', 'a fixed staircase', 'Its $+$ end is exactly $V$ higher than its $-$ end. Any current can flow.'],
        ['Pump (current source)', 'a lift with a fixed flow', 'It forces its current. How far it lifts is whatever the circuit needs.'],
        ['Resistor', 'a slide', 'Current slides **downhill**. Current $=\\dfrac{\\text{fall}}{R}$, fall $=$ current $\\times R$.'],
        ['Diamond (dependent source)', 'a battery or pump whose size is set elsewhere', 'Find the thing it depends on first, then treat it like a normal source.'],
    ])
    CO('tip', '**Two laws and one power rule.** At every wire: **current in = current out**. Around any loop: **total climbs = total falls** '
              '(you end at the height you started). Power = current $\\times$ height change: climbing **gives** energy (green ▲), '
              'falling **uses** it (orange ▼).')
    CO('info', '**The recipe (every example uses it).** ① Ground the lowest wire. ② Place the heights the batteries fix. '
                  '③ Give each unknown height a letter and write **in = out** there. ④ Solve. '
                  '⑤ Currents $=$ fall $\\div R$. ⑥ Power: climbs = falls.' + ('\n\n**New this week:** ' + new_rule if new_rule else ''))
