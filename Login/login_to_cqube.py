import time

from Data.parameters import Data
from reuse_func import GetData


class Login_to_cqube():
    def __init__(self,driver):
        self.driver =driver

    def test_login(self):
        d = GetData()
        self.driver.find_element_by_id(Data.email).send_keys(d.get_username())
        self.driver.find_element_by_id(Data.passwd).send_keys(d.get_password())
        time.sleep(2)
        self.driver.find_element_by_id(Data.login).click()
        time.sleep(3)
        self.driver.find_element_by_id(Data.logout).click()
        time.sleep(2)

