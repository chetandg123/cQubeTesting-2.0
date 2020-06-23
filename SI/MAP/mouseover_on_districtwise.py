import time

from Data.parameters import Data
from reuse_func import GetData


class mouseover():
    def __init__(self,driver):
        self.driver = driver
    def test_mousehover(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        print("Mousehover on each markers..")
        # self.data.test_mouse_over()
        time.sleep(3)
