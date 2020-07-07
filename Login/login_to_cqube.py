import time

from Data.parameters import Data
from reuse_func import GetData


class Login_to_cqube():
    def __init__(self,driver):
        self.driver =driver

    def test_login(self):
        self.p = GetData()
        self.driver.find_element_by_id(Data.email).send_keys(self.p.get_username())
        self.driver.find_element_by_id(Data.passwd).send_keys(self.p.get_password())
        self.driver.find_element_by_id(Data.login).click()
        self.p.page_loading(self.driver)
        time.sleep(2)
        self.driver.find_element_by_id(Data.logout).click()

