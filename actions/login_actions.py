"""Reusable business-level login workflows."""

from page_objects.login_page import LoginPage


class LoginActions:
    def __init__(self, login_page: LoginPage) -> None:
        self.login_page = login_page

    def login(self, base_url: str, username: str, password: str) -> None:
        self.login_page.open(base_url)
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()
