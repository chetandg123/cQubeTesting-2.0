import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from reuse_func import GetData


class Hyperlink():
    def __init__(self,driver):
        self.driver = driver

    def click_on_hyperlinks(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        dist = Select(self.driver.find_element_by_name("myDistrict"))
        dist.select_by_index(1)
        time.sleep(4)
        block = Select(self.driver.find_element_by_name("myBlock"))
        block.select_by_index(1)
        time.sleep(4)
        cluster = Select(self.driver.find_element_by_name("myCluster"))
        cluster.select_by_index(1)
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.school_hyper).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Data.cluster_hyper).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Data.dist_hyper).click()
        time.sleep(4)
        result1 = self.driver.find_element_by_name('myBlock').is_displayed()
        time.sleep(2)
        result2 = self.driver.find_element_by_name('myCluster').is_displayed()
        time.sleep(2)
        dist = Select(self.driver.find_element_by_name('myDistrict'))
        choose_dist = dist.first_selected_option.text
        time.sleep(5)
        return result1, result2, choose_dist