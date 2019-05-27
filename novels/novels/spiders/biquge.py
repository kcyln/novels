# -*- coding: utf-8 -*-
import scrapy
import re
from novels.items import NovelsItem
import time

class BiqugeSpider(scrapy.Spider):
    name = "biquge"
    allowed_domains = ["biqudu.com"]
    start_urls = ['https://www.biqudu.com/43_43821/']

    def parse(self, response):
        num = 0
        links = response.xpath("//dt[2]/following-sibling::dd/a/@href").extract()
        for link in links:
            link = "https://www.biqudu.com" + link
            # time.sleep(0.5)
            num += 1
            yield scrapy.Request(link, callback=self.parse_detail, meta={"num": num})
    
    def parse_detail(self, response):
        
        item = NovelsItem()
        item['num'] = response.meta['num']
        item['name'] = response.xpath("//h1/text()").extract_first()
        item['content'] = response.css("#content").extract_first()
        yield item
