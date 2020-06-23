import time

from Data.parameters import Data


class check_order_of_tabledata():
    def __init__(self,driver):
        self.driver =driver
    def test_order(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        dist = self.driver.find_elements_by_xpath("//select[@name='myDistrict']/options")
        for i in range(len(dist)):
            print(dist[i].text)
