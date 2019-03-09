# -*- coding: utf-8 -*-
import scrapy

from imgZOL.items import ImgzolItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/bizhi/7373_91358_2.html']

    def parse(self, response):
        img_url = response.xpath('//*[@id="bigImg"]/@src').extract_first()
        img_name = response.xpath('string(//h3)').extract_first().strip().replace('\r\n\t\t','')
        next_img_url = response.xpath('//*[@id="pageNext"]/@href').extract_first()
        print(img_url,img_name,next_img_url)
        # item = ImgzolItem()
        # item['img_urls']=img_url
        # item['img_name'] = img_name
        # yield item
        yield {
            'image_url':img_url,
            'image_name':img_name,
        }
        yield scrapy.Request(response.urljoin(next_img_url),callback=self.parse)
