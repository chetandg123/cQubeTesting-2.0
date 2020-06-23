import time

from Data.parameters import Data


class cluster_level_csv():
    def __init__(self,driver):
        self.driver =driver
    def test_clusterwise(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.scm_dist).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.scm_blk).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.scm_clust).click()
        time.sleep(3)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
