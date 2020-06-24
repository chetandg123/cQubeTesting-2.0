import configparser
import sys
import os

from SAR import student_attendance_smoke_testing
from SR import semester_report_smoke_testing

sys.path.append('/home/devraj/PycharmProjects/cQubeTesting')
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
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_smoke_testing.cQube_Student_Attendance),
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_report_smoke_testing.cQube_Semester_Report),

        ])
        p= pwd()
        outfile = open(p.get_smoke_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Smoke Test Report',
            verbosity=1,

        )

        runner1.run(smoke_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()