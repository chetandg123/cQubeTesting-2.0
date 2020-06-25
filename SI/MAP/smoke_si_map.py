import time
import unittest

from SI.MAP.check_with_districts_from_select_box import District_names
from SI.MAP.check_with_map_on_schoolinfra import check_markers_on_map
from SI.MAP.check_with_schoolinfra_options import School_infra_options
from SI.MAP.click_on_Dashboard import click_dashboard
from SI.MAP.click_on_anydistrict_and_download_csv import download_icon

from SI.MAP.click_on_blk_clus_school_and_home import click_on_home
from SI.MAP.click_on_block_cluster_school_and_check_schoolscount import Block_school_count
from SI.MAP.click_on_blocks import click_on_blocks
from SI.MAP.click_on_clusters import cluster_button
from SI.MAP.click_on_district_options import District_options

from SI.MAP.click_on_hyperlink import click_on_hyperlink
from SI.MAP.click_on_infra_scores_options import select_infrascore_options
from SI.MAP.download_districtwise_csv import districtwise_csv
from SI.MAP.mouseover_on_districtwise import mouseover
from SI.MAP.select_district_block_from_select_box import select_blockwise

from reuse_func import GetData


class cQube_SI_Map_Report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_school_infrastructure_map()
        time.sleep(5)

    def test_click_on_block(self):
        b = click_on_blocks(self.driver)
        res = b.test_blocks_button()
        self.assertNotEqual(0, res, msg="Records are not present on map ")

    def test_check_district_names(self):
        b = District_names(self.driver)
        result = b.test_districtlist()
        self.assertNotEqual(0,result,msg="All Districts are not present in select box!..")

    def test_check_markes_on_map(self):
        b = check_markers_on_map(self.driver)
        result = b.test_map()
        self.assertNotEqual(0, result, msg="Data not present on map")

    def test_school_infra_options(self):
        b = School_infra_options(self.driver)
        res1,res2 = b.test_options()
        self.assertEqual(res1, "Report", msg="option is not available")
        self.assertEqual(res2, "Map based Report", msg="option is not available")

    def test_download(self):
        b = download_icon(self.driver)
        res = b.test_donwload()
        if "school-infra-map" in self.driver.current_url:
            print("School infrastructure map based report present")
        else:
            print("School infra map report is not exist")
        time.sleep(3)

    def test_click_on_home(self):
        b = click_on_home(self.driver)
        c1, c2, c3 = b.test_home()
        self.assertNotEqual(0, c1, msg="Records are not present on map ")
        self.assertNotEqual(0, c2, msg="Records are not present on map ")
        self.assertNotEqual(0, c3, msg="Records are not present on map ")

    def test_no_of_schools(self):
        b = Block_school_count(self.driver)
        r, r1, r2, r3 = b.test_counter()
        self.assertEqual(int(r), int(r1), msg="mis match found in no of school in block level")
        self.assertEqual(int(r), int(r2), msg="mis match found in no of school in cluster level")
        self.assertEqual(int(r), int(r3), msg="mis match found in no of school in school level")

    def test_dashboard(self):
        b = click_dashboard(self.driver)
        res = b.test_dashboard()
        self.assertEqual("cQube - Dashboard", res, msg="Dashboard is not exists!")

    def test_district_options(self):
        b = District_options(self.driver)
        res = b.test_options()
        self.assertNotEqual(0,res,msg="District names are not present")

    def test_clusterbtn(self):
        b =cluster_button(self.driver)
        self.assertNotEqual(0,b,msg="Records are not present on map ")

    def test_hyperlink(self):
        b = click_on_hyperlink(self.driver)
        res = b.test_link()
        if "school-infra-map" in self.driver.current_url:
            print("School infrastructure map based report present")
        else:
            print("School infra map report is not exist")
        time.sleep(3)


    def test_infrascore_click(self):
        b = select_infrascore_options(self.driver)
        res = b.test_infrascores()
        self.assertNotEqual(0, res, msg="lists are absent")

    def test_districtwise_csv(self):
        b = districtwise_csv(self.driver)
        res = b.test_districtwise()
        if "school-infra-map" in self.driver.current_url:
            print("School infrastructure map based report present")
        else:
            print("School infra map report is not exist")
        time.sleep(3)

    def test_mouseover_on_dots(self):
        b = mouseover(self.driver)
        res = b.test_mousehover()
        count = self.data.test_mouse_over()
        self.assertNotEqual(0,count,msg="markers not present in map ")

    def test_blockwise(self):
        b = select_blockwise(self.driver)
        res = b.test_dist_blocks()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()