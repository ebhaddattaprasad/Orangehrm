"""Base page providing shared Playwright primitives."""

from __future__ import annotations

from playwright.sync_api import Page

from helpers.logger import LoggableMixin


class BasePage(LoggableMixin):
    def __init__(self, page: Page) -> None:
        self.page = page
        super().__init__()
