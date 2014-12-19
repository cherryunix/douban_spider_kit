from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from DoubanMovie.items import DoubanmovieItem
from scrapy.http import HtmlResponse
import re
 
#流程：使用xpath找到分类，根据分类爬取电影信息
#sel.xpath("//div[@class='article']/table[1]//a").extract()#找分类
#sel.xpath("//tr[@class='item']//a/@href").extract()#电影链接
#sel.xpath("//span[@class='next']/link/@href").extract()#下一页

class MovieMainSpider(CrawlSpider):
    name = "MovieMain"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["http://movie.douban.com/tag/%E7%88%B1%E6%83%85",
        "http://movie.douban.com/tag/%E5%96%9C%E5%89%A7",
        "http://movie.douban.com/tag/%E5%8A%A8%E7%94%BB",
        "http://movie.douban.com/tag/%E7%A7%91%E5%B9%BB",
        "http://movie.douban.com/tag/%E7%BB%8F%E5%85%B8",
        "http://movie.douban.com/tag/%E5%89%A7%E6%83%85",
        "http://movie.douban.com/tag/%E5%8A%A8%E4%BD%9C",
        "http://movie.douban.com/tag/%E9%9D%92%E6%98%A5",
        "http://movie.douban.com/tag/%E6%82%AC%E7%96%91",
        "http://movie.douban.com/tag/%E6%83%8A%E6%82%9A",
        "http://movie.douban.com/tag/%E7%8A%AF%E7%BD%AA",
        "http://movie.douban.com/tag/%E7%BA%AA%E5%BD%95%E7%89%87",
        "http://movie.douban.com/tag/%E6%96%87%E8%89%BA",
        "http://movie.douban.com/tag/%E5%8A%B1%E5%BF%97",
        "http://movie.douban.com/tag/%E6%90%9E%E7%AC%91",
        "http://movie.douban.com/tag/%E6%81%90%E6%80%96",
        "http://movie.douban.com/tag/%E7%9F%AD%E7%89%87",
        "http://movie.douban.com/tag/%E6%88%98%E4%BA%89",
        "http://movie.douban.com/tag/%E9%AD%94%E5%B9%BB",
        "http://movie.douban.com/tag/%E9%BB%91%E8%89%B2%E5%B9%BD%E9%BB%98",
        "http://movie.douban.com/tag/%E5%8A%A8%E7%94%BB%E7%9F%AD%E7%89%87",
        "http://movie.douban.com/tag/%E6%83%85%E8%89%B2",
        "http://movie.douban.com/tag/%E4%BC%A0%E8%AE%B0",
        "http://movie.douban.com/tag/%E6%84%9F%E4%BA%BA",
        "http://movie.douban.com/tag/%E6%9A%B4%E5%8A%9B",
        "http://movie.douban.com/tag/%E7%AB%A5%E5%B9%B4",
        "http://movie.douban.com/tag/%E9%9F%B3%E4%B9%90",
        "http://movie.douban.com/tag/%E5%90%8C%E5%BF%97",
        "http://movie.douban.com/tag/%E9%BB%91%E5%B8%AE",
        "http://movie.douban.com/tag/%E6%B5%AA%E6%BC%AB",
        "http://movie.douban.com/tag/%E5%A5%B3%E6%80%A7",
        "http://movie.douban.com/tag/%E5%AE%B6%E5%BA%AD",
        "http://movie.douban.com/tag/%E5%8F%B2%E8%AF%97",
        "http://movie.douban.com/tag/%E7%AB%A5%E8%AF%9D",
        "http://movie.douban.com/tag/%E7%83%82%E7%89%87",
        "http://movie.douban.com/tag/cult"
    ]
 
    rules = [
        
    ]
 
    def __get_id_from_movie_url(self, url):
        m =  re.search("^http://movie.douban.com/subject/([^/]+)/$", url)
        if(m):
            return m.group(1) 
        else:
            return 0
 
 
 
    def add_cookie(self, request):
        request.replace(cookies=[
 
        ]);
        return request;
 
    def parse_group_topic_list(self, response):
        self.log("Fetch group topic list page: %s" % response.url)
        pass
