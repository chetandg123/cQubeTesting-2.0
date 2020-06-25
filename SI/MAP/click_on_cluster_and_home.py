import time



from Data.parameters import Data



class click_cluster_and_home():
    def __init__(self,driver):
        self.driver=driver
    def test_cluster(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.scm_dist).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(Data.scm_blk).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(Data.scm_clust).click()
        time.sleep(3)
        lists = self.driver.find_elements_by_class_name(Data.dots)
        time.sleep(2)
        count = len(lists)-1
        self.driver.find_element_by_id(Data.homeicon).click()
        time.sleep(5)
        return count