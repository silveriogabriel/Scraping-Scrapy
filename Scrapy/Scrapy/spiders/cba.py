import scrapy


class CbaSpider(scrapy.Spider):
    name = 'cba'
    start_urls = ['http://www.cba.com.br/produtos/produtos-transformados//']

    def parse(self, response):
        self.produtos = []
        self.titulos = []
        self.imagens = []
        self.descricoes = []
        for c in response.css('.highlight-title ::text').getall():
            self.titulos.append(c)
        for c in response.css('.highlight--col .hidden-phone ::attr(src)').getall():
            self.imagens.append(c)
            self.descricoes.append('NULL')
        for c in range(len(self.titulos)):
            self.produtos.append([self.titulos[c], self.imagens[c], self.descricoes[c]])
        yield {'cba': self.produtos}