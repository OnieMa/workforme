import requests

# 配置代理
proxies = {
    "http": "http://10.30.6.49:9090",
    "https": "http://10.30.6.49:9090"
}

# SSE接口的URL
sse_url = 'http://165.154.57.177:60020/sse'

# 创建一个Session对象
session = requests.Session()

# 设置代理
session.proxies = proxies

# 发起一个GET请求，stream=True意味着请求将以流的方式接收数据
response = session.get(sse_url, stream=True)

# 处理SSE事件
try:
    for line in response.iter_lines():
        # 过滤掉空行
        if line:
            decoded_line = line.decode('utf-8')
            print(f"Received line: {decoded_line}")
            # TODO: 在这里添加你的处理逻辑
except KeyboardInterrupt:
    print("Interrupted by user")

# 关闭连接
session.close()
