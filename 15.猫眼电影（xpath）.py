# -*- coding: utf-8 -*-
#使用Xpath爬取猫眼电影信息
import time

from lxml import etree
from fake_useragent import UserAgent
import requests

#https://maoyan.com/films/248172
headers = {'User-Agent':UserAgent().random}
def getMovieListHtml(url):
    '''
    :param url:电影列表url
    :return: 电影列表html
    '''
    headers = {'User-Agent':UserAgent().random}
    rsp = requests.get(url,headers=headers)
    time.sleep(1)
    if rsp.status_code == 200:
        rsp.encoding = 'utf-8'
        html = rsp.text
        return html
    else:
        return None

def getMovieUrlList(html):
    '''
    :param html:电影列表html
    :return: 电影url列表
    '''
    html = etree.HTML(html)
    urls = html.xpath("//div[@class='movie-item']/a/@href")
    # urlList = []
    # for url in urls:
    #     url_c = 'https://maoyan.com{}'.format(url)
    #     urlList.append(url_c)
    urlList = ['https://maoyan.com{}'.format(url) for url in urls]
    return urlList

def getMovieDetail(url):
    '''
    :param url: 电影详细url
    :return: 电影详细信息 名称，类型，演员，等
    '''
    resp = requests.get(url,headers=headers)
    html = etree.HTML(resp.text)
    name = html.xpath("//div[@class='movie-brief-container']/h3/text()")[0]
    category = html.xpath("//div[@class='movie-brief-container']/ul/li[1]/text()")[0]
    actors = html.xpath("//div[@class='celebrity-group'][2]/ul/li/div/a/text()")
    actors = set_actors(actors)
    return {'name':name,'category':category,'actors':actors}
def set_actors(actors):
    '''
    :param actors: 演员列表
    :return: 去除重复与空格的演员列表
    '''
    actorList = set()
    for actor in actors:
        actorList.add(actor.strip())
    return actorList
def main():
    page=int(input('请输入需要查阅的页数：'))
    for i in range(page):
        url = 'https://maoyan.com/films?showType=3&offset={}'.format(i*30)
        movieListHtml = getMovieListHtml(url)
        movieUrlList = getMovieUrlList(movieListHtml)
        # print(movieUrlList)
        for movieUrl in movieUrlList:
            print(getMovieDetail(movieUrl))

if __name__ == '__main__':
    main()