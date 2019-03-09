# -*- coding: utf-8 -*-
#xpath练习
#获取起点网小说名称与作者
from lxml import etree
from fake_useragent import UserAgent
import requests

url = 'https://www.qidian.com/rank/yuepiao?chn=21'
headers ={"User-Agent":UserAgent().random}

rsp = requests.get(url,headers)

html = etree.HTML(rsp.text)
names = html.xpath("//div[@class='book-mid-info']/h4/a/text()")
authors = html.xpath("//p[@class='author']/a[1]/text()")

for name,author in zip(names,authors):
    print(name,':',author)