import time


from Data.parameters import Data


class check_markers_on_map():
    def __init__(self,driver):
        self.driver = driver
    def test_map(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        time.sleep(3)
        count = len(dots)-1
        return count
