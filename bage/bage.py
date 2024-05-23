from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    #初始化对象
    def __init__(self, driver):
        self.driver = driver

    # 获取浏览器对象
    def open_url(self, url):
        self.driver.get(url)

    #切换窗口
    def switch_url(self,num):
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[num])

    #查找单个页面元素
    def find_element(self, loc, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(loc))
            return element
        except TimeoutException:
            print(f"Timeout waiting for element with locator: {loc}")
            return False
        except Exception as e:
            print(f"Error finding element: {e}")
            return None

    #查找多个页面元素
    def find_elements(self, loc, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(loc))
            return elements
        except TimeoutException:
            print(f"Timeout waiting for elements with locator: {loc}")
            return False
        except Exception as e:
            print(f"Error finding elements: {e}")
            return None

    #判断页面元素是否存在
    def is_element_not_present(self, loc, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(loc))
            return True
        except TimeoutException:
            print(f"Timeout waiting for element with locator: {loc}")
            return False

    #点击方法
    def click_element(self, loc):
        element = self.find_element(loc)
        if element:
            element.click()

    #输入方法
    def input_text(self,loc,text):
        element = self.find_element(loc)
        element.clear()
        if element:
            element.send_keys(text)

    #输入多个方法
    def input_texts(self, loc, texts):
        elements = self.find_elements(loc)
        if len(elements) != len(texts):
            raise ValueError("The number of elements and texts must be the same.")
        for element, text in zip(elements, texts):
            element.clear()
            element.send_keys(text)

    #获取文本
    def get_text(self, loc):
        element = self.find_element(loc)
        if element:
            return element.text
        return None

    # 获取整数文本
    def get_int_text(self, loc):
        element = self.find_element(loc)
        if element:
            return int(element.text)
        return None

    #获取表格数据
    def get_element(self,loc,value):
        element=self.find_element(loc)
        if element:
            rows = element.find_elements(By.TAG_NAME, value)
            return rows
        return None

    # 获取表格行数据
    def get_table_rows(self,loc):
        return self.get_element(loc, "tr")

    #获取页面元素的某个属性
    def get_element_attribute(self,loc,attribute):
        return self.find_element(loc).get_attribute(attribute)

    #分割字符串
    def split_string(self,combined_string, delimiter):
        return combined_string.split(delimiter)

    # 判断下一页按钮是否可用
    def next_page_disable(self,next_page):
        li_element = self.find_element(next_page)
        if li_element is None:
            raise ValueError("未找到分页控件的'下一页'按钮")
        if 'ivu-page-disabled' in li_element.get_attribute('class'):
            return True
        else:
            # 检查'disabled'属性是否包含'disabled'字符串
            return False

    # 表格分页查询
    def table_page_search(self,first_num,search_data,next_page,table_loc):
        found_match = False
        rows = self.get_table_rows(table_loc)
        for row in rows:
            row_data = row.find_elements(By.TAG_NAME, 'td')[first_num:len(search_data)+first_num]
            if(len(row_data)==len(search_data)):
                if all(item.text == var for item, var in zip(row_data, search_data)):
                    found_match = True
                    break
            else:
                raise ValueError("列不相等")
        if not found_match and not self.next_page_disable(next_page):
            self.click_element(next_page)
            self.table_page_search(first_num, search_data, next_page, table_loc)
            # 再次检查'下一页'按钮是否被禁用
        else:
            return found_match
                # 如果找到了匹配项或者'下一页'按钮被禁用，则退出循环

    # 表格模糊分页查询
    def table_page_in_search(self,first_num,search_data,next_page,table_loc):
        rows = self.get_table_rows(table_loc)[:5]
        found_match=False
        for row in rows:
            row_data = row.find_elements(By.TAG_NAME, 'td')[first_num:len(search_data)+first_num]
            # 逐个检查搜索参数是否模糊匹配行数据
            if all(param.lower() in cell.text.lower() for param, cell in zip(search_data, row_data)):
                found_match=True
            else:
                return False
        # 检查'下一页'按钮是否被禁用，如果没有被禁用，则翻到下一页
        if not self.next_page_disable(next_page):
            self.click_element(next_page)
            self.table_page_in_search(first_num,search_data,next_page,table_loc)
        return found_match
            # '下一页'按钮被禁用，跳出循环
