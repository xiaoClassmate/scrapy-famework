# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MizunoItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Code = scrapy.Field()
    Sports = scrapy.Field()
    Price = scrapy.Field()
    Size = scrapy.Field()
    Colors = scrapy.Field()
    RatingValue = scrapy.Field()
    RatingCount = scrapy.Field()
    Material = scrapy.Field()
    Feature = scrapy.Field()
    
