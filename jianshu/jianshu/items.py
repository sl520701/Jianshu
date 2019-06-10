# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    publish_time = scrapy.Field()
    word = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()
    view_count = scrapy.Field()
    comment_count = scrapy.Field()
    like_count = scrapy.Field()
    reward_count = scrapy.Field()
