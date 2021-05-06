

import csv
import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class exception_download():

    def __init__(self,driver):
        self.driver = driver


    def get_exceptions(self):

        self.data  = GetData()
        self.driver.implicitly_wait(200)
        management_types_1 = Select(self.driver.find_element_by_id('management'))
        count = 0
        for i in range(1,len(management_types_1.options)):

            management_types = Select(self.driver.find_element_by_id('management'))
            management_types.select_by_index(i)
            name = management_types.options[i].text
            time.sleep(4)
            print(name,'is selected')
            self.driver.find_element_by_id('isdata').click()
            time.sleep(4)
            print(name, 'is selected and downloading csv file')
            self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[2]/button').click()
            time.sleep(30)
            self.p = pwd()
            self.filename = self.p.get_download_dir() + '/school_invalid_data.csv'
            if os.path.isfile(self.filename) != True:
                print(name, 'Download exception list is not downloaded ')
                count = count + 1
            else:
                with open(self.filename) as fin:
                    csv_reader = csv.reader(fin, delimiter=',')
                    header = next(csv_reader)
                    data = list(csv_reader)
                    row_count = len(data)
                    overall = row_count
                    if int(row_count) > 0:
                        print(name, row_count ,  'Exception records are present ')
                    else:
                        print(name, 'exception records are not present')
                        count = count + 1
                    # overall = 0+row_count
                    # if management_types.options[i].text in data:
                    #     print(name , 'having exception list')
                    # else:
                    #     print(name,"selected management exception is not present in downloaded file")
                    #     count = count + 1
                    os.remove(self.filename)
            self.driver.find_element_by_id('homeBtn').click()
            time.sleep(5)
        return count