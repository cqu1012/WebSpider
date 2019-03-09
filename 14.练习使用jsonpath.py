# -*- coding: utf-8 -*-
#练习使用jsonpath
from jsonpath import jsonpath
from fake_useragent import UserAgent
import requests
url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {'User-Agent':UserAgent().random}

resp = requests.get(url,headers=headers)

# print(resp.json())
ids = jsonpath(resp.json(),('$..id'))
names = jsonpath(resp.json(),'$..name')
for id,name in zip(ids,names):
    print(id,':',name)

