import unittest

from HTMLTestRunner import HTMLTestRunner

from Management_Reports.Management_Exception_Reports.Teacher_attendance_Exception import teacher_exception_management_1, \
    teacher_exception_management_2, teacher_exception_management_3, teacher_exception_management_4, \
    teacher_exception_management_5, teacher_exception_management_6, teacher_exception_management_7
from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_issue01(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_1.cQube_management_teacher_exception_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_2.cQube_management_teacher_exception_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_3.cQube_management_teacher_exception_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_4.cQube_management_teacher_exception_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_5.cQube_management_teacher_exception_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_6.cQube_management_teacher_exception_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_7.cQube_management_teacher_exception_report),




        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Teacher Exception functional Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()
