
from Data.parameters import Data


class click_on_hyperlink():
    def __init__(self,driver):
        self.driver = driver

    def test_link(self):
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_xpath(Data.infra_hyperlink).click()
        self.driver.find_element_by_css_selector('p >span').click()
        print(self.driver.current_url)
