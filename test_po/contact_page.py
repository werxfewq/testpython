import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_po.base_page import BasePage
from test_po.profile_page import ProfilePage
from test_po.wework_page import WeWork


class ContactPage(BasePage):
    _username=(By.NAME, "username" )
    _alias=(By.NAME, "english_name")
    _id=(By.NAME, "acctid")
    _mobile=(By.NAME, "mobile")
    _cancel=(By.CSS_SELECTOR,".js_btn_cancel")
    _leave=(By.XPATH,"//*[text()='离开此页']")
    _search=(By.CSS_SELECTOR,".ww_searchInput_text")
    _add =(By.CSS_SELECTOR, ".js_has_member .ww_operationBar .js_add_member")
    def __init__(self, wework: WeWork):
         self._driver =wework.driver
    def add_member(self,name, alias, id , mobile, **kwargs):
        #locator=".js_has_member .ww_operationBar .js_add_member"
        WebDriverWait( self._driver, 10, 1, ignored_exceptions=(TimeoutException) ).until(
            expected_conditions.element_to_be_clickable( self._add ) )
        self.click_by_js(*self._add)
        #self.driver.find_element(*self._username).send_keys( name )
        self.find(self._username).send_keys(name)
        #self.driver.find_element( *self._alias ).send_keys( alias )
        self.find(self._alias).send_keys(alias)
        #self.driver.find_element(*self._id ).send_keys( id )
        self.find(self._id).send_keys(id)
        #self.driver.find_element(*self._mobile ).send_keys( mobile )
        self.find(self._mobile).send_keys(mobile)
        self.click_by_js(*self._cancel)

        self.click_by_js(*self._leave)
        return self  #返回当前页面，如果跳到其它页面，就使用其他po

    def delete_member(self):
        pass
    def get_tips(self):
        return "OK"
    def search_member(self, key):
        self._driver.find_element( *self._search ).send_keys( key )
        return ProfilePage( self._driver )


    # def click_by_js(self, by, locator):
    #     self.driver.execute_script("arguments[0].click();",
    #                                self.driver.find_element(by, locator)
    #                                )