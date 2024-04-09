import requests
from bs4 import BeautifulSoup

r = requests.get('https://bsi.uniriotec.br')
pagina = BeautifulSoup(r.text, "html.parser")

# Retorna as classes existem na página do BSI em formato de conjunto
tags = pagina.find_all(True)
conj_tags = set()
for tag in tags:
    if tag.has_attr("class"):
        for string in tag['class']:
            conj_tags.add("".join(string))
print(sorted(conj_tags))

# Retorna quantas vezes cada classe aparece na página do BSI
classes = dict()
for tag in tags:
    if tag.has_attr("class"):
        for string in tag['class']:
            if not classes.get("".join(string)):
                classes["".join(string)] = 1
            else:
                classes["".join(string)] += 1
for classe in sorted(classes.keys()):
    print(classe, ":", classes[classe])
    



