import requests
from fake_useragent import UserAgent

headers = {
    "User-Agent": UserAgent().random,
}
url = "https://www.baidu.com/s"
params = {
    "wd": "B站"
}
response = requests.get(url, headers=headers, params=params)
print(response.text)
