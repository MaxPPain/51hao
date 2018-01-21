# -*- coding: utf-8 -*-
import logging
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = connection[settings['MONGODB_DB']]


    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            try:
                self.db.phone.insert(dict(item))
            except Exception as err:
                raise DropItem("Duplicated Item: {}".format(item['phone']))
        return item

