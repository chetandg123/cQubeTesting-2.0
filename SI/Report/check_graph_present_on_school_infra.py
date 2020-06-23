import time

from Data.parameters import Data


class check_with_graph():
    def __init__(self,driver):
        self.driver = driver

    def test_graph(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        if "myChart" in self.driver.page_source:
            print("Scattor plot is present")
        else:
            print("Scattor plot is not present")
