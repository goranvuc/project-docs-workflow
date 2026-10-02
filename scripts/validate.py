#!/usr/bin/env python3
"""Read-only structural validation of this distribution, not of user projects.

Standard library only. Inline Markdown links and heading/HTML anchors outside
fenced code are checked. External URLs, code examples, and claim truth are not.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "project-docs-workflow"


def prose(text: str) -> str:
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def anchors(text: str) -> set[str]:
    visible = prose(text)
    result = set(re.findall(r'\bid=["\']([^"\']+)["\']', visible))
    seen = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", visible, re.MULTILINE):
        heading = re.sub(r"<[^>]+>", "", heading)
        base = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = seen.get(base, 0)
        seen[base] = count + 1
        result.add(base if count == 0 else f"{base}-{count}")
    return result


def validate() -> list[str]:
    errors = []
    required = [
        ROOT / "README.md", ROOT / "README.sr.md", ROOT / "LICENSE",
        ROOT / "AGENTS.md", ROOT / "docs" / "validation.md",
        SKILL / "SKILL.md", SKILL / "agents" / "openai.yaml",
        *[SKILL / "references" / name for name in ("adoption.md", "consolidation.md")],
        *[SKILL / "assets" / name for name in (
            "agents-section.md", "overview.md", "plan.md", "journal-readme.md"
        )],
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")

    skill_file = SKILL / "SKILL.md"
    if skill_file.is_file():
        text = skill_file.read_text(encoding="utf-8")
        front = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        if not front:
            errors.append("SKILL.md requires YAML frontmatter")
        else:
            name = re.search(r"^name: (.+)$", front[1], re.MULTILINE)
            description = re.search(r"^description: (.+)$", front[1], re.MULTILINE)
            if not name or name[1].strip('"\'') != SKILL.name:
                errors.append("Skill name must match its directory")
            if not description or not description[1].strip() or len(description[1]) > 1024:
                errors.append("A non-empty single-line description up to 1024 characters is required")

    markdown = [p for p in ROOT.rglob("*.md") if ".git" not in p.relative_to(ROOT).parts]
    for path in markdown:
        visible = prose(path.read_text(encoding="utf-8"))
        for match in re.finditer(r"\[[^\]\n]*\]\(([^)\n]+)\)", visible):
            target = match[1].strip().split(' "', 1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            label = path.relative_to(ROOT)
            if not destination.is_relative_to(ROOT.resolve()):
                errors.append(f"{label}: link leaves repository: {target}")
            elif not destination.exists():
                errors.append(f"{label}: missing link target: {target}")
            elif parsed.fragment and destination.is_file() and destination.suffix == ".md":
                if unquote(parsed.fragment) not in anchors(destination.read_text(encoding="utf-8")):
                    errors.append(f"{label}: missing anchor: {target}")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        print("\n".join(f"FAIL: {failure}" for failure in failures))
        sys.exit(1)
    print("PASS: package structure, required metadata, and local Markdown links/anchors")
    print("Not checked: external URLs, template customization, semantic truth, or agent behavior")
