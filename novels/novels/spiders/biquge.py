# -*- coding: utf-8 -*-
import scrapy


class BiqugeSpider(scrapy.Spider):
    name = "biquge"
    allowed_domains = ["biquge5.com"]
    start_urls = ['http://biquge5.com/']

    def parse(self, response):
        pass
