import pytest
from selenium import webdriver
from page_element import element_login
from bage.bage import Base
from time import sleep
#初始化浏览器对象
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    login=Base(driver)
    login.open_url("http://192.168.4.21:8995/login")
    sleep(1)
    login.input_text(element_login.login_email,"shenfeicheng@century-cn.com")
    login.input_text(element_login.login_password,"sfc20011224")
    login.click_element(element_login.login_btn)
    yield driver
    driver.quit()