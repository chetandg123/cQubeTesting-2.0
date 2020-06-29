import configparser
import sys
import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
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


    def test_Issue01(self):
        self.logger.info("Login execution started")
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(login_regression_testing.cQube_Login_Test),
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
        self.logger.info("Login execution ended")


    def test_Issue02(self):
        self.data.navigate_to_student_report()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
        else:
            self.logger.info("student attendance report execution started")
            time.sleep(3)
            select_year = Select(self.driver.find_element_by_name(Data.select_year))
            select_month = Select(self.driver.find_element_by_name(Data.select_month))
            time.sleep(3)

            year = []
            month = []

            for x in select_year.options:
                year.append(x.text)
            for y in select_month.options:
                month.append(y.text)

            for x in range(1, len(year)):
                for y in range(1, len(month)):
                    a = arg()
                    a.list.append(year[x])
                    a.list.append(month[y])
                    self.logger.info(month[y] + "started")
                    regression_test = unittest.TestSuite()
                    regression_test.addTests([
                        # file name .class name
                        unittest.defaultTestLoader.loadTestsFromTestCase(
                            student_attendance_regression_testing.cQube_Student_Attendance),

                    ])
                    p = pwd()
                    outfile = open(p.get_regression_report_path(), "a")

                    runner1 = HTMLTestRunner.HTMLTestRunner(
                        stream=outfile,
                        title=month + "Student Attendance" + 'Regression Test Report',
                        verbosity=1,

                    )

                    runner1.run(regression_test)
                    outfile.close()
                    self.logger.info(month[y] + "ended")
                    a.list.clear()

            self.logger.info("student attendance report execution ended")

    def test_Issue03(self):
        self.data.navigate_to_crc_report()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
        else:
            self.logger.info("crc report execution started")
            regression_test = unittest.TestSuite()
            regression_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(crc_report_regression_testing.cQube_CRC_Report),
            ])
            p = pwd()
            outfile = open(p.get_regression_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Crc Regression Test Report',
                verbosity=1,

            )

            runner1.run(regression_test)
            outfile.close()
            self.logger.info("crc report execution ended")

    def test_Issue04(self):
        self.data.navigate_to_semester_report()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
        else:
            self.logger.info("semester report execution started")
            regression_test = unittest.TestSuite()
            regression_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(semester_report_regression_testing.cQube_Semester_Report),
            ])
            p = pwd()
            outfile = open(p.get_regression_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Semester Regression Test Report',
                verbosity=1,

            )

            runner1.run(regression_test)
            outfile.close()
            self.logger.info("semester report execution ended")

    def test_Issue05(self):
        self.data.navigate_to_school_infrastructure_map()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
        else:
            self.logger.info("school infra map report execution started")
            regression_test = unittest.TestSuite()
            regression_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(School_Map_regression_testing.cQube_SI_Map_Report),
            ])
            p = pwd()
            outfile = open(p.get_regression_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='School Infrastructure Map Regression Test Report',
                verbosity=1,

            )

            runner1.run(regression_test)
            outfile.close()
            self.logger.info("school infra map report execution ended")

    def test_Issue06(self):
        self.data.navigate_to_school_infrastructure()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
        else:
            self.logger.info("school infra report execution started")
            regression_test = unittest.TestSuite()
            regression_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(School_report_regression_testing.cQube_SI_Report)
            ])
            p = pwd()
            outfile = open(p.get_regression_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='School Infrastructure Report Regression Test Report',
                verbosity=1,

            )

            runner1.run(regression_test)
            outfile.close()
            self.logger.info("school infra report execution started")

    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
