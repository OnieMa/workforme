import yaml
import json
import jsonref

# 读取YAML文件
with open('sky.yml', 'r') as f:
    yaml_data = yaml.safe_load(f)

# 将YAML转换为JSON
json_data = json.dumps(yaml_data)

data = jsonref.loads(json_data)
with open('result.json', 'w') as f:
    json.dump(data, f, indent=2)
