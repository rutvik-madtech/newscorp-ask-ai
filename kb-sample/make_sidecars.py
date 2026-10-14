"""Write a Bedrock Knowledge Base metadata sidecar next to every page in docs/.

Does what the publish job in the plan (§2.1) does: reads each page's
"Applies to tier:", "Business unit:" and "Console page:" lines and writes
<page>.md.metadata.json. A page with no tier line gets Power User and Admin
only, so a missing tag never exposes a page to Agency users.

Run from this folder:  python3 make_sidecars.py
"""
import json
import pathlib
import re
import sys

ROLES = ["Power User", "Admin", "Agency"]
DEFAULT_TIERS = ["Power User", "Admin"]
UPDATED = "2026-10-01"

DOC_TYPES = {
    "getting-started": "guide", "glossary": "glossary", "roles-and-access": "policy",
    "overview-page": "guide", "taxonomy": "guide", "build-an-audience": "how_to",
    "audience-gates": "concept", "matched-vs-modelled": "concept", "analysis-runs": "how_to",
    "delivery-destinations": "concept", "permissible-use-envelope": "concept",
    "delivery-troubleshooting": "troubleshooting", "rules-of-use-approvals": "how_to",
    "gating-rules": "policy", "agent-endpoint": "concept", "admin-access-roles": "how_to",
    "admin-connectors": "guide", "consent-ledger": "policy", "audit-trail": "guide",
    "bu-dow-jones": "guide", "bu-realtor": "guide", "faq": "faq", "release-notes": "release_notes",
}


def line(text, label):
    m = re.search(rf"^{label}:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else None


def pillar(link):
    if link.startswith("/admin"):
        return "admin"
    return {"/": "overview"}.get(link, link.strip("/").replace("-", "_"))


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
        link = line(text, "Console page") or "/"
        attrs = {
            "title": title,
            "doc_type": DOC_TYPES.get(page.stem, "guide"),
            "pillar": pillar(link),
            "allowed_tiers": tiers,
            # One flag per role as well, in case the vector store can't filter a list (plan §5.3).
            "tier_power_user": "Power User" in tiers,
            "tier_admin": "Admin" in tiers,
            "tier_agency": "Agency" in tiers,
            "business_unit": line(text, "Business unit") or "all",
            "console_link": link,
            "source_updated_at": UPDATED,
        }
        sidecar = page.with_name(page.name + ".metadata.json")
        sidecar.write_text(json.dumps({"metadataAttributes": attrs}, indent=2) + "\n")
        rows.append((page.name, ", ".join(tiers) + ("  (default)" if not tier_line else ""), attrs["business_unit"]))
    for name, tiers, bu in rows:
        print(f"{name:32} {tiers:38} {bu}")
    if errors:
        sys.exit("\n".join(errors))
    print(f"{len(rows)} sidecars written")


if __name__ == "__main__":
    main()
