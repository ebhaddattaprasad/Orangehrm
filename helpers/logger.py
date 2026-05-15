"""Simple logger factory used by actions/helpers."""

from __future__ import annotations

import logging

from configs.project_config import get_log_level_name, get_log_profile

# file | line | method() — makes it easy to jump to the keyword during troubleshooting
LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(name)s | "
    "%(filename)s:%(lineno)d | %(funcName)s() | %(message)s"
)
LOG_DATE_FORMAT = "%H:%M:%S"


def _resolve_log_level() -> int:
    """Map configured level name to a ``logging`` level constant."""
    level_name = get_log_level_name()
    return getattr(logging, level_name, logging.INFO)


def configure_root_logging() -> None:
    """Apply framework log level to the root logger (used by pytest ``log_cli``)."""
    level = _resolve_log_level()
    root = logging.getLogger()
    root.setLevel(level)


def get_logger(logger_name: str) -> logging.Logger:
    """
    Return a configured logger.

    Use ``logger_name_for_class()`` for action/page classes.
    Set ``[logging].level`` in ``project.toml`` or ``LOG_LEVEL`` env to control output.

    Loggers propagate to root so pytest ``log_cli`` prints them in the terminal.
    """
    configure_root_logging()
    logger = logging.getLogger(logger_name)
    logger.propagate = True
    level = _resolve_log_level()
    logger.setLevel(level)
    return logger


def logger_name_for_class(cls: type, profile: str) -> str:
    """Build a logger name like ``default.actions.common_actions.CommonActions``."""
    qualified = f"{cls.__module__}.{cls.__name__}"
    return f"{profile}.{qualified}" if profile else qualified


class LoggableMixin:
    """
    Adds ``self.logger`` after the rest of the cooperative ``__init__`` chain.

    Use on page objects and action (keyword) classes::

        self.logger.info("successful")
        self.logger.debug("successful")
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.logger = get_logger(logger_name_for_class(self.__class__, get_log_profile()))
