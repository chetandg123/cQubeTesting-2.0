import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data.parameters import Data


class Schools():
    def __init__(self, driver):
        self.driver = driver

    def check_markers_on_clusters_map(self):
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        time.sleep(30)
        result = self.driver.find_elements_by_class_name(Data.dots)
        return   result

    # def check_markers_on_clusters_map(self):
    #     try :
    #
    #         self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
    #         time.sleep(40)
    #         result= self.driver.find_elements_by_class_name(Data.dots)
    #         return result
    #     except ElementClickInterceptedException:
    #         print("Element is not available")

