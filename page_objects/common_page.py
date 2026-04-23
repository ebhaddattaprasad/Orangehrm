"""Common page object locators."""

from page_objects.base_page import BasePage


class CommonPage(BasePage):
    NAVIGATION_LEFT_SIDEBAR_ITEM = {"role": "link", "exact": True}
    HEADER_TEXT = {"role": "heading", "exact": True}
    SUB_SIDEBAR_ITEM = {"role": "link", "exact": True}
