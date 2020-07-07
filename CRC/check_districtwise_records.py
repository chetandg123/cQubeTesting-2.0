import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class test_crc_report_districtwise():

    def __init__(self,driver):
        self.driver = driver

    def test_districtwise(self):
        p = pwd()
        self.cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            nodata = self.driver.find_element_by_id("errMsg").text
            if nodata == "No data found":
                print(select_district.options[x].text, "no data found!")
            else:
                self.driver.find_element_by_id(Data.Download).click()
                time.sleep(3)
                self.filename = p.get_download_dir() + "/Block_level_CRC_Report.csv"
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    schools = 0
                    vsts = 0
                    totscs = 0
                    for row in csv.reader(fin):
                        schools += int(row[0])
                        vsts += int(row[11])
                        totscs +=int(row[1])
                    totalschools = self.driver.find_element_by_id("schools").text
                    schoolvisited = self.driver.find_element_by_id("visited").text
                    visits = self.driver.find_element_by_id("visits").text
                    sc= re.sub('\D', "", schoolvisited)
                    vs = re.sub('\D',"",visits)
                    tsc = re.sub('\D',"",totalschools)
                    self.cal.page_loading(self.driver)
                    if int(sc) != schools:
                        print("mismatch found at", select_district.options[x].text, ":", "total no of schools visited :",schools, int(sc))
                    if int(tsc) != totscs:
                        print("mismatch found at", select_district.options[x].text, ":", "total no of schools visited :",totscs, int(tsc))
                    if int(vs) != vsts:
                        print("mismatch found at", select_district.options[x].text, ":", "total no of schools visited :",vsts, int(vs))

                os.remove(self.filename)
