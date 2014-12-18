#流程：使用xpath找到分类，根据分类爬取电影信息
#sel.xpath("//div[@class='article']/table[1]//a").extract()#找分类
#sel.xpath("//tr[@class='item']//a/@href").extract()#电影链接
#sel.xpath("//span[@class='next']/link/@href").extract()#下一页
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from douban.items import DoubanmovieItem
from scrapy.http import HtmlResponse
import re

class testmoviespider(CrawlSpider)
    name ="test"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        http://movie.douban.com/subject/25779218/
        ]

def movie_parse(self.response)
    for sel in response.xpath("/body/div[@id='content']")
        item = DoubanmovieItem()
        item('MovieTitle') = sel.xpath("/h1/span[@property='v:itemreviewed']/text()").extract()
        item('MovieYear') = sel.xpath("/h1/span[@class='year']/text()").extract()
        item('MovieDirector') = sel.xpath("//div[@id='info']/span[1]/span[@class='attrs']/a").extract()
        item('MovieGenre') = sel.xpath("//div[@id='info']//span[@property='v:genre']/a").extract()
        item('MovieLang') = sel.xpath("//div[@id='info']//span[7]/following-sibling::text()[1]").extract()
        item('MovieLocal') = sel.xpath("//div[@id='info']//span[6]/following-sibling::text()[1]").extract()
        item('MovieShort')
        item('MovieLong') = sel.xpath("//div[@id='info']//span[@property='v:runtime']/@content").extract()
        item('MovieVoteScore')
        item('MovieVoteNumber')
        sel.xpath("//div[@id='info']//span[6]/text()").extract()