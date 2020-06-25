year = "2019"
month ="October"

print("District_wise_report_"+month+"_"+year+".csv")
print("District_wise_report_October_2019.csv")

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
