import configparser
import os
from pathlib import Path


class pwd():

    def get_system_path(self):
        pwd = os.path.dirname(__file__)
        return pwd

    def get_admin_login_path(self):
        cwd = os.path.dirname(__file__)
        report_path = os.path.join(cwd, 'Reports/admin_login_report.html')
        return report_path

    def get_report_path(self):
        cwd = os.path.dirname(__file__)
        report_path = os.path.join(cwd, 'Reports/report.html')
        return report_path

    def get_sanity_report_path(self):
        cwd = os.path.dirname(__file__)
        report_path = os.path.join(cwd, 'Reports/SanityReports/sanity_testing_report.html')
        return report_path

    def get_regression_report_path(self):
        cwd = os.path.dirname(__file__)
        report_path = os.path.join(cwd, 'Reports/RegressionReports/regression_testing_report.html')
        return report_path

    def get_smoke_report_path(self):
        cwd = os.path.dirname(__file__)
        report_path = os.path.join(cwd, 'Reports/SmokeReports/smoke_testing_report.html')
        return report_path
    def get_functional_report_path(self):
        cwd = os.path.dirname(__file__)
        report_path = os.path.join(cwd, 'Reports/functional_testing_report.html')
        return report_path
    def get_system_report_path(self):
        cwd = os.path.dirname(__file__)
        report_path = os.path.join(cwd, 'Reports/system_testing_report.html')
        return report_path

    def get_config_ini_path(self):
        cwd = os.path.dirname(__file__)
        ini = os.path.join(cwd, 'config.ini')
        return ini

    def get_driver_path(self):
        cwd = os.path.dirname(__file__)
        driver_path = os.path.join(cwd, 'Driver/chromedriver')
        return driver_path

    def get_screenshot_path(self):
        swd = os.path.dirname(__file__)
        image_path = os.path.join(swd, 'Screenshots/demo.png')
        return image_path

    def get_download_dir(self):
        cwd = os.path.dirname(__file__)
        download_path = os.path.join(cwd, 'Downloads')
        return download_path

    def get_functional_testing_log_dir(self):
        cwd = os.path.dirname(__file__)
        log_dir_path = os.path.join(cwd, 'Logs/test_functional_testing.log')
        return log_dir_path

    def get_sanity_testing_log_dir(self):
        cwd = os.path.dirname(__file__)
        log_dir_path = os.path.join(cwd, 'Logs/test_sanity_testing.log')
        return log_dir_path

    def get_smoke_testing_log_dir(self):
        cwd = os.path.dirname(__file__)
        log_dir_path = os.path.join(cwd, 'Logs/test_smoke_testing.log')
        return log_dir_path

    def get_regression_testing_log_dir(self):
        cwd = os.path.dirname(__file__)
        log_dir_path = os.path.join(cwd, 'Logs/test_regression_testing.log')
        return log_dir_path

    def get_clear_fields(self,driver):
        self.driver = driver
        self.driver.find_element_by_id("fname").clear()
        self.driver.find_element_by_id("mname").clear()
        self.driver.find_element_by_id("lname").clear()
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("designattion").clear()
        self.driver.find_element_by_id("passswd").clear()
