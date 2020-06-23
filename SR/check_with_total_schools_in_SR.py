import re
import time

from Data.parameters import Data


class TotalSchools():
    def __init__(self, driver):
        self.driver = driver
        self.school_count = ''

    global school_count

    def block_no_of_schools(self):
        self.driver.find_element_by_css_selector('p >span').click()
        time.sleep(5)
        no_schools = self.driver.find_element_by_id(Data.schoolcount).text
        schools = re.sub("\D", "", no_schools)
        self.school_count = schools
        time.sleep(2)
        self.driver.find_element_by_id(Data.sr_block_btn).click()
        time.sleep(5)
        Bschools = self.driver.find_element_by_id(Data.schoolcount).text
        Bschools = re.sub("\D", "", Bschools)
        return self.school_count, Bschools

    def cluster_no_of_schools(self):
        self.driver.find_element_by_id(Data.sr_cluster_btn).click()
        time.sleep(30)
        Cschools = self.driver.find_element_by_id(Data.schoolcount).text
        Cschools = re.sub("\D", "", Cschools)
        return self.school_count, Cschools

    def schools_no_of_schools(self):
        self.driver.find_element_by_id(Data.sr_schools_btn).click()
        time.sleep(45)
        Sschools = self.driver.find_element_by_id(Data.schoolcount).text
        Sschools = re.sub("\D", "", Sschools)
        return self.school_count, Sschools

