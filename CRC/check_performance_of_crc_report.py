import time

from Data.parameters import Data
from reuse_func import GetData


class CRC_report():
    def __init__(self,driver):
        self.driver = driver

    def test_crc_report(self):
        if "crc-report" in self.driver.current_url:
            print("CRC Report page is loaded within 3 seconds")
        else:
            print("CRC report page is not loaded within 3 seconds")
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)