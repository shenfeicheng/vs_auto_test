from selenium.webdriver.common.by import By
from bage.bage import Base
from page_element import element_map
from bage.mouse import Mouse
from time import sleep


class PageMap():
    def __init__(self,driver):
        self.page=Base(driver)
        self.mouse=Mouse(driver)

    #进入某个地图页面
    def enter_map(self, name):
        self.page.click_element((By.XPATH, f'//td/div/div/div[contains(text(), "{name}")]'))
        self.page.switch_url(-1)
        self.page.click_element(element_map.btn_left)

    #选择门店
    def click_store(self,name):
        self.page.click_element(element_map.drop_down)
        sleep(0.1)
        self.page.click_element((By.XPATH,f'//li[contains(text(), "{name}")]'))

    #新增地图图片
    def add_map(self,map_name,map_address):
        self.mouse.move_element(element_map.add_map)
        self.page.click_element(element_map.add_map)
        self.page.input_text(element_map.input_map_name,map_name)
        self.page.find_element(element_map.input_map).send_keys(map_address)
        # sleep(1)
        # img=self.page.get_element_attribute(element_map.img_map,'src')
        self.page.click_element(element_map.add_map_yes)
        # return img
    #获取地图名称
    def get_map_name(self):
        num=len(self.page.get_element((By.CLASS_NAME,'list-wrap'),'div'))
        return self.page.get_text((By.XPATH,f'//*[@id="app"]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[{num-1}]/p/span'))

    #获取地图图片
    def get_map_pic(self):
        num = len(self.page.get_element((By.CLASS_NAME, 'list-wrap'), 'div'))
        return self.page.get_element_attribute((By.XPATH, f'//*[@id="app"]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[{num-1}]/img'),'src')



