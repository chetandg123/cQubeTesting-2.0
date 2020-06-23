import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class donwload_clusterwise_csv():
    def __init__(self,driver):
        self.driver = driver

    def test_clusterwise(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        p =pwd()
        District_wise=Select(self.driver.find_element_by_name("downloadType"))
        District_wise.select_by_index(3)
        time.sleep(5)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(20)
        self.filename = p.get_download_dir() + "/Cluster_level_Infra_Report.csv"
        return os.path.isfile(self.filename)

    def remove_csv(self):
        os.remove(self.filename)


