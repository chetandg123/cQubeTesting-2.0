import configparser
import sys
import os
sys.path.append('/home/devraj/PycharmProjects/cQubeTesting')
from get_dir import pwd
from CRC import crc
from Login import cQube_login
from SI.MAP import SI_mapreport
from SI.Report import SI_Report




import unittest
from fileinput import close
from HTMLTestRunner import HTMLTestRunner

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(cQube_login.cQube_Login_Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(crc.cQube_CRC_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(SI_mapreport.cQube_SI_Map_Report),
            unittest.defaultTestLoader.loadTestsFromTestCase(SI_Report.cQube_SI_Report)
        ])
        p= pwd()
        outfile = open(p.get_functional_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Functional Test Report',
            verbosity=1,
        )

        runner1.run(functional_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()