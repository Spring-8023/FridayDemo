from appium.webdriver.webdriver import WebDriver

from SpringDemo.appiumDemo.page.base_page import BasePage


class CoursePage(BasePage):


    def course(self):

        r = self.find_by_id("rbtn_tab_course").is_selected()
        print("------")
        return r

        # self.driver.find_element_by_id("rbtn_tab_course").is_selected()