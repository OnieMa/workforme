import configparser
import json
import logging
import sys
import time
from datetime import datetime

import redis
import requests
from tendo import singleton

red = redis.Redis(host='localhost', port=6379, db=0)  # 默认连接本地redis，端口为6379，使用数据库0



# 设置代理
proxies = {
    "http": "http://10.30.6.49:9090",
    "https": "http://10.30.6.49:9090"
}

_morning: str = ""
_afternoon: str = ""
_flag: bool = True
error_flag = 50
config = ""


def get_time():
    global _morning
    global _afternoon
    global _flag
    global error_flag

    # 创建Session对象
    session = requests.Session()

    # 设置代理
    session.proxies = proxies
    headers = {
        'Connection': "keep-alive",
        'Content-Type': "application/json",
    }

    resp = session.get("http://165.154.57.177:60020/getTime", headers=headers)
    if resp.status_code == 200:
        result = json.loads(resp.text)
        _flag = result["state"]
        if _morning != result["morning"][:-3] or _afternoon != result["afternoon"][:-3]:
            _afternoon = result["afternoon"][:-3]
            _morning = result["morning"][:-3]
            logging.info("修改了本地时间 ---> %s  %s  %s", _morning, _afternoon, _flag)
            send2dd(result)
    else:
        if error_flag == 50:
            logging.info("获取服务器时间失败... %s", resp)
        error_flag -= 1
        if error_flag == 0:
            logging.info("获取服务器时间失败...%s", resp)
            error_flag = 50

    session.close()


def send2dd(msg):
    # 创建Session对象
    session = requests.Session()

    # 设置代理
    session.proxies = proxies
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


def send2vx(msg):
    # 创建Session对象
    session = requests.Session()

    # 设置代理
    session.proxies = proxies
    # 请求的URL，WebHook地址
    web_url = "http://www.pushplus.plus/send"

    headers = {'Content-Type': 'application/json'}  # 定义数据类型
    # 定义要发送的数据
    data = {
        "token": "dd47b3ab3a6640948ddd7e88dc5c4856",
        "title": "daka",
        "content": msg

    }

    requests.packages.urllib3.disable_warnings()
    body = json.dumps(data).encode(encoding='utf-8')
    res = session.post(web_url, data=body, headers=headers, verify=False)  # 发送post请求
    text = res.text
    logging.info("call weixin result : %s", text)
    session.close()


def dry_and_stimulating():
    global config
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

    # res = connn.getresponse()
    # data = res.read()
    # result = json.loads(data.decode("utf-8"))
    # logging.info(result)
    # send2dd(result)


def get_config():
    global config
    config = configparser.ConfigParser()
    with open('config.ini', 'r', encoding='utf-8') as f:
        config.read_file(f)


def renewal_of_contract():
    while True:
        red.set("isRun", str(datetime.now()), ex=10, nx=True)
        time.sleep(5)


def start():
    while True:
        get_time()
        if _flag:
            if datetime.now().strftime("%Y-%m-%d %H:%M") == _morning or datetime.now().strftime(
                    "%Y-%m-%d %H:%M") == _afternoon:
                dry_and_stimulating()
                time.sleep(2)
                logging.info("关闭实例")
                exit(0)
            time.sleep(5)
        else:
            logging.info("The secret of happiness has been closed...")
            time.sleep(60)


if __name__ == '__main__':

    # 配置日志
    logging.basicConfig(
        level=logging.INFO,  # 设置日志级别为DEBUG，也可以是INFO, WARNING, ERROR, CRITICAL
        format='%(asctime)s - %(name)s - %(levelname)s    %(message)s',  # 日志格式
        datefmt='%Y-%m-%d %H:%M:%S',  # 时间格式
        filename='myapp.log',  # 日志文件名
        filemode='a',  # 文件模式，'a'代表追加，'w'代表覆盖
        encoding='utf-8'  # 设置文件编码为UTF-8
    )
    get_config()

    try:
        me = singleton.SingleInstance()
    except singleton.SingleInstanceException:
        sys.exit("Script is already running.")
    except Exception as e:
        sys.exit("Another error occurred: " + str(e))

    # 脚本的主要部分
    logging.info('-------------Script is not already running, continue execution------------------')

    # 使用redis判断是否在运行实例
    # isRun = red.get("isRun")
    #
    # if not isRun is None:
    #     exit(0)
    # else:
    #     red.set("isRun", str(datetime.now()), ex=10, nx=True)
    #     logging.info("开启实例....")

    # t = threading.Thread(target=renewal_of_contract)
    # t.daemon = True
    # t.start()

    start()
