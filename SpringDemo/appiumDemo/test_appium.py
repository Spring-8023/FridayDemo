# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction


class TestAppium:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        # caps["deviceName"] = "emulator-5554"
        caps["deviceName"] = "0123456789ABCDEF"
        caps["appPackage"] = "com.xtuone.android.syllabus"
        caps["appActivity"] = "com.xtuone.android.friday.InitActivity"
        caps["autoGrantPermissions"] = True
        caps["noReset"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)




    def login(self):


        # self.driver.find_element_by_id("dlg_btn_sure").click()

        self.driver.implicitly_wait(5)

        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'账号密码登录')]").click()
        # 输入账号
        self.driver.find_element_by_id("user_login_edt_account").send_keys("jin2@xt.com")
        # 输入密码
        self.driver.find_element_by_id("user_login_edt_password").send_keys("134679")

        self.driver.find_element_by_id("user_login_btn_one").click()

        self.driver.implicitly_wait(35)

        for i in range(4):
            sleep(5)
            TouchAction(self.driver).press(x=23, y=912).move_to(x=87, y=888).release().perform()
            # TouchAction(driver).press(x=743, y=912).move_to(x=203, y=903).release().perform()

            # self.driver.swipe(23, 912, 87, 888, 5)
            # sleep(5)

    def treehold(self):


    # 首页tab/rbtn_tab_social  下课聊/rbtn_tab_playground   课程表/rbtn_tab_course  小纸条/rbtn_tab_papers  我/rbtn_tab_settings
        self.driver.find_element_by_id("rbtn_tab_playground").click()
        # self.driver.find_element_by_xpath("//@resource-id='com.xtuone.android.syllabus:id/rbtn_tab_playground'").click()
        assert self.driver.find_element_by_id("tv_hot_title").text == "今日热议"

    def test_course1(self):
        # sleep(10)
        self.driver.find_element_by_id("campus_news_item_head_tip").click()
        print(self.driver.find_element_by_id("rbtn_tab_course").is_selected())
        assert self.driver.find_element_by_id("rbtn_tab_course").is_selected() == True


    def teardown(self):
        sleep(10)
        self.driver.quit()



