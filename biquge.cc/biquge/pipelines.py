# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BiqugePipeline(object):
    def open_spider(self,spider):
        self.filename = open('文艺青年.txt','w',encoding='utf-8')
    def close_spider(self,spider):
        self.filename.close()
    def process_item(self, item, spider):
        txtContent = item['title'] + '\n' +item['content'] + '\n'
        self.filename.write(txtContent)
        self.filename.flush()
        return item
