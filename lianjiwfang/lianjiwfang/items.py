# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiwfangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class chengduItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    title = scrapy.Field()
    image = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    label = scrapy.Field()
    price = scrapy.Field()
    addr_area = scrapy.Field()
    addr_landmark = scrapy.Field()
    addr_detail = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
