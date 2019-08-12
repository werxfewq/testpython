from time import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from test_po.base_page import BasePage


class ProfilePage(BasePage):
    _edit=(By.CSS_SELECTOR,".ww_operationBar .js_edit")
    _username=(By.NAME, "username")
    _save=(By.CSS_SELECTOR, ".js_save")
    _disable=(By.CSS_SELECTOR,".ww_operationBar .js_disable")
    _sure=(By.XPATH,"//*[text()='确认']")
    _tips=(By.ID,"js_tips")
    # def __init__(self,driver : WebDriver):
    #     self.driver=driver
    def update(self, **kwargs):
        self.click_by_js(*self._edit)
        element=self._driver.find_element( *self._username )
        element.clear()
        element.send_keys(kwargs["name"])
        self._driver.find_element( *self._save ).click()


        pass
    def disable(self, disable):
        if self._driver.find_element(*self._disable).text == "禁用" :

            self.click_by_js(*self._disable)
            self._driver.find_element(*self._sure).click()
            element=self._driver.find_element(*self._tips).text
            assert disable == element
        else:
            return "已被禁用"

    def enable(self,enable):
        if self._driver.find_element( *self._disable ).text == "启用":
            self.click_by_js( *self._disable )
            #self._driver.find_element( *self._sure ).click()
            element_enable = self._driver.find_element( *self._tips ).text
            print(element_enable)
            assert enable == element_enable
        else:
            return "已被启用"





    def delete(self):
        pass
    def invite(self):
        pass
    # def click_by_js(self, by, locator):
    #     self.driver.execute_script("arguments[0].click();",
    #                                self.driver.find_element(by, locator)
    #                                )
