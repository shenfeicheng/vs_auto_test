from selenium.webdriver.common.by import By
from bage.bage import Base
from page_element import element_store
from bage.mouse import Mouse
from time import sleep

class PageStore():
    def __init__(self,driver):
        self.page=Base(driver)
        self.mouse=Mouse(driver)

    # 进入某个门店页面
    def enter_store(self, name):
        self.page.click_element((By.XPATH, f'//td/div/div/div[contains(text(), "{name}")]'))
        self.page.switch_url(-1)
        self.page.click_element(element_store.btn_left)
        sleep(1)

    #新增区域方法
    def area_add(self,name):
        self.page.click_element(element_store.btn_area_add)
        self.page.input_text(element_store.input_area,name)
        self.page.click_element(element_store.area_add_yes)
        sleep(1)

    #获取新增区域名称
    def get_add_area_name(self):
        num=len(self.page.find_elements((By.CLASS_NAME,'region-menu')))
        return self.page.get_text((By.XPATH,f'//*[@id="app"]/div/div[2]/div/div/div/div[2]/div[1]/div/div[{num}]/div/span'))

    # 点击对应区域
    def click_area(self, name):
        self.page.click_element((By.XPATH, f"//span[contains(text(), '{name}') and @class='active-cell-label']"))

    #修改区域名称
    def rework_area_name(self,last_name,new_name):
        self.click_area(last_name)
        self.mouse.mouse_hover(element_store.area_more)
        sleep(1)
        self.page.click_element((By.XPATH,"//div[contains(@x-placement,'left-start')]/ul/li[1]/div"))
        self.page.input_text(element_store.input_area, new_name)
        self.page.click_element(element_store.area_add_yes)
        sleep(1)

    #获取修改后的区域名称
    def get_rework_area_name(self,text):
        num=By.XPATH,f'//span[@class="active-cell-label" and text()="{text}"]'
        return self.page.is_element_not_present(num)

    # 删除区域方法
    def del_area(self,name):
        self.click_area(name)
        row=len(self.page.get_table_rows(element_store.table))
        self.mouse.mouse_hover(element_store.area_more)
        sleep(1)
        self.mouse.mouse_click((By.XPATH, "//div[contains(@x-placement,'left-start')]/ul/li[2]/div"))
        self.page.click_element(element_store.btn_store_del_yes)
        sleep(1)
        return row

    #点击新增门店按钮
    def click_btn_store_add(self):
        self.page.click_element(element_store.btn_store_add)
        sleep(1)

    #新增门店输入
    def store_add(self,name,address,timezone,area,linkman,email,phone):
        self.page.input_text(element_store.input_store_name,name)
        self.page.input_text(element_store.input_store_address,address)
        sleep(0.5)
        self.page.click_element((By.XPATH,'//*[@id="store_map"]/div[3]/div[2]/div[3]/div[1]/ul/li[1]'))
        self.page.input_text(element_store.input_store_linkman,linkman)
        self.page.input_text(element_store.input_store_email,email)
        self.page.input_text(element_store.input_store_phone,phone)
        self.page.click_element(element_store.area_click)
        sleep(0.5)
        self.page.click_element((By.XPATH, f'//li[contains(., "{area}")]'))
        self.page.click_element(element_store.btn_store_add_yes)
        sleep(1)

    #新增门店验证方法
    def table_add_search(self,name,area,adddress,linkman,phone):
        self.click_area(area) #点击门店对应的区域
        text=name,area,adddress,linkman,phone
        sleep(1)
        return self.page.table_page_search(0,text,element_store.nextpage,element_store.table)

    # 新增门店失败验证方法
    def add_fail_search(self):
        if self.page.is_element_not_present((By.CLASS_NAME,'ivu-modal-body')):
            self.page.click_element(element_store.btn_store_add_no)
            return True
        return False

    #修改门店方法
    def rework_store(self,last_name,new_name,address,timezone,area,linkman,email,phone):
        self.page.click_element((By.XPATH,f'//td/div/span[contains(text(), "{last_name}")]'))
        sleep(1)
        self.store_add(new_name,address,timezone,area,linkman,email,phone)

    #修改门店失败验证方法
    def rework_fail_search(self):
        if self.page.is_element_not_present((By.CLASS_NAME, 'content-title')):
            self.page.click_element(element_store.btn_back)
            return True
        return False

    #删除门店方法
    def del_store(self,name):
        self.page.click_element((By.XPATH, f'//td/div/span[contains(text(), "{name}")]'))
        self.mouse.move_element(element_store.btn_store_del)
        self.page.click_element(element_store.btn_store_del)
        self.page.click_element(element_store.btn_store_del_yes)
        sleep(1)

    #删除门店验证方法
    def table_del_search(self,name):
        rows = self.page.get_table_rows(element_store.table)
        found_match = True
        for row in rows:
            row_data = row.find_elements(By.TAG_NAME, 'td')[0]
            # 逐个检查搜索参数是否模糊匹配行数据
            if name==row_data.text:
                return False
        # 检查'下一页'按钮是否被禁用，如果没有被禁用，则翻到下一页
        if not self.page.next_page_disable(element_store.nextpage):
            self.page.click_element(element_store.nextpage)
            self.table_del_search(name)
        self.page.click_element(element_store.firstpage)
        return found_match
