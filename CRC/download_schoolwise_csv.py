import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class school_wise_download():
    def __init__(self,driver):
        self.driver = driver

    def test_schoolwise(self):
        count = 0
        self.cal = GetData()
        self.fname=file_extention()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('nm').text
        name = management_name[16:].strip().lower()
        p =pwd()
        District_wise=Select(self.driver.find_element_by_id("downloader"))
        # District_wise.select_by_visible_text(" School Wise Report ")
        District_wise.select_by_index(4)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        self.cal.page_loading(self.driver)
        self.filename = p.get_download_dir() + '/' + self.fname.crc_school()+name+'_overall_allSchools_'+self.cal.get_current_date()+'.csv'
        self.cal.page_loading(self.driver)
        if not os.path.isfile(self.filename):
            print("District wise csv file not downloaded")
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                tschools = 0
                vsts = 0
                vstd = 0
                for row in csv.reader(fin):
                    tschools += int(row[0])
                    vsts += int(row[2])
                    vstd += int(row[1])
                totalschools = self.driver.find_element_by_id("schools").text
                visited = self.driver.find_element_by_id("visited").text
                visits = self.driver.find_element_by_id("visits").text
                tsc = re.sub('\D', "", totalschools)
                vs = re.sub('\D', "", visits)
                vd = re.sub('\D', "", visited)
                if int(tsc) != tschools:
                    print("total no of schools  :", tschools,
                          int(tsc), "records are mismatch found")
                    count = count + 1
                if int(vs) != vsts:
                    print("total no of visits  :", int(vs), vsts,
                          "records are mismatch found")
                    count = count + 1
                if int(vd) != vstd:
                    print("Total no of visits  :", int(vd), vstd,
                          "records are mismatch found")
                    count = count + 1

            os.remove(self.filename)
        return count


