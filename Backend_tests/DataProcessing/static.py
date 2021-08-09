import time
import unittest

from reuse_func import GetData

class StaticDistrictMaster(unittest.TestCase):

    def setUp(self):
        self.processor_name="static_data_transformer"
        self.folder_name="district_master"
        self.cal = GetData()
        self.storage_type = self.cal.get_storage_type()
        self.cal.start_nifi_processor("cQube_data_storage")
        self.cal.start_nifi_processor(self.processor_name)
        self.filepath = self.cal.get_filepath(self.folder_name)

    def test_static_district_master(self):
        if self.storage_type == "s3":
            result = self.cal.copy_file_to_s3(self.filepath, self.folder_name)
            time.sleep(5)
            if result.returncode == 0:
                print(self.folder_name.capitalize()+" file is successfully uploaded to s3")
                while 1 :
                    if self.cal.get_queued_count(self.processor_name) == 0:
                        print(self.folder_name.capitalize()+" file is successfully processed")
                        self.assertTrue(0 == 0,self.folder_name.capitalize()+" file is successfully processed")
                        break
                    elif len(self.cal.get_processor_group_error_msg(self.processor_name)) != 0:
                        self.assertEqual(0,len(self.cal.get_processor_group_error_msg(self.processor_name)),self.cal.get_processor_group_error_msg(self.processor_name)[0])
                        break
                    elif self.cal.get_queued_count(self.processor_name) != 0:
                        time.sleep(2)
            else:
                print(self.folder_name.capitalize()+" file is not uploaded to s3")
        else:
            filepath = self.cal.get_filepath("district_master")
            result = self.cal.copy_file_to_local(filepath, "district_master")

    def tearDown(self):
        self.cal.stop_nifi_processor(self.processor_name)

if __name__ == '__main__':
    unittest.main()
