"""Login page object with locators and elementary interactions."""

from playwright.sync_api import Page


class LoginPage:
    DASHBOARD_HEADER = "h6:has-text('Dashboard')"
    ERROR_MESSAGE = ".oxd-alert-content-text"

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url)

    def enter_username(self, username: str) -> None:
        username_input = self.page.get_by_role("textbox", name="Username")
        username_input.click()
        username_input.fill(username)

    def enter_password(self, password: str) -> None:
        password_input = self.page.get_by_role("textbox", name="Password")
        password_input.click()
        password_input.fill(password)

    def click_login(self) -> None:
        self.page.get_by_role("button", name="Login").click()

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).inner_text()

    def wait_for_dashboard_loaded(self, timeout_ms: int = 15000) -> bool:
        self.page.wait_for_url("**/dashboard/**", timeout=timeout_ms)
        self.page.locator(self.DASHBOARD_HEADER).first.wait_for(state="visible", timeout=timeout_ms)
        return True
