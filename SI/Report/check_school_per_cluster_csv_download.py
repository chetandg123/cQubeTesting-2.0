import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class School_per_csv():

    def __init__(self,driver):
        self.driver =driver

    def test_search(self):
        print("school level table data is loading and csv downloaded")
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        select_cluster = Select(self.driver.find_element_by_name('myCluster'))
        count = 0
        cl = len(select_cluster.options)-1
        p =pwd()
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            time.sleep(2)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                time.sleep(2)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    time.sleep(2)
                    self.driver.find_element_by_id('download').click()
                    time.sleep(3)
                    filename = p.get_download_dir() + "/schoolPerCluster_report.csv"
                    if os.path.isfile(filename) != True:
                        print("District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    if os.path.isfile(filename) == True:
                        os.remove(filename)

        return cl





