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
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)

    def  test_login_without_credentails(self):
        b =login_without_inputs(self.driver)
        res =b.test_loginbtn()
        self.assertEqual(res, "This field is required", msg="Failed")

    def test_login_to_cqube(self):
        b = Login_to_cqube(self.driver)
        res = b.test_login()
        self.assertEqual("cQube",self.driver.title,msg="login is not working")

    def test_invalid_inputs(self):
        b = login_test(self.driver)
        res = b.test_login()
        self.assertEqual(res,"Enter atleast 4 characters" , msg="Failed")

    def test_login_and_logout(self):
        b =test_logout(self.driver)
        res = b.test_logoutbtn()

    def test_login_not_valids(self):
        b = login_test(self.driver)
        res = b.test_login()
        self.assertEqual(res,"Enter atleast 4 characters" , msg="Failed")

    def test_credentials(self):
        b =login_test_for_credentials(self.driver)
        res =b.test_credentials()
        self.assertEqual(res,"Invalid email address" , msg="Failed")


    def test_cqube_home(self):
        b =Login_to_cQube(self.driver)
        res =b.test_home()

    def test_invalids(self):
        b =login_test_invalidvalues(self.driver)
        res =b.test_login()
        self.assertEqual(res,"User validity exceeded" , msg="Failed")


    def test_invalidpassword(self):
        b =login_test_with_invalid_password(self.driver)
        res =b.test_invalidpwd()
        self.assertEqual(res,"Enter atleast 4 characters" , msg="Failed")

    def test_invalidpassuser(self):
        b =login_test_with_invalid_user(self.driver)
        res =b.test_invaliduser()
        self.assertEqual(res,"User not found" , msg="Failed")

    def test_nopasswd(self):
        b = login_with_no_passwd(self.driver)
        res = b.test_nopwd()
        self.assertEqual(res,"This field is required" , msg="Failed")

    def test_wrong_values(self):
        b = login_with_wrong_values(self.driver)
        res = b.test_wrongvalues()
        self.assertEqual(res,"Enter atleast 4 characters" , msg="Failed")


    @classmethod
    def tearDownClass(cls):
            cls.driver.close()