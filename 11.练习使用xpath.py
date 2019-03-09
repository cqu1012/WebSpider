# -*- coding: utf-8 -*-
#使用Xpath爬取百战程序员的标题
from fake_useragent import UserAgent
from lxml import etree
import requests

url = 'https://www.itbaizhan.cn/stages/id/17'
rsp = requests.get(url,headers={'User-Agent':UserAgent().random})
# print(rsp.text)
html = etree.HTML(rsp.text)
courseList = html.xpath("//div[@class='info_title_0']/a/text()")