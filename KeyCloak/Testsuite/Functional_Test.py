from Authentications import Authentication_option
from Clients import  Clients_testing
from RealmSetting import realm_setting
from Roles import roles_option
from Users import user_list
from get_dir import pwd
import unittest
from HTMLTestRunner import HTMLTestRunner

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):

            functional_test = unittest.TestSuite()
            functional_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(Authentication_option.Authentication_options),
                unittest.defaultTestLoader.loadTestsFromTestCase(Clients_testing.Clients),
                unittest.defaultTestLoader.loadTestsFromTestCase(realm_setting.realm_settings),
                unittest.defaultTestLoader.loadTestsFromTestCase(roles_option.roles_options),
                unittest.defaultTestLoader.loadTestsFromTestCase(user_list.user_options),
            ])
            p= pwd()
            outfile = open(p.get_functional_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Keycloak  Test Report',
                verbosity=1,
            )

            runner1.run(functional_test)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()