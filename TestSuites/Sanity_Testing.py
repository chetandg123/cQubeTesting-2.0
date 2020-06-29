import configparser
import sys
import os

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

class MyTestSuite(unittest.TestCase):

    def test_Issue01(self):
        sanity_test = unittest.TestSuite()
        sanity_test.addTests([
            # file name .class name
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
    def test_Issue02(self):
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
    def test_Issue03(self):
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
    def test_Issue04(self):
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
    def test_Issue05(self):
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
    def test_Issue06(self):
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


if __name__ == '__main__':
     unittest.main()