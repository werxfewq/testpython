from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class Driver:
        def __init__(self):
                caps = {}
                caps["platformName"] = "android"
                caps["deviceName"] = "hogwarts"
                caps["appPackage"] = "com.xueqiu.android"
                caps["appActivity"] = ".view.WelcomeActivityAlias"
                caps["autoGrantPermissions"] = True
                caps['automationName'] = 'uiautomator2'

                self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
                self.driver.implicitly_wait(30)
                self.driver.find_element_by_id("user_profile_icon")


        def get_driver(self):
                return self.driver