# -*- coding: utf-8 -*-
import pymongo
from douban.settings import MONGODB_HOST, MONGODB_NAME, MONGODB_PROT, MONGODB_COLLECTION

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        host = MONGODB_HOST
        port = MONGODB_PROT
        name = MONGODB_NAME
        sheetname = MONGODB_COLLECTION
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[name]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        print(item)
        data = dict(item)
        self.post.insert(data)
        return item
