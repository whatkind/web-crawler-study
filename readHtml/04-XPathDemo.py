from fake_useragent import UserAgent
from lxml import etree
import requests

url = "https://www.qidian.com/rank/yuepiao?style=1"
headers = {
    "User-Agent": UserAgent().random,
}
response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
names = e.xpath('//h4/a/text()')
authors = e.xpath('//p[@class="author"]/a[1]/text()')
authors_desc = e.xpath('//p[@class="author"]/a[1]/@href')

print("书名", names)
print("作者", authors)
print("作者详情url", authors_desc)

# for num in range(len(names)):
#     print(names[num], ":", authors[num])

for name, author in zip(names, authors):
    print(name, ":", author)
