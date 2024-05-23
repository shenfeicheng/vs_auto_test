from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip

class Keybord:
    def __init__(self, driver):
        self.driver = driver
    #复制文本
    def copy_text(self,text):
        pyperclip.copy(text)

    #模拟ctrl+v
    def ctrl_v(self):
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    #模拟回车
    def enter(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

