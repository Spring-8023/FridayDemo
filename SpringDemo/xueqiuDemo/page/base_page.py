from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver=None):
        self.driver: WebDriver = driver

    def find_by_id(self, id):
        return self.driver.find_element_by_id(id)
