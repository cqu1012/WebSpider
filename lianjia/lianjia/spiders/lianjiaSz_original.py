# -*- coding: utf-8 -*-
import scrapy
import re

from lianjia.items import LianjiaItem


class LianjiaszSpider(scrapy.Spider):
    name = 'lianjiaSz'
    allowed_domains = ['sz.lianjia.com']
    start_urls = ['https://sz.lianjia.com/zufang/pg{}rt200600000002/'.format(i) for i in range(1)]

    def parse(self, response):
        url_list = response.xpath("//div[@class='content__list--item--main']/p[1]/a/@href").extract()
        for url in url_list:
            #过滤公寓类型房屋
            if re.match(r'/zufang/',url):
                yield scrapy.Request(response.urljoin(url),callback=self.getInfo)

    def getInfo(self,response):
        #租房标题
        title  = response.xpath("//p[@class='content__title']/text()").extract_first()
        #租房价格
        price = response.xpath("string(//p[@class='content__aside--title'])").extract_first()
        #地址
        location = response.xpath("string(//div[@class= 'content__article__info4']/ul/li[1])").extract_first().strip().replace('\n            ','')
        #租房信息
        base_Info = response.xpath("//p[@class='content__article__table']")
        rent_way = base_Info.xpath("./span[1]/text()").extract_first()
        rent_type = base_Info.xpath("./span[2]/text()").extract_first()
        rent_area = base_Info.xpath("./span[3]/text()").extract_first()
        rent_dire = base_Info.xpath("./span[4]/text()").extract_first()
        #楼层与电梯
        floor = response.xpath("//div[@class='content__article__info']/ul/li[8]/text()").extract_first()
        elevator = response.xpath("//div[@class='content__article__info']/ul/li[last()-8]/text()").extract_first()
        if elevator == None:
            elevator='暂无数据'
        if floor == None:
            floor ='暂无数据'
        items = LianjiaItem()
        items['title'] = title
        items['price'] = price
        items['location'] = location
        items['rent_way'] = rent_way
        items['rent_type'] = rent_type
        items['rent_area'] = rent_area
        items['rent_dire'] = rent_dire
        items['floor'] = floor
        items['elevator'] = elevator
        yield items

