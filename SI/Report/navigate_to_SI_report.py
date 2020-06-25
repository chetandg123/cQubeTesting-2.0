import time

from Data.parameters import Data


class si_report():
    def __init__(self,driver):
        self.driver = driver
    def test_url(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        print("school infra report page")
        time.sleep(5)


