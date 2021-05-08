import csv
import os
import re
import time

import pandas as pd
from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class pat_time_periodwise():
    def __init__(self, driver):
        self.driver = driver

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
                print("School level markers are not present ")
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
                print('School level footer mismatch found', int(sattd), int(attd))
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
                    self.filename = p.get_download_dir() + "/" + self.fname.pat_districtwise() +management+'_'+timeseries.lower()+'_allGrades__blocks_of_district_' + value.strip() + cal.get_current_date() + '.csv'
                    if not os.path.isfile(self.filename):
                        print("District " + select_district.first_selected_option.text + " csv is not downloaded")
                        count = count + 1
                    else:
                        # with open(self.filename) as fin:
                        #     csv_reader = csv.reader(fin, delimiter=',')
                        #     header = next(csv_reader)
                        #     student = 0
                        #     schools = 0
                        #     attended = 0
                        #     for row in csv.reader(fin):
                        #         student += int(row[5])
                        #         schools += int(row[7])
                        #         attended +=int(row[6])
                        data = pd.read_csv(self.filename)
                        student = data['Total Students'].sum()
                        schools = data['Total Schools'].sum()
                        attended = data['Students Attended'].sum()
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
                    self.filename = p.get_download_dir() + "/" + self.fname.pat_districtwise()+management+'_'+timeseries.lower() + '_allGrades__blocks_of_district_' + values+'_' + cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print("District " + select_district.first_selected_option.text + " csv is not downloaded")
                        count = count + 1
                    else:
                        # with open(self.filename) as fin:
                        #     csv_reader = csv.reader(fin, delimiter=',')
                        #     header = next(csv_reader)
                        #     student = 0
                        #     schools = 0
                        #     attended = 0
                        #     for row in csv.reader(fin):
                        #         student += int(row[5])
                        #         schools += int(row[7])
                        #         attended += int(row[6])
                        #     print(self.filename, ':', student, schools, attended)
                        data = pd.read_csv(self.filename)
                        student = data['Total Students'].sum()
                        schools = data['Total Schools'].sum()
                        attended = data['Students Attended'].sum()
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


    def check_districts_block(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        count = 0
        for x in range(len(select_district.options)-1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(len(select_block.options)-2, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                value = value[4:]+'_'
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if len(markers) - 1 == 0:
                    print("District" + select_district.first_selected_option.text +"Block"+ select_block.first_selected_option.text +"No Data")
                    count = count + 1
                else:
                    time.sleep(2)
                    self.driver.find_element_by_id('download').click()
                    time.sleep(2)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + self.fname.pat_blockwise()+management+'_all_allGrades__clusters_of_block_'+value.strip()+cal.get_current_date()+'.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print("District" + select_district.first_selected_option.text +"Block"+ select_block.first_selected_option.text+"csv is not downloaded")
                        count = count + 1
                    else:
                        with open(self.filename) as fin:
                            csv_reader = csv.reader(fin, delimiter=',')
                            header = next(csv_reader)
                            data = list(csv_reader)
                            row_count = len(data)
                            dots = len(markers) - 1
                            if dots != row_count:
                                print('Markers records and csv file records are not matching ', dots, row_count)
                                count = count + 1
                        os.remove(self.filename)
                return count

    def check_last30days_districts_block(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period =Select(self.driver.find_element_by_id('period'))
        period.select_by_index(2)
        timeseries = period.first_selected_option.text
        timeseries = timeseries.lower().replace(" ",'_')
        time.sleep(3)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        count = 0
        for x in range(len(select_district.options) - 1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                value = value.split(":")
                values = value[1].strip()
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if len(markers) - 1 == 0:
                    print(
                        "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Data")
                    count = count + 1
                else:
                    time.sleep(2)
                    self.driver.find_element_by_id('download').click()
                    time.sleep(3)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + self.fname.pat_blockwise()+management+'_'+timeseries+'_allGrades__clusters_of_block_' + values+'_' + cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    else:
                        data = pd.read_csv(self.filename)
                        student = data['Total Students'].sum()
                        schools = data['Total Schools'].sum()
                        attended = data['Students Attended'].sum()
                        students = self.driver.find_element_by_id("students").text
                        studs = re.sub('\D', "", students)

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
                                "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + " student count mismatched",
                                int(studs), int(student))
                            count = count + 1

                        if int(sc) != int(schools):
                            print(
                                "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text+ " school count mismatched",
                                int(sc), int(schools))
                            count = count + 1

                        if int(atd) != int(attended):
                            print(
                                "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text+ " student attended mismatched",
                                int(atd), int(attended))
                            count = count + 1

                    os.remove(self.filename)
                    return count

    def check_last7days_districts_block(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(3)
        timeseries = period.first_selected_option.text
        timeseries = timeseries.lower().replace(" ", '_')
        time.sleep(3)
        select_district = Select(self.driver.find_element_by_id('choose_dist'))
        select_block = Select(self.driver.find_element_by_id('choose_block'))
        count = 0
        for x in range(len(select_district.options) - 1, len(select_district.options)):
            select_district.select_by_index(x)
            cal.page_loading(self.driver)
            for y in range(len(select_block.options)-3, len(select_block.options)):
                select_block.select_by_index(y)
                cal.page_loading(self.driver)
                value = self.driver.find_element_by_id('choose_block').get_attribute('value')
                value = value.split(":")
                values = value[1].strip()
                markers = self.driver.find_elements_by_class_name(Data.dots)
                if len(markers) - 1 == 0:
                    print(
                        "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "No Data")
                    count = count + 1
                else:
                    time.sleep(2)
                    self.driver.find_element_by_id('download').click()
                    time.sleep(2)
                    p = pwd()
                    self.filename = p.get_download_dir() + "/" + self.fname.pat_blockwise() + management +"_"+timeseries + '_allGrades__clusters_of_block_' + values+"_"+ cal.get_current_date() + '.csv'
                    print(self.filename)
                    if not os.path.isfile(self.filename):
                        print(
                            "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "csv is not downloaded")
                        count = count + 1
                    else:
                        data = pd.read_csv(self.filename)
                        student = data['Total Students'].sum()
                        schools = data['Total Schools'].sum()
                        attended = data['Students Attended'].sum()
                        students = self.driver.find_element_by_id("students").text
                        studs = re.sub('\D', "", students)

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
                                "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + " student count mismatched",
                                int(studs), int(student))
                            count = count + 1

                        if int(sc) != int(schools):
                            print(
                                "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text+ " school count mismatched",
                                int(sc), int(schools))
                            count = count + 1

                        if int(atd) != int(attended):
                            print(
                                "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text+ " student attended mismatched",
                                int(atd), int(attended))
                            count = count + 1

                    os.remove(self.filename)
                    return count

    def check_last30_district_block_cluster(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(2)
        time.sleep(3)
        if 'No Data found' in self.driver.page_source:
            print(period.first_selected_option.text, ' is not having data')
        else:
            timeseries = period.first_selected_option.text
            timeseries = timeseries.lower().replace(" ", '_')
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            select_block = Select(self.driver.find_element_by_id('choose_block'))
            select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
            count = 0
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                for y in range(len(select_block.options) - 1, len(select_block.options)):
                    select_block.select_by_index(y)
                    cal.page_loading(self.driver)
                    for z in range(len(select_cluster.options) - 2, len(select_cluster.options)):
                        select_cluster.select_by_index(z)
                        time.sleep(2)
                        cal.page_loading(self.driver)
                        value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                        value = value.split(":")
                        values = value[1].strip() + '_'
                        markers = self.driver.find_elements_by_class_name(Data.dots)
                        if len(markers) - 1 == 0:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                            count = count + 1
                        time.sleep(2)
                        self.driver.find_element_by_id('download').click()
                        time.sleep(3)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.pat_clusterwise() + management + '_' + timeseries + '_allGrades__schools_of_cluster_' + values + cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                            count = count + 1
                        else:
                            data = pd.read_csv(self.filename)
                            student = data['Total Students'].sum()
                            schools = data['Total Schools'].sum()
                            attended = data['Students Attended'].sum()
                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

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
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text+ " student count mismatched",
                                    int(studs), int(student))
                                count = count + 1

                            if int(sc) != int(schools):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text+ " school count mismatched",
                                    int(sc), int(schools))
                                count = count + 1

                            if int(atd) != int(attended):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text+ " student attended mismatched",
                                    int(atd), int(attended))
                                count = count + 1

                            os.remove(self.filename)
                        return count


    def check_last7_district_block_cluster(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        period = Select(self.driver.find_element_by_id('period'))
        period.select_by_index(3)
        time.sleep(3)
        if 'No Data found' in self.driver.page_source:
            print(period.first_selected_option.text, ' is not having data')
        else:
            timeseries = period.first_selected_option.text
            timeseries = timeseries.lower().replace(" ", '_')
            select_district = Select(self.driver.find_element_by_id('choose_dist'))
            select_block = Select(self.driver.find_element_by_id('choose_block'))
            select_cluster = Select(self.driver.find_element_by_id('choose_cluster'))
            count = 0
            for x in range(len(select_district.options) - 1, len(select_district.options)):
                select_district.select_by_index(x)
                cal.page_loading(self.driver)
                for y in range(len(select_block.options) - 1, len(select_block.options)):
                    select_block.select_by_index(y)
                    cal.page_loading(self.driver)
                    for z in range(len(select_cluster.options) - 2, len(select_cluster.options)):
                        select_cluster.select_by_index(z)
                        time.sleep(2)
                        cal.page_loading(self.driver)
                        value = self.driver.find_element_by_id('choose_cluster').get_attribute('value')
                        value = value.split(":")
                        values = value[1].strip() + '_'
                        markers = self.driver.find_elements_by_class_name(Data.dots)
                        if len(markers) - 1 == 0:
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "No data")
                            count = count + 1
                        time.sleep(2)
                        self.driver.find_element_by_id('download').click()
                        time.sleep(3)
                        p = pwd()
                        self.filename = p.get_download_dir() + "/" + self.fname.pat_clusterwise() + management + '_' + timeseries + '_allGrades__schools_of_cluster_' + values + cal.get_current_date() + '.csv'
                        print(self.filename)
                        if not os.path.isfile(self.filename):
                            print(
                                "District" + select_district.first_selected_option.text + "Block" + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + "csv is not downloaded")
                            count = count + 1
                        else:
                            data = pd.read_csv(self.filename)
                            student = data['Total Students'].sum()
                            schools = data['Total Schools'].sum()
                            attended = data['Students Attended'].sum()
                            students = self.driver.find_element_by_id("students").text
                            studs = re.sub('\D', "", students)

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
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text + " student count mismatched",
                                    int(studs), int(student))
                                count = count + 1

                            if int(sc) != int(schools):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text+ " school count mismatched",
                                    int(sc), int(schools))
                                count = count + 1

                            if int(atd) != int(attended):
                                print(
                                    "District " + select_district.first_selected_option.text + "Block " + select_block.first_selected_option.text + "Cluster" + select_cluster.first_selected_option.text+ " student attended mismatched",
                                    int(atd), int(attended))
                                count = count + 1

                            os.remove(self.filename)
                        return count
