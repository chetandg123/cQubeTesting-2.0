import csv
import os
import re
import time

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class DistrictwiseCsv():

    def __init__(self, driver):
        self.driver = driver

    def click_download_icon(self):
        cal = GetData()
        count =0
        management = self.driver.find_element_by_id('nm').text
        management = management[16:].lower().strip()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.pat_district()+management+'_all_allGrades__allDistricts_'+cal.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            markers = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(markers)-1
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                data = list(csv_reader)
                row_count = len(data)
                # total = 0
                # schools = 0
                # for row in csv.reader(fin):
                #     total += int(row[2])
                #     schools += int(row[3])
                # students = self.driver.find_element_by_id("students").text
                # res = re.sub('\D', "", students)
                #
                # school = self.driver.find_element_by_id("schools").text
                # sc = re.sub('\D', "", school)
                # if int(res) != total:
                #     print("student count mismatched")
                #     count = count + 1
                # if int(sc) != schools:
                #     print("school count mismatched")
                #     count = count + 1
                if int(dots) != row_count:
                    print("Markers and csv file records count mismatched",dots,row_count)
                    count = count + 1
            os.remove(self.filename)
        return count


