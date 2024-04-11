import requests
from bs4 import BeautifulSoup, Comment

url = 'https://bsi.uniriotec.br/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 14) Quantidade de tags que não são parágrafos
num_tags_nao_paragrafos = 0
for tag in soup.find_all():
    if tag.name != 'p':
        num_tags_nao_paragrafos += 1

# Imprime o resultado
print(f"14) Quantidade de tags que não são parágrafos: {num_tags_nao_paragrafos}")


'''
24) Para que serve o atributo .contents? 
O atributo .contents de um objeto Tag retorna uma lista com todos os elementos 
filhos diretos da tag, incluindo tanto texto quanto outras tags. É útil para 
iterar sobre os elementos filhos e manipulá-los.

Aluna: Vívian Rqiue Gil Ferraro

14) Quantidade de tags que não são parágrafos

import requests
from bs4 import BeautifulSoup
url = 'https://bsi.uniriotec.br/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
num_tags_nao_paragrafos = 0
for tag in soup.find_all():
    if tag.name != 'p':
        num_tags_nao_paragrafos += 1
print(f"Quantidade de tags que não são parágrafos: {num_tags_nao_paragrafos}")



24) Para que serve o atributo .contents? 
O atributo .contents permite acessar o conteúdo de um elemento BeautifulSoup como uma lista de objetos com todos os 
elementos filhos diretos da tag, incluindo tanto texto quanto outras tags. É útil para iterar sobre os elementos 
filhos e manipulá-los.


'''
