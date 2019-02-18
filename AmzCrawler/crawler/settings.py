from os import path, sep

# 数据库URI
SQLITE_DB_URI = '%sdata.db'% (sep.join(path.dirname(path.realpath(__file__)).split(sep)[:-1])+sep)



BOT_NAME = 'amazon'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# 日志级别
LOG_LEVEL = 'WARN'

# 默认用户代理
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'

# 默认请求头信息
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# 下载延迟时间
DOWNLOAD_DELAY = 3

# 初始下载延迟
AUTOTHROTTLE_START_DELAY = 3

# 最大延迟时间
AUTOTHROTTLE_MAX_DELAY = 10

# 开启Cookie
COOKIES_ENABLED = True

# 管道控制
ITEM_PIPELINES = {
   'crawler.pipelines.AmazonPipeline': 300,
}

# 下载中间件
DOWNLOADER_MIDDLEWARES = {
   'crawler.middlewares.RandomUserAgentMiddleware': 543,
}


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 16


# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16


# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'taobao.middlewares.TaobaoSpiderMiddleware': 543,
#}


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True


# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
