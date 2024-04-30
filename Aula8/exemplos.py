import requests
from bs4 import BeautifulSoup
import re

# Faz a requisição HTTP para a página
url = 'https://bsi.uniriotec.br/institucional/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
pagina = BeautifulSoup(response.text, 'html.parser')

# Encontra todos os textos na página
all_text = soup.get_text()

# Encontra todos os links na página
all_links = soup.find_all('a')

msg='1227 122228 104 1222222226 1232323 1523 121212512'

print(msg, '\n')
padrao = '12*'
print('Padrão: "12*"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')

print(msg, '\n')
padrao = '12*2'
print('Padrão: "12*2"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')

msg='1227 122228 104 1222222224 124 14 1204'
print(msg, '\n')
padrao = '12*4'
print('Padrão: "12*4"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')

msg='Sistemas de informação são descritos em termos de suas dimensões tecnológica, organizacional e humana, o que exige uma abordagem multidisciplinar. Nosso curso BSI-UNIRIO propicia uma formação básica sólida em Sistemas de Informação, Ciência da Computação e Matemática, além de propiciar formação com ênfase no estudo das tecnologias, das organizações e de fatores humanos.'
print('\n')
padrao = 'BS.*O'   #.* = qualquer coisa
print('Padrão: "BS.*O"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')

msg='1227 122228 104 1222222226 1232323 1523 121212512'
print('\n')
padrao = '12+'   #+ = 1 ou mais
print('Padrão: "12+"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')

padrao = '12+2'
print('Padrão: "12+2"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')

padrao = '122+2'
print('Padrão: "122+2"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')

msg='1227 122228 106 16 1222222226 1232323 1523 121212512'
print(msg, '\n')
padrao = '12+6'
print('\nPadrão: "12+6"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')

msg='Sistemas de informação são descritos em termos de suas dimensões tecnológica, organizacional e humana, o que exige uma abordagem multidisciplinar. Nosso curso BSI-UNIRIO propicia uma formação básica sólida em Sistemas de Informação, Ciência da Computação e Matemática, além de propiciar formação com ênfase no estudo das tecnologias, das organizações e de fatores humanos.'
padrao = 'human?' #? = 0 ou 1
print('Padrão: "human?"')
teste = re.findall(padrao, msg)
print(teste)
padrao = 'humano?'
print('Padrão: "humano?"')
teste = re.findall(padrao, msg)
print(teste)
padrao = 'humana?'
print('Padrão: "humana?"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')
padrao = 'human[a-z]?'
print('Padrão: "human[a-z]?"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')
padrao = 'human[^a]?'
print('Padrão: "human[^a]?"')
teste = re.findall(padrao, msg)
print(teste)

msg='1227 122228 104 1222222226 1232323 1523 121212512'
print('\nmsg =', msg, "\n")
padrao = '12{3}'  # {3} = 3 vezes
print('Padrão: "12{3}"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')
padrao = '12{0,3}'   # {0,3} = 0 a 3 vezes
print('Padrão: "12{0-3}"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')
padrao = '12{2,}'   # {2,} = 2 ou mais vezes
print('Padrão: "12{2,}"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')

