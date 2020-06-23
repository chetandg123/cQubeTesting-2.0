import time

from Data.parameters import Data


class login_test():
    def __init__(self,driver):
        self.driver = driver

    def test_login(self):
        self.driver.find_element_by_id(Data.email).send_keys("tibil@cqe.com")
        self.driver.find_element_by_id(Data.passwd).send_keys("tibl")
        time.sleep(2)
        self.driver.find_element_by_id(Data.login).click()
        time.sleep(3)
        errormsg = self.driver.find_element_by_xpath("//p").text
        return errormsg

