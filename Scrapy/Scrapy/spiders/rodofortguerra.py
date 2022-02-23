import scrapy


class RodofortguerraSpider(scrapy.Spider):
    name = 'rodofortguerra'
    start_urls = ['http://www.rodofortguerra.com.br/#produtos/']

    def parse(self, response):
        imagems = response.css('.no_border ::attr(src)').getall()
        titudos = response.css('.margin-bottom-10 ::text').getall()
        descricoes = response.css('.wpb_wrapper .margin-bottom-none ::text').getall()
        self.produtos = []
        for i, imagem in enumerate(imagems):
            self.produtos.append([imagem, titudos[i], descricoes[i]])
            

        yield {'Rodofortguerra' : self.produtos}

