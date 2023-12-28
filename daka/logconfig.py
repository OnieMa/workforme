import logging
import sys

from tendo import singleton


class LogConfig:
    # 配置日志
    # 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # 设置日志级别

    # 定义日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # 创建一个文件处理器，并设置级别和格式
    file_handler = logging.FileHandler('new.log', mode='a', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # 创建一个流处理器，用于输出到控制台，并设置级别和格式
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    # 将处理器添加到logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    try:
        me = singleton.SingleInstance()
    except singleton.SingleInstanceException:
        sys.exit("Script is already running.")
    except Exception as e:
        sys.exit("Another error occurred: " + str(e))

    # 脚本的主要部分
    logging.info('-------------Script is not already running, continue execution------------------')
