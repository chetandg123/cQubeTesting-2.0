import time


from Data.parameters import Data


class clusterwise_download():
    def __init__(self,driver):
        self.driver =driver

    def test_download(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        self.driver.find_element_by_id(Data.scm_cluster).click()
        time.sleep(10)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        time.sleep(3)
        count =len(dots)-1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        return count

