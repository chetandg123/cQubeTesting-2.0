import unittest

from HTMLTestRunner import HTMLTestRunner

from Management_Reports.UDISE_Management_report import udise_management_1, udise_management_2, udise_management_3, \
    udise_management_4, udise_management_5, udise_management_6, udise_management_7
from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_issue01(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_1.cQube_udise_management_wise_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_2.cQube_udise_management_wise_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_3.cQube_udise_management_wise_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_4.cQube_udise_management_wise_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_5.cQube_udise_management_wise_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_6.cQube_udise_management_wise_reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(udise_management_7.cQube_udise_management_wise_reports),




        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Udise functional Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()
