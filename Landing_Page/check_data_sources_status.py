import unittest
import yaml
from reuse_func import GetData


class cQube_Reports_Homepage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)


        file_path = "/home/chetan/datasources_config.yml"
        with open(file_path) as file:
            source_list = yaml.load(file, Loader=yaml.FullLoader)

        self.nifi_crc= source_list['nifi_crc']
        self.nifi_attendance= source_list['nifi_attendance']
        self.nifi_semester= source_list['nifi_semester']
        self.nifi_infra= source_list['nifi_infra']
        self.nifi_diksha= source_list['nifi_diksha']
        self.nifi_telemetry= source_list['nifi_telemetry']
        self.nifi_udise= source_list['nifi_udise']
        self.nifi_pat= source_list['nifi_pat']
        self.nifi_composite= source_list['nifi_composite']
        self.nifi_healthcard= source_list['nifi_healthcard']
        self.nifi_teacher_attendance= source_list['nifi_teacher_attendance']
        self.nifi_data_replay= source_list['nifi_data_replay']
        self.nifi_sat= source_list['nifi_sat']

    def test_crc_table_report(self):
        count = 0
        if self.nifi_crc == True:
            self.data.navigate_to_crc_report()
            if 'No data found' in self.driver.page_source:
                 print(self.driver.current_url,'Report showing no data found!...')
            else:
                 print(self.driver.current_url,'is not showing no data found!')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        elif self.nifi_crc == False:
            self.data.navigate_to_school_infrastructure_map()
            if 'Coming soon' in self.driver.page_source:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
            else:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        self.assertEqual(count,0,msg='Msg is not displayed on screen ')

    def test_student_attendance_report(self):
        count = 0
        if self.nifi_attendance == True:
            self.data.navigate_to_student_report()
            if 'No data found' in self.driver.page_source:
                 print(self.driver.current_url,'Report showing no data found!...')
            else:
                 print(self.driver.current_url,'is not showing no data found!')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        elif self.nifi_attendance == False:
            self.data.navigate_to_school_infrastructure_map()
            if 'Coming soon' in self.driver.page_source:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
            else:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        self.assertEqual(count,0,msg='Msg is not displayed on screen ')

    def test_semester_exception_report(self):
        count = 0
        if self.nifi_semester == True:
            self.data.navigate_to_semester_exception()
            if 'No data found' in self.driver.page_source:
                 print(self.driver.current_url,'Report showing no data found!...')
            else:
                 print(self.driver.current_url,'is not showing no data found!')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        elif self.nifi_semester == False:
            self.data.navigate_to_school_infrastructure_map()
            if 'Coming soon' in self.driver.page_source:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
            else:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        self.assertEqual(count,0,msg='Msg is not displayed on screen ')

    def test_sat_report(self):
        count = 0
        if self.nifi_sat == True:
            self.data.navigate_to_semester_report()
            if 'No data found' in self.driver.page_source:
                 print(self.driver.current_url,'Report showing no data found!...')
            else:
                 print(self.driver.current_url,'is not showing no data found!')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        elif self.nifi_sat == False:
            self.data.navigate_to_school_infrastructure_map()
            if 'Coming soon' in self.driver.page_source:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
            else:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        self.assertEqual(count,0,msg='Msg is not displayed on screen ')

    def test_infrastructure_map_report(self):
        count = 0
        if self.nifi_infra == True:
            self.data.navigate_to_school_infrastructure_map()
            if 'No data found' in self.driver.page_source:
                 print(self.driver.current_url,'Report showing no data found!...')
            else:
                 print(self.driver.current_url,'is not showing no data found!')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        elif self.nifi_infra == False:
            self.data.navigate_to_school_infrastructure_map()
            if 'Coming soon' in self.driver.page_source:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
            else:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        self.assertEqual(count,0,msg='Error msg is not displayed on screen')

    def test_diksha_report(self):
        count = 0
        if self.nifi_diksha == True:
            self.data.navigate_to_diksha_content_course()
            if 'No data found' in self.driver.page_source:
                 print(self.driver.current_url,'Report showing no data found!...')
            else:
                 print(self.driver.current_url,'is not showing no data found!')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        elif self.nifi_diksha == False:
            self.data.navigate_to_school_infrastructure_map()
            if 'Coming soon' in self.driver.page_source:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
            else:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        self.assertEqual(count,0,msg='Error msg is not displayed on screen')

    def test_telemetry_report(self):
        count = 0
        if self.nifi_telemetry == True:
            self.data.navigate_to_telemetry()
            if 'No data found' in self.driver.page_source:
                 print(self.driver.current_url,'Report showing no data found!...')
            else:
                 print(self.driver.current_url,'is not showing no data found!')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        elif self.nifi_telemetry == False:
            self.data.navigate_to_school_infrastructure_map()
            if 'Coming soon' in self.driver.page_source:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
            else:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        self.assertEqual(count,0,msg='Error msg is not displayed on screen')

    def test_udise_report(self):
        count = 0
        if self.nifi_udise == True:
            self.data.navigate_to_udise_report()
            if 'No data found' in self.driver.page_source:
                 print(self.driver.current_url,'Report showing no data found!...')
            else:
                 print(self.driver.current_url,'is not showing no data found!')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        elif self.nifi_udise == False:
            self.data.navigate_to_school_infrastructure_map()
            if 'Coming soon' in self.driver.page_source:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
            else:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        self.assertEqual(count,0,msg='Error msg is not displayed on screen')

    def test_pat_report(self):
        count = 0
        if self.nifi_pat == True:
            self.data.navigate_to_periodic_report()
            if 'No data found' in self.driver.page_source:
                 print(self.driver.current_url,'Report showing no data found!...')
            else:
                 print(self.driver.current_url,'is not showing no data found!')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        elif self.nifi_pat == False:
            self.data.navigate_to_school_infrastructure_map()
            if 'Coming soon' in self.driver.page_source:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
            else:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        self.assertEqual(count,0,msg='Error msg is not displayed on screen')

    def test_composite_report(self):
        count = 0
        if self.nifi_composite == True:
            self.data.navigate_to_composite_report()
            if 'No data found' in self.driver.page_source:
                 print(self.driver.current_url,'Report showing no data found!...')
            else:
                 print(self.driver.current_url,'is not showing no data found!')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        elif self.nifi_composite == False:
            self.data.navigate_to_school_infrastructure_map()
            if 'Coming soon' in self.driver.page_source:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
            else:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        self.assertEqual(count,0,msg='Error msg is not displayed on screen')

    def test_progress_card_report(self):
        count = 0
        if self.nifi_healthcard == True:
            self.data.navigate_to_health_card_index()
            if 'No data found' in self.driver.page_source:
                 print(self.driver.current_url,'Report showing no data found!...')
            else:
                 print(self.driver.current_url,'is not showing no data found!')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        elif self.nifi_healthcard == False:
            self.data.navigate_to_school_infrastructure_map()
            if 'Coming soon' in self.driver.page_source:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
            else:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        self.assertEqual(count,0,msg='Error msg is not displayed on screen')

    def test_teacher_attendance_report(self):
        count = 0
        if self.nifi_teacher_attendance == True:
            self.data.navigate_to_teacher_attendance_report()
            if 'No data found' in self.driver.page_source:
                 print(self.driver.current_url,'Report showing no data found!...')
            else:
                 print(self.driver.current_url,'is not showing no data found!')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        elif self.nifi_teacher_attendance == False:
            self.data.navigate_to_school_infrastructure_map()
            if 'Coming soon' in self.driver.page_source:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
            else:
                 print(self.driver.current_url,'Coming soon is displayed on screen...')
                 count = count+1
            self.driver.find_element_by_id("homeBtn").click()
            self.data.page_loading(self.driver)
        self.assertEqual(count,0,msg='Error msg is not displayed on screen')

    # def test_data_reply_report(self):
    #     count = 0
    #     if self.nifi_data_replay == True:
    #         # self.data()
    #         if 'No data found' in self.driver.page_source:
    #              print(self.driver.current_url,'Report showing no data found!...')
    #         else:
    #              print(self.driver.current_url,'is not showing no data found!')
    #              count = count+1
    #         self.driver.find_element_by_id("homeBtn").click()
    #         self.data.page_loading(self.driver)
    #     elif self.nifi_data_replay == False:
    #         self.data.navigate_to_school_infrastructure_map()
    #         if 'Coming soon' in self.driver.page_source:
    #              print(self.driver.current_url,'Coming soon is displayed on screen...')
    #         else:
    #              print(self.driver.current_url,'Coming soon is displayed on screen...')
    #              count = count+1
    #         self.driver.find_element_by_id("homeBtn").click()
    #         self.data.page_loading(self.driver)
    #     self.assertEqual(count,0,msg='Error msg is not displayed on screen')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
