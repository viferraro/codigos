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