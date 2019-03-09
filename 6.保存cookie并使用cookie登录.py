# -*- coding: utf-8 -*-
#登录使用cookie

from urllib.request import Request,build_opener,urlopen
from fake_useragent import UserAgent
from urllib.request import HTTPCookieProcessor
from urllib.parse import urlencode

url = 'http://www.sxt.cn/index/login/login'
form_date ={
    'user':'18664344229',
    'password':'1012jing',
}

headers = {
    'User-Agent':UserAgent().random,
}
rsp = Request(url,headers=headers,data=urlencode(form_date).encode())
handler = HTTPCookieProcessor()
opener = build_opener(handler)
rspe = opener.open(rsp)
# print(rspe.read().decode())

#------登录成功--------

url1 = 'http://www.sxt.cn/index/user.html'

rsp1 = Request(url1,headers=headers)

rspe = opener.open(rsp1)

print(rspe.read().decode())

