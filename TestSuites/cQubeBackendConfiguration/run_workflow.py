from Backend_tests.DataProcessing import static
from get_dir import pwd
import unittest
from HTMLTestRunner import HTMLTestRunner

from reuse_func import GetData


class MyTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.cal  = GetData()
        print("")

    def test_Issue01(self):
        if self.cal.get_nifi_static() == "true":
            functional_test = unittest.TestSuite()
            functional_test.addTests([
                # file name .class name
                unittest.defaultTestLoader.loadTestsFromTestCase(static.DistrictMaster),
                unittest.defaultTestLoader.loadTestsFromTestCase(static.BlockMaster),
                unittest.defaultTestLoader.loadTestsFromTestCase(static.ClusterMaster),
                unittest.defaultTestLoader.loadTestsFromTestCase(static.SchoolMaster),
                unittest.defaultTestLoader.loadTestsFromTestCase(static.SchoolManagement)
            ])
            p = pwd()
            outfile = open(p.get_nifi_workflow_report_path(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Static Nifi Workflow',
                verbosity=1,
            )
            runner1.run(functional_test)
            outfile.close()
        else:
            print("Nifi static data source is disabled")

    # def test_Issue02(self):
    #     if self.cal.get_nifi_infra() == "true":
    #
    #         functional_test = unittest.TestSuite()
    #         functional_test.addTests([
    #             # file name .class name
    #             unittest.defaultTestLoader.loadTestsFromTestCase(),
    #         ])
    #         p = pwd()
    #         outfile = open(p.get_nifi_workflow_report_path(), "a")
    #
    #         runner1 = HTMLTestRunner.HTMLTestRunner(
    #             stream=outfile,
    #             title='Infra Nifi Workflow',
    #             verbosity=1,
    #         )
    #         runner1.run(functional_test)
    #         outfile.close()
    #     else:
    #         print("Nifi infra data source is disabled")
    #
    # def test_Issue03(self):
    #     if self.cal.get_nifi_crc() == "true":
    #
    #         functional_test = unittest.TestSuite()
    #         functional_test.addTests([
    #             # file name .class name
    #             unittest.defaultTestLoader.loadTestsFromTestCase(),
    #         ])
    #         p = pwd()
    #         outfile = open(p.get_nifi_workflow_report_path(), "a")
    #
    #         runner1 = HTMLTestRunner.HTMLTestRunner(
    #             stream=outfile,
    #             title='CRC Nifi Workflow',
    #             verbosity=1,
    #         )
    #         runner1.run(functional_test)
    #         outfile.close()
    #     else:
    #         print("Nifi crc data source is disabled")
    #
    # def test_Issue04(self):
    #     if self.cal.get_nifi_attendance() == "true":
    #
    #         functional_test = unittest.TestSuite()
    #         functional_test.addTests([
    #             # file name .class name
    #             unittest.defaultTestLoader.loadTestsFromTestCase(),
    #         ])
    #         p = pwd()
    #         outfile = open(p.get_nifi_workflow_report_path(), "a")
    #
    #         runner1 = HTMLTestRunner.HTMLTestRunner(
    #             stream=outfile,
    #             title='Student attendance Nifi Workflow',
    #             verbosity=1,
    #         )
    #         runner1.run(functional_test)
    #         outfile.close()
    #     else:
    #         print("Nifi student attendance data source is disabled")
    #
    # def test_Issue05(self):
    #     if self.cal.get_nifi_teacher_attendance() == "true":
    #
    #         functional_test = unittest.TestSuite()
    #         functional_test.addTests([
    #             # file name .class name
    #             unittest.defaultTestLoader.loadTestsFromTestCase(),
    #         ])
    #         p = pwd()
    #         outfile = open(p.get_nifi_workflow_report_path(), "a")
    #
    #         runner1 = HTMLTestRunner.HTMLTestRunner(
    #             stream=outfile,
    #             title='Teacher attendance Nifi Workflow',
    #             verbosity=1,
    #         )
    #         runner1.run(functional_test)
    #         outfile.close()
    #     else:
    #         print("Nifi teacher attendance data source is disabled")
    #
    # def test_Issue06(self):
    #     if self.cal.get_nifi_pat() == "true":
    #
    #         functional_test = unittest.TestSuite()
    #         functional_test.addTests([
    #             # file name .class name
    #             unittest.defaultTestLoader.loadTestsFromTestCase(),
    #         ])
    #         p = pwd()
    #         outfile = open(p.get_nifi_workflow_report_path(), "a")
    #
    #         runner1 = HTMLTestRunner.HTMLTestRunner(
    #             stream=outfile,
    #             title='PAT Nifi Workflow',
    #             verbosity=1,
    #         )
    #         runner1.run(functional_test)
    #         outfile.close()
    #     else:
    #         print("Nifi pat data source is disabled")
    #
    # def test_Issue07(self):
    #     if self.cal.get_nifi_sat() == "true":
    #
    #         functional_test = unittest.TestSuite()
    #         functional_test.addTests([
    #             # file name .class name
    #             unittest.defaultTestLoader.loadTestsFromTestCase(),
    #         ])
    #         p = pwd()
    #         outfile = open(p.get_nifi_workflow_report_path(), "a")
    #
    #         runner1 = HTMLTestRunner.HTMLTestRunner(
    #             stream=outfile,
    #             title='SAT Nifi Workflow',
    #             verbosity=1,
    #         )
    #         runner1.run(functional_test)
    #         outfile.close()
    #     else:
    #         print("Nifi sat data source is disabled")
    #
    # def test_Issue08(self):
    #     if self.cal.get_nifi_udise() == "true":
    #
    #         functional_test = unittest.TestSuite()
    #         functional_test.addTests([
    #             # file name .class name
    #             unittest.defaultTestLoader.loadTestsFromTestCase(),
    #         ])
    #         p = pwd()
    #         outfile = open(p.get_nifi_workflow_report_path(), "a")
    #
    #         runner1 = HTMLTestRunner.HTMLTestRunner(
    #             stream=outfile,
    #             title='Udise Nifi Workflow',
    #             verbosity=1,
    #         )
    #         runner1.run(functional_test)
    #         outfile.close()
    #     else:
    #         print("Nifi udise data source is disabled")
    #
    # def test_Issue09(self):
    #     if self.cal.get_nifi_diksha() == "true":
    #
    #         functional_test = unittest.TestSuite()
    #         functional_test.addTests([
    #             # file name .class name
    #             unittest.defaultTestLoader.loadTestsFromTestCase(),
    #         ])
    #         p = pwd()
    #         outfile = open(p.get_nifi_workflow_report_path(), "a")
    #
    #         runner1 = HTMLTestRunner.HTMLTestRunner(
    #             stream=outfile,
    #             title='Diksha Nifi Workflow',
    #             verbosity=1,
    #         )
    #         runner1.run(functional_test)
    #         outfile.close()
    #     else:
    #         print("Nifi diksha data source is disabled")
    #
    # def test_Issue10(self):
    #     if self.cal.get_nifi_composite() == "true":
    #
    #         functional_test = unittest.TestSuite()
    #         functional_test.addTests([
    #             # file name .class name
    #             unittest.defaultTestLoader.loadTestsFromTestCase(),
    #         ])
    #         p = pwd()
    #         outfile = open(p.get_nifi_workflow_report_path(), "a")
    #
    #         runner1 = HTMLTestRunner.HTMLTestRunner(
    #             stream=outfile,
    #             title='Composite Nifi Workflow',
    #             verbosity=1,
    #         )
    #         runner1.run(functional_test)
    #         outfile.close()
    #     else:
    #         print("Nifi composite data source is disabled")
    #
    # def test_Issue11(self):
    #     if self.cal.get_nifi_healthcard() == "true":
    #
    #         functional_test = unittest.TestSuite()
    #         functional_test.addTests([
    #             # file name .class name
    #             unittest.defaultTestLoader.loadTestsFromTestCase(),
    #         ])
    #         p = pwd()
    #         outfile = open(p.get_nifi_workflow_report_path(), "a")
    #
    #         runner1 = HTMLTestRunner.HTMLTestRunner(
    #             stream=outfile,
    #             title='Progress card Nifi Workflow',
    #             verbosity=1,
    #         )
    #         runner1.run(functional_test)
    #         outfile.close()
    #     else:
    #        print("Nifi progress card data source is disabled")


    @classmethod
    def tearDownClass(self):
        print("")


if __name__ == '__main__':
    unittest.main()
