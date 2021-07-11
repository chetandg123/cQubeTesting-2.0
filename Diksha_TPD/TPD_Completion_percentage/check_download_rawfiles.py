import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class download_raw_files_for_each_time_period():
    def __init__(self,driver):
        self.driver = driver

    def test_overall_rawfile_download(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        if " No Data Available " in self.driver.page_source:
            print("Report is not having data..")
            return count
        else:
            self.driver.find_element_by_id('rawDownload').click()
            time.sleep(35)
            self.filename = self.p.get_download_dir() + "/overall.csv"
            if os.path.isfile(self.filename) != True:
                print('Downlaod raw file is not downloaded')
                count = count + 1
            else:
                 print('Download raw file is downloaded..')
                 os.remove(self.filename)
            return count

