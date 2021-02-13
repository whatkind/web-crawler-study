from threading import Thread
from queue import Queue
from fake_useragent import UserAgent
import requests
from lxml import etree


class CrawlInfo(Thread):
    def __init__(self, url_queue, html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue

    def run(self):
        headers = {
            "User-Agent": UserAgent().random,
        }
        while not self.url_queue.empty():
            response = requests.get(self.url_queue.get(), headers=headers)
            if response.status_code == 200:
                self.html_queue.put(response.text)


class ParseInfo(Thread):
    def __init__(self, html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue

    def run(self):
        while not self.html_queue.empty():
            e = etree.HTML(self.html_queue.get())
            span_contents = e.xpath('//div[@class="content"]/span[1]')
            with open('duanzi.txt', 'a', encoding='utf-8') as f:
                for span in span_contents:
                    info = span.xpath('string(.)')
                    f.write(info + '\n')


if __name__ == '__main__':
    # 存储url容器
    url_queue = Queue()
    # 存储html容器
    html_queue = Queue()
    base_url = "https://www.qiushibaike.com/text/page/{}/"
    for i in range(1, 14):
        new_url = base_url.format(i)
        url_queue.put(new_url)

    # 开始爬取网站
    crawl_list = []
    for i in range(0, 3):
        crawl1 = CrawlInfo(url_queue, html_queue)
        crawl_list.append(crawl1)
        crawl1.start()
    for crawl in crawl_list:
        crawl.join()

    parse_list = []
    for i in range(0, 3):
        parse = ParseInfo(html_queue)
        parse_list.append(parse)
        parse.start()
    for p in parse_list:
        p.join()
