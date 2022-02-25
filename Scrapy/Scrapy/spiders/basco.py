import scrapy


class BascoSpider(scrapy.Spider):
    name = 'basco'
    start_urls = ['http://www.basco.com.br/produtos/']

    def parse(self, response):
        self.produtos = []
        self.titulos = []
        self.imagems = []
        self.descricoes = []
        links = ['http://www.basco.com.br/produtos']
        for i in response.css('#menu_secundario div ::attr(href)').getall():
            links.append(i)
        for link in links:
            yield scrapy.Request(link, callback=self.parse_produtos)

    def parse_produtos(self ,response):
        self.products = response.css('#menu_produtos li ::attr(href)').getall()
        for produto in self.products:
            yield scrapy.Request(produto)
            try:
                self.titulos.append(response.css('h1 ::text').get())
            except:
                self.titulos.append('NULL')

            try:
                self.imagems.append(response.css('#grande ::attr(src)').get())
            except:
                self.imagems.append('NULL')

            try:
                self.descricoes.append(response.css('.esquerda .conteudo ::text').getall()[5])
            except:
                self.descricoes.append('NULL')
            if len(self.descricoes) == 27:
                for i in range(len(self.titulos)):
                    self.produtos.append([self.titulos[i],self.imagems[i],self.descricoes[i]])
                yield{'basco': self.produtos}