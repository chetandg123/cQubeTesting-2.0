import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class Blocks():
    def __init__(self, driver):
        self.driver = driver

    def check_markers_on_block_map(self):
        self.driver.find_element_by_id(Data.block_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        return dots

    def check_last_30_days(self):
        cal = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        times= Select(self.driver.find_element_by_id('period'))
        times.select_by_index(2)
        print(times.first_selected_option.text)
        time.sleep(3)
        schools = self.driver.find_element_by_id('schools').text
        students = self.driver.find_element_by_id('students').text
        attended = self.driver.find_element_by_id('studentsAttended').text

        schol = re.sub('\D', "", schools)
        std = re.sub('\D', "", students)
        attd = re.sub('\D', "", attended)

        print('Expected footer values : ', schol, std, attd)

        print('***************Block level footer values******************')

        self.driver.find_element_by_id(Data.block_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(5)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        markers = len(dots) - 1
        if markers == 0:
            print("Block level markers are not present ")
            count = count + 1
        else:
            bschools = self.driver.find_element_by_id('schools').text
            bsch = re.sub('\D', "", bschools)

            bstudents = self.driver.find_element_by_id('students').text
            bstd = re.sub('\D', "", bstudents)

            battended = self.driver.find_element_by_id('studentsAttended').text
            battd = re.sub('\D', "", battended)

            print('after Clicking of block footer values ', bsch, bstd, battd)

            count = 0
            if int(bsch) != int(schol):
                print('Block level footer mismatch found', int(bsch), int(schol))
                count = count + 1
            if int(bstd) != int(std):
                print('Block level footer mismatch found', int(bstd), int(std))
                count = count + 1
            if int(battd) != int(attd):
                print('Block level footer mismatch found', int(battd), int(attd))
                count = count + 1

            print('***************Cluster level footer values******************')

            self.driver.find_element_by_id(Data.cluster_btn).click()
            cal = GetData()
            cal.page_loading(self.driver)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(dots) - 1
            if dots == 0:
                print("Cluster level markers are not present ")
                count = count + 1

            cschools = self.driver.find_element_by_id('schools').text
            csch = re.sub('\D', '', cschools)

            cstudents = self.driver.find_element_by_id('students').text
            cstd = re.sub('\D', '', cstudents)

            cattended = self.driver.find_element_by_id('studentsAttended').text
            cattd = re.sub('\D', '', cattended)

            print('after Clicking of cluster footer values ', csch, cstd, cattd)

            if int(csch) != int(schol):
                print('Cluster level footer mismatch found', int(csch), int(schol))
                count = count + 1
            if int(cstd) != int(std):
                print('Cluster level footer mismatch found', int(cstd), int(std))
                count = count + 1
            if int(cattd) != int(attd):
                print('Cluster level footer mismatch found', int(cattd), int(attd))
                count = count + 1

            print('***************School level footer values******************')

            self.driver.find_element_by_id(Data.schoolbtn).click()
            cal = GetData()
            cal.page_loading(self.driver)
            result = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(result) - 1
            if dots == 0:
                print("Cluster level markers are not present ")
                count = count + 1

            sschools = self.driver.find_element_by_id('schools').text
            ssch = re.sub('\D', '', cschools)

            sstudents = self.driver.find_element_by_id('students').text
            sstd = re.sub('\D', '', cstudents)

            sattended = self.driver.find_element_by_id('studentsAttended').text
            sattd = re.sub('\D', '', cattended)

            print('after Clicking of School footer values ', ssch, sstd, sattd)

            if int(ssch) != int(schol):
                print('School level footer mismatch found', int(ssch), int(schol))
                count = count + 1
            if int(sstd) != int(std):
                print('School level footer mismatch found', int(sstd), int(std))
                count = count + 1
            if int(sattd) != int(attd):
                print('Cluster level footer mismatch found', int(sattd), int(attd))
                count = count + 1
        return count

    def check_last_7_days(self):
        cal = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        times = Select(self.driver.find_element_by_id('period'))
        times.select_by_index(3)
        print(times.first_selected_option.text)
        time.sleep(3)
        schools = self.driver.find_element_by_id('schools').text
        students = self.driver.find_element_by_id('students').text
        attended = self.driver.find_element_by_id('studentsAttended').text

        schol = re.sub('\D', "", schools)
        std = re.sub('\D', "", students)
        attd = re.sub('\D', "", attended)

        print('Expected footer values : ', schol, std, attd)

        print('***************Block level footer values******************')

        self.driver.find_element_by_id(Data.block_btn).click()
        cal = GetData()
        cal.page_loading(self.driver)
        time.sleep(5)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        markers = len(dots) - 1
        if markers == 0:
            print("Block level markers are not present ")
            count = count + 1
        else:
            bschools = self.driver.find_element_by_id('schools').text
            bsch = re.sub('\D', "", bschools)

            bstudents = self.driver.find_element_by_id('students').text
            bstd = re.sub('\D', "", bstudents)

            battended = self.driver.find_element_by_id('studentsAttended').text
            battd = re.sub('\D', "", battended)

            print('after Clicking of block footer values ', bsch, bstd, battd)

            count = 0
            if int(bsch) != int(schol):
                print('Block level footer mismatch found', int(bsch), int(schol))
                count = count + 1
            if int(bstd) != int(std):
                print('Block level footer mismatch found', int(bstd), int(std))
                count = count + 1
            if int(battd) != int(attd):
                print('Block level footer mismatch found', int(battd), int(attd))
                count = count + 1

            print('***************Cluster level footer values******************')

            self.driver.find_element_by_id(Data.cluster_btn).click()
            cal = GetData()
            cal.page_loading(self.driver)
            dots = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(dots) - 1
            if dots == 0:
                print("Cluster level markers are not present ")
                count = count + 1

            cschools = self.driver.find_element_by_id('schools').text
            csch = re.sub('\D', '', cschools)

            cstudents = self.driver.find_element_by_id('students').text
            cstd = re.sub('\D', '', cstudents)

            cattended = self.driver.find_element_by_id('studentsAttended').text
            cattd = re.sub('\D', '', cattended)

            print('after Clicking of cluster footer values ', csch, cstd, cattd)

            if int(csch) != int(schol):
                print('Cluster level footer mismatch found', int(csch), int(schol))
                count = count + 1
            if int(cstd) != int(std):
                print('Cluster level footer mismatch found', int(cstd), int(std))
                count = count + 1
            if int(cattd) != int(attd):
                print('Cluster level footer mismatch found', int(cattd), int(attd))
                count = count + 1

            print('***************School level footer values******************')

            self.driver.find_element_by_id(Data.schoolbtn).click()
            cal = GetData()
            cal.page_loading(self.driver)
            result = self.driver.find_elements_by_class_name(Data.dots)
            dots = len(result) - 1
            if dots == 0:
                print("Cluster level markers are not present ")
                count = count + 1

            sschools = self.driver.find_element_by_id('schools').text
            ssch = re.sub('\D', '', cschools)

            sstudents = self.driver.find_element_by_id('students').text
            sstd = re.sub('\D', '', cstudents)

            sattended = self.driver.find_element_by_id('studentsAttended').text
            sattd = re.sub('\D', '', cattended)

            print('after Clicking of School footer values ', ssch, sstd, sattd)

            if int(ssch) != int(schol):
                print('School level footer mismatch found', int(ssch), int(schol))
                count = count + 1
            if int(sstd) != int(std):
                print('School level footer mismatch found', int(sstd), int(std))
                count = count + 1
            if int(sattd) != int(attd):
                print('Cluster level footer mismatch found', int(sattd), int(attd))
                count = count + 1
        return count

    def check_last_30_days_districts(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        times= Select(self.driver.find_element_by_id('period'))
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        for i in range(2,len(times.options)):
            times.select_by_index(i)
            timeseries = times.options[i].text
            timeseries = timeseries.replace(' ','_')
            time.sleep(3)
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            count = 0
            for x in range(1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
                value = value[4:] + '_'
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if (len(markers) - 1) == 0:
                    print("District " + select_district.first_selected_option.text + " no data")
                    count = count + 1
                else:
                    self.driver.find_element_by_id('download').click()
                    p = pwd()
                    time.sleep(5)
                    self.filename = p.get_download_dir() + "/" + self.fname.sr_districtwise() +management+'_'+timeseries.lower()+'_allGrades__blocks_of_district_' + value.strip() + cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print("District " + select_district.first_selected_option.text + " csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            student = 0
                            schools = 0
                            attended = 0
                            for row in csv.reader(fin):
                                student += int(row[5])
                                schools += int(row[7])
                                attended +=int(row[6])
                            print(self.filename ,':', student,schools,attended)

                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)

                            attend = self.driver.find_element_by_id("studentsAttended").text
                            atd = re.sub('\D', "", attend)

                            print('value on footer', student, schools, attended)
                            print('value on csv file', studs,sc,atd)

                            if int(studs) != int(student):
                                print(
                                    "District " + select_district.first_selected_option.text + " student count mismatched",int(studs) , int(student))
                                count = count + 1

                            if int(sc) != int(schools):
                                print(
                                    "District " + select_district.first_selected_option.text + " school count mismatched",int(sc) , int(schools))
                                count = count + 1

                            if int(atd) != int(attended):
                                print("District " + select_district.first_selected_option.text + " student attended mismatched",int(atd) , int(attended))
                                count = count + 1

                        os.remove(self.filename)
            return count

    def check_last_7_days_districts(self):
        cal = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        cal.page_loading(self.driver)
        times = Select(self.driver.find_element_by_id('period'))
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        for i in range(3, len(times.options)):
            times.select_by_index(i)
            timeseries = times.options[i].text
            timeseries = timeseries.replace(' ', '_')
            time.sleep(3)
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            count = 0
            for x in range(1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_dist').get_attribute('value')
                value = value.split(":")
                values = value[1].strip()
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if (len(markers) - 1) == 0:
                    print("District " + select_district.first_selected_option.text + " no data")
                    count = count + 1
                else:
                    self.driver.find_element_by_id('download').click()
                    p = pwd()
                    time.sleep(5)
                    self.filename = p.get_download_dir() + "/" + self.fname.sr_districtwise()+management+'_'+timeseries.lower() + '_allGrades__blockPerDistricts_of_district_' + values+'_' + cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print("District " + select_district.first_selected_option.text + " csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            student = 0
                            schools = 0
                            attended = 0
                            for row in csv.reader(fin):
                                student += int(row[5])
                                schools += int(row[7])
                                attended += int(row[6])
                            print(self.filename, ':', student, schools, attended)

                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

                            school = self.driver.find_element_by_id("schools").text
                            sc = re.sub('\D', "", school)

                            attend = self.driver.find_element_by_id("studentsAttended").text
                            atd = re.sub('\D', "", attend)

                            print('value on footer', student, schools, attended)
                            print('value on csv file', studs, sc, atd)

                            if int(studs) != int(student):
                                print(
                                    "District " + select_district.first_selected_option.text + " student count mismatched",
                                    int(studs), int(student))
                                count = count + 1

                            if int(sc) != int(schools):
                                print(
                                    "District " + select_district.first_selected_option.text + " school count mismatched",
                                    int(sc), int(schools))
                                count = count + 1

                            if int(atd) != int(attended):
                                print(
                                    "District " + select_district.first_selected_option.text + " student attended mismatched",
                                    int(atd), int(attended))
                                count = count + 1

                        os.remove(self.filename)
            return count
