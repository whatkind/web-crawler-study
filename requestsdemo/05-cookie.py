import requests
from fake_useragent import UserAgent

session = requests.Session()
headers = {
    "User-Agent": UserAgent().random,
    "Content-Type": "application/json"
}
login_url = "https://sznlh.it97xy.cn/auth/login"
params = {
    "mobile": "admin",
    "password": "123456"
}
response = session.post(login_url, headers=headers, json=params)
info_url = ""
resp = session.get(info_url, headers=headers)
