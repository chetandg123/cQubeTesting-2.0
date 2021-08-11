import time
import unittest

from reuse_func import GetData
class Composite(unittest.TestCase):

    def setUp(self):
        self.processor_name="composite"
        self.folder_name = "composite"
        self.cal = GetData()
        self.storage_type = self.cal.get_storage_type()
        self.cal.start_nifi_processor("cQube_data_storage")
        self.cal.start_nifi_processor(self.processor_name)

    def test_inspection_master(self):
                while 1 :
                    if self.cal.get_queued_count(self.processor_name) == 0 and len(self.cal.get_processor_group_error_msg(self.processor_name)) == 0:
                        print(self.folder_name.capitalize()+" data is successfully processed")
                        self.assertTrue(0 == 0,self.folder_name.capitalize()+" file is successfully processed")
                        break
                    elif len(self.cal.get_processor_group_error_msg(self.processor_name)) != 0:
                        self.assertEqual(0,len(self.cal.get_processor_group_error_msg(self.processor_name)),self.cal.get_processor_group_error_msg(self.processor_name)[0])
                        break
                    elif self.cal.get_queued_count(self.processor_name) != 0:
                        time.sleep(2)


    def tearDown(self):
        self.cal.stop_nifi_processor(self.processor_name)