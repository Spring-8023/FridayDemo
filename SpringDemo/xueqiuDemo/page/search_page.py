from SpringDemo.xueqiuDemo.page.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def search(self, keyword):
        self.find_by_id("search_input_text").send_keys(keyword)
        self.find_by_id('name').click()

        return self

    def get_price(self, keyword=None):
        price = self.find_by_id('current_price').text

        return float(price)