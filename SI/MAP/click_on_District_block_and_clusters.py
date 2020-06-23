import re
import time

from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Data.parameters import Data



class select_Dist_block_cluster():
    def __init__(self,driver):
        self.driver =driver
    def test_select_district_block_cluster(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        print("ok")
    # def test_select_district_block_cluster(self):
    #         select_district = Select(self.driver.find_element_by_id("choose_dist"))
    #         select_block = Select(self.driver.find_element_by_id("choose_block"))
    #         select_cluster = Select(self.driver.find_element_by_id("choose_cluster"))
    #         count = 0
    #         for x in range(1, len(select_district.options)):
    #                 select_district.select_by_index(x)
    #                 time.sleep(4)
    #                 for y in range(1, len(select_block.options)):
    #                     select_block.select_by_index(y)
    #                     time.sleep(4)
    #                     for z in range(1, len(select_cluster.options)):
    #                         select_cluster.select_by_index(z)
    #                         time.sleep(4)
    #                         dots = self.driver.find_elements_by_class_name(Data.dots)
    #                         schools = self.driver.find_element_by_id(Data.sc_no_of_schools).text
    #                         time.sleep(4)
    #                         res = re.sub('\D',"",schools)
    #                         if int(len(dots) - 1) != int(res):
    #                                     count = count + 1
    #                                     print("no of schools and number of dots are mis matched at", select_district.options[x].text,select_block.options[y].text ,select_cluster.options[z].text )
    #         if count != 0:
    #                 raise self.failureException('data not matched')
    #













