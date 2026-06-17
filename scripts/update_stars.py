#!/usr/bin/env python3
"""Update static GitHub stars badges in README.md with retry and fallback."""

from __future__ import annotations

import os
import re
import sys
import time
from pathlib import Path

import requests


README_PATH = Path("README.md")
BADGE_RE = re.compile(
    r"<!--stars:(?P<repo>[^>]+)-->(?P<badge>.*?)<!--/stars-->",
    re.DOTALL,
)
API_URL = "https://api.github.com/repos/{repo}"
TIMEOUT_SECONDS = 15
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 5


def format_stars(count: int) -> str:
    if count >= 1_000_000:
        value = f"{count / 1_000_000:.1f}".removesuffix(".0")
        return f"{value}M"
    if count >= 1_000:
        value = f"{count / 1_000:.1f}".removesuffix(".0")
        return f"{value}k"
    return str(count)


def parse_existing_stars(badge_text: str) -> str | None:
    """Extract existing star count from badge text like '⭐ 87.2k'."""
    match = re.search(r"⭐\s*([\d.]+[kM]?)", badge_text.strip())
    return match.group(1) if match else None


def fetch_stars(repo: str, token: str | None) -> tuple[int, int]:
    """Fetch stars from GitHub API. Returns (stars_count, http_status).
    Returns (0, -1) for network errors."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(API_URL.format(repo=repo), headers=headers, timeout=TIMEOUT_SECONDS)
    except requests.exceptions.RequestException:
        return 0, -1
    
    if not response.ok:
        return 0, response.status_code
    
    data = response.json()
    stars = data.get("stargazers_count")
    if not isinstance(stars, int):
        return 0, 200
    
    return stars, response.status_code


def fetch_stars_with_retry(repo: str, token: str | None) -> int | None:
    """Fetch stars with exponential backoff retry. Returns None on final failure.
    
    Only retries on rate limit (403), server errors (5xx), or network errors (-1).
    Not on auth failures (401) or missing repos (404).
    """
    for attempt in range(MAX_RETRIES):
        stars, status = fetch_stars(repo, token)
        
        if status == 200:
            return stars
        
        # Don't retry on client errors (401, 404, etc.)
        if status in (401, 404) or attempt >= MAX_RETRIES - 1:
            print(f"{repo}: {'all attempts failed' if attempt >= MAX_RETRIES - 1 else 'failed'} (HTTP {status})", file=sys.stderr)
            return None
        
        wait = RETRY_DELAY_SECONDS * (2 ** attempt)
        print(f"{repo}: attempt {attempt + 1} failed (HTTP {status}), retrying in {wait}s...", file=sys.stderr)
        time.sleep(wait)
    
    return None


def build_badge(repo: str, stars: str) -> str:
    return (
        f"<!--stars:{repo}-->"
        f"⭐ {stars}"
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
    skipped_count = 0
    updated_count = 0

    for match in matches:
        repo = match.group("repo").strip()
        old_badge = match.group(0)
        old_stars = parse_existing_stars(match.group("badge"))

        count = fetch_stars_with_retry(repo, token)
        if count is None:
            # Fallback: keep existing star count if available
            if old_stars:
                print(f"{repo}: failed to fetch, keeping existing value ({old_stars})")
                skipped_count += 1
                continue
            else:
                print(f"{repo}: failed to fetch and no existing value to keep", file=sys.stderr)
                had_error = True
                continue

        formatted = format_stars(count)
        replacement = build_badge(repo, formatted)

        if old_badge == replacement:
            print(f"{repo}: already up to date ({formatted})")
        else:
            print(f"{repo}: updated to {formatted}")
            updated_count += 1
            replacements[match.span()] = replacement

    if had_error:
        print(f"\nWarning: some repos failed and had no existing values to keep", file=sys.stderr)
        # Still proceed with partial updates rather than failing entirely

    if not replacements:
        print(f"\nREADME.md unchanged. ({skipped_count} repos skipped, {updated_count} updated)")
        return 0

    updated = readme
    for (start, end), replacement in reversed(replacements.items()):
        updated = updated[:start] + replacement + updated[end:]

    README_PATH.write_text(updated, encoding="utf-8")
    print(f"\nREADME.md updated. ({skipped_count} repos skipped, {updated_count} updated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
