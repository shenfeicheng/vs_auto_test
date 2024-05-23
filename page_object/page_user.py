from selenium.webdriver.common.by import By
from bage.bage import Base
from page_element import element_user
from bage.mouse import Mouse
from time import sleep

class PageUser():
    def __init__(self,driver):
        self.page=Base(driver)
        self.mouse=Mouse(driver)

    #进入某个用户模块
    def enter_user(self, name):
        self.page.click_element((By.XPATH, f'//td/div/div/div[contains(text(), "{name}")]'))
        self.page.switch_url(-1)
        self.page.click_element(element_user.btn_left)
    #点击新增用户按钮
    def click_btn_user_add(self):
        self.page.click_element(element_user.btn_add_user)

    #输入用户信息
    def input_user(self,name,email,phone,role,scope):
        self.page.input_text(element_user.user_name,name)
        self.page.input_text(element_user.email,email)
        #self.page.input_text(element_user.phone,phone)
        self.page.click_element((By.XPATH,f'//label[contains(text(), "{role}")]/span/input[@type="radio"]'))
        self.page.click_element(element_user.drop_down)
        sleep(0.5)
        new_scope=self.page.split_string(scope,('/'))
        if len(new_scope)>0:
            i=0
            while i<len(new_scope):
                self.mouse.move_element((By.XPATH,f'//span[contains(@class, "ivu-tree-title") and text()="{new_scope[i]}"]'))
                self.page.click_element((By.XPATH,f'//span[contains(@class, "ivu-tree-title") and text()="{new_scope[i]}"]'))
                i+=1
        self.page.click_element(element_user.btn_add_user_yes)

    #验证范围
    def add_scope_search(self,scope):
        new_scope = self.page.split_string(scope, ('/'))
        num = len(self.page.get_element((By.XPATH, '//table/tbody/tr[1]/td[6]/div/div/div/div'), 'span'))
        i=1
        while i<=num:
            if new_scope[i-1]==self.page.get_text((By.XPATH, f'//table/tbody/tr[1]/td[6]/div/div/div/div/span[{i}]')):i+=1
            else:return False
        return True
    #新增用户验证
    def add_table_search(self,name,email,phone,role):
        text = name, email, phone, role
        sleep(15)
        return self.page.table_page_search(1,text,element_user.nextpage,element_user.table)


