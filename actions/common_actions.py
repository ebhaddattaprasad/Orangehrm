from playwright.sync_api import expect

from page_objects.common_page import CommonPage


class CommonActions:
    def __init__(self, page) -> None:
        self.page = page
        self.common_page = CommonPage(page)

    def navigate_to_left_sidebar_item(self, option_name: str) -> None:
        sidebar_locator = self.common_page.NAVIGATION_LEFT_SIDEBAR_ITEM.copy()
        sidebar_locator["name"] = option_name
        expect(self.page.get_by_role(**sidebar_locator)).to_be_visible()
        self.page.get_by_role(**sidebar_locator).click()

        header_locator = self.common_page.HEADER_TEXT.copy()
        header_locator["name"] = option_name
        expect(self.page.get_by_role(**header_locator)).to_be_visible()

    def navigate_to_sub_sidebar_item(self, option_name: str) -> None:
        sub_sidebar_locator = self.common_page.SUB_SIDEBAR_ITEM.copy()
        sub_sidebar_locator["name"] = option_name
        expect(self.page.get_by_role(**sub_sidebar_locator)).to_be_visible()
        self.page.get_by_role(**sub_sidebar_locator).click()

        sub_header_locator = self.common_page.SUB_SIDEBAR_ITEM.copy()
        sub_header_locator["name"] = option_name
        expect(self.page.get_by_role(**sub_header_locator)).to_be_visible()