from selenium.webdriver.common.by import By
nextpage=By.XPATH,'//li[@title="下一页"]'
firstpage=By.XPATH,'//li[@title="1"]'
btn_left=By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[5]/img'
#新增
btn_add=By.XPATH,'//button/span[contains(text(), "新增商家")]/parent::button'
name=By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div[2]/form/div[2]/div/div[1]/input'
linkman=By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div[2]/form/div[4]/div/div[1]/input'
email=By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div[2]/form/div[6]/div/div[1]/input'
tel=By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div[2]/form/div[8]/div/div/input'
logo=By.XPATH,'/html/body/div[4]/div[2]/div/div/div/div[2]/form/div[10]/div/div/div/img'
ant=By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div[2]/form/div[11]/div[4]/div/div/div[2]/input'
btn_add_true=By.XPATH,'//button/span[text()="确定"]'
table=By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/table'
#编辑
rework_name=By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]/div/form/div[2]/div/div/input'
rework_linkman=By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]/div/form/div[4]/div/div/input'
rework_email=By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]/div/form/div[6]/div/div/input'
rework_tel=By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]/div/form/div[8]/div/div/input'
btn_rework=By.XPATH,'//button/span[text()="应用"]'
#删除
btn_del=By.XPATH,'//button/span[text()="删除"]'
btn_del_true=By.XPATH,'//button/span[text()="是"]'