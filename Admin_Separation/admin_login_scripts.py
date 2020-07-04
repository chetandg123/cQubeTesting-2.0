import time
import unittest
from select import select

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from Login.login_to_cqube import Login_to_cqube
from get_dir import pwd
from reuse_func import GetData


class Test_admin_login(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.p = pwd()
        self.driver = self.data.get_driver()
        self.data.open_admin_appln(self.driver)
        self.data.page_loading(self.driver)
        self.data.login_admin(self.driver)

    def test_admin_page(self):
        pagetitle = self.driver.find_element_by_tag_name("h1").text
        self.assertEqual("Create User",pagetitle,msg="Admin login page is not exists")

    def test_login_to_adminpage(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.logout).click()
        self.data.page_loading(self.driver)
        self.data.login_admin(self.driver)
        self.data.page_loading(self.driver)

    def test_dashboardoptions(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Dashboard).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.cuser).click()
        self.data.page_loading(self.driver)
        createuser = self.driver.find_element_by_xpath("//h1").text
        self.assertEqual(createuser,"Create User",msg="Create user page is not loaded ")

    def test_create_user(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Dashboard).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.cuser).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id("fname").send_keys("admin2")
        self.driver.find_element_by_id("mname").send_keys("admins")
        self.driver.find_element_by_id("lname").send_keys("admin")
        self.driver.find_element_by_id("Mgender").click()
        self.driver.find_element_by_id("email").send_keys("admin2@cqube.com")
        self.driver.find_element_by_id("designattion").send_keys("Admin")
        self.driver.find_element_by_id("passswd").send_keys("admin2")
        self.driver.find_element_by_id("btn").click()
        self.p.get_clear_fields(self.driver)
        self.data.page_loading(self.driver)

    def test_create_adminrole(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Dashboard).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.cuser).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id("fname").send_keys("admin")
        self.driver.find_element_by_id("mname").send_keys("admins")
        self.driver.find_element_by_id("lname").send_keys("admin")
        self.driver.find_element_by_id("Mgender").click()
        self.driver.find_element_by_id("email").send_keys("adminrole@cqube.com")
        self.driver.find_element_by_id("designattion").send_keys("Admin")
        role = (Select(self.driver.find_element_by_id("role")))
        for i in range(len(role.options)):
            role.select_by_visible_text(" Admin ")
            self.data.page_loading(self.driver)
        self.driver.find_element_by_id("passswd").send_keys("adminrole")
        self.driver.find_element_by_id("btn").click()
        self.p.get_clear_fields(self.driver)
        self.data.page_loading(self.driver)

    def test_create_report_viewer(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Dashboard).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.cuser).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id("fname").send_keys("dashboard")
        self.driver.find_element_by_id("mname").send_keys("report")
        self.driver.find_element_by_id("lname").send_keys("viewer")
        self.driver.find_element_by_id("Fgender").click()
        self.driver.find_element_by_id("email").send_keys("reportviewer@cqube.com")
        self.driver.find_element_by_id("designattion").send_keys("Admin")
        role = (Select(self.driver.find_element_by_id("role")))
        for i in range(len(role.options)):
            role.select_by_visible_text(" Dashboard report viewer ")
            self.data.page_loading(self.driver)
        self.driver.find_element_by_id("passswd").send_keys("report123")
        self.driver.find_element_by_id("btn").click()
        self.p.get_clear_fields(self.driver)
        self.data.page_loading(self.driver)

    def test_chagepassword(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Dashboard).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.cpass).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id("newPasswd").send_keys("")
        self.driver.find_element_by_id("cnfPasswd").send_keys("")
        self.driver.find_element_by_id("btn").click()
        self.data.page_loading(self.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
