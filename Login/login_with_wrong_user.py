import time

from Data.parameters import Data


class login_with_unuser():
    def __init__(self,driver):
        self.driver = driver
    def test_unuser(self):

        self.driver.find_element_by_id(Data.email).send_keys("xyz@")
        self.driver.find_element_by_id(Data.passwd).send_keys("tibi")
        time.sleep(2)
        self.driver.find_element_by_id(Data.login).click()
        time.sleep(3)
        errormsg = self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[2]/div[2]/form/div[1]/div/label").text
        return errormsg
