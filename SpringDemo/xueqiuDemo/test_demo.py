# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from selenium.webdriver.common.keys import Keys


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "0123456789ABCDEF"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True
        caps['autoGrantPermissions'] = True
        caps['noReset'] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("tv_agree").click()

    def test_search(self):
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys("alibaba")
        assert self.driver.find_element_by_id("name").text == "阿里巴巴"
        self.driver.find_element_by_id('name').click()
        price = self.driver.find_element_by_id('current_price').text
        assert float(price) > 200

    def teardown(self):
        sleep(5)
        self.driver.quit()
