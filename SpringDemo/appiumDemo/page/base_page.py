from appium.webdriver.webdriver import WebDriver
from time import sleep

class BasePage:

    def __init__(self, driver=None):
        self.driver: WebDriver = driver


    def find_by_id(self, id):
        return self.driver.find_element_by_id(id)

    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def is_element_exist(self, element):
        sleep(3)
        # source = self.driver.page_source
        # print(source)
        #
        # if element in source:
        #     print('存在')
        #     return True
        #
        # else:
        #     print('不存在')
        #     return False

        #
        #
        if self.driver.find_element_by_id(element) != []:
            print(self.driver.find_element_by_id(element))
            print('存在')
            return True
        else:
            print('不存在')
            return False

