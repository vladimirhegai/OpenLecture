import ast
import json
import math
import os
import subprocess
import sys

from .errors import DomainError
from .schemas import BinomialRequest, MathRequest


def calculate(request: MathRequest):
    try:
        process = subprocess.run(
            [sys.executable, "-m", "open_lecture.math_engine"],
            input=request.model_dump_json().encode(),
            capture_output=True,
            timeout=10,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
        )
    except subprocess.TimeoutExpired as error:
        raise DomainError(
            "computation_timeout", "Math computation exceeded ten seconds including process startup", 422
        ) from error
    if process.returncode:
        raise DomainError("invalid_expression", process.stderr.decode("utf-8", errors="replace")[:1000], 422)
    return json.loads(process.stdout)


def compute(request: MathRequest):
    import sympy as sp

    tree = ast.parse(request.expression, mode="eval")
    if len(list(ast.walk(tree))) > 80:
        raise ValueError("Expression exceeds 80 syntax nodes")
    symbols = {name: sp.Symbol(name, real=True) for name in ("x", "y", "t", "n")}
    functions = {
        "sin": sp.sin,
        "cos": sp.cos,
        "tan": sp.tan,
        "exp": sp.exp,
        "log": sp.log,
        "sqrt": sp.sqrt,
        "abs": sp.Abs,
    }

    def convert(node, depth=0):
        if depth > 15:
            raise ValueError("Expression nesting exceeds 15 levels")
        if isinstance(node, ast.Expression):
            return convert(node.body, depth + 1)
        if isinstance(node, ast.Constant) and type(node.value) in {int, float}:
            if not math.isfinite(node.value) or abs(node.value) > 1e12:
                raise ValueError("Numeric constants must be finite and at most 1e12 in magnitude")
            return sp.Rational(str(node.value))
        if isinstance(node, ast.Name):
            if node.id in symbols:
                return symbols[node.id]
            if node.id in {"pi", "e"}:
                return sp.pi if node.id == "pi" else sp.E
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            operand = convert(node.operand, depth + 1)
            return operand if isinstance(node.op, ast.UAdd) else -operand
        if isinstance(node, ast.BinOp):
            left, right = convert(node.left, depth + 1), convert(node.right, depth + 1)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                if right == 0:
                    raise ValueError("Division by zero")
                return left / right
            if isinstance(node.op, ast.Pow):
                if not right.is_Number or abs(right) > 100:
                    raise ValueError("Exponents must be numeric constants between -100 and 100")
                return left**right
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in functions:
            if len(node.args) != 1 or node.keywords:
                raise ValueError("Functions accept exactly one positional argument")
            return functions[node.func.id](convert(node.args[0], depth + 1))
        raise ValueError("Allowed: x, y, t, n, pi, e, arithmetic, sin/cos/tan/exp/log/sqrt/abs")

    expression = convert(tree)
    if request.operation == "differentiate":
        result = sp.diff(expression, symbols[request.variable])
    elif request.operation == "solve":
        polynomial = sp.Poly(expression, symbols[request.variable])
        if polynomial.total_degree() > 6 or expression.free_symbols - {symbols[request.variable]}:
            raise ValueError("Solving supports numeric polynomials of degree at most six in one variable")
        if polynomial.is_zero:
            raise ValueError("Zero polynomial has infinitely many solutions")
        roots = sp.solve(expression, symbols[request.variable])
        return {
            "engine": "sympy",
            "verified": True,
            "interpretation": "expression = 0 over the reals",
            "solutions": [str(root) for root in roots],
            "latex": [sp.latex(root) for root in roots],
        }
    else:
        result = expression
    result = result.subs({symbols[k]: sp.Rational(str(v)) for k, v in request.values.items()})
    if result.has(sp.zoo, sp.nan, sp.oo, -sp.oo):
        raise ValueError("Expression is undefined or non-finite")
    numeric = None
    if not result.free_symbols and result.is_real:
        numeric = float(result.evalf())
        if not math.isfinite(numeric):
            raise ValueError("Numeric result exceeds finite floating-point range")
    if len(str(result)) > 10000:
        raise ValueError("Result exceeds output size limit")
    return {
        "engine": "sympy",
        "verified": True,
        "exact": str(result),
        "latex": sp.latex(result),
        "numeric": numeric,
    }


def binomial(request: BinomialRequest):
    n, p, k = request.n, request.p, request.k
    pmf = [math.comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(n + 1)]
    return {
        "schema_version": 1,
        "card_type": "binomial_distribution",
        "engine": "python.math",
        "verified": True,
        "parameters": request.model_dump(),
        "parameter_schema": BinomialRequest.model_json_schema(),
        "formula_latex": r"P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}",
        "outputs": {
            "probability_exact": pmf[k],
            "probability_cumulative": sum(pmf[: k + 1]),
            "expected_value": n * p,
            "variance": n * p * (1 - p),
        },
        "chart": {"x": list(range(n + 1)), "y": pmf, "x_label": "Successes", "y_label": "Probability"},
    }


if __name__ == "__main__":
    try:
        result = compute(MathRequest.model_validate_json(sys.stdin.buffer.read(10000)))
        sys.stdout.buffer.write(json.dumps(result, allow_nan=False).encode())
    except Exception as error:
        sys.stderr.buffer.write(str(error).encode("utf-8"))
        raise SystemExit(1)
