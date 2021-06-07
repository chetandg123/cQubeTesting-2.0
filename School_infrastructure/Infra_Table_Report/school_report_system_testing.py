

import unittest

from School_infrastructure.Infra_Table_Report.check_sc_scattor_clusterwise_records import Test_schoolwise
from School_infrastructure.Infra_Table_Report.check_table_data_metrics import download_report
from School_infrastructure.Infra_Table_Report.click_on_Report_from_scinfra import check_schoolinfra_report
from School_infrastructure.Infra_Table_Report.click_on_table_and_check_with_orderof_values import check_order_of_tabledata
from School_infrastructure.Infra_Table_Report.download_blockwise_csv import donwload_blockwise_csv
from School_infrastructure.Infra_Table_Report.download_clusterwise_csv import donwload_clusterwise_csv
from School_infrastructure.Infra_Table_Report.download_schoolwise_csv import school_wise_donwload
from reuse_func import GetData


class cQube_SI_Report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_school_infrastructure()
        self.data.page_loading(self.driver)

    def test_school_report(self):
        b = check_schoolinfra_report(self.driver)
        res = b.test_report()
        self.assertEqual("menu", res, msg="Dashboard is not exists!")
        print("Menu list is displayed")
        self.data.page_loading(self.driver)

    def test_download_district_wise(self):
        b = download_report(self.driver)
        path = b.test_schools()
        self.assertEqual(path, 0, msg="File is not downloaded")
        print("districtwise csv file is downloaded")
        self.data.page_loading(self.driver)


    def test_download_blockwise(self):
        b = donwload_blockwise_csv(self.driver)
        res = b.test_block()
        self.assertEqual(res,0, msg="File is not downloaded")
        print("blockwise csv file downloaded")
        self.data.page_loading(self.driver)

    def test_schoolwise_download(self):
        b = school_wise_donwload(self.driver)
        res = b.test_schoolwise()
        self.assertEqual(res,0, msg="File is not downloaded")
        print("school wise csv file is downloaded")
        self.data.page_loading(self.driver)

    def test_clusterwise_download(self):
        b = donwload_clusterwise_csv(self.driver)
        res = b.test_clusterwise()
        self.assertEqual(res,0, msg="File is not downloaded")
        print("cluster wise csv file is downloaded")
        self.data.page_loading(self.driver)

    def test_check_orderwise(self):
        b = check_order_of_tabledata(self.driver)
        print("Table record order wise..")
        res = b.test_tablevalue()
        print("checked with orderwise of table data")
        self.data.page_loading(self.driver)

    def test_schools_per_cluster_csv_download(self):
        school = Test_schoolwise(self.driver)
        result = school.check_csv_download1()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download1 is working")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
