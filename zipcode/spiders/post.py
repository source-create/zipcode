# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.selector import Selector


class PostSpider(scrapy.Spider):
    name = "post"
    allowed_domains = ["post.japanpost.jp"]
    start_urls = ['http://www.post.japanpost.jp/zipcode/']

    def parse(self, response):
    	response = HtmlResponse(url='http://www.post.japanpost.jp/zipcode/', body=response.body)
    	link=response.css('.areaTxt a').xpath('@href').extract()
    	for url in link:
    		scrapy.Request('http://google.com', callback=self.parse_link)
  

    def parse_link(self,response):
    	#response = HtmlResponse(url='http://www.post.japanpost.jp/zipcode/', body=response.body)
    	print "Test\n"

