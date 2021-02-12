from pyquery import PyQuery as pq
import requests
from fake_useragent import UserAgent

url = "https://ip.jiangxianli.com/"
headers = {
    "User-Agent": UserAgent().random,
}
# 构造请求
response = requests.get(url, headers=headers)
doc = pq(response.text)
trs = doc('.layui-table tbody tr')
for i in range(trs.length):
    tr = trs.eq(i)
    print(tr.find('td').eq(0).text())
# ips = doc('.layui-table tbody tr').eq(1).find('td').text()
# ports = doc()
# ips = doc()
