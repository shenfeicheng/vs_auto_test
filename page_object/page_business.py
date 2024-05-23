from selenium.webdriver.common.by import By
from bage.bage import Base
from page_element import element_business
from time import sleep

class PageBusiness():
    def __init__(self,driver):
        self.page=Base(driver)

    #新增商家输入方法
    def business_input(self,name,linkman,email,tel,logo,ant):
        self.page.click_element(element_business.btn_add)
        self.page.input_text(element_business.name,name)
        self.page.input_text(element_business.linkman,linkman)
        self.page.input_text(element_business.email,email)
        self.page.input_text(element_business.tel,tel)
        self.page.input_text(element_business.ant,ant)
        self.page.click_element(element_business.btn_add_true)

    #判断新增商家是否增加
    def business_add_sucess(self,text):
        sleep(1)
        return self.page.table_page_search(1, text, element_business.nextpage,element_business.table)

    #进入某个商家页面
    def enter_business(self,name):
        self.page.click_element((By.XPATH,f'//td/div/div/div[contains(text(), "{name}")]'))
        self.page.switch_url(-1)
        self.page.click_element(element_business.btn_left)

    #修改商家信息
    def rework_business(self,name,linkman,email,tel):
        self.page.input_text(element_business.rework_name,name)
        self.page.input_text(element_business.rework_linkman,linkman)
        self.page.input_text(element_business.rework_email,email)
        self.page.input_text(element_business.rework_tel,tel)
        self.page.click_element(element_business.btn_rework)
        self.page.switch_url(-2)

    def del_business(self):
        self.page.click_element(element_business.btn_del)
        self.page.click_element(element_business.btn_del_true)
        self.page.switch_url(0)

