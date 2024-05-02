import requests
from bs4 import BeautifulSoup
import re

# Faz a requisição HTTP para a página
url = 'https://bsi.uniriotec.br/institucional/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
pagina = BeautifulSoup(response.text, 'html.parser')
paragrafos = soup.find_all('p')

# msg="""Sistemas de informação são descritos em termos de suas dimensões 
# tecnológica, organizacional e humana, 
# o que exige uma abordagem multidisciplinar. 
# Nosso curso BSI-UNIRIO propicia uma formação básica sólida em Sistemas 
# de Informação, Ciência da Computação 
# e Matemática, além de propiciar formação com ênfase no estudo das 
# tecnologias, das organizações e de 
# fatores humanos."""
# padrao = '^S'
# print('Padrão: "^S"')
# teste = re.findall(padrao, msg)
# print(teste)
# padrao = '^N'
# print('Padrão: "^N"')
# teste = re.findall(padrao, msg)
# print(teste)

# padrao = '^O'
# cont = 0
# for paragrafo in paragrafos:
#     if re.search(padrao, paragrafo.text):
#         cont += 1
#         #print("\n", paragrafo.text)
# print("\nNúmero de parágrafos: ", cont)

# padrao = '^O Bacharel'
# cont = 0
# for paragrafo in paragrafos:
#     if re.search(padrao, paragrafo.text):
#         cont += 1
#         #print("\n", paragrafo.text)
# print("\nNúmero de parágrafos: ", cont)

# padrao = '.{20}$'
# print('Padrão: ".{20}$"')
# for paragrafo in paragrafos:
#     if len(paragrafo.text) > 0:
#         teste = re.findall(padrao, paragrafo.text)
#         print(teste)

# padrao = 'humanos.$'
# cont = 0
# for paragrafo in paragrafos:
#     if re.search(padrao, paragrafo.text):
#         cont += 1
#         print("\n", paragrafo.text)
# print("\nNúmero de parágrafos: ", cont)

# paragrafos = soup.find_all('p')
# padrao = ' formação (?!básica)'
# cont = 0
# for paragrafo in paragrafos:
#     teste = re.findall(padrao, paragrafo.text)
#     if len(teste) > 0:
#         cont += 1
#         #print("\n", paragrafo)
# print("\nQuantidade: ", cont)

# padrao = r'Bacharelado[\w\s]+(?!UNIRIO)'
# cont = 0
# for paragrafo in paragrafos:
#     teste = re.findall(padrao, paragrafo.text)
#     if len(teste) > 0:
#         cont += 1
#         #print("\n", paragrafo)
# print("\nQuantidade: ", cont)

# padrao = '^(?!O Bacharel)'
# cont = 0
# for paragrafo in paragrafos:
#     if re.search(padrao, paragrafo.text):
#         cont += 1
#         print("\n", paragrafo.text)
# print("\nNúmero de parágrafos: ", cont)

# padrao = ' formação (?=com ênfase)'
# cont = 0
# for paragrafo in paragrafos:
#     if re.search(padrao, paragrafo.text):
#         cont += 1
#         print("\n", paragrafo.text)
# print("\nNúmero de parágrafos: ", cont)

# padrao = 'formação'
# cont = 0
# for paragrafo in paragrafos:
#     teste = re.findall(padrao, paragrafo.text)
#     if len(teste) > 0:
#         cont += 1
# print("Quantidade 'formação': ", cont)
# padrao = r'\bformação\b'
# cont = 0
# for paragrafo in paragrafos:
#     teste = re.findall(padrao, paragrafo.text)
#     if len(teste) > 0:
#         cont += 1
# print("Quantidade '\\bformação\\b': ", cont)

# obj_re = re.compile(r'\bBacharelado\b')
# print("\n",type(obj_re))
# cont = 0
# for paragrafo in paragrafos:
#     if obj_re.search(paragrafo.text):
#         cont += 1
#         print("\n", paragrafo.text)
# print("Quantidade:", cont, "\n")

# find_info = re.compile(r'informação', re.IGNORECASE)
# info_count = len(find_info.findall(soup.text))
# find_sys = re.compile(r'sistemas', re.IGNORECASE)
# sys_count = len(find_sys.findall(soup.text))
# print(f'Informações: {info_count}')
# print(f'Sistemas: {sys_count}')

# msg='E agora, José? A festa acabou, a luz apagou, o povo sumiu, a noite esfriou, e agora, José? e agora, você? você que é sem nome, que zomba dos outros, você que faz versos, que ama, protesta? e agora, José?'
# padrao = 'e '
# print("\nPadrão: " + padrao)
# teste = re.search(padrao,msg)
# print('\n*** search')
# print(teste.group())
# print('\n*** findall com case-sensitive')
# teste = re.findall(padrao, msg)
# print(teste)
# print('\n*** findall sem case-sensitive ')
# teste = re.findall(padrao, msg, re.IGNORECASE)
# print(teste, "\n")

# texto_CL = "Renda-se, como eu me rendi. Mergulhe no que você não conhece como eu mergulhei. Não se preocupe em entender, viver ultrapassa qualquer entendimento."
# x = re.split("\s", texto_CL)
# print("\n", x)
# x = re.split("\s", texto_CL, 4)
# print("\n", x)
# x = re.split("\s+", texto_CL)
# print("\n", x, "\n")

# padrao = r'\bBacharelado\b'
# x = re.split(padrao, paragrafos[1].text)
# print("\n", paragrafos[1].text)
# print("\n", x)

texto_CL = "Renda-se, como eu me rendi. Mergulhe no que você não conhece como eu mergulhei. Não se preocupe em entender, viver ultrapassa qualquer entendimento."
x = re.sub("\s", "999", texto_CL, 3)
print(x) 