import time

from Data.parameters import Data
from reuse_func import GetData


class login_test():
    def __init__(self,driver):
        self.driver = driver
    def test_login(self):
        self.url = GetData()
        self.driver.get(self.url.get_domain_name())
        self.driver.find_element_by_id(Data.email).send_keys("tibil")
        self.driver.find_element_by_id(Data.passwd).send_keys("t")
        time.sleep(2)
        self.driver.find_element_by_id(Data.login).click()
        time.sleep(3)
        errormsg = self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[2]/div[2]/form/div[2]/div/label").text
        time.sleep(2)
        self.driver.find_element_by_id(Data.email).clear()
        self.driver.find_element_by_id(Data.passwd).clear()
        time.sleep(2)
        return errormsg


