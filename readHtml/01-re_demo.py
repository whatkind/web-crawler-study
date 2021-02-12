import re

str1 = "I Study Python3.7 Everyday"
print("-----------------match------------------")
try:
    m1 = re.match(r'I', str1)
    m2 = re.match(r'\w', str1)
    m3 = re.match(r'../REdemo', str1)
    m4 = re.match(r'\D', str1)
    m5 = re.match(r'i', str1, re.I)
    m6 = re.match(r'\S', str1, re.I)
    m7 = re.match(r'Study', str1)  # 匹配不到，因为match是从左开始匹配的
    print(m7.group())
except Exception as e:
    print('结果未匹配', e)

print("\r\n----------------search------------------")
try:
    s1 = re.search(r'Study', str1)
    s2 = re.search(r'S\w+', str1)  # 匹配Study
    s3 = re.search(r'P\w+.\d', str1)  # 匹配Python3.7
    print(s3.group())
except Exception as e:
    print('结果未匹配', e)

print("\r\n----------------findall------------------")
try:
    # 匹配所有y
    f1 = re.findall(r'y', str1)
    print(f1)
except Exception as e:
    print('结果未匹配', e)

print("\r\n----------------网页标签匹配------------------")
str2 = '<div><a href="https://www.baidu.com">百度搜索</a></div>'
try:
    t1 = re.findall(r'[\u4e00-\u9fa5]\w+', str2)  # 按中文匹配
    t2 = re.findall(r'<a href="https://www.baidu.com">(.+)</a>', str2)  # 获取a标签标题
    t3 = re.findall(r'href="(.+)"', str2)  # 获取a标签href
    print(t3)
except Exception as e:
    print('结果未匹配', e)

print("\r\n----------------sub------------------")
try:
    s1 = re.sub(r'<div>(.+)</div>', r'<span>\1</span>', str2)  # 将div标签里所有内容获取到，然后放在span标签下 \1代表第一组
    print(s1)
except Exception as e:
    print('结果未匹配', e)
