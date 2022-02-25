import scrapy


class ArgiSpider(scrapy.Spider):
    name = 'Argi'
    start_urls = ['http://www.argi.com.br/produtos/furgao-carga-geral/1/']

    def parse(self, response):
        self.links = response.css('.separator+ li ::attr(href)').getall()
        self.produtos = []
        imagem = response.css('#galeriacontent img ::attr(src)').get()
        titulo = response.css('.title ::text').get()
        descricao = response.css('#content p ::text').get()
        self.produtos.append([imagem,titulo,descricao])
        for link in self.links[1:]:
            yield scrapy.Request(link, callback=self.parse_paginas)

    def parse_paginas(self, response):
        imagem = response.css('#galeriacontent img ::attr(src)').get()
        titulo = response.css('.title ::text').get()
        descricao = response.css('#content p ::text').get()
        self.produtos.append([titulo,imagem,descricao])
        print(self.links)
        if response.url == 'http://www.argi.com.br/produtos/produtos-especiais/5':
            yield {'Arqgi': self.produtos}