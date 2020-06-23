import time

from Data.parameters import Data


class loading_crc():
    def __init__(self,driver):
        self.driver = driver

    def test_crc(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        if "crc-report" in self.driver.current_url:
            print("CRC Report page is loaded within 3 seconds")
        else:
            print("CRC report page is not loaded within 3 seconds")
        time.sleep(3)
