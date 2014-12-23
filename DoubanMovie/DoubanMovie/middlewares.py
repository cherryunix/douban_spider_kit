import random

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        fd = open('~/DoubanSpiderKit/DoubanMovie/DoubanMovie/data/proxy_list.txt','r')
        data = fd.readlines()
        fd.close()
        length = len(data)
        index  = random.randint(0, length -1)
        item   = data[index]
        arr    = item.split(' ')
        request.meta['proxy'] = 'http://%s:%s' % (arr[0],arr[1])