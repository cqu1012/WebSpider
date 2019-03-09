# -*- coding: utf-8 -*-

import requests
from fake_useragent import UserAgent

headers = {
    'User-Agent':UserAgent().random,
}
url_yzm = 'http://www.yundama.com/index/captcha'
rsp1 =requests.Session()
rsp =rsp1.get(url_yzm,headers=headers)

with open('yzm.jpg','wb') as f:
    f.write(rsp.content)


url = 'http://www.yundama.com/index/login'
code=input('请输入验证码：')
from_date={
   'username':'425086207',
    'password':'1012jing',
    'utype':'1',
    'vcode':code,
}
resp = rsp1.get(url,headers=headers,params=from_date)
resp.encoding='utf-8'
print(resp.text)