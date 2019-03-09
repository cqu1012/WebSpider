# -*- coding: utf-8 -*-
#Proxy的使用
from urllib.request import Request,build_opener
from urllib.request import ProxyHandler
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'
headers ={
    'User-Agent':UserAgent().chrome,
}
#链接对象（网站，头文件）
req = Request(url,headers=headers)
#建立连接对象（设置代理IP）
handler = ProxyHandler({"http":'125.123.143.204:9999'})

opener = build_opener(handler)
resp = opener.open(req)
print(resp.read().decode())
