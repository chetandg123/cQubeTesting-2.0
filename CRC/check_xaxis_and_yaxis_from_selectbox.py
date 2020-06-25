import time


from Data.parameters import Data

from get_dir import pwd


class plot_values():
    def __init__(self,driver):
        self.driver =driver

    def test_plots(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        xaxis_lists = self.driver.find_elements_by_xpath(Data.xaxis)
        yaxis_lists = self.driver.find_elements_by_xpath(Data.yaxis)
        count = len(xaxis_lists)-1

        for i in range(len(xaxis_lists)):
            xaxis_lists[i].click()
            time.sleep(3)
        for j in range(len(yaxis_lists)):
                yaxis_lists[j].click()
                time.sleep(4)
        time.sleep(3)
        return count
