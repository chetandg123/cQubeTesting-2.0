import time


from Data.parameters import Data


class cluster_level_map_check():
    def __init__(self,driver):
        self.driver = driver
    def test_blockwise_data(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.scm_dist).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.scm_blk).click()
        time.sleep(3)
        lists = self.driver.find_elements_by_class_name(Data.dots)
        time.sleep(2)
        count = len(lists)-1
        time.sleep(2)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        return count