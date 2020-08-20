
from reuse_func import GetData


class SemesterReport():
    def __init__(self, driver):
        self.driver = driver

    def click_on_semester(self):
        cal = GetData()
        cal.navigate_to_semester_report()
        cal.page_loading(self.driver)
        return self.driver.page_source


