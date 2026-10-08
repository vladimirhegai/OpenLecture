# Circuit language v1

This netlist language is for analysis. Drawings in notes use the separate coordinate-based schematic language in `src/open_lecture/skills/schematic.md`, rendered by `schematic.py`.

The initial language supports resistors and independent DC voltage/current sources. It is deliberately smaller than SPICE. Capacitors, inductors, dependent sources, AC analysis and arbitrary transient networks are not supported yet; unsupported input fails explicitly.

```text
circuit "Voltage divider"
V1 vin 0 DC 10V
R1 vin vout 2kOhm
R2 vout 0 3kOhm
analyze dc
probe V(vout)
probe I(V1)
```

Grammar: a quoted circuit title; component lines `Rname node+ node- valueOhm`, `Vname node+ node- DC valueV`, or `Iname node+ node- DC valueA`; one `analyze dc`; optional voltage/current probes. `#` introduces a comment. A source's positive-to-negative ordering defines voltage and passive current direction. Current sources push current from the first terminal to the second. Ground is `0`.

Node names are alphanumeric/underscore, up to 32 characters, and case-insensitive. Component names start R/V/I and are unique ignoring case. Prefixes: p, n, u, m, k, M, G. Units are case-sensitive (`Ohm`, `V`, `A`). Scientific notation is supported. Resistors must be positive, between 1e-9 and 1e12 Ohm; source magnitudes may not exceed 1e12. Limits: 100 components, 80 nodes.

Topology is independent of future layout coordinates. Probes must resolve to a real node or component. The compiler emits a restricted `.op` netlist without accepting arbitrary SPICE directives or includes. These netlists are **not executed by ngspice in this release**.

## Verified computations

`circuit_simulate` runs NumPy modified nodal analysis. Results include node voltages, branch currents, component powers, units, residual, power balance, engine identity and the immutable circuit artifact ID. Singular circuits and non-finite or failed-residual solutions produce explicit errors. The divider above produces 6 V at `vout`, 2 mA resistor current, and -20 mW source power. Automated tests verify these results and a current-source network.

`math_linear_ode` separately explores real constant-coefficient first/second-order equations. It can illustrate an RC curve once the correct differential equation is derived, but does not turn an arbitrary RC/RLC topology into a transient simulation. Its output says `scipy.linalg.expm`, not ngspice. General circuit transient/AC simulation remains planned.
