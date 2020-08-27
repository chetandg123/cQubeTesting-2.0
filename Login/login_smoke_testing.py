import unittest

from Login.login_to_cqube import Login_to_cqube
from reuse_func import GetData


class cQube_Login_smoke_Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.page_loading(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)

    def test_login_to_cqube(self):
        b = Login_to_cqube(self.driver)
        res = b.test_login()
        print(self.driver.title)
        self.assertEqual("Log in to cQube", self.driver.title, msg="login is not working")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
