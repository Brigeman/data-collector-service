from scrapy.crawler import CrawlerProcess
from data_collector.spiders.real_estate_spider import RealEstateSpider

process = CrawlerProcess()
process.crawl(RealEstateSpider)
process.start()