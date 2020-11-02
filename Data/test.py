# from files import Files
#
# name = Files()
# sr_block = name.sr_block
# print(sr_block)
#
# exception_districtwise = name.exception_districtwise
# print(type(exception_districtwise))
import csv
import os

# filename="home/chetan/Downloads/collectionType_course_data_of_All_content_course.csv"
# filename ="collectionType_course_data_of_All_content_course.csv"
# print("File is " , os.path.isfile(filename))
# with open(filename) as fin:
#     csv_reader = csv.reader(fin, delimiter=',')
#     header = next(csv_reader)
#     content = 0
#     for row in csv.reader(fin):
#         content += int(row[4])
#     print(content)

# txt = "banana_"
#
# # x = txt.rstrip("_")
#
# print(txt[:-1])


with open(self.filename) as fin:
    csv_reader = csv.reader(fin, delimiter=',')
    header = next(csv_reader)
    data = list(csv_reader)
    row_count = len(data)
os.remove(self.filename)
tablecount = self.driver.find_elements_by_tag_name('tr')
records = int(len(tablecount)) - 2
time.sleep(2)
if row_count != records:
    print(districts.options[x].text, "records count mismatch in downloaded file and table records")
    count = count + 1