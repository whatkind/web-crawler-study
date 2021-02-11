# 爬取百度贴吧数据
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

def get_html(url):
    headers = {
        "User-Agent": UserAgent().random
    }
    # 设置request对象
    request = Request(url, headers=headers)
    return urlopen(request).read()

def save_html(filename,html):
    with open(filename, "wb") as f:
        f.write(html)

def main():
    content = "主机"
    pn = (int(input("请输入第几页："))-1) * 50
    args = {
        "kw": content,
        "pn": pn
    }
    html = get_html("https://tieba.baidu.com/f?ie=UTF-8&{}".format(urlencode(args)))
    file_name = content + str(pn + 1) + ".html"
    save_html(file_name, html)

if __name__ == "__main__":
    main()
