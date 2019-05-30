# -*- coding: utf-8 -*-
import scrapy
import re
from novels.items import NovelsItem
import time

class BiqugeSpider(scrapy.Spider):
    name = "biquge"
    allowed_domains = ["biqudu.com"]
    start_urls = ['https://www.biqudu.com/xuanhuanxiaoshuo/']

    def parse(self, response):
        cate_li = response.css(".r li .s2 a::attr(href)").extract()
        for cate in cate_li:
            cate = "https://www.biqudu.com" + cate
            yield scrapy.Request(cate, callback=self.parse_list)
    
    def parse_list(self, response):
        """获取章节列表"""
        num = 0  # 利用num对小说章节进行排序
        item = NovelsItem()
        item["book_name"] = response.xpath("//h1/text()").extract_first()
        item["author"] = response.xpath("//div[@id='info']/p[1]/text()").extract_first().replace("作\xa0\xa0\xa0\xa0者：", "")
        item["desp"] = response.xpath("//div[@id='intro']").extract()
        item["desp"] = " ".join(item["desp"])
        links = response.xpath("//dt[2]/following-sibling::dd/a/@href").extract()
        for link in links:
            link = "https://www.biqudu.com" + link
            num += 1
            # item["num"] = num
            yield scrapy.Request(link, callback=self.parse_detail, meta={"item": item, "num": num})


    def parse_detail(self, response):
        """获取章节内容"""
        item = response.meta['item']
        item["num"] = response.meta['num']
        item['name'] = response.xpath("//h1/text()").extract_first()
        item['content'] = response.css("#content").extract_first()
        yield item
