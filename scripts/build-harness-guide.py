"""Build docs/how-it-works.html from docs/harness-docs/ai-ba-harness.md.

    python scripts/build-harness-guide.py          # write the page
    python scripts/build-harness-guide.py --check  # exit 1 if the page is out of date

The Markdown guide is the source; never edit the HTML by hand. Like build-walkthrough.py, this
script takes the <head>, the styles and the brand from docs/index.html, so the three pages match.
Links to repository files become relative paths, so they work when the page is opened from a local
clone. Run it after every change to the guide, and commit both files. Standard library only.
"""
import html
import os
import re
import struct
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
GUIDE_DIR = os.path.join(DOCS, "harness-docs")
SRC = os.path.join(GUIDE_DIR, "ai-ba-harness.md")
OUT = os.path.join(DOCS, "how-it-works.html")
HANDBOOK = os.path.join(DOCS, "index.html")

EXTRA_CSS = """
/* how-it-works.html: generated from docs/harness-docs/ai-ba-harness.md */
figure.diagram{margin:1.2rem 0 1.6rem}
figure.diagram a{display:block;border:1px solid var(--border);border-radius:12px;background:#fff;padding:10px;box-shadow:var(--shadow)}
figure.diagram img{display:block;width:100%;height:auto}
figure.diagram figcaption{font-size:.8rem;color:var(--muted);margin-top:.45rem}
main h2 .num{color:var(--muted);font-weight:500;margin-right:.35rem}
main pre{white-space:pre;overflow-x:auto;max-width:100%}
"""


def slug(text):
    """GitHub's heading anchor: lower case, punctuation dropped, spaces to hyphens."""
    t = re.sub(r"<[^>]+>", "", text).lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")


def href_for(target):
    """Map a link in the guide (relative to docs/harness-docs/) to one that works from docs/."""
    if re.match(r"^[a-z]+:", target) or target.startswith("#"):
        return target
    path, _, frag = target.partition("#")
    full = os.path.normpath(os.path.join(GUIDE_DIR, path))
    if full == os.path.normpath(SRC):
        return "#" + frag if frag else "#top"
    out = os.path.relpath(full, DOCS).replace(os.sep, "/")
    if os.path.isdir(full):
        out += "/"
    return out + ("#" + frag if frag else "")


def png_size(rel):
    """Width and height from a PNG's header, so the page keeps its layout while images load."""
    with open(os.path.join(DOCS, rel), "rb") as f:
        head = f.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        sys.exit(f"build-harness-guide: {rel} is not a PNG")
    return struct.unpack(">II", head[16:24])


def inline(text):
    keep = []

    def stash(s):
        keep.append(s)
        return f"\x00{len(keep) - 1}\x00"

    def link(m):
        return stash(f'<a href="{html.escape(href_for(m.group(2)))}">{inline(m.group(1))}</a>')

    text = re.sub(r"\[((?:[^\[\]`]|`[^`]*`)+)\]\(([^)\s]+)\)", link, text)
    text = re.sub(r"`([^`]+)`", lambda m: stash(f"<code>{html.escape(m.group(1), quote=False)}</code>"), text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])", r"<em>\1</em>", text)
    while "\x00" in text:
        text = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], text)
    return text


def plain(text):
    """A sidebar label: the heading's text without code formatting or other tags."""
    return re.sub(r"<[^>]+>", "", inline(text))


def cells(row):
    row = row.strip().strip("|")
    parts = re.split(r"(?<!\\)\|", row)
    return [inline(p.strip().replace("\\|", "|")) for p in parts]


def convert(md):
    lines = md.split("\n")
    body, nav, title, lede = [], [], "", ""
    i, para = 0, []

    def flush():
        nonlocal lede
        if para:
            text = inline(" ".join(s.strip() for s in para))
            if not lede and title and not nav:
                lede = text
            else:
                body.append(f"<p>{text}</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith("```"):
            flush()
            lang = s[3:].strip()
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            cls = f' class="language-{lang}"' if lang else ""
            body.append(f"<pre><code{cls}>{html.escape(chr(10).join(code), quote=False)}</code></pre>")
        elif s.startswith("# "):
            flush()
            title = s[2:].strip()
        elif s.startswith("## "):
            flush()
            text = s[3:].strip()
            if text == "Contents":  # the sidebar replaces the guide's own contents list
                i += 1
                while i < len(lines) and not lines[i].startswith("## "):
                    i += 1
                continue
            anchor = slug(text)
            m = re.match(r"^(\d+)\.\s+(.*)$", text)
            heading = f'<span class="num">{m.group(1)}.</span>{inline(m.group(2))}' if m else inline(text)
            nav.append((anchor, plain(m.group(2) if m else text)))
            body.append(f'<h2 id="{anchor}">{heading}</h2>')
        elif s.startswith("### "):
            flush()
            body.append(f'<h3 id="{slug(s[4:])}">{inline(s[4:])}</h3>')
        elif re.match(r"^!\[[^\]]*\]\([^)]+\)$", s):
            flush()
            alt, src = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", s).groups()
            src = href_for(src)
            w, h = png_size(src)
            body.append(f'<figure class="diagram"><a href="{html.escape(src)}" title="Open full size">'
                        f'<img src="{html.escape(src)}" alt="{html.escape(alt)}" width="{w}" height="{h}" loading="lazy"></a>'
                        f"<figcaption>Click the diagram to open it full size.</figcaption></figure>")
        elif s.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i])
                i += 1
            head, rest = cells(rows[0]), rows[2:]
            out = ["<table><thead><tr>" + "".join(f"<th>{c}</th>" for c in head) + "</tr></thead><tbody>"]
            for r in rest:
                out.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells(r)) + "</tr>")
            body.append("\n".join(out) + "</tbody></table>")
            continue
        elif re.match(r"^(- |\d+\. )", s) and not line.startswith(" "):
            flush()
            ordered = bool(re.match(r"^\d+\. ", s))
            items = []
            while i < len(lines):
                cur = lines[i]
                if re.match(r"^(- |\d+\. )", cur):
                    items.append([re.sub(r"^(- |\d+\. )", "", cur)])
                elif cur.startswith(" ") and cur.strip() and items:
                    items[-1].append(cur.strip())
                else:
                    break
                i += 1
            tag = "ol" if ordered else "ul"
            body.append(f"<{tag}>" + "".join(f'<li>{inline(" ".join(it))}</li>' for it in items) + f"</{tag}>")
            continue
        elif not s:
            flush()
        else:
            para.append(line)
        i += 1
    flush()
    return title, lede, nav, "\n".join(body)


def build():
    handbook = open(HANDBOOK, encoding="utf-8").read()
    head = handbook[: handbook.index("</head>")]
    head = re.sub(r"<title>.*?</title>", "<title>How the BA Harness Works</title>", head)
    head = head.replace("</style>", EXTRA_CSS + "</style>", 1)
    version = re.search(r"BA handbook · (v[0-9.]+)", handbook).group(1)
    brand = re.search(r'<div class="brand">.*?</div>\s*</div>', handbook, flags=re.S).group(0)
    brand = brand.replace(f"BA handbook · {version}", f"How it works · {version}")

    title, lede, nav, body = convert(open(SRC, encoding="utf-8").read())
    nav_html = "\n".join(f'  <a href="#{a}">{t}</a>' for a, t in nav)
    return f"""{head}</head>
<body>
<!-- Generated by scripts/build-harness-guide.py from docs/harness-docs/ai-ba-harness.md. Do not edit by hand. -->
<div class="layout">
<nav>
  {brand}
  <h2>How it works</h2>
{nav_html}
  <h2>More</h2>
  <a href="index.html">The BA handbook</a>
  <a href="walkthrough.html">FleetKeep walkthrough</a>
</nav>
<main id="top">
<h1>{inline(title)}</h1>
<p class="lede">{lede}</p>
{body}

<footer>
<p>This page is generated from <a href="harness-docs/ai-ba-harness.md"><code>docs/harness-docs/ai-ba-harness.md</code></a>
by <code>scripts/build-harness-guide.py</code>. Edit the Markdown, then run the script. The diagrams'
editable source is <a href="harness-docs/diagrams/ai-ba-harness/ai-ba-harness.drawio"><code>ai-ba-harness.drawio</code></a>.</p>
<p>AI BA Harness · MIT License.</p>
</footer>
</main>
</div>
</body>
</html>
"""


def main():
    page = build()
    if "--check" in sys.argv:
        current = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if current != page:
            sys.exit("build-harness-guide: docs/how-it-works.html is out of date; run python scripts/build-harness-guide.py")
        print("build-harness-guide: up to date")
        return
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    print(f"docs/how-it-works.html written ({len(page)} characters, {page.count('<h2 id=')} sections)")


if __name__ == "__main__":
    main()
