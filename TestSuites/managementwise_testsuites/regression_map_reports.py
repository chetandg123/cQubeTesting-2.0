

import unittest

from HTMLTestRunner import HTMLTestRunner

from Management_Reports.Infrastructure_Map_Report import infrastructure_report_management_1, \
    infrastructure_report_management_2, infrastructure_report_management_3, infrastructure_report_management_4, \
    infrastructure_report_management_5, infrastructure_report_management_6, infrastructure_report_management_7
from Management_Reports.Semester_report import semester_map_management_1, semester_map_management_2, \
    semester_map_management_3, semester_map_management_4, semester_map_management_5, semester_map_management_6
from Management_Reports.Student_attendance_report import student_attendance_management_1, \
    student_attendance_management_2, student_attendance_management_3, student_attendance_management_4, \
    student_attendance_management_5, student_attendance_management_6, student_attendance_management_7
from Management_Reports.Teacher_attendance_report import teacher_attendance_management_1, \
    teacher_attendance_management_2, teacher_attendance_management_3, teacher_attendance_management_5, \
    teacher_attendance_management_6, teacher_attendance_management_4, teacher_attendance_management_7
from Management_Reports.UDISE_Management_report import udise_management_1, udise_management_2, udise_management_3, \
    udise_management_4, udise_management_5, udise_management_6, udise_management_7
from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_issue01(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_1.Management_student_attendance_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_2.Management_student_attendance_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_3.Management_student_attendance_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_4.Management_student_attendance_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_5.Management_student_attendance_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_6.Management_student_attendance_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_7.Management_student_attendance_report),

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Teacher functional Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    def test_issue02(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_1.cQube_udise_management_wise_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_2.cQube_udise_management_wise_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_3.cQube_udise_management_wise_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_4.cQube_udise_management_wise_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_5.cQube_udise_management_wise_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_6.cQube_udise_management_wise_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_7.cQube_udise_management_wise_reports)

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Udise management wise Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    def test_issue03(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_attendance_management_1.Management_teacher_attendance_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_attendance_management_2.Management_teacher_attendance_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_attendance_management_3.Management_teacher_attendance_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_attendance_management_4.Management_teacher_attendance_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_attendance_management_5.Management_teacher_attendance_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_attendance_management_6.Management_teacher_attendance_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_attendance_management_7.Management_teacher_attendance_report),

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Teacher attendance managementwise Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    def test_issue04(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_1.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_2.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_3.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_4.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_5.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_6.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_7.cQube_SI_Map_Report),

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Infrastructure managementwise Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    def test_issue05(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_map_management_1.cQube_Semester_management_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_map_management_2.cQube_Semester_management_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_map_management_3.cQube_Semester_management_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_map_management_4.cQube_Semester_management_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_map_management_5.cQube_Semester_management_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_map_management_6.cQube_Semester_management_Reports),

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Semester managementwise Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
