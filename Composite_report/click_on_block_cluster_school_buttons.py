from Data.parameters import Data
from reuse_func import GetData


class Blocks_cluster_schools_Buttons():
    def __init__(self,driver):
        self.driver = driver

    def click_on_blocks_button(self):
        count = 0
        self.data  = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.block_btn).click()
        self.data.page_loading(self.driver)
        self.data.page_loading(self.driver)
        graph = self.driver.find_element_by_id('myChart')
        result = graph.is_displayed()
        if True != result:
            print("Block level graph is not displayed ")
            count = count + 1
        return count

    def click_on_clusters_button(self):
        count = 0
        self.data  = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.block_btn).click()
        self.data.page_loading(self.driver)
        self.data.page_loading(self.driver)
        graph = self.driver.find_element_by_id('myChart')
        result = graph.is_displayed()
        if True != result:
            print("Cluster level graph is not displayed ")
            count = count + 1
        return count

    def click_on_school_button(self):
        count = 0
        self.data  = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.schoolbtn).click()
        self.data.page_loading(self.driver)
        self.data.page_loading(self.driver)
        graph = self.driver.find_element_by_id('myChart')
        result = graph.is_displayed()
        if True != result:
            print("School level graph is not displayed ")
            count = count + 1
        return count


