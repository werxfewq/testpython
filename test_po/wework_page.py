import time
from selenium import webdriver

class WeWork:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait( 3 )
        # self.driver.get('https://testerhome.com')

        url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        self.driver.get( url )
        cookies = {
            "wwrtx.vst": "xlw72UZVDWpUfirbTpKOXTj8MNVPVVCS-UUxoesFAzCD-bjag1w95i_iPjJ2Sg6odo-Wpu78hIQfQuPXcefKe_8EslBFdEix53Zv7gKxKk21bMOHO9fhLqj4IX9nqXEmG7QFvFAAxp4eIydhXyeh5ZlQW6B_AjWFa6yCCO05w-_7wpvEWI04hh9nQEneoEo_MoVtw1eJxNXWA-S2fsI5iAKgBmO9-ZfJyXbImIF2oRlJxctK2eCrqF0i7kA8ubdKJdlyS2_dhfWD2hTViaE6TQ",
            "wwrtx.d2st": "a5383987",
            "wwrtx.sid": "NdhFhwA3Kd-hy4x35N0D37c25G06m8LF2Raq0du09CRJadkEAKV9cwhqtQbfammv",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970325033079206",
            "wwrtx.vid":"1688852475034664",
            "wxpay.vid": "1688852475034664",
        }
        for k, v in cookies.items():
            self.driver.add_cookie( {"name": k, "value": v} )
        self.driver.get( url )
    def quit(self):
        self.driver.quit()

