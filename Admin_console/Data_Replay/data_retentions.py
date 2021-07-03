from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

from reuse_func import GetData



class data_retentions():

    def __init__(self,driver):
        self.driver = driver

    def check_with_default_retention_period(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath("//div[@id='replay']").click()
        self.data.page_loading(self.driver)
        ret_days=Select(self.driver.find_element_by_id('retDays'))
        default = ret_days.first_selected_option()
        if default == '90':
            print("Default selection of data retention is working ")
        else:
            print('Default Data retention days is not showing')
            count = count + 1
        self.driver.find_element_by_id('ret-submit').click()
        obj = Alert(self.driver)
        obj.accept()
        self.data.page_loading(self.driver)
        return count

    def check_with_highest_retention_period(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath("//div[@id='replay']").click()
        self.data.page_loading(self.driver)
        ret_days=Select(self.driver.find_element_by_id('retDays'))
        days = ret_days.select_by_visible_text('360')
        if ret_days.first_selected_option() == '360':
            print(ret_days.first_selected_option(),"selection of data retention is working ")
        else:
            print(ret_days.first_selected_option(),'Data retention days is not Selected')
            count = count + 1
        self.driver.find_element_by_id('ret-submit').click()
        obj = Alert(self.driver)
        obj.accept()
        self.data.page_loading(self.driver)
        return count
    def check_with_lowest_retention_period(self):
        self.data = GetData()
        count = 0
        self.driver.find_element_by_xpath("//div[@id='replay']").click()
        self.data.page_loading(self.driver)
        ret_days=Select(self.driver.find_element_by_id('retDays'))
        days = ret_days.select_by_visible_text('30')
        if ret_days.first_selected_option() == '30':
            print(ret_days.first_selected_option(),"selection of data retention is working ")
        else:
            print(ret_days.first_selected_option(),'Data retention days is not Selected')
            count = count + 1
        self.driver.find_element_by_id('ret-submit').click()
        obj = Alert(self.driver)
        obj.accept()
        self.data.page_loading(self.driver)
        return count

