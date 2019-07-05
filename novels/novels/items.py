# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    content = scrapy.Field()
    num = scrapy.Field()
    book_name = scrapy.Field()
    book_image_url = scrapy.Field()
    author = scrapy.Field()
    intro = scrapy.Field()
    desp = scrapy.Field()