import requests
from fake_useragent import UserAgent

url = "https://www.12306.cn/index/"
headers = {
    "User-Agent": UserAgent().random
}
response = requests.get(url, headers=headers)
response.encoding = "utf-8"
print(response.text)
