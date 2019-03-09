# -*- coding: utf-8 -*-
#练习使用pyquery
from fake_useragent import UserAgent
import requests
from pyquery import PyQuery as pq

url = 'https://www.qidian.com/rank/yuepiao?chn=21'
headers = {'User-Agent':UserAgent().random}
resp = requests.get(url,headers)
doc = pq(resp.text)
names = [aobj.text for aobj in doc('h4 a')]
# author = doc('.author').find('a')
# print(author)
authors=[doc('.author').find('a').eq(num).text() for num in range(len(doc('.author').find('a'))) if num%2==0]
for name ,author in zip(names,authors):
    print(name,':',author)

