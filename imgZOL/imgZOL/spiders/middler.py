# -*- coding: utf-8 -*-
import scrapy


class MiddlerSpider(scrapy.Spider):
    name = 'middler'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        print(response.text)

