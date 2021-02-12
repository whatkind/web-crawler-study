from bs4 import BeautifulSoup
from bs4.element import Comment

str1 = '''
<title id="title">bs4例子</title>
<div class="info" float="left">HelloWorld</div>
<div class="info" float="right">
    <span>Right Right Right</span>
    <a href="http://www.baidu.com">百度一下</a>
    <strong><!--注释--></strong>
</div>
'''
print("获取标签代码")
soup = BeautifulSoup(str1, 'lxml')
print(soup.title)
print(soup.div)

print("\r\n标签操作")
# 标签操作
print(soup.div.attrs)  # 获取div里属性
print(soup.div.get("class"))  # 获取div里属性
print(soup.div['float'])  # 获取div里属性
print(soup.a['href'])  # 获取a里属性

print("\r\n获取内容")
# 获取内容
print(soup.div.string)
print(soup.div.text)

print("\r\n获取注释")
if type(soup.strong.string) == Comment:
    print(soup.strong.string)
    print(soup.strong.prettify())
else:
    print(soup.strong.text)

print("\r\n----------------find_all------------------")
print(soup.find_all('title'))
print(soup.find_all(id='title'))
print(soup.find_all(class_='info'))
print(soup.find_all("div", attrs={'float': 'left'}))

print("\r\n----------------css------------------")
print(soup.select("title"))
print(soup.select("#title"))
print(soup.select(".info"))
print(soup.select("div span"))
print(soup.select("div > span"))
print(soup.select("div")[1].select("a"))
print(soup.select("title")[0].text)
