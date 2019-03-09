# -*- coding: utf-8 -*-
import scrapy

class BiqugetxtSpider(scrapy.Spider):
    name = 'biqugeTxt'
    allowed_domains = ['biquge.cc']
    start_urls = ['https://www.biquge.cc/html/103/103395/3743334.html']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract()[0]
        content = response.xpath("string(//div[@id='content'])").extract_first().strip().replace('    ','\n')
        nextPageUrl = response.xpath("//a[@id='pager_next']/@href").extract()[0]

        yield {
            "title":title,
            'content':content,
        }
        if nextPageUrl != './':
            yield scrapy.Request(response.urljoin(nextPageUrl),callback=self.parse)

