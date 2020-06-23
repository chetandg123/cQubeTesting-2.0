import time

from selenium.common import exceptions
from selenium.webdriver.support.select import Select

from Data.parameters import Data


class Graph_values():
    def __init__(self,driver):
        self.driver =driver

    def test_plots(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        try:
            x_axis = Select(self.driver.find_element_by_id(Data.x))
            y_axis = Select(self.driver.find_element_by_id(Data.y))
            time.sleep(3)
            for x in range(1, len(x_axis.options)):
                time.sleep(2)
                x_axis.select_by_index(x)
                time.sleep(2)
                for y in range(1, len(y_axis.options)):
                    time.sleep(2)
                    y_axis.select_by_index(y)
                    time.sleep(2)
        except exceptions.NoSuchElementException:
            print("Both x and y axis are selectable ")
        # select = Select(self.driver.find_element_by_name('xAxis'))
        #
        # for index in range(len(select.options)):
        #     select = Select(self.driver.find_element_by_name('xAxis'))
        #     time.sleep(2)
        #     select.select_by_index(index)
        #     time.sleep(3)
        #     for index in range(len(select.options)):
        #         select = Select(self.driver.find_element_by_name('yAxis'))
        #         time.sleep(2)
        #         select.select_by_index(index)
        #         time.sleep(3)

