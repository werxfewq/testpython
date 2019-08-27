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
    def test_delete(self):
        text =self.homepage.goto_optional().delete()
        assert text in "已从自选删除"