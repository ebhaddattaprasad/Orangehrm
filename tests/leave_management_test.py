#BASE_URL=https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
import pytest
from playwright.sync_api import Page

from actions.common_actions import CommonActions
from actions.dashboard_functions_actions import DashboardActions
from actions.leave_actions import LeaveActions
from configs.env_config import get_user_credentials
from page_objects.login_page import LoginPage


@pytest.mark.key(id="PORTAL-T001")
def test_verify_Apply_Leave_page_loads(page: Page, get_test_data) -> None:
    """TC001: Verify Apply Leave page loads."""
    login_page = LoginPage(page)
    common_actions = CommonActions(page)
    dashboard_actions = DashboardActions(page, login_page)

    admin_credentials = get_user_credentials("admin")
    test_data = get_test_data("PORTAL-T001")

    dashboard_actions.login_and_wait_for_dashboard(**admin_credentials)
    dashboard_actions.verify_dashboard_loaded()
    common_actions.navigate_to_left_sidebar_item(test_data["sidebar_item"])


@pytest.mark.key(id="PORTAL-T002")
def test_Verify_message_when_no_leave_balance_exists(page: Page, get_test_data) -> None:
    """TC002: Verify message when no leave balance exists."""
    login_page = LoginPage(page)
    common_actions = CommonActions(page)
    dashboard_actions = DashboardActions(page, login_page)
    leave_actions = LeaveActions(page)
    admin_credentials = get_user_credentials("admin")
    test_data = get_test_data("PORTAL-T002")

    dashboard_actions.login_and_wait_for_dashboard(**admin_credentials)
    dashboard_actions.verify_dashboard_loaded()
    common_actions.navigate_to_left_sidebar_item(test_data["sidebar_item"])
    leave_actions.navigate_to_apply_leave_page()


@pytest.mark.key(id="PORTAL-T003")
def test_Verify_Apply_tab_is_active_highlighted_on_load(page: Page, get_test_data) -> None:
    """TC003: Verify Apply tab is active/highlighted on load."""
    login_page = LoginPage(page)
    common_actions = CommonActions(page)
    dashboard_actions = DashboardActions(page, login_page)
    leave_actions = LeaveActions(page)
    admin_credentials = get_user_credentials("admin")
    test_data = get_test_data("PORTAL-T003")
    dashboard_actions.login_and_wait_for_dashboard(**admin_credentials)
    dashboard_actions.verify_dashboard_loaded()
    common_actions.navigate_to_left_sidebar_item(test_data["sidebar_item"])
    # leave_actions.navigate_to_apply_leave_page()
    common_actions.navigate_to_sub_sidebar_item(test_data["sub_sidebar_item"])
    leave_actions.verify_background_color_of_apply_leave_page()


@pytest.mark.key(id="PORTAL-T004")
def test_Verify_default_date_range_and_status_chips_on_load(page: Page, get_test_data) -> None:
    """TC004: Verify default date range and status chips on load."""
    login_page = LoginPage(page)
    common_actions = CommonActions(page)
    dashboard_actions = DashboardActions(page, login_page)
    leave_actions = LeaveActions(page)
    admin_credentials = get_user_credentials("admin")
    test_data = get_test_data("PORTAL-T004")
    dashboard_actions.login_and_wait_for_dashboard(**admin_credentials)
    dashboard_actions.verify_dashboard_loaded()
    common_actions.navigate_to_left_sidebar_item(test_data["sidebar_item"])
    common_actions.navigate_to_sub_sidebar_item(test_data["sub_sidebar_item"])
    leave_actions.verify_default_date_range_and_status_chips_on_load()


@pytest.mark.key(id="PORTAL-T005")
def test_Verify_Search_returns_No_Records_Found_when_no_leaves_exist(
    page: Page, get_test_data
) -> None:
    """TC005: Verify Search returns No Records Found when no leaves exist."""
    login_page = LoginPage(page)
    common_actions = CommonActions(page)
    dashboard_actions = DashboardActions(page, login_page)
    leave_actions = LeaveActions(page)
    admin_credentials = get_user_credentials("admin")
    test_data = get_test_data("PORTAL-T005")
    dashboard_actions.login_and_wait_for_dashboard(**admin_credentials)
    dashboard_actions.verify_dashboard_loaded()
    common_actions.navigate_to_left_sidebar_item(test_data["sidebar_item"])
    common_actions.navigate_to_sub_sidebar_item(test_data["sub_sidebar_item"])
    leave_actions.verify_default_date_range_and_status_chips_on_load()
    leave_actions.verify_search_returns_no_records_found_when_no_leaves_exist()
