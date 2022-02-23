import requests
import os
from time import sleep

os.system('cls')
os.system('color a')
resp = input('Deseja instalar as blibliotecas[S/N]?: ')[0].upper()
if resp == 'S':
    os.system('pip install requests')
    os.system('pip install scrapy') 
print('Iniciando scrapy...')
sleep(2)
os.system('scrapy crawl Argi -O Arquivos/produtos.json')
os.system('scrapy crawl rodofortguerra -o Arquivos/produtos.json')
os.system('scrapy crawl axionlift -o Arquivos/produtos.json')
input('VERIFIQUE A PASTA ARQUIVOS E PRESSIONE ENTER PARA SAIR...')