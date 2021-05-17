import os
from selenium.webdriver.support.select import Select
from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class download_district_wise_csv():
    def __init__(self,driver):
        self.driver =driver

    def test_districtwise(self):
        self.cal = GetData()
        self.fname = file_extention()
        self.driver.implicitly_wait(20)
        management = self.driver.find_element_by_id('nm').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        p =pwd()
        count = 0
        District_wise=Select(self.driver.find_element_by_name("downloadType"))
        District_wise.select_by_index(1)
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download_scator).click()
        self.cal.page_loading(self.driver)
        self.filename = p.get_download_dir() + "/" + self.fname.sc_district()+management+'_allDistricts_'+self.cal.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            print('File is not downloaded ')
            count = count + 1
        else:
            print('Block level file is downloaded')
            os.remove(self.filename)
        return count


