from selenium.webdriver.common.by import By
nextpage=By.XPATH,'//li[@title="下一页"]'
firstpage=By.XPATH,'//li[@title="1"]'
btn_left=By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[8]/img'
table=By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/table'

btn_add_user=By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div/div[1]/div/button[2]'
user_name=By.XPATH,"//div[contains(@class,'ivu-modal-body')]/form/div[2]/div[1]/div[2]/div/div[1]/input"
email=By.XPATH,"//div[contains(@class,'ivu-modal-body')]/form/div[2]/div[2]/div[2]/div/div[1]/input"
#phone=By.XPATH,"//div[contains(@class,'ivu-modal-body')]/form/div[4]/div/div/input"
drop_down=By.XPATH,"//div[contains(@class,'ivu-modal-body')]/form/div[6]/div[2]/div/div[1]/ul/li/span[1]/i"
btn_add_user_yes=By.XPATH,'//button[span="确定"]'
