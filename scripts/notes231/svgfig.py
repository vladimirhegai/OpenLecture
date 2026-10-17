"""Tiny SVG figure maker for the ELEC 231 notes (no matplotlib needed).

    from svgfig import Fig
    f = Fig(xlim=(-5, 5), ylim=(-5, 5), xlabel='Re', ylabel='Im')
    f.axes(xticks=[-4, -2, 2, 4], yticks=[-4, -2, 2, 4])
    f.curve(lambda t: math.exp(-t), color='blue', label='e^{-t}')   # or f.polyline(xs, ys)
    f.point(3, 4, '3 + j4'); f.arrow(0, 0, 3, 4); f.text(1, 1, 'θ')
    f.save('w1_plane')      # -> /figures/elec231/w1_plane.svg (served by the app) ; returns the URL

Figures are written to frontend/public/figures/elec231/ (kept by every frontend build) and copied into
src/open_lecture/web/figures/elec231/ (what the running server serves).
"""
import html
import math
import os
import shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(ROOT, 'frontend', 'public', 'figures', 'elec231')
WEB = os.path.join(ROOT, 'src', 'open_lecture', 'web', 'figures', 'elec231')
COLORS = {'blue': '#2b59c3', 'orange': '#e07b00', 'green': '#2e8b57', 'red': '#c0392b', 'purple': '#7d3c98',
          'grey': '#888888', 'black': '#222222'}


def _c(c):
    return COLORS.get(c, c)


class Fig:
    def __init__(self, xlim, ylim, width=560, height=340, xlabel='', ylabel='', margin=(46, 18, 22, 40), equal=False):
        """margin = (left, right, top, bottom) in px. equal=True keeps 1 unit the same length on both axes."""
        self.x0, self.x1 = xlim
        self.y0, self.y1 = ylim
        self.W, self.H = width, height
        self.ml, self.mr, self.mt, self.mb = margin
        if equal:  # shrink one direction so the scales match
            sx = (width - self.ml - self.mr) / (self.x1 - self.x0)
            sy = (height - self.mt - self.mb) / (self.y1 - self.y0)
            s = min(sx, sy)
            extra_x = (width - self.ml - self.mr) - s * (self.x1 - self.x0)
            extra_y = (height - self.mt - self.mb) - s * (self.y1 - self.y0)
            self.ml += extra_x / 2
            self.mr += extra_x / 2
            self.mt += extra_y / 2
            self.mb += extra_y / 2
        self.xlabel, self.ylabel = xlabel, ylabel
        self.items = []
        self.legend_items = []

    # data -> pixels
    def X(self, x):
        return self.ml + (x - self.x0) / (self.x1 - self.x0) * (self.W - self.ml - self.mr)

    def Y(self, y):
        return self.H - self.mb - (y - self.y0) / (self.y1 - self.y0) * (self.H - self.mt - self.mb)

    def _t(self, x, y, s, size=13, color='black', anchor='middle', weight='normal', italic=False, dy=0):
        style = ' font-style="italic"' if italic else ''
        self.items.append(f'<text x="{x:.1f}" y="{y + dy:.1f}" font-size="{size}" fill="{_c(color)}" text-anchor="{anchor}" '
                          f'font-weight="{weight}"{style}>{html.escape(s)}</text>')

    def axes(self, xticks=(), yticks=(), grid=True, origin_axes=True, xfmt=None, yfmt=None):
        fx = xfmt or (lambda v: f'{v:g}')
        fy = yfmt or (lambda v: f'{v:g}')
        for v in xticks:
            if grid:
                self.items.append(f'<line x1="{self.X(v):.1f}" y1="{self.Y(self.y0):.1f}" x2="{self.X(v):.1f}" y2="{self.Y(self.y1):.1f}" stroke="#e6e6e6"/>')
        for v in yticks:
            if grid:
                self.items.append(f'<line x1="{self.X(self.x0):.1f}" y1="{self.Y(v):.1f}" x2="{self.X(self.x1):.1f}" y2="{self.Y(v):.1f}" stroke="#e6e6e6"/>')
        ax = 0 if (origin_axes and self.y0 <= 0 <= self.y1) else self.y0
        ay = 0 if (origin_axes and self.x0 <= 0 <= self.x1) else self.x0
        self.arrow(self.x0, ax, self.x1, ax, color='black', width=1.3, head=7)
        self.arrow(ay, self.y0, ay, self.y1, color='black', width=1.3, head=7)
        for v in xticks:
            self.items.append(f'<line x1="{self.X(v):.1f}" y1="{self.Y(ax) - 3:.1f}" x2="{self.X(v):.1f}" y2="{self.Y(ax) + 3:.1f}" stroke="#222"/>')
            self._t(self.X(v), self.Y(ax) + 17, fx(v), size=12, color='grey')
        for v in yticks:
            self.items.append(f'<line x1="{self.X(ay) - 3:.1f}" y1="{self.Y(v):.1f}" x2="{self.X(ay) + 3:.1f}" y2="{self.Y(v):.1f}" stroke="#222"/>')
            self._t(self.X(ay) - 7, self.Y(v) + 4, fy(v), size=12, color='grey', anchor='end')
        if self.xlabel:
            self._t(self.X(self.x1) - 2, self.Y(ax) - 8, self.xlabel, size=13, anchor='end', italic=True)
        if self.ylabel:
            self._t(self.X(ay) + 8, self.Y(self.y1) + 12, self.ylabel, size=13, anchor='start', italic=True)

    def polyline(self, xs, ys, color='blue', width=2.4, dash=None, label=None):
        pts = ' '.join(f'{self.X(x):.1f},{self.Y(y):.1f}' for x, y in zip(xs, ys))
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.items.append(f'<polyline points="{pts}" fill="none" stroke="{_c(color)}" stroke-width="{width}" '
                          f'stroke-linejoin="round" stroke-linecap="round"{d}/>')
        if label:
            self.legend_items.append((label, color, dash))

    def curve(self, f, a=None, b=None, n=400, clip=True, **kw):
        a = self.x0 if a is None else a
        b = self.x1 if b is None else b
        xs = [a + (b - a) * k / n for k in range(n + 1)]
        segs, cur = [], ([], [])
        for x in xs:
            try:
                y = f(x)
            except (ValueError, ZeroDivisionError, OverflowError):
                y = None
            if y is None or (clip and not (self.y0 - 1e-9 <= y <= self.y1 + 1e-9)):
                if cur[0]:
                    segs.append(cur)
                cur = ([], [])
                continue
            cur[0].append(x)
            cur[1].append(y)
        if cur[0]:
            segs.append(cur)
        label = kw.pop('label', None)
        for i, (sx, sy) in enumerate(segs):
            self.polyline(sx, sy, label=label if i == 0 else None, **kw)

    def line(self, x1, y1, x2, y2, color='grey', width=1.3, dash='5,4'):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.items.append(f'<line x1="{self.X(x1):.1f}" y1="{self.Y(y1):.1f}" x2="{self.X(x2):.1f}" y2="{self.Y(y2):.1f}" '
                          f'stroke="{_c(color)}" stroke-width="{width}"{d}/>')

    def arrow(self, x1, y1, x2, y2, color='blue', width=2.2, head=10):
        X1, Y1, X2, Y2 = self.X(x1), self.Y(y1), self.X(x2), self.Y(y2)
        ang = math.atan2(Y2 - Y1, X2 - X1)
        bx, by = X2 - head * math.cos(ang), Y2 - head * math.sin(ang)
        self.items.append(f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{_c(color)}" stroke-width="{width}"/>')
        p1 = (X2, Y2)
        p2 = (bx + head * 0.45 * math.sin(ang), by - head * 0.45 * math.cos(ang))
        p3 = (bx - head * 0.45 * math.sin(ang), by + head * 0.45 * math.cos(ang))
        self.items.append(f'<polygon points="{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} {p3[0]:.1f},{p3[1]:.1f}" fill="{_c(color)}"/>')

    def point(self, x, y, label='', color='blue', r=4.5, dx=8, dy=-8, anchor='start', size=13):
        self.items.append(f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="{r}" fill="{_c(color)}"/>')
        if label:
            self._t(self.X(x) + dx, self.Y(y) + dy, label, size=size, color=color, anchor=anchor, weight='bold')

    def text(self, x, y, s, color='black', size=13, anchor='middle', italic=False, weight='normal'):
        self._t(self.X(x), self.Y(y), s, size=size, color=color, anchor=anchor, italic=italic, weight=weight)

    def circle(self, cx, cy, r, color='grey', width=1.3, dash='5,4'):
        rx = abs(self.X(cx + r) - self.X(cx))
        ry = abs(self.Y(cy + r) - self.Y(cy))
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.items.append(f'<ellipse cx="{self.X(cx):.1f}" cy="{self.Y(cy):.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="none" '
                          f'stroke="{_c(color)}" stroke-width="{width}"{d}/>')

    def arc(self, cx, cy, r, a0, a1, color='orange', width=1.8, label='', label_r=None):
        """Angle arc from a0 to a1 degrees (counter-clockwise if a1 > a0), radius r in x-units."""
        n = 40
        xs = [cx + r * math.cos(math.radians(a0 + (a1 - a0) * k / n)) for k in range(n + 1)]
        ys = [cy + r * math.sin(math.radians(a0 + (a1 - a0) * k / n)) for k in range(n + 1)]
        self.polyline(xs, ys, color=color, width=width)
        if label:
            m = math.radians((a0 + a1) / 2)
            lr = label_r or r * 1.35
            self._t(self.X(cx + lr * math.cos(m)), self.Y(cy + lr * math.sin(m)) + 4, label, color=color, size=13)

    def legend(self, x=None, y=None):
        """Legend box in the top-right corner (or at pixel x, y)."""
        if not self.legend_items:
            return
        w = 18 + max(len(l) for l, _, _ in self.legend_items) * 7.2 + 30
        x = self.W - self.mr - w - 4 if x is None else x
        y = self.mt + 4 if y is None else y
        h = 8 + 20 * len(self.legend_items)
        self.items.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="6" fill="white" fill-opacity="0.92" stroke="#ddd"/>')
        for k, (lab, col, dash) in enumerate(self.legend_items):
            yy = y + 16 + 20 * k
            d = f' stroke-dasharray="{dash}"' if dash else ''
            self.items.append(f'<line x1="{x + 10:.1f}" y1="{yy - 4:.1f}" x2="{x + 34:.1f}" y2="{yy - 4:.1f}" stroke="{_c(col)}" stroke-width="2.6"{d}/>')
            self._t(x + 42, yy, lab, size=12.5, anchor='start')

    def svg(self):
        body = '\n'.join(self.items)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.W}" height="{self.H}" viewBox="0 0 {self.W} {self.H}" '
                f'font-family="Inter, Segoe UI, Arial, sans-serif">\n'
                f'<rect width="100%" height="100%" rx="10" fill="white"/>\n{body}\n</svg>\n')

    def save(self, name):
        os.makedirs(SRC, exist_ok=True)
        os.makedirs(WEB, exist_ok=True)
        path = os.path.join(SRC, name + '.svg')
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(self.svg())
        shutil.copy(path, os.path.join(WEB, name + '.svg'))
        return f'/figures/elec231/{name}.svg'
