from appium import webdriver
from selenium.webdriver.common.by import By

from SpringDemo.appiumDemo.page.base_page import BasePage
from SpringDemo.appiumDemo.page.course_page import CoursePage
from SpringDemo.appiumDemo.page.treehole_page import TreeholePage
from time import sleep

class MainPage(BasePage):
    def __init__(self):
        caps = {}
        caps["platformName"] = "Android"
        # caps["deviceName"] = "emulator-5554"
        caps["deviceName"] = "0123456789ABCDEF"
        caps["appPackage"] = "com.xtuone.android.syllabus"
        caps["appActivity"] = "com.xtuone.android.friday.InitActivity"
        caps["autoGrantPermissions"] = True
        caps["noReset"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        print("成功启动")

    def to_course(self):
        sleep(10)
        print("进入首页")
        self.find_by_id("campus_news_item_head_tip").click()

        return CoursePage(self.driver)

    def to_treehole(self):
        return TreeholePage


    def ad(self, element=None):
        sleep(3)
        source = self.driver.page_source
        print(source)
        #
        # if element in source:
        #
        #      True
        # else:
        #     return False
        # # 闪屏跳过按钮  ignore_top
        #
        #
        if self.driver.find_element_by_id('ignore_top') != []:
            print(self.driver.find_element_by_id('ignore_top'))
            print(True)
        else:

            print(False)
        #
        # if BasePage().is_element_exist(args):
        #     self.find_by_id('ignore_top').click()
        # self.driver.find_element_by_accessibility_id("Friday").click()
        #
        # self.driver.find_element_by_id("title_item_back").click()

        # self.find_by_id("treehole_banner_image").click()
        # self.find_by_id("topic_info_announcement_name").text

        return self

