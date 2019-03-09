# -*- coding: utf-8 -*-
#获取糗事百科段子
import requests
from fake_useragent import UserAgent
import re

url = 'https://www.qiushibaike.com/hot/'
rsp = requests.get(url,headers={'User-Agent':UserAgent().random})
# print(rsp.text)
text = re.findall(r'<div class="content">\s*<span>\s*(.*)',rsp.text)

with open('qiushi.txt','a',encoding='utf-8') as f:
    for content in text:
        f.write(content+'\n\n')

