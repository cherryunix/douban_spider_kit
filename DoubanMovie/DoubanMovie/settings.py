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

SPIDER_MIDDLEWARES = {

    'scrapy.dupefilter.RFPDupeFilter': 543,   
}

DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = False
