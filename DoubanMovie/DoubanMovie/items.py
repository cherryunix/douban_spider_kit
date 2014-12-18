# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    MovieTitle = scrapy.Field()
    MovieDirector = scrapy.Field()
    MovieGenre = scrapy.Field()
    MovieLang = scrapy.Field()
    MovieLocal = scrapy.Field()
    MovieShort = scrapy.Field()
    MovieLong = scrapy.Field()
    MovieVoteScore = scrapy.Field()
    MovieVoteNumber = scrapy.Field()
