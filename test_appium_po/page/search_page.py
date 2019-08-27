from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from test_appium_po.page.basepage import BasePage


class SearchPage(BasePage):


    def search(self, keyword):
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")\
            .send_keys(keyword)
        return self

    def select(self, index):
        self.driver.find_elements_by_id("name")[index].click()
        return self

    def get_price(self, stock_type):
        price = float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'stockCode') and @text='"
            + stock_type
            + "']/../../.."
            "//*[contains(@resource-id, 'current_price')]").text)
        return price

    def get_name(self):
        return self.driver.page_source

    def add_optional(self):
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id,'follow_btn') and @instance='9']").click()
        return self
    def get_optional(self):
        text=self.driver.find_element(By.XPATH, "//*[contains(@resource-id,'follow_btn') and @instance='9']").get_attribute("text")
        return text

    def get_hint(self):
        text=self.driver.find_element(By.XPATH, "//*[@text='添加成功']").get_attribute("text")
        return text
