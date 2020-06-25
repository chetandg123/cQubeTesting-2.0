import time

from Data.parameters import Data
from reuse_func import GetData


class CRC_report():
    def __init__(self,driver):
        self.driver = driver

    def test_crc_report(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
