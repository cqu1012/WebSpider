# -*- coding: utf-8 -*-
#获取糗事百科前三页数据
from urllib.request import Request,urlopen

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}
base_url = 'https://www.qiushibaike.com/8hr/page/{}/'
for i in range(3):
    rsp = Request(base_url.format(i+1),headers=headers)
    resp = urlopen(rsp)
    context = resp.read().decode()
    filename = '第{}页.html'.format(i+1)
    with open(filename,'w',encoding='utf-8') as f:
        f.write(context)
