import requests
from bs4 import BeautifulSoup
import re

# Faz a requisição HTTP para a página
url = 'https://bsi.uniriotec.br/institucional/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontra todos os textos na página
all_text = soup.get_text()

# Usa expressão regular para encontrar números com mais de um dígito
multiple_digit_numbers = re.findall(r'\d{2,}', all_text)

# Conta o número de números encontrados
total_multiple_digit_numbers = len(multiple_digit_numbers)

print(f"Total de números com mais de um dígito: {total_multiple_digit_numbers}")