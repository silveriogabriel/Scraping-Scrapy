import scrapy


class AspokSpider(scrapy.Spider):
    name = 'aspok'
    start_urls = ['http://aspock.com.br/produtos/?lang=pt/']

    def parse(self, response):
        imagens = response.css('.produto ::attr(src)').getall()
        nomes  = response.css('h2 ::text').getall()[2:]
        produtos = []
        for i in range(len(imagens)):
            produtos.append([nomes[i],imagens[i],'NULL'])
        yield {'aspok':produtos}
