"""Diagrams for Weeks 2-4 (SVG, served at /figures/elec231/). Each make_wN() returns {name: url}."""
import math

from svgfig import Fig


def make_w2():
    f = Fig(xlim=(0, 3), ylim=(0, 6.2), width=560, height=340, xlabel='t', ylabel='y')
    f.axes(xticks=[1, 2, 3], yticks=[1, 2, 3, 4, 5, 6])
    for K in (-3, -1, 1, 3):
        f.curve(lambda t, K=K: 3 + K * math.exp(-2 * t), color='grey', width=1.3, dash='4,4')
    f.curve(lambda t: 3 - 2 * math.exp(-2 * t), color='blue', label='y(0) = 1:  y = 3 − 2e^(−2t)')
    f.curve(lambda t: 3 + 2 * math.exp(-2 * t), color='orange', label='y(0) = 5:  y = 3 + 2e^(−2t)')
    f.line(0, 3, 3, 3, color='green', dash='2,3', width=1.6)
    f.point(0, 1, '', color='blue')
    f.point(0, 5, '', color='orange')
    f.text(2.95, 3.25, 'every curve settles at y = 3', color='green', size=12, anchor='end')
    f.legend()
    return {'family': f.save('w2_family')}


def make_w3():
    urls = {}
    f = Fig(xlim=(-0.3, 4), ylim=(-0.4, 4.8), width=560, height=360, xlabel='t', ylabel='y')
    f.axes(xticks=[1, 2, 3, 4], yticks=[1, 2, 3])
    g = lambda t, c: (2 * (t - c) / 3) ** 1.5 if t >= c else 0.0  # noqa: E731
    f.curve(lambda t: 0.0, a=0, b=4, color='orange', label='y = 0')
    f.curve(lambda t: g(t, 0), a=0, b=4, color='blue', label='y = (2t/3)^(3/2)')
    for c in (1, 2):
        f.curve(lambda t, c=c: g(t, c), a=0, b=4, color='grey', width=1.4, dash='5,4',
                label='wait at 0, then lift off (also solutions)' if c == 1 else None)
    f.point(0, 0, 'start (0, 0)', color='black', dx=8, dy=-10)
    f.legend(x=120, y=20)
    urls['cube'] = f.save('w3_cube_root')

    f = Fig(xlim=(-1, 1.6), ylim=(0, 10), width=560, height=330, xlabel='t', ylabel='y')
    f.axes(xticks=[-1, 0.5, 1, 1.5], yticks=[2, 4, 6, 8])
    f.curve(lambda t: 1 / (1 - t), a=-1, b=0.995, color='blue', label='y = 1/(1 − t)')
    f.line(1, 0, 1, 10, color='red', dash='6,4', width=1.6)
    f.text(1.04, 8.8, 't = 1: the solution', color='red', size=12, anchor='start')
    f.text(1.04, 8.0, 'shoots to infinity', color='red', size=12, anchor='start')
    f.point(0, 1, 'y(0) = 1', color='blue', dx=-8, dy=-8, anchor='end')
    f.legend(x=70, y=30)
    urls['blowup'] = f.save('w3_blowup')
    return urls


def make_w4():
    f = Fig(xlim=(-3.2, 6.4), ylim=(-2.6, 2.6), width=560, height=320, xlabel='t', ylabel='y', equal=True)
    f.axes(xticks=[-3, -2, -1, 1, 2, 3], yticks=[-2, -1, 1, 2])
    cols = ['blue', 'green', 'orange', 'purple']
    for C, col in zip((3, 8, 15, 24), cols):
        a, b = math.sqrt(C / 3), math.sqrt(C / 4)
        xs = [a * math.cos(2 * math.pi * k / 200) for k in range(201)]
        ys = [b * math.sin(2 * math.pi * k / 200) for k in range(201)]
        f.polyline(xs, ys, color=col, label=f'3t² + 4y² = {C}')
    f.legend(x=f.X(3.35), y=f.Y(2.3))
    return {'levels': f.save('w4_level_curves')}



def make_w5():
    import math as m
    over = lambda t: 70 * m.exp(-10 * t) + 20 * m.exp(-40 * t)  # noqa: E731  (t in ms)
    crit = lambda t: (1200 * t + 90) * m.exp(-20 * t)  # noqa: E731
    under = lambda t: m.exp(-12 * t) * (90 * m.cos(16 * t) + 120 * m.sin(16 * t))  # noqa: E731
    f = Fig(xlim=(0, 0.45), ylim=(-35, 125), width=560, height=360, xlabel='t (ms)', ylabel='v (V)')
    f.axes(xticks=[0.1, 0.2, 0.3, 0.4], yticks=[-25, 25, 50, 75, 100])
    f.curve(over, color='blue', label='overdamped  (R = 2 kΩ)')
    f.curve(crit, color='green', label='critically damped  (R = 2.5 kΩ)')
    f.curve(under, color='orange', label='underdamped  (R ≈ 4.17 kΩ)')
    f.point(0, 90, '', color='black')
    f.text(0.012, 112, 'all three start at 90 V', size=12.5, anchor='start', weight='bold')
    f.legend()
    return {'damping': f.save('w5_damping')}


if __name__ == '__main__':
    print(make_w2(), make_w3(), make_w4(), make_w5())
