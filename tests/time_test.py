import pytest
from playwright.sync_api import Page

from actions.common_actions import CommonActions
from actions.dashboard_functions_actions import DashboardActions
from actions.time_actions import TimeActions
from configs.env_config import get_user_credentials
from page_objects.login_page import LoginPage


@pytest.mark.key(id="PORTAL-T201")
def test_no_timesheet_found_for_the_employee(page: Page, get_test_data) -> None:
    """TC201: No timesheet found for the employee."""
    login_page = LoginPage(page)
    common_actions = CommonActions(page)
    dashboard_actions = DashboardActions(page, login_page)
    time_actions = TimeActions(page)
    admin_credentials = get_user_credentials("admin")
    test_data = get_test_data("PORTAL-T201")

    dashboard_actions.login_and_wait_for_dashboard(**admin_credentials)
    dashboard_actions.verify_dashboard_loaded()
    common_actions.navigate_to_left_sidebar_item(test_data["sidebar_item"])
    # Capture string from function 1, pass to function 2
    employee_name = time_actions.get_the_first_entry_from_employee_list()
    time_actions.click_on_search_button_and_enter_the_employee_name(employee_name)
    time_actions.click_on_view_button()
    time_actions.verify_no_timesheets_found_for_the_employee()


@pytest.mark.key(id="PORTAL-T202")
def test_verify_timesheet_for_the_employee(page: Page, get_test_data) -> None:
    """TC202: Verify punch in and out for the employee."""
    login_page = LoginPage(page)
    common_actions = CommonActions(page)
    dashboard_actions = DashboardActions(page, login_page)
    time_actions = TimeActions(page)
    admin_credentials = get_user_credentials("admin")
    test_data = get_test_data("PORTAL-T202")

    dashboard_actions.login_and_wait_for_dashboard(**admin_credentials)
    dashboard_actions.verify_dashboard_loaded()
    common_actions.navigate_to_left_sidebar_item(test_data["sidebar_item"])
    time_actions.select_punch_in_and_out_from_dropdown()
    time_actions.add_date_and_time(common_actions.get_today_date(), common_actions.get_today_time())
    time_actions.add_note(test_data["note"])
    time_actions.click_on_punch_in_or_out_button()
    time_actions.verify_success_message()
