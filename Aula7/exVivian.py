import requests
from bs4 import BeautifulSoup
import re

# Faz a requisição HTTP para a página
url = 'https://bsi.uniriotec.br/institucional/'
response = requests.get(url)
pagina = BeautifulSoup(response.text, 'html.parser')

texto = pagina.body.text


# Usa expressão regular para encontrar números com mais de um dígito
numeros = re.findall(r'\d+', texto)
print(numeros)

# Conta o número de números encontrados
total_numeros = len(numeros)

print(f"Total de números com mais de um dígito: {total_numeros}")

print("------------------------------------------------------------------------")


# Usa expressão regular para encontrar números com mais de um dígito
numeros = re.findall('[0-9][0-9]', texto)
print(numeros)

# Conta o número de números encontrados
total_numeros = len(numeros)

print(f"Total de números com mais de um dígito: {total_numeros}")

print("------------------------------------------------------------------------")

# Usa expressão regular para encontrar números com mais de um dígito
numeros = re.findall(r'\d{2,}', texto)
print(numeros)

# Conta o número de números encontrados
total_numeros = len(numeros)

print(f"Total de números com mais de um dígito: {total_numeros}")