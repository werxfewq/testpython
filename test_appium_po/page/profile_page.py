from selenium.webdriver.common.by import By

from test_appium_po.page.basepage import BasePage



class ProfilePage(BasePage):
    _phone_login=(By.ID,"iv_login_phone")
    _account_login=(By.ID,"tv_login_with_account")
    _account=(By.ID,"login_account")
    _password=(By.ID,"login_password")
    _next=(By.ID,"button_next")
    _content=(By.ID,"md_content")
    def Login(self,account,password):
        self.driver.find_element(*self._phone_login).click()
        self.driver.find_element(*self._account_login).click()
        self.driver.find_element(*self._account).send_keys(account)
        self.driver.find_element(*self._password).send_keys(password)
        self.driver.find_element(*self._next).click()
        text=self.driver.find_element(*self._content).get_attribute("text")
        return text
