from selenium.webdriver.common.by import By
nextpage=By.XPATH,'//li[@title="下一页"]'
firstpage=By.XPATH,'//li[@title="1"]'
btn_left=By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[6]/img'
table=By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/table'
#区域
btn_area_add=By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div/div[2]/div[1]/button'
input_area=By.XPATH,'//div[contains(@class, "region-input-box")]/div[contains(@class, "region-input")]/input'
area_add_yes=By.XPATH,"//i[contains(concat(' ', normalize-space(@style), ' '), ' font-size: 20px; ')]"
area_more=By.XPATH,"//div[contains(@class,'menu-cell region-cell cursor-pointer active-cell')]/div/div/div/img"
#门店
btn_store_add=By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div/div[1]/div/button'
input_store_name=By.XPATH,"//div[contains(@class,'form-left')]/div[3]/div/div[1]/input"
input_store_address=By.XPATH,'//*[@id="store_map"]/div[3]/div[2]/div[3]/input'
input_store_timezone=By.XPATH,"//div[contains(@class,'form-left')]/div[7]/div/div/div/div/input"
area_click=By.XPATH,"//div[contains(@class,'form-left')]/div[9]/div/div/div/div"
input_store_linkman=By.XPATH,"//div[contains(@class,'form-right')]/div[3]/div/div/input"
input_store_email=By.XPATH,"//div[contains(@class,'form-right')]/div[5]/div/div/input"
input_store_phone=By.XPATH,"//div[contains(@class,'form-right')]/div[7]/div/div/input"
btn_store_add_yes=By.XPATH,"//div[contains(@class,'footer')]/button[1]"
btn_store_del=By.XPATH,"//div[contains(@class,'footer')]/button[3]"
btn_store_del_yes=By.XPATH,"//div[contains(@class,'ivu-modal-confirm-footer')]/button[1]"