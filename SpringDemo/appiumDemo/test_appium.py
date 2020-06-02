# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

class TestAppium:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "spring"
        caps["appPackage"] = "com.xtuone.android.syllabus"
        caps["appActivity"] = "com.xtuone.android.friday.InitActivity"
        caps["autoGrantPermissions"] = True
        # caps["noReset"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)


    def test_login(self):


        el1 = self.driver.find_element_by_id("com.xtuone.android.syllabus:id/dlg_btn_sure")
        el1.click()

        el2 = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'账号密码登录')]")
        el2.click()

        el2 = self.driver.find_element_by_id("com.xtuone.android.syllabus:id/user_login_edt_account")
        el2.click()
        # 输入账号
        el2.send_keys("jin2@xt.com")
        el3 = self.driver.find_element_by_id("com.xtuone.android.syllabus:id/user_login_edt_password")
        el3.click()
        # 输入密码
        el3.send_keys("134679")
        el4 = self.driver.find_element_by_id("com.xtuone.android.syllabus:id/user_login_btn_one")
        el4.click()

        # 首页tab/rbtn_tab_social  下课聊/rbtn_tab_playground   课程表/rbtn_tab_course  小纸条/rbtn_tab_papers  我/rbtn_tab_settings
        el5 = self.driver.find_element_by_xpath("//@resource-id='com.xtuone.android.syllabus:id/rbtn_tab_papers'")
        el5.click()


        for i in range(4):

            self.driver.swipe(10, 30, 15, 30, 5)

        self.driver.quit()


