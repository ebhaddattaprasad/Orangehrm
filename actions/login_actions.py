"""Reusable business-level login workflows."""

from helpers.logger import LoggableMixin
from page_objects.login_page import LoginPage


class LoginActions(LoggableMixin):
    def __init__(self, login_page: LoginPage) -> None:
        self.login_page = login_page
        super().__init__()

    def login(self, base_url: str, username: str, password: str) -> None:
        self.login_page.open(base_url)
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()
