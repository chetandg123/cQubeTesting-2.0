import unittest

from HTMLTestRunner import HTMLTestRunner

from Exceptions_Reports.Periodic_Exception import  smoke_pat_exception
from Exceptions_Reports.Semester_Exception import  exception_smoke_testing
from Exceptions_Reports.Student_Exception import  smoke_student_exception
from Exceptions_Reports.Teacher_Exception import  smoke_teacher_exception
from get_dir import pwd
from reuse_func import GetData


class MyTestSuite_Exception(unittest.TestCase):

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
        self.data.navigate_to_semester_exception()
        if 'No data found' in self.driver.page_source:
            print('Semester Exception Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    exception_smoke_testing.cQube_semester_exception_report)
            ])
            p = pwd()
            outfile = open(p.get_smoke_exception_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Semester Exception Smoke Test Report',
                verbosity=1,
            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue02(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_student_exception()
        if 'No data found' in self.driver.page_source:
            print('Student Exception Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    smoke_student_exception.cQube_smoke_Student_exception)
            ])
            p = pwd()
            outfile = open(p.get_smoke_exception_report(), "a")
            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Student Exception Smoke Test Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue03(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_teacher_exception()
        if 'No data found' in self.driver.page_source:
            print('Teacher Exception Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    smoke_teacher_exception.cQube_teacher_exception_smoke_report)
            ])
            p = pwd()
            outfile = open(p.get_smoke_exception_report(), "a")
            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Teacher Exception Smoke Test Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue04(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_pat_exception()
        if 'No data found' in self.driver.page_source:
            print('PAT Exception Report is showing no data found!..')
            self.driver.close()
        else:
            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    smoke_pat_exception.cQube_pat_exception_smoke_report)
            ])
            p = pwd()
            outfile = open(p.get_smoke_exception_report(), "a")
            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='PAT Exception Smoke Test Report',
                verbosity=1,
            )
            runner1.run(smoke_test)
            outfile.close()

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
