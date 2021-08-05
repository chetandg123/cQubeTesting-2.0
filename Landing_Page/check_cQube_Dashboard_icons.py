from reuse_func import GetData


class cQube_Dashboard_Reports():
    def __init__(self,driver):
        self.driver = driver

    def check_Student_attendance(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("sar").click()
        self.cal.page_loading(self.driver)
        count=0
        if 'student-attendance' in self.driver.current_url:
            print('Student attendance Report home page is displayed..')
        else:
             count = count + 1
        return count

    def check_CRC(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("crcr").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'crc' in self.driver.current_url:
            print('CRC Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_Semester(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//div[@id='sat']").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'sat' in self.driver.current_url:
            print('Semester Assessment Test Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_TAR(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("tar").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'teacher-attendance' in self.driver.current_url:
            print('Teacher Attendance Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_school_map(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("imr").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'infrastructure' in self.driver.current_url:
            print('Infrastructure access by location Test Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_school_chart(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("cr").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'infrastructure' in self.driver.current_url:
            print('Infrastructure composite Table Test Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_diksha_course(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//div[@id='dcc']").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'usage-by-course' in self.driver.current_url:
            print('Diksha usage by course Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_telemetry_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("telemData").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'telemetry' in self.driver.current_url:
            print('Telemetry Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_semester_exception(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("SemExp").click()
        self.cal.page_loading(self.driver)
        return count

    def check_completionerror(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("isdata").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def check_udise_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("udise").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def check_periodic_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("pat").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def check_periodic_heatchart_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("heatChart1").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def check_periodic_lotable_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id('lotable1').click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def check_composite_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("composite").click()
        self.cal.page_loading(self.driver)
        count = self.cal.get_no_data_found_status()
        return count

    def check_diksha_course_content_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("dtr").click()
        self.cal.page_loading(self.driver)
        count =0
        if 'usage-by-content-course' in self.driver.current_url:
            print('Diksha usage by content course Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_diksha_textbook_content_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//div[@id='utc']").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'usage-by-content-textbook' in self.driver.current_url:
            print('Diksha usage by content textbook Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_diksha_textbook_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//div[@id='ut']").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'usage-by-textbook' in self.driver.current_url:
            print('Diksha usage by textbook Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_tpd_course_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("tdp-cp").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'tpd-course-progress' in self.driver.current_url:
            print('Diksha TPD course Progress Report home page is displayed..')
        else:
            count = count + 1
        return count


    def check_tpd_enrollment_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//div[@id='tpd-enroll']").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'tpd-enrollement' in self.driver.current_url:
            print('Diksha TPD Enrollmemt/completion Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_tpd_completion_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//div[@id='tpd-comp']").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'tpd-completion' in self.driver.current_url:
            print('Diksha TPD completion Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_teacher_exception_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("tarExp").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'teacher-exception' in self.driver.current_url:
            print('Teacher Exception Report home page is displayed..')
        else:
            count = count + 1
        return count


    def check_periodic_exception_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("patExcpt").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'periodic-exception' in self.driver.current_url:
            print('Periodic Exception Report home page is displayed..')
        else:
            count = count + 1
        return count

    def check_student_exception_report(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id("sarExcpt").click()
        self.cal.page_loading(self.driver)
        count = 0
        if 'student-exception' in self.driver.current_url:
            print('Student Exception Report home page is displayed..')
        else:
            count = count + 1
        return count

