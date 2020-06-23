import time

from Data.parameters import Data


class login_test_with_invalid_user():
    def __init__(self,driver):
        self.driver = driver
    def test_invaliduser(self):

        self.driver.find_element_by_id(Data.email).send_keys("tibil@gmail.com")
        self.driver.find_element_by_id(Data.passwd).send_keys("tibil123")
        time.sleep(2)
        self.driver.find_element_by_id(Data.login).click()
        time.sleep(3)
        errormsg = self.driver.find_element_by_xpath("//p").text
        time.sleep(2)
        self.driver.find_element_by_id(Data.email).clear()
        self.driver.find_element_by_id(Data.passwd).clear()
        time.sleep(2)
        return errormsg
