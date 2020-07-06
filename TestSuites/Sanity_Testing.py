import configparser
import sys
import os
import time

from Landing_Page import cQube_home_page
from SAR import student_attendance_sanity_testing
from SR import semester_report_sanity_testing
from get_dir import pwd
from CRC import crc, crc_report_sanity_testing
from Login import cQube_login, login_sanity_testing
from SI.MAP import SI_mapreport, School_Map_sanity_testing
from SI.Report import SI_Report, School_report_sanity_testing

import unittest
from fileinput import close
from HTMLTestRunner import HTMLTestRunner

from reuse_func import GetData


class MyTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.logger = self.data.get_sanity_log()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)

    def test_Issue01(self):
        self.logger.info("Login execution started")
        sanity_test = unittest.TestSuite()
        sanity_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(login_sanity_testing.cQube_Login_Test),

        ])
        p= pwd()
        outfile = open(p.get_sanity_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Login Sanity Test Report',
            verbosity=1,

        )

        runner1.run(sanity_test)
        outfile.close()
        self.logger.info("Login execution ended")

    def test_Issue02(self):
        self.data.navigate_to_student_report()
        time.sleep(2)
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the student attendance report page")
        else:
            self.logger.info("student attendance report execution started")
            sanity_test = unittest.TestSuite()
            sanity_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_sanity_testing.cQube_Student_Attendance),
            ])
            p= pwd()
            outfile = open(p.get_sanity_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Student Attendance Sanity Test Report',
                verbosity=1,

            )

            runner1.run(sanity_test)
            outfile.close()
            self.logger.info("student attendance report execution ended")

    def test_Issue03(self):
        self.data.navigate_to_crc_report()
        time.sleep(2)
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the crc report page")
        else:
            self.logger.info("crc report execution started")
            sanity_test = unittest.TestSuite()
            sanity_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(crc_report_sanity_testing.cQube_CRC_Report),
            ])
            p= pwd()
            outfile = open(p.get_sanity_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Crc Sanity Test Report',
                verbosity=1,

            )

            runner1.run(sanity_test)
            outfile.close()
            self.logger.info("crc report execution started")

    def test_Issue04(self):
        self.data.navigate_to_semester_report()
        time.sleep(2)
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the semester report page")
        else:
            self.logger.info("semester report execution started")

            sanity_test = unittest.TestSuite()
            sanity_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(semester_report_sanity_testing.cQube_Semester_Report),
            ])
            p= pwd()
            outfile = open(p.get_sanity_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Semester Sanity Test Report',
                verbosity=1,

            )

            runner1.run(sanity_test)
            outfile.close()
            self.logger.info("semester report execution ended")

    def test_Issue05(self):
        self.data.navigate_to_school_infrastructure_map()
        time.sleep(2)
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the school infrastructure map page")
        else:
            self.logger.info("school infra map report execution started")
            sanity_test = unittest.TestSuite()
            sanity_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(School_Map_sanity_testing.cQube_SI_Map_Report),
            ])
            p= pwd()
            outfile = open(p.get_sanity_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='School Infra Map Sanity Test Report',
                verbosity=1,

            )

            runner1.run(sanity_test)
            outfile.close()
            self.logger.info("school infra map report execution started")

    def test_Issue06(self):
        self.data.navigate_to_school_infrastructure()
        time.sleep(2)
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the school infrastructure report page")
        else:
            self.logger.info("school infra report execution started")
            sanity_test = unittest.TestSuite()
            sanity_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(School_report_sanity_testing.cQube_SI_Report)
            ])
            p= pwd()
            outfile = open(p.get_sanity_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='School Infra Report Sanity Test Report',
                verbosity=1,

            )

            runner1.run(sanity_test)
            outfile.close()
            self.logger.info("school infra report execution started")

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
     unittest.main()