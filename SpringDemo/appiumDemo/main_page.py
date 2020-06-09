from appium import webdriver

from SpringDemo.appiumDemo.course_page import CoursePage
from SpringDemo.appiumDemo.treehole_page import TreeholePage


class MainPage:
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

    def to_course(self):

        return CoursePage

    def to_treehole(self):
        return TreeholePage


    def ad(self):
        #
        # self.driver.find_element_by_accessibility_id("Friday").click()
        #
        # self.driver.find_element_by_id("title_item_back").click()

        self.driver.find_element_by_id("treehole_banner_image").click()
        self.driver.find_element_by_id("topic_info_announcement_name").text

        return self