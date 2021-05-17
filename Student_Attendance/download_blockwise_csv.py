import csv
import os
import re
import time

import pandas as pd

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class BlockwiseCsv():

    def __init__(self, driver, year, month):
        self.driver = driver
        self.year = year.strip()
        self.month = month.strip()

    def click_download_icon_of_blocks(self):
        cal = GetData()
        file = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.year,self.month = cal.get_student_month_and_year_values()
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        cal.page_loading(self.driver)
        time.sleep(5)
        if 'No data found' in self.driver.page_source:
            print("Year and month does not having data showing no data found")
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(5)
            p = pwd()
            count=0
            self.filename = p.get_download_dir() +file.student_block_download()+name+'_allBlocks_'+self.month+'_'+self.year+'_'+cal.get_current_date()+".csv"
            print(self.filename)
            if os.path.isfile(self.filename) != True:
                print('Block level csv file is not downloaded')
                count = count + 1
            else:
                df = pd.read_csv(self.filename)
                student = df['Number Of Students'].sum()
                sch=df['Number Of Schools'].sum()

                students = self.driver.find_element_by_id("students").text
                stds = re.sub('\D', "", students)

                school  = self.driver.find_element_by_id('schools').text
                scs = re.sub('\D',"",school)

                if int(stds) != int(student):
                    print('Number of students with missing data mismatch found', stds, student)
                    count = count + 1
                if int(scs) != int(sch):
                    print('Number of schools with missing data mismatch found', scs, sch)
                    count = count + 1
                os.remove(self.filename)

            return count


