# 查看京东商品价格
from time import sleep
from selenium import webdriver
from lxml import etree

driver = webdriver.Chrome()
driver.get("https://search.jd.com/Search?keyword=macbook%20pro&enc=utf-8&suggest=4.def.0.base&wq=mac&pvid=1ad3d40a604c4622bc999dbb46f7a406")
js = 'document.documentElement.scrollTop=10000'
driver.execute_script(js)
sleep(3)
html = driver.page_source
e = etree.HTML(html)
prices = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i/text()')
titles = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a[name(.)!="p-tag"]/em')
print(len(titles))
for price, title in zip(prices, titles):
    print(title.xpath('string(.)'), ':', price)
sleep(3)
driver.quit()
