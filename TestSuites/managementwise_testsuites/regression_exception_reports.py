


import unittest

from HTMLTestRunner import HTMLTestRunner

from Exceptions_Reports.Download_Exception import  download_exception_regression_suite

from Management_Reports.Management_Exception_Reports.Semester_Exception_management import \
    semester_exception_management_1, semester_exception_management_2, semester_exception_management_3, \
    semester_exception_management_4, semester_exception_management_5, semester_exception_management_6, \
    semester_exception_management_7
from Management_Reports.Management_Exception_Reports.Student_attendance_exception import student_exception_management_1, \
    student_exception_management_7, student_exception_management_2, student_exception_management_4, \
    student_exception_management_5, student_exception_management_3, student_exception_management_6
from Management_Reports.Management_Exception_Reports.Teacher_attendance_Exception import teacher_exception_management_1, \
    teacher_exception_management_2, teacher_exception_management_3, teacher_exception_management_4, \
    teacher_exception_management_5, teacher_exception_management_6, teacher_exception_management_7
from Management_Reports.Management_Exception_Reports.pat_exception_management import pat_exception_management_1, \
    pat_exception_management_2, pat_exception_management_3, pat_exception_management_4, pat_exception_management_5, \
    pat_exception_management_6, pat_exception_management_7
from Management_Reports.SAT_Report.SAT_Heatchart import sat_heatchart_management_1, sat_heatchart_management_2, \
    sat_heatchart_management_3, sat_heatchart_management_4, sat_heatchart_management_5, sat_heatchart_management_6, \
    sat_heatchart_management_7
from Management_Reports.composite_Report import composite_report_management_1, composite_report_management_2, \
    composite_report_management_3, composite_report_management_4, composite_report_management_5, \
    composite_report_management_6
from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_issue01(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_1.cQube_management_teacher_exception_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_2.cQube_management_teacher_exception_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_3.cQube_management_teacher_exception_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_4.cQube_management_teacher_exception_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_5.cQube_management_teacher_exception_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_6.cQube_management_teacher_exception_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(teacher_exception_management_7.cQube_management_teacher_exception_report),




        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Teacher Exception management wise Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    def test_issue02(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(student_exception_management_1.cQube_Student_Attendance_regression),
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_exception_management_2.cQube_Student_Attendance_regression),
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_exception_management_3.cQube_Student_Attendance_regression),
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_exception_management_4.cQube_Student_Attendance_regression),
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_exception_management_5.cQube_Student_Attendance_regression),
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_exception_management_6.cQube_Student_Attendance_regression),
            # unittest.defaultTestLoader.loadTestsFromTestCase(student_exception_management_7.cQube_Student_Attendance_regression),

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Teacher Exception management wise Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    def test_issue03(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(semester_exception_management_1.cQube_semester_exception_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(semester_exception_management_2.cQube_semester_exception_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(semester_exception_management_3.cQube_semester_exception_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(semester_exception_management_4.cQube_semester_exception_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(semester_exception_management_5.cQube_semester_exception_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(semester_exception_management_6.cQube_semester_exception_report),
            # unittest.defaultTestLoader.loadTestsFromTestCase(semester_exception_management_7.cQube_semester_exception_report),

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Semester Exception management wise Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    def test_issue04(self):
            regression_test = unittest.TestSuite()
            regression_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(pat_exception_management_1.cQube_pat_exception_managementwise_report),
                # unittest.defaultTestLoader.loadTestsFromTestCase(pat_exception_management_2.cQube_pat_exception_managementwise_report),
                # unittest.defaultTestLoader.loadTestsFromTestCase(pat_exception_management_3.cQube_pat_exception_managementwise_report),
                # unittest.defaultTestLoader.loadTestsFromTestCase(pat_exception_management_4.cQube_pat_exception_managementwise_report),
                # unittest.defaultTestLoader.loadTestsFromTestCase(pat_exception_management_5.cQube_pat_exception_managementwise_report),
                # unittest.defaultTestLoader.loadTestsFromTestCase(pat_exception_management_6.cQube_pat_exception_managementwise_report),
                # unittest.defaultTestLoader.loadTestsFromTestCase(pat_exception_management_7.cQube_pat_exception_managementwise_report),

            ])
            p = pwd()
            outfile = open(p.get_functional_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='PAT Exception management wise Test Test',
                verbosity=1,

            )
            runner1.run(regression_test)
            outfile.close()

    def test_issue05(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(
                download_exception_regression_suite.cQube_regression_download_exceptions),

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Download Exception management wise Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    def test_issue06(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(composite_report_management_1.composite_report_managementwise),
            # unittest.defaultTestLoader.loadTestsFromTestCase(composite_report_management_2.composite_report_managementwise),
            # unittest.defaultTestLoader.loadTestsFromTestCase(composite_report_management_3.composite_report_managementwise),
            # unittest.defaultTestLoader.loadTestsFromTestCase(composite_report_management_4.composite_report_managementwise),
            # unittest.defaultTestLoader.loadTestsFromTestCase(composite_report_management_5.composite_report_managementwise),
            # unittest.defaultTestLoader.loadTestsFromTestCase(composite_report_management_6.composite_report_managementwise),

        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Composite across metrics report management wise Test Report',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    def test_issue07(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(
                sat_heatchart_management_1.cQube_satchart_management_wise_test),
            # unittest.defaultTestLoader.loadTestsFromTestCase(
            #     sat_heatchart_management_2.cQube_satchart_management_wise_test),
            # unittest.defaultTestLoader.loadTestsFromTestCase(
            #     sat_heatchart_management_3.cQube_satchart_management_wise_test),
            # unittest.defaultTestLoader.loadTestsFromTestCase(
            #     sat_heatchart_management_4.cQube_satchart_management_wise_test),
            # unittest.defaultTestLoader.loadTestsFromTestCase(
            #     sat_heatchart_management_5.cQube_satchart_management_wise_test),
            # unittest.defaultTestLoader.loadTestsFromTestCase(
            #     sat_heatchart_management_6.cQube_satchart_management_wise_test),
            # unittest.defaultTestLoader.loadTestsFromTestCase(
            #     sat_heatchart_management_7.cQube_satchart_management_wise_test),
        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='SAT Heatchart report management wise Test Report',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()
