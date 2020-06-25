import time

from Data.parameters import Data


class loading_crc():
    def __init__(self,driver):
        self.driver = driver

    def test_crc(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(2)
        self.driver.find_element_by_id(Data.CRC).click()
        time.sleep(4)

