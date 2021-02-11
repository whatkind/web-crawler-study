# get请求 quote转码
from urllib.request import Request, urlopen
from urllib.parse import quote

search = input("请输入需要搜索的内容：")
url = "https://www.baidu.com/s?ie=UTF-8&wd={}".format(quote(search))
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
# 设置请求头，伪装成谷歌浏览器
headers = {
    "User-Agent": user_agent
}
# 设置request对象
request = Request(url, headers=headers)
# 请求
print(urlopen(request).read().decode())
