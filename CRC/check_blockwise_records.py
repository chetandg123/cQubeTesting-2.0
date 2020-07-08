import csv
import os
import re
import time
import unittest

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class crc_blockwise_records():

    def __init__(self,driver):
        self.driver = driver

    def test_blockwise(self):
        p = pwd()
        self.cal = GetData()
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                self.cal.page_loading(self.driver)
                nodata = self.driver.find_element_by_id("errMsg").text
                if nodata == "No data found":
                    print(select_block.options[y].text, "no data found!")
                else:
                    self.driver.find_element_by_id(Data.Download).click()
                    time.sleep(3)
                    self.filename = p.get_download_dir() + "/Cluster_level_CRC_Report.csv"
                    if not os.path.isfile(self.filename):
                        print(select_block.options[y].text , "csv file is not downloaded")
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            schools = 0
                            vsts = 0
                            totscs = 0
                            for row in csv.reader(fin):
                                schools += int(row[0])
                                vsts += int(row[13])
                                totscs += int(row[1])
                            totalschools = self.driver.find_element_by_id("schools").text
                            schoolvisited = self.driver.find_element_by_id("visited").text
                            visits = self.driver.find_element_by_id("visits").text
                            sc = re.sub('\D', "", schoolvisited)
                            vs = re.sub('\D', "", visits)
                            tsc = re.sub('\D', "", totalschools)
                            self.cal.page_loading(self.driver)
                            if int(sc) != schools:
                                print("mismatch found at", select_block.options[y].text, ":",
                                      "total no of schools visited :", schools, int(sc))
                            if int(tsc) != totscs:
                                print("mismatch found at", select_block.options[y].text, ":",
                                      "total no of schools visited :", totscs, int(tsc))
                            if int(vs) != vsts:
                                print("mismatch found at", select_block.options[y].text, ":",
                                      "total no of schools visited :", vsts, int(vs))

                        os.remove(self.filename)
