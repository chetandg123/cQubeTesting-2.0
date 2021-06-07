import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class download_report():
    def __init__(self,driver):
        self.driver = driver

    def test_schools(self):
        p = pwd()
        self.cal = GetData()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('nm').text
        management = management[16:].lower().strip()
        District_wise = Select(self.driver.find_element_by_id("downloader"))
        # District_wise.select_by_visible_text(" Dist Wise Infra_Table_Report ")
        District_wise.select_by_index(1)
        self.cal.page_loading(self.driver)
        self.file= file_extention()
        self.driver.find_element_by_id(Data.Download_scator).click()
        time.sleep(5)
        count = 0
        self.filename = p.get_download_dir() +'/'+ self.file.sc_district()+management+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        self.cal.page_loading(self.driver)
        if os.path.isfile(self.filename) != True:
            print("District wise csv file is not downloaded")
            count = count + 1
        os.remove(self.filename)
        return  count

