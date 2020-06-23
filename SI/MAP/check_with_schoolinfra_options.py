import time


from Data.parameters import Data


class School_infra_options():
    def __init__(self,driver):
        self.driver = driver

    def test_options(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.School_infra).click()
        time.sleep(3)
        report = self.driver.find_element_by_id(Data.Report).text
        mapreport = self.driver.find_element_by_id(Data.Reportmap).text
        return report , mapreport



