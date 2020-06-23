import time


from Data.parameters import Data



class click_on_reportmap():
    def __init__(self,driver):
        self.driver =driver
    def test_reportmap(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        self.driver.find_element_by_id(Data.Dashboard).click()
        text = self.driver.find_element_by_xpath(Data.header).text
        self.driver.find_element_by_xpath(Data.School_infra).click()
        time.sleep(3)
        self.driver.find_element_by_id(Data.Reportmap).click()
        time.sleep(3)
        if "school-infra-map" in self.driver.current_url:
            print("Shool infrastructure report page")
        else:
            print("School infrastructure report page is not exist")
        time.sleep(4)
        return text
