from playwright.sync_api import expect

from actions.common_actions import CommonActions
from helpers.logger import LoggableMixin
from page_objects.time_page import TimePage


class TimeActions(LoggableMixin):
    def __init__(self, page) -> None:
        self.page = page
        self.time_page = TimePage(page)
        self.common_actions = CommonActions(page)
        super().__init__()

    def get_the_first_entry_from_employee_list(self) -> str:
        """Read first employee name from the list and return it as a string."""
        self.logger.info("Getting the first entry from employee list")
        first_employee = self.page.locator(self.time_page.EMPLOYEE_FIRST_NAME).first
        expect(first_employee).to_be_visible()
        employee_name = first_employee.inner_text().strip()
        self.logger.info(f"First entry from employee list: {employee_name}")
        return employee_name

    def click_on_search_button_and_enter_the_employee_name(self, employee_name: str) -> None:
        """Type employee name and select matching option from the dropdown."""
        self.logger.info(f"Entering employee name: {employee_name}")
        expect(self.page.get_by_role(**self.time_page.EMPLOYEE_NAME_INPUT)).to_be_visible()
        self.page.get_by_role(**self.time_page.EMPLOYEE_NAME_INPUT).click()
        self.page.get_by_role(**self.time_page.EMPLOYEE_NAME_INPUT).fill(employee_name)

        dropdown_option = self.time_page.EMPLOYEE_NAME_DROPDOWN.copy()
        dropdown_option["name"] = employee_name
        expect(self.page.get_by_role(**dropdown_option)).to_be_visible(timeout=10000)
        self.page.get_by_role(**dropdown_option).click()
        self.logger.info(f"Selected employee from dropdown: {employee_name}")
    
    def click_on_view_button(self) -> None:
        """Click on the View button to open the timesheet."""
        self.logger.info("Clicking on the View button")
        expect(self.page.locator(self.time_page.FORM_LOCATOR).get_by_role(**self.time_page.VIEW_BUTTON)).to_be_visible()
        self.page.locator(self.time_page.FORM_LOCATOR).get_by_role(**self.time_page.VIEW_BUTTON).click()
        self.logger.info("Clicked on the View button")
    
    def verify_no_timesheets_found_for_the_employee(self) -> None:
        """Verify that no timesheets are found for the employee."""
        expect(self.page.get_by_role(**self.time_page.NO_RECORDS_FOUND)).to_be_visible()
        self.logger.info("No timesheets found for the employee")

    def select_punch_in_and_out_from_dropdown(self) -> None:
        """Select punch in and out from the dropdown."""
        expect(self.page.get_by_role(self.time_page.LISTITEM_LOCATOR).filter(has_text="Attendance")).to_be_visible()
        self.page.get_by_role(self.time_page.LISTITEM_LOCATOR).filter(has_text="Attendance").click()
        self.logger.info("Selected punch in and out from the dropdown")
        expect(self.page.get_by_role(**self.time_page.PUNCH_IN_AND_OUT_LOCATOR)).to_be_visible()
        self.page.get_by_role(**self.time_page.PUNCH_IN_AND_OUT_LOCATOR).click()
        self.logger.info("Clicked on the punch in and out button")
    
    def add_date_and_time(self, date: str, time: str) -> None:
        """Add date and time to the timesheet."""
        self.page.get_by_role(**self.time_page.DATE_TEXT_BOX).click()
        self.page.get_by_role(**self.time_page.DATE_TEXT_BOX).press("ControlOrMeta+a")
        self.page.get_by_role(**self.time_page.DATE_TEXT_BOX).fill(self.common_actions.get_today_date())
        self.page.get_by_role(**self.time_page.DATE_TEXT_BOX).press("ControlOrMeta+Tab")
        self.logger.info(f"Added date and time to the timesheet: {date}")
        self.page.get_by_role(**self.time_page.TIME_TEXT_BOX).click()
        self.page.get_by_role(**self.time_page.TIME_TEXT_BOX).press("ControlOrMeta+a")
        self.page.get_by_role(**self.time_page.TIME_TEXT_BOX).fill(self.common_actions.get_today_time())
        self.logger.info(f"Added time to the timesheet: {time}")
    
    def add_note(self, note: str) -> None:
        """Add note to the timesheet."""
        self.page.locator(".orangehrm-paper-container").click()
        self.page.get_by_role(**self.time_page.NOTE_TEXT_BOX).click()
        self.page.get_by_role(**self.time_page.NOTE_TEXT_BOX).press("ControlOrMeta+a")
        self.page.get_by_role(**self.time_page.NOTE_TEXT_BOX).fill(note)
        self.logger.info(f"Added note to the timesheet: {note}")
    
    def click_on_punch_in_or_out_button(self, button_name: str) -> None:
        """Click on the punch in or out button."""
        button_locator = self.time_page.PUNCH_IN_OR_OUT_BUTTON.copy()
        button_locator["name"] = button_name
        expect(self.page.get_by_role(**button_locator)).to_be_visible()
        self.page.get_by_role(**button_locator).click()
        self.page.get_by_role(**button_locator).click()
        self.logger.info(f"Clicked on the {button_name} button")
    
    def verify_success_message(self) -> None:
        """Verify that the punch in is successful."""
        expect(self.page.get_by_text(self.time_page.SUCCESS_MESSAGE_LOCATOR, exact=True)).to_be_visible()
        self.logger.info("Success message is visible")

    