import time
import unittest

from reuse_func import GetData

class TeacherTransformer(unittest.TestCase):

    def test_teacher_data_processing(self,storage_type):
        if storage_type == "s3":
            cal = GetData()
            filepath = cal.get_filepath("teacher_attendance")
            result = cal.copy_file_to_s3(filepath,"teacher_attendance")
            if result.returncode == 0:
                print("teacher_attendance file is successfully uploaded to s3")
                cal.start_nifi_processor(cal.get_processor_group_id("teacher_attendance_transformer"))
                while 1:
                    if cal.get_queued_count("teacher_attendance_transformer") !=0:
                        time.sleep(60)
                    else:
                        cal.stop_nifi_processor(cal.get_processor_group_id("teacher_attendance_transformer"))
                        break
            else :
                print("teacher_attendance file is not uploaded to s3")
        else:
            cal = GetData()
            filepath = cal.get_filepath("teacher_attendance")
            result = cal.copy_file_to_local(filepath, "teacher_attendance")
            if result.returncode == 0:
                print("teacher_attendance file is successfully copied to local emission directory")
                cal.start_nifi_processor(cal.get_processor_group_id("teacher_attendance_transformer"))
                while 1:
                    if cal.get_queued_count("teacher_attendance_transformer") != 0:
                        time.sleep(60)
                    else:
                        cal.stop_nifi_processor(cal.get_processor_group_id("teacher_attendance_transformer"))
                        break
            else:
                print("teacher_attendance file is not copied to local emission directory")


if __name__ == '__main__':
    unittest.main()
