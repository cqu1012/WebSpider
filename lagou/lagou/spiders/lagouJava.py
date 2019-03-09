# -*- coding: utf-8 -*-
import scrapy


class LagoujavaSpider(scrapy.Spider):
    name = 'lagouJava'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/jobs/list_Java?px=default&gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&xl=%E6%9C%AC%E7%A7%91&city=%E6%B7%B1%E5%9C%B3#filterBox']

    def parse(self, response):
        position = response.xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').extract()
        location = response.xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/span/em').extract()
        company = response.xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[2]/div[1]/a').extract()
        salary = response.xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[2]/div/span').extract()
        print('positon：{}，location:{},company:{},salary:{}'.format(position,location,company,salary))
