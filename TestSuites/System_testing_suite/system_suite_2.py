
import unittest
from Diksha_Reports.usage_by_course import usage_by_course_system_testing
from Diksha_Reports.usage_by_textbook import usage_by_textbook_system_suite
from Diksha_Reports.content_course import content_course_system_suite
from Diksha_Reports.content_textbook import content_textbook_system_suite
from Diksha_TPD.TPD_Completion_percentage import completion_system_test
from Diksha_TPD.TPD_Course_Progress import tpd_course_system_test
from Diksha_TPD.TPD_Enrollment_completion import enrollment_system_test
from Diksha_TPD.TPD_Teacher_Percentage import lpd_percentage_system_test
from Exceptions_Reports.Periodic_Exception import pat_exception_system_test
from Exceptions_Reports.Student_Exception import student_exception_system_test
from Exceptions_Reports.Teacher_Exception import teacher_exception_system_test
from Health_Card_Index import health_card_system_test
from Periodic_Test_Reports.Pat_Heatchart import patheatchart_system_test
from Teacher_Attendance import teacher_attendance_system_testing
from get_dir import pwd
from Periodic_Test_Reports.pat_LO_Table import PAT_LO_Table_system_suite
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
        status = self.data.get_student_status("pat")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_heatchart_report()
            if 'No data found' in self.driver.page_source:
                print(' PAT Heat chart Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        patheatchart_system_test.cQube_heatchart_system_test
                        )
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' PAT Heat chart  System Test  ',
                    verbosity=1,)
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue02(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("pat")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_lo_table_report()
            if 'No data found' in self.driver.page_source:
                print(' PAT LO Table Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        PAT_LO_Table_system_suite.cQube_pat_lotable_system_test
                      )
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' PAT LO Table System Test  ',
                    verbosity=1,)
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue03(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_diksha_content_course()
            if 'No data found' in self.driver.page_source:
                print('Diksha Content Course Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                    content_course_system_suite.cQube_content_course_system_suite)
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Diksha Content BY Course System Test ',
                    verbosity=1,)
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue04(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_diksha_content_textbook()
            if 'No data found' in self.driver.page_source:
                print('Diksha Content Textbook Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        content_textbook_system_suite.cQube_content_textbook_systemtest
                    )
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Diksha Content By Textbook report System Test  ',
                    verbosity=1,

                )
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue05(self):
        p = pwd()
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_column_course()
            if 'No data found' in self.driver.page_source:
                print('Diksha usage by course Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        usage_by_course_system_testing.cQube_diskha_course_system_report)])
                outfile = open(p.get_system_report_path(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(stream=outfile,title=' Diksha Usage By Course System Test  ',verbosity=1,)
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue06(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_ETB")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_column_textbook()
            if 'No data found' in self.driver.page_source:
                print('Diksha usage by textbook Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        usage_by_textbook_system_suite.cQube_usage_textbook_system_report
                    )
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' Usage By Textbook   System Test  ',
                    verbosity=1,)
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue07(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_content_progress()
            if 'No data found' in self.driver.page_source:
                print('TPD Course Progress Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        tpd_course_system_test.cQube_lpdcontent_system_Test
                    )
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' Usage By TPD Course   System Test  ',
                    verbosity=1,)
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue08(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_percentage_progress()
            if 'No data found' in self.driver.page_source:
                print('TPD Course Percentage Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        lpd_percentage_system_test.cQube_lpdpercentage_system_Test )])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")
                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' Usage By TPD Percentage   System Test  ',
                    verbosity=1,
                )
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue09(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_enrollment_report()
            if 'No data found' in self.driver.page_source:
                print('TPD Enrollment/Completion Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        enrollment_system_test.cQube_enrollment_systemtest
                    )
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' Usage By TPD Enrollment/Completion   System Test  ',
                    verbosity=1,)
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue10(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("Diksha_TPD")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_tpd_completion_percentage()
            if 'No data found' in self.driver.page_source:
                print('TPD Completion Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        completion_system_test.cQube_completion_percentage_system
                    )
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title=' Usage By TPD Percentage  System Test  ',
                    verbosity=1,

                )
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")


    def test_issue12(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("teacher")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_teacher_attendance_report()
            if 'No data found' in self.driver.page_source:
                print('Teacher Attendance Report is showing no data found!..')
                self.driver.close()
            else:
                system_test = unittest.TestSuite()
                system_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        teacher_attendance_system_testing.cQube_Teacher_Attendance_systemTest
                    )
                ])
                p = pwd()
                outfile = open(p.get_system_report_path(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Teacher Attendance System Test  ',
                    verbosity=1,)
                runner1.run(system_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")


    def test_issue13(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("student")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_student_exception()
            if 'No data found' in self.driver.page_source:
                print('Student Exception Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        student_exception_system_test.cQube_System_Student_exception)
                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Student Exception System Test Report',
                    verbosity=1,
                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")

    def test_issue14(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("teacher")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_teacher_exception()
            if 'No data found' in self.driver.page_source:
                print('Teacher Exception Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        teacher_exception_system_test.cQube_teacher_exception_system_report)
                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='Teacher Exception System Test Report',
                    verbosity=1,

                )
                runner1.run(regression_test)
                outfile.close()
        else:
            print(status,"is selected due to this unable to run suite")


    def test_issue15(self):
        self.data.page_loading(self.driver)
        status = self.data.get_student_status("pat")
        if status == str(True):
            self.data.page_loading(self.driver)
            self.data.navigate_to_pat_exception()
            if 'No data found' in self.driver.page_source:
                print('PAT Exception Report is showing no data found!..')
                self.driver.close()
            else:
                regression_test = unittest.TestSuite()
                regression_test.addTests([
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        pat_exception_system_test.cQube_pat_exception_system_report)
                ])
                p = pwd()
                outfile = open(p.get_regression_map_reports(), "a")

                runner1 = HTMLTestRunner.HTMLTestRunner(
                    stream=outfile,
                    title='PAT Exception System Test Report',
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