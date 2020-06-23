import time

from selenium.common import exceptions

from Data.parameters import Data


class check_with_table():

    def __init__(self,driver):
        self.driver = driver

    def test_graph_and_table_present_on_school_infra(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        try:
            tablehead = self.driver.find_element_by_tag_name("table")
            return tablehead.is_displayed()

        except exceptions.NoSuchElementException:
            print("Table is present ")