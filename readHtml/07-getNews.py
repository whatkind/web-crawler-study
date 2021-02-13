import requests
from lxml import etree
from fake_useragent import UserAgent

url = "http://www.farmer.com.cn/2021/01/26/99865031.html"
headers = {
    "User-Agent": UserAgent().random,
}
response = requests.get(url, headers=headers)
response.encoding = "utf-8"
e = etree.HTML(response.text)
title = e.xpath('//h1[@class="article-title"]/text()')
contents = e.xpath('//div[@class="article-main"]/p')
for content in contents:
    print(content)
images = e.xpath('//div[@class="article-main"]/p/img/@src')
print(title)
# print(contents)
print(images)
