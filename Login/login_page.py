import unittest

from Login.login_to_cQube import cQube_login
from reuse_func import GetData


class login(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        # self.driver = self.data.get_firefox_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.page_loading(self.driver)

    def test_login_page(self):
        function = cQube_login(self.driver)
        result = function.test_login_to_cQube()
        self.assertEqual(0,result,msg='Login is failed!')
        self.data.page_loading(self.driver)

    def test_infomsgs(self):
        self.data.page_loading(self.driver)
        info = self.driver.find_elements_by_id('tooltip-primary').get_attribute("data-original-title")
        for i in range(len(info)):
            print(info[i].text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()