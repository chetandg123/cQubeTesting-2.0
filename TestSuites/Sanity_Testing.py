import configparser
import sys
import os

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

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        sanity_test = unittest.TestSuite()
        sanity_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(login_sanity_testing.cQube_Login_Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(cQube_home_page.cQube_Home),
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_sanity_testing.cQube_Student_Attendance),
            unittest.defaultTestLoader.loadTestsFromTestCase(crc_report_sanity_testing.cQube_CRC_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_report_sanity_testing.cQube_Semester_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(School_Map_sanity_testing.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(School_report_sanity_testing.cQube_SI_Report)
        ])
        p= pwd()
        outfile = open(p.get_sanity_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Sanity Test Report',
            verbosity=1,

        )

        runner1.run(sanity_test)
        outfile.close()


if __name__ == '__main__':
     unittest.main()