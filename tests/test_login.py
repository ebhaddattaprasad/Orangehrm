"""Example tests demonstrating test case id tagging + JSON data usage."""

import pytest

from actions.login_actions import LoginActions
from page_objects.login_page import LoginPage


@pytest.mark.test_case_id("test_case_001")
def test_valid_login(page, env_config: dict, case_data: dict) -> None:
    login_page = LoginPage(page)
    login_actions = LoginActions(login_page)

    base_url = case_data.get("base_url", env_config["base_url"])
    username = case_data.get("username", env_config["username"])
    password = case_data.get("password", env_config["password"])
    expected_url_keyword = case_data.get("expected_url_keyword", "/dashboard")

    login_actions.login(base_url, username, password)

    assert expected_url_keyword in page.url
    assert login_page.wait_for_dashboard_loaded()
