import requests
from bs4 import BeautifulSoup
import re

# Faz a requisição HTTP para a página
url = 'https://bsi.uniriotec.br/institucional/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
pagina = BeautifulSoup(response.text, 'html.parser')
paragrafos = soup.find_all('p')

# # 1) Qual o padrão de uma RegEx dos e-mails da UNIRIO ('nomealuno@edu.unirio.br' ou '...@uniriotec.br')?
# padrao = r'\b[\w\.-]+@(edu\.unirio\.br\b | \b[\w\.-]+@uniriotec\.br\b'
# print('Padrão: "...@edu.unirio.br" ou "...@uniriotec.br"')
# teste = re.findall(padrao, pagina.text)
# print(teste)

# # 2) Para a página https://bsi.uniriotec.br/institucional/, em quantos parágrafos aparecem a palavra “graduação” mais de uma vez?
# padrao = r'\bgraduação\b'
# cont = 0
# for paragrafo in paragrafos:
#     if re.findall(padrao, paragrafo.text):
#         cont += 1
#         print("\n", paragrafo.text)
# print("\nNúmero de parágrafos: ", cont)

# 3) Para a página https://bsi.uniriotec.br/institucional/, lista as siglas e os seus significados.
# padrao = r'\b[A-Z]{2,}\b'
# cont = 0
# for paragrafo in paragrafos:
#     if re.findall(padrao, paragrafo.text):
#         cont += 1
#         print("\n", paragrafo.text)
# print("\nNúmero de parágrafos: ", cont)

texto = soup.get_text()
padrao = r'[A-ZÀ-Ü]{2,}\s\([A-ZÀ-Üa-zà-ü\s]*\)'
palavras = re.findall(padrao, texto)
siglas = set(palavras)
for sigla in siglas:
    print(sigla)
print("Quantidade = ", len(siglas))

