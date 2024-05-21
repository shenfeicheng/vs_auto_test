from bage.bage import Base
from selenium.webdriver.common.action_chains import ActionChains

class Mouse:
    def __init__(self, driver):
        self.driver = driver
        self.base=Base(driver)
    #鼠标悬停
    def mouse_hover(self,loc):
        ActionChains(self.driver).move_to_element(self.base.find_element(loc)).perform()

    #移动到元素
    def move_element(self,loc):
        ActionChains(self.driver).scroll_to_element(self.base.find_element(loc)).perform()

    #点击元素
    def mouse_click(self,loc):
        ActionChains(self.driver).move_to_element(self.base.find_element(loc)).click().perform()