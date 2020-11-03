import unittest

from Diksha_Reports.Location_by_course import usage_by_course_regression_suite
from Diksha_Reports.Location_by_textbook import usage_by_textbook_regression_suite
from Diksha_Reports.content_course import content_course_regression_suite
from Diksha_Reports.content_textbook import content_textbook_regression_suite
from Pat_Heatchart import patheatchart_regression_test
from get_dir import pwd
from pat_LO_Table import PAT_LO_Table_regression_suite
from reuse_func import GetData
from HTMLTestRunner import HTMLTestRunner


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
        self.data.navigate_to_heatchart_report()
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print("No data in pat heat chart Report")
        else:
            regression_test = unittest.TestSuite()
            regression_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    patheatchart_regression_test.cQube_heatchart_regression_test
                    )
            ])
            p = pwd()
            outfile = open(p.get_regression_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' PAT Heat chart Report Regression Test Report',
                verbosity=1,

            )
            runner1.run(regression_test)
            outfile.close()

    def test_issue02(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_lo_table_report()
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print("No data in PAT LO Table Report")
        else:
            regression_test = unittest.TestSuite()
            regression_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    PAT_LO_Table_regression_suite.cQube_pat_lotable_regression_test
                )
            ])
            p = pwd()
            outfile = open(p.get_regression_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' PAT LO Table Report Regression Test Report',
                verbosity=1,

            )
            runner1.run(regression_test)
            outfile.close()

    def test_issue03(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_diksha_content_course()
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print("No data content course Report")
        else:
            regression_test = unittest.TestSuite()
            regression_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                content_course_regression_suite.cQube_content_course_regression)
            ])
            p = pwd()
            outfile = open(p.get_regression_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Content BY Course Regression Test Report',
                verbosity=1,

            )
            runner1.run(regression_test)
            outfile.close()

    def test_issue04(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_diksha_content_textbook()
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print("No data in content textbook Report")
        else:
            regression_test = unittest.TestSuite()
            regression_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    content_textbook_regression_suite.cQube_content_textbook_regression
                )
            ])
            p = pwd()
            outfile = open(p.get_regression_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Content By Textbook report Regression Test Report',
                verbosity=1,

            )
            runner1.run(regression_test)
            outfile.close()

    def test_issue05(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_column_course()
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print("No data in usage by course Report")
        else:
            regression_test = unittest.TestSuite()
            regression_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    usage_by_course_regression_suite.cQube_diskha_course_regression_report
                )
            ])
            p = pwd()
            outfile = open(p.get_regression_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' Usage By Course Report Regression Test Report',
                verbosity=1,

            )
            runner1.run(regression_test)
            outfile.close()

    def test_issue06(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_column_textbook()
        self.data.page_loading(self.driver)
        if 'No data found' in self.driver.page_source:
            print("No data in usage by textbook Report")
        else:
            regression_test = unittest.TestSuite()
            regression_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    usage_by_textbook_regression_suite.cQube_usage_textbook_regression_report
                )
            ])
            p = pwd()
            outfile = open(p.get_regression_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' Usage By Textbook Report Regression Test Report',
                verbosity=1,

            )
            runner1.run(regression_test)
            outfile.close()

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()