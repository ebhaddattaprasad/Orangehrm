"""Simple logger factory used by actions/helpers."""

from __future__ import annotations

import logging


def get_logger(profile: str, name: str) -> logging.Logger:
    """
    Return a configured logger.

    `profile` is kept to match team conventions (e.g., "default", "qa").
    """
    logger_name = f"{profile}.{name}" if profile else name
    logger = logging.getLogger(logger_name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
