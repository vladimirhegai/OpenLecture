const TOOL_VERBS: [RegExp, string][] = [
  [/^source search/, "Searching course sources"],
  [/^source read/, "Reading a source"],
  [/^source page/, "Looking at a page"],
  [/^source list/, "Listing sources"],
  [/^document (read|find)/, "Reading notes"],
  [/^document plan/, "Planning a note"],
  [/^document create/, "Writing a note"],
  [/^document (update|edit)/, "Editing a note"],
  [/^document list revisions/, "Checking note history"],
  [/^context/, "Gathering context"],
  [/^course study guidance|^study skill/, "Checking study guidance"],
  [/^course/, "Checking the course"],
  [/^(math|probability)/, "Calculating"],
  [/^logic/, "Building a truth table"],
  [/^circuit/, "Analyzing a circuit"],
  [/^artifact/, "Reading saved results"],
  [/^chat/, "Updating the chat"],
];

export function toolVerb(name: string) {
  return TOOL_VERBS.find(([pattern]) => pattern.test(name))?.[1] ?? name.charAt(0).toUpperCase() + name.slice(1);
}

/** "claude-opus-4-8[1m]" -> "Opus 4.8 (1M context)"; "gpt-6-astra" -> "GPT-6-Astra". */
export function prettyModel(id: string | null | undefined) {
  if (!id) return "";
  const context = /\[1m\]$/i.test(id) ? " (1M context)" : "";
  const bare = id.replace(/\[.*\]$/, "");
  const claude = bare.match(/^claude-([a-z]+)-(\d+)(?:-(\d{1,2}))?(?:-\d{8})?$/);
  if (claude) {
    const name = claude[1].charAt(0).toUpperCase() + claude[1].slice(1);
    return `${name} ${claude[2]}${claude[3] ? "." + claude[3] : ""}${context}`;
  }
  return bare.replace(/^gpt/i, "GPT").replace(/-([a-z])/g, (_, c) => "-" + c.toUpperCase()) + context;
}
