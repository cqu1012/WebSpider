# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Biquge2txtSpider(CrawlSpider):
    name = 'biquge2Txt'
    allowed_domains = ['biquge.cc']
    start_urls = ['https://www.biquge.cc/html/198/198351/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r"//a[@class='contentHerf']/@href"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//*[@id="pager_next"]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        title = response.xpath('//h1/text()').extract()[0]
        content = response.xpath("string(//div[@id='content'])").extract_first().strip().replace('　　　　', '\n')
        yield {
            "title": title,
            'content': content,
        }
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
