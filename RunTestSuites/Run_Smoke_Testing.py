from TestSuites.SmokeTestSuite.Smoke_Testing import MyTestSuite
from reuse_func import GetData


class SmokeTestCases:

    def __init__(self):
        self.data = GetData()
        self.logger = self.data.get_smoke_log()

    def check_data_on_sar(self):
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_student_report()
        self.errMsg= self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
        else:
            self.logger.info("student attendance report execution started")
            cal_sar = MyTestSuite()
            cal_sar.test_Issue02()
            self.logger.info("student attendance report execution ended")
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
        self.errMsg= self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
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
        self.data.navigate_to_semester_report()
        self.errMsg= self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
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
        self.data.navigate_to_semester_report()
        self.errMsg= self.data.get_data_status()
        if self.errMsg.text == 'No data found':
            print("No data in the page")
            self.driver.close()
        else:
            self.logger.info("school infra report execution started")
            cal_school_infra_report = MyTestSuite()
            cal_school_infra_report.test_Issue06()
            self.logger.info("school infra report execution ended")
            self.driver.close()

cal = SmokeTestCases()

log = GetData()
logg = log.get_smoke_log()

logg.info("Login execution started")
login = MyTestSuite()
login.test_Issue01()
logg.info("Login execution ended")

cal.check_data_on_sar()
cal.check_data_on_crc()
cal.check_data_on_sr()
cal.check_data_on_school_infra_map()
cal.check_data_on_school_infra_report()











