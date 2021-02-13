# xpath爬取猫眼电影
from fake_useragent import UserAgent
import requests
from lxml import etree
from random import randint
from time import sleep


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
    e = etree.HTML(html)
    all_urls = e.xpath('//div[@class="movie-item film-channel"]/a/@href')
    return ['https://maoyan.com{}'.format(url) for url in all_urls]


def parse_info(html):
    e = etree.HTML(html)
    name = e.xpath('//h1/text()')
    types = e.xpath('//li[@class="ellipsis"]/a/text()')
    actors = e.xpath('//li[@class="celebrity actor"]/div/a/text()')
    actors = format_actors(actors)
    return {
        "name": name,
        "types": types,
        "actors": actors
    }


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
