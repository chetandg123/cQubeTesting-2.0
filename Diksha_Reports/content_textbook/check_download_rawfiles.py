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
        times = Select(self.driver.find_element_by_name('timePeriod'))
        times.select_by_index(1)
        if " No Data Available " in self.driver.page_source:
            print(times.first_selected_option.text,"is not having data..")
            return count
        else:
            self.driver.find_element_by_id('rawDownload').click()
            time.sleep(35)
            timeperiod = (times.first_selected_option.text).lower()
            self.filename = self.p.get_download_dir() + "/"+timeperiod+".csv"
            if os.path.isfile(self.filename) != True:
                print(timeperiod,'raw file is not downloaded')
                count = count + 1
            else:
                 print(timeperiod,'raw file is downloaded..')
                 os.remove(self.filename)
            return count

    def test_last_30_days_rawfile_download(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        times.select_by_index(2)
        time.sleep(3)
        if " No Data Available " in self.driver.page_source:
            print(times.first_selected_option.text,"is not having data..")
            return count
        else:
            self.driver.find_element_by_id('rawDownload').click()
            time.sleep(35)
            timeperiod = (times.first_selected_option.text.replace("","_")).lower()
            self.filename = self.p.get_download_dir() + "/last_30_days"+".csv"
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print(timeperiod,'raw file is not downloaded')
                count = count + 1
            else:
                 print(timeperiod,'raw file is downloaded..')
                 os.remove(self.filename)
            return count

    def test_last_7_days_rawfile_download(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        times.select_by_index(3)
        time.sleep(3)
        if " No Data Available " in self.driver.page_source:
            print(times.first_selected_option.text,"is not having data..")
            return count
        else:
            self.driver.find_element_by_id('rawDownload').click()
            time.sleep(35)
            timeperiod = (times.first_selected_option.text.replace("","_")).lower()
            self.filename = self.p.get_download_dir() + "/last_7_days"+".csv"
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print(timeperiod,'raw file is not downloaded')
                count = count + 1
            else:
                 print(timeperiod,'raw file is downloaded..')
                 os.remove(self.filename)
            return count

    def test_last_day_rawfile_download(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        times.select_by_index(4)
        time.sleep(5)
        if " No Data Available " in self.driver.page_source:
            print(times.first_selected_option.text,"is not having data..")
            return count
        else:
            self.driver.find_element_by_id('rawDownload').click()
            time.sleep(35)
            timeperiod = (times.first_selected_option.text.replace("","_")).lower()
            self.filename = self.p.get_download_dir() + "/last_day"+".csv"
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print(timeperiod,'raw file is not downloaded')
                count = count + 1
            else:
                 print(timeperiod,'raw file is downloaded..')
                 os.remove(self.filename)
            return count
