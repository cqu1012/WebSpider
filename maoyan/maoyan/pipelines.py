# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class MaoyanPipeline(object):
    def open_spider(self,spider):
        #获取链接数据库对象
        self.client = MongoClient('localhost',27017)
        #获取数据库实例
        self.db = self.client.db
        #获取集合
        self.movie = self.db.movie
    def close_spider(self,spider):
        self.client.close()
    def process_item(self, item, spider):
        self.movie.insert(item)
        return item
import pymysql
class MaoyanPipelineMysql(object):
    def open_spider(self,spider):
        config = {
            'db': 'maoyanmovies',
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'123456',
            'charset':'utf8'
        }
        # #获取链接数据库对象
        self.db = pymysql.connect(**config)
        #获取集合
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):
        # for name,score in item.items():
        # sql = 'insert into movies values(0,{},{})'
        # self.cursor.execute(sql.format(item['name'],item['score']))
        sql = 'insert into movies values(0,%s,%s)'
        self.cursor.execute(sql,[item['name'],item['score']])
        self.db.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()

