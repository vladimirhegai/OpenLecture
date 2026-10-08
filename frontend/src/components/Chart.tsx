import { useMemo, useState } from "react";

const W = 560;
const H = 200;
const PAD = { top: 12, right: 12, bottom: 34, left: 46 };

function niceTicks(min: number, max: number, count = 4) {
  if (min === max) return [min];
  const span = max - min;
  const step = 10 ** Math.floor(Math.log10(span / count));
  const unit = [1, 2, 2.5, 5, 10].map((m) => m * step).find((s) => span / s <= count) ?? step * 10;
  const ticks = [];
  for (let value = Math.ceil(min / unit) * unit; value <= max + unit * 1e-9; value += unit) ticks.push(value);
  return ticks;
}

export function fmt(value: number) {
  if (!Number.isFinite(value)) return String(value);
  if (value === 0) return "0";
  const abs = Math.abs(value);
  if (abs >= 1e5 || abs < 1e-3) return value.toExponential(2);
  return Number(value.toPrecision(4)).toString();
}

/** Single-series chart: bars for discrete outcomes, a 2px line for trajectories. */
export function Chart({
  x,
  y,
  xLabel,
  yLabel,
  kind,
}: {
  x: number[];
  y: number[];
  xLabel?: string;
  yLabel?: string;
  kind: "bar" | "line";
}) {
  const [hover, setHover] = useState<number | null>(null);
  const geometry = useMemo(() => {
    const yMax = Math.max(0, ...y);
    const yMin = Math.min(0, ...y);
    const yTicks = niceTicks(yMin, yMax);
    const top = Math.max(yMax, yTicks[yTicks.length - 1] ?? yMax);
    const bottom = Math.min(yMin, yTicks[0] ?? yMin);
    const xMin = Math.min(...x);
    const xMax = Math.max(...x);
    const innerW = W - PAD.left - PAD.right;
    const innerH = H - PAD.top - PAD.bottom;
    const band = innerW / x.length;
    const px = (index: number) =>
      kind === "bar"
        ? PAD.left + band * (index + 0.5)
        : PAD.left + (xMax === xMin ? innerW / 2 : ((x[index] - xMin) / (xMax - xMin)) * innerW);
    const py = (value: number) => PAD.top + innerH - ((value - bottom) / (top - bottom || 1)) * innerH;
    return { yTicks, px, py, band, innerW, xTicks: kind === "bar" ? x : niceTicks(xMin, xMax, 5), xMin, xMax };
  }, [x, y, kind]);
  const { yTicks, px, py, band, xTicks, xMin, xMax, innerW } = geometry;
  const zero = py(0);
  const barWidth = Math.max(2, Math.min(28, band * 0.62));
  const xTickPos = (value: number) =>
    kind === "bar" ? px(x.indexOf(value)) : PAD.left + ((value - xMin) / (xMax - xMin || 1)) * innerW;

  function bar(index: number) {
    const cx = px(index);
    const yv = py(y[index]);
    const height = Math.abs(zero - yv);
    const r = Math.min(4, barWidth / 2, height);
    const left = cx - barWidth / 2;
    const right = cx + barWidth / 2;
    if (height < 0.5) return `M${left},${zero}H${right}`;
    return `M${left},${zero}V${yv + r}Q${left},${yv} ${left + r},${yv}H${right - r}Q${right},${yv} ${right},${yv + r}V${zero}Z`;
  }

  const line = x.map((_, i) => `${i ? "L" : "M"}${px(i).toFixed(1)},${py(y[i]).toFixed(1)}`).join("");

  function onMove(event: React.PointerEvent<SVGRectElement>) {
    const rect = event.currentTarget.ownerSVGElement!.getBoundingClientRect();
    const svgX = ((event.clientX - rect.left) / rect.width) * W;
    let best = 0;
    for (let i = 1; i < x.length; i++) if (Math.abs(px(i) - svgX) < Math.abs(px(best) - svgX)) best = i;
    setHover(best);
  }

  return (
    <figure className="chart" style={{ margin: 0 }}>
      <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={`${yLabel ?? "y"} by ${xLabel ?? "x"}`}>
        {yTicks.map((tick) => (
          <g key={tick}>
            <line className="grid" x1={PAD.left} x2={W - PAD.right} y1={py(tick)} y2={py(tick)} />
            <text x={PAD.left - 8} y={py(tick) + 4} textAnchor="end">
              {fmt(tick)}
            </text>
          </g>
        ))}
        <line className="axis" x1={PAD.left} x2={W - PAD.right} y1={zero} y2={zero} />
        {xTicks
          .filter((_, i, all) => all.length <= 12 || i % Math.ceil(all.length / 12) === 0)
          .map((tick) => (
            <text key={tick} x={xTickPos(tick)} y={H - PAD.bottom + 16} textAnchor="middle">
              {fmt(tick)}
            </text>
          ))}
        {xLabel && (
          <text x={PAD.left + innerW / 2} y={H - 2} textAnchor="middle">
            {xLabel}
          </text>
        )}
        {kind === "bar" ? (
          x.map((_, i) => <path key={i} className="mark" d={bar(i)} opacity={hover === null || hover === i ? 1 : 0.55} />)
        ) : (
          <path className="line" d={line} />
        )}
        {kind === "line" && hover !== null && (
          <>
            <line className="crosshair" x1={px(hover)} x2={px(hover)} y1={PAD.top} y2={H - PAD.bottom} />
            <circle className="dot" cx={px(hover)} cy={py(y[hover])} r={4.5} />
          </>
        )}
        <rect
          className="hit"
          x={PAD.left}
          y={PAD.top}
          width={innerW}
          height={H - PAD.top - PAD.bottom}
          onPointerMove={onMove}
          onPointerLeave={() => setHover(null)}
        />
      </svg>
      {hover !== null && (
        <div
          className="tooltip"
          style={{ left: `${(px(hover) / W) * 100}%`, top: `${(py(y[hover]) / H) * 100}%` }}
        >
          <span>{xLabel ?? "x"} </span>
          {fmt(x[hover])}
          <br />
          <span>{yLabel ?? "y"} </span>
          {fmt(y[hover])}
        </div>
      )}
    </figure>
  );
}
