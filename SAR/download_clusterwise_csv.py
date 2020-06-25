import os
import re
import time
import unittest

from Data.parameters import Data
from get_dir import pwd


class ClusterwiseCsv():

    def __init__(self, driver, year, month):
        self.driver = driver
        self.year = year.strip()
        self.month = month.strip()

    def click_download_icon_of_clusters(self):
        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        time.sleep(15)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        self.filename = p.get_download_dir() + "/Cluster_wise_report_" + self.month + "_" + self.year + ".csv"
        return os.path.isfile(self.filename)

    def remove_csv(self):
        os.remove(self.filename)
