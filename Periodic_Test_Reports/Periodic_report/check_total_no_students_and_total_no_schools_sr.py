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
        time.sleep(4)
        schools = self.driver.find_element_by_id('schools').text
        scs = re.sub('\D',"",schools)

        student = self.driver.find_element_by_id('students').text
        stds = re.sub('\D',"",student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        attds = re.sub('\D',"",attended)

        print('Expected Footer values : ',scs,stds,attds)
        "********************Block level Records *******************"
        self.driver.find_element_by_id(Data.block_btn).click()
        cal.page_loading(self.driver)


        schools = self.driver.find_element_by_id('schools').text
        bscs = re.sub('\D',"",schools)

        student = self.driver.find_element_by_id('students').text
        bstds = re.sub('\D',"",student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        battds = re.sub('\D',"",attended)
        count=0
        if scs != bscs:
            print('Block level schools count mismatch found','fi:'+scs,bscs)
            count = count + 1
        if stds != bstds:
            print('Block level students count mismatch found',stds,bstds)
            count = count + 1
        if attds != battds:
            print('Block level schools count mismatch found',attds,battds)
            count = count + 1
        "********************Cluster level Records *******************"
        self.driver.find_element_by_id(Data.cluster_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(10)
        schools = self.driver.find_element_by_id('schools').text
        cscs = re.sub('\D',"",schools)

        student = self.driver.find_element_by_id('students').text
        cstds = re.sub('\D',"",student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        cattds = re.sub('\D',"",attended)
        if scs != cscs:
            print('Cluster level schools count mismatch found',scs,cscs)
            count = count + 1
        if stds != cstds:
            print('Cluster level students count mismatch found',stds,cstds)
            count = count + 1
        if attds != cattds:
            print('Cluster level schools count mismatch found',attds,cattds)
            count = count + 1
        "********************School level Records *******************"
        self.driver.find_element_by_id(Data.schoolbtn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(10)
        schools = self.driver.find_element_by_id('schools').text
        sscs = re.sub('\D',"",schools)

        student = self.driver.find_element_by_id('students').text
        sstds = re.sub('\D',"",student)

        attended = self.driver.find_element_by_id('studentsAttended').text
        sattds = re.sub('\D',"",attended)

        if scs != sscs:
            print('School level schools count mismatch found', scs, sscs)
            count = count + 1
        if stds != sstds:
            print('School level students count mismatch found', stds, sstds)
            count = count + 1
        if attds != sattds:
            print('School level schools count mismatch found', attds, sattds)
            count = count + 1

        return count