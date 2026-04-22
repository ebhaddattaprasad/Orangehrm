"""Dashboard-focused tests for post-login workflows."""

import pytest
from playwright.sync_api import Page

from actions.dashboard_functions_actions import DashboardActions
from configs.env_config import get_user_credentials
from page_objects.login_page import LoginPage


@pytest.mark.key(id="PORTAL-T3625")
def test_case_001_user_logged_in(page: Page, get_test_data) -> None:
    """TC001: Login and land on dashboard for further development."""
    login_page = LoginPage(page)

    dashboard_actions = DashboardActions(page, login_page)

    admin_credentials = get_user_credentials("admin")
    test_data = get_test_data("PORTAL-T3625")

    dashboard_actions.login_and_wait_for_dashboard(
        admin_credentials["base_url"],
        admin_credentials["username"],
        admin_credentials["password"],
    )
    assert test_data["expected_url_keyword"] in page.url
    dashboard_actions.verify_dashboard_loaded()


@pytest.mark.key(id="PORTAL-T3626")
def test_case_002_user_logged_in(page: Page, get_test_data) -> None:
    """TC001: Login and land on dashboard for further development."""
    login_page = LoginPage(page)
    dashboard_actions = DashboardActions(page, login_page)

    admin_credentials = get_user_credentials("admin")
    test_data = get_test_data("PORTAL-T3626")

    dashboard_actions.login_and_wait_for_dashboard(
        admin_credentials["base_url"],
        admin_credentials["username"],
        admin_credentials["password"],
    )
    assert test_data["expected_url_keyword"] in page.url
    dashboard_actions.verify_dashboard_loaded()
