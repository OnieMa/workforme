import json


def get_json_type(b, k, value):
	"""判断字段的类型并返回对应的字符串表示"""
	if value is None:
		b[k] = "null"
	elif isinstance(value, bool):
		b[k] = "boolean"
	elif isinstance(value, (int, float)):
		b[k] = "number"
	elif isinstance(value, str):
		b[k] = "string"
	elif isinstance(value, dict):
		setValue2Type(b[k])
	elif isinstance(value, list):
		setValue2Type(b[k][0])


def setValue2Type(a):
	keys = set(a.keys())
	print()
	for k in keys:
		get_json_type(a, k, a[k])

	return a


# 读取json文件
def load_json(file_path):
	with open(file_path, 'r', encoding='utf-8') as f:
		return json.load(f)


# 保存json文件
def save_json(file_path, data):
	with open(file_path, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)


# 示例使用
a = load_json('a.json')
b = load_json('b.json')

save_json('sorted_a.json', setValue2Type(a))
save_json('sorted_b.json', setValue2Type(b))
