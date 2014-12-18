from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from douban.items import DoubanmovieItem
from scrapy.http import HtmlResponse
import re
 
class MovieMainSpider(CrawlSpider):
    name = "MovieMain"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "http://movie.douban.com/tag/"
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
 
 
    