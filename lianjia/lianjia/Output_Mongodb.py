# -*- coding: utf-8 -*-
import redis
import pymongo
import json
def main():
    #与redis数据库建立连接
    r = redis.Redis(host='192.168.137.1', port=6379,db=0)
    #与Mongo数据库建立连接
    client = pymongo.MongoClient(host='localhost',port=27017)
    #获得Mongo数据库
    db  = client.db
    #获得Mongo集合
    lianjia = db.lianjia

    while True:
        #从redis中提取出需要的数据，source是Key，date是value
        source,data = r.blpop('lianjiaSz:items')
        #转换为字典类型
        item = json.loads(data)
        #插入Mongo数据库
        lianjia.insert(item)

if __name__ ==  '__main__':
    main()
