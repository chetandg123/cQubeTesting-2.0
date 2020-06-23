import time

from Data.parameters import Data


class check_order_of_tabledata():
    def __init__(self,driver):
        self.driver =driver

    def test_tablevalue(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.d_names).click()
        time.sleep(2)
        values = self.driver.find_elements_by_xpath("//th[1]")
        for i in values:
            print(i.get_attribute("aria-sort"))

        time.sleep(6)
        self.driver.find_element_by_xpath(Data.d_names).click()
        time.sleep(2)
        value = self.driver.find_elements_by_xpath("//th[1]")
        for i in value:
            print(i.get_attribute("aria-sort"))
