# -*- coding: utf-8 -*-


BOT_NAME = 'hao'

SPIDER_MODULES = ['hao.spiders']
NEWSPIDER_MODULE = 'hao.spiders'

USER_AGENT_CHOICES = [
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
    'DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)',
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
    'ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)',
]

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 3

CONCURRENT_REQUESTS_PER_DOMAIN = 16
DOWNLOADER_MIDDLEWARES = {
    'hao.middlewares.RotateUserAgentMiddleware': 110,
}


ITEM_PIPELINES = {
    'hao.pipelines.MongoDBPipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 300
}
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "51hao"


# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

#DEPTH_LIMIT = 1
