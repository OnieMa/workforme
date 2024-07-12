import json
import logging
import random
import sched
import sys
import time
import pytz
from datetime import datetime, timedelta

import requests

addr = 'http://localhost:60090'

# 配置日志
logging.basicConfig(
	level='INFO',  # 设置日志级别为DEBUG，也可以是INFO, WARNING, ERROR, CRITICAL
	format='%(asctime)s - %(name)s - %(levelname)s    %(message)s',  # 日志格式
	datefmt='%Y-%m-%d %H:%M:%S',  # 时间格式
	filename='/opt/daka/server.log',  # 日志文件名
	filemode='a',  # 文件模式，'a'代表追加，'w'代表覆盖
	encoding='utf-8'  # 设置文件编码为UTF-8
)


def send2dd(msg):
	# 创建Session对象
	session = requests.Session()

	# 请求的URL，WebHook地址
	web_url = "https://oapi.dingtalk.com/robot/send?access_token" \
	          "=d6c6970faefd08f8a674eb3c0e6312121d80dd88f5179c144d79a30633d4d029 "

	headers = {'Content-Type': 'application/json'}  # 定义数据类型
	# 定义要发送的数据
	# "at": {"atMobiles": "['"+ mobile + "']"
	data = {
		"msgtype": "text",
		"text": {"content": msg},
		"isAtAll": True}
	requests.packages.urllib3.disable_warnings()
	res = session.post(web_url, data=json.dumps(data), headers=headers, verify=False)  # 发送post请求
	text = res.text
	logging.info("call dingding result : %s", json.loads(text))
	session.close()


def visit_taiwan():
	session = requests.session()
	resp = session.get(addr + "/do")
	if resp.status_code != 200:
		logging.info("Something went wrong, " + str(resp.status_code))
		logging.info(resp.text)
		send2dd("py call java  Something went wrong...")
	elif resp.text is None:
		logging.info("The response data is empty")
		
	else:
		session.close()
		logging.info(datetime.now().strftime("%H:%M:%S") + "  The current status is:" + str(resp.text))


def health_examination():
	session = requests.session()
	resp = session.get(addr + "/state")
	if resp.status_code != 200 or int(resp.text) != 0:
		logging.info("Something went wrong, " + str(resp.status_code) + " resp:  " + resp.text)
		send2dd("   SERVICE IS STOP  ")
		sys.exit(0)
	logging.info("The system is starting. . .")
	session.close()


if __name__ == '__main__':
	health_examination()

	# 创建一个调度器实例
	scheduler = sched.scheduler(time.time, time.sleep)

	# 生成一个随机秒数
	random_second = random.randint(10, 600)

	# 在起始时间上加上随机秒数得到最终时间
	random_time = datetime.now(pytz.utc) + timedelta(seconds=random_second)
	# 转换为北京时间
	beijing_timezone = pytz.timezone("Asia/Shanghai")
	beijing_time = random_time.astimezone(beijing_timezone)

	# 格式化输出时间
	logging.info("will be " + str(random_second) + " seconds later: " + beijing_time.strftime('%Y-%m-%d %H:%M:%S'))

	# 使用调度器在指定时间执行任务
	scheduler.enter(delay=random_second, priority=1, action=visit_taiwan)
	scheduler.run()
	print("\n")
	print("\n")
