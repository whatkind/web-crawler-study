# 错误访问信息
from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.error import URLError

url = "https://www.bilibili.com/get"
headers = {
    "User-Agent": UserAgent().random,
}
try:
    request = Request(url, headers=headers)
    urlopen(request).read().decode()
except URLError as e:
    if e.args == ():
        print(e.code)
    else:
        print(e.args[0].errno)
print("done")
