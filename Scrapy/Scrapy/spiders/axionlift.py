import scrapy


class AxionliftSpider(scrapy.Spider):
    name = 'axionlift'
    start_urls = ['https://axionlift.com/pt/productos/']
    handle_httpstatus_all = True

    def parse(self, response):
        self.links = response.css('.col-xs-6 ::attr(href)').getall()
        self.produtos = []
        self.titulos = []
        self.imagens = []
        self.descricoes = []
        for link in self.links:
            yield scrapy.Request(link, callback=self.parse_paginas)
        

    def parse_paginas(self, response):
        if response.url != 'https://axionlift.com/pt/hidrogruas/':
            links = ['https://axionlift.com/pt/elevadores/']
            for c in response.css('.page-numbers ::attr(href)').getall()[:-1]:
                links.append(c)
            for self.link in links:
                yield scrapy.Request(self.link, callback=self.parse_titulos)
            else:
                yield scrapy.Request('https://axionlift.com/pt/hidrogruas/', callback=self.parse_titulos)
            
    
    def parse_titulos(self, response):
        for c in response.css('.card-info h1 ::text').getall():
            self.titulos.append(c)
        imagens = response.css('.col-sm-4 ::attr(src)').getall()[1::2]
        for img in imagens:
            self.imagens.append(img)

        for c in response.css('.col-sm-4 ::attr(href)').getall():
            yield scrapy.Request(c, callback=self.parse_descricao)
    
    
    def parse_descricao(self, response):
        self.descricoes.append(response.css('.product-description p ::text').get())
        if len(self.descricoes) == len(self.titulos):
            for i, titulo in enumerate(self.titulos):
                self.produtos.append([titulo, self.imagens[i], self.descricoes[i]])
            yield {'Axionlift': self.produtos}