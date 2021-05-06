import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from reuse_func import GetData


class TotalStudentsSchools():
    def __init__(self, driver):
        self.driver = driver

    global student_count

    def block_cluster_schools_footer_info(self):
        cal = GetData()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)

        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(4)

        schools = self.driver.find_element_by_id('schools').text
        scs = re.sub('\D','',schools)

        student = self.driver.find_element_by_id('students').text
        stds = re.sub('\D','',student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        attds = re.sub('\D','',attended)


        self.driver.find_element_by_id(Data.block_btn).click()
        cal.page_loading(self.driver)

        dots = self.driver.find_elements_by_class_name(Data.dots)
        bmarkers= len(dots)-1
        schools = self.driver.find_element_by_id('schools').text
        bscs = re.sub('\D', '', schools)

        student = self.driver.find_element_by_id('students').text
        bstds = re.sub('\D', '', student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        battds = re.sub('\D', '', attended)


        self.driver.find_element_by_id(Data.cluster_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(10)
        cmarkers= len(dots)-1
        schools = self.driver.find_element_by_id('schools').text
        cscs = re.sub('\D', '', schools)

        student = self.driver.find_element_by_id('students').text
        cstds = re.sub('\D', '', student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        cattds = re.sub('\D', '', attended)



        self.driver.find_element_by_id(Data.schoolbtn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(10)
        smarkers= len(dots)-1
        schools = self.driver.find_element_by_id('schools').text
        sscs = re.sub('\D', '', schools)

        student = self.driver.find_element_by_id('students').text
        sstds = re.sub('\D', '', student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        sattds = re.sub('\D', '', attended)
        print(stds,scs,attds ,bstds,bscs,battds,cstds,cscs,cattds,sstds,sscs,sattds)

        return stds,scs,attds ,bstds,bscs,battds,cstds,cscs,cattds,sstds,sscs,sattds