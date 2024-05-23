import allure
from page_object.page_user import PageUser
import pytest
from bage import read_excel

@allure.feature("用户")
class TestUser():
    # 前置条件
    @pytest.fixture(scope="module", autouse=True)
    def setup(self, driver):
        page = PageUser(driver)
        page.enter_user("自动化测试")
    @allure.story("新增用户成功")
    @pytest.mark.run(order=1)
    #@pytest.mark.skip
    @pytest.mark.parametrize("testdata", read_excel.load_testdata('../../data/data_user.xlsx', '新增用户成功'))
    def test_add_user_success(self, driver, testdata):
        page = PageUser(driver)
        page.click_btn_user_add()
        page.input_user(testdata['用户名称'],testdata['电子邮件'],testdata['电话号码'],testdata['角色'],testdata['管理范围'])
        assert page.add_table_search(testdata['用户名称'],testdata['电子邮件'],testdata['电话号码'],testdata['角色'],testdata['管理范围'])