"""Write a Bedrock Knowledge Base metadata sidecar next to every page in docs/.

Does what the publish job in the plan (§2.1) does: reads each page's
"Applies to tier:", "Business unit:", "Console page:", "Article type:" and
"Category:" lines and writes <page>.md.metadata.json. A page with no tier line
gets Power User only, so a missing tag never exposes a page to Agency users.

Run from this folder:  python3 make_sidecars.py
"""
import json
import pathlib
import re
import sys

ROLES = ["Power User", "Agency"]
DEFAULT_TIERS = ["Power User"]
DOC_TYPES = {"getting_started", "how_to", "faq", "concept", "troubleshooting", "reference"}
UPDATED = "2026-10-18"


def line(text, label):
    m = re.search(rf"^{label}:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else None


def pillar(link):
    if link.startswith("/admin"):
        return "admin"
    return {"/": "overview", "/login": "account"}.get(link, link.strip("/").split("/")[0].replace("-", "_"))


def main():
    docs = pathlib.Path(__file__).parent / "docs"
    rows, errors = [], []
    for page in sorted(docs.glob("*.md")):
        text = page.read_text()
        title = re.search(r"^# (.+)$", text, re.M).group(1).strip()
        tier_line = line(text, "Applies to tier")
        tiers = [t.strip() for t in tier_line.split(",")] if tier_line else DEFAULT_TIERS
        bad = [t for t in tiers if t not in ROLES]
        if bad:
            errors.append(f"{page.name}: unknown role {bad}")
        doc_type = line(text, "Article type") or "how_to"
        if doc_type not in DOC_TYPES:
            errors.append(f"{page.name}: unknown article type {doc_type!r}")
        link = line(text, "Console page") or "/"
        attrs = {
            "title": title,
            "doc_type": doc_type,
            "pillar": line(text, "Category") or pillar(link),
            "allowed_tiers": tiers,
            # One flag per role as well, in case the vector store can't filter a list (plan §5.3).
            "tier_power_user": "Power User" in tiers,
            "tier_agency": "Agency" in tiers,
            "business_unit": line(text, "Business unit") or "all",
            "console_link": link,
            "source_updated_at": UPDATED,
        }
        sidecar = page.with_name(page.name + ".metadata.json")
        sidecar.write_text(json.dumps({"metadataAttributes": attrs}, indent=2) + "\n")
        rows.append((page.name, ", ".join(tiers) + ("  (default)" if not tier_line else ""), doc_type))
    for name, tiers, doc_type in rows:
        print(f"{name:44} {tiers:28} {doc_type}")
    if errors:
        sys.exit("\n".join(errors))
    print(f"{len(rows)} sidecars written")


if __name__ == "__main__":
    main()
