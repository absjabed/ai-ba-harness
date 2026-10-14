"""Build docs/walkthrough.html from the handbook's "Follow a whole project" section.

    python scripts/build-walkthrough.py

The worked example is written once, in docs/index.html, between <h2 id="example"> and the next
section. This script copies it into a page of its own, with the handbook's styles, so the two never
drift. Run it after every change to that section, and commit both files.
"""
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent
handbook = (root / "docs" / "index.html").read_text(encoding="utf-8")

head = handbook[: handbook.index("</head>")]
head = re.sub(r"<title>.*?</title>", "<title>FleetKeep Walkthrough</title>", head)
version = re.search(r"BA handbook · (v[0-9.]+)", handbook).group(1)

start = handbook.index('<h2 id="example">')
end = handbook.index('<h2 id="commands">')
section = handbook[start:end]

# The section's own heading and lede become the page title; links to other handbook sections point
# at the handbook.
section = re.sub(r'<h2 id="example">.*?</h2>\s*', "", section, count=1, flags=re.S)
section = re.sub(r'href="#(?!ex-)([^"]+)"', r'href="index.html#\1"', section)
section = re.sub(
    r'<p class="lede">(.*?)</p>',
    lambda m: '<p class="lede">' + re.sub(r"\s*The same example, as a page of its own.*", "", m.group(1), flags=re.S) + "</p>",
    section, count=1, flags=re.S)

parts = re.findall(r'<h3 id="(ex-[^"]+)">(.*?)</h3>', section, flags=re.S)
nav_items = []
for anchor, title in parts:
    text = re.sub(r"<[^>]+>", "", title)
    css = ' class="sub"' if text.startswith("Part") else ""
    nav_items.append(f'  <a{css} href="#{anchor}">{text.replace("Part ", "")}</a>')
nav_links = "\n".join(nav_items)

brand = re.search(r'<div class="brand">.*?</div>\s*</div>', handbook, flags=re.S).group(0)
brand = brand.replace(f"BA handbook · {version}", f"Walkthrough · {version}")

page = f"""{head}</head>
<body>
<div class="layout">
<nav>
  {brand}
  <h2>The walkthrough</h2>
{nav_links}
  <h2>More</h2>
  <a href="index.html">The BA handbook</a>
</nav>
<main>
<h1>FleetKeep, from setup to ask</h1>
{section.strip()}

<footer>
<p>This page is generated from the "Follow a whole project" section of the
<a href="index.html#example">BA handbook</a>, which also has the reference for every command, the
knowledge base rules and the safety layers. The files Parts 1 to 4 end with are in
<code>examples/fleetkeep-ba-knowledge/</code>; start with its <code>EXAMPLE.md</code>.</p>
<p>AI BA Harness · Private repository. All rights reserved.</p>
</footer>
</main>
</div>
</body>
</html>
"""
(root / "docs" / "walkthrough.html").write_text(page, encoding="utf-8", newline="\n")
print(f"docs/walkthrough.html written ({len(page)} characters, {len(parts)} sections, {version})")
