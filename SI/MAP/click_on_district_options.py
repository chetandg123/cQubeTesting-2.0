import time


from Data.parameters import Data


class District_options():
    def __init__(self,driver):
        self.driver = driver
    def test_options(self):
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        time.sleep(5)
        Districts = self.driver.find_elements_by_xpath(Data.sc_choosedist)
        for i in range(len(Districts)):
            Districts[i].click()
            time.sleep(5)
            print(Districts[i].text)

