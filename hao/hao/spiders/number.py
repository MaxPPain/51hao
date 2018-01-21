# coding:utf-8
import re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from hao.items import PhoneItem
class MySpider(CrawlSpider):
    name = 'hao'
    allowed_domains = ['www.51hao.cc']
    start_urls = ['http://www.51hao.cc/city/jiangsu/nanjing.php']
    rules = (
        Rule(LinkExtractor(allow=(r'http://www.51hao.cc/mobile/nanjing_\d{7}.html')), callback='parse_item'),
    )
    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        phone_list = re.findall("\d{11}", str(response.body), re.I)
        if phone_list:
            for phone in phone_list:
                item = PhoneItem()
                item['phone'] = phone
                yield item
