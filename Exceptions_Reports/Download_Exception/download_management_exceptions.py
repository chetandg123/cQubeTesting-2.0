import csv
import os
import time

from selenium.webdriver.support.select import Select

from get_dir import pwd
from reuse_func import GetData


class exception_list_download():

    def __init__(self,driver):
        self.driver = driver


    def get_each_management_wise_exception_list(self):

        self.data  = GetData()
        self.driver.implicitly_wait(200)


        management_types = Select(self.driver.find_element_by_id('management'))
        # count = len(management_types.options)-1
        count = 0
        management_types.select_by_index(1)
        name = management_types.options[1].text
        time.sleep(4)
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
            time.sleep(3)

        management_types = Select(self.driver.find_element_by_id('management'))
        management_types.select_by_index(2)
        name = management_types.options[2].text
        time.sleep(4)
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
                central = row_count
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

        management_types = Select(self.driver.find_element_by_id('management'))
        management_types.select_by_index(3)
        name = management_types.options[3].text
        time.sleep(4)
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
                Govt = row_count
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

        management_types = Select(self.driver.find_element_by_id('management'))
        management_types.select_by_index(4)
        name = management_types.options[4].text
        time.sleep(4)
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
                granted = row_count
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

        management_types = Select(self.driver.find_element_by_id('management'))
        management_types.select_by_index(5)
        name = management_types.options[5].text
        time.sleep(4)
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
                model = row_count
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

        management_types = Select(self.driver.find_element_by_id('management'))
        management_types.select_by_index(6)
        name = management_types.options[6].text
        time.sleep(4)
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
                private = row_count
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

        management_types = Select(self.driver.find_element_by_id('management'))
        management_types.select_by_index(7)
        name = management_types.options[7].text
        time.sleep(4)
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
                social = row_count
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

        management_types = Select(self.driver.find_element_by_id('management'))
        management_types.select_by_index(8)
        name = management_types.options[8].text
        time.sleep(4)
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
                tribal = row_count
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
        total_managemnt = int(social + tribal + granted + Govt + central + private + model)
        if int(overall) != total_managemnt:
            print(overall,total_managemnt , 'exceptions list are not equal to all other management' )
            count = count+1
        return count

