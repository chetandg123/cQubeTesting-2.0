import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class donwload_clusterwise_csv():
    def __init__(self,driver):
        self.driver = driver

    def test_clusterwise(self):
        self.p = GetData()
        self.fname = file_extention()
        management = self.driver.find_element_by_id('nm').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        p =pwd()
        District_wise=Select(self.driver.find_element_by_name("downloadType"))
        District_wise.select_by_index(3)
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download_scator).click()
        time.sleep(5)
        count = 0
        self.filename = p.get_download_dir() + "/" + self.fname.sc_cluster()+management+'_allClusters_'+self.p.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            print('File is not downloaded ')
            count = count + 1
        else:
            print('Block level file is downloaded')
            os.remove(self.filename)
        return count



