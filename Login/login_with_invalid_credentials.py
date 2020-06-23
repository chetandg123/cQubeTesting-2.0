import time


from Data.parameters import Data
from get_dir import pwd


class login_test_invalidvalues():
    def __init__(self,driver):
        self.driver =driver
    def test_login(self):

        self.driver.find_element_by_id(Data.email).send_keys("abc@cqube.com")
        self.driver.find_element_by_id(Data.passwd).send_keys("abc123")
        time.sleep(2)
        self.driver.find_element_by_id(Data.login).click()
        time.sleep(3)
        errormsg = self.driver.find_element_by_xpath("//p").text
        time.sleep(2)
        self.driver.find_element_by_id(Data.email).clear()
        self.driver.find_element_by_id(Data.passwd).clear()
        time.sleep(2)
        return errormsg
