# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SmallcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    order = scrapy.Field()
    href = scrapy.Field()
    time = scrapy.Field()
    starturl = scrapy.Field()
    title = scrapy.Field()

