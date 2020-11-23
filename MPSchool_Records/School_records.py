import time
import unittest

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.select import Select

from reuse_func import GetData


class mp(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.driver.get('https://www.mponline.gov.in/Portal/Services/NTSE/NTSEReport.aspx')

    def test_fetch_allrecords(self):
        self.data = GetData()
        districts =Select(self.driver.find_element_by_id('ddlSchoolDistrict'))
        blocks = Select(self.driver.find_element_by_id("ddlBlock"))
        records = []
        for x in range(len(districts.options)-1, len(districts.options)):
                districts.select_by_index(x)
                self.data.page_loading(self.driver)
                time.sleep(3)
                for y in range(len(blocks.options) - 1, len(blocks.options)):
                    blocks.select_by_index(y)
                    time.sleep(3)
                    self.driver.find_element_by_name('btnSearch').click()
                    time.sleep(3)
                    data = self.driver.find_elements_by_xpath('//*[@id="gvSchoolDetail"]/tbody/tr')
                    for i in range(len(data)):
                        records.append(data[i].text)
                        self.data.page_loading(self.driver)

        print(records)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

