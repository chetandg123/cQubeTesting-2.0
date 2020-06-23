import time

from Data.parameters import Data


class select_blockwise():
    def __init__(self,driver):
        self.driver = driver
    def test_dist_blocks(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        Districts = self.driver.find_elements_by_xpath(Data.sc_choosedist)
        blocks = self.driver.find_elements_by_xpath(Data.sc_chooseblock)
        for i in range(1,len(Districts)):
            Districts[i].click()
            print(Districts[i].text)
            time.sleep(3)

