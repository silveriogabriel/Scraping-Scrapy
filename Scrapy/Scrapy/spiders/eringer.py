import scrapy


class EringerSpider(scrapy.Spider):
    name = 'eringer'
    start_urls = ['http://heringer.eng.br/produtos/']

    def parse(self, response):
        self.produtos = []
        self.titulos = []
        self.imagens = []
        self.descricoes = []
        for i in response.css('h5 ::text').getall():
            self.titulos.append(i)
        for i in response.css('.cs-image-alignment-center a .cs-chosen-image ::attr(src)').getall():
            self.imagens.append(i)
        links = response.css('section .cs-widgets ::attr(href)').getall()
        print(links)
        for i in links:
            yield scrapy.Request(i, callback=self.parse_produto)
    def parse_produto(self, response):
        self.descricoes.append(response.css('p ::text').get())
        if len(self.descricoes) == 15:
            for i in range(len(self.titulos)):
                self.produtos.append([self.titulos[i], self.imagens[i], self.descricoes[i]])
            yield {'eringer':self.produtos}
        