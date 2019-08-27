from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_appium_po.driver.driver import Driver
from test_appium_po.page.basepage import BasePage
from test_appium_po.page.optional import Option
from test_appium_po.page.profile_page import ProfilePage
from test_appium_po.page.search_page import SearchPage


class HomePage(BasePage):
    _optional=(By.XPATH, "//*[@text='自选' and contains(@resource-id,'tab_name')]")

    def __int__(self):
        self.driver =Driver().get_driver()
    def geto_search(self):
        self.driver.find_element(By.ID,"home_search").click()
        return SearchPage(self.driver)
    def goto_profile(self):
        self.driver.find_element(By.XPATH,"//*[contains(@resource-id,'user_profile_icon') and contains(@class,'ImageView')]").click()
        return ProfilePage(self.driver)
    def goto_optional(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.text_to_be_present_in_element(
            self._optional, "自选"))
        self.driver.find_element(*self._optional).click()
        TouchAction(self.driver).tap(x=400, y=800, count=5).release().perform()
        return Option(self.driver)
