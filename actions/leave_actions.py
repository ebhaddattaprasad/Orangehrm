from playwright.sync_api import expect

from actions.common_actions import CommonActions
from helpers.logger import LoggableMixin
from page_objects.leave_page import LeavePage


class LeaveActions(LoggableMixin):
    def __init__(self, page) -> None:
        self.page = page
        self.leave_page = LeavePage(page)
        self.common_actions = CommonActions(page)
        super().__init__()

    def navigate_to_apply_leave_page(self) -> None:
        self.page.get_by_role(**self.leave_page.APPLY_LEAVE_LINK).click()
        expect(self.page.locator(self.leave_page.APPLY_LEAVE_HEADER)).to_contain_text(
            "Apply Leave", timeout=10000
        )
        expect(self.page.locator(self.leave_page.LEAVE_BALANCE_HEADER)).to_contain_text(
            "Leave Balance", timeout=10000
        )

    def verify_background_color_of_apply_leave_page(self) -> None:
        expect(self.page.locator(self.leave_page.APPLY_LEAVE_TITLE)).to_have_css(
            "background-color", "rgba(255, 123, 29, 0.1)"
        )

    def verify_default_date_range_and_status_chips_on_load(self) -> None:
        expect(self.page.locator(self.leave_page.MY_LEAVE_LIST_HEADER)).to_have_text(
            "My Leave List", timeout=10000
        )
        filter_labels = self.page.locator(self.leave_page.LEAVE_DROPDOWN_FILTER)
        expected_filters = self.leave_page.EXPECTED_LEAVE_DROPDOWN_FILTERS
        expect(filter_labels).to_have_count(len(expected_filters), timeout=10000)
        for index, expected_filter in enumerate(expected_filters):
            expect(filter_labels.nth(index)).to_contain_text(expected_filter, timeout=10000)

    def verify_search_returns_no_records_found_when_no_leaves_exist(self) -> None:
        expect(
            self.page.locator(self.leave_page.LEAVE_ALL_SIDEBAR_ITEMS).filter(
                has_text="No Records Found"
            )
        ).to_be_visible(timeout=10000)

    def add_to_from_date_filter(
        self, to_date: str | None = None, from_date: str | None = None
    ) -> None:
        """Fill To/From date filters; values can be provided by the test."""
        resolved_from_date = from_date or self.common_actions.get_last_month_date()
        resolved_to_date = to_date or self.common_actions.get_today_date()

        date_inputs = self.page.get_by_role(**self.leave_page.DATE_TEXT_BOX)

        # To Date (first date field on My Leave filter row)
        date_inputs.first.click()
        date_inputs.first.press("ControlOrMeta+a")
        date_inputs.first.fill(resolved_from_date)

        # From Date (second date field on My Leave filter row)
        date_inputs.nth(1).click()
        date_inputs.nth(1).press("ControlOrMeta+a")
        date_inputs.nth(1).fill(resolved_to_date)

    def click_search_button(self) -> None:
        self.page.get_by_role(**self.leave_page.SEARCH_BUTTON).click()
