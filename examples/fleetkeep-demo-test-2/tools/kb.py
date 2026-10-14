"""Knowledge base tool: rebuild the generated files, check the knowledge base, find the next free ID.

    python tools/kb.py rebuild       rewrite knowledge/index.md and the three registers
    python tools/kb.py check         check links, names, properties and IDs (exit 1 on errors)
    python tools/kb.py next CAP      print the next free ID for a prefix (CAP, BR, Q, ACT, T, ...)

Plain Python 3.8 or later, no packages. The harness commands run it when Python is available; when
it isn't, they follow knowledge/_meta/conventions.md section 12 by hand, which describes the same
output. The GitHub workflow in .github/workflows/kb-check.yml runs `check` on every push and pull
request.
"""
import datetime
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = os.path.join(ROOT, "knowledge")
STATUSES = ("draft", "confirmed", "approved", "superseded")
PAGE_TYPES = {"capability": "CAP", "entity": "ENT", "process": "PROC", "decision": "DEC",
              "question": "Q", "source": "SRC"}
SECTION_TITLES = {"capability": "Capabilities", "entity": "Entities", "process": "Processes",
                  "decision": "Decisions", "question": "Questions", "source": "Sources"}
LIST_PROPS = ("sources", "rules", "aliases", "tags", "blocks")
DATE_PROPS = ("created", "updated", "approved_on", "decided_on", "asked_on", "due", "answered_on",
              "input_date", "reviewed_on", "delivered_on")
SKIP_DIRS = {"_meta", "_staging", ".obsidian", "assets"}
GENERATED = ("index.md", "business-rules.md", "decisions.md", "open-questions.md")
# Fixed entries for the root pages, in this order: (path in knowledge/, label, one line)
ROOT_PAGES = [
    ("glossary.md", "Glossary", "Every project term with its definition, the words people use for it, and its source."),
    ("stakeholders.md", "Stakeholders", "Who is involved, what they own, what they can decide, and the RACI for recurring decisions."),
    ("raid.md", "Risks, assumptions, issues, dependencies and actions", "One table each, with owner, status and source."),
    ("business-rules.md", "Business rules", "Every rule in force, with the page that defines it. Generated."),
    ("decisions.md", "Decisions", "Every decision, with date, decider and status. Generated."),
    ("open-questions.md", "Open questions", "Open questions first, with who to ask and what they block. Generated."),
    ("log.md", "Change log", "One line per accepted change, newest last."),
    ("README.md", "How to read and contribute to this knowledge base", "Start here if you are new."),
    ("_meta/conventions.md", "Knowledge base conventions", "The rules every command follows when it reads or changes this knowledge base."),
]


# ---------------------------------------------------------------- reading pages

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def parse(path):
    """Flat YAML properties and the body. Returns (None, text) when there are no properties."""
    text = read(path).replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        return None, text
    props, key = {}, None
    for line in m.group(1).splitlines():
        if re.match(r"^\s+- ", line) and key:
            if not isinstance(props.get(key), list):
                props[key] = []
            props[key].append(unquote(line.split("- ", 1)[1].strip()))
        elif re.match(r"^[A-Za-z_][\w-]*:", line):
            key, val = line.split(":", 1)
            key, val = key.strip(), val.split(" #")[0].strip()
            if val.startswith("[") and val.endswith("]"):
                props[key] = [unquote(v.strip()) for v in val[1:-1].split(",") if v.strip()]
            else:
                props[key] = [] if val == "" and key in LIST_PROPS else unquote(val)
    return props, m.group(2)


def unquote(v):
    return v[1:-1] if len(v) > 1 and v[0] == v[-1] and v[0] in "'\"" else v


def as_list(v):
    if isinstance(v, list):
        return v
    return [] if v in (None, "", "[]") else [v]


def rel(path, start=KB):
    return os.path.relpath(path, start).replace(os.sep, "/")


def plain(text):
    """Markdown to one plain line: links become their text, emphasis and code marks go."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def summary(props, body):
    """The page's `summary` property, or the first sentence of the first paragraph after the title."""
    if props.get("summary"):
        return plain(props["summary"])
    lines = body.splitlines()
    i = next((n for n, l in enumerate(lines) if l.startswith("# ")), -1) + 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    para = []
    while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", "|", ">", "-", "<!--")):
        para.append(lines[i].strip())
        i += 1
    p = plain(" ".join(para))
    m = re.match(r"(.+?[.?!])(\s|$)", p)
    return m.group(1) if m else p


def number(id_):
    m = re.search(r"(\d+)$", id_ or "")
    return int(m.group(1)) if m else 0


def load_pages():
    pages = []
    for root, dirs, files in os.walk(KB):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for f in sorted(files):
            if not f.endswith(".md") or (root == KB and f in GENERATED):
                continue
            path = os.path.join(root, f)
            props, body = parse(path)
            if props and props.get("type") in PAGE_TYPES:
                pages.append({"path": path, "rel": rel(path), "props": props, "body": body})
    return pages


def profile_areas():
    try:
        text = read(os.path.join(ROOT, "PROJECT-PROFILE.md"))
    except OSError:
        return []
    m = re.search(r"^## 4\..*?(?=^## 5\.)", text, re.S | re.M)
    return re.findall(r"^\| `([a-z0-9-]+)` \|", m.group(0), re.M) if m else []


def profile_setting(name, default):
    try:
        m = re.search(r"^" + name + r":\s*(\S+)", read(os.path.join(ROOT, "PROJECT-PROFILE.md")), re.M)
    except OSError:
        return default
    return m.group(1) if m else default


def rules_on(page):
    """{BR-id: statement} for every rule line on a page, and {BR-id: replacement} for retired ones."""
    active, retired = {}, {}
    for line in page["body"].splitlines():
        m = re.match(r"^\d+\.\s+~~\*\*(BR-\d+)\*\*\s*(.*?)~~\s*(.*)$", line)
        if m:
            repl = re.search(r"(BR-\d+)", m.group(3))
            retired[m.group(1)] = (plain(m.group(2)), repl.group(1) if repl else "")
            continue
        m = re.match(r"^\d+\.\s+\*\*(BR-\d+)\*\*\s+(.+)$", line)
        if m:
            stmt = re.sub(r"\s*\((?:\[?(?:SRC|DEC|Q|BR)-|\[?[A-Z][A-Z0-9]+-\d).*\)\s*$", "", m.group(2))
            active[m.group(1)] = plain(stmt)
    return active, retired


# ---------------------------------------------------------------- rebuild

def link(page, root_rel=""):
    p = page["props"]
    return f"[{p['id']} {p['title']}]({root_rel}{page['rel']})"


def header(id_, title, intro):
    return ["---", "type: register" if id_ != "INDEX" else "type: index", f"id: {id_}", f"title: {title}",
            "---", "", f"# {title}", "", intro, ""]


def build():
    pages = load_pages()
    by_id = {p["props"].get("id"): p for p in pages}
    out = {}

    # index.md
    lines = header("INDEX", "Knowledge base index",
                   "Generated by `tools/kb.py rebuild` from every page's properties. Don't edit it by hand.")
    lines += [f"{len(pages)} pages. Superseded pages are listed for history; don't rely on them.", ""]
    if not pages:
        lines += ["*Empty. `/kb-seed` and `/intake` add pages here as the BA accepts them.*", ""]
    areas = profile_areas()
    for t in PAGE_TYPES:
        group = [p for p in pages if p["props"]["type"] == t]
        if not group:
            continue
        lines += [f"## {SECTION_TITLES[t]}", ""]

        def entry(p):
            st = p["props"].get("status", "")
            if t == "question":
                st += ", " + p["props"].get("state", "")
            return f"- {link(p)} · {st} · {summary(p['props'], p['body'])}"

        if t in ("capability", "process"):
            found = sorted({p["props"].get("area", "") for p in group},
                           key=lambda a: (areas.index(a) if a in areas else len(areas), a))
            for a in found:
                lines += [f"### {a or 'no area'}", ""]
                lines += [entry(p) for p in sorted((g for g in group if g["props"].get("area", "") == a),
                                                   key=lambda g: number(g["props"]["id"]))]
                lines.append("")
        else:
            lines += [entry(p) for p in sorted(group, key=lambda g: number(g["props"]["id"]))]
            lines.append("")
    lines += ["## Registers and guides", ""]
    for path, label, line in ROOT_PAGES:
        if os.path.exists(os.path.join(KB, path)):
            lines.append(f"- [{label}]({path}) · {line}")
    lines.append("")
    out["index.md"] = lines

    # business-rules.md
    rules, retired = [], []
    for p in pages:
        active, gone = rules_on(p)
        for br in as_list(p["props"].get("rules")):
            rules.append((number(br), br, active.get(br, "(statement not found on the page)"), p))
        for br, (stmt, repl) in gone.items():
            retired.append((number(br), br, stmt, repl, p))
    lines = header("REG-rules", "Business rules",
                   "Generated by `tools/kb.py rebuild` from the `rules` property of every page. Don't edit it by hand.\nEach rule is defined, in context, on the page linked.")
    lines += ["| Rule | Statement | Defined on |", "|---|---|---|"]
    lines += [f"| {br} | {stmt} | {link(p)} |" for _, br, stmt, p in sorted(rules, key=lambda r: r[0])]
    if retired:
        lines += ["", "## Retired rules", "", "| Rule | Statement | Replaced by | Page |", "|---|---|---|---|"]
        lines += [f"| {br} | {stmt} | {repl or 'none'} | {link(p)} |" for _, br, stmt, repl, p in sorted(retired, key=lambda r: r[0])]
    lines.append("")
    out["business-rules.md"] = lines

    # decisions.md
    lines = header("REG-decisions", "Decisions",
                   "Generated by `tools/kb.py rebuild` from `decisions/`. Don't edit it by hand.")
    lines += ["| Decision | Date | Decided by | Status |", "|---|---|---|---|"]
    for p in sorted((p for p in pages if p["props"]["type"] == "decision"), key=lambda g: number(g["props"]["id"])):
        pr = p["props"]
        lines.append(f"| {link(p)} | {pr.get('decided_on', '')} | {pr.get('decided_by', '')} | {pr.get('status', '')} |")
    lines.append("")
    out["decisions.md"] = lines

    # open-questions.md
    qs = [p for p in pages if p["props"]["type"] == "question"]

    def by_state(s):
        return [q for q in qs if q["props"].get("state", "open") == s]

    lines = header("REG-questions", "Open questions",
                   "Generated by `tools/kb.py rebuild` from `questions/`. Don't edit it by hand. Open questions\ncome first, the earliest due date first.")
    lines += ["## Open", "", "| Question | Asked of | Due | Blocks |", "|---|---|---|---|"]
    for q in sorted(by_state("open"), key=lambda q: (q["props"].get("due") or "9999", number(q["props"]["id"]))):
        pr = q["props"]
        lines.append(f"| {link(q)} | {pr.get('asked_of', '')} | {pr.get('due', '')} | {', '.join(as_list(pr.get('blocks'))) or 'none'} |")
    lines += ["", "## Answered", "", "| Question | Answered on | Answer source |", "|---|---|---|"]
    for q in sorted(by_state("answered"), key=lambda q: number(q["props"]["id"])):
        pr = q["props"]
        src = by_id.get(pr.get("answer_source"))
        lines.append(f"| {link(q)} | {pr.get('answered_on', '')} | {link(src) if src else pr.get('answer_source', '')} |")
    lines += ["", "## Won't fix", "", "| Question | Owner |", "|---|---|"]
    for q in sorted(by_state("wontfix"), key=lambda q: number(q["props"]["id"])):
        lines.append(f"| {link(q)} | {q['props'].get('owner', '')} |")
    lines.append("")
    out["open-questions.md"] = lines
    return {k: "\n".join(v) for k, v in out.items()}


def rebuild():
    for name, text in build().items():
        with open(os.path.join(KB, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    print("Rebuilt " + ", ".join("knowledge/" + n for n in GENERATED))


# ---------------------------------------------------------------- check

def slug(heading):
    """GitHub's anchor for a heading (Obsidian accepts the same links)."""
    h = re.sub(r"[`*_]|\[([^\]]*)\]\([^)]*\)", r"\1", heading).strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


def anchors(path):
    text = re.sub(r"```.*?```", "", read(path), flags=re.S)
    return {slug(h) for h in re.findall(r"^#{1,6}\s+(.+?)\s*$", text, re.M)}


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def defined_ids(pages):
    ids = {p["props"]["id"] for p in pages}
    for p in pages:
        active, gone = rules_on(p)
        ids |= set(active) | set(gone)
    for name, pattern in (("glossary.md", r"\*\*(T-\d+)\*\*"), ("raid.md", r"^\| ((?:R|A|I|D|ACT)-\d+) \|")):
        try:
            ids |= set(re.findall(pattern, read(os.path.join(KB, name)), re.M))
        except OSError:
            pass
    req = os.path.join(ROOT, "requirements")
    if os.path.isdir(req):
        for d in os.listdir(req):
            ids |= {f"REQ-{d}", f"REVIEW-{d}"}
    return ids


def check():
    errors, warnings = [], []
    pages = load_pages()
    today = datetime.date.today()

    # Pages: properties, names, statuses, dates
    seen = {}
    for p in pages:
        pr, name = p["props"], os.path.basename(p["path"])
        for k in ("type", "id", "title", "status"):
            if not pr.get(k):
                errors.append(f"{p['rel']}: missing property `{k}`")
        id_ = pr.get("id", "")
        if id_ in seen:
            errors.append(f"{p['rel']}: ID {id_} is also used by {seen[id_]}")
        seen[id_] = p["rel"]
        prefix = PAGE_TYPES[pr["type"]]
        if not re.fullmatch(prefix + r"-\d{3,}", id_):
            errors.append(f"{p['rel']}: ID {id_} doesn't fit the {prefix}- pattern")
        if not name.startswith(id_ + "-") or not re.fullmatch(r"[A-Z]+-\d+-[a-z0-9]+(-[a-z0-9]+)*\.md", name):
            errors.append(f"{p['rel']}: file name must be <ID>-<lowercase-hyphenated-slug>.md")
        if len(name) > 64:
            errors.append(f"{p['rel']}: file name longer than 64 characters")
        st = pr.get("status")
        if st and st not in STATUSES:
            errors.append(f"{p['rel']}: unknown status `{st}`")
        if st == "superseded" and not pr.get("superseded_by"):
            errors.append(f"{p['rel']}: superseded without `superseded_by`")
        if st == "approved" and pr["type"] != "decision" and not (pr.get("approved_by") and pr.get("approved_on")):
            errors.append(f"{p['rel']}: approved without `approved_by` and `approved_on`")
        if pr["type"] == "question" and pr.get("state") not in ("open", "answered", "wontfix"):
            errors.append(f"{p['rel']}: `state` must be open, answered or wontfix")
        for k in DATE_PROPS:
            v = pr.get(k)
            if v and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(v)):
                errors.append(f"{p['rel']}: `{k}` must be YYYY-MM-DD")
        if pr["type"] == "question" and pr.get("state") == "open" and re.fullmatch(r"\d{4}-\d{2}-\d{2}", pr.get("due", "")):
            if datetime.date.fromisoformat(pr["due"]) < today:
                warnings.append(f"{p['rel']}: open question past its due date {pr['due']}")
        if st == "draft" and re.fullmatch(r"\d{4}-\d{2}-\d{2}", pr.get("updated", "")):
            age = (today - datetime.date.fromisoformat(pr["updated"])).days
            if age > int(profile_setting("draft_age_days", "30")):
                warnings.append(f"{p['rel']}: draft for {age} days")
        listed = set(as_list(pr.get("rules")))
        active, gone = rules_on(p)
        for br in listed - set(active):
            errors.append(f"{p['rel']}: `rules` lists {br}, which isn't a rule line on the page")
        for br in set(active) - listed:
            errors.append(f"{p['rel']}: {br} is on the page but not in `rules`")
        for br in listed & set(gone):
            errors.append(f"{p['rel']}: retired {br} is still in `rules`")

    # IDs in the RAID log and the glossary are unique
    for name, pattern in (("raid.md", r"^\| ((?:R|A|I|D|ACT)-\d+) \|"), ("glossary.md", r"\*\*(T-\d+)\*\*")):
        try:
            text = re.sub(r"<!--.*?-->", "", read(os.path.join(KB, name)), flags=re.S)
        except OSError:
            continue
        found = re.findall(pattern, text, re.M)
        for dup in sorted({i for i in found if found.count(i) > 1}):
            errors.append(f"knowledge/{name}: {dup} is used more than once")

    # Rule IDs unique across pages
    owners = {}
    for p in pages:
        active, gone = rules_on(p)
        for br in list(active) + list(gone):
            if br in owners and owners[br] != p["rel"]:
                errors.append(f"{br} is defined on both {owners[br]} and {p['rel']}")
            owners[br] = p["rel"]

    # Links and anchors in the knowledge base, requirements and root guides
    files = [os.path.join(ROOT, f) for f in ("README.md", "CLAUDE.md", "AGENTS.md", "PROJECT-PROFILE.md")]
    for base in (KB, os.path.join(ROOT, "requirements")):
        for root, dirs, fs in os.walk(base):
            dirs[:] = [d for d in dirs if d not in (".obsidian", "templates")]
            files += [os.path.join(root, f) for f in fs if f.endswith(".md")]
    for path in files:
        if not os.path.exists(path):
            continue
        text = strip_code(read(path))
        if "[[" in text:
            errors.append(f"{rel(path, ROOT)}: wikilink; use relative markdown links")
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target):
                continue
            path_part, _, anchor = target.partition("#")
            dest = os.path.normpath(os.path.join(os.path.dirname(path), path_part)) if path_part else path
            in_staging = "/_staging/" in path.replace(os.sep, "/")
            if not os.path.exists(dest):
                if in_staging and re.search(r"-new(-\d|\b)", path_part):
                    continue  # a staging file may link a page it is proposing
                errors.append(f"{rel(path, ROOT)}: broken link {target}")
            elif anchor and dest.endswith(".md") and anchor not in anchors(dest):
                errors.append(f"{rel(path, ROOT)}: no heading for #{anchor} in {target}")

    # Cited IDs exist; provisional IDs only in staging
    ids = defined_ids(pages)
    guides = {os.path.join(ROOT, f) for f in ("README.md", "CLAUDE.md", "AGENTS.md", "PROJECT-PROFILE.md")}
    guides.add(os.path.join(KB, "README.md"))
    cited_in = [f for f in files if f not in guides and "/_meta/" not in f.replace(os.sep, "/")]
    trace = os.path.join(ROOT, "trace", "map.csv")
    if os.path.exists(trace):
        cited_in.append(trace)
    for path in cited_in:
        r = rel(path, ROOT)
        text = re.sub(r"<!--.*?-->", "", read(path), flags=re.S)
        if "/_staging/" not in "/" + r.replace(os.sep, "/") and re.search(r"\b[A-Z]{1,5}-new(-\d+)?\b", text):
            errors.append(f"{r}: provisional ID (like CAP-new-1) outside a staging file")
        if "/_staging/" in "/" + r:
            continue
        for c in sorted(set(re.findall(r"\b(?:CAP|ENT|PROC|DEC|Q|SRC|BR|T|R|A|I|D|ACT)-\d{3,}\b", text))):
            if c not in ids:
                errors.append(f"{r}: cites {c}, which doesn't exist")

    # Actions past due, staging files older than a day
    try:
        raid = read(os.path.join(KB, "raid.md"))
        for m in re.finditer(r"^\| (ACT-\d+) \|[^|]*\|[^|]*\| (\d{4}-\d{2}-\d{2}) \| (\w+) \|", raid, re.M):
            if m.group(3) == "open" and datetime.date.fromisoformat(m.group(2)) < today:
                warnings.append(f"knowledge/raid.md: {m.group(1)} is open past its due date {m.group(2)}")
    except OSError:
        pass
    staging = os.path.join(KB, "_staging")
    if os.path.isdir(staging):
        for f in os.listdir(staging):
            m = re.match(r"(\d{4}-\d{2}-\d{2})-", f)
            if f.endswith(".md") and m and (today - datetime.date.fromisoformat(m.group(1))).days > 1:
                warnings.append(f"knowledge/_staging/{f}: waiting for decisions for more than a day")

    # Generated files are up to date
    for name, text in build().items():
        path = os.path.join(KB, name)
        if not os.path.exists(path) or read(path).replace("\r\n", "\n") != text:
            errors.append(f"knowledge/{name}: out of date; run `python tools/kb.py rebuild`")

    try:
        json.loads(read(os.path.join(KB, "_meta", "sync.json")))
    except (OSError, ValueError) as e:
        errors.append(f"knowledge/_meta/sync.json: {e}")

    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("error:", e)
    print(f"{len(pages)} pages, {len(files)} files checked: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


# ---------------------------------------------------------------- next ID

def next_id(prefix):
    prefix = prefix.upper().rstrip("-")
    pages = load_pages()
    used = {i for i in defined_ids(pages) if re.fullmatch(prefix + r"-\d+", i)}
    n = max((number(i) for i in used), default=0) + 1
    print(f"{prefix}-{n:03d}")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "rebuild":
        rebuild()
    elif len(sys.argv) >= 2 and sys.argv[1] == "check":
        sys.exit(check())
    elif len(sys.argv) == 3 and sys.argv[1] == "next":
        next_id(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(2)
