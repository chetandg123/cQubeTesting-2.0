import time


from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class Logout_function():
   def __init__(self,driver):
       self.driver = driver
   def test_logout(self):
       self.driver.find_element_by_xpath(Data.hyper).click()
       time.sleep(5)
       self.driver.find_element_by_id(Data.logout).click()
       time.sleep(2)
       if "cQube" in self.driver.title:
           print("login page is displayed")
       else:
           print("logout is not working")
       time.sleep(4)
       data  = GetData()
       data.login_cqube(self.driver)
       time.sleep(3)
       data.navigate_to_crc_report()


