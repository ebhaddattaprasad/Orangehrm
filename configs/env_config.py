"""Environment-backed configuration for secure test credentials."""

from __future__ import annotations

import os


def _required_env(name: str) -> str:
    """Return a required environment value or raise a helpful error."""
    value = os.getenv(name, "").strip()
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def get_user_credentials(role: str = "admin") -> dict[str, str]:
    """
    Return credentials for a role from environment variables.

    Rules:
    - `BASE_URL` is shared across all roles.
    - For `admin`, `APP_USERNAME`/`APP_PASSWORD` are used.
    - For other roles, `<ROLE>_USERNAME`/`<ROLE>_PASSWORD` are used.
      Example for role `designer`: `DESIGNER_USERNAME`, `DESIGNER_PASSWORD`.
    """
    normalized_role = role.strip().lower()
    base_url = _required_env("BASE_URL")

    if normalized_role == "admin":
        username = _required_env("APP_USERNAME")
        password = _required_env("APP_PASSWORD")
    else:
        role_key = normalized_role.upper()
        username = _required_env(f"{role_key}_USERNAME")
        password = _required_env(f"{role_key}_PASSWORD")

    return {
        "base_url": base_url,
        "username": username,
        "password": password,
    }
