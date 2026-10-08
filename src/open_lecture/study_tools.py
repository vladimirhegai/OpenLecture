"""Small, bounded computations for probability, mathematical methods, and digital systems."""

import ast
import itertools
import warnings

import numpy as np
from scipy import linalg, stats

from .errors import DomainError
from .schemas import DistributionRequest, LinearODERequest, LogicRequest


def distribution(data: DistributionRequest):
    match data.distribution:
        case "normal":
            model = stats.norm(loc=data.mean, scale=data.std)
            formula = r"f(x)=\frac{e^{-(x-\mu)^2/(2\sigma^2)}}{\sigma\sqrt{2\pi}}"
        case "poisson":
            model = stats.poisson(mu=data.rate)
            formula = r"P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}"
        case "exponential":
            model = stats.expon(scale=1 / data.rate)
            formula = r"f(x)=\lambda e^{-\lambda x},\quad x\geq0"
        case "uniform":
            model = stats.uniform(loc=data.low, scale=data.high - data.low)
            formula = r"f(x)=\frac{1}{b-a},\quad a\leq x\leq b"
        case "gamma":
            model = stats.gamma(a=data.shape, scale=data.scale)
            formula = r"f(x)=\frac{x^{k-1}e^{-x/\theta}}{\Gamma(k)\theta^k},\quad x\geq0"
    discrete = data.distribution == "poisson"
    low, high = model.ppf(0.0001), model.ppf(0.9999)
    x = np.arange(0, int(high) + 1) if discrete else np.linspace(low, high, 161)
    values = model.pmf(x) if discrete else model.pdf(x)
    cdf, sf = float(model.cdf(data.x)), float(model.sf(data.x))
    return {
        "schema_version": 1,
        "card_type": "probability_distribution",
        "engine": "scipy.stats",
        "verified": True,
        "distribution": data.distribution,
        "parameters": data.model_dump(),
        "parameter_schema": type(data).model_json_schema(),
        "formula_latex": formula,
        "outputs": {
            "cdf": cdf,
            "survival_probability": sf,
            "mean": float(model.mean()),
            "variance": float(model.var()),
            "point_probability": float(model.pmf(data.x)) if discrete else 0.0,
            "density": None if discrete else float(model.pdf(data.x)),
        },
        "chart": {
            "x": x.tolist(),
            "y": values.tolist(),
            "cdf": model.cdf(x).tolist(),
            "kind": "pmf" if discrete else "pdf",
            "truncated_tails": True,
            "x_label": "x",
            "y_label": "Probability mass" if discrete else "Probability density",
        },
        "assumptions": "Poisson x is a nonnegative count. Continuous density is not point probability.",
    }


def linear_ode(data: LinearODERequest):
    # Constant forcing is represented by an extra state fixed to one.
    if data.order == 1:
        matrix = np.array([[data.a, data.forcing], [0.0, 0.0]])
        initial = np.array([data.y0, 1.0])
        equation = "dy/dt = a*y + forcing"
    else:
        matrix = np.array([[0.0, 1.0, 0.0], [data.b, data.a, data.forcing], [0.0, 0.0, 0.0]])
        initial = np.array([data.y0, data.dy0, 1.0])
        equation = "d2y/dt2 = a*dy/dt + b*y + forcing"
    time = np.linspace(0, data.duration, data.samples)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        states = np.array([linalg.expm(matrix * t) @ initial for t in time])
    if not np.all(np.isfinite(states)) or np.max(np.abs(states)) > 1e100:
        raise DomainError(
            "unstable_trajectory", "Trajectory exceeds supported numeric range; shorten the interval", 422
        )
    derivative = states @ matrix.T
    return {
        "schema_version": 1,
        "card_type": "linear_ode",
        "engine": "scipy.linalg.expm",
        "verified": True,
        "equation": equation,
        "parameters": data.model_dump(),
        "parameter_schema": LinearODERequest.model_json_schema(),
        "chart": {
            "x": time.tolist(),
            "y": states[:, 0].tolist(),
            "dy": derivative[:, 0].tolist(),
            "x_label": "Time (units supplied by the model)",
            "y_label": "y(t)",
        },
        "initial_condition_error": float(abs(states[0, 0] - data.y0)),
        "method": "Numerical matrix exponential of a constant-coefficient augmented linear system",
        "scope": "Constant forcing, real coefficients, t starts at 0. No general circuit or nonlinear ODE simulation.",
    }


def truth_table(data: LogicRequest):
    import sympy as sp

    try:
        tree = ast.parse(data.expression, mode="eval")
        if len(list(ast.walk(tree))) > 80:
            raise ValueError("Expression exceeds 80 syntax nodes")
        allowed = set(data.variables)

        def evaluate(node, values):
            if isinstance(node, ast.Expression):
                return evaluate(node.body, values)
            if isinstance(node, ast.Name) and node.id in allowed:
                return values[node.id]
            if isinstance(node, ast.Constant) and type(node.value) is int and node.value in {0, 1}:
                return bool(node.value)
            if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Invert):
                return not evaluate(node.operand, values)
            if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.BitAnd, ast.BitOr, ast.BitXor)):
                left, right = evaluate(node.left, values), evaluate(node.right, values)
                if isinstance(node.op, ast.BitAnd):
                    return left and right
                if isinstance(node.op, ast.BitOr):
                    return left or right
                return left != right
            raise ValueError("Use declared variables, 0/1, parentheses, ~ (NOT), & (AND), | (OR), ^ (XOR)")

        rows = []
        for bits in itertools.product([0, 1], repeat=len(data.variables)):
            values = dict(zip(data.variables, bits, strict=True))
            rows.append({"inputs": values, "output": int(evaluate(tree, values))})
        symbols = [sp.Symbol(name) for name in data.variables]
        minterms = [index for index, row in enumerate(rows) if row["output"]]
        simplified = sp.SOPform(symbols, minterms)
        for row in rows:
            if (
                int(bool(simplified.subs({symbol: bool(row["inputs"][str(symbol)]) for symbol in symbols})))
                != row["output"]
            ):
                raise ValueError("Simplification failed exhaustive verification")
        kmap = None
        if 2 <= len(symbols) <= 4:
            split = len(symbols) // 2
            row_bits, col_bits = split, len(symbols) - split

            def gray(width):
                return [format(i ^ (i >> 1), f"0{width}b") for i in range(2**width)]

            row_labels, col_labels = gray(row_bits), gray(col_bits)
            kmap = {
                "row_variables": data.variables[:split],
                "column_variables": data.variables[split:],
                "row_labels": row_labels,
                "column_labels": col_labels,
                "values": [[rows[int(r + c, 2)]["output"] for c in col_labels] for r in row_labels],
            }
        return {
            "schema_version": 1,
            "card_type": "logic_truth_table",
            "engine": "boolean_enumeration_and_sympy_SOPform",
            "verified": True,
            "parameters": data.model_dump(),
            "rows": rows,
            "simplified_sop": str(simplified),
            "latex": sp.latex(simplified),
            "karnaugh_map": kmap,
            "scope": "Combinational two-valued Boolean logic; no timing, sequential state, or don't-cares.",
        }
    except (ValueError, SyntaxError, RecursionError) as error:
        raise DomainError("invalid_logic", str(error), 422) from error
