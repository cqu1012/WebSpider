# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
class ImgzolPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # return [Request(x) for x in item.get(self.images_urls_field, [])]
        #传递文件名
        yield Request(item['image_url'],meta={'name':item['image_name']})
    def file_path(self, request, response=None, info=None):
        #设置文件名
        name = request.meta['name']
        name = name.replace('/','_')
        return name+'.jpg'
    #     pass
