import re
import time

from Data.parameters import Data
from reuse_func import GetData


class TotalStudents():
    def __init__(self, driver):
        self.driver = driver
        self.student_count = ''

    global student_count

    def block_total_no_of_students(self):
        state = GetData()
        state.click_on_state(self.driver)
        time.sleep(3)
        total_students = self.driver.find_element_by_id(Data.students).text
        students = re.sub("\D", "", total_students)
        self.student_count = students
        time.sleep(2)
        self.driver.find_element_by_id(Data.SAR_Blocks_btn).click()
        time.sleep(15)
        Bstudents = self.driver.find_element_by_id(Data.students).text
        Bstudent = re.sub("\D", "", Bstudents)
        return self.student_count, Bstudent

    def cluster_total_no_of_students(self):
        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        time.sleep(30)
        Cstudents = self.driver.find_element_by_id(Data.students).text
        Cstudent = re.sub("\D", "", Cstudents)
        return self.student_count, Cstudent

    def schools_total_no_of_students(self):
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        time.sleep(45)
        Sstudents = self.driver.find_element_by_id(Data.students).text
        Sstudent = re.sub("\D", "", Sstudents)
        return self.student_count, Sstudent

