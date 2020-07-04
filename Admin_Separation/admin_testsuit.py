import configparser
import sys
import os

from Admin_Separation import admin_login_scripts, check_login_to_cqube, test_login_to_admin_page

from get_dir import pwd


import unittest
from fileinput import close
from HTMLTestRunner import HTMLTestRunner

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        functional_test = unittest.TestSuite()
        functional_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(admin_login_scripts.Test_admin_login),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_login_to_cqube.Test_login_to_cqube),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_login_to_admin_page.Test_admin_login),
        ])
        p= pwd()
        outfile = open("/home/chetan/Desktop/cQube/cQubeTesting/Admin_Separation/admin_separation.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Functional Test Report',
            verbosity=1,
            description="Admin login Test Result "
        )

        runner1.run(functional_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()