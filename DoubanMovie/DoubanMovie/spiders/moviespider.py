# coding=gbk
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from DoubanMovie.items import DoubanmovieItem
from DoubanMovie.items import DoubanTagInfo
from scrapy.http import HtmlResponse
import re
 
#流程：使用xpath找到分类，根据分类爬取电影信息
#sel.xpath("//div[@class='article']/table[1]//a").extract()#找分类
#sel.xpath("//tr[@class='item']//a/@href").extract()#电影链接
#sel.xpath("//span[@class='next']/link/@href").extract()#下一页

class MovieMainSpider(CrawlSpider):
    name = "MovieMain"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["http://movie.douban.com/tag/%E7%88%B1%E6%83%85?start=0&type=T",
        "http://movie.douban.com/tag/%E5%96%9C%E5%89%A7?start=0&type=T",
        "http://movie.douban.com/tag/%E5%8A%A8%E7%94%BB?start=0&type=T",
        "http://movie.douban.com/tag/%E7%A7%91%E5%B9%BB?start=0&type=T",
        "http://movie.douban.com/tag/%E7%BB%8F%E5%85%B8?start=0&type=T",
        "http://movie.douban.com/tag/%E5%89%A7%E6%83%85?start=0&type=T",
        "http://movie.douban.com/tag/%E5%8A%A8%E4%BD%9C?start=0&type=T",
        "http://movie.douban.com/tag/%E9%9D%92%E6%98%A5?start=0&type=T",
        "http://movie.douban.com/tag/%E6%82%AC%E7%96%91?start=0&type=T",
        "http://movie.douban.com/tag/%E6%83%8A%E6%82%9A?start=0&type=T",
        "http://movie.douban.com/tag/%E7%8A%AF%E7%BD%AA?start=0&type=T",
        "http://movie.douban.com/tag/%E7%BA%AA%E5%BD%95%E7%89%87?start=0&type=T",
        "http://movie.douban.com/tag/%E6%96%87%E8%89%BA?start=0&type=T",
        "http://movie.douban.com/tag/%E5%8A%B1%E5%BF%97?start=0&type=T",
        "http://movie.douban.com/tag/%E6%90%9E%E7%AC%91?start=0&type=T",
        "http://movie.douban.com/tag/%E6%81%90%E6%80%96?start=0&type=T",
        "http://movie.douban.com/tag/%E7%9F%AD%E7%89%87?start=0&type=T",
        "http://movie.douban.com/tag/%E6%88%98%E4%BA%89?start=0&type=T",
        "http://movie.douban.com/tag/%E9%AD%94%E5%B9%BB?start=0&type=T",
        "http://movie.douban.com/tag/%E9%BB%91%E8%89%B2%E5%B9%BD%E9%BB%98?start=0&type=T",
        "http://movie.douban.com/tag/%E5%8A%A8%E7%94%BB%E7%9F%AD%E7%89%87?start=0&type=T",
        "http://movie.douban.com/tag/%E6%83%85%E8%89%B2?start=0&type=T",
        "http://movie.douban.com/tag/%E4%BC%A0%E8%AE%B0?start=0&type=T",
        "http://movie.douban.com/tag/%E6%84%9F%E4%BA%BA?start=0&type=T",
        "http://movie.douban.com/tag/%E6%9A%B4%E5%8A%9B?start=0&type=T",
        "http://movie.douban.com/tag/%E7%AB%A5%E5%B9%B4?start=0&type=T",
        "http://movie.douban.com/tag/%E9%9F%B3%E4%B9%90?start=0&type=T",
        "http://movie.douban.com/tag/%E5%90%8C%E5%BF%97?start=0&type=T",
        "http://movie.douban.com/tag/%E9%BB%91%E5%B8%AE?start=0&type=T",
        "http://movie.douban.com/tag/%E6%B5%AA%E6%BC%AB?start=0&type=T",
        "http://movie.douban.com/tag/%E5%A5%B3%E6%80%A7?start=0&type=T",
        "http://movie.douban.com/tag/%E5%AE%B6%E5%BA%AD?start=0&type=T",
        "http://movie.douban.com/tag/%E5%8F%B2%E8%AF%97?start=0&type=T",
        "http://movie.douban.com/tag/%E7%AB%A5%E8%AF%9D?start=0&type=T",
        "http://movie.douban.com/tag/%E7%83%82%E7%89%87?start=0&type=T",
        "http://movie.douban.com/tag/cult?start=0&type=T"
    ]
 
    rules = (
            Rule(LinkExtractor(allow=('tag/.+?start=[0-9]+',)),callback='get_tag_page'),
            Rule(LinkExtractor(allow=('subject/[0-9]+/',),deny=('[0-9]+/.+')),callback='get_movie_page_info'),
        )


    def get_tag_page_parse(self,response):
        item = DoubanTagInfo()
        sel = Selector(response)
        moviepool = sel.xpath("//div[@class='article']//tr[@class='item]//div[@class='pl2']'")
        for movie in moviepool:
            movieurl = movie.xpath("//a/@href").extract()
            urlpool.append(moviepool)
        nexturl = sel.xpath("//span[@class='next']/link/@href").extract()
        urlpool.append(nextpool)
        return urlpool


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
        item['MovieLang'] = response.xpath("//div[@id='info']//span[6+count]/following-sibling::text()[1]").extract()
        item['MovieLocal'] = response.xpath("//div[@id='info']//span[5+count]/following-sibling::text()[1]").extract()
        item['MovieShort'] = response.xpath("//div[@id='comments-section']//h2/span[@class='pl']/a").extract()
        item['MovieLeng'] = response.xpath("//div[@id='info']//span[@property='v:runtime']/@content").extract()
        item['MovieLong'] = response.xpath("//div[@id='review_section']//span[@class='pl']/a/text()").extract()
        item['MovieVoteScore'] = response.xpath("//div[@class='rating_wrap clearbox']/p[1]/strong/text()").extract()
        item['MovieVoteNumber'] = response.xpath("//div[@class='rating_wrap clearbox']/p[2]//span/text()").extract()
        yield item
