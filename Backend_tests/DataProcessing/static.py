import time
import unittest

from reuse_func import GetData

class StaticTransformer(unittest.TestCase):

    def test_static_data_processing(self):
        self.cal = GetData()
        storage_type = self.cal.get_storage_type()
        if storage_type == "s3":
            filepath = self.cal.get_filepath("district_master")
            result = self.cal.copy_file_to_s3(filepath,"district_master")
            self.cal.start_nifi_processor(self.cal.get_processor_group_id("cQube_data_storage"))
            self.cal.start_nifi_processor(self.cal.get_processor_group_id("static_data_transformer"))
            time.sleep(60)
            filepath = self.cal.get_filepath("block_master")
            result = self.cal.copy_file_to_s3(filepath, "block_master")
            time.sleep(60)
            filepath = self.cal.get_filepath("cluster_master")
            result = self.cal.copy_file_to_s3(filepath, "cluster_master")
            time.sleep(60)
            filepath = self.cal.get_filepath("school_master")
            result = self.cal.copy_file_to_s3(filepath, "school_master")
            time.sleep(60)
            filepath = self.cal.get_filepath("school_management")
            result = self.cal.copy_file_to_s3(filepath, "school_management")
            time.sleep(60)
            self.cal.stop_nifi_processor(self.cal.get_processor_group_id("static_data_transformer"))
        else:
            filepath = self.cal.get_filepath("district_master")
            result = self.cal.copy_file_to_local(filepath, "district_master")
            self.cal.start_nifi_processor(self.cal.get_processor_group_id("cQube_data_storage"))
            self.cal.start_nifi_processor(self.cal.get_processor_group_id("static_data_transformer"))
            time.sleep(60)
            filepath = self.cal.get_filepath("block_master")
            result = self.cal.copy_file_to_local(filepath, "block_master")
            time.sleep(60)
            filepath = self.cal.get_filepath("cluster_master")
            result = self.cal.copy_file_to_local(filepath, "cluster_master")
            time.sleep(60)
            filepath = self.cal.get_filepath("school_master")
            result = self.cal.copy_file_to_local(filepath, "school_master")
            time.sleep(60)
            filepath = self.cal.get_filepath("school_management")
            result = self.cal.copy_file_to_local(filepath, "school_management")
            time.sleep(60)
            self.cal.stop_nifi_processor(self.cal.get_processor_group_id("static_data_transformer"))


if __name__ == '__main__':
    unittest.main()
