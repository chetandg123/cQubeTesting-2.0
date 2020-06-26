
import os

from CRC import smoke_crc
from Login import smoke_login
from SAR import student_attendance_smoke_testing
from SI.MAP import smoke_si_map
from SI.Report import smoke_si_report
from SR import semester_report_smoke_testing


from get_dir import pwd

import unittest
from fileinput import close
from HTMLTestRunner import HTMLTestRunner

class MyTestSuite(unittest.TestCase):

    def test_Issue01(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(smoke_login.cQube_Login_smoke_Test),
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

    def test_Issue02(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_smoke_testing.cQube_Student_Attendance),
        ])
        p = pwd()
        outfile = open(p.get_smoke_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            verbosity=1,

        )

        runner1.run(smoke_test)
        outfile.close()

    def test_Issue03(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(smoke_crc.cQube_CRC_Report),
        ])
        p = pwd()
        outfile = open(p.get_smoke_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            verbosity=1,

        )

        runner1.run(smoke_test)
        outfile.close()

    def test_Issue04(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_report_smoke_testing.cQube_Semester_Report),
        ])
        p = pwd()
        outfile = open(p.get_smoke_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            verbosity=1,

        )

        runner1.run(smoke_test)
        outfile.close()

    def test_Issue05(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(smoke_si_map.cQube_SI_Map_Report),

        ])
        p = pwd()
        outfile = open(p.get_smoke_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            verbosity=1,

        )

        runner1.run(smoke_test)
        outfile.close()

    def test_Issue06(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(smoke_si_report.cQube_SI_Report)
        ])
        p = pwd()
        outfile = open(p.get_smoke_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            verbosity=1,

        )

        runner1.run(smoke_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()