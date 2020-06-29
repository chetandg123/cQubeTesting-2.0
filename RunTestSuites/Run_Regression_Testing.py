import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

from Data.parameters import Data
from SAR.arg import arg
from TestSuites.Regression_Testing import MyTestSuite
from get_dir import pwd
# pwd = Data()
from reuse_func import GetData


class RegressionTestCases():
    def __init__(self):
        self.data = GetData()
        self.logger = self.data.get_regression_log()

    def check_data_on_sar(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_student_report()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
        else:
            time.sleep(3)
            select_year = Select(self.driver.find_element_by_name(Data.select_year))
            select_month = Select(self.driver.find_element_by_name(Data.select_month))
            time.sleep(3)

            year = []
            month = []

            for x in select_year.options:
                year.append(x.text)
            for y in select_month.options:
                month.append(y.text)

            for x in range(1, len(year)):
                for y in range(1, len(month)):
                    a = arg()
                    a.list.append(year[x])
                    a.list.append(month[y])
                    self.logger.info(month[y] + "started")
                    cal = MyTestSuite()
                    cal.test_Issue02(month[y])
                    self.logger.info(month[y] + "ended")
                    a.list.clear()
            self.driver.close()

    def check_data_on_crc(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_crc_report()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the crc ")
            self.driver.close()
        else:
            self.logger.info("crc report execution started")
            cal_crc = MyTestSuite()
            cal_crc.test_Issue03()
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
            cal_sr.test_Issue04()
            self.logger.info("semester report execution ended")
            self.driver.close()

    def check_data_on_school_infra_map(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_school_infrastructure_map()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the school infrastructure map")
            self.driver.close()
        else:
            self.logger.info("school infra map report execution started")
            cal_school_infra_map = MyTestSuite()
            cal_school_infra_map.test_Issue05()
            self.logger.info("school infra map report execution ended")
            self.driver.close()

    def check_data_on_school_infra_report(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_school_infrastructure()
        self.errMsg = self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the school infrastructure report")
            self.driver.close()
        else:
            self.logger.info("school infra report execution started")
            cal_school_infra_report = MyTestSuite()
            cal_school_infra_report.test_Issue06()
            self.logger.info("school infra report execution ended")
            self.driver.close()


cal = RegressionTestCases()
login = MyTestSuite()

log = GetData()
logg = log.get_regression_log()

logg.info("Login execution started")
login.test_Issue01()
logg.info("Login execution ended")

cal.check_data_on_sar()
cal.check_data_on_crc()
cal.check_data_on_sr()
cal.check_data_on_school_infra_map()
cal.check_data_on_school_infra_report()
