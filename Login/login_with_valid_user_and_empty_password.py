import time

from Data.parameters import Data


class login_with_no_passwd():
    def __init__(self,driver):
        self.driver = driver
    def test_nopwd(self):

        self.driver.find_element_by_id(Data.email).send_keys("xyz@gmail.com")
        time.sleep(2)
        self.driver.find_element_by_id(Data.login).click()
        time.sleep(3)
        errormsg = self.driver.find_element_by_xpath(Data.fieldReq).text
        time.sleep(2)
        self.driver.find_element_by_id(Data.email).clear()
        # self.driver.find_element_by_id(Data.passwd).clear()
        time.sleep(2)
        return errormsg
