import scrapy


class DanaSpider(scrapy.Spider):
    name = 'dana'
    allowed_domains = ['www.dana.com/products']
    start_urls = ['http://www.dana.com/products/']

    def parse(self, response):
        pass
