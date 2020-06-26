import time

from reuse_func import GetData

data = GetData()
logger = data.get_regression_log()

import unittest

from reuse_func import GetData


class Test(unittest.TestCase):
    total = 3

    def test_add(self,):
        data = GetData()
        logger = data.get_regression_log()
        log = GetData()
        print("adding",)
        time.sleep(3)

    def test_sub(self):
        data = GetData()
        logger = data.get_regression_log()
        print("subtracitn")
        time.sleep(3)

    def test_div(self):
        data = GetData()
        logger = data.get_regression_log()
        print("dividing")
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()

# import time
#
# from selenium.common.exceptions import WebDriverException
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from Data.parameters import Data
# from get_dir import pwd
# from reuse_func import GetData
#
# p = pwd()
# getdata = GetData()
#
# options = Options()
# options.page_load_strategy = 'normal'
# driver = webdriver.Chrome(options=options,executable_path='/home/devraj/PycharmProjects/cQubeTesting/Driver/chromedriver')
#
# getdata.open_cqube_appln(driver)
# getdata.login_cqube(driver)
# driver.find_element_by_id(Data.SAR_Schools_btn).click()
#
# wait = WebDriverWait(driver,30)
# elemnet =wait.until(EC.element_to_be_clickable((By.ID,'home')))
#
# dots = driver.find_elements_by_class_name(Data.dots)
# print(len(dots))
# time.sleep(2)

# import time
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.select import Select
#
# from Data.parameters import Data
# from get_dir import pwd
# from reuse_func import GetData
#
# p = pwd()
# getdata = GetData()
# driver = getdata.get_driver()
# getdata.open_cqube_appln(driver)
# getdata.login_cqube(driver)
# dots = driver.find_elements_by_class_name(Data.dots)
# actions = ActionChains(driver)
# list = []
# for x in dots:
#     actions.move_to_element(x).perform()
#     print("data is "+ x.text)
#     dots.pop(0)
#     time.sleep(3)
# actions.move_to_element(dots).perform()


# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# from Data.parameters import Data
# from get_dir import pwd
# from reuse_func import GetData
#
# p = pwd()
# getdata = GetData()
# driver = getdata.get_driver()
# getdata.open_cqube_appln(driver)
# getdata.login_cqube(driver)
# select_district = Select(driver.find_element_by_name('myDistrict'))
# select_block = Select(driver.find_element_by_name('myBlock'))
# select_cluster = Select(driver.find_element_by_name('myCluster'))
# loader = driver.find_element_by_id('loader')
# print(loader)
# count = 0
# for x in range(1, len(select_district.options)):
#     select_district.select_by_index(x)
#     driver.implicitly_wait(5,)
#     for y in range(1, len(select_block.options)):
#         select_block.select_by_index(y)
#         driver.implicitly_wait(5)
#         for z in range(1, len(select_cluster.options)):
#             select_cluster.select_by_index(z)
#             driver.implicitly_wait(5)
