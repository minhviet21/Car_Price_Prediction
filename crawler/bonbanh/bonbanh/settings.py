# Scrapy settings for bonbanh project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "bonbanh"

SPIDER_MODULES = ["bonbanh.spiders"]
NEWSPIDER_MODULE = "bonbanh.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "bonbanh (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "bonbanh.middlewares.BonbanhSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
'''DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

ROTATING_PROXY_LIST = [
"69.163.165.253:47876",
    "51.83.135.35:2846",
    "177.38.5.192:4153",
    "213.96.98.213:15724",
    "188.68.236.126:3128",
    "178.63.0.115:30510",
    "177.105.67.205:4153",
    "195.2.71.201:16072",
    "94.28.14.70:4145",
    "185.66.59.192:42647",
    "83.17.222.146:5678",
    "77.192.165.202:5678",
    "177.128.120.85:5678",
    "110.77.232.172:4145",
    "197.234.13.27:4145",
    "134.236.59.240:4145",
    "188.72.6.98:50321",
    "38.127.172.23:11537",
    "164.90.160.201:3128",
    "123.200.9.30:5678",
    "84.236.32.196:8080",
    "188.255.244.5:1080",
    "185.220.226.108:3128",
    "166.62.85.224:61760",
    "109.73.181.133:4145",
    "212.33.205.4:1080",
    "185.184.197.101:5678",
    "8.210.62.161:10020",
    "177.38.5.250:4153",
    "178.62.79.49:16614",
    "88.12.54.146:1081",
    "103.59.190.2:56252",
    "190.109.72.33:33633",
    "117.241.135.30:7777",
    "197.234.13.97:4145",
    "128.14.226.130:60080",
    "95.0.206.211:10820",
    "210.179.101.88:3128",
    "188.255.245.205:1080",
    "85.116.120.106:3629",
    "198.89.91.198:5678",
    "186.251.255.73:31337",
    "39.187.83.37:1080",
    "103.210.35.62:4145",
    "104.25.108.120:80",
    "1.1.1.18:80",
    "137.220.53.12:10544",
    "197.234.13.70:4145",
    "37.252.86.97:5678",
    "68.183.111.115:14061",
    "45.112.125.53:4145",
    "112.2.34.103:10800",
    "172.105.251.72:4003",
    "191.102.135.67:3128",
    "188.214.129.3:4048",
    "86.57.181.122:51801",
    "179.96.142.75:5678",
    "95.140.124.217:1080",
    "143.255.249.74:7497",
    "185.32.44.157:4153",
    "66.42.63.207:13802",
    "91.90.16.211:1080",
    "183.88.122.200:8080",
    "122.248.46.253:4145",
    "202.40.188.201:4145",
    "46.161.196.174:4145",
    "76.120.215.137:4252",
    "177.38.5.230:4153",
    "185.105.237.11:3128",
    "101.51.105.245:4145",
    "185.81.153.162:3389",
    "43.129.233.215:23863",
    "116.58.232.91:4145",
    "194.31.33.50:1080",
    "67.43.42.117:8080",
    "103.81.117.225:4153",
    "128.199.150.88:64054",
    "93.87.73.58:1080",
    "103.79.96.225:4153",
    "138.117.179.54:5678",
    "64.25.54.2:45160",
    "93.171.224.53:4153",
    "182.253.158.52:5678",
    "177.73.248.38:55290",
    "103.212.93.254:45639",
    "168.205.218.26:4145",
    "202.165.38.185:17538",
    "104.16.105.106:80",
    "103.134.220.49:8080",
    "185.66.59.203:42647",
    "197.234.13.29:4145",
    "94.198.213.252:49979",
    "197.157.254.162:4145",
    "186.235.184.9:4153",
    "149.20.253.250:12551",
    "23.94.73.246:1080",
    "38.127.172.167:46656",
    "124.131.202.102:3128",
    "203.24.108.194:80",
    "104.27.83.183:80",
    "138.197.69.132:19260",
    "81.150.169.217:5678",
    "175.201.245.187:808",
    "45.70.30.199:5678",
    "202.124.43.253:4145",
    "110.78.149.110:4145",
    "178.162.202.44:2261",
    "199.192.28.108:7497",
    "104.19.225.70:80",
    "177.200.2.96:5678",
    "170.130.55.153:5001",
    "185.6.104.150:5678",
    "182.253.109.182:8080",
    "221.219.97.117:1080",
    "185.162.229.70:80",
    "118.174.219.41:4153"
]'''


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "bonbanh.pipelines.BonbanhPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
