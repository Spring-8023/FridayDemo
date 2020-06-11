from selenium.webdriver.common.by import By

from SpringDemo.appiumDemo.page.main_page import MainPage


class TestCoursePo:

    def test_course(self):

        # print(type(MainPage().to_course().course()))
        # assert MainPage().to_course().course() == True
        MainPage().is_element_exist()