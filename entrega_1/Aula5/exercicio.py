import requests
from bs4 import BeautifulSoup

r = requests.get('https://bsi.uniriotec.br')
pagina = BeautifulSoup(r.text, "html.parser")

# Encontra todos os elementos <p> com alguma classe CSS
paragrafos_com_classe = pagina.select('p[class]')

print("\nNúmero de parágrafos com classe CSS: " + str(len(paragrafos_com_classe)))