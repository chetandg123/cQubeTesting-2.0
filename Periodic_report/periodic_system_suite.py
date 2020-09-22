
from reuse_func import GetData
import unittest


class periodic_system_testing(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_periodic_report()
        self.data.page_loading(self.driver)















    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
