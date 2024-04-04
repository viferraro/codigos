import requests
import random
from bs4 import BeautifulSoup, Comment

# pagina = BeautifulSoup('''
#     <html>
#         <body background="red">
#             <h1 id="teste" color="blue">Um cabeçalho</h1>
#             <p>Um parágrafo</p>
#             <ul>
#                <li>Sistemas de Informação</li>
#                <li>Engenharia de Produção</li>
#                <li>Matemática</li> 
#         </body>
#     </html>
#     ''', "html.parser")
# tag = pagina.body
# print("\ntag: \n", tag.contents)
# print("\nQuantidade de tags: ", len(tag.contents))
# print()
# for i in range(0, len(tag.contents)):
#     print("tag[", i, "]: ", tag.contents[i])

print("-----------------------------------------------------------------------")

# pagina = BeautifulSoup('''
#     <html>
#         <body background="red">
#             <h1 id="teste" color="blue">Um cabeçalho</h1>
#             <p>Um parágrafo</p>
#             <ul>
#                <li>Sistemas de Informação</li>
#                <li>Engenharia de Produção</li>
#                <li>Matemática</li>
#             </ul>
#         </body>
#     </html>
#     ''', "html.parser")
# tag = pagina.body
# print("\nContents: \n", tag.contents)
# print("\nChildren: \n", tag.children)
# print("\nfilhos")
# for filho in tag.children:
#     print(filho.text)

print("-----------------------------------------------------------------------")

# pagina = BeautifulSoup('''
#     <html>
#         <body background="red">
#             <h1 id="teste" color="blue">Um cabeçalho</h1>
#             <p>Um parágrafo</p>
#             <ul>
#                <li>Sistemas de Informação</li>
#                <li>Engenharia de Produção</li>
#                <li>Matemática</li> 
#         </body>
#     </html>
#     ''', "html.parser")
# tag = pagina.body
# print("\nPai do body: ", tag.parent.name)
# print("\nPai da lista: ", tag.ul.parent.name)
# # tag.ul.contents[3] é o segundo item da lista, pq considera as quebras de linha.
# print("\nPai do segundo item da lista: ", tag.ul.contents[3].string, ", Pai: ", 
#       tag.ul.contents[3].parent.name)   

print("-----------------------------------------------------------------------")

# pagina = BeautifulSoup('''
#     <html>
#         <body background="red">
#             <h1 id="teste" color="blue">Um cabeçalho</h1>
#             <p>Um parágrafo</p>
#             <ul>
#                <li>Sistemas de Informação</li>
#                <li>Engenharia de Produção</li>
#                <li>Matemática</li> 
#         </body>
#     </html>
#     ''', "html.parser")
# # vai imprimir none, pq considera as quebras de linha.
# print("\nTag anterior: ",  pagina.p.previous_sibling.name)
# print("\nTag posterior: ", pagina.p.next_sibling.name)

# # print("\nTag anterior: ",  pagina.p.previous_sibling.previous_sibling.name)
# # print("\nTag posterior: ", pagina.p.next_sibling.next_sibling.name)

print("-----------------------------------------------------------------------")

# pagina = BeautifulSoup('''
#     <html>
#         <body background="red">
#             <h1 id="teste" color="blue">Um cabeçalho</h1>
#             <p>Um parágrafo</p>
#             <ul>
#                <li>Sistemas de Informação</li>
#                <li>Engenharia de Produção</li>
#                <li>Matemática</li> 
#         </body>
#     </html>
#     ''', "html.parser")
# print("\nTag anterior: ",  pagina.ul.next_element.next_element.name)
# print("\nTag posterior: ", pagina.li.previous_element.previous_element.name)
# print("\nTag posterior: ", 
# pagina.ul.contents[3].previous_element.previous_element.text)

print("-----------------------------------------------------------------------")

# resp = requests.get('https://www.python.org')
# pagina = BeautifulSoup(resp.text, "html.parser")
# links = pagina.find_all('a')
# print('\nQuantidade de links =', len(links))
# paragrafos = pagina.find_all('p')
# print('Quantidade de parágrafos =', len(paragrafos))
# tags = pagina.find_all(['a', 'p'])
# print('Quantidade de tags =', len(tags), '\n')

print("-----------------------------------------------------------------------")

# resp = requests.get('https://www.python.org')
# pagina = BeautifulSoup(resp.text, "html.parser")
# links = pagina.find_all('a')
# print('\nQuantidade de links =', len(links))
# paragrafos = pagina.find_all(['p', 'h1'])
# print('Quantidade de parágrafos =', len(paragrafos))
# tags = pagina.find_all(['a', 'p'])
# print('Quantidade de tags =', len(tags), '\n')

print("-----------------------------------------------------------------------")

# resp = requests.get('https://www.python.org')
# pagina = BeautifulSoup(resp.text, "html.parser")
# links = pagina.find_all("a", limit=2)
# print('\n', links[0])
# print('\n', links[1], "\n")

print("-----------------------------------------------------------------------")

# resp = requests.get('https://www.python.org')
# pagina = BeautifulSoup(resp.text, "html.parser")
# links = pagina.find_all("a", href=True)
# print("\nQuantidade de links =", len(links), "\n")
# for item in links:
#     print(item['href'])

print("-----------------------------------------------------------------------")

# resp = requests.get('https://www.python.org')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tags = pagina.find_all(True)
# print('\nQuantidade de tags =', len(tags), "\n")
# conj_tags = set()
# for tag in tags:
#     conj_tags.add(tag.name)
# print('Quantidade de tags diferentes =', len(conj_tags))
# for tag in conj_tags:
#     print(tag)

print("-----------------------------------------------------------------------")

# resp = requests.get('https://www.python.org')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tags = pagina.find_all(text="Documentation")
# print('\nQuantidade de tags =', len(tags), "\n")
# for tag in tags:
#     print(tag)

print("-----------------------------------------------------------------------")

# resp = requests.get('https://www.python.org/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tags = pagina.find_all(id="touchnav-wrapper")
# print("\nQuantidade de tags =", len(tags))
# i = 1
# for tag in tags:
#     print("i =", i, ": ", tag.name)
#     i += 1
# print()

print("-----------------------------------------------------------------------")

# resp = requests.get('https://www.python.org/')
# pagina = BeautifulSoup(resp.text, "html.parser")
# tags = pagina.find_all("span", {"aria-hidden":"true"})
# print("\nQuantidade de tags =", len(tags))
# i = 1
# for tag in tags:
#     print(tag)
#     i += 1
# print()

print("-----------------------------------------------------------------------")

resp = requests.get('https://www.python.org/')
pagina = BeautifulSoup(resp.text, "html.parser")
tags = pagina.find_all("span", {"aria-hidden":"true", 
"class":"icon-get-started"})
print("\nQuantidade de tags =", len(tags))
i = 1
for tag in tags:
    print(tag)
    i += 1
print()

print("-----------------------------------------------------------------------")