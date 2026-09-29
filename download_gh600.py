"""
Script to download all Microsoft Learn documentation for Course GH-600T00
in the exact tree structure as Markdown files, keeping only title, canonicalUrl,
and description in the front-matter.
"""

import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

BASE_LEARN_URL = "https://learn.microsoft.com/en-us/training"

COURSE = {
    "title": "GH-600T00: Developing in Agentic AI Systems",
    "url": f"{BASE_LEARN_URL}/courses/gh-600t00?accept=text/markdown",
    "filename": "course.md",
}

STRUCTURE = [
    {
        "id": "gh-developing-agentic-systems-1",
        "title": "Developing in Agentic AI Systems Part 1 of 2",
        "url": f"{BASE_LEARN_URL}/paths/gh-developing-agentic-systems-1/?accept=text/markdown",
        "dir": "gh-developing-agentic-systems-1",
        "modules": [
            {
                "id": "foundations-agentic-ai",
                "title": "Foundations of Agentic AI in GitHub",
                "url": f"{BASE_LEARN_URL}/modules/foundations-agentic-ai/?accept=text/markdown",
                "dir": "foundations-agentic-ai",
            },
            {
                "id": "design-agent-architecture-integration",
                "title": "Designing Agent Architecture and SDLC Integration",
                "url": f"{BASE_LEARN_URL}/modules/design-agent-architecture-integration/?accept=text/markdown",
                "dir": "design-agent-architecture-integration",
            },
            {
                "id": "agent-tooling-mcp-execution-environments",
                "title": "Tooling, MCP, and Agent Execution Environments",
                "url": f"{BASE_LEARN_URL}/modules/agent-tooling-mcp-execution-environments/?accept=text/markdown",
                "dir": "agent-tooling-mcp-execution-environments",
            },
        ],
    },
    {
        "id": "github-agentic-systems-part-two",
        "title": "Developing in Agentic AI Systems Part 2 of 2",
        "url": f"{BASE_LEARN_URL}/paths/github-agentic-systems-part-two/github-agentic-systems-part-two?accept=text/markdown",
        "dir": "github-agentic-systems-part-two",
        "modules": [
            {
                "id": "multi-agent-systems-orchestration",
                "title": "Multi-Agent systems and orchestration",
                "url": f"{BASE_LEARN_URL}/modules/multi-agent-systems-orchestration/?accept=text/markdown",
                "dir": "multi-agent-systems-orchestration",
            },
            {
                "id": "memory-state-evaluation",
                "title": "Memory, State, and Evaluation",
                "url": f"{BASE_LEARN_URL}/modules/memory-state-evaluation/?accept=text/markdown",
                "dir": "memory-state-evaluation",
            },
            {
                "id": "governance-guardrails-operations",
                "title": "Governance, guardrails, and operations",
                "url": f"{BASE_LEARN_URL}/modules/governance-guardrails-operations/?accept=text/markdown",
                "dir": "governance-guardrails-operations",
            },
        ],
    },
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/markdown,text/plain,*/*",
}


def clean_frontmatter(markdown_text: str) -> str:
    """
    Keep only 'title', 'canonicalUrl', and 'description' in the YAML front-matter.
    Preserves the rest of the markdown document untouched.
    """
    if not markdown_text.startswith("---"):
        return markdown_text

    parts = markdown_text.split("---", 2)
    if len(parts) < 3:
        return markdown_text

    fm_raw = parts[1]
    body = parts[2]

    # Extract required fields: title, canonicalUrl, description
    fields = {}
    lines = fm_raw.splitlines()
    for i, line in enumerate(lines):
        for key in ["title", "canonicalUrl", "description"]:
            if re.match(rf"^{key}:", line):
                val_lines = [line]
                j = i + 1
                while j < len(lines) and (
                    lines[j].startswith("  ") or lines[j].startswith("\t")
                ):
                    val_lines.append(lines[j])
                    j += 1
                fields[key] = "\n".join(val_lines)

    new_fm_lines = ["---"]
    for key in ["title", "canonicalUrl", "description"]:
        if key in fields:
            new_fm_lines.append(fields[key])
    new_fm_lines.append("---")

    new_fm = "\n".join(new_fm_lines)
    return f"{new_fm}{body}"


def fetch_url(url: str, max_retries: int = 3, delay: float = 0.5) -> str:
    """Fetch URL content with retries and return decoded text."""
    for attempt in range(1, max_retries + 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                return data.decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            if attempt == max_retries:
                raise RuntimeError(f"HTTP {e.code} error fetching {url}") from e
            time.sleep(delay * attempt)
        except Exception as e:
            if attempt == max_retries:
                raise RuntimeError(f"Error fetching {url}: {e}") from e
            time.sleep(delay * attempt)
    raise RuntimeError(f"Failed to fetch {url} after {max_retries} retries")


def extract_unit_slugs(module_markdown: str):
    """
    Extract list of (title, slug) from module markdown.
    Format in module markdown is typically: - [Unit Title](slug)
    """
    pattern = r"-\s+\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(pattern, module_markdown)
    valid_units = []
    for title, link in matches:
        clean_link = link.strip().rstrip("/")
        if clean_link.startswith("http") or clean_link.startswith("#") or clean_link.startswith("mailto"):
            continue
        valid_units.append((title.strip(), clean_link))
    return valid_units


def save_markdown_file(path: Path, content: str, description: str = ""):
    """Clean front-matter and save content to markdown file ensuring parent directories exist."""
    cleaned_content = clean_frontmatter(content)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(cleaned_content)
    size_kb = len(cleaned_content.encode("utf-8")) / 1024
    print(f"  [SAVED] {path} ({size_kb:.1f} KB) - {description}")


def main():
    root_dir = Path(__file__).resolve().parent
    print(f"Starting download of GH-600 documentation into: {root_dir}")
    print("Front-matter will be filtered to only contain: title, canonicalUrl, description")
    print("=" * 70)

    stats = {
        "courses": 0,
        "paths": 0,
        "modules": 0,
        "units": 0,
        "total_files": 0,
        "errors": [],
    }

    # 1. Course overview
    print("\n[1/3] Fetching Course Overview...")
    try:
        course_md = fetch_url(COURSE["url"])
        course_file = root_dir / COURSE["filename"]
        save_markdown_file(course_file, course_md, COURSE["title"])
        stats["courses"] += 1
        stats["total_files"] += 1

        # Also save as README.md
        readme_file = root_dir / "README.md"
        save_markdown_file(readme_file, course_md, "Course Overview (README.md)")
        stats["total_files"] += 1
    except Exception as e:
        print(f"  [ERROR] Failed to fetch course: {e}")
        stats["errors"].append(("Course", COURSE["url"], str(e)))

    # 2. Learning Paths & Modules
    for path_idx, path_info in enumerate(STRUCTURE, start=1):
        print(f"\n[2/3] Processing Learning Path {path_idx}/{len(STRUCTURE)}: {path_info['title']}")
        path_dir = root_dir / path_info["dir"]
        path_dir.mkdir(parents=True, exist_ok=True)

        # Fetch path overview
        try:
            path_md = fetch_url(path_info["url"])
            path_file = path_dir / "index.md"
            save_markdown_file(path_file, path_md, f"Path Overview: {path_info['title']}")
            stats["paths"] += 1
            stats["total_files"] += 1
        except Exception as e:
            print(f"  [ERROR] Failed to fetch path {path_info['id']}: {e}")
            stats["errors"].append((f"Path {path_info['id']}", path_info["url"], str(e)))

        # Process modules
        for mod_idx, mod_info in enumerate(path_info["modules"], start=1):
            print(f"\n  --> Module {mod_idx}/{len(path_info['modules'])}: {mod_info['title']}")
            mod_dir = path_dir / mod_info["dir"]
            mod_dir.mkdir(parents=True, exist_ok=True)

            try:
                mod_md = fetch_url(mod_info["url"])
                mod_file = mod_dir / "index.md"
                save_markdown_file(mod_file, mod_md, f"Module Overview: {mod_info['title']}")
                stats["modules"] += 1
                stats["total_files"] += 1
            except Exception as e:
                print(f"    [ERROR] Failed to fetch module {mod_info['id']}: {e}")
                stats["errors"].append((f"Module {mod_info['id']}", mod_info["url"], str(e)))
                continue

            # Extract units from module overview markdown
            units = extract_unit_slugs(mod_md)
            print(f"    Found {len(units)} units in module '{mod_info['id']}'")

            for unit_idx, (unit_title, unit_slug) in enumerate(units, start=1):
                unit_url = f"{BASE_LEARN_URL}/modules/{mod_info['id']}/{unit_slug}/?accept=text/markdown"
                unit_filename = f"{unit_slug}.md"
                unit_file = mod_dir / unit_filename
                try:
                    unit_md = fetch_url(unit_url)
                    save_markdown_file(unit_file, unit_md, f"Unit: {unit_title}")
                    stats["units"] += 1
                    stats["total_files"] += 1
                except Exception as e:
                    print(f"      [ERROR] Failed to fetch unit '{unit_slug}': {e}")
                    stats["errors"].append((f"Unit {mod_info['id']}/{unit_slug}", unit_url, str(e)))

                time.sleep(0.15)  # brief polite delay

    # Summary
    print("\n" + "=" * 70)
    print("DOWNLOAD SUMMARY")
    print("=" * 70)
    print(f"Courses saved:        {stats['courses']}")
    print(f"Learning paths saved: {stats['paths']}")
    print(f"Modules saved:        {stats['modules']}")
    print(f"Units saved:          {stats['units']}")
    print(f"Total files written:  {stats['total_files']}")
    if stats["errors"]:
        print(f"\nErrors encountered ({len(stats['errors'])}):")
        for item, url, err in stats["errors"]:
            print(f" - {item} ({url}): {err}")
    else:
        print("\nAll documents downloaded and front-matter cleaned successfully with 0 errors!")

    return 0 if not stats["errors"] else 1


if __name__ == "__main__":
    sys.exit(main())
