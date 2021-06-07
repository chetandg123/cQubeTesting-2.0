import os
import re
import time
import unittest

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class SchoolwiseCsv():

    def __init__(self, driver):
        self.driver = driver

    def click_download_icon_of_schools(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(Data.schoolbtn).click()
        cal.page_loading(self.driver)
        time.sleep(10)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(15)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() + "/" + self.fname.sr_school()+management+'_all_allGrades__allSchools_'+cal.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            print('School level csv file is not download')
            count = count + 1
        return count
