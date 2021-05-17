import csv
import datetime
import re
import unittest
from datetime import date

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from reuse_func import GetData

#
# class cQube_Student_Attendance_exception(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(self):
#         self.data = GetData()
#         self.driver = self.data.get_driver()
#         self.data.open_cqube_appln(self.driver)
#         self.data.login_cqube(self.driver)
#         self.data.navigate_to_student_exception()
#         self.data.page_loading(self.driver)
#
#     def test_demo_month_year(self):
#         self.data.page_loading(self.driver)
#         times = Select(self.driver.find_element_by_id('period'))
#         times.select_by_visible_text(' Year and Month ')
#         self.data.page_loading(self.driver)
#         year = Select(self.driver.find_element_by_id(Data.sar_year))
#         month = Select(self.driver.find_element_by_id(Data.sar_month))
#         self.year = (year.first_selected_option.text).strip()
#         self.month= (month.first_selected_option.text).strip()
#         self.data.page_loading(self.driver)
#         print(self.year,self.month)
#
#
#
#
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.close()
# today = date.today().strftime('%d-%m-%Y').strip()
# print(today)

# value = '1: 2425040001'
# csv2 = '2: 242504002'
# value = '32: 2407'
# value = "1: 234333"
# print(value[1:].replace(':',''))
# value = value[3:].strip()
# print(value)
#
# s = "Chetan"
# # print(s.lower())
#
# str = "management Type: Overall"
# # print(str[16:].strip().lower())
# print(str.capitalize())

value="6: 242506"
value = value.split(":")
print(value[1].strip())
#
# schools="Number of Schools: 107"
# # schol = re.sub('\D','',schools)
# # print(schol)
# print(schools.replace(' ','_'))

# with open("/home/chetan/Desktop/semester_assessment_test_exception_overall_overall_allGrades__blocks_of_district_2407_07-05-2021.csv") as fin:
#     csv_reader = csv.reader(fin, delimiter=',')
#     header = next(csv_reader)
#     schools = 0
# import pandas as pd
# # df = pd.read_csv("/home/chetan/Desktop/semester_assessment_test_exception_overall_overall_allGrades__blocks_of_district_2407_07-05-2021.csv")
# # print(df.head())
# # df['total'] = df['Schools With Missing Data'].sum()
# # print(df)
#
# data = pd.read_csv("/home/chetan/Desktop/semester_assessment_test_exception_overall_overall_allGrades__blocks_of_district_2407_07-05-2021.csv")
#
# # sum of all salary
# print(data)
# val = data["Total Schools With Missing Data"].sum()
# print(val)
long_month_name="January"
datetime_object = datetime.datetime.strptime(long_month_name, "%B")
month_number = datetime_object.month
print(month_number)