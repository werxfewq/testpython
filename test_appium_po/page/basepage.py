from selenium.webdriver.remote.webdriver import WebDriver
from test_appium_po.driver.driver import Driver


class BasePage:
    def __init__(self, driver:WebDriver):
        self.driver=driver
    def find(self):
        #todo 处理弹窗，异常处理 动态元素的浮动处理
        pass