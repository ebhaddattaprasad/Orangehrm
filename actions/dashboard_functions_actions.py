"""Reusable dashboard actions for authenticated users."""

from actions.login_actions import LoginActions
from page_objects.dashboard_functions_page import DashboardPage
from page_objects.login_page import LoginPage
from playwright.sync_api import expect


class DashboardActions:
    def __init__(self, page, login_page: LoginPage) -> None:
        self.login_actions = LoginActions(login_page)
        self.dashboard_page = DashboardPage(page)

    def login_and_wait_for_dashboard(self, base_url: str, username: str, password: str) -> None:
        """Login with valid credentials and wait for dashboard."""
        self.login_actions.login(base_url, username, password)
        self.dashboard_page.wait_for_dashboard_loaded()

    def verify_dashboard_loaded(self) -> None:
        """Verify dashboard is loaded."""
        expect(self.dashboard_page.page.locator(self.dashboard_page.DASHBOARD_HEADER).first).to_be_visible()
        expect(self.dashboard_page.page.locator(self.dashboard_page.ADMIN_LINK).first).to_be_visible()
        expect(self.dashboard_page.page.locator(self.dashboard_page.MY_ACTIONS).first).to_be_visible()

    