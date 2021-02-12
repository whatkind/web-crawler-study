import json
import requests
from fake_useragent import UserAgent
from jsonpath import jsonpath

# str1 = '{"demo": "测试"}'
# print(type(str1), str1)
# obj = json.loads(str1)
# print(type(obj), obj)
#
# str2 = json.dumps(obj, ensure_ascii=False)  # 关闭ascii码
# print(type(str2), str2)
# json.dump(obj, open("movies.txt", 'w', encoding='utf-8'), ensure_ascii=False)
#
# str3 = json.load(open("movies.txt", encoding='utf-8'))
# print(type(str3), str3)

# 获取所有城市json
url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent": UserAgent().random,
}
response = requests.get(url, headers=headers)
names = jsonpath(json.loads(response.text), '$..name')
codes = jsonpath(response.json(), '$..code')
print(names)
print(codes)
