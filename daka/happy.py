import configparser
import json
import logging
import random
import sys
import time
from datetime import datetime, timedelta
import requests

from tendo import singleton

morning = None
afternoon = None
evening = None
state = True


def generate_random_time(start_hour, start_minute, end_hour, end_minute):
    start_time = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
    end_time = datetime.now().replace(hour=end_hour, minute=end_minute, second=0, microsecond=0)
    random_time = start_time + timedelta(minutes=random.randint(0, (end_time - start_time).seconds // 60))
    return random_time.strftime("%H:%M")


def get_the_configuration_switch():
    global state
    session = requests.session()
    resp = session.get("http://165.154.57.177:60020/getState")
    if resp.status_code != 200:
        logging.info("Something went wrong, " + str(resp.status_code))
    else:
        status = resp.text
        if status == 'true':
            state = True
        else:
            state = False
    session.close()
    logging.info(datetime.now().strftime("%H:%M:%S") + "  The current status is:" + str(state))


def generate_operation_time():
    global morning
    global afternoon
    global evening

    morning = generate_random_time(8, 20, 8, 30)
    afternoon = generate_random_time(18, 00, 18, 30)
    evening = generate_random_time(21, 1, 21, 5)

    while True:
        if datetime.now().hour < 12 and morning < datetime.now().strftime("%H:%M"):
            hour = datetime.now().hour
            minute = datetime.now().minute
            morning = generate_random_time(hour, minute, hour, minute + 1)
            break
        if 14 < datetime.now().hour < 19 and afternoon < datetime.now().strftime("%H:%M"):
            hour = datetime.now().hour
            minute = datetime.now().minute
            afternoon = generate_random_time(hour, minute, hour, minute + 1)
            break
        if 21 <= datetime.now().hour and afternoon < datetime.now().strftime("%H:%M"):
            hour = datetime.now().hour
            minute = datetime.now().minute
            evening = generate_random_time(hour, minute, hour, minute + 1)
            break
        break
    logging.info("Get the status switch of the server ...")
    get_the_configuration_switch()


def dry_and_stimulating():
    config = configparser.ConfigParser()
    with open('config.ini', 'r', encoding='utf-8') as f:
        config.read_file(f)
    session = requests.Session()
    Authorization = config.get('headers', 'Authorization')
    X_Auth = config.get('headers', 'X_Auth')

    headers = {
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Authorization': Authorization,
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        'Content-Type': "application/json",
        'Pragma': "no-cache",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36",
        'X-Authorization': X_Auth
    }

    response = session.post("https://portal.dahuatech.com/portal-home/api/Attendance/Clock", headers=headers)
    data = response.json()
    logging.info(data)
    send2dd(json.loads(data['data']))
    session.close()


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


if __name__ == '__main__':
    try:
        me = singleton.SingleInstance()
    except singleton.SingleInstanceException:
        sys.exit("Script is already running.")
    except Exception as e:
        sys.exit("Another error occurred: " + str(e))

    # 配置日志
    logging.basicConfig(
        level='INFO',  # 设置日志级别为DEBUG，也可以是INFO, WARNING, ERROR, CRITICAL
        format='%(asctime)s - %(name)s - %(levelname)s    %(message)s',  # 日志格式
        datefmt='%Y-%m-%d %H:%M:%S',  # 时间格式
        filename='myapp.log',  # 日志文件名
        filemode='a',  # 文件模式，'a'代表追加，'w'代表覆盖
        encoding='utf-8'  # 设置文件编码为UTF-8
    )
    generate_operation_time()

    map = {"mor": morning, "aft": afternoon, "env": evening}
    send2dd(map)
    while True:
        if state:
            if datetime.now().strftime("%H:%M") == morning or datetime.now().strftime(
                    "%H:%M") == afternoon or evening == datetime.now().strftime("%H:%M"):
                logging.info("executed ... ")
                dry_and_stimulating()
                exit(0)
            time.sleep(5)
        else:
            time.sleep(60)
            get_the_configuration_switch()
