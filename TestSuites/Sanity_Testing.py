import configparser
import sys
import os

from SAR import student_attendance_sanity_testing
from SR import semester_report_sanity_testing
from get_dir import pwd
from CRC import crc
from Login import cQube_login
from SI.MAP import SI_mapreport
from SI.Report import SI_Report




import unittest
from fileinput import close
from HTMLTestRunner import HTMLTestRunner

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        sanity_test = unittest.TestSuite()
        sanity_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(cQube_login.cQube_Login_Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_sanity_testing.cQube_Student_Attendance),
            unittest.defaultTestLoader.loadTestsFromTestCase(crc.cQube_CRC_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_report_sanity_testing.cQube_Semester_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(SI_mapreport.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(SI_Report.cQube_SI_Report)
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