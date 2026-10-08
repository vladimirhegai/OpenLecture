import { Binary, Calculator, CircuitBoard, Gauge } from "lucide-react";
import { useEffect, useState } from "react";
import { api, course, type Artifact } from "../api";
import { Chart, fmt } from "./Chart";
import { Markdown, Tex } from "./Markdown";

const cache = new Map<string, Promise<Artifact>>();

function load(courseId: string, id: string) {
  if (!cache.has(id)) cache.set(id, api<Artifact>(`${course(courseId)}/artifacts/${id}`));
  return cache.get(id)!;
}

const SI: [number, string][] = [
  [1e9, "G"],
  [1e6, "M"],
  [1e3, "k"],
  [1, ""],
  [1e-3, "m"],
  [1e-6, "µ"],
  [1e-9, "n"],
];

function engineering(value: number, unit: string) {
  if (Math.abs(value) < 1e-15) return `0 ${unit}`;
  const [scale, prefix] = SI.find(([s]) => Math.abs(value) >= s * 0.9995) ?? SI[SI.length - 1];
  return `${Number((value / scale).toPrecision(4))} ${prefix}${unit}`;
}

function label(key: string) {
  const text = key.replace(/_/g, " ");
  return text.charAt(0).toUpperCase() + text.slice(1);
}

function Values({ values, unit, symbol }: { values: Record<string, unknown>; unit?: string; symbol?: string }) {
  return (
    <div className="kv">
      {Object.entries(values)
        .filter(([, value]) => typeof value === "number")
        .map(([key, value]) => (
          <div key={key}>
            <span>{symbol ? `${symbol}(${key})` : label(key)}</span>
            <strong>{unit ? engineering(value as number, unit) : fmt(value as number)}</strong>
          </div>
        ))}
    </div>
  );
}

function Body({ artifact }: { artifact: Artifact }) {
  const p = artifact.payload;
  if (artifact.kind === "simulation") {
    return (
      <>
        <Values values={Object.fromEntries(Object.entries(p.node_voltages ?? {}).filter(([n]) => n !== "0"))} unit="V" symbol="V" />
        <Values values={p.branch_currents ?? {}} unit="A" symbol="I" />
        <Values values={p.component_power ?? {}} unit="W" symbol="P" />
        <div className="artifact-caption">Currents follow the passive sign convention, positive to negative terminal.</div>
      </>
    );
  }
  if (artifact.kind === "circuit") {
    return <pre style={{ margin: 0, fontSize: 13 }}>{p.definition}</pre>;
  }
  if (p.card_type === "logic_truth_table") {
    const variables: string[] = p.parameters?.variables ?? [];
    return (
      <>
        {p.latex && <Tex latex={`F = ${p.latex}`} />}
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                {variables.map((v) => (
                  <th key={v}>{v}</th>
                ))}
                <th>F</th>
              </tr>
            </thead>
            <tbody>
              {(p.rows ?? []).map((row: { inputs: Record<string, number>; output: number }, i: number) => (
                <tr key={i}>
                  {variables.map((v) => (
                    <td key={v}>{row.inputs[v]}</td>
                  ))}
                  <td>
                    <strong>{row.output}</strong>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </>
    );
  }
  const chart = p.chart;
  const discrete = chart && chart.x.every((value: number) => Number.isInteger(value)) && chart.x.length <= 60;
  return (
    <>
      {p.formula_latex && <Tex latex={p.formula_latex} />}
      {!p.formula_latex && p.equation && <div className="artifact-caption">{p.equation}</div>}
      {p.outputs && <Values values={p.outputs} />}
      {chart?.x?.length > 1 && (
        <Chart x={chart.x} y={chart.y} xLabel={chart.x_label} yLabel={chart.y_label} kind={discrete ? "bar" : "line"} />
      )}
    </>
  );
}

const icons: Record<string, typeof Gauge> = {
  simulation: Gauge,
  circuit: CircuitBoard,
  logic_card: Binary,
  math_card: Calculator,
};

export function ArtifactCard({ courseId, id, caption }: { courseId: string; id: string; caption: string }) {
  const [artifact, setArtifact] = useState<Artifact | null>(null);
  const [error, setError] = useState<string | null>(null);
  useEffect(() => {
    load(courseId, id).then(setArtifact, (e) => {
      cache.delete(id);
      setError(e.message);
    });
  }, [courseId, id]);
  const Icon = icons[artifact?.kind ?? ""] ?? Calculator;
  return (
    <div className="artifact">
      <div className="artifact-head">
        <Icon size={16} />
        <strong>{artifact?.title ?? (error ? "Saved result unavailable" : "Loading result")}</strong>
        {artifact?.payload.verified && <span className="tag">Computed</span>}
      </div>
      <div className="artifact-body">
        {artifact ? <Body artifact={artifact} /> : error && <div className="artifact-caption">{error}</div>}
        {caption && <div className="artifact-caption"><Markdown text={caption} inline /></div>}
      </div>
    </div>
  );
}
