"""Scratch note that exercises every math-tool fence (steps, graph, graph3d). Run: python tooltest.py"""
import json
import sys
import urllib.request

from lib231 import API, _send, _get

STEPS = r'''```steps
title "Separate, then integrate"
$$ \dfrac{dy}{dt}=t\,y $$
Start from the equation.
$$ \hl{\dfrac{1}{y}\,dy}=\hl{t\,dt} $$
Divide by $y$, multiply by $dt$: every $y$ on the left, every $t$ on the right.
$$ \hl{\int}\dfrac{1}{y}\,dy=\hl{\int} t\,dt $$
Integrate both sides.
$$ \hl{\ln|y|}=\hl{\tfrac12 t^2+C} $$
Antiderivatives: $\int \frac1y\,dy=\ln|y|$ and $\int t\,dt=\frac12t^2$.
$$ y=\hl{A\,e^{t^2/2}} $$
Exponentiate both sides; $A=\pm e^{C}$ is any constant.
```'''

GRAPH = r'''```graph
title "Decay: $y=y_0e^{-t/\tau}$"
x 0 5 label="$t$"
y 0 5 label="$y$"
slider tau 0.2 3 1 step=0.05 label="$\tau$" animate
slider y0 0.5 4.5 4 step=0.1 label="$y_0$"
curve "y0*exp(-t/tau)" label="$y_0e^{-t/\tau}$"
vline "tau" label="$t=\tau$"
point "tau" "y0*exp(-1)" label="37\% left"
readout "$y(\tau)=$" "y0*exp(-1)"
```'''

FIELD = r'''```graph
title "Slope field of $y'=y-t$; drag the start point"
x -3 3 label="$t$"
y -3 3 label="$y$"
field "y-t"
drag P 0 0.5 label="$(t_0,y_0)$"
solution "y-t" x0="P_x" y0="P_y" label="the solution through your point"
curve "t+1" dash label="$y=t+1$"
```'''

COMPLEX = r'''```graph
title "Multiply complex numbers: lengths multiply, angles add"
x -4 4 label="Re"
y -3 3 label="Im"
equal
drag Z 2 1 label="$z$" color=1
drag W 0.5 1.2 label="$w$" color=3
arrow "Z_x" "Z_y" color=1
arrow "W_x" "W_y" color=3
arrow "Z_x*W_x-Z_y*W_y" "Z_x*W_y+Z_y*W_x" color=2 label="$zw$"
circle "0" "0" "1" dash color=0
readout "$|z|=$" "hypot(Z_x,Z_y)"
readout "$|w|=$" "hypot(W_x,W_y)"
readout "$|zw|=$" "hypot(Z_x,Z_y)*hypot(W_x,W_y)"
readout "$\angle z+\angle w=$" "deg(atan2(Z_y,Z_x))+deg(atan2(W_y,W_x))" unit="°"
```'''

REGION = r'''```graph
title "Where is $f=\sqrt{y}$ safe?"
x -2 2 label="$t$"
y -2 2 label="$y$"
region "y>0" label="$f$ and $\partial f/\partial y$ continuous"
family C -2 2 0.5 "(t+C)^2/4*step(t+C)" label="solutions"
hline "0"
```'''

LEVEL = r'''```graph
title "Level curves $F(x,y)=x^2+xy+y^2=C$"
x -3 3
y -3 3
equal
slider C 0.2 6 2 label="$C$"
level "x^2+x*y+y^2" value="C" label="$F=C$"
level "x^2+x*y+y^2" values="1,3,5,7" color=0
```'''

SURF = r'''```graph3d
title "Exact equation: solutions are level curves of $F$"
x -2 2
y -2 2
z -1 8 label="$F$"
slider C 0 7 3 label="$C$"
surface "x^2+x*y+y^2" label="$F(x,y)=x^2+xy+y^2$"
plane "C" label="height $C$: the curve $F=C$"
levels values="1,3,5"
```'''

HELIX = r'''```graph3d
title "$e^{jt}$ walks around a circle as $t$ grows"
x -1.2 1.2 label="Re"
y 0 12 label="$t$"
z -1.2 1.2 label="Im"
curve3 "cos(s)" "s" "sin(s)" 0 12 label="$e^{jt}$"
point3 "cos(T)" "T" "sin(T)" label="now"
slider T 0 12 2 label="$t$"
```'''

ELLIPSE = r'''```graph
title "Exact: $3t\,dt+4y\,dy=0$ (vertical tangents where $y=0$)"
x -3 3 label="$t$"
y -2.5 2.5 label="$y$"
equal
field "-3*t/(4*y)"
drag P 1 1 label="start"
solution "-3*t/(4*y)" x0="P_x" y0="P_y" label="traced solution"
level "3*x^2+4*y^2" value="3*P_x^2+4*P_y^2" dash color=2 label="true level curve"
```'''

BLOW = r'''```graph
title "$y'=y^2$ blows up"
x -1 3 label="$t$"
y -1 8
drag P 0 1
solution "y^2" x0="P_x" y0="P_y"
vline "P_x+1/P_y"
```'''

BAD = r'''```graph
x 0 5
curve "foo(t)"
```'''

blocks = [{"type": "heading", "level": 1, "text": "Tool test"}]
for name, f in [('steps', STEPS), ('graph', GRAPH), ('field', FIELD), ('complex', COMPLEX), ('region', REGION),
                ('level', LEVEL), ('surface', SURF), ('helix', HELIX), ('ellipse', ELLIPSE), ('blow', BLOW), ('bad', BAD)]:
    blocks.append({"type": "paragraph", "text": f"**{name}**\n\n{f}"})
blocks.append({"type": "practice_problem", "title": "Stepper inside a solution", "difficulty": "introductory", "origin": "original",
               "prompt": "Solve $y'=ty$.", "solution": STEPS, "steps": [], "answer": "$y=Ae^{t^2/2}$"})

docs = _get(f'{API}/documents')
old = [d for d in docs if d['title'] == 'Tool test (scratch)']
body = {"title": "Tool test (scratch)", "document_type": "study_notes", "topic_keys": ["tool_test"], "blocks": blocks,
        "actor": "agent", "separate_copy": True}
if old:
    doc = _get(f"{API}/documents/{old[0]['document_id']}")
    ops = [{"op": "remove", "block_id": b['id']} for b in doc['blocks']]
    prev = None
    import uuid
    for b in blocks:
        b = dict(b, id=str(uuid.uuid4()))
        ops.append({"op": "insert", "block": b, "after_id": prev})
        prev = b['id']
    _send(f"{API}/documents/{doc['document_id']}", {"expected_revision": doc['revision'], "operations": ops, "actor": "agent"}, 'PATCH')
    print(doc['document_id'])
else:
    _send(f'{API}/documents', body, 'POST')
    print([d for d in _get(f'{API}/documents') if d['title'] == 'Tool test (scratch)'][0]['document_id'])
