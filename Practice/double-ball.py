# 爬取双色球数据入库
import requests
from fake_useragent import UserAgent
from lxml import etree
import pymysql

url = 'https://datachart.500.com/ssq/'
headers = {
    "User-Agent": UserAgent().random,
}
response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
data_times = e.xpath('//tbody[@id="tdata"]/tr/td[1]/text()')
trs = e.xpath('//tbody[@id="tdata"]/tr[not(@class)]')

# mysql
client = pymysql.connect(host='localhost', port=3306, user='root', password='root', charset='utf8mb4', db='test')
cursor = client.cursor()
sql = 'INSERT INTO t_ball VALUES(%s,%s,%s)'
select_sql = 'SELECT * FROM t_ball where data_time=%s'
data_times.reverse()

index = 0
for data_time in data_times:
    result = cursor.execute(select_sql, [data_time])
    if result == 1:
        break
    index += 1
trs.reverse()

print('新数据', index)
print('获取数据', len(data_times))

for i in range(index):
    red_ball = '-'.join(trs[i].xpath('./td[@class="chartBall01"]/text()'))
    blue_ball = trs[i].xpath('./td[@class="chartBall02"]/text()')[0]
    cursor.execute(sql, [data_times[i], red_ball, blue_ball])
    client.commit()
    print(data_times[i], red_ball, blue_ball)

# for data_time, tr in zip(data_times, trs):
#     red_ball = '-'.join(tr.xpath('./td[@class="chartBall01"]/text()'))
#     blue_ball = tr.xpath('./td[@class="chartBall02"]/text()')[0]
#     print(data_time, red_ball, blue_ball)
