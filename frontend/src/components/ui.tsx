import { X } from "lucide-react";
import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useRef,
  useState,
  type CSSProperties,
  type ReactNode,
} from "react";

/** Close on outside pointer-down or Escape. */
export function useDismiss(open: boolean, onClose: () => void, ref: React.RefObject<HTMLElement | null>) {
  useEffect(() => {
    if (!open) return;
    const down = (event: PointerEvent) => {
      if (ref.current && !ref.current.contains(event.target as Node)) onClose();
    };
    const key = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        event.stopPropagation();
        onClose();
      }
    };
    document.addEventListener("pointerdown", down);
    document.addEventListener("keydown", key);
    return () => {
      document.removeEventListener("pointerdown", down);
      document.removeEventListener("keydown", key);
    };
  }, [open, onClose, ref]);
}

/** A trigger plus an anchored popover. ``render`` receives a close callback. */
export function Popover({
  trigger,
  children,
  style,
  className = "",
  wrapStyle,
}: {
  trigger: (props: { open: boolean; toggle: () => void }) => ReactNode;
  children: (close: () => void) => ReactNode;
  style?: CSSProperties;
  className?: string;
  wrapStyle?: CSSProperties;
}) {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);
  const close = useCallback(() => setOpen(false), []);
  useDismiss(open, close, ref);
  return (
    <div ref={ref} style={{ position: "relative", ...wrapStyle }}>
      {trigger({ open, toggle: () => setOpen((value) => !value) })}
      {open && (
        <div className={`popover ${className}`} style={style} role="menu">
          {children(close)}
        </div>
      )}
    </div>
  );
}

export function Dialog({
  title,
  onClose,
  children,
  wide,
  className = "",
  bare,
}: {
  title?: string;
  onClose: () => void;
  children: ReactNode;
  wide?: boolean;
  className?: string;
  bare?: boolean;
}) {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const previous = document.activeElement as HTMLElement | null;
    // Prefer the first field, then the primary action, before falling back to any button.
    const first = ["input:not([type=hidden])", "textarea", "button.primary", "button"]
      .map((selector) => ref.current?.querySelector<HTMLElement>(selector))
      .find(Boolean);
    first?.focus();
    const key = (event: KeyboardEvent) => event.key === "Escape" && onClose();
    document.addEventListener("keydown", key);
    return () => {
      document.removeEventListener("keydown", key);
      previous?.focus?.();
    };
  }, [onClose]);
  return (
    <div className="scrim" onPointerDown={(event) => event.target === event.currentTarget && onClose()}>
      <div
        ref={ref}
        className={`dialog ${wide ? "wide" : ""} ${className}`}
        role="dialog"
        aria-modal="true"
        aria-label={title}
      >
        {!bare && (
          <div className="dialog-head">
            <h2>{title}</h2>
            <button className="icon-btn" onClick={onClose} aria-label="Close">
              <X size={16} />
            </button>
          </div>
        )}
        {children}
      </div>
    </div>
  );
}

export function Confirm({
  title,
  body,
  action,
  danger,
  onConfirm,
  onClose,
}: {
  title: string;
  body: ReactNode;
  action: string;
  danger?: boolean;
  onConfirm: () => void;
  onClose: () => void;
}) {
  return (
    <Dialog title={title} onClose={onClose}>
      <div className="dialog-body">
        <p>{body}</p>
        <div className="dialog-actions">
          <button className="btn" onClick={onClose}>
            Cancel
          </button>
          <button
            className={`btn ${danger ? "danger" : "primary"}`}
            onClick={() => {
              onConfirm();
              onClose();
            }}
          >
            {action}
          </button>
        </div>
      </div>
    </Dialog>
  );
}

type Toast = { id: number; text: string; action?: { label: string; run: () => void } };
const ToastContext = createContext<(text: string, action?: Toast["action"]) => void>(() => {});
export const useToast = () => useContext(ToastContext);

export function Toasts({ children }: { children: ReactNode }) {
  const [toasts, setToasts] = useState<Toast[]>([]);
  const push = useCallback((text: string, action?: Toast["action"]) => {
    const id = Date.now() + Math.random();
    setToasts((list) => [...list.slice(-2), { id, text, action }]);
    setTimeout(() => setToasts((list) => list.filter((toast) => toast.id !== id)), action ? 7000 : 3500);
  }, []);
  return (
    <ToastContext.Provider value={push}>
      {children}
      <div className="toasts" role="status" aria-live="polite">
        {toasts.map((toast) => (
          <div className="toast" key={toast.id}>
            <span>{toast.text}</span>
            {toast.action && (
              <button
                onClick={() => {
                  toast.action!.run();
                  setToasts((list) => list.filter((item) => item.id !== toast.id));
                }}
              >
                {toast.action.label}
              </button>
            )}
          </div>
        ))}
      </div>
    </ToastContext.Provider>
  );
}

export function BrandMark({ className = "brand-mark" }: { className?: string }) {
  return (
    <svg className={className} viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <rect x="4" y="2.5" width="16" height="19" rx="3" stroke="currentColor" strokeWidth="1.8" />
      <path
        d="M7.5 12.5c1.2 0 1.6-3 2.8-3s1.6 6 2.9 6 1.6-3 2.8-3"
        stroke="currentColor"
        strokeWidth="1.8"
        strokeLinecap="round"
      />
    </svg>
  );
}
