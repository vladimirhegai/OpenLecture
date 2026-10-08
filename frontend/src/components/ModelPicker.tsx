import { Check, ChevronDown, LogIn, Settings2 } from "lucide-react";
import type { Provider } from "../api";
import { prettyModel } from "../labels";
import { Popover } from "./ui";

export type Selection = { provider: "claude" | "codex"; model: string; effort: string | null };

export function defaultModelName(provider: Provider | undefined) {
  if (!provider?.default_model) return null;
  return provider.models.find((m) => m.id === provider.default_model)?.label ?? prettyModel(provider.default_model);
}

export function modelLabel(providers: Provider[], selection: Selection) {
  const provider = providers.find((p) => p.id === selection.provider);
  const model = provider?.models.find((m) => m.id === selection.model);
  const name = provider?.name ?? selection.provider;
  const label = !model || model.id === "default" ? defaultModelName(provider) : model.label;
  if (!label) return name;
  return selection.provider === "codex" ? label : `${name} ${label}`;
}

const EFFORT_NAMES: Record<string, string> = { xhigh: "Extra high", max: "Max", ultra: "Ultra" };
export const effortName = (effort: string) => EFFORT_NAMES[effort] ?? effort.charAt(0).toUpperCase() + effort.slice(1);

export function ModelPicker({
  providers,
  selection,
  onChange,
  onSignIn,
  onManage,
  pending,
}: {
  providers: Provider[];
  selection: Selection;
  onChange: (selection: Selection) => void;
  onSignIn: (provider: Provider["id"]) => void;
  onManage: () => void;
  pending: Provider["id"] | null;
}) {
  const provider = providers.find((p) => p.id === selection.provider);
  const model = provider?.models.find((m) => m.id === selection.model) ?? provider?.models[0];

  return (
    <Popover
      className="picker"
      style={{ left: 0, bottom: 36 }}
      trigger={({ toggle, open }) => (
        <button className="model-btn" onClick={toggle} aria-expanded={open} aria-haspopup="menu" title="Choose model">
          <span>{modelLabel(providers, selection)}</span>
          {selection.effort && <span style={{ color: "var(--ink-3)", fontWeight: 400 }}>{effortName(selection.effort)}</span>}
          <ChevronDown size={14} />
        </button>
      )}
    >
      {(close) => (
        <>
          <div className="segmented" role="tablist" aria-label="Provider">
            {providers.map((p) => (
              <button
                key={p.id}
                role="tab"
                aria-pressed={p.id === selection.provider}
                onClick={() => onChange({ provider: p.id, model: "default", effort: null })}
              >
                {p.signed_in && <span className="presence on" />}
                {p.name}
              </button>
            ))}
          </div>

          {provider && !provider.installed && (
            <div className="picker-note">
              The {provider.name} CLI isn't installed on this computer. Install it, then reopen this menu.
            </div>
          )}
          {provider && provider.installed && !provider.signed_in && (
            <div className="picker-note">
              <p style={{ margin: "0 0 10px" }}>Sign in to use {provider.name} models with your own account.</p>
              <button className="btn primary" style={{ width: "100%" }} onClick={() => onSignIn(provider.id)} disabled={pending === provider.id}>
                {pending === provider.id ? <span className="spinner" /> : <LogIn size={15} />}
                {pending === provider.id ? "Waiting for sign-in" : `Sign in to ${provider.name}`}
              </button>
            </div>
          )}
          {provider?.signed_in && (
            <>
              <div className="menu-label">Model</div>
              <div style={{ maxHeight: 260, overflowY: "auto" }}>
                {provider.models.map((m) => (
                  <button
                    key={m.id}
                    className="menu-item"
                    role="menuitemradio"
                    aria-checked={m.id === model?.id}
                    onClick={() =>
                      onChange({
                        provider: provider.id,
                        model: m.id,
                        effort: selection.effort && m.efforts.includes(selection.effort) ? selection.effort : null,
                      })
                    }
                  >
                    <span className="grow">
                      {m.label}
                      {m.id === "default" && (
                        <span className="sub">
                          {defaultModelName(provider)
                            ? `${defaultModelName(provider)}, from your ${provider.name} settings`
                            : `Uses your ${provider.name} CLI setting`}
                        </span>
                      )}
                    </span>
                    {m.id === model?.id && <Check size={15} className="check" />}
                  </button>
                ))}
              </div>
              {model && model.efforts.length > 0 && (
                <>
                  <div className="menu-label">Effort</div>
                  <div className="efforts">
                    <button className="effort" aria-pressed={selection.effort === null} onClick={() => onChange({ ...selection, effort: null })}>
                      Auto
                    </button>
                    {model.efforts.map((effort) => (
                      <button key={effort} className="effort" aria-pressed={selection.effort === effort} onClick={() => onChange({ ...selection, effort })}>
                        {effortName(effort)}
                      </button>
                    ))}
                  </div>
                </>
              )}
            </>
          )}
          <div className="menu-sep" />
          <button
            className="menu-item"
            onClick={() => {
              close();
              onManage();
            }}
          >
            <Settings2 size={16} />
            <span className="grow">Manage accounts</span>
          </button>
        </>
      )}
    </Popover>
  );
}
