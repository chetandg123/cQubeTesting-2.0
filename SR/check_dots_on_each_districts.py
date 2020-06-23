import os
import time
import unittest

from selenium.webdriver.support.select import Select

from Data.parameters import Data


class DotsOnDistricts():
    def __init__(self, driver):
        self.driver = driver

    def check_dots_on_each_districts(self):
        self.driver.find_element_by_css_selector('p >span').click()
        time.sleep(5)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        count = 0
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            time.sleep(3)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            if int(len(dots) - 1) == 0:
                print("District" + select_district.first_selected_option.text + "Markers are not found")
                count = count + 1

        return count
