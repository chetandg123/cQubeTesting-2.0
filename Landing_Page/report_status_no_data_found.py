import unittest

from Landing_Page.cqube_reports_home_page import cQube_Reports_Homepage
from reuse_func import GetData


class cQube_Reports(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)

    def test_student_attendance_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_Student_attendance()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_teacher_attendance_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_TAR()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_crc_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_CRC()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_infrastructure_map_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_school_map()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_infrastructure_chart_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_school_chart()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_udise_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_udise_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_composite_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_composite_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_patmap_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_periodic_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    # def test_pat_heatchart_report(self):
    #     fun =cQube_Reports_Homepage(self.driver)
    #     cal = fun.test_periodic_heatchart_report()
    #     self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
    #     self.data.page_loading(self.driver)
    #
    # def test_pat_lotable_report(self):
    #     fun =cQube_Reports_Homepage(self.driver)
    #     cal = fun.test_periodic_lotable_report()
    #     self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
    #     self.data.page_loading(self.driver)

    def test_diksha_course_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_diksha_course()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_diksha_textbook_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_diksha_table_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_telemetry_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_telemetry_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_semester_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_Semester()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_semester_exception_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_semester_exception()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_diksha_c_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_diksha_course()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_diksha_t_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_diksha_textbook_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_diksha_content_course_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_diksha_course_content_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_diksha_content_textbook_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_diksha_textbook_content_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_tpd_course_progress_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_tpd_course_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    # def test_tpd_progress_percentage_report(self):
    #     fun =cQube_Reports_Homepage(self.driver)
    #     cal = fun.test_tpd_percentage_report()
    #     self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
    #     self.data.page_loading(self.driver)

    def test_tpd_enrollment_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_tpd_enrollment_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_tpd_completion_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_tpd_completion_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_teacher_exception_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_teacher_exception_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    def test_student_exception_report(self):
        fun =cQube_Reports_Homepage(self.driver)
        cal = fun.test_student_exception_report()
        self.assertEqual(cal,0,msg='Report is not shown no data found msg ')
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()