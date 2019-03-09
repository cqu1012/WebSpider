# -*- coding: utf-8 -*-
#bs练习

from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

url = 'https://www.itbaizhan.cn/stages/id/17'
headers={"User-Agent":UserAgent().random}
rsp = requests.get(url,headers)
# print(rsp.text)
bs = BeautifulSoup(rsp.text,'lxml')

# print(bs.find_all('div'))
# print(bs.select('a[class=info_title]'))
print(bs.find_all('div',class_='hdlm'))