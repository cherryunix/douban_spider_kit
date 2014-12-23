# -*- coding: utf-8 -*-

# Scrapy settings for DoubanMovie project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'DoubanMovie'

SPIDER_MODULES = ['DoubanMovie.spiders']
NEWSPIDER_MODULE = 'DoubanMovie.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DoubanMovie (+http://www.yourdomain.com)'

# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
    # Fix path to this module
    'DoubanMovie.randomproxy.RandomProxy': 100,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
    'DoubanMovie.rotate_useragent.RotateUserAgentMiddleware' :400
}

PROXY_LIST = '/DoubanMovie/data/proxy_list.txt'

SPIDER_MIDDLEWARES = {

    'scrapy.dupefilter.RFPDupeFilter': 543,   
}

DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLED = False
