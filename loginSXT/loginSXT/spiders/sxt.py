# -*- coding: utf-8 -*-
import scrapy


class SxtSpider(scrapy.Spider):
    name = 'sxt'
    allowed_domains = ['sxt.cn']
    # start_urls = ['http://sxt.cn/']
    def start_requests(self):
        from_date = {
            'user':'18664344229',
            'password':'1012jing',
        }
        url = 'http://www.sxt.cn/index/login/login.html'
        yield scrapy.FormRequest(url=url,formdata=from_date)
    def parse(self, response):
        print(response.text)
