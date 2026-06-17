#!/usr/bin/env python3
"""Update static GitHub stars badges in README.md."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import requests


README_PATH = Path("README.md")
BADGE_RE = re.compile(
    r"<!--stars:(?P<repo>[^>]+)-->(?P<badge>.*?)<!--/stars-->",
    re.DOTALL,
)
API_URL = "https://api.github.com/repos/{repo}"
TIMEOUT_SECONDS = 15


def format_stars(count: int) -> str:
    if count >= 1_000_000:
        value = f"{count / 1_000_000:.1f}".removesuffix(".0")
        return f"{value}M"
    if count >= 1_000:
        value = f"{count / 1_000:.1f}".removesuffix(".0")
        return f"{value}k"
    return str(count)


def fetch_stars(repo: str, token: str | None) -> int:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(API_URL.format(repo=repo), headers=headers, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    data = response.json()

    stars = data.get("stargazers_count")
    if not isinstance(stars, int):
        raise ValueError(f"GitHub API response for {repo} did not include stargazers_count")
    return stars


def build_badge(repo: str, stars: str) -> str:
    return (
        f"<!--stars:{repo}-->"
        f"![GitHub stars](https://img.shields.io/github/stars/{repo}?style=social)"
        f"<!--/stars-->"
    )


def main() -> int:
    if not README_PATH.exists():
        print("README.md not found", file=sys.stderr)
        return 1

    token = os.environ.get("GITHUB_TOKEN")
    readme = README_PATH.read_text(encoding="utf-8")
    matches = list(BADGE_RE.finditer(readme))

    if not matches:
        print("No stars badge markers found.")
        return 0

    replacements: dict[tuple[int, int], str] = {}
    had_error = False

    for match in matches:
        repo = match.group("repo").strip()
        try:
            count = fetch_stars(repo, token)
        except requests.RequestException as exc:
            print(f"{repo}: failed to fetch stars: {exc}", file=sys.stderr)
            had_error = True
            continue
        except ValueError as exc:
            print(f"{repo}: {exc}", file=sys.stderr)
            had_error = True
            continue

        formatted = format_stars(count)
        replacement = build_badge(repo, formatted)
        replacements[match.span()] = replacement

        old_badge = match.group(0)
        if old_badge == replacement:
            print(f"{repo}: already up to date ({formatted})")
        else:
            print(f"{repo}: updated to {formatted}")

    if had_error:
        return 1

    updated = readme
    for (start, end), replacement in reversed(replacements.items()):
        updated = updated[:start] + replacement + updated[end:]

    if updated == readme:
        print("README.md unchanged.")
        return 0

    README_PATH.write_text(updated, encoding="utf-8")
    print("README.md updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
