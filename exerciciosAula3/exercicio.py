import requests
import random
from bs4 import BeautifulSoup, Comment

# Fazendo a requisição para a página do BSI
url = 'https://bsi.uniriotec.br'
resposta = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if resposta.status_code == 200:
    # Analisando o conteúdo da página
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # Encontrando todos os parágrafos
    paragrafos = soup.find_all('p')
    print(f'Quantidade de parágrafos na página: {len(paragrafos)}')
    
    # Contando quantas vezes a palavra UNIRIO aparece na página
    texto_pagina = soup.get_text()
    contagem_unirio = texto_pagina.upper().count('UNIRIO')
    print(f'A palavra UNIRIO aparece {contagem_unirio} vezes na página.')
else:
    print('Não foi possível acessar a página do BSI.')