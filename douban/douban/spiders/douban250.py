# -*- coding: utf-8 -*-
import scrapy

# from douban.douban.items import DoubanItem
from .items import DoubanItem


class Douban250Spider(scrapy.Spider):
    name = 'douban250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movieList=response.xpath("//div/a/span[@class='title'][1]/text()").extract()
        scoreList = response.xpath("//span[@class='rating_num']/text()").extract()
        for movie,score in zip(movieList,scoreList):
            # print(movie,score)
            #保存到item中
            dbmovie =  DoubanItem()
            dbmovie['movie_name'] = movie
            dbmovie['movie_score'] =score
            yield dbmovie
            #推送到pipelines
            # yield {
            #     'movie':movie,
            #     'score':score,
            # }
