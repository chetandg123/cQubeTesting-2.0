import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class District():
    def __init__(self, driver):
        self.driver = driver
    def remove_csv(self):
        os.remove(self.filename)

    def check_district(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(4)
        time.sleep(3)
        self.year ,self.month = cal.pat_year_month_firstselected()
        cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        count = 0
        for x in range(len(select_district.options)-5, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
            value = value[4:]+'_'
            markers = self.driver.find_elements_by_class_name(Data.dots)
            time.sleep(3)
            if (len(markers)- 1) == 0 :
                print("District" + select_district.first_selected_option.text +"no data")
                count = count + 1
            else :
                self.driver.find_element_by_id('download').click()
                time.sleep(4)
                p = pwd()
                file =file_extention()
                self.filename = p.get_download_dir() + "/"+file.pat_districtwise()+management+"_"+self.year+'_'+self.month+'_allGrades__blocks_of_district_'+value.strip()+cal.get_current_date()+'.csv'
                print(self.filename)
                if not os.path.isfile(self.filename):
                    print("District" + select_district.first_selected_option.text + "csv is not downloaded")
                    count = count + 1
                else:
                    markers = self.driver.find_elements_by_class_name(Data.dots)
                    dots = len(markers) - 1
                    with open(self.filename) as fin:
                        csv_reader = csv.reader(fin, delimiter=',')
                        header = next(csv_reader)
                        data = list(csv_reader)
                        row_count = len(data)
                        students = 0
                        schools = 0
                        attended = 0
                        for row in csv.reader(fin):
                            students += int(row[4])
                            schools += int(row[6])
                            attended += int(row[5])
                        schools = self.driver.find_element_by_id('schools').text
                        scs = re.sub('\D', '', schools)

                        student = self.driver.find_element_by_id('students').text
                        stds = re.sub('\D', '', student)

                        attended = self.driver.find_element_by_id('studentsAttended').text
                        attds = re.sub('\D', '', attended)

                        if int(dots) != row_count:
                            print("Markers and csv file records count mismatched", dots, row_count)
                            count = count + 1

                        if int(scs) != int(schools):
                            print("schools count in footer and csv file records count mismatched", int(scs) , int(schools))
                            count = count + 1

                        if int(stds) != int(students):
                            print("student count in footer and csv file records count mismatched", int(scs) , int(schools))
                            count = count + 1

                        if int(attds) != int(attended):
                            print("Attended count in footer and csv file records count mismatched", int(scs) , int(schools))
                            count = count + 1

                    os.remove(self.filename)
                return count












