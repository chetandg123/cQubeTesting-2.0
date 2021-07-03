


import unittest

from Diksha_Reports.usage_by_course import usage_by_course_regression_suite
from Diksha_Reports.usage_by_textbook import usage_by_textbook_regression_suite
from Diksha_Reports.content_course import content_course_regression_suite
from Diksha_Reports.content_textbook import content_textbook_regression_suite
from Diksha_TPD.TPD_Completion_percentage import completion_regression_test
from Diksha_TPD.TPD_Course_Progress import lpd_content_regression_test
from Diksha_TPD.TPD_Enrollment_completion import enrollment_regression_test
from Diksha_TPD.TPD_Teacher_Percentage import lpd_percentage_regression_test
from Teacher_Attendance import teacher_attendance_regression_testing

from get_dir import pwd

from reuse_func import GetData
from HTMLTestRunner import HTMLTestRunner


class MyTestSuite_Diksha_tpds(unittest.TestCase):

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
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_diksha_content_course()
            if 'No data found' in self.driver.page_source:
                print('Diksha Content Course Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                    content_course_regression_suite.cQube_content_course_regression)
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "w")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Content BY Course Regression Test Infra_Table_Report',
                    verbosity=1,)
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue02(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_diksha_content_textbook()
            if 'No data found' in self.driver.page_source:
                print('Diksha Content Textbook Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        content_textbook_regression_suite.cQube_content_textbook_regression
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Content By Textbook report Regression Test Infra_Table_Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue03(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_column_course()
            if 'No data found' in self.driver.page_source:
                print('Diksha usage by course Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        usage_by_course_regression_suite.cQube_diskha_course_regression_report
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' Usage By Course Infra_Table_Report Regression Test Infra_Table_Report',
                    verbosity=1,

                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue04(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_column_textbook()
            if 'No data found' in self.driver.page_source:
                print('Diksha usage by textbook Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                       usage_by_textbook_regression_suite.cQube_usage_textbook_regression_report
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' Usage By Textbook Infra_Table_Report Regression Test Infra_Table_Report',
                    verbosity=1,

                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue05(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_content_progress()
            if 'No data found' in self.driver.page_source:
                print('TPD Course Progress Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        lpd_content_regression_test.cQube_lpdcontent_regression_Test
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD course Progress Regression Test Infra_Table_Report',
                    verbosity=1,)
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")



    def test_issue06(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_percentage_progress()
            if 'No data found' in self.driver.page_source:
                print('TPD Course Percentage Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        lpd_percentage_regression_test.cQube_lpdpercentage_regression_Test
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD Percentage Progress Regression Test Infra_Table_Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue07(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_enrollment_report()
            if 'No data found' in self.driver.page_source:
                print('TPD Enrollment/Completion Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        enrollment_regression_test.cQube_enrollment_regression
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD Enrollment Regression Test Infra_Table_Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")


    def test_issue08(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_completion_percentage()
            if 'No data found' in self.driver.page_source:
                print('TPD Completion Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        completion_regression_test.cQube_completion_percentage_regression
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD Completion percentage Regression Test Infra_Table_Report',
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