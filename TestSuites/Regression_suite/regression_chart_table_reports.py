


from CRC import  crc_report_regression_testing
from Composite_report import composite_regression_testing
from Health_Card_Index import health_card_regression_test
from Periodic_Test_Reports.Pat_Heatchart import patheatchart_regression_test

from School_infrastructure.Infra_Table_Report import  School_report_regression_testing
from Telemetry import telemetry_regression_testing
from Periodic_Test_Reports.pat_LO_Table import PAT_LO_Table_regression_suite

from get_dir import pwd

import unittest
from HTMLTestRunner import HTMLTestRunner

from reuse_func import GetData


class MyTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)

    def test_issue01(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("crc")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_crc_report()
            if 'No data found' in self.driver.page_source:
                print('CRC Report is showing no data found!..')
                self.driver.close()
            else:
                 regression_test = unittest.TestSuite()
                 regression_test.addTests([
                        # file name .class name
                        unittest.defaultTestLoader.loadTestsFromTestCase(crc_report_regression_testing.cQube_CRC_Report),
                    ])
                 p = pwd()
                 outfile = open(p.get_regression_chart_table_reports(), "a")
                 runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Crc regression Test Report',
                    verbosity=1,)
                 runner1.run(regression_test)
                 outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")


    def test_issue02(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("infrastructure")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_school_infrastructure()
            if 'No data found' in self.driver.page_source:
                print('School infrastructure Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(School_report_regression_testing.cQube_SI_Report)
                ])
                p = pwd()
                outfile = open(p.get_regression_chart_table_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='School Infrastructure regression Table Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue05(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("composite")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_composite_report()
            if 'No data found' in self.driver.page_source:
                print('Composite Accross metrics Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(composite_regression_testing.composite_regression_report)
                ])
                p = pwd()
                outfile = open(p.get_regression_chart_table_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Composite Table Report Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")


    def test_issue06(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("pat")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_heatchart_report()
            if 'No data found' in self.driver.page_source:
                print(' PAT Heat chart Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        patheatchart_regression_test.cQube_heatchart_regression_test
                    )
                ])
                p = pwd()
                outfile = open(p.get_regression_chart_table_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' PAT Heat chart Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")


    def test_issue07(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("pat")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_lo_table_report()
            if 'No data found' in self.driver.page_source:
                print(' PAT LO Table Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        PAT_LO_Table_regression_suite.cQube_pat_lotable_regression_test
                    )
                ])
                p = pwd()
                outfile = open(p.get_regression_chart_table_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' PAT LO Table Regression Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

