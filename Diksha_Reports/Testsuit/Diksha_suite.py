import unittest

from HTMLTestRunner import HTMLTestRunner

from Diksha_Reports.Diksha_charts import  diksha_chart_Regression_testing
from Diksha_Reports.Diksha_column_chart import column_chart
from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_issue01(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(column_chart.cQube_diskha_column_report),
        ])
        p = pwd()
        outfile = open("path",'w')
        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Diksha Column Test Report',
            verbosity=1,

        )
        runner1.run(smoke_test)

    # def test_issue02(self):
    #     smoke_test = unittest.TestSuite()
    #     smoke_test.addTests([
    #         unittest.defaultTestLoader.loadTestsFromTestCase(diksha_table.cQube_diskha_report),
    #     ])
    #     p = pwd()
    #     outfile = open("/home/chetan/Desktop/cQubeTesting/Diksha_Reports/Testsuit/DikshaReports_regression.html", "a")
    #
    #     runner1 = HTMLTestRunner.HTMLTestRunner(
    #         stream=outfile,
    #         title='Diksha Table Regression Report',
    #         verbosity=1,
    #
    #     )
    #     runner1.run(smoke_test)
    #     outfile.close()
    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()