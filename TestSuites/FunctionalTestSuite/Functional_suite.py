import unittest

from HTMLTestRunner import HTMLTestRunner

from Composite_report import composite_functional_testing
from get_dir import pwd
from reuse_func import GetData


class MyTestSuite(unittest.TestCase):

    # @classmethod
    # def setUpClass(self):
    #     self.data = GetData()
    #     self.driver = self.data.get_driver()
    #     self.driver.implicitly_wait(100)
    #     self.data.open_cqube_appln(self.driver)
    #     self.data.login_cqube(self.driver)
    #     self.data.page_loading(self.driver)
    #

    def test_issue01(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(composite_functional_testing.composite_report),
        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Composite Report functional Test Report',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
