# coding=gbk
#流程：使用xpath找到分类，根据分类爬取电影信息
#sel.xpath("//div[@class='article']/table[1]//a").extract()#找分类
#sel.xpath("//tr[@class='item']//a/@href").extract()#电影链接
#sel.xpath("//span[@class='next']/link/@href").extract()#下一页
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from DoubanMovie.items import DoubanmovieItem
from scrapy.http import HtmlResponse
import re

class testmoviespider(CrawlSpider):
    name ="test"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "http://movie.douban.com/subject/25779218/"
        ]

def movie_parse(self,response):
        item = DoubanmovieItem()
        item['MovieTitle'] = response.xpath("//h1/span[@property='v:itemreviewed']/text()").extract()
        MovieTitle = response.xpath("//h1/span[@property='v:itemreviewed']/text()").extract()
        item['MovieYear'] = response.xpath("//h1/span[@class='year']/text()").extract()
        item['MovieDirector'] = response.xpath("//div[@id='info']/span[1]/span[@class='attrs']/a").extract()
        item['MovieGenre'] = response.xpath("//div[@id='info']//span[@property='v:genre']/a").extract()
        item['MovieLang'] = response.xpath("//div[@id='info']//span[7]/following-sibling::text()[1]").extract()
        item['MovieLocal'] = response.xpath("//div[@id='info']//span[6]/following-sibling::text()[1]").extract()
        item['MovieShort'] = response.xpath("//div[@class='mod-hd']//h2/span[@class='pl']/a").extract()
        item['MovieLeng'] = response.xpath("//div[@id='info']//span[@property='v:runtime']/@content").extract()
        item['MovieLong'] = response.xpath("//a[@class='comment_btn'/h2/span[@class='pl']/a").extract()
        item['MovieVoteScore'] = response.xpath("//div[@class='rating_wrap clearbox']/p[1]/strong/text()").extract()
        item['MovieVoteNumber'] = response.xpath("//div[@class='rating_wrap clearbox']/p[2]//span/text()").extract()
        return item