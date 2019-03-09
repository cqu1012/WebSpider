# -*- coding: utf-8 -*-
import scrapy


class MaoyanmovieSpider(scrapy.Spider):
    name = 'maoyanMovie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&offset={}'.format(i*30) for i in range(3)]
    def parse(self, response):
        movie_name = response.xpath("//div[@class='channel-detail movie-item-title']/a/text()").extract()
        movie_score = [div.xpath('string(.)').extract_first() for div in response.xpath("//div[@class='channel-detail channel-detail-orange']")]
        for name,score in zip(movie_name,movie_score):
            yield {
                'name':name,
                'score':score,
            }
