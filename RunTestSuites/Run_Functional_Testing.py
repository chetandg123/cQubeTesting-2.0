import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestSuites.Functional_Testing import MyTestSuite
from reuse_func import GetData


class FunctionalTestCases:

    def __init__(self):
        self.data = GetData()
        self.logger =self.data.get_functional_log()

    def check_data_on_crc(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_crc_report()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the crc report")
            self.driver.close()
        else:
            self.logger.info("crc report execution started")
            cal_crc = MyTestSuite()
            cal_crc.test_Issue01()
            self.logger.info("crc report execution ended")
            self.driver.close()


    def check_data_on_sr(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_semester_report()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the semester report")
            self.driver.close()
        else:
            self.logger.info("semester report execution started")
            cal_sr = MyTestSuite()
            cal_sr.test_Issue02()
            self.logger.info("semester report execution ended")
            self.driver.close()

    def check_data_on_school_infra_map(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_semester_report()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the school infra map")
            self.driver.close()
        else:
            self.logger.info("school infra map report execution started")
            cal_school_infra_map = MyTestSuite()
            cal_school_infra_map.test_Issue03()
            self.logger.info("school infra map report execution ended")
            self.driver.close()

    def check_data_on_school_infra_report(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_semester_report()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the school infra report")
            self.driver.close()
        else:
            self.logger.info("school infra report execution started")
            cal_school_infra_report = MyTestSuite()
            cal_school_infra_report.test_Issue04()
            self.logger.info("school infra report execution ended")
            self.driver.close()


cal = FunctionalTestCases()
cal.check_data_on_crc()
cal.check_data_on_sr()
cal.check_data_on_school_infra_map()
cal.check_data_on_school_infra_report()
