# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
class LianjiaPipeline(object):
    def open_spider(self,spider):
        #创建客户端
        self.client = MongoClient('localhost',27017)
        #获得数据库
        self.db = self.client.db
        #获得集合(数据库表)
        self.lianjia = self.db.lianjiaInfo
    def close_spider(self,spider):
        self.client.close()
    def process_item(self, item, spider):
        self.lianjia.insert(dict(item))
        return item
