# -*- coding: utf-8 -*-
import scrapy
from smallcrawler.items import SmallcrawlerItem
import time

starttime = time.time()
class SmallcrawlerSpiderSpider(scrapy.Spider):
    name = 'smallcrawler_spider'
    start_urls = ['http://www.jumei.com']

    def parse(self, response):
        endtime = time.time()
        responsetime = endtime - starttime
        item = SmallcrawlerItem()
        hrefs = response.xpath("//a/@href").extract()

        title = response.xpath("//title/text()").extract()

        for index,href in enumerate(hrefs):

            item['title'] = str(title).strip()
            item['starturl'] = response.url
            item['order'] = index+1
            item['href'] = href
            item['time'] = responsetime
            yield item
            yield scrapy.Request(item['href'],callback=self.parse)