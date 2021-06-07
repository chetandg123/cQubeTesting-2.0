
import time
import unittest

from CRC.check_clusterwise_records import crc_schoolevel_records
from CRC.check_crc_block_per_district_csv_download import blockwise
from CRC.check_crc_tabledata_by_districtwise import schoolwise_tabledata
from CRC.check_crc_tabledata_by_selecting_districts import districtwise_tabledata
from CRC.check_districtwise_records import test_crc_report_districtwise
from CRC.check_homebtn import Homeicon
from CRC.check_table_data_order import Check_order_of_tabledata

from CRC.check_total_no_of_visited_in_districtwise import visited
from CRC.check_total_no_of_visits_in_districtwise import school_visits
from CRC.check_totalschools_count_in_districtwise import school_count
from CRC.check_xaxis_and_yaxis_from_selectbox import plot_values
from CRC.download_blockwise_csv import donwload_blockwise_csv
from CRC.download_clusterwise_csv import load_clusterwise_csv

from CRC.download_districtwise_csv import Districtwise_donwload
from CRC.download_schoolwise_csv import school_wise_download
from CRC.navigate_to_crc_and_click_on_logout import Logout_function
from CRC.navigate_to_crc_report import loading_crc
from CRC.navigate_to_dashboard import Dashboard_menu

from reuse_func import GetData


class cQube_CRC_Report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
            self.data = GetData()
            self.driver = self.data.get_driver()
            self.data.open_cqube_appln(self.driver)
            self.data.login_cqube(self.driver)
            self.data.navigate_to_crc_report()
            self.data.page_loading(self.driver)

    def test_navigate_crc(self):
        b = loading_crc(self.driver)
        res = b.test_crc()
        if "crc-report" in self.driver.current_url:
            print("Navigated back to crc report")
        else:
            print("CRC report is not loaded ")
        self.data.page_loading(self.driver)

    def test_download_districtwise(self):
        b = Districtwise_donwload(self.driver)
        result = b.test_districtwise()
        self.assertEqual(0, result, msg="File is not downloaded")
        print("district wise csv file is downloaded ")
        self.data.page_loading(self.driver)

    def test_download_blockwise_csv(self):
        b = donwload_blockwise_csv(self.driver)
        result = b.test_blockwise()
        self.assertEqual(0, result, msg="File is not downloaded")
        print("blockwise csv file is downloaded ")
        self.data.page_loading(self.driver)

    def test_download_clusterwise_csv(self):
        b = load_clusterwise_csv(self.driver)
        result = b.test_clusterwise()
        self.assertEqual(0, result, msg="File is not downloaded")
        print("cluster wise csv file is downloaded ")
        self.data.page_loading(self.driver)

    def test_download_schoolwise(self):
        b = school_wise_download(self.driver)
        result = b.test_schoolwise()
        self.assertEqual(0, result, msg="File is not downloaded")
        print("district wise csv file is downloaded ")
        self.data.page_loading(self.driver)

    def test_crc_districtwise(self):
        b = test_crc_report_districtwise(self.driver)
        result = b.test_districtwise()
        self.assertEqual(0, result, msg="File is not downloaded")
        print('checked with districts records')
        self.data.page_loading(self.driver)

    def test_homeicon(self):
        b = Homeicon(self.driver)
        result = b.test_homeicon()
        self.assertTrue(result, msg="Home button not working ")
        print("checking with home icon and it is working ")
        self.data.page_loading(self.driver)

    def test_schools_per_cluster_csv_download1(self):
        school = crc_schoolevel_records(self.driver)
        result = school.check_csv_download()
        self.assertEqual(result, 0, msg='csv file is not downloaded')
        self.data.page_loading(self.driver)

    def test_districtwise_tabledata(self):
        b = districtwise_tabledata(self.driver)
        result = b.test_table_data()
        if result != 0:
            raise self.failureException('Data not found on table')
        print("checked with districtwise table data")
        self.data.page_loading(self.driver)

    def test_logout(self):
        b = Logout_function(self.driver)
        res = b.test_logout()
        if "crc-report" in self.driver.current_url:
            print("Navigated back to crc report")
        else:
            print("CRC report is not loaded ")
        self.data.page_loading(self.driver)

    def test_crc_graph(self):
        b = plot_values(self.driver)
        res1, res2 = b.test_plots()
        self.assertNotEqual(0, res1, msg="Xaxis options are not present")
        self.assertNotEqual(0, res2, msg='Yaxis options are not present')
        self.data.page_loading(self.driver)
        print("checked graph x and y axis options")

    def test_orderwise_tabledata(self):
        b = Check_order_of_tabledata(self.driver)
        result = b.test_order()
        self.assertEqual(result, "menu", msg="Menu is not exist")
        print("check order of table records is working ")
        self.data.page_loading(self.driver)


    def test_homebutton(self):
        b = Homeicon(self.driver)
        result = b.test_homebutton()
        self.assertEqual(0, result, msg="Home button is not working ")
        print("checking with home icon and it is working ")
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()