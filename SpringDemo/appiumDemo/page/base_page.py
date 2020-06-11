from appium.webdriver.webdriver import WebDriver
from time import sleep

class BasePage:

    def __init__(self, driver=None):
        self.driver: WebDriver = driver


    def find_by_id(self, id):
        return self.driver.find_element_by_id(id)

    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def is_element_exist(self):
        # source = self.driver.page_source
        # print(source)
        # if element in source:
        #     return True
        # else:
        #     return False

        sleep(3)
        source = self.driver.page_source
        print(source)
        #
        if 'ignore_top' in source:

             print('存在')
        else:
            print('不存在')
        # # 闪屏跳过按钮  ignore_top
        #
        #
        # if self.driver.find_element_by_id('ignore_top') != []:
        #     print(self.driver.find_element_by_id('ignore_top'))
        #     print(True)
        # else:
        #
        #     print(False)

