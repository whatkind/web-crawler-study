# ajax请求
from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20"
headers = {
    "User-Agent": UserAgent().random
}
i = 0
while True:
    request = Request(url, headers=headers)
    response = urlopen(request).read().decode()
    print(response)
    if response == "" or response is None:
        break
    i += 1
