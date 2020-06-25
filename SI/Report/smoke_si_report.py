import time
import unittest

from SI.Report.check_block_per_district_csv_download import blocklevel_csv
from SI.Report.check_graph_present_on_school_infra import check_with_graph
from SI.Report.check_homebtn import home_button
from SI.Report.check_table_data_metrics import download_report

from SI.Report.check_table_present_on_schoolinfra import check_with_table
from SI.Report.check_with_hyperlink import Hyperlink
from SI.Report.click_on_district_block_cluster_home import check_home
from SI.Report.download_blockwise_csv import donwload_blockwise_csv
from SI.Report.download_districtwise_csv import download_district_wise_csv
from SI.Report.navigate_to_SI_report import si_report

from reuse_func import GetData


class cQube_SI_Report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_school_infrastructure()
        time.sleep(5)

    def test_graph(self):
        b = check_with_graph(self.driver)
        res = b.test_graph()
        self.assertIn("myChart", self.driver.page_source, msg="Does not exist")
        time.sleep(2)

    def test_home(self):
        b =home_button(self.driver)
        res = b.test_home()
        self.assertTrue(res, msg="Home button not working ")

    def test_downloadreportwise(self):
        b = download_report(self.driver)
        path = b.test_schools()
        self.assertTrue(path, msg="File is not downloaded")
        b.remove_csv()


    def test_check_hyperlinks(self):
        hyperlinks = Hyperlink(self.driver)
        result1, result2, choose_dist = hyperlinks.click_on_hyperlinks()
        if result1 == False and result2 == False and choose_dist == "Choose a District ":
            print("hyperlinks are working")
        else:
            raise self.failureException("hyperlinks are not working")


    def test_tabledata(self):
        b = check_with_table(self.driver)
        res = b.test_graph_and_table_present_on_school_infra()
        self.assertTrue(res, msg="Table is not exist")

    def test_cluster_home(self):
        b = check_home(self.driver)
        time.sleep(5)
        res = b.test_home()
        if "school-infrastructure" in self.driver.current_url:
            print("School infra report page")
        else:
            print("school infra page not loaded")
        time.sleep(2)

    def test_download_districtwise(self):
        b = download_district_wise_csv(self.driver)
        res = b.test_districtwise()
        self.assertTrue(res, msg="File is not downloaded")
        b.remove_file()

    def test_blockwise_from_selectbox(self):
        b = blocklevel_csv(self.driver)
        res = b.test_search()
        self.assertEqual(0, res, msg="Some files are not downloaded")

    def test_donwload_blockwise(self):
        b = donwload_blockwise_csv(self.driver)
        res =b.test_block()
        self.assertTrue(res, msg = "File is not downloaded")
        b.remove_csv()
        time.sleep(3)

    def test_schoolreport(self):
        b = si_report(self.driver)
        res =b.test_url()
        self.assertNotIn(" School infrastructure for: ",self.driver.page_source,msg="School infrastructure report not exist ")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()