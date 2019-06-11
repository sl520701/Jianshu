# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem
import time

class JianshuSpiderSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/p/5ed0a7ec99e2']

    rules = (
        Rule(LinkExtractor(allow=r'.+/p/[a-z0-9]+'), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        title = response.xpath("//div[@class='article']/h1[@class='title']/text()").get()
        author = response.xpath("//div[@class='info']/span[@class='name']/a/text()").get()
        publish_time = response.xpath("//div[@class='meta']/span[@class='publish-time']/text()").get()
        word = response.xpath("//div[@class='meta']/span[@class='wordage']/text()").get()
        content = response.xpath("//div[@class='show-content-free']/p//text()").getall()
        content = "".join(content).replace("\u3000", "").replace("\xa0", "").strip()
        url = response.url
        id = url.split("?")[0].split("/")[-1]
        view_count = response.xpath("//div[@class='meta']/span[@class='view-count']/text()").get()
        comment_count = response.xpath("//div[@class='meta']/span[@class='comments-count']/text()").get()
        like_count = response.xpath("//div[@class='meta']/span[@class='likes-count']/text()").get()
        reward_count = response.xpath("//div[@class='meta']/span[@class='rewards-count']/text()").get()
        item = JianshuItem(title=title, author=author, publish_time=publish_time, word=word, content=content,
                           url=url,id=id, view_count=view_count,comment_count=comment_count, like_count=like_count, reward_count=reward_count)
        yield item

