import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class donwload_blockwise_csv():
    def __init__(self,driver):
        self.driver = driver

    def test_blockwise(self):
        p =pwd()
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        District_wise=Select(self.driver.find_element_by_id("downloader"))
        District_wise.select_by_visible_text(" Block_Wise Report ")
        time.sleep(5)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(10)
        self.filename = p.get_download_dir() + "/Block_level_CRC_Report.csv"
        time.sleep(4)
        return os.path.isfile(self.filename)
    def remove_file(self):
        os.remove(self.filename)

