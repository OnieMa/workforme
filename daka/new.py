import configparser
import logging
import sys
import time
import requests
import json

from datetime import datetime
import logconfig

file_config = ''
_morning = ''
_afternoon = ''
_flag = True
error_flag = 50


class MyConfig:
    global file_config
    file_config = configparser.ConfigParser()
    with open('config.ini', 'r', encoding='utf-8') as f:
        file_config.read_file(f)
    logging.info('finished loading configuration file')


class MyProxy:
    session = requests.Session()

    # 在类的实例失效后应当释放连接
    def __del__(self):
        self.session.close()

    def __init__(self):
        # 设置代理
        proxies = {
            "http": "http://10.30.6.49:9090",
            "https": "http://10.30.6.49:9090"
        }
        # 设置代理
        self.session.proxies = proxies
        logging.info("proxy over ...")

    def get_session(self):
        return self.session

    def send2dd(self, msg: str):
        # 请求的URL，WebHook地址
        web_url = "https://oapi.dingtalk.com/robot/send?access_token" \
                  "=d6c6970faefd08f8a674eb3c0e6312121d80dd88f5179c144d79a30633d4d029 "

        headers = {'Content-Type': 'application/json'}  # 定义数据类型
        # 定义要发送的数据
        data = {
            "msgtype": "text",
            "text": {"content": msg},
            "isAtAll": True}
        requests.packages.urllib3.disable_warnings()
        res = self.session.post(web_url, data=json.dumps(data), headers=headers, verify=False)  # 发送post请求
        text = res.text
        logging.info("call dingding result : %s", json.loads(text))

    def get_time(self):
        global _morning
        global _afternoon
        global _flag
        global error_flag

        # 创建Session对象
        session = self.session

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
                self.send2dd(result)
        else:
            if error_flag == 50:
                logging.error("获取服务器时间失败... %s", resp)
            error_flag -= 1
            if error_flag == 0:
                logging.error("获取服务器时间失败...%s", resp)
                error_flag = 50


def dry_and_stimulating():
    global file_config
    pro = MyProxy()
    config = file_config
    session = pro.get_session()

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

    response = session.post("https://work.dahuatech.com/portal-home/api/Attendance/Clock", headers=headers,
                            verify=False)
    data = response.json()
    logging.info(data)
    pro.send2dd(data)


def start():
    global _flag
    proxy = MyProxy()
    while True:
        proxy.get_time()
        if _flag:
            if datetime.now().strftime("%Y-%m-%d %H:%M") == _morning or datetime.now().strftime(
                    "%Y-%m-%d %H:%M") == _afternoon:
                dry_and_stimulating()
                time.sleep(2)
                logging.info("关闭实例")
                sys.exit(0)  # 使用 sys.exit()

            time.sleep(3)

        else:
            logging.info("The secret of happiness has been closed...")
            time.sleep(60)


if __name__ == '__main__':
    start()
