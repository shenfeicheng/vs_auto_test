import allure
from page_object.page_store import PageStore
import pytest
from bage import read_excel

@allure.feature("门店")
class TestStore():
    # 前置条件
    @pytest.fixture(scope="module", autouse=True)
    def setup(self, driver):
        page = PageStore(driver)
        page.enter_store("自动化测试")

    @allure.story("新增门店成功")
    @pytest.mark.run(order=1)
    #@pytest.mark.skip
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_store.xlsx', '新增门店成功'))
    def test_add_store_sucess(self, driver,testdata):
        page=PageStore(driver)
        page.click_area("所有门店")
        page.click_btn_store_add()
        page.store_add(testdata['门店名字'],testdata['地址'],testdata['时区'],testdata['区域'],testdata['联系人'],
                       testdata['电子邮件'],testdata['电话'])
        assert page.table_add_search(testdata['门店名字'],testdata['区域'],testdata['地址'],testdata['联系人'],testdata['电话'])

    @allure.story("新增门店失败")
    @pytest.mark.run(order=2)
    #@pytest.mark.skip
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_store.xlsx', '新增门店失败'))
    def test_add_store_fail(self, driver, testdata):
        page = PageStore(driver)
        page.click_area("所有门店")
        page.click_btn_store_add()
        page.store_add(testdata['门店名字'], testdata['地址'], testdata['时区'], testdata['区域'], testdata['联系人'],
                       testdata['电子邮件'], testdata['电话'])
        assert page.add_fail_search()

    @allure.story("修改门店成功")
    @pytest.mark.run(order=3)
    #@pytest.mark.skip
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_store.xlsx', '修改门店成功'))
    def test_rework_store_sucess(self,driver,testdata):
        page=PageStore(driver)
        page.rework_store(testdata['修改前的门店名'],testdata['门店名字'],testdata['地址'],testdata['时区'],testdata['区域'],testdata['联系人'],
                       testdata['电子邮件'],testdata['电话'])
        assert page.table_add_search(testdata['门店名字'],testdata['区域'],testdata['地址'],testdata['联系人'],testdata['电话'])

    @allure.story("修改门店失败")
    @pytest.mark.run(order=4)
    #@pytest.mark.skip
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_store.xlsx', '修改门店失败'))
    def test_rework_store_fail(self, driver, testdata):
        page = PageStore(driver)
        page.click_area("所有门店")
        page.rework_store(testdata['修改前的门店名'], testdata['门店名字'], testdata['地址'], testdata['时区'],
                          testdata['区域'], testdata['联系人'],
                          testdata['电子邮件'], testdata['电话'])
        assert page.rework_fail_search()

    @allure.story("删除门店成功")
    @pytest.mark.run(order=5)
    #@pytest.mark.skip
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_store.xlsx', '删除门店成功'))
    def test_del_store_sucess(self,driver,testdata):
        page=PageStore(driver)
        page.click_area("所有门店")
        page.del_store(testdata['删除的门店名称'])
        assert page.table_del_search(testdata['删除的门店名称'])