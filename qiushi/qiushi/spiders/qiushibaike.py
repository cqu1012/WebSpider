# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


#lpush qiushi:start_url https://www.qiushibaike.com/text/
from scrapy_redis.spiders import RedisCrawlSpider


class QiushibaikeSpider(RedisCrawlSpider):
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['https://www.qiushibaike.com/text/']
    redis_key = "qiushi:start_url"
    rules = (
        Rule(LinkExtractor(restrict_xpaths=r"//a[@class='contentHerf']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r"//ul[@class='pagination']/li/a"), callback='parse_item', follow=True),
    )
    # rules = (
    #     Rule(LinkExtractor(allow=r"/article/\d+"), callback='parse_item', follow=True),
    #     Rule(LinkExtractor(allow=r"/text/page/\d+/"), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        title = response.xpath("//h1[@class='article-title']/text()")
        if title:
            title = title.extract_first().strip()
            haoxiao = response.xpath("string(//span[@class='stats-vote'])").extract_first().strip()
            content = response.xpath("//div[@class='content']/text()").extract_first()
            yield {
                'title':title,
                'haoxiao':haoxiao,
                'contene':content
            }
        # print(title,haoxiao,content)
        return item
