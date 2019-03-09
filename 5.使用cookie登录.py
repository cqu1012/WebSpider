# -*- coding: utf-8 -*-
#使用cookie,直接使用cookie
from urllib.request import Request,urlopen
from fake_useragent import UserAgent
headers = {
    'User-Agent':UserAgent().random,
    'Cookie':' PHPSESSID=h7g4nfn9fvggen1q02d36od1g4; UM_distinctid=1690a32de0c7b0-0e9cd9cda31807-6313363-e1000-1690a32de0db7b; CNZZDATA1261969808=993143005-1550649659-http%253A%252F%252Fwww.sxt.cn%252F%7C1550649659',
}
url ='http://www.sxt.cn/index/user.html'

rsp = Request(url,headers=headers)

rspe = urlopen(rsp)
print(rspe.read().decode())