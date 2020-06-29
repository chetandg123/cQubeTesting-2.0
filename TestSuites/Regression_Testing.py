import configparser
import sys
import os

from SAR import sar
from SR import semester_report_regression_testing
from get_dir import pwd
from CRC import crc, crc_report_regression_testing
from Login import cQube_login, login_regression_testing
from SI.MAP import SI_mapreport, School_Map_regression_testing
from SI.Report import SI_Report, School_report_regression_testing

import unittest
from fileinput import close
from HTMLTestRunner import HTMLTestRunner

class MyTestSuite(unittest.TestCase):
    def test_Issue01(self,month):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(sar.cQube_Student_Attendance),

        ])
        p= pwd()
        outfile = open(p.get_regression_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title= month + 'Regression Test Report',
            verbosity=1,

        )

        runner1.run(regression_test)
        outfile.close()

    def test_Issue02(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(login_regression_testing.cQube_Login_Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(crc_report_regression_testing.cQube_CRC_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_report_regression_testing.cQube_Semester_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(School_Map_regression_testing.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(School_report_regression_testing.cQube_SI_Report)
        ])
        p= pwd()
        outfile = open(p.get_regression_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Regression Test Report',
            verbosity=1,

        )

        runner1.run(regression_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()