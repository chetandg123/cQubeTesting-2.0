from reuse_func import GetData


class cQube_Reports_Homepage():
    def __init__(self,driver):
        self.driver = driver

    def test_Student_attendance(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("sar").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_CRC(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("crcr").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_Semester(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//div[@id='sat']").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_TAR(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("tar").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_school_map(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("imr").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_school_chart(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("cr").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_diksha_course(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//div[@id='dcc']").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_telemetry_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("telemData").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_semester_exception(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("SemExp").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_completionerror(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("isdata").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_udise_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("udise").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_periodic_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("pat").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    # def test_periodic_heatchart_report(self):
    #     self.cal = GetData()
    #     self.cal.page_loading(self.driver)
    #     self.driver.find_element_by_xpath("").click()
    #     self.cal.page_loading(self.driver)
    #     count = self.cal.get_no_data_found_status()
    #     return count
    #
    # def test_periodic_lotable_report(self):
    #     self.cal = GetData()
    #     self.cal.page_loading(self.driver)
    #     self.driver.find_element_by_id().click()
    #     self.cal.page_loading(self.driver)
    #     count = self.cal.get_no_data_found_status()
    #     return count

    def test_composite_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("composite").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_diksha_course_content_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("dtr").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_diksha_textbook_content_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//div[@id='utc']").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_diksha_textbook_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//div[@id='ut']").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_tpd_course_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("tdp-cp").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    # def test_tpd_percentage_report(self):
    #     self.cal = GetData()
    #     self.cal.page_loading(self.driver)
    #     self.driver.find_element_by_id("").click()
    #     self.cal.page_loading(self.driver)
    #     count = self.cal.get_no_data_found_status()
    #     return count

    def test_tpd_enrollment_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//div[@id='tpd-enroll']").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_tpd_completion_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//div[@id='tpd-comp']").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_teacher_exception_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("tarExp").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count


    def test_periodic_exception_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("patExcpt").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def test_student_exception_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("sarExcpt").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

