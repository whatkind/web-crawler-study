# cookie使用场景：有的网站登录后会将登录信息存在cookie以便鉴权访问
from urllib.request import build_opener, Request, urlopen, HTTPCookieProcessor
from fake_useragent import UserAgent
from http.cookiejar import MozillaCookieJar

# 登录
# 保存cookie到文件里
def get_cookie():
    login_url = "https://www.bilibili.com/"
    headers = {
        "User-Agent": UserAgent().random,
    }
    request = Request(login_url, headers=headers)
    cookie_jar = MozillaCookieJar()
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    opener.open(request)
    cookie_jar.save("cookie.text", ignore_expires=True, ignore_discard=True)
# 登陆后使用cookie发送请求
def use_cookie():
    info_url = ""
    headers = {
        "User-Agent": UserAgent().random,
    }
    request = Request(info_url, headers=headers)
    cookie_jar = MozillaCookieJar()
    cookie_jar.load("cookie.text", ignore_expires=True, ignore_discard=True)
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    opener.open(request)

if __name__ == "__main__":
    get_cookie()
    use_cookie()
