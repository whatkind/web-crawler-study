# 设置请求头访问
from urllib.request import Request, urlopen
from random import choice
from fake_useragent import UserAgent

url = "http://www.baidu.com"
user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
              "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"]
# 设置请求头，伪装成谷歌浏览器
headers = {
    "User-Agent": choice(user_agent)
}
# 设置request对象
request = Request(url, headers=headers)
# 请求
print(urlopen(request).read().decode())

# UserAgent库
ua = UserAgent()
print(ua.chrome)
print(ua.firefox)
