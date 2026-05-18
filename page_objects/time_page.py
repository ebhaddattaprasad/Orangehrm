from page_objects.base_page import BasePage


class TimePage(BasePage):
    EMPLOYEE_FIRST_NAME = ".orangehrm-container .oxd-table-card .oxd-table-cell.oxd-padding-cell"
    EMPLOYEE_NAME_INPUT = {"role": "textbox", "name": "Type for hints..."}
    # Set "name" at runtime: dropdown.copy(); dropdown["name"] = employee_name
    EMPLOYEE_NAME_DROPDOWN = {"role": "option"}
    # Scoped via employee search row in TimeActions (avoids strict mode: many "View" buttons)
    VIEW_BUTTON = {"role": "button", "name": "View", "exact": True}
    FORM_LOCATOR = "form"
    NO_RECORDS_FOUND = {"role": "cell", "name": "No Records Found"}
    LISTITEM_LOCATOR = "listitem"
    PUNCH_IN_AND_OUT_LOCATOR = {"role": "menuitem", "name": "Punch In/Out"}
    DATE_TEXT_BOX = {"role": "textbox", "name": "yyyy-dd-mm"}
    TIME_TEXT_BOX = {"role": "textbox", "name": "hh:mm"}
    NOTE_TEXT_BOX = {"role": "textbox", "name": "Type here"}
    PUNCH_IN_BUTTON = {"role": "button", "name": "In", "exact": True}
    PUNCH_OUT_BUTTON = {"role": "button", "name": "Out", "exact": True}
    PUNCH_FORM_LOCATOR = ".orangehrm-paper-container"
    SUCCESS_MESSAGE_LOCATOR = "Success"
