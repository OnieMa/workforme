import subprocess

import pyautogui
from selenium import webdriver

# 定义Chrome浏览器的路径
chrome_path = r"C:\Users\354101\AppData\Local\Google\Chrome\Application\chrome.exe"

# 打开Chrome并导航到指定的网址
subprocess.Popen([chrome_path, 'https://work.dahuatech.com/#/home'])

# 给软件一些时间来启动
pyautogui.sleep(2)
# 使用快捷键Alt + Space然后按x来最大化窗口
pyautogui.hotkey('win', 'up')
pyautogui.hotkey('F12')

pyautogui.sleep(2)
# 移动鼠标
pyautogui.moveTo(1642, 143)
# 点击鼠标
pyautogui.click()
pyautogui.sleep(2)
pyautogui.hotkey('ctrl', '2')
pyautogui.sleep(1)
pyautogui.moveTo(110, 453)
pyautogui.click()

# # 移动鼠标
# pyautogui.moveTo(1885, 6)
# # 点击鼠标
# pyautogui.click()
#
# sys.exit(0)
