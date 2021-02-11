# https请求
from urllib.request import Request, urlopen
from fake_useragent import UserAgent
import ssl

url = "https://www.12306.cn/index/"
headers = {
    "User-Agent": UserAgent().random
}
# 加入忽略证书的方法（暂时未写）
request = Request(url, headers=headers)
print(urlopen(request).read().decode())
