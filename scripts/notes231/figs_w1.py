"""Week 1 diagrams (SVG). Run before build_w1.py; build_w1.py imports make()."""
import math
from svgfig import Fig


def make():
    urls = {}
    f = Fig(xlim=(-5.5, 5.5), ylim=(-5.2, 5.2), width=560, height=430, xlabel='Re', ylabel='Im', equal=True)
    f.axes(xticks=[-4, -2, 2, 4], yticks=[-4, -2, 2, 4])
    for (a, b, col, lab, dx, anc) in [(3, 4, 'blue', '3 + j4', 8, 'start'), (-3, 4, 'orange', '−3 + j4', -8, 'end'),
                                      (-3, -4, 'green', '−3 − j4', -8, 'end'), (3, -4, 'purple', '3 − j4', 8, 'start')]:
        f.arrow(0, 0, a, b, color=col)
        f.point(a, b, lab, color=col, dx=dx, anchor=anc)
    f.arc(0, 0, 1.1, 0, 53.13, color='blue', label='53.13°', label_r=1.8)
    f.arc(0, 0, 0.7, 0, 126.87, color='orange', label='126.87°', label_r=1.3)
    f.line(3, 0, 3, 4); f.line(0, 4, 3, 4)  # noqa: E702
    f.text(3.25, 1.6, 'b = 4', color='grey', size=12, anchor='start')
    f.text(1.5, 4.25, 'a = 3', color='grey', size=12)
    f.text(1.0, 2.3, 'c = 5', color='blue', size=12, anchor='end')
    f.text(4.0, 4.8, '1st quadrant', color='grey', size=12); f.text(-4.0, 4.8, '2nd quadrant', color='grey', size=12)  # noqa: E702
    f.text(-4.0, -5.0, '3rd quadrant', color='grey', size=12); f.text(4.0, -5.0, '4th quadrant', color='grey', size=12)  # noqa: E702
    urls['plane'] = f.save('w1_plane')

    f = Fig(xlim=(-4.2, 4.2), ylim=(-4.2, 4.2), width=460, height=430, xlabel='Re', ylabel='Im', equal=True)
    f.axes(xticks=[-3, 3], yticks=[-3, 3])
    f.circle(0, 0, 3)
    for k, ang in enumerate((15, 105, 195, 285)):
        x, y = 3 * math.cos(math.radians(ang)), 3 * math.sin(math.radians(ang))
        f.arrow(0, 0, x, y, color='blue', width=1.8)
        lab = f'3∠{ang}°'
        right = math.cos(math.radians(ang)) >= 0
        f.point(x, y, lab, color='blue', dx=8 if right else -8, anchor='start' if right else 'end', dy=-6 if y >= 0 else 16)
    f.arc(0, 0, 0.9, 0, 15, color='orange', label='15°', label_r=1.45)
    f.arc(0, 0, 1.3, 15, 105, color='green', label='+90°', label_r=1.75)
    urls['roots'] = f.save('w1_roots')

    f = Fig(xlim=(0, 5.6), ylim=(0, 1.08), width=560, height=320, xlabel='t / τ', ylabel='i / I₀')
    f.axes(xticks=[1, 2, 3, 4, 5], yticks=[0.37, 1], yfmt=lambda v: f'{v:g}')
    f.curve(lambda t: math.exp(-t), color='blue', label='i(t) = I₀ e^(−t/τ)')
    f.line(1, 0, 1, math.exp(-1)); f.line(0, math.exp(-1), 1, math.exp(-1))  # noqa: E702
    f.point(1, math.exp(-1), '37% left after one τ', color='orange', dx=10, dy=-6)
    f.point(5, math.exp(-5), 'under 1% after 5τ', color='green', dx=-6, dy=-14, anchor='end')
    f.legend()
    urls['tau'] = f.save('w1_tau')
    return urls


if __name__ == '__main__':
    print(make())
