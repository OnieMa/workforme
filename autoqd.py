import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# from seleniumwire import webdriver

os.system('taskkill /f /im %s' % 'chrome.exe')

# # 添加保持登录的数据路径：安装目录一般在C:\Users\****\AppData\Local\Google\Chrome\User Data
user_data_dir = r'C:\Users\354101\AppData\Local\Google\Chrome\User Data'
# # 这是一个选项类
user_option = webdriver.ChromeOptions()
# # 添加浏览器用户数据
user_option.add_argument(f'--user-data-dir={user_data_dir}')
# # 创建Service对象并指定WebDriver的路径
service = Service(r'D:\environment\chromedriver-win64\chromedriver.exe')

# 实例化浏览器（带上用户数据）
driver = webdriver.Chrome(service=service, options=user_option)
# driver = webdriver.Chrome(service=service)

# "C:\Program Files\Mozilla Firefox\firefox.exe"


time.sleep(3)
# 打开网页
driver.get('https://work.dahuatech.com/#/home')
driver.refresh()
first_tab_handle = driver.current_window_handle
time.sleep(2)

# driver.find_element(by=By.XPATH,
#                     value='/html/body/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/section/span[1]').click()
time.sleep(2)

# 关闭浏览器
driver.quit()
