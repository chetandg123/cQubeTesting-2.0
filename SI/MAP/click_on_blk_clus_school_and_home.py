import time


from Data.parameters import Data



class click_on_home():
    def __init__(self,driver):
        self.driver =driver
    def test_home(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)

        self.driver.find_element_by_id(Data.scm_block).click()
        time.sleep(4)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        time.sleep(3)
        count1 = len(dots) - 1

        self.driver.find_element_by_id(Data.scm_cluster).click()
        time.sleep(10)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        time.sleep(3)
        count2 = len(dots) - 1
        time.sleep(5)

        self.driver.find_element_by_id(Data.scm_school).click()
        time.sleep(25)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        time.sleep(3)
        count3 = len(dots) - 1
        time.sleep(3)
        self.driver.find_element_by_id(Data.homeicon).click()
        return count1 , count2 ,count3
