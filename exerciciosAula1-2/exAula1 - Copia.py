import requests

from bs4 import BeautifulSoup
URL = "https://bsi.uniriotec.br"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())

# Abra o arquivo no modo de escrita. Se o arquivo não existir, ele será criado.
with open('meu_arquivo.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())