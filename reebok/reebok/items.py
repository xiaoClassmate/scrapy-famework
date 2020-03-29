# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReebokItem(scrapy.Item):
    # define the fields for your item here like:
    Sport = scrapy.Field()
    Name = scrapy.Field()
    MinPrice = scrapy.Field()
    MaxPrice = scrapy.Field()
    Color = scrapy.Field()
    Size = scrapy.Field()
    StyleNumber = scrapy.Field()
    Feature = scrapy.Field()
    Material = scrapy.Field()
    ImageUrl = scrapy.Field()
    AverageRating = scrapy.Field()
    ReviewNumber = scrapy.Field()
    Gender = scrapy.Field()
    pass
