# 保存图片
import requests
from fake_useragent import UserAgent
from lxml import etree

url = "https://yuehaimo.tuchong.com/83087994/"
headers = {
    "User-Agent": UserAgent().random,
}
response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
img_urls = e.xpath('//article[@class="post-content"]/img/@src')
for url in img_urls:
    response = requests.get(url, headers=headers)
    img_name = url[url.rfind('/')+1:]
    with open('img/' + img_name, "wb") as f:
        f.write(response.content)
