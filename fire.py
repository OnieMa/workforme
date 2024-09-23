from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# 设置 Firefox 配置
options = Options()
options.set_preference("profile", r" C:\Users\354101\AppData\Roaming\Mozilla\Firefox\Profiles\jw7igr51.default-release")

# 启动 Firefox 浏览器并应用配置的 profile
driver = webdriver.Firefox(options=options)
# 关闭浏览器

# 将数据转换为 JSON 字符串
data_script = "const data = {}; for (const key in data) { window.localStorage.setItem(key, data[key]); }"

# 设置本地存储数据
driver.execute_script(data_script)


# 打开网页
# driver.get("https://work.dahuatech.com/#/home")
driver.get("https://www.baidu.com")

cks = driver.get_cookies()
print(cks)
print("\n=============\n")
local_storage = driver.execute_script("return window.localStorage;")
print(local_storage)





# driver.quit()
