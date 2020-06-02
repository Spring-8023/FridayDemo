# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "spring"
caps["appPackage"] = "com.xtuone.android.syllabus"
caps["appActivity"] = "com.xtuone.android.friday.InitActivity"
caps["autoGrantPermissions"] = True
caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)

# el1 = driver.find_element_by_id("com.xtuone.android.syllabus:id/dlg_btn_sure")
# el1.click()

el2 = driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'账号密码登录')]")
el2.click()

el2 = driver.find_element_by_id("com.xtuone.android.syllabus:id/user_login_edt_account")
el2.click()

el2.send_keys("jin2@xt.com")
el3 = driver.find_element_by_id("com.xtuone.android.syllabus:id/user_login_edt_password")
el3.click()

el3.send_keys("134679")
el4 = driver.find_element_by_id("com.xtuone.android.syllabus:id/user_login_btn_one")
el4.click()




'''
# el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.CheckBox")
el2 = driver.find_element_by_class_name('android.widget.CheckBox')
el2.click()

# el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.TextView")
el3 = driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"本机号码一键登录")]')
el3.click()
'''
driver.quit()