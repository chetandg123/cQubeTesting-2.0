import unittest

from HTMLTestRunner import HTMLTestRunner

from Management_Reports.Student_attendance_report import student_attendance_management_1, \
    student_attendance_management_2, student_attendance_management_3, student_attendance_management_4, \
    student_attendance_management_5, student_attendance_management_6, student_attendance_management_7
from Management_Reports.Teacher_attendance_report import teacher_attendance_management_1, \
    teacher_attendance_management_2, teacher_attendance_management_3, teacher_attendance_management_5, \
    teacher_attendance_management_6, teacher_attendance_management_4, teacher_attendance_management_7
from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_issue01(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_1.Management_student_attendance_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_2.Management_student_attendance_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_3.Management_student_attendance_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_4.Management_student_attendance_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_5.Management_student_attendance_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_6.Management_student_attendance_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_attendance_management_7.Management_student_attendance_report),

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
            title='Teacher functional Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()
