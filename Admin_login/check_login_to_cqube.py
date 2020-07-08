import unittest

from Data.parameters import Data
from reuse_func import GetData


class Test_login_to_cqube(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_vpn_cqube(self.driver)
        self.data.page_loading(self.driver)

    def test_login_with_admin(self):
        self.data.login_admin(self.driver)
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Dashboard).click()
        self.data.page_loading(self.driver)
        options = self.driver.find_elements_by_xpath(Data.dashboard_options)
        for i in range(len(options)):
            print(options[i].text)
        self.driver.find_element_by_id(Data.logout).click()
        self.data.page_loading(self.driver)

    def test_login_with_reportviewer(self):
        self.driver.find_element_by_id(Data.email).send_keys(Data.reportuser)
        self.driver.find_element_by_id(Data.passwd).send_keys(Data.reportpass)
        self.driver.find_element_by_id("login").click()
        self.data.page_loading(self.driver)
        user = self.driver.find_element_by_id("err").text
        self.assertEqual("Unauthorised User",user,msg="user  does not exists!..")
        self.data.page_loading(self.driver)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()