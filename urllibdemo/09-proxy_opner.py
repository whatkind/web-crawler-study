# build_opener使用
from urllib.request import build_opener, Request, HTTPHandler
from fake_useragent import UserAgent

url = "http://www.baidu.com"
headers = {
    "User-Agent": UserAgent().random
}
request = Request(url, headers=headers)
handler = HTTPHandler()
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
