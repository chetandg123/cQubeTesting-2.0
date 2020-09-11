
import unittest

from Diksha_Reports.Diksha_table_report.check_with_timeperiods import timeperiod_options
from Diksha_Reports.Diksha_table_report.click_on_hyperlink import Diksha_hyperlink
from reuse_func import GetData
from Data.parameters import Data

from Diksha_Reports.Diksha_table_report.check_all_records_with_last7days import All_Districtwise_lastweek_record
from Diksha_Reports.Diksha_table_report.check_all_records_with_lastday import All_Districtwise_lastday_records
from Diksha_Reports.Diksha_table_report.check_all_records_with_lastmonth import All_Districtwise_lastmonth_chart
from Diksha_Reports.Diksha_table_report.check_course_records_last7days import course_districtwise_lastweek_record
from Diksha_Reports.Diksha_table_report.check_course_records_lastday import course_districtwise_lastday_records

from Diksha_Reports.Diksha_table_report.check_course_records_lastmonth import course_districtwise_lastmonth_chart
from Diksha_Reports.Diksha_table_report.check_textbook_records_of_last7days import textbook_districtwise_lastweek_record
from Diksha_Reports.Diksha_table_report.check_textbook_records_of_lastday import textbook_districtwise_lastday_records
from Diksha_Reports.Diksha_table_report.check_textbook_records_of_lastmonth import textbook_districtwise_lastmonth_chart
from Diksha_Reports.Diksha_table_report.check_with_order_of_table import Table_orderwise

from Diksha_Reports.Diksha_table_report.check_each_districts import district_list
from Diksha_Reports.Diksha_table_report.click_on_homeicon import Diksha_homeicon
from Diksha_Reports.Diksha_table_report.navigate_to_diskha_report import Diksha_page


class cQube_diskha_regression(unittest.TestCase):

    @classmethod
    def setUpClass(self):
            self.data = GetData()
            self.driver = self.data.get_driver()
            self.data.open_cqube_appln(self.driver)
            self.data.login_cqube(self.driver)
            self.data.navigate_to_diksha_table()
            self.data.page_loading(self.driver)

    # def test_Diksha_homeicon(self):
    #     b = Diksha_homeicon(self.driver)
    #     res = b.test_homeicon()
    #     #self.assertEqual(res, 0, msg="Homeicon is not working ")
    #     self.data.page_loading(self.driver)
    #
    # def test_homebtn(self):
    #     count = 0
    #     self.driver.find_element_by_xpath(Data.hyper_link).click()
    #     self.data.page_loading(self.driver)
    #     self.driver.find_element_by_id('homeBtn').click()
    #     if "home" in self.driver.current_url:
    #         print("Navigated to landing page")
    #     else:
    #         print('Home button is not working')
    #         count = count + 1
    #     self.assertEqual(0,count,msg="Home button is not working")
    #     self.data.navigate_to_diksha_table()
    #     self.data.page_loading(self.driver)
    #

    def test_navigate_dikshareport(self):
        b = Diksha_page(self.driver)
        result = b.test_navigation()
        print("Navigation to diksha report is working")
        self.data.page_loading(self.driver)

    def test_timeperiods(self):
        b = timeperiod_options(self.driver)
        res = b.test_districts()
        self.assertNotEqual(0, res, msg="Time period options are not exists ")



    def test_choosedistricts(self):
        b = district_list(self.driver)
        res = b.test_each_districts()
        print('Each districts are displaying records on screen')
        self.assertNotEqual(0, res, msg="Districts are missing ")
        self.data.page_loading(self.driver)

    #
    # def test_all_last7days(self):
    #     b = All_Districtwise_lastweek_record(self.driver)
    #     res = b.test_each_districts()
    #     self.assertEqual(0, res, msg="Some mismatch found at file records and table records")
    #     self.data.page_loading(self.driver)


    def test_all_lastday(self):
        b = All_Districtwise_lastday_records(self.driver)
        res = b.test_each_districts()
        self.assertEqual(0, res, msg="Some mismatch found at file records and table records")
        self.data.page_loading(self.driver)

    #
    # def test_all_lastmonth(self):
    #     b = All_Districtwise_lastmonth_chart(self.driver)
    #     res = b.test_each_districts()
    #     self.assertEqual(0, res, msg="Some mismatch found at file records and table records")
    #     self.data.page_loading(self.driver)
    #
    # def test_course_last7days(self):
    #     b = course_districtwise_lastweek_record(self.driver)
    #     res = b.test_each_districts()
    #     self.assertEqual(0, res, msg="Some mismatch found at file records and table records")
    #     self.data.page_loading(self.driver)
    #
    #
    # def test_course_lastday(self):
    #     b = course_districtwise_lastday_records(self.driver)
    #     res = b.test_each_districts()
    #     self.assertEqual(0, res, msg="Some mismatch found at file records and table records")
    #     self.data.page_loading(self.driver)
    #
    #
    # def test_course_lastmonth(self):
    #     b = course_districtwise_lastmonth_chart(self.driver)
    #     res = b.test_each_districts()
    #     self.assertEqual(0, res, msg="Some mismatch found at file records and table records")
    #     self.data.page_loading(self.driver)
    #
    #
    # def test_textbook_last7days(self):
    #     b = textbook_districtwise_lastweek_record(self.driver)
    #     res = b.test_each_districts()
    #     self.assertEqual(0, res, msg="Some mismatch found at file records and table records")
    #     self.data.page_loading(self.driver)
    #
    #
    # def test_textbook_lastday(self):
    #     b = textbook_districtwise_lastday_records(self.driver)
    #     res = b.test_each_districts()
    #     self.assertEqual(0, res, msg="Some mismatch found at file records and table records")
    #     self.data.page_loading(self.driver)
    #
    #
    # def test_textbook_lastmonth(self):
    #     b = textbook_districtwise_lastmonth_chart(self.driver)
    #     res = b.test_each_districts()
    #     self.assertEqual(0, res, msg="Some mismatch found at file records and table records")
    #     self.data.page_loading(self.driver)

    def test_hyperlink(self):
        b = Diksha_hyperlink(self.driver)
        result = b.test_hyperlink()
        print("Checking with hyper link")
        self.data.page_loading(self.driver)

    def test_tableorder(self):
        b = Table_orderwise(self.driver)
        res = b.test_tablevalue()
        print("diksha table order is changed by clicking table headers")
        self.data.page_loading(self.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()