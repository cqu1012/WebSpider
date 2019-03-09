# -*- coding: utf-8 -*-
import scrapy


class ZonghengSpider(scrapy.Spider):
    name = 'zongheng'
    allowed_domains = ['zongheng.com']
    start_urls = ['http://www.zongheng.com/rank/details.html?rt=1&d=1']

    def parse(self, response):
        names= response.xpath("//div[@class='rank_d_b_name']/a/text()").extract()
        authors =response.xpath("//div[@class='rank_d_b_cate']/a/text()").extract()
        books =[]

        for name,author in zip(names,authors):
            # print(name,author)
            books.append(
                {
                    'name':name,
                    'author':author,
                }
            )
        print(books)
        return books

