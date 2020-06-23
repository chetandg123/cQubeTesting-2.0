import time

from Data.parameters import Data


class login_without_inputs():
    def __init__(self,driver):
        self.driver = driver
    def test_loginbtn(self):
        self.driver.find_element_by_id(Data.login).click()
        time.sleep(3)
        errormsg = self.driver.find_element_by_xpath(Data.fieldReq).text
        return errormsg


