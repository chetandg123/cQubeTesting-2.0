import unittest

from Diksha_Reports.content_course import content_course_functional_test
from Diksha_Reports.content_textbook import content_textbook_functional_test
from Diksha_Reports.usage_by_course import location_course_functional_testing
from Diksha_Reports.usage_by_textbook import location_textbook_functional_testing
from Diksha_TPD.TPD_Completion_percentage import tpd_completion_functionaltest
from Diksha_TPD.TPD_Course_Progress import tpd_course_functional_test
from Diksha_TPD.TPD_Enrollment_completion import enrollment_functional_test
from Student_Attendance import student_attendance_functional_testing
from get_dir import pwd
from HTMLTestRunner import HTMLTestRunner

from reuse_func import GetData


class MyTestSuite_Functional(unittest.TestCase):

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
                functional_test = unittest.TestSuite()
                functional_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(content_course_functional_test.cQube_content_course_functional)
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "w")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Content BY Course Functional Test Report',
                    verbosity=1,)
                runner1.run(functional_test)
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
                functional_test = unittest.TestSuite()
                functional_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(content_textbook_functional_test.cQube_content_textbook_Functional)
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Content By Textbook report Functional Test Report',
                    verbosity=1,
                )
                runner1.run(functional_test)
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
                functional_test = unittest.TestSuite()
                functional_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(location_course_functional_testing.cQube_diskha_course_functional_report)
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' Usage By Course Report Functional Test Report',
                    verbosity=1,

                )
                runner1.run(functional_test)
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
                functional_test = unittest.TestSuite()
                functional_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(location_textbook_functional_testing.cQube_usage_textbook_functional_report)
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' Usage By Textbook Report Functional Test Report',
                    verbosity=1,)
                runner1.run(functional_test)
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
                functional_test = unittest.TestSuite()
                functional_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(tpd_course_functional_test.cQube_lpdcontent_functional_Test)
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD course Progress Functional Test Infra_Table_Report',
                    verbosity=1,)
                runner1.run(functional_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")


    #
    # def test_issue06(self):
    #     self.data.page_loading(self.driver)
    #     status = self.data.get_student_status("Diksha_TPD")
    #     if status == str(True):
    #         self.data.page_loading(self.driver)
    #         self.data.navigate_to_tpd_percentage_progress()
    #         if 'No data found' in self.driver.page_source:
    #             print('TPD Course Percentage Report is showing no data found!..')
    #             self.driver.close()
    #         else:
    #             regression_test = unittest.TestSuite()
    #             regression_test.addTests([
    #                 unittest.defaultTestLoader.loadTestsFromTestCase(tpd_completion_functionaltest.cQube_completion_percentage_functional)
    #             ])
    #             p = pwd()
    #             outfile = open(p.get_diksha_tpds_regression_report(), "a")
    #
    #             runner1 = HTMLTestRunner.HTMLTestRunner(
    #                 stream=outfile,
    #                 title='TPD Percentage Progress Regression Test Infra_Table_Report',
    #                 verbosity=1,
    #             )
    #             runner1.run(regression_test)
    #             outfile.close()
    #     else:
    #         print(status,"is selected due to this unable to run suite")

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
                functional_test = unittest.TestSuite()
                functional_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(enrollment_functional_test.cQube_enrollment_functionalTest)
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD Enrollment Functional Test Infra_Table_Report',
                    verbosity=1,
                )
                runner1.run(functional_test)
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
                functional_test = unittest.TestSuite()
                functional_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        tpd_completion_functionaltest.cQube_completion_percentage_functional
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='TPD Completion percentage Functional Test Report',
                    verbosity=1,
                )
                runner1.run(functional_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue09(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("student")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_completion_percentage()
            if 'No data found' in self.driver.page_source:
                print('Student Attendance Report is showing no data found!..')
                self.driver.close()
            else:
                functional_test = unittest.TestSuite()
                functional_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                       student_attendance_functional_testing.cQube_Student_Attendance_functional
                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Student Attendance Functional Test Report',
                    verbosity=1,
                )
                runner1.run(functional_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue010(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("sat")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_completion_percentage()
            if 'No data found' in self.driver.page_source:
                print('Semester Report is showing no data found!..')
                self.driver.close()
            else:
                functional_test = unittest.TestSuite()
                functional_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(

                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Semester Assessment Functional Test Report',
                    verbosity=1,
                )
                runner1.run(functional_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue011(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("sat")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_completion_percentage()
            if 'No data found' in self.driver.page_source:
                print('Semester Heat Chart Report is showing no data found!..')
                self.driver.close()
            else:
                functional_test = unittest.TestSuite()
                functional_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(

                    )
                ])
                p = pwd()
                outfile = open(p.get_diksha_tpds_regression_report(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Semester Assessment Heatchart Functional Test Report',
                    verbosity=1,
                )
                runner1.run(functional_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
