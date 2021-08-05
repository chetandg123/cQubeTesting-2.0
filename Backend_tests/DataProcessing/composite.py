import time
import unittest

from reuse_func import GetData

class CompositeTransformer(unittest.TestCase):

    def test_composite_data_processing(self,storage_type):
        if storage_type == "s3":
            self.cal = GetData()
            self.cal.start_nifi_processor(self.cal.get_processor_group_id("composite_transformer"))
            time.sleep(60000)
            self.cal.stop_nifi_processor(self.cal.get_processor_group_id("composite_transformer"))
        else:
            self.cal.start_nifi_processor(self.cal.get_processor_group_id("composite_transformer"))
            time.sleep(60000)
            self.cal.stop_nifi_processor(self.cal.get_processor_group_id("composite_transformer"))


if __name__ == '__main__':
    unittest.main()
