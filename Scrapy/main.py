import requests
import os
from time import sleep
import json

os.system('cls')
os.system('color a')
resp = input('Deseja instalar as blibliotecas[S/N]?: ')[0].upper()
if resp == 'S':
    os.system('pip install requests')
    os.system('pip install scrapy') 
sleep(2)
resp = input('Deseja recarregar o Scrapy[S/N]?: ')[0].upper()
if resp == 'S':
    print('Iniciando scrapy...')
    os.system('scrapy crawl Argi -O Arquivos/produtos_argi.json')
    os.system('scrapy crawl rodofortguerra -O Arquivos/produtos_rodofortguerra.json')
    os.system('scrapy crawl axionlift -O Arquivos/produtos_axion.json')
    os.system('scrapy crawl cba -O Arquivos/produtos_cba.json')
    os.system('scrapy crawl aspok -O Arquivos/produtos_aspok.json')
    os.system('scrapy crawl basco -O Arquivos/produtos_basco.json')
    os.system('scrapy crawl eringer -O Arquivos/produtos_eringer.json')
    os.system('scrapy crawl dana -O Arquivos/produtos_dana.json')
with open('Arquivos/produtos_argi.json') as json_file:
    dados = json.load(json_file)
    dados = dados[0]['Arqgi']
    for i in dados:
        print(i[0])
        print('\n')
        print(i[1])
        print('\n')
        print(i[2])
        print('\n')
        print('='*120)
        print('\n')
        sleep(0.02)
with open('Arquivos/produtos_rodofortguerra.json') as json_file:
    dados = json.load(json_file)
    dados = dados[0]['Rodofortguerra']
    for i in dados:
        print(i[0])
        print('\n')
        print(i[1])
        print('\n')
        print(i[2])
        print('\n')
        print('='*120)
        print('\n')
        sleep(0.02)
with open('Arquivos/produtos_axion.json') as json_file:
    dados = json.load(json_file)
    dados = dados[0]['Axionlift']
    for i in dados:
        print(i[0])
        print('\n')
        print(i[1])
        print('\n')
        print(i[2])
        print('\n')
        print('='*120)
        print('\n')
        sleep(0.02)
with open('Arquivos/produtos_cba.json') as json_file:
    dados = json.load(json_file)
    dados = dados[0]['cba']
    for i in dados:
        print(i[0])
        print('\n')
        print(i[1])
        print('\n')
        print(i[2])
        print('\n')
        print('='*120)
        print('\n')
        sleep(0.02)
'''with open('Arquivos/produtos_basco.json') as json_file:
    dados = json.load(json_file)
    dados = dados[0]['basco']
    for i in dados:
        print(i[0])
        print('\n')
        print(i[1])
        print('\n')
        print(i[2])
        print('\n')
        print('='*120)
        print('\n')'''
with open('Arquivos/produtos_aspok.json') as json_file:
    dados = json.load(json_file)
    dados = dados[0]['aspok']
    for i in dados:
        print(i[0])
        print('\n')
        print(i[1])
        print('\n')
        print(i[2])
        print('\n')
        print('='*120)
        print('\n')
        sleep(0.02)
with open('Arquivos/produtos_eringer.json') as json_file:
    dados = json.load(json_file)
    dados = dados[0]['eringer']
    for i in dados:
        print(i[0])
        print('\n')
        print(i[1])
        print('\n')
        print(i[2])
        print('\n')
        print('='*120)
        print('\n')
        sleep(0.02)
'''with open('Arquivos/produtos_dana.json') as json_file:
    dados = json.load(json_file)
    dados = dados[0]['dana']
    for i in dados:
        print(i[0])
        print('\n')
        print(i[1])
        print('\n')
        print(i[2])
        print('\n')
        print('='*120)
        print('\n')
'''
input('VERIFIQUE A PASTA ARQUIVOS E PRESSIONE ENTER PARA SAIR...')