import time

from test_appium_po.driver.driver import Driver
from test_appium_po.page.homepage import HomePage
from test_appium_po.page.profile_page import ProfilePage


class TestPorfile:
    def setup(self):
        self.driver=Driver().get_driver()
        self.homepage=HomePage(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    def test_login_wrong_phone(self):
        assert  self.homepage.goto_profile().Login("1321312","3123113") in "手机号码填写错误"
    def test_login_wrong_account(self):
        assert self.homepage.goto_profile().Login("13510234567", "3123113") in "用户名或密码错误"