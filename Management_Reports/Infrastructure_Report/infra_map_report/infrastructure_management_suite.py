import unittest

from HTMLTestRunner import HTMLTestRunner

from Management_Reports.Infrastructure_Report.infra_map_report import infrastructure_report_management_3, \
    infrastructure_report_management_4, infrastructure_report_management_2, infrastructure_report_management_6, \
    infrastructure_report_management_5, infrastructure_report_management_7, infrastructure_report_management_1
from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_issue01(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_1.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_2.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_3.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_4.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_5.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_6.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(infrastructure_report_management_7.cQube_SI_Map_Report),


        ])
        p = pwd()
        outfile = open(p.get_functional_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Infrastructure functional Test Test',
            verbosity=1,

        )
        runner1.run(regression_test)
        outfile.close()
