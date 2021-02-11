# cookie两种使用 1.在header里设置 2.opener携带
from urllib.request import build_opener, Request, urlopen, HTTPCookieProcessor
from fake_useragent import UserAgent

login_url = "https://www.bilibili.com/"
headers = {
    "User-Agent": UserAgent().random,
}
request = Request(login_url, headers=headers)
handler = HTTPCookieProcessor()
opener = build_opener(handler)
print(opener.open(request).read().decode())
# 登陆后已经获取到cookie
info_url = ""
request = Request(login_url, headers=headers)
# opener已经携带cookie
print(opener.open(request).read().decode())
