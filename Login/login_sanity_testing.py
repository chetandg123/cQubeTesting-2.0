import time
import unittest

from Login.Invalid_credentials_check import login_test
from Login.Login_and_logout import test_logout
from Login.check_login_with_empty_inputs import login_without_inputs
from Login.login_test_with_invalid_email import login_test_for_credentials
from Login.login_to_cQube import Login_to_cQube
from Login.login_to_cqube import Login_to_cqube
from Login.login_with_invalid_credentials import login_test_invalidvalues
from Login.login_with_invalid_password import login_test_with_invalid_password
from Login.login_with_invalid_user import login_test_with_invalid_user
from Login.login_with_valid_user_and_empty_password import login_with_no_passwd
from Login.login_wrong_credentials import login_with_wrong_values
from reuse_func import GetData


class cQube_Login_Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.total_tests = 12
        self.tests = [0] * 13
        self.data = GetData()
        self.logger = self.data.get_sanity_log()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)

    def  test_login_without_credentails(self):
        self.tests.pop()
        self.logger.info("test_login_without_credentails" + " " + "Total :" + " " + str(
            self.total_tests) + " " + "Remaining :" + " " + str(len(self.tests) - 1))
        b =login_without_inputs(self.driver)
        res =b.test_loginbtn()
        self.assertEqual(res, "This field is required", msg="Failed")
        self.logger.info("test_login_without_credentails is completed...")

    def test_login_to_cqube(self):
        self.tests.pop()
        self.logger.info("test_login_to_cqube" + " " + "Total :" + " " + str(
            self.total_tests) + " " + "Remaining :" + " " + str(len(self.tests) - 1))
        b = Login_to_cqube(self.driver)
        res = b.test_login()
        self.assertEqual("cQube",self.driver.title,msg="login is not working")
        self.logger.info("test_login_to_cqube is completed...")


    def test_invalid_inputs(self):
        self.tests.pop()
        self.logger.info("test_invalid_inputs" + " " + "Total :" + " " + str(
            self.total_tests) + " " + "Remaining :" + " " + str(len(self.tests) - 1))
        b = login_test(self.driver)
        res = b.test_login()
        self.assertEqual(res,"Enter atleast 4 characters" , msg="Failed")
        self.logger.info("test_invalid_inputs is completed...")


    def test_login_and_logout(self):
        self.tests.pop()
        self.logger.info("test_login_and_logout" + " " + "Total :" + " " + str(
            self.total_tests) + " " + "Remaining :" + " " + str(len(self.tests) - 1))
        b =test_logout(self.driver)
        res = b.test_logoutbtn()
        self.logger.info("test_login_and_logout is completed...")

    def test_login_not_valids(self):
        self.tests.pop()
        self.logger.info("test_login_not_valids" + " " + "Total :" + " " + str(
            self.total_tests) + " " + "Remaining :" + " " + str(len(self.tests) - 1))
        b = login_test(self.driver)
        res = b.test_login()
        self.assertEqual(res,"Enter atleast 4 characters" , msg="Failed")
        self.logger.info("test_login_not_valids is completed...")

    def test_credentials(self):
        self.tests.pop()
        self.logger.info("test_credentials" + " " + "Total :" + " " + str(
            self.total_tests) + " " + "Remaining :" + " " + str(len(self.tests) - 1))
        b =login_test_for_credentials(self.driver)
        res =b.test_credentials()
        self.assertEqual(res,"Invalid email address" , msg="Failed")
        self.logger.info("test_credentials is completed...")


    def test_cqube_home(self):
        self.tests.pop()
        self.logger.info("test_cqube_home" + " " + "Total :" + " " + str(
            self.total_tests) + " " + "Remaining :" + " " + str(len(self.tests) - 1))
        b =Login_to_cQube(self.driver)
        res =b.test_home()
        self.logger.info("test_cqube_home is completed...")

    def test_invalids(self):
        self.tests.pop()
        self.logger.info("test_invalids" + " " + "Total :" + " " + str(
            self.total_tests) + " " + "Remaining :" + " " + str(len(self.tests) - 1))
        b =login_test_invalidvalues(self.driver)
        res =b.test_login()
        self.assertEqual(res,"User not found" , msg="Failed")
        self.logger.info("test_invalids is completed...")

    def test_invalidpassword(self):
        self.tests.pop()
        self.logger.info("test_invalidpassword" + " " + "Total :" + " " + str(
            self.total_tests) + " " + "Remaining :" + " " + str(len(self.tests) - 1))
        b =login_test_with_invalid_password(self.driver)
        res =b.test_invalidpwd()
        self.assertEqual(res,"Enter atleast 4 characters" , msg="Failed")
        self.logger.info("test_invalidpassword is completed...")

    def test_invalidpassuser(self):
        self.tests.pop()
        self.logger.info("test_invalidpassuser" + " " + "Total :" + " " + str(
            self.total_tests) + " " + "Remaining :" + " " + str(len(self.tests) - 1))
        b =login_test_with_invalid_user(self.driver)
        res =b.test_invaliduser()
        self.assertEqual(res,"User not found" , msg="Failed")
        self.logger.info("test_invalidpassuser is completed...")

    def test_nopasswd(self):
        self.tests.pop()
        self.logger.info("test_nopasswd" + " " + "Total :" + " " + str(
            self.total_tests) + " " + "Remaining :" + " " + str(len(self.tests) - 1))
        b = login_with_no_passwd(self.driver)
        res = b.test_nopwd()
        self.assertEqual(res,"This field is required" , msg="Failed")
        self.logger.info("test_nopasswd is completed...")

    def test_wrong_values(self):
        self.tests.pop()
        self.logger.info("test_wrong_values" + " " + "Total :" + " " + str(
            self.total_tests) + " " + "Remaining :" + " " + str(len(self.tests) - 1))
        b = login_with_wrong_values(self.driver)
        res = b.test_wrongvalues()
        self.assertEqual(res,"Enter atleast 4 characters" , msg="Failed")
        self.logger.info("test_wrong_values is completed...")


    @classmethod
    def tearDownClass(cls):
            cls.driver.close()