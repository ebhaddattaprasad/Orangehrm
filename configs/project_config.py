"""Load framework settings from ``project.toml`` at the repo root."""

from __future__ import annotations

import os
import tomllib
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PROJECT_TOML = ROOT_DIR / "project.toml"

_project_config: dict | None = None


def load_project_config() -> dict:
    """Return parsed ``project.toml`` (cached)."""
    global _project_config
    if _project_config is not None:
        return _project_config
    if not PROJECT_TOML.is_file():
        _project_config = {}
        return _project_config
    with PROJECT_TOML.open("rb") as config_file:
        _project_config = tomllib.load(config_file)
    return _project_config


def get_log_level_name() -> str:
    """
    Resolve log level: ``LOG_LEVEL`` env overrides ``[logging].level`` in project.toml.
    """
    env_level = os.getenv("LOG_LEVEL", "").strip()
    if env_level:
        return env_level.upper()
    logging_cfg = load_project_config().get("logging", {})
    return str(logging_cfg.get("level", "INFO")).strip().upper() or "INFO"


def get_log_profile() -> str:
    """
    Resolve log profile: ``LOG_PROFILE`` env overrides ``[logging].profile`` in project.toml.
    """
    env_profile = os.getenv("LOG_PROFILE", "").strip()
    if env_profile:
        return env_profile
    logging_cfg = load_project_config().get("logging", {})
    profile = str(logging_cfg.get("profile", "default")).strip()
    return profile or "default"
