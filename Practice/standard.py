import requests
from fake_useragent import UserAgent
from lxml import etree


# url管理
class URLManager:
    def __init__(self):
        self.new_url = []
        self.old_url = []

    # 获取一个url
    def get_new_url(self):
        url = self.new_url.pop()
        self.old_url.append(url)
        return url

    # 增加一个url
    def add_new_url(self, url):
        if url not in self.new_url and url and url not in self.old_url:
            self.new_url.append(url)

    # 增加多个urls
    def add_new_urls(self, urls):
        for url in urls:
            self.add_new_url(url)

    # 获取可爬取的数量
    def has_new_url(self):
        return self.get_new_url_size() > 0

    # 获取可爬取的数量
    def get_new_url_size(self):
        return len(self.new_url)

    # 获取已经爬取的数量
    def get_old_url_size(self):
        return len(self.old_url)


# 爬取
class Downloader:
    def download(self, url):
        response = requests.get(url, headers={"User-Agent": UserAgent().random})
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        else:
            return None


# 解析
class Parser:
    def parse(self, html, data_xpath, urls_xpath):
        e = etree.HTML(html)
        datas = e.xpath(data_xpath)
        urls = e.xpath(urls_xpath)
        return datas, urls


# 数据处理
class DataOutput:
    def save(self, datas):
        with open('data.txt', 'a', encoding='utf-8') as f:
            for data in datas:
                f.write(data)
        print(data)


# 调度
class Executer:
    def __init__(self):
        self.downloader = Downloader()
        self.url_manager = URLManager()
        self.parser = Parser()
        self.data_server = DataOutput()

    def run(self, url, data_xpath, urls_xpath):
        self.url_manager.add_new_url(url)
        while self.url_manager.has_new_url():
            url = self.url_manager.get_new_url()
            html = self.downloader.download(url)
            data, urls = self.parser.parse(html, data_xpath, urls_xpath)
            self.data_server.save(data)
            self.url_manager.add_new_urls(urls)


if __name__ == '__main__':
    execute = Executer()
    execute.run("https://www.qiushibaike.com/text/")
