import time

from Data.parameters import Data


class Check_order_of_tabledata():
    def __init__(self,driver):
        self.driver = driver
    def test_order(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        title = self.driver.find_element_by_id(Data.Dashboard).text
        time.sleep(3)
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_id(Data.CRC).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.t_head).click()
        time.sleep(2)
        values = self.driver.find_elements_by_xpath("//th[1]")
        for i in values:
            print(i.get_attribute("aria-sort"))

        time.sleep(10)
        self.driver.find_element_by_xpath(Data.t_head).click()
        time.sleep(2)
        value = self.driver.find_elements_by_xpath("//th[1]")
        for i in value:
            print(i.get_attribute("aria-sort"))

        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        return title

