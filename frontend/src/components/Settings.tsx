import { Copy, LogIn, LogOut, Monitor, Moon, RefreshCw, Sun } from "lucide-react";
import { useEffect, useState } from "react";
import { api, type AppSettings, type ModelChoice, type Provider } from "../api";
import type { ThemePref } from "../theme";
import { effortName, type Selection } from "./ModelPicker";
import { Confirm, Dialog, useToast } from "./ui";

const INSTALL = {
  claude: "https://code.claude.com/docs/en/setup",
  codex: "https://developers.openai.com/codex/cli",
};

export function Settings({
  onClose,
  theme,
  onTheme,
  providers,
  onRefresh,
  refreshing,
  selection,
  onSelection,
  onSignIn,
  onSignOut,
  pending,
  manualCommand,
}: {
  onClose: () => void;
  theme: ThemePref;
  onTheme: (theme: ThemePref) => void;
  providers: Provider[];
  onRefresh: () => void;
  refreshing: boolean;
  selection: Selection;
  onSelection: (selection: Selection) => void;
  onSignIn: (provider: Provider["id"]) => void;
  onSignOut: (provider: Provider["id"]) => void;
  pending: Provider["id"] | null;
  manualCommand: string | null;
}) {
  const toast = useToast();
  const [confirm, setConfirm] = useState<Provider | null>(null);
  const [version, setVersion] = useState<string | null>(null);
  const [reading, setReading] = useState<ModelChoice | null>(null);
  useEffect(() => {
    api<{ version: string }>("/health").then((h) => setVersion(h.version), () => {});
    api<AppSettings>("/settings").then((s) => setReading(s.reading_model), () => {});
  }, []);

  function saveReading(next: ModelChoice) {
    setReading(next);
    api<AppSettings>("/settings", { method: "PUT", json: { reading_model: next } }).then(
      () => toast("Source reading model saved"),
      (e) => toast(e.message),
    );
  }
  const provider = providers.find((p) => p.id === selection.provider);
  const model = provider?.models.find((m) => m.id === selection.model);

  function describe(p: Provider) {
    if (!p.installed) return `${p.id === "claude" ? "Claude Code" : "Codex"} CLI isn't installed on this computer`;
    if (pending === p.id) return "Finish signing in in the terminal window";
    if (!p.signed_in) return "Not signed in";
    const cli = p.version ? ` · ${p.id === "claude" ? "Claude Code" : "Codex CLI"} ${p.version}` : "";
    if (p.account) return `${p.account}${p.plan ? `, ${p.plan} plan` : ""}${cli}`;
    return (p.method ? `Signed in with ${p.method}` : "Signed in") + cli;
  }

  return (
    <Dialog title="Settings" onClose={onClose} wide>
      <div className="dialog-body">
        <section className="settings-section">
          <h3>Appearance</h3>
          <div className="segmented" role="radiogroup" aria-label="Theme">
            {(
              [
                ["system", Monitor, "System"],
                ["light", Sun, "Light"],
                ["dark", Moon, "Dark"],
              ] as const
            ).map(([value, Icon, label]) => (
              <button key={value} role="radio" aria-checked={theme === value} aria-pressed={theme === value} onClick={() => onTheme(value)}>
                <Icon size={14} /> {label}
              </button>
            ))}
          </div>
        </section>

        <section className="settings-section">
          <div style={{ display: "flex", alignItems: "center" }}>
            <h3 style={{ flex: 1, margin: 0 }}>AI accounts</h3>
            <button className="icon-btn" onClick={onRefresh} title="Check again" aria-label="Check sign-in status again">
              {refreshing ? <span className="spinner" /> : <RefreshCw size={15} />}
            </button>
          </div>
          <p style={{ margin: "4px 0 10px", fontSize: 13 }}>
            Chats run through the Claude Code and Codex apps on this computer, using their own sign-in. Open Lecture never sees your password or tokens.
          </p>
          {providers.map((p) => (
            <div className="row" key={p.id}>
              <div className="grow">
                <div className="name">
                  {p.name}
                  {p.signed_in && <span className="presence on" title="Signed in" />}
                </div>
                <div className="sub">{describe(p)}</div>
              </div>
              {!p.installed && (
                <a className="btn" href={INSTALL[p.id]} target="_blank" rel="noreferrer">
                  How to install
                </a>
              )}
              {p.installed &&
                (p.signed_in ? (
                  <button className="btn" onClick={() => setConfirm(p)}>
                    <LogOut size={15} /> Sign out
                  </button>
                ) : (
                  <button className="btn primary" onClick={() => onSignIn(p.id)} disabled={pending === p.id}>
                    {pending === p.id ? <span className="spinner" /> : <LogIn size={15} />}
                    {pending === p.id ? "Waiting" : "Sign in"}
                  </button>
                ))}
            </div>
          ))}
          {manualCommand && (
            <div style={{ marginTop: 12, fontSize: 13, color: "var(--ink-2)" }}>
              A terminal couldn't be opened automatically. Run this in a terminal, then select Check again:
              <div className="cmd">
                <code>{manualCommand}</code>
                <button
                  className="icon-btn"
                  aria-label="Copy command"
                  onClick={() => navigator.clipboard.writeText(manualCommand).then(() => toast("Command copied"))}
                >
                  <Copy size={14} />
                </button>
              </div>
            </div>
          )}
        </section>

        <section className="settings-section">
          <h3>Chat model</h3>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1.4fr 1fr", gap: 8 }}>
            <label className="field">
              <span>Provider</span>
              <select
                className="input"
                value={selection.provider}
                onChange={(e) => onSelection({ provider: e.target.value as Provider["id"], model: "default", effort: null })}
              >
                {providers.map((p) => (
                  <option key={p.id} value={p.id}>
                    {p.name}
                  </option>
                ))}
              </select>
            </label>
            <label className="field" style={{ marginTop: 0 }}>
              <span>Model</span>
              <select
                className="input"
                value={selection.model}
                onChange={(e) => {
                  const next = provider?.models.find((m) => m.id === e.target.value);
                  onSelection({
                    ...selection,
                    model: e.target.value,
                    effort: selection.effort && next?.efforts.includes(selection.effort) ? selection.effort : null,
                  });
                }}
              >
                {provider?.models.map((m) => (
                  <option key={m.id} value={m.id}>
                    {m.label}
                  </option>
                ))}
              </select>
            </label>
            <label className="field" style={{ marginTop: 0 }}>
              <span>Effort</span>
              <select
                className="input"
                value={selection.effort ?? ""}
                disabled={!model?.efforts.length}
                onChange={(e) => onSelection({ ...selection, effort: e.target.value || null })}
              >
                <option value="">Auto</option>
                {model?.efforts.map((effort) => (
                  <option key={effort} value={effort}>
                    {effortName(effort)}
                  </option>
                ))}
              </select>
            </label>
          </div>
          <p style={{ margin: "8px 0 0", fontSize: 12.5, color: "var(--ink-3)" }}>
            Used for chat and for writing weekly notes. You can also switch from the chat box at any time.
          </p>
        </section>

        {reading && (
          <section className="settings-section">
            <h3>Source reading model</h3>
            <p style={{ margin: "0 0 10px", fontSize: 13 }}>
              Every uploaded PDF or image is read page by page from page images, including handwriting and circuit diagrams. The
              AI and your notes use these readings instead of the raw PDF text.
            </p>
            <ModelSelects providers={providers} value={reading} onChange={saveReading} />
          </section>
        )}

        <section className="settings-section">
          <h3>About</h3>
          <dl className="dl">
            <dt>Version</dt>
            <dd>{version ?? "Unknown"}</dd>
            <dt>Storage</dt>
            <dd>Local, on this computer</dd>
            <dt>Developer API</dt>
            <dd>
              <a href="/docs" target="_blank" rel="noreferrer" style={{ color: "var(--accent-text)" }}>
                Open API reference
              </a>
            </dd>
          </dl>
        </section>
      </div>
      {confirm && (
        <Confirm
          title={`Sign out of ${confirm.name}?`}
          body={`This signs out the ${confirm.id === "claude" ? "Claude Code" : "Codex"} app on this computer, not just Open Lecture. Other apps using it will need you to sign in again.`}
          action="Sign out"
          danger
          onConfirm={() => onSignOut(confirm.id)}
          onClose={() => setConfirm(null)}
        />
      )}
    </Dialog>
  );
}

function ModelSelects({
  providers,
  value,
  onChange,
}: {
  providers: Provider[];
  value: ModelChoice;
  onChange: (value: ModelChoice) => void;
}) {
  const provider = providers.find((p) => p.id === value.provider);
  const model = provider?.models.find((m) => m.id === value.model);
  return (
    <div style={{ display: "grid", gridTemplateColumns: "1fr 1.4fr 1fr", gap: 8 }}>
      <label className="field">
        <span>Provider</span>
        <select
          className="input"
          value={value.provider}
          onChange={(e) => onChange({ provider: e.target.value as Provider["id"], model: "default", effort: null })}
        >
          {providers.map((p) => (
            <option key={p.id} value={p.id}>
              {p.name}
            </option>
          ))}
        </select>
      </label>
      <label className="field" style={{ marginTop: 0 }}>
        <span>Model</span>
        <select
          className="input"
          value={value.model}
          onChange={(e) => {
            const next = provider?.models.find((m) => m.id === e.target.value);
            onChange({ ...value, model: e.target.value, effort: value.effort && next?.efforts.includes(value.effort) ? value.effort : null });
          }}
        >
          {provider?.models.map((m) => (
            <option key={m.id} value={m.id}>
              {m.label}
            </option>
          ))}
          {provider && !provider.models.some((m) => m.id === value.model) && <option value={value.model}>{value.model}</option>}
        </select>
      </label>
      <label className="field" style={{ marginTop: 0 }}>
        <span>Effort</span>
        <select className="input" value={value.effort ?? ""} onChange={(e) => onChange({ ...value, effort: e.target.value || null })}>
          <option value="">Auto</option>
          {(model?.efforts ?? (value.effort ? [value.effort] : [])).map((effort) => (
            <option key={effort} value={effort}>
              {effortName(effort)}
            </option>
          ))}
        </select>
      </label>
    </div>
  );
}
