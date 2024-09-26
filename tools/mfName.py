import os
import sys
from datetime import datetime

# 指定文件夹路径
args = sys.argv

folder_path = args[1]
if folder_path is None:
	print("参数错误")
	sys.exit(0)

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
	# 检查文件名是否为纯时间戳（假设时间戳命名的文件为整数形式）
	filename = filename.split(".")[0]
	print(filename)
	if filename.isdigit():
		# 获取时间戳并转换为秒（有些时间戳是以毫秒为单位的，如果是这样，取消下一行的注释）
		# timestamp = int(filename)
		timestamp = int(filename) / 1000  # 如果时间戳是毫秒级别，使用这一行

		# 将时间戳转换为中国时间（CST）
		dt = datetime.fromtimestamp(timestamp)
		china_time = dt.strftime('%F_%H_%M_%S')

		# 获取文件扩展名（假设原文件有扩展名，如果没有扩展名，忽略此行）
		_, ext = os.path.splitext(filename)

		# 生成新的文件名（包含扩展名）
		new_filename = china_time + ext

		# 构造旧文件和新文件的完整路径
		old_file_path = os.path.join(folder_path, filename + '.log')
		new_file_path = os.path.join(folder_path, new_filename + '.log')

		# 重命名文件
		os.rename(old_file_path, new_file_path)
		print(f'{filename} -> {new_filename}')
