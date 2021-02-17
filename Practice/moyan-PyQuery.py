# PyQuery爬取猫眼电影
from fake_useragent import UserAgent
import requests
from random import randint
from time import sleep
from pyquery import PyQuery as pq


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
    doc = pq(html)
    all_a = doc("div.movie-item.film-channel").children('a')
    all_urls = []
    for a in all_a:
        all_urls.append(a.get('href'))
    return ['https://maoyan.com{}'.format(url) for url in all_urls]


def parse_info(html):
    doc = pq(html)
    name = to_arr(doc("h1.name"))
    types = to_arr(doc("li.ellipsis a"))
    actors = to_arr(doc("li.celebrity.actor div a"))
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
