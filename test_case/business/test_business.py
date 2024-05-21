import allure
from page_object.page_business import PageBusiness
import pytest
from bage import read_excel

@allure.feature("商家")
class TestBusiness():
    @allure.story("新增商家成功")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_business.xlsx', '新增商家成功'))
    def test_add_success(self,driver,testdata):
        page=PageBusiness(driver)
        page.business_input(testdata['商家名称'],testdata['联系人'],testdata['电子邮件'],testdata['电话号码'],testdata['商标'],testdata['天线限制'])
        text = testdata['商家名称'],testdata['联系人'],testdata['电子邮件'],testdata['电话号码']
        assert page.business_add_sucess(text)

    @allure.story("修改商家成功")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_business.xlsx', '修改商家成功'))
    def test_rework_success(self,driver,testdata):
        page = PageBusiness(driver)
        page.enter_business(testdata['修改前名称'])
        page.rework_business(testdata['商家名称'],testdata['联系人'],testdata['电子邮件'],testdata['电话号码'])
        driver.refresh()
        text = testdata['商家名称'], testdata['联系人'], testdata['电子邮件'], testdata['电话号码']
        assert page.business_add_sucess(text)

    @allure.story("删除商家成功")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_business.xlsx', '删除商家成功'))
    def test_del_success(self, driver, testdata):
        page = PageBusiness(driver)
        page.enter_business(testdata['删除的商家'])
        page.del_business()
        driver.refresh()
        assert not page.business_add_sucess(testdata['删除的商家'])