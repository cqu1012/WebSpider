# -*- coding: utf-8 -*-
#爬取猫眼电影电影分数
from fake_useragent import UserAgent
from lxml import etree
import requests
class NoFindHtml(Exception):
    print('未找到页面')

def getHtml(url):
    '''
    :param url:电影页面Url
    :return: 返回Html
    '''
    headers = {"User-Agent": UserAgent().random}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.html
    else:
        raise NoFindHtml
def getMovieInfo(Html):
    '''
    :param Html:电影Html页面
    :return: 返回电影名称以及评分
    '''
    html = etree.HTML(Html)
    nameList = html.xpath('//div[@class="channel-detail movie-item-title"]/a/text()')
    socoreList = html.xpath('')

def main():
    url = 'https://maoyan.com/films?showType=3&offset=0'
    html=getHtml(url)
    print(getMovieInfo(html))


if __name__ == '__main__':
    main()