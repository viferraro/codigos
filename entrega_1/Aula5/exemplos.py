import requests, re
import random
from bs4 import BeautifulSoup, Comment

# resp = requests.get('https://www.python.org/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# print('\n*** Primeiro Parágrafo')
# print(pagina.find('p').text)
# print('\n*** Primeiro Link')
# print(pagina.find('a').text)
# print("\n")

print("-----------------------------------------------------------------------")

# resp = requests.get('https://www.python.org/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tag = pagina.find('a', id="python-network" )
# print("\n", tag)
# print(tag.name)
# print(tag.text)
# print(tag.strings)
# print(tag.contents)
# print("\n")

print("-----------------------------------------------------------------------")

# resp = requests.get('https://www.python.org/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tag = pagina.find("span", {"aria-hidden":"true", "class":"icon-get-started"})
# print("\n", tag, "\n")

print("-----------------------------------------------------------------------")

# resp = requests.get('https://www.python.org/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tag = pagina.find('p')
# print(tag)
# print(type(tag))
# #print(type(tag[0]), "\n")
# tag = pagina.find_all('p', limit=1)
# print(tag)
# print(type(tag))
# print(type(tag[0])), "\n"

print("-----------------------------------------------------------------------")

# resp = requests.get('https://bsi.uniriotec.br/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tag = pagina.find("a", string=re.compile("UNIRIO", re.I))
# print(tag)
# print(type(tag), "\n")
# tag = pagina.find_all("a", string=re.compile("UNIRIO", re.I))
# print(tag)
# print(type(tag))

print("-----------------------------------------------------------------------")

# import requests, bs4, re
# resp = requests.get('https://bsi.uniriotec.br/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tag = pagina.find("p", attrs={"class":"czr-copyright"})
# print(tag)
# print(type(tag), "\n")
# tag = pagina.find_all("p", attrs={"class":"czr-copyright"})
# print(tag)
# print(type(tag))

print("-----------------------------------------------------------------------")

import requests, bs4, re
resp = requests.get('https://bsi.uniriotec.br/')
pagina = bs4.BeautifulSoup(resp.text, "html.parser")
tag = pagina.find("div", attrs={"id": "colophon", "class": "colophon"})
print(tag)
print(type(tag), "\n")
tag = pagina.find_all("div", attrs={"id": "colophon", "class": "colophon"})
print(tag)
print(type(tag))
print("Quantidade = ", len(tag))

print("-----------------------------------------------------------------------")

print("-----------------------------------------------------------------------")

print("-----------------------------------------------------------------------")

print("-----------------------------------------------------------------------")

print("-----------------------------------------------------------------------")