# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VnexpressItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    body = scrapy.Field()
    category = scrapy.Field()
    pass
