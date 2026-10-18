/*
 * A small, safe math expression language for interactive note tools (graphs, 3-D surfaces, readouts).
 * Expressions are parsed into a tree and evaluated by walking it: note text is never executed as code.
 *
 *   numbers 2, 0.5, 1e-3      operators + - * / ^ (right-associative), unary -, parentheses
 *   constants pi, e           functions sin cos tan asin acos atan atan2(y,x) sinh cosh tanh exp ln log10
 *                             sqrt cbrt abs sign floor ceil round min max step(x) (0 for x<0, else 1)
 *                             deg(rad) rad(deg) hypot(a,b) mod(a,b) if(cond, a, b) (cond > 0 picks a)
 *   comparisons < <= > >= give 1 or 0, so "x > 0" can be used in if(...) and regions
 *   variables                 any other name, bound at evaluation time (x, y, t, s, slider and point names)
 */

export type Env = Record<string, number>;
export type Compiled = { (env: Env): number; vars: Set<string> };

type Node =
  | { k: "num"; v: number }
  | { k: "var"; name: string }
  | { k: "neg"; a: Node }
  | { k: "bin"; op: string; a: Node; b: Node }
  | { k: "call"; fn: string; args: Node[] };

const FNS: Record<string, (...a: number[]) => number> = {
  sin: Math.sin, cos: Math.cos, tan: Math.tan, asin: Math.asin, acos: Math.acos, atan: Math.atan,
  atan2: Math.atan2, sinh: Math.sinh, cosh: Math.cosh, tanh: Math.tanh, exp: Math.exp, ln: Math.log,
  log: Math.log, log10: Math.log10, sqrt: Math.sqrt, cbrt: Math.cbrt, abs: Math.abs, sign: Math.sign,
  floor: Math.floor, ceil: Math.ceil, round: Math.round, min: Math.min, max: Math.max, hypot: Math.hypot,
  step: (x) => (x < 0 ? 0 : 1),
  deg: (r) => (r * 180) / Math.PI,
  rad: (d) => (d * Math.PI) / 180,
  mod: (a, b) => a - b * Math.floor(a / b),
  if: (c, a, b) => (c > 0 ? a : b),
};
const CONSTS: Record<string, number> = { pi: Math.PI, e: Math.E };

export class ExprError extends Error {}

function tokenize(src: string): string[] {
  const out: string[] = [];
  const re = /\s*(\d+\.?\d*(?:[eE][+-]?\d+)?|\.\d+(?:[eE][+-]?\d+)?|[A-Za-z_][A-Za-z_0-9]*|<=|>=|[-+*/^(),<>])/y;
  let i = 0;
  while (i < src.length) {
    if (/^\s*$/.test(src.slice(i))) break;
    re.lastIndex = i;
    const m = re.exec(src);
    if (!m) throw new ExprError(`unexpected "${src.slice(i).trim()[0]}" in ${src}`);
    out.push(m[1]);
    i = re.lastIndex;
  }
  return out;
}

function parse(src: string): Node {
  const toks = tokenize(src);
  let p = 0;
  const peek = () => toks[p];
  const take = (want?: string) => {
    const t = toks[p++];
    if (want !== undefined && t !== want) throw new ExprError(`expected "${want}" in ${src}`);
    if (t === undefined) throw new ExprError(`unexpected end of ${src}`);
    return t;
  };
  // compare < sum < product < unary < power < atom
  function compare(): Node {
    let a = sum();
    while (["<", "<=", ">", ">="].includes(peek())) {
      const op = take();
      a = { k: "bin", op, a, b: sum() };
    }
    return a;
  }
  function sum(): Node {
    let a = product();
    while (peek() === "+" || peek() === "-") {
      const op = take();
      a = { k: "bin", op, a, b: product() };
    }
    return a;
  }
  function product(): Node {
    let a = unary();
    while (peek() === "*" || peek() === "/") {
      const op = take();
      a = { k: "bin", op, a, b: unary() };
    }
    return a;
  }
  function unary(): Node {
    if (peek() === "-") {
      take();
      return { k: "neg", a: unary() };
    }
    if (peek() === "+") {
      take();
      return unary();
    }
    return power();
  }
  function power(): Node {
    const a = atom();
    if (peek() === "^") {
      take();
      return { k: "bin", op: "^", a, b: unary() }; // -x^2 = -(x^2); 2^-1 works; right-associative
    }
    return a;
  }
  function atom(): Node {
    const t = take();
    if (t === "(") {
      const a = compare();
      take(")");
      return a;
    }
    if (/^[\d.]/.test(t)) return { k: "num", v: Number(t) };
    if (/^[A-Za-z_]/.test(t)) {
      if (peek() === "(") {
        if (!(t in FNS)) throw new ExprError(`unknown function ${t}() in ${src}`);
        take("(");
        const args: Node[] = [];
        if (peek() !== ")") {
          args.push(compare());
          while (peek() === ",") {
            take();
            args.push(compare());
          }
        }
        take(")");
        return { k: "call", fn: t, args };
      }
      if (t in CONSTS) return { k: "num", v: CONSTS[t] };
      return { k: "var", name: t };
    }
    throw new ExprError(`unexpected "${t}" in ${src}`);
  }
  const tree = compare();
  if (p < toks.length) throw new ExprError(`unexpected "${toks[p]}" in ${src}`);
  return tree;
}

function collect(n: Node, into: Set<string>) {
  if (n.k === "var") into.add(n.name);
  else if (n.k === "neg") collect(n.a, into);
  else if (n.k === "bin") {
    collect(n.a, into);
    collect(n.b, into);
  } else if (n.k === "call") n.args.forEach((a) => collect(a, into));
}

function evaluate(n: Node, env: Env): number {
  switch (n.k) {
    case "num":
      return n.v;
    case "var": {
      const v = env[n.name];
      return v === undefined ? NaN : v;
    }
    case "neg":
      return -evaluate(n.a, env);
    case "bin": {
      const a = evaluate(n.a, env);
      const b = evaluate(n.b, env);
      switch (n.op) {
        case "+": return a + b;
        case "-": return a - b;
        case "*": return a * b;
        case "/": return a / b;
        case "^": return Math.pow(a, b);
        case "<": return a < b ? 1 : 0;
        case "<=": return a <= b ? 1 : 0;
        case ">": return a > b ? 1 : 0;
        default: return a >= b ? 1 : 0;
      }
    }
    case "call":
      return FNS[n.fn](...n.args.map((a) => evaluate(a, env)));
  }
}

const cache = new Map<string, Compiled>();

/** Parse once, evaluate many times. Unknown variables evaluate to NaN (nothing is drawn there). */
export function compile(src: string): Compiled {
  const hit = cache.get(src);
  if (hit) return hit;
  const tree = parse(src);
  const vars = new Set<string>();
  collect(tree, vars);
  const fn = ((env: Env) => evaluate(tree, env)) as Compiled;
  fn.vars = vars;
  cache.set(src, fn);
  return fn;
}

/** Check that every variable an expression uses is one of `known`; returns the first unknown name. */
export function unknownVar(fn: Compiled, known: Set<string>): string | undefined {
  for (const v of fn.vars) if (!known.has(v)) return v;
  return undefined;
}
