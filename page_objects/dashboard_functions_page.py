"""Dashboard page object with basic dashboard-level interactions."""

from playwright.sync_api import Page


class DashboardPage:
    DASHBOARD_HEADER = "h6:has-text('Dashboard')"
    USER_DROPDOWN = ".oxd-userdropdown-tab"
    TIME_AT_WORK_WIDGET = "text=Time at Work"
    ADMIN_LINK = "span:has-text('Admin')"
    MY_ACTIONS = "text=My Actions"

    def __init__(self, page: Page) -> None:
        self.page = page

    def wait_for_dashboard_loaded(self, timeout_ms: int = 15000) -> None:
        """Wait until dashboard URL and key dashboard header are visible."""
        self.page.wait_for_url("**/dashboard/**", timeout=timeout_ms)
        self.page.locator(self.DASHBOARD_HEADER).first.wait_for(state="visible", timeout=timeout_ms)

    def is_dashboard_visible(self) -> bool:
        """Return True if dashboard header is visible."""
        return self.page.locator(self.DASHBOARD_HEADER).first.is_visible()
