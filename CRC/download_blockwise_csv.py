import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class donwload_blockwise_csv():
    def __init__(self,driver):
        self.driver = driver

    def test_blockwise(self):
        p =pwd()
        count = 0
        self.cal  = GetData()
        self.fname = file_extention()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('nm').text
        name = management_name[16:].strip().lower()
        District_wise=Select(self.driver.find_element_by_id("downloader"))
        # District_wise.select_by_visible_text(" Block Wise Report ")
        District_wise.select_by_index(2)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(4)
        self.filename = p.get_download_dir() + '/' + self.fname.crc_block()+name+'_overall_allBlocks_'+self.cal.get_current_date()+'.csv'
        print(self.filename)
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

