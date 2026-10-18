/*
 * Line format shared by the ```graph and ```graph3d fences: one statement per line,
 *   kind positional... key=value... flag...
 * Tokens with spaces go in double quotes ("C*exp(k*t)", label="$y=Ce^{kt}$"). A line starting with # is a comment.
 */
import { compile, ExprError, unknownVar, type Compiled } from "./expr";

export type Stmt = { kind: string; args: string[]; opts: Record<string, string>; line: number };

export class SpecError extends Error {}

function tokens(line: string, no: number): string[] {
  const out: string[] = [];
  let i = 0;
  while (i < line.length) {
    if (line[i] === " " || line[i] === "\t") {
      i++;
      continue;
    }
    let tok = "";
    while (i < line.length && line[i] !== " " && line[i] !== "\t") {
      if (line[i] === '"') {
        const end = line.indexOf('"', i + 1);
        if (end < 0) throw new SpecError(`line ${no}: unclosed quote`);
        tok += line.slice(i + 1, end);
        i = end + 1;
      } else tok += line[i++];
    }
    out.push(tok);
  }
  return out;
}

export function parseSpec(source: string): Stmt[] {
  const out: Stmt[] = [];
  source.split(/\r?\n/).forEach((raw, idx) => {
    const line = raw.trim();
    if (!line || line.startsWith("#")) return;
    const [kind, ...rest] = tokens(line, idx + 1);
    const args: string[] = [];
    const opts: Record<string, string> = {};
    for (const t of rest) {
      const m = /^([a-z][a-z0-9_]*)=([\s\S]*)$/.exec(t);
      if (m) opts[m[1]] = m[2];
      else args.push(t);
    }
    out.push({ kind, args, opts, line: idx + 1 });
  });
  return out;
}

/** A number written as a constant expression ("2*pi", "-1.5"). */
export function constant(s: string | undefined, fallback: number, where: Stmt): number {
  if (s === undefined || s === "") return fallback;
  const v = expr(s, new Set(), where)({});
  if (!Number.isFinite(v)) throw new SpecError(`line ${where.line}: "${s}" is not a number`);
  return v;
}

/** Compile an expression and check it only uses names the tool will bind. */
export function expr(s: string | undefined, known: Set<string>, where: Stmt): Compiled {
  if (s === undefined || s === "") throw new SpecError(`line ${where.line}: ${where.kind} needs an expression`);
  try {
    const fn = compile(s);
    const bad = unknownVar(fn, known);
    if (bad) throw new SpecError(`line ${where.line}: unknown name "${bad}" in ${s}`);
    return fn;
  } catch (e) {
    if (e instanceof ExprError) throw new SpecError(`line ${where.line}: ${e.message}`);
    throw e;
  }
}

export type Slider = { name: string; min: number; max: number; value: number; step: number; label: string; animate: boolean };

export function sliderOf(st: Stmt): Slider {
  const [name, lo, hi, v] = st.args;
  if (!name || !/^[A-Za-z_][A-Za-z_0-9]*$/.test(name)) throw new SpecError(`line ${st.line}: slider needs a name`);
  const min = constant(lo, 0, st);
  const max = constant(hi, 1, st);
  if (!(max > min)) throw new SpecError(`line ${st.line}: slider max must be above min`);
  const value = constant(v, min, st);
  return {
    name,
    min,
    max,
    value: Math.min(max, Math.max(min, value)),
    step: constant(st.opts.step, (max - min) / 100, st),
    label: st.opts.label ?? `$${name}$`,
    animate: st.args.includes("animate"),
  };
}

/** Short, readable numbers for readouts and tick labels. */
export function fmtNum(v: number, digits = 3): string {
  if (!Number.isFinite(v)) return "—";
  if (Math.abs(v) < 1e-9) return "0";
  const a = Math.abs(v);
  if (a >= 1e5 || a < 1e-3) return v.toExponential(2);
  return String(Number(v.toPrecision(digits)));
}

export function niceStep(span: number, count: number): number {
  const raw = span / Math.max(1, count);
  const p = 10 ** Math.floor(Math.log10(raw));
  return [1, 2, 2.5, 5, 10].map((m) => m * p).find((s) => s >= raw) ?? p * 10;
}

export function ticks(min: number, max: number, count: number): number[] {
  const s = niceStep(max - min, count);
  const out: number[] = [];
  for (let v = Math.ceil(min / s - 1e-9) * s; v <= max + s * 1e-9; v += s) out.push(Math.abs(v) < s * 1e-9 ? 0 : v);
  return out;
}
