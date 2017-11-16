# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json

class SmallcrawlerPipeline(object):

    def __init__(self):
        self.crawledHrefs = set()

    def process_item(self, item, spider):
        if item['href'] in self.crawledHrefs:
            raise DropItem("duplicate href founded %s" % item['href'])
        else:
            self.crawledHrefs.add(item['href'])
            with open("result.json",'a') as f:

                json.dump(dict(item),f,ensure_ascii=False)
                f.write(',\n')

            return item