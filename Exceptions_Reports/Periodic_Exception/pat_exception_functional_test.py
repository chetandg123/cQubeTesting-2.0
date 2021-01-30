# -*- coding: utf-8 -*-
import unittest
import time

from Data.parameters import Data
from Exceptions_Reports.Periodic_Exception.pat_scripts import pat_exception_report
from reuse_func import GetData


class cQube_pat_exception_functional_report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
            self.data = GetData()
            self.driver = self.data.get_driver()
            self.data.open_cqube_appln(self.driver)
            self.data.login_cqube(self.driver)
            self.data.navigate_to_semester_exception()
            self.data.page_loading(self.driver)

    def test_ClusterPerBlockCsvDownload(self):
        b = pat_exception_report(self.driver)
        res = b.ClusterPerBlockCsvDownload()
        self.assertEqual(0,res , msg='Some cluster level files are not downloaded')

    def test_DistrictwiseDownload(self):
        b = pat_exception_report(self.driver)
        res = b.check_districts_csv_download()
        self.assertEqual(0,res,msg="Some district level csv file is not downloaded")

    def test_DotsOnDistrictwise_map(self):
        b = pat_exception_report(self.driver)
        res = b.check_dots_on_each_districts()
        self.assertEqual(0,res,msg='Markers are not present on districtwise map ')

    def test_Data_not_recieved(self):
        b = pat_exception_report(self.driver)
        res,r1,r2,r3 = b.test_total_not_recieved_data()
        self.assertEqual(res,r1,msg='Block level data not recieved count mismatch found')
        self.assertEqual(res,r2,msg='cluster level data not recieved count mismatch found')
        self.assertEqual(res,r3,msg='School level data not recieved count mismatch found')

    def test_Semester_Blocks(self):
        b = pat_exception_report(self.driver)
        res = b.check_markers_on_block_map()
        self.assertNotEqual(0,res,msg="markers are not present on block level map")

    def test_semester_clusters(self):
        b = pat_exception_report(self.driver)
        res = b.check_markers_on_clusters_map()
        self.assertNotEqual(0,res,msg="markers are not present on cluster level map")

    def test_semesterschool(self):
        b = pat_exception_report(self.driver)
        res = b.check_markers_on_school_map()
        self.assertNotEqual(0,res,msg="markers are not present on cluster level map")

    def test_sem_dashboard(self):
        b = pat_exception_report(self.driver)
        res = b.test_click_on_dashboard()
        self.assertEqual(0,res,msg='Dashboard button is not working ')

    def test_sem_exception_hyperlink(self):
        b = pat_exception_report(self.driver)
        result1, result2, choose_dist = b.click_on_hyperlinks()
        if result1 == False and result2 == False and choose_dist == "Choose a District":
            print("hyperlinks are working")
        else:
            raise self.failureException("hyperlinks are not working")

    def test_semester_exception_icon(self):
        b = pat_exception_report(self.driver)
        res = b.test_icon()
        self.assertEqual(0,res,msg='Semester exception report is not displayed')

    def test_sem_exception_Logout(self):
        b = pat_exception_report(self.driver)
        res = b.click_on_logout()
        self.assertEqual(res,'Log in to cQube',msg="logout button is not working")
        self.data.login_cqube(self.driver)
        self.data.navigate_to_semester_exception()
        self.data.page_loading(self.driver)


    def test_homepage(self):
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(2)
        count =0
        self.driver.find_element_by_id('').click()
        self.data.page_loading(self.driver)
        if 'pat-exception' in self.driver.current_url:
            print("Home page of pat exception is present ")
        else:
            print('home page does not exist')
            count= count + 1
        self.assertEqual(0,count,msg='Home page not exists')



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()