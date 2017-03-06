# -*- coding: utf-8 -*-
import scrapy


class PostSpider(scrapy.Spider):
    name = "post"
    allowed_domains = ["post.japanpost.jp"]
    start_urls = ['http://www.post.japanpost.jp/zipcode/']

    def parse(self, response):
    	page = response.url.split("/")[-2]
        filename = 'crawl-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
