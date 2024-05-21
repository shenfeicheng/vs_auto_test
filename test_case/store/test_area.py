import allure
from page_object.page_store import PageStore
import pytest
from bage import read_excel

@allure.feature("区域")
class TestArea():
    # 前置条件
    @pytest.fixture(scope="module", autouse=True)
    def setup(self, driver):
        page = PageStore(driver)
        page.enter_store("自动化测试")

    @allure.story("新增区域成功")
    @pytest.mark.run(order=1)
    #@pytest.mark.skip
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_store.xlsx', '新增区域成功'))
    def test_add_success(self, driver, testdata):
        page = PageStore(driver)
        page.area_add(testdata['区域名称'])
        assert page.get_area_name() == testdata['区域名称']

    @allure.story("修改区域成功")
    @pytest.mark.run(order=2)
    #@pytest.mark.skip
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_store.xlsx', '修改区域成功'))
    def test_rework_sucess(self,driver,testdata):
        page=PageStore(driver)
        page.rework_area_name(testdata['要修改的区域名称'],testdata['修改后的区域名称'])
        assert page.get_rework_area_name(testdata['修改后的区域名称'])

    @allure.story("删除区域失败")
    @pytest.mark.run(order=5)
    #@pytest.mark.skip
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_store.xlsx', '删除区域失败'))
    def test_del_fail(self,driver,testdata):
        page=PageStore(driver)
        row=page.del_area(testdata['要删除的区域'])
        if row>0:assert page.get_rework_area_name(testdata['要删除的区域'])

    @allure.story("删除区域成功")
    @pytest.mark.run(order=3)
    #@pytest.mark.skip
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_store.xlsx', '删除区域成功'))
    def test_del_sucess(self, driver, testdata):
        page = PageStore(driver)
        row = page.del_area(testdata['要删除的区域'])
        if row == 0: assert not page.get_rework_area_name(testdata['要删除的区域'])