# 代理请求
from urllib.request import build_opener, Request, ProxyHandler
from fake_useragent import UserAgent

# 次链接能获取请求IP
url = "http://httpbin.org/get"
headers = {
    "User-Agent": UserAgent().random
}
request = Request(url, headers=headers)
handler = ProxyHandler({
    "http": "ip:port"
})
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
