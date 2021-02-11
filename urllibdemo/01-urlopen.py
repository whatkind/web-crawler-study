# 简单获取页面
from urllib.request import urlopen

# 简单获取页面信息
response = urlopen("http://www.baidu.com")
# 简单获取页面html信息
# print(response.read().decode())
# 获取状态码
print("状态码：", response.getcode())
# 获取url
print("真实url：", response.geturl())
# 获取响应头
print("响应头：", response.info())
