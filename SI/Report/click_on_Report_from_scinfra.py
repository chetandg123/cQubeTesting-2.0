import time

from selenium.common import exceptions

from Data.parameters import Data


class check_schoolinfra_report():
    def __init__(self,driver):
        self.driver = driver

    def test_report(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        try:
            time.sleep(3)
            self.driver.find_element_by_id(Data.Dashboard).click()
            time.sleep(2)
            text = self.driver.find_element_by_id(Data.Dashboard).text
            print(text)
            self.driver.find_element_by_xpath(Data.School_infra).click()
            time.sleep(3)
            self.driver.find_element_by_id(Data.Report).click()
            time.sleep(3)
            if "school-infrastructure" in self.driver.current_url:
                print("Shool infrastructure report page")
            else:
                print("School infrastructure report page is not exist")
            return text
        except exceptions.NoSuchElementException:
            print("school infra report page is present on screen")
            time.sleep(5)