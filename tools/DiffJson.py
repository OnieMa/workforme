import json


def get_json_type(value):
	"""判断字段的类型并返回对应的字符串表示"""
	if value is None:
		return "null"
	elif isinstance(value, bool):
		return "boolean"
	elif isinstance(value, (int, float)):
		return "number"
	elif isinstance(value, str):
		return "string"
	elif isinstance(value, list):
		return "array"
	elif isinstance(value, dict):
		return "object"
	return "unknown"


def sort_and_replace_types(a, b):
	if isinstance(a, dict) and isinstance(b, dict):
		# 找到相同的字段，并排序
		common_keys = sorted(set(a.keys()) & set(b.keys()))

		# 将不同的字段分别排序
		a_unique_keys = sorted(set(a.keys()) - set(b.keys()))
		b_unique_keys = sorted(set(b.keys()) - set(a.keys()))

		# 分别按照字段排序并替换为字段类型
		sorted_a = {k: sort_and_replace_types(a[k], b.get(k)) if k in b else get_json_type(a[k]) for k in common_keys}
		sorted_b = {k: sort_and_replace_types(a.get(k), b[k]) if k in a else get_json_type(b[k]) for k in common_keys}

		# 将不同的字段也替换为字段类型
		sorted_a.update({k: get_json_type(a[k]) for k in a_unique_keys})
		sorted_b.update({k: get_json_type(b[k]) for k in b_unique_keys})

		return sorted_a, sorted_b

	elif isinstance(a, list) and isinstance(b, list):
		# 如果是列表，递归处理列表中的每个元素
		return [sort_and_replace_types(ai, bi) for ai, bi in zip(a, b)]

	return get_json_type(a)  # 如果是基础类型，直接返回类型名


def sort_json_file_with_types(json_data, sorted_keys):
	"""按照排序后的字段顺序，替换字段值为类型"""
	if isinstance(json_data, dict):
		# 按照 sorted_keys 的顺序排序并替换类型
		sorted_dict = {k: sort_json_file_with_types(json_data[k], sorted_keys) if isinstance(json_data[k], (
		dict, list)) else get_json_type(json_data[k]) for k in sorted_keys if k in json_data}
		return sorted_dict
	elif isinstance(json_data, list):
		return [sort_json_file_with_types(item, sorted_keys) for item in json_data]
	return get_json_type(json_data)


# 读取json文件
def load_json(file_path):
	with open(file_path, 'r', encoding='utf-8') as f:
		return json.load(f)


# 保存json文件
def save_json(file_path, data):
	with open(file_path, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=4)


# 示例使用
a_json = load_json('a.json')
b_json = load_json('b.json')

# 对相同字段进行排序并替换类型，得到排序后的字段顺序
sorted_a, sorted_b = sort_and_replace_types(a_json, b_json)

# 使用得到的相同字段的顺序来排序和替换各自的文件
sorted_a_keys = list(sorted_a.keys())  # 获取排序后的键
sorted_b_keys = list(sorted_b.keys())

# 按照排序好的键顺序对两个 JSON 文件进行处理，并替换字段值为类型
final_sorted_a = sort_json_file_with_types(a_json, sorted_a_keys)
final_sorted_b = sort_json_file_with_types(b_json, sorted_b_keys)

# 保存处理后的文件
save_json('sorted_a.json', final_sorted_a)
save_json('sorted_b.json', final_sorted_b)
