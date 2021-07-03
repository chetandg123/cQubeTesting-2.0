import time
import unittest

from get_dir import pwd
from reuse_func import GetData


class Data_retention(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.p = pwd()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_to_adminconsole(self.driver)
        time.sleep(2)
