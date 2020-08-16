import os
import time
import unittest

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class Test_Telemetry(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.p = pwd()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.page_loading(self.driver)
        self.data.login_to_adminconsole(self.driver)
        time.sleep(2)
        self.data.navigate_to_telemetry()
        time.sleep(3)

    def test_navigate_to_telemetry(self):
        count = 0
        # self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('homeBtn').click()
        self.data.page_loading(self.driver)
        if "" in self.driver.page_source:
            print("Admin console landing page is displayed")
        else:
            print("homebutton is not working ")
            count = count + 1
        self.data.page_loading(self.driver)
        self.data.navigate_to_telemetry()
        self.assertEqual(0,count,msg='Homebtn is not worked ')
        self.driver.find_element_by_id(Data.homeicon).click()
        self.data.page_loading(self.driver)

    def test_navigate_by_dashboard(self):
        count = 0
        # self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('homeBtn').click()
        self.data.page_loading(self.driver)
        self.test_navigate_to_telemetry()
        if '' in self.driver.current_url:
            print("Telemetry page is present ")
        else:
            print("Telemetry page is not present ")
            count = count + 1
        self.assertEqual(0,count,msg='Telemetry page is not displayed')
        self.driver.find_element_by_id(Data.homeicon).click()
        self.data.page_loading(self.driver)

    def test_click_on_blocks(self):
        # self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.sr_block_btn).click()
        self.data.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        self.assertNotEqual(0, count  , msg="Markers not present on block level ")
        self.data.page_loading(self.driver)

    def test_click_on_cluster(self):
        # self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.sr_cluster_btn).click()
        self.data.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        self.assertNotEqual(0, count  , msg="Markers not present on cluster level ")
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        self.data.page_loading(self.driver)

    # def test_click_on_school(self):
    #     self.driver.find_element_by_xpath(Data.hyper_link).click()
    #     self.data.page_loading(self.driver)
    #     self.driver.find_element_by_id(Data.sr_schools_btn).click()
    #     self.data.page_loading(self.driver)
    #     dots = self.driver.find_elements_by_class_name(Data.dots)
    #     count = len(dots) - 1
    #     self.assertNotEqual(0, count, msg="Markers not present on cluster level ")
    #     self.data.page_loading(self.driver)

    # def test_hyperlink(self):
    #     # self.driver.find_element_by_xpath(Data.hyper_link).click()
    #     self.data.page_loading(self.driver)
    #     self.driver.find_element_by_id(Data.sr_block_btn).click()
    #     # self.driver.find_element_by_xpath(Data.hyper_link).click()

    def test_yeardropdown(self):
        # self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        yearlist = Select(self.driver.find_element_by_id('year'))
        for i in range(len(yearlist.options)):
            yearlist.select_by_index(i)
            print(yearlist.options[i].text,'is selectable')
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        self.data.page_loading(self.driver)

    def test_monthdropdown(self):
        # self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        monthlist = Select(self.driver.find_element_by_id('month'))
        for i in range(len(monthlist.options)):
            monthlist.select_by_index(i)
            print(monthlist.options[i].text,'is selectable')
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        self.data.page_loading(self.driver)

    def test_datedropdown(self):
        # self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        datelist = Select(self.driver.find_element_by_id('date'))
        for i in range(len(datelist.options)):
            datelist.select_by_index(i)
            print(datelist.options[i].text,'is selectable')
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        self.data.page_loading(self.driver)

    def test_hourdropdown(self):
        # self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        hourlist = Select(self.driver.find_element_by_id('hour'))
        for i in range(len(hourlist.options)):
            hourlist.select_by_index(i)
            print(hourlist.options[i].text, 'is selectable')
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        self.data.page_loading(self.driver)

    def test_homeicon(self):
        # self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.sr_block_btn).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.sr_cluster_btn).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.sr_schools_btn).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.homeicon).click()
        self.data.page_loading(self.driver)

    def test_clickon_homebtn(self):
        count = 0
        # self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('homeBtn').click()
        self.data.page_loading(self.driver)
        self.test_navigate_to_telemetry()
        if '' in self.driver.current_url:
            print("Telemetry page is present ")
        else:
            print("Telemetry page is not present ")
            count = count + 1
        self.assertEqual(0, count, msg='Telemetry page is not displayed')
        self.driver.find_element_by_id(Data.homeicon).click()
        self.data.page_loading(self.driver)

    # def test_click_on_donwload(self):
    #     p = pwd()
    #     # self.driver.find_element_by_xpath(Data.hyper_link).click()
    #     self.data.page_loading(self.driver)
    #     self.driver.find_element_by_id(Data.Download).click()
    #     time.sleep(4)
    #     self.filename = p.get_download_dir() + '/'
    #     file = os.path.isfile(self.filename)
    #     self.assertTrue(file,msg="File is not downloaded ")
    #     self.data.page_loading(self.driver)
    #     self.driver.find_element_by_id(Data.homeicon).click()
    #     self.data.page_loading(self.driver)

    # def test_check_recordsat_eachlevel(self):
    #     p = pwd()
    #     # self.driver.find_element_by_xpath(Data.hyper_link).click()
    #     self.data.page_loading(self.driver)
    #     selectyear = Select(self.driver.find_element_by_id('year'))
    #     selectyear.select_by_index(2)
    #     selectmonth = Select(self.driver.find_element_by_id('month'))
    #     selectmonth.select_by_index(2)
    #     selectdate =Select(self.driver.find_element_by_id('date'))
    #     selectdate.select_by_index(2)
    #     selecthour = Select(self.driver.find_element_by_id('hour'))
    #     selecthour.select_by_index(2)
    #     markers = self.driver.find_elements_by_class_name(Data.dots)
    #     dots = len(markers) - 1
    #     self.assertNotEqual(0,dots,msg="Markers are not present on map ")
    #     self.driver.find_element_by_id(Data.Download).click()
    #     time.sleep(5)
    #     self.filename = p.get_download_dir() + '/'
    #     time.sleep(2)
    #     file = os.path.isfile(self.filename)
    #     self.assertTrue(file , msg='file is not downloaded')
    #     self.data.page_loading(self.driver)

    def test_logout(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.logout).click()
        time.sleep(5)
        self.assertEqual('Log in to cQube',self.driver.title,msg="logout is not working ")
        self.data.login_to_adminconsole(self.driver)
        self.data.navigate_to_telemetry()
        time.sleep(4)
        if 'telemetry' in self.driver.current_url:
            print("Telemetry page is displayed")
        else:
            print('Failed to navigate to telemetry report page ')
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()