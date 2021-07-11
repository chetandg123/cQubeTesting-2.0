import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class Schools():
    def __init__(self, driver):
        self.driver = driver

    def check_markers_on_schools_map(self):
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        cal = GetData()
        time.sleep(10)
        cal.page_loading(self.driver)
        result = self.driver.find_elements_by_class_name(Data.dots)
        return   result

    def test_academicYear_dropdown(self):
        cal = GetData()
        count = 0
        p = pwd()
        cal.page_loading(self.driver)
        cal.click_on_state(self.driver)
        time.sleep(2)
        academic = Select(self.driver.find_element_by_id('academicYear'))
        opt = len(academic.options)-1
        for i in range(1,len(academic.options)):
             academic.select_by_index(i)
             time.sleep(3)
             year = academic.first_selected_option.text+""
             self.driver.find_element_by_id('downloadRaw').click()
             time.sleep(5)
             self.filename = p.get_download_dir()+"/student_attendance_all_districts_"+year+".csv"
             if self.filename != True:
                 print(year,'raw file is not downloaded')
                 count = count + 1
             else:
                 print(year,"raw file is downloaded")
                 os.remove(self.filename)
        return count,opt


    def test_click_on_trends_link(self):
        cal = GetData()
        count = 0
        p = pwd()
        cal.page_loading(self.driver)
        cal.click_on_state(self.driver)
        self.driver.find_element_by_id('trends').click()
        time.sleep(2)
        if "student-attendance-chart" in self.driver.current_url:
            print("Trend chart screen is displayed ")
        else:
            print("Trend chart is not displayed")
            count = count + 1
        return count