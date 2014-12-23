# -*- coding: utf-8 -*-
#流程：使用xpath找到分类，根据分类爬取电影信息
#sel.xpath("//div[@class='article']/table[1]//a").extract()#找分类
#sel.xpath("//tr[@class='item']//a/@href").extract()#电影链接
#sel.xpath("//span[@class='next']/link/@href").extract()#下一页
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from DoubanMovie.items import DoubanmovieItem,DoubanTagInfo,UrlLink
from scrapy.http import HtmlResponse
import re

class testmoviespider(CrawlSpider):
    name ="test"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["http://movie.douban.com/tag/%E5%8A%A8%E4%BD%9C?start=0&type=T",
        "http://movie.douban.com/tag/%E9%9D%92%E6%98%A5?start=0&type=T",
        "http://movie.douban.com/tag/%E6%82%AC%E7%96%91?start=0&type=T",
        "http://movie.douban.com/tag/%E6%83%8A%E6%82%9A?start=0&type=T",
        "http://movie.douban.com/tag/%E7%8A%AF%E7%BD%AA?start=0&type=T",
        "http://movie.douban.com/tag/%E7%BA%AA%E5%BD%95%E7%89%87?start=0&type=T"
        ]
    
    rules = (
            Rule(LinkExtractor(allow=('tag/.+',)),callback='parse'),
            Rule(LinkExtractor(allow=('subject/[0-9]+/',),deny=('[0-9]+/.+')),callback='get_movie_page_info'),
        )

    def parse(self,response):
        sel = Selector(response)
        moviepool = sel.xpath("//div[@class='']//div[@class='pl2']//a/@href").extract()
        for url in moviepool:
            yield self.make_requests_from_url(url).replace(callback=self.get_movie_page_info)
        nexturl = sel.xpath("//div[@class='paginator']/span[@class='next']/link/@href").extract()
        if len(nexturl)>0:
            yield self.make_requests_from_url(nexturl[0])
        

    def get_movie_page_info(self,response):
        item = DoubanmovieItem()
        sel = Selector(response)
        item['MovieTitle'] = response.xpath("//h1/span[@property='v:itemreviewed']/text()").extract()
        item['MovieYear'] = response.xpath("//h1/span[@class='year']/text()").extract()
        item['MovieDirector'] = response.xpath("//div[@id='info']/span[1]/span[@class='attrs']/a").extract()
        genres = sel.xpath("//div[@id='info']//span[@property='v:genre']")
        item['MovieGenre']=[]
        count = 0
        for genre in genres:
            count+1
            mgenre = genre.xpath("text()").extract()
            item['MovieGenre'].append(mgenre)
        langpath = "//div[@id='info']//span[6+%s]/following-sibling::text()[1]" %count
        localpath = "//div[@id='info']//span[5+%s]/following-sibling::text()[1]" %count
        item['MovieLang'] = response.xpath(langpath).extract() 
        item['MovieLocal'] = response.xpath(localpath).extract()
        item['MovieShort'] = response.xpath("//div[@id='comments-section']//h2/span[@class='pl']/a").extract()
        item['MovieLeng'] = response.xpath("//div[@id='info']//span[@property='v:runtime']/@content").extract()
        item['MovieLong'] = response.xpath("//div[@id='review_section']//span[@class='pl']/a/text()").extract()
        item['MovieVoteScore'] = response.xpath("//div[@class='rating_wrap clearbox']/p[1]/strong/text()").extract()
        item['MovieVoteNumber'] = response.xpath("//div[@class='rating_wrap clearbox']/p[2]//span/text()").extract()
        yield item