# -*- coding: utf-8 -*-
#创建request类
from urllib.request import Request, urlopen
from random import choice

url = 'http://www.baidu.com/'

ua = ['u1','u2','u3']
headers = {
'User-Agent': choice(ua),
}


rsp = Request(url,headers=headers)

resp = urlopen(rsp)

print(resp.read().decode)

print(rsp.get_header('User-agent'))