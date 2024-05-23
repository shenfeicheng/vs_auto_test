import allure
from page_object.page_map import PageMap
import pytest
from bage import read_excel

@allure.feature("地图")
class TestMap():
    # 前置条件
    @pytest.fixture(scope="module", autouse=True)
    def setup(self, driver):
        page = PageMap(driver)
        page.enter_map("自动化测试")
    @allure.story("新增地图成功")
    @pytest.mark.run(order=1)
    #@pytest.mark.skip
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_map.xlsx', '新增地图成功'))
    def test_add_map_success(self, driver, testdata):
        page = PageMap(driver)
        page.click_store(testdata['门店名称'])
        img=page.add_map(testdata['地图名称'],testdata['地图地址'])
        #assert img==page.get_map_pic()
        assert page.get_map_name()==testdata['地图名称']
