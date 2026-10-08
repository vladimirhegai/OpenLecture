import {
  AlertCircle,
  ArrowUp,
  Check,
  ChevronDown,
  Copy,
  FileText,
  LogIn,
  MessageSquare,
  PanelRightClose,
  Plus,
  Quote,
  Square,
  SquarePen,
  X,
} from "lucide-react";
import { useCallback, useEffect, useLayoutEffect, useRef, useState } from "react";
import {
  api,
  course as coursePath,
  relativeTime,
  runAgent,
  type Block,
  type Chat as ChatRecord,
  type Course,
  type DocumentReference,
  type DocumentSummary,
  type Message,
  type Provider,
} from "../api";
import { toolVerb } from "../labels";
import { Markdown } from "./Markdown";
import { ModelPicker, type Selection } from "./ModelPicker";
import { Popover, useToast } from "./ui";
import type { Ask } from "./Views";

export type Viewing =
  | { kind: "doc"; label: string; document_id: string; revision: number }
  | { kind: "source"; label: string; source_id: string; page?: number }
  | null;

type Segment = { kind: "tool"; name: string } | { kind: "text"; text: string };

function blockPreview(block: Block) {
  const text =
    "text" in block
      ? block.text
      : "latex" in block
        ? block.latex
        : "prompt" in block
          ? block.prompt
          : "title" in block
            ? block.title
            : "items" in block
              ? block.items.join(", ")
              : "caption" in block && block.caption
                ? block.caption
                : block.type.replace("_", " ");
  return text.length > 60 ? `${text.slice(0, 60)}…` : text;
}

function storedChat(courseId: string) {
  try {
    return localStorage.getItem(`ol-chat:${courseId}`);
  } catch {
    return null;
  }
}

function storeChat(courseId: string, chatId: string | null) {
  try {
    if (chatId) localStorage.setItem(`ol-chat:${courseId}`, chatId);
    else localStorage.removeItem(`ol-chat:${courseId}`);
  } catch {
    /* storage unavailable */
  }
}

export function Chat({
  course,
  docs,
  viewing,
  ask,
  providers,
  selection,
  onSelection,
  onSignIn,
  pending,
  onManage,
  onClose,
  onOpenReference,
}: {
  course: Course;
  docs: DocumentSummary[];
  viewing: Viewing;
  ask: (Ask & { nonce: number }) | null;
  providers: Provider[];
  selection: Selection;
  onSelection: (selection: Selection) => void;
  onSignIn: (provider: Provider["id"]) => void;
  pending: Provider["id"] | null;
  onManage: () => void;
  onClose: () => void;
  onOpenReference: (reference: DocumentReference) => void;
}) {
  const toast = useToast();
  const [chats, setChats] = useState<ChatRecord[]>([]);
  const [chatId, setChatId] = useState<string | null>(() => storedChat(course.id));
  const [messages, setMessages] = useState<Message[]>([]);
  const [draft, setDraft] = useState("");
  const [useContext, setUseContext] = useState(true);
  const [block, setBlock] = useState<Block | null>(null);
  const [segments, setSegments] = useState<Segment[] | null>(null);
  const [failure, setFailure] = useState<{ message: string; retry: string } | null>(null);
  const [copied, setCopied] = useState<string | null>(null);
  const abort = useRef<AbortController | null>(null);
  const skipLoad = useRef<string | null>(null);
  const thread = useRef<HTMLDivElement>(null);
  const input = useRef<HTMLTextAreaElement>(null);
  const pinned = useRef(true);
  const running = segments !== null;
  const ready = providers.some((p) => p.signed_in);
  const current = providers.find((p) => p.id === selection.provider);

  const loadChats = useCallback(() => {
    api<ChatRecord[]>(`${coursePath(course.id)}/chats?limit=100`).then(
      (list) => setChats([...list].sort((a, b) => b.created_at.localeCompare(a.created_at))),
      () => setChats([]),
    );
  }, [course.id]);

  useEffect(() => {
    abort.current?.abort();
    setChatId(storedChat(course.id));
    setFailure(null);
    setBlock(null);
    loadChats();
  }, [course.id, loadChats]);

  const loadMessages = useCallback(async (id: string) => {
    const all: Message[] = [];
    for (let after = 0; ; ) {
      const page = await api<Message[]>(`${coursePath(course.id)}/chats/${id}/messages?after=${after}&limit=100`);
      all.push(...page);
      if (page.length < 100) break;
      after = page[page.length - 1].sequence;
    }
    return all;
  }, [course.id]);

  useEffect(() => {
    storeChat(course.id, chatId);
    if (!chatId) {
      setMessages([]);
      return;
    }
    if (skipLoad.current === chatId) {
      skipLoad.current = null;
      return;
    }
    let live = true;
    loadMessages(chatId).then(
      (list) => live && setMessages(list),
      () => {
        if (!live) return;
        setChatId(null);
        setMessages([]);
      },
    );
    return () => {
      live = false;
    };
  }, [chatId, course.id, loadMessages]);

  // Messages written by other clients (for example an MCP agent) appear without a reload.
  useEffect(() => {
    const listener = (event: Event) => {
      const detail = (event as CustomEvent).detail;
      if (detail.type === "chat.message_added" && detail.payload.chat_id === chatId && !abort.current) {
        loadMessages(chatId!).then(setMessages, () => {});
      }
    };
    window.addEventListener("ol:event", listener);
    return () => window.removeEventListener("ol:event", listener);
  }, [chatId, loadMessages]);

  useLayoutEffect(() => {
    if (pinned.current && thread.current) thread.current.scrollTop = thread.current.scrollHeight;
  }, [messages, segments, failure]);

  useLayoutEffect(() => {
    const area = input.current;
    if (!area) return;
    area.style.height = "auto";
    area.style.height = `${Math.min(area.scrollHeight, 220)}px`;
  }, [draft]);

  useEffect(() => {
    if (viewing) setUseContext(true);
    setBlock(null);
  }, [viewing?.kind, viewing && (viewing.kind === "doc" ? viewing.document_id : viewing.source_id)]);

  const send = useCallback(
    async (textArg?: string, blockArg?: Block | null) => {
      const text = (textArg ?? draft).trim();
      if (!text || abort.current) return;
      if (!current?.signed_in) {
        setFailure({ message: `Sign in to ${current?.name ?? "an AI provider"} to start chatting.`, retry: text });
        return;
      }
      setFailure(null);
      pinned.current = true;
      let id = chatId;
      const controller = new AbortController();
      abort.current = controller;
      setSegments([]);
      const temp: Message = {
        id: `temp-${Date.now()}`,
        role: "user",
        content: text,
        sequence: 0,
        created_at: new Date().toISOString(),
        references: [],
      };
      setMessages((list) => [...list, temp]);
      setDraft("");
      try {
        if (!id) {
          const title = text.length > 60 ? `${text.slice(0, 57).trimEnd()}…` : text;
          const chat = await api<ChatRecord>(`${coursePath(course.id)}/chats`, { method: "POST", json: { title } });
          id = chat.id;
          skipLoad.current = id;
          setChats((list) => [chat, ...list]);
          setChatId(id);
        }
        const focus = blockArg === undefined ? block : blockArg;
        const body: Record<string, unknown> = {
          provider: selection.provider,
          model: selection.model,
          effort: selection.effort,
          content: text,
        };
        if (viewing && useContext) {
          if (viewing.kind === "doc")
            body.document = { document_id: viewing.document_id, revision: viewing.revision, block_id: focus?.id ?? null };
          else Object.assign(body, { source_id: viewing.source_id, source_page: viewing.page ?? null });
        }
        setBlock(null);
        for await (const event of runAgent(course.id, id, body, controller.signal)) {
          if (event.type === "user_message") setMessages((list) => list.map((m) => (m.id === temp.id ? event.message : m)));
          else if (event.type === "text_start") setSegments((list) => [...(list ?? []), { kind: "text", text: "" }]);
          else if (event.type === "text")
            setSegments((list) => {
              const next = [...(list ?? [])];
              const last = next[next.length - 1];
              if (last?.kind === "text") next[next.length - 1] = { kind: "text", text: last.text + event.delta };
              else next.push({ kind: "text", text: event.delta });
              return next;
            });
          else if (event.type === "tool") setSegments((list) => [...(list ?? []), { kind: "tool", name: event.name }]);
          else if (event.type === "done") setMessages((list) => [...list, event.message]);
          else if (event.type === "error") setFailure({ message: event.message, retry: text });
        }
      } catch (error) {
        if (controller.signal.aborted) toast("Stopped");
        else setFailure({ message: (error as Error).message, retry: text });
      } finally {
        abort.current = null;
        setSegments(null);
      }
    },
    [draft, chatId, course.id, selection, viewing, useContext, block, current, toast],
  );

  useEffect(() => {
    if (!ask) return;
    if (ask.block) {
      setBlock(ask.block);
      setUseContext(true);
    }
    if (ask.text && ask.send) send(ask.text, ask.block ?? null);
    else if (ask.text) setDraft(ask.text);
    setTimeout(() => input.current?.focus(), 50);
    // Only react to a new request.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [ask?.nonce]);

  function newChat() {
    abort.current?.abort();
    setChatId(null);
    setMessages([]);
    setFailure(null);
    setTimeout(() => input.current?.focus(), 30);
  }

  function copy(message: Message) {
    navigator.clipboard.writeText(message.content).then(() => {
      setCopied(message.id);
      setTimeout(() => setCopied(null), 1400);
    });
  }

  const title = chats.find((chat) => chat.id === chatId)?.title ?? "New chat";
  const suggestions =
    viewing?.kind === "doc"
      ? ["Summarize this note in five bullet points.", "Quiz me on this note, one question at a time.", "What's the hardest idea here? Explain it simply."]
      : viewing?.kind === "source" && viewing.page
        ? ["Summarize this page.", "Explain the key equations on this page.", "What on this page is likely to be tested?"]
        : viewing?.kind === "source"
          ? ["Summarize this file.", "Explain the key ideas in this file.", "Make practice questions from this file."]
        : ["What are the main topics in this course?", "Make a study plan for the next two weeks.", "Which parts of this course build on each other?"];
  const lastText = segments?.filter((s) => s.kind === "text").at(-1);

  return (
    <aside className="chat" aria-label="Chat">
      <div className="chat-head">
        <Popover
          wrapStyle={{ flex: 1, minWidth: 0 }}
          style={{ left: 0, top: 36, width: 300 }}
          trigger={({ toggle, open }) => (
            <button className="chat-title" onClick={toggle} aria-expanded={open} style={{ width: "100%" }}>
              <span>{title}</span>
              <ChevronDown size={14} />
            </button>
          )}
        >
          {(close) => (
            <>
              <button
                className="menu-item"
                onClick={() => {
                  newChat();
                  close();
                }}
              >
                <Plus size={16} />
                <span className="grow">New chat</span>
              </button>
              {chats.length > 0 && <div className="menu-sep" />}
              <div style={{ maxHeight: 320, overflowY: "auto" }}>
                {chats.map((chat) => (
                  <button
                    key={chat.id}
                    className="menu-item"
                    onClick={() => {
                      setChatId(chat.id);
                      setFailure(null);
                      close();
                    }}
                  >
                    <MessageSquare size={16} />
                    <span className="grow">
                      <span style={{ display: "block", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{chat.title}</span>
                      <span className="sub">{relativeTime(chat.created_at)}</span>
                    </span>
                    {chat.id === chatId && <Check size={15} className="check" />}
                  </button>
                ))}
              </div>
            </>
          )}
        </Popover>
        <button className="icon-btn" onClick={newChat} title="New chat" aria-label="New chat">
          <SquarePen size={17} />
        </button>
        <button className="icon-btn" onClick={onClose} title="Close chat (Ctrl+J)" aria-label="Close chat">
          <span className="desktop-only" style={{ display: "contents" }}>
            <PanelRightClose size={17} />
          </span>
          <span className="mobile-only" style={{ display: "contents" }}>
            <X size={18} />
          </span>
        </button>
      </div>

      <div
        className="thread"
        ref={thread}
        onScroll={(e) => {
          const el = e.currentTarget;
          pinned.current = el.scrollHeight - el.scrollTop - el.clientHeight < 80;
        }}
      >
        {messages.length === 0 && !running && (
          <div className="chat-empty">
            {ready ? (
              <>
                <h3>Ask about {course.code}</h3>
                <p>Answers come from your course material, with page citations. Notes are only written when you ask.</p>
                <div className="prompts">
                  {suggestions.map((s) => (
                    <button key={s} className="prompt-chip" onClick={() => send(s)}>
                      {s}
                    </button>
                  ))}
                </div>
              </>
            ) : (
              <>
                <h3>Connect an AI</h3>
                <p>
                  Open Lecture uses the Claude Code or Codex app on this computer, so chats run on your own subscription.
                  Sign-in happens in a terminal window that opens for you.
                </p>
                <div className="connect">
                  {providers.map((p) => (
                    <button key={p.id} className="btn" onClick={() => onSignIn(p.id)} disabled={!p.installed || pending === p.id}>
                      {pending === p.id ? <span className="spinner" /> : <LogIn size={15} />}
                      {!p.installed ? `${p.name} isn't installed` : pending === p.id ? "Waiting for sign-in" : `Sign in to ${p.name}`}
                    </button>
                  ))}
                </div>
              </>
            )}
          </div>
        )}

        {messages.map((message) =>
          message.role === "user" ? (
            <div key={message.id} className="msg user">
              <div className="bubble">{message.content}</div>
              {message.references.map((reference) => (
                <button key={reference.document_id} className="msg-ref" onClick={() => onOpenReference(reference)}>
                  <FileText size={12} />
                  {docs.find((d) => d.document_id === reference.document_id)?.title ?? "Note"}
                </button>
              ))}
            </div>
          ) : (
            <div key={message.id} className="msg">
              <div className="chat-md">
                <Markdown text={message.content} />
              </div>
              <div className="msg-actions">
                <button className="icon-btn" onClick={() => copy(message)} title="Copy" aria-label="Copy answer">
                  {copied === message.id ? <Check size={14} /> : <Copy size={14} />}
                </button>
              </div>
            </div>
          ),
        )}

        {running && (
          <div className="msg">
            <div className="activity">
              {segments.map((segment, i) =>
                segment.kind === "tool" ? (
                  <div key={i} className="activity-row">
                    {i === segments.length - 1 ? <span className="spinner" /> : <Check size={14} />}
                    {toolVerb(segment.name)}
                  </div>
                ) : segment !== lastText ? (
                  segment.text.trim() && (
                    <div key={i} className="chat-md interim">
                      <Markdown text={segment.text} />
                    </div>
                  )
                ) : null,
              )}
              {segments.length === 0 && (
                <div className="activity-row">
                  <span className="spinner" />
                  Thinking
                </div>
              )}
            </div>
            {lastText && lastText.text.trim() && (
              <div className="chat-md">
                <Markdown text={lastText.text} />
              </div>
            )}
          </div>
        )}

        {failure && (
          <div className="msg">
            <div className="msg-error">
              <AlertCircle size={15} />
              <div style={{ flex: 1 }}>
                {failure.message}
                <div style={{ display: "flex", gap: 6, marginTop: 8 }}>
                  {/sign.?in|log.?in|auth|logged/i.test(failure.message) && current?.installed ? (
                    <button className="btn" style={{ height: 28 }} onClick={() => onSignIn(selection.provider)}>
                      Sign in to {current.name}
                    </button>
                  ) : (
                    <button className="btn" style={{ height: 28 }} onClick={() => send(failure.retry)}>
                      Try again
                    </button>
                  )}
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      <div className="composer-wrap">
        <div className="composer">
          {block ? (
            <div className="context-chip">
              <Quote size={13} />
              <span>{blockPreview(block)}</span>
              <button className="icon-btn" onClick={() => setBlock(null)} aria-label="Remove quoted block">
                <X size={13} />
              </button>
            </div>
          ) : (
            viewing && (
              <div className={`context-chip ${useContext ? "" : "off"}`}>
                <FileText size={13} />
                <span>{viewing.label}</span>
                <button
                  className="icon-btn"
                  onClick={() => setUseContext(!useContext)}
                  aria-label={useContext ? "Don't include what I'm viewing" : "Include what I'm viewing"}
                  title={useContext ? "Don't include" : "Include"}
                >
                  {useContext ? <X size={13} /> : <Plus size={13} />}
                </button>
              </div>
            )
          )}
          <textarea
            ref={input}
            rows={1}
            value={draft}
            placeholder={ready ? `Ask about ${course.code}` : "Sign in to an AI to start"}
            aria-label="Message"
            onChange={(e) => setDraft(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
                e.preventDefault();
                send();
              }
            }}
          />
          <div className="composer-bar">
            <ModelPicker
              providers={providers}
              selection={selection}
              onChange={onSelection}
              onSignIn={onSignIn}
              onManage={onManage}
              pending={pending}
            />
            <span className="grow" />
            {running ? (
              <button className="send stop" onClick={() => abort.current?.abort()} aria-label="Stop" title="Stop">
                <Square size={11} fill="currentColor" />
              </button>
            ) : (
              <button className="send" onClick={() => send()} disabled={!draft.trim()} aria-label="Send" title="Send (Enter)">
                <ArrowUp size={16} />
              </button>
            )}
          </div>
        </div>
      </div>
    </aside>
  );
}
