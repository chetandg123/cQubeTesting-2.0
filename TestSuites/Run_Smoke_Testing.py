import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestSuites.Smoke_Testing import MyTestSuite
from reuse_func import GetData


class SmokeTestCases:

    def __init__(self):
        self.data = GetData()

    def check_data_on_sar(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_student_report()
        self.errMsg= self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
            exit(0)
        else:
            cal_sar = MyTestSuite()
            cal_sar.test_Issue01()
            cal_sar.test_Issue02()
            self.driver.close()

    def check_data_on_crc(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_crc_report()
        self.errMsg= self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
            exit(0)
        else:
            cal_crc = MyTestSuite()
            cal_crc.test_Issue03()
            self.driver.close()

    def check_data_on_sr(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_semester_report()
        self.errMsg= self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
            exit(0)
        else:
            cal_sr = MyTestSuite()
            cal_sr.test_Issue04()
            self.driver.close()

    def check_data_on_school_infra_map(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_semester_report()
        self.errMsg= self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
            exit(0)
        else:
            cal_school_infra_map = MyTestSuite()
            cal_school_infra_map.test_Issue05()
            self.driver.close()

    def check_data_on_school_infra_report(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_semester_report()
        self.errMsg= self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
            exit(0)
        else:
            cal_school_infra_report = MyTestSuite()
            cal_school_infra_report.test_Issue06()
            self.driver.close()

cal = SmokeTestCases()

cal.check_data_on_sar()
cal.check_data_on_crc()
cal.check_data_on_sr()
cal.check_data_on_school_infra_map()
cal.check_data_on_school_infra_report()











