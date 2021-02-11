# post请求
from urllib.request import Request, urlopen
from fake_useragent import UserAgent
import json

url = "https://sznlh.it97xy.cn/auth/login"
form_data = {
    "mobile": "admin",
    "password": "123456"
}
headers = {
    "User-Agent": UserAgent().random,
    "Content-Type": "application/json"
}
request = Request(url, data=json.dumps(form_data).encode(), headers=headers)
response = urlopen(request)
print(response.read().decode())
