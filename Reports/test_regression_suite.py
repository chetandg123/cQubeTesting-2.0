import unittest

from HTMLTestRunner import HTMLTestRunner

from CRC import crc_report_regression_testing
from Composite_report import composite_regression_testing
from Diksha_Reports.Diksha_charts import diksha_chart_Regression_testing
from Diksha_Reports.Diksha_column_chart import column_regression_suite
from Diksha_Reports.Diksha_table_report import diksha_table_regression_testing
from Periodic_report import periodic_regression_testing
from SAR import student_attendance_regression_testing
from SI.MAP import School_Map_regression_testing
from SI.Report import School_report_regression_testing
from SR import semester_report_regression_testing
from Semester_Exception import exception_regression_testing
from Telemetry import telemetry_regression_testing
from UDISE import udise_regression_testing
from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    @classmethod

    def test_issue01(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            # file name .class name
            # unittest.defaultTestLoader.loadTestsFromTestCase(login_page.login),
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_regression_testing.cQube_Student_Attendance),
            unittest.defaultTestLoader.loadTestsFromTestCase(crc_report_regression_testing.cQube_CRC_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_report_regression_testing.cQube_Semester_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(School_Map_regression_testing.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(School_report_regression_testing.cQube_SI_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(diksha_chart_Regression_testing.cQube_diskha_chart),
            unittest.defaultTestLoader.loadTestsFromTestCase(diksha_table_regression_testing.cQube_diskha_regression),
            unittest.defaultTestLoader.loadTestsFromTestCase(column_regression_suite.cQube_diskha_column_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(exception_regression_testing.cQube_semester_exception_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(telemetry_regression_testing.Test_Telemetry),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_regression_testing.cQube_udise_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(composite_regression_testing.composite_regression_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(periodic_regression_testing.periodic_regression),

        ])
        p = pwd()
        outfile = open(p.get_regression_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='login to cQube regression Test Report',
            verbosity=1,

        )
        runner1.run(regression_test)


    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
