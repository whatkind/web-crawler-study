import requests
from fake_useragent import UserAgent

url = "http://httpbin.org/get"
headers = {
    "User-Agent": UserAgent().random
}
proxies = {
    "http": "ip:port"
}
response = requests.get(url, headers=headers, proxies=proxies)
print(response.text)
