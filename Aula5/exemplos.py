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

# resp = requests.get('https://bsi.uniriotec.br/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tag = pagina.find("div", attrs={"id": "colophon", "class": "colophon"})
# print(tag)
# print(type(tag), "\n")
# tag = pagina.find_all("div", attrs={"id": "colophon", "class": "colophon"})
# print(tag)
# print(type(tag))
# print("XXXXXXXXX")
# print("Quantidade = ", len(tag))

print("-----------------------------------------------------------------------")

# resp = requests.get('https://bsi.uniriotec.br/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tag = pagina.find(attrs={"id": "colophon", "class": "colophon"})
# print(tag)
# print(type(tag), "\n")
# tag = pagina.find_all(attrs={"id": "colophon", "class": "colophon"})
# print(tag)
# print(type(tag))
# print("Quantidade = ", len(tag))

print("-----------------------------------------------------------------------")

# resp = requests.get('https://bsi.uniriotec.br/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tag = pagina.find(attrs={"id": "post-3466", "class": ["grid-item", "col-xl-4", "type-post"]})
# print(type(tag), "\n")
# tag = pagina.find_all(attrs={"id": "post-3466", "class": ["grid-item", "col-xl-4", "type-post"]})
# print(type(tag))
# print("Quantidade = ", len(tag))

print("-----------------------------------------------------------------------")

# resp = requests.get('https://bsi.uniriotec.br/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tag = pagina.find( attrs={"id": "post-3466"},  class_=["grid-item", "col-xl-4", "type-post"])   #usando class_ ao invés de "class"
# print(type(tag), "\n")
# tag = pagina.find_all( attrs={"id": "post-3466"},  class_=["grid-item", "col-xl-4", "type-post"])
# print(type(tag))
# print("Quantidade = ", len(tag))

print("-----------------------------------------------------------------------")

# resp = requests.get('https://bsi.uniriotec.br/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tag = pagina.find(class_="row fp-widget-area").find(class_="featured-page").find(class_="widget-front")
# # ou tag = pagina.find(attrs={"class":"row fp-widget-area"}).find(attrs={"class":"featured-page"}).find(attrs={"class":"widget-front"})
# print("*** tag")
# print(tag)
# print("\n*** text")
# print(tag.text)
# print("\n*** type")
# print(type(tag), "\n")

print("-----------------------------------------------------------------------")

# r = requests.get('http://bsi.uniriotec.br')
# pagina = BeautifulSoup(r.text, "html.parser")
# # Título da página
# paragrafos = pagina.select('p')
# print(paragrafos)

print("-----------------------------------------------------------------------")

# r = requests.get('http://bsi.uniriotec.br')
# pagina = BeautifulSoup(r.text, "html.parser")
#  # Título da página
# print("\n*** Titulo")
# titulo = pagina.select('title')
# print("Tipo de objeto: "     + str(type(titulo)))
# print("Linha do Título: "    + str(titulo))
# print("Conteudo do titulo: " + titulo[0].getText())
# print("Conteudo do titulo: " + titulo[0].text)
#  # Metas da página (Metas são informações sobre a página)
# print("\n*** Metas")
# meta = pagina.select('meta')
# print("Num. de metas =", len(meta))
# print(type(meta))
# print('META 0:' + str(meta[0]))
# print('META 1:' + str(meta[1]))
# print('META 2:' + str(meta[2]))

print("-----------------------------------------------------------------------")

# r = requests.get('http://guialinux.uniriotec.br')
# pagina = BeautifulSoup(r.text, "html.parser")
# span = pagina.select('div span')
# print("\nNúmero de spans em divs: " + str(len(span)))
# print(span[10])
# img = pagina.select('img')
# print("\nNúmero de imagens: " + str(len(img)))
# print(img[0])
# dd = pagina.select('dd') # dd é uma tag de definição
# print("\nNúmero de dds: " + str(len(dd)))
# print(dd[5])
# dd= str(dd[5].getText())
# print(dd + "\n")

print("-----------------------------------------------------------------------")

# r = requests.get('https://www.python.org/')
# pagina = BeautifulSoup(r.text, "html.parser")
# classe = pagina.select('.icon-arrow-up, .text-shrink')
# print("\nNúmero encontrado: " + str(len(classe)))
# for item in classe:
#     print(item)
# print()

print("-----------------------------------------------------------------------")

# r = requests.get('https://www.python.org/')
# pagina = BeautifulSoup(r.text, "html.parser")
# links = pagina.select('a[href]')
# print("\nNúmero encontrado: " + str(len(links)))
# for item in links:
#     print(item)

print("-----------------------------------------------------------------------")

# r = requests.get('https://www.python.org/')
# pagina = BeautifulSoup(r.text, "html.parser")
# links = pagina.select('a[href="#python-network"]')
# print("\nNúmero encontrado: " + str(len(links)))
# for item in links:
#     print(item)

print("-----------------------------------------------------------------------")

# r = requests.get('https://www.python.org/')
# pagina = BeautifulSoup(r.text, "html.parser")
# links = pagina.select('a[href="#python-network"]' and 'a[id="back-to-top-1"]')
# print("\nNúmero encontrado: " + str(len(links)))
# for item in links:
#     print(item)

print("-----------------------------------------------------------------------")

# r = requests.get('https://www.python.org/')
# pagina = BeautifulSoup(r.text, "html.parser")
# classes = set() 
# tags = pagina.find_all()
# for tag in tags:
#     if tag.has_attr( "class" ): 
#         if len( tag['class'] ) != 0:
#             for string in tag['class']:
#                 classes.add("".join( string)) 
# print(sorted(classes))

print("-----------------------------------------------------------------------")

r = requests.get('https://bsi.uniriotec.br')
pagina = BeautifulSoup(r.text, "html.parser")
links = pagina.select('a[href]')
print("\nNúmero de links: " + str(len(links)))
for link in links:
    print(link)

print("-----------------------------------------------------------------------")