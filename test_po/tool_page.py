import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_po.base_page import BasePage
from test_po.wework_page import WeWork


class ToolPage(BasePage):
    _menu_manage=(By.ID,"menu_manageTools")
    _library=(By.XPATH,"//*[text()='素材库']")
    _image=(By.CSS_SELECTOR,'a[href="#material/image"]')
    _upload=(By.CSS_SELECTOR,".js_upload_file_selector")
    _file=(By.ID,"uploadImageFile")
    _cancel=(By.CSS_SELECTOR, ".js_uploadProgress_cancel")
    def __init__(self, wework: WeWork):
         self._driver =wework.driver
    def upload_picturce(self,path):
        self.click_by_js(*self._menu_manage)
        self.click_by_js(*self._library)
        self.click_by_js(*self._image)
        self.click_by_js(*self._upload)
        self._driver.find_element(*self._file).send_keys(path)
        WebDriverWait(self._driver, 5).until(
            expected_conditions.invisibility_of_element_located(self._cancel)
        )
        self._driver.execute_script("arguments[0].click();",
                                   self._driver.find_element_by_css_selector(".js_next"))
    # def goto_picture(self):
    #     self.click_by_js(By.ID,"menu_manageTools")
    #     self.click_by_js( By.XPATH, "//*[text()='素材库']" )
    #     self.click_by_js( By.CSS_SELECTOR, 'a[href="#material/mpnews"]' )
    #     self.click_by_js(By.CSS_SELECTOR,".js_enter_create")



