# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodScItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FoodItem(scrapy.Item):
    df = scrapy.Field()
    lines = scrapy.Field()
    name = scrapy.Field()
