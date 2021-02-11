# get请求 urlencode转码
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

search = input("请输入需要搜索的内容：")
args = {
    "wd": search
}
url = "https://www.baidu.com/s?ie=UTF-8&{}".format(urlencode(args))
print(url)
# 设置请求头，伪装成谷歌浏览器
# headers = {
#     "User-Agent": UserAgent().random
# }
# # 设置request对象
# urllib = Request(url, headers=headers)
# # 请求
# print(urlopen(urllib).read().decode())
