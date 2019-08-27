from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_appium_po.page.basepage import BasePage


class Option(BasePage):

     def delete(self):
         element = self.driver.find_element(By.XPATH, "//*[@text='招商银行']")
         TouchAction(self.driver).long_press(element, 3000).release().perform()
         self.driver.find_element(By.XPATH, "//*[@text='删除']").click()
         delete_text = self.driver.find_element(By.XPATH, "//*[@text='已从自选删除']").get_attribute("text")
         return delete_text
