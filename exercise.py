import json

with open("data/경영학과/2019학년도 1학기.json", "r", encoding="utf-8") as f:
    data = json.load(f)
dict_example = json.loads(data)
print(dict_example)
