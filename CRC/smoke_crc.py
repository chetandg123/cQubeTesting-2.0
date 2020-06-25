
import time
import unittest

from CRC.check_crc_block_per_district_csv_download import blockwise
from CRC.check_homebtn import Homebutton
from CRC.check_performance_for_blockwise_report import download_blockwise_csv
from CRC.check_performance_for_districtwise_report import download_districtwise_csv
from CRC.check_performance_of_crc_report import CRC_report

from CRC.check_table_data_order import Check_order_of_tabledata
from CRC.check_total_no_of_visited_in_districtwise import visited
from CRC.check_total_no_of_visits_in_districtwise import school_visits
from CRC.check_xaxis_and_yaxis_from_selectbox import plot_values
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
            time.sleep(5)


    def test_download_districtwise(self):
        b = Districtwise_donwload(self.driver)
        result  = b.test_districtwise()
        print("District wise crc report download")
        self.assertTrue(result, msg="File is not downloaded")
        b.remove_csv()

    def test_download_schoolwise(self):
        b =school_wise_download(self.driver)
        res = b.test_schoolwise()
        print("schoolwise crc report download")
        self.assertTrue(res, msg="File is not downloaded")
        b.remove_file()

    def test_logout(self):
        b = Logout_function(self.driver)
        res = b.test_logout()
        if "crc-report" in self.driver.current_url:
            print("Navigated back to crc report")
        else:
            print("CRC report is not loaded ")
        time.sleep(2)

    def test_navigate_crc(self):
        b =loading_crc(self.driver)
        res = b.test_crc()
        if "crc-report" in self.driver.current_url:
            print("CRC Report page is loaded within 3 seconds")
        else:
            print("CRC report page is not loaded within 3 seconds")
        time.sleep(3)

    def test_dash_menu(self):
        b =Dashboard_menu(self.driver)
        res = b.test_dashboard()
        if "crc-report" in self.driver.current_url:
            print("Navigate back to CRC report page")
        else:
            print("CRC report page is not displayed")
        time.sleep(3)

    def test_visited(self):
        b = visited(self.driver)
        result1, result2 = b.test_schools()
        self.assertEqual(int(result1), result2, msg="total no of visited are mismatching in district level")
        b.remove_file()

    def test_visits(self):
        b = school_visits(self.driver)
        res1, res2 = b.test_visits()
        self.assertEqual(int(res1), res2, msg="total no of visits are mismatching in district level")
        b.remove_file()

    def test_crc_graph(self):
        b = plot_values(self.driver)
        result = b.test_plots()
        self.assertNotEqual(0, result, msg="Axis options are not contains in select box")

    def test_orderwise_tabledataa(self):
        b = Check_order_of_tabledata(self.driver)
        result = b.test_order()
        self.assertEqual(result ,"menu",msg="CRC Table is present..")

    def test_homeicon(self):
        b=Homebutton(self.driver)
        result = b.test_homeicon()
        self.assertTrue(result,msg="Home button not working ")

    def test_peformance_blockwise(self):
        b = download_blockwise_csv(self.driver)
        result = b.test_blockwise()
        self.assertTrue(result, msg = "File is not downloaded")
        print("Block wise csv file is downloaded within 10 seconds")
        b.remove_file()

    def test_peformance_districtwise(self):
        b = download_districtwise_csv(self.driver)
        result = b.test_districtwise_csv()
        self.assertTrue(result, msg = "File is not downloaded")
        print("district wise csv file is downloaded within 10 seconds")
        b.remove_file()

    def test_peformance_of_crc_report(self):
        b = CRC_report(self.driver)
        result = b.test_crc_report()
        if "crc-report" in self.driver.current_url:
            print("CRC Report page is loaded within 3 seconds")
        else:
            print("CRC report page is not loaded within 3 seconds")
        time.sleep(3)

    def test_blockwise_data(self):
        b = blockwise(self.driver)
        result = b.test_blocklevel()
        self.assertNotEqual(0, result, msg="Districts are present in select box")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()