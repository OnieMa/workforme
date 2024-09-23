import subprocess

import pyautogui
from selenium import webdriver

# 定义Chrome浏览器的路径
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# 打开Chrome并导航到指定的网址
Chrome = subprocess.Popen([chrome_path, 'https://work.dahuatech.com/#/home'])

# 给软件一些时间来启动
pyautogui.sleep(3)
# 使用快捷键Alt + Space然后按x来最大化窗口
pyautogui.hotkey('win', 'up')

pyautogui.sleep(2)
# 移动鼠标
pyautogui.moveTo(1648, 163)
# 点击鼠标
pyautogui.click()
pyautogui.sleep(3)

pyautogui.hotkey('alt', 'F4')


# # 移动鼠标
# pyautogui.moveTo(1885, 6)
# # 点击鼠标
# pyautogui.click()
#
# sys.exit(0)
