import time


from Data.parameters import Data



class download_icon():
    def __init__(self,driver):
        self.driver = driver

    def test_donwload(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.scm_dist).click()
        time.sleep(4)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)

