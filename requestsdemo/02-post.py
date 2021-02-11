import requests
from fake_useragent import UserAgent

headers = {
    "User-Agent": UserAgent().random,
    "Content-Type": "application/json"
}
url = "https://sznlh.it97xy.cn/auth/login"
params = {
    "mobile": "admin",
    "password": "123456"
}
response = requests.post(url, headers=headers, json=params)
print(response.text)
