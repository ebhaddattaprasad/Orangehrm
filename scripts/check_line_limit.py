"""Fail if Python files exceed a configured line limit."""

from __future__ import annotations

import sys
from pathlib import Path

MAX_LINES = 500
TARGET_DIRS = ("tests", "page_objects", "actions")


def _iter_python_files(root: Path):
    for directory in TARGET_DIRS:
        base = root / directory
        if not base.exists():
            continue
        yield from base.rglob("*.py")


def main() -> int:
    root = Path.cwd()
    violations: list[tuple[Path, int]] = []

    for file_path in _iter_python_files(root):
        line_count = sum(1 for _ in file_path.open("r", encoding="utf-8"))
        if line_count > MAX_LINES:
            violations.append((file_path, line_count))

    if not violations:
        return 0

    print(f"Line limit check failed (max {MAX_LINES} lines):")
    for file_path, line_count in violations:
        relative_path = file_path.relative_to(root)
        print(f" - {relative_path}: {line_count} lines")
    return 1


if __name__ == "__main__":
    sys.exit(main())
