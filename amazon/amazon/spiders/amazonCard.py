# -*- coding: utf-8 -*-
import scrapy

#https://www.amazon.cn/s/ref=sr_pg_2?rh=n%3A664978051%2Ck%3A%E5%8D%8E%E4%B8%BA&page=1&keywords=%E5%8D%8E%E4%B8%BA&ie=UTF8&qid=1551923130

class AmazoncardSpider(scrapy.Spider):
    name = 'amazonCard'
    allowed_domains = ['amazon.cn']
    start_urls = ['https://www.amazon.cn/s/ref=sr_pg_2?rh=n%3A664978051%2Ck%3A%E5%8D%8E%E4%B8%BA&page=1&keywords=%E5%8D%8E%E4%B8%BA&ie=UTF8&qid=1551923130']

    def parse(self, response):
        # print(response.text)
        url_list = [ div.xpath('./@href').extract_first() for div in response.xpath("//div[@class='a-row a-spacing-none sx-line-clamp-4']/a")]
        for url in url_list:
            yield scrapy.Request(response.urljoin(url),callback=self.getInfo)
    def getInfo(self,reponse):
        title = reponse.xpath('//h1/span/text()').extract_first().strip()
        brand = reponse.xpath("//div[@class='a-section a-spacing-none']/a/text()").extract_first()
        star = reponse.xpath("//span[@class='a-declarative']/span/span/a/i/span/text()").extract_first()
        price = reponse.xpath("//td[@class='a-span12']/span[1]/text()").extract_first()
        status = reponse.xpath('//span[@class="a-color-success ddm-font-size-15"]/text()').extract_first()

        yield {
            'title':title,
            'brand':brand,
            'star' : star,
            'price':price,
            'status':status,
        }






