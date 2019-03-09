# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from json import dumps

class DoubanPipeline(object):
    #打开爬虫执行此方法
    def open_spider(self,spider):
        self.filename = open('movie.txt','w',encoding='utf-8')
    #关闭爬虫执行此方法
    def close_spider(self,spider):
        self.filename.close()
    #爬虫过程方法
    def process_item(self, item, spider):
        #yield到pipelines用该方法
        # self.filename.write(dumps(item,ensure_ascii=False)+'\n')
        #保存到items类中用该方法
        self.filename.write(dumps(dict(item),ensure_ascii=False)+'\n')

        return item
