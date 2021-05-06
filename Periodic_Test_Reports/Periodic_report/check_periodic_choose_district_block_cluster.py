import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class DistrictBlockCluster():
    def __init__(self, driver):
        self.driver = driver
    def remove_csv(self):
        os.remove(self.filename)

    def check_district_block_cluster(self):
        self.cal = GetData()
        self.driver.implicitly_wait(50)
        self.cal.click_on_state(self.driver)
        self.cal.page_loading(self.driver)
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(4)
        self.cal.page_loading(self.driver)
        self.fname = file_extention()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
        count = 0
        for x in range(len(select_district.options)-1,len(select_district.options)):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            for y in range(len(select_block.options)-1, len(select_block.options)):
                select_block.select_by_index(y)
                self.cal.page_loading(self.driver)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    self.cal.page_loading(self.driver)
                    value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                    value = value[3:]+'_'
                    time.sleep(3)
                    nodata = self.driver.find_element_by_id("errMsg").text
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    if len(markers) - 1 == 0:
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                        count = count + 1
                    self.driver.find_element_by_id('download').click()
                    time.sleep(3)
                    p = pwd()
                    self.filename = p.get_download_dir() +"/" + self.fname.pat_clusterwise()+value.strip()+self.cal.get_current_date()+'.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                            students = 0
                            schools = 0
                            attended = 0
                            for row in csv.reader(fin):
                                students += int(row[9])
                                schools += int(row[0])
                                attended += int(row[0])
                            schools = self.driver.find_element_by_id('schools').text
                            scs = re.sub('\D', '', schools)

                            student = self.driver.find_element_by_id('students').text
                            stds = re.sub('\D', '', student)

                            attended = self.driver.find_element_by_id('studentsAttended').text
                            attds = re.sub('\D', '', attended)


                            if int(scs) != int(schools):
                                print("schools count in footer and csv file records count mismatched", int(scs),
                                      int(schools))
                                count = count + 1

                            if int(stds) != int(students):
                                print("student count in footer and csv file records count mismatched", int(scs),
                                      int(schools))
                                count = count + 1

                            if int(attds) != int(attended):
                                print("Attended count in footer and csv file records count mismatched", int(scs),
                                      int(schools))
                                count = count + 1

                        os.remove(self.filename)
                        return count
