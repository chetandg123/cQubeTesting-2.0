import re
import time

from Data.parameters import Data


class TotalStudents():
    def __init__(self, driver):
        self.driver = driver
        self.student_count = ''

    global student_count

    def block_total_no_of_students(self):
        self.driver.find_element_by_css_selector('p >span').click()
        total_students = self.driver.find_element_by_id(Data.students).text
        students = re.sub("\D", "", total_students)
        self.student_count = students
        time.sleep(2)
        self.driver.find_element_by_id(Data.sr_block_btn).click()
        time.sleep(15)
        Bstudents = self.driver.find_element_by_id(Data.students).text
        Bstudent = re.sub("\D", "", Bstudents)
        return self.student_count, Bstudent

    def cluster_total_no_of_students(self):
        self.driver.find_element_by_id(Data.sr_cluster_btn).click()
        time.sleep(30)
        Cstudents = self.driver.find_element_by_id(Data.students).text
        Cstudent = re.sub("\D", "", Cstudents)
        return self.student_count, Cstudent

    def schools_total_no_of_students(self):
        self.driver.find_element_by_id(Data.sr_schools_btn).click()
        time.sleep(45)
        Sstudents = self.driver.find_element_by_id(Data.students).text
        Sstudent = re.sub("\D", "", Sstudents)
        return self.student_count, Sstudent

