# RE爬取猫眼电影
from fake_useragent import UserAgent
import requests
from random import randint
from time import sleep
import re


def get_html(url):
    headers = {
        "User-Agent": UserAgent().random,
    }
    sleep(randint(3, 10))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_index(html):
    all_urls = re.findall(r'<div class="movie-item film-channel">\s+<a href="(.+)" target="_blank" data-act="movie-click" data-val="{movieid:\d+}">', html)
    return ['https://maoyan.com{}'.format(url) for url in all_urls]


def parse_info(html):
    name = re.findall(r'<h1 class="name">(.+)</h1>', html)
    types = re.findall(r'<a class="text-link".+> (.+) </a>', html)
    actors = re.findall(r'<li class="celebrity actor".+>\s+<a.+>\s+<img.+ alt=" (.+)" />', html)
    actors = format_actors(actors)
    return {
        "name": name,
        "types": types,
        "actors": actors
    }


# 解析bs数组对象
def to_arr(params):
    param_set = set()
    for param in params:
        param_set.add(param.text.strip())
    return param_set


def format_actors(actors):
    actors_set = set()
    for actor in actors:
        actors_set.add(actor.strip())
    return actors_set


def main():
    index_html = "https://maoyan.com/films"
    html = get_html(index_html)
    movie_urls = parse_index(html)
    for url in movie_urls:
        movie_html = get_html(url)
        film = parse_info(movie_html)
        print(film)


if __name__ == '__main__':
    main()
