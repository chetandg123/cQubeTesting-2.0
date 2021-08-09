import time
import unittest

from reuse_func import GetData

class StaticDistrictMaster(unittest.TestCase):

    def setUp(self):
        self.cal = GetData()
        self.storage_type = self.cal.get_storage_type()
        self.cal.start_nifi_processor(self.cal.get_processor_group_id("cQube_data_storage"))
        self.cal.start_nifi_processor(self.cal.get_processor_group_id("static_data_transformer"))
        self.filepath = self.cal.get_filepath("district_master")

    def test_static_district_master(self):
        if self.storage_type == "s3":
            self.processor_name="static_data_transformer"
            result = self.cal.copy_file_to_s3(self.filepath, "district_master")
            if result.returncode == 0:
                print("District master file is successfully uploaded to s3")
                while 1 :
                    if self.cal.get_queued_count("static_data_transformer") ==0 and len(self.cal.get_processor_group_error_msg("static_data_transformer"))==0:
                       self.assertTrue("district master file is successfully processed")
                       break
                    elif len(self.cal.get_processor_group_error_msg("static_data_transformer"))!=0:
                        self.assertEqual(0,len(self.cal.get_processor_group_error_msg("static_data_transformer")),self.cal.get_processor_group_error_msg("static_data_transformer"))
                        break
                    elif self.cal.get_queued_count("static_data_transformer") !=0:
                        time.sleep(60)
            else:
                print("District master file is not uploaded to s3")
        else:
            filepath = self.cal.get_filepath("district_master")
            result = self.cal.copy_file_to_local(filepath, "district_master")

    def tearDown(self):
        print()

if __name__ == '__main__':
    unittest.main()
