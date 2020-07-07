import configparser
import sys
import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from Landing_Page import cQube_home_page
from SAR import student_attendance_regression_testing
from SAR.arg import arg
from SR import semester_report_regression_testing
from get_dir import pwd
from CRC import crc, crc_report_regression_testing
from Login import cQube_login, login_regression_testing
from SI.MAP import SI_mapreport, School_Map_regression_testing
from SI.Report import SI_Report, School_report_regression_testing

import unittest
from fileinput import close
from HTMLTestRunner import HTMLTestRunner

from reuse_func import GetData


class MyTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.logger = self.data.get_regression_log()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)

    def test_Issue(self):
        self.logger.info("Login Landing page and Sar execution started")
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(login_regression_testing.cQube_Login_Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(cQube_home_page.cQube_Home),
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_regression_testing.cQube_Student_Attendance),

        ])
        p = pwd()
        outfile = open(p.get_regression_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Login Regression Test Report',
            verbosity=1,

        )

        runner1.run(regression_test)
        outfile.close()
        self.logger.info("Login Landing page and Sar execution ended")



    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()