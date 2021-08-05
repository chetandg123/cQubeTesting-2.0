import time
import unittest

from reuse_func import GetData

class StudentTransformer(unittest.TestCase):

    def test_student_data_processing(self,storage_type):
        self.cal = GetData()
        storage_type = self.cal.get_storage_type()
        if storage_type == "s3":
            filepath = self.cal.get_filepath("student_attendance")
            result = self.cal.copy_file_to_s3(filepath,"student_attendance")
            if result.returncode == 0:
                print("student_attendance file is successfully uploaded to s3")
                self.cal.start_nifi_processor(self.cal.get_processor_group_id("student_attendance_transformer"))
                while 1:
                    if self.cal.get_queued_count("student_attendance_transformer") !=0:
                        time.sleep(60)
                    else:
                        self.cal.stop_nifi_processor(self.cal.get_processor_group_id("student_attendance_transformer"))
                        break
            else :
                print("student_attendance file is not uploaded to s3")
        else:
            filepath = self.cal.get_filepath("student_attendance")
            result = self.cal.copy_file_to_local(filepath, "student_attendance")
            if result.returncode == 0:
                print("student_attendance file is successfully copied to local emission directory")
                self.cal.start_nifi_processor(self.cal.get_processor_group_id("student_attendance_transformer"))
                while 1:
                    if self.cal.get_queued_count("student_attendance_transformer") != 0:
                        time.sleep(60)
                    else:
                        self.cal.stop_nifi_processor(self.cal.get_processor_group_id("student_attendance_transformer"))
                        break
            else:
                print("student_attendance file is not copied to local emission directory")


if __name__ == '__main__':
    unittest.main()
