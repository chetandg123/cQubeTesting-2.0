import csv
import os
import re
import time
import unittest

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData
import pandas as pd

class check_DistrictwiseCsv():

    def __init__(self, driver):
        self.driver = driver

    def click_download_csv_of_districts(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.exception_district()+management+'_overall_allGrades__allBlocks_'+cal.get_current_date()+'.csv'
        print(self.filename)
        cal.page_loading(self.driver)
        if not os.path.isfile(self.filename):
            print("Districtwise csv is not downloaded")
            count = count + 1
        else:
            # with open(self.filename) as fin:
            #     csv_reader = csv.reader(fin, delimiter=',')
            #     header = next(csv_reader)
            #     schools = 0
            #     for row in csv.reader(fin):
            #         schools += int(row[4])
            data = pd.read_csv(self.filename)
            schools = data["Total Schools With Missing Data"].sum()
            school = self.driver.find_element_by_id("schools").text
            sc = re.sub('\D', "", school)
            if int(sc) != int(schools):
                print("school count mismatched", int(sc), int(schools))
                count = count + 1
        os.remove(self.filename)
        return count


