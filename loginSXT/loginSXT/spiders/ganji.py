# -*- coding: utf-8 -*-
import scrapy
import re
from PIL import Image

class GanjiSpider(scrapy.Spider):
    name = 'ganji'
    allowed_domains = ['ganji.com']
    start_urls = ['https://passport.ganji.com/login.php']

    def parse(self, response):
        #获取hash（csrf_token）值
        hash_code = re.search(r'"__hash__":"(.+)"}',response.text).group(1)
        #获取验证码
        yzm_url =  'https://passport.ganji.com/ajax.php?dir=captcha&module=login_captcha'
        yield scrapy.Request(yzm_url,meta={'hash_code':hash_code},callback=self.get_form)
    def get_form(self,response):
        with open('yzm.jpg','wb') as f:
            f.write(response.body)
        code = input('请输入验证码：')
        hash_code = response.request.meta['hash_code']
        form_data={
            'username':'15112634495',
            'password':'1012jing',
            'setcookie':'0',
            'next':'/',
            'source':'passport',
            '__hash__':hash_code,
            'checkCode':code,
        }
        yield scrapy.FormRequest('https://passport.ganji.com/login.php',formdata=form_data,callback=self.loginStatus)
    def loginStatus(self,response):
        print(response.text)
