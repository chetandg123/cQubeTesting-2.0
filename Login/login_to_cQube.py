import time

from Data.parameters import Data
from reuse_func import GetData


class Login_to_cQube():
    def __init__(self,driver):
        self.driver = driver
    def test_home(self):
        p = GetData()
        p.login_cqube(self.driver)
        if "home" in self.driver.current_url:
            print("Home page")
        else:
            print("Home page is not loaded")
        time.sleep(2)
        self.driver.find_element_by_id(Data.logout).click()
        time.sleep(3)
