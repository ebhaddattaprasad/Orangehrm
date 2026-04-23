from page_objects.base_page import BasePage


class LeavePage(BasePage):
    APPLY_LEAVE_LINK = {"role": "link", "name": "Apply"}
    APPLY_LEAVE_HEADER = "#app .orangehrm-card-container .orangehrm-main-title"
    LEAVE_BALANCE_HEADER = "#app .orangehrm-card-container .orangehrm-leave-balance"
    APPLY_LEAVE_TITLE = ".oxd-topbar-body-nav .oxd-topbar-body-nav-tab.--visited"
    MY_LEAVE_LIST_HEADER = ".oxd-table-filter-header"
    LEAVE_DROPDOWN_FILTER = ".oxd-form-row .oxd-label"
    EXPECTED_LEAVE_DROPDOWN_FILTERS = [
        "From Date",
        "To Date",
        "Show Leave with Status",
        "Leave Type",
    ]
    LEAVE_ALL_SIDEBAR_ITEMS = "#app .oxd-text.oxd-text--span"
    DATE_TEXT_BOX = {"role": "textbox", "name": "yyyy-dd-mm"}
    SEARCH_BUTTON = {"role": "button", "name": "Search"}
