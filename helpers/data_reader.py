"""Utility methods for reading JSON test data."""

from __future__ import annotations

import json
from pathlib import Path


def read_json_file(file_path: Path) -> dict:
    """Read a JSON file and return a dictionary."""
    with file_path.open(mode="r", encoding="utf-8") as json_file:
        return json.load(json_file)
