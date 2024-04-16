import requests
import random
from bs4 import BeautifulSoup, Comment

resp = requests.get('https://bsi.uniriotec.br')
print("\n*** Página do BSI")
print(dir(resp))
num = random.randrange(0, 10)
print("\n*** Número aleatório: ", num)
print(dir(num))
print("\n*** Módulo random")
print(dir(random))
print("\n*** Lista dos nomes locais (escopo da chamada)")
print(dir())

print("2---------------------------------")
resp = requests.get('https://www.python.org')
pagina = BeautifulSoup(resp.text, "html.parser")
print(pagina.prettify())
print("3---------------------------------")

pagina = BeautifulSoup('''
    <html>
        <body background="red">
            <h1 id="teste" color="blue">Um cabeçalho</h1>
            <p>Um parágrafo</p>
        </body>
    </html>
    ''', "html.parser")
tag = pagina.body
print("---------------------------------")
pagina = BeautifulSoup('''
<html>
<body background="red">
<h1 id="teste" color="blue">Um cabeçalho</h1>
<p>Um parágrafo</p>
</body>
</html>
''', "html.parser")
tag = pagina.body
print("\ntag: \n", tag)
print("\nname: ", tag.name)
print("\nbackground: ", tag['background'])
print("\natributos: ", tag.attrs)
print("\nH1: ", tag.h1.attrs)
print("\nH1: ", tag.h1['id'])
print("---------------------------------")
pagina = BeautifulSoup('''
    <html>
        <body>
            <h1>Um cabeçalho</h1>
            <p>Um parágrafo</p>
        </body>
    </html>
    ''', "html.parser")
tag = pagina.body
print("\ntag: \n", tag)
print("\nname: ", tag.name)
print("\ntext: ", tag.text)
print("\ncontents: ", tag.contents)
print("\nparent: ", tag.parent.name, "\n")
filhos = tag.contents
print("Num. filhos: ", len(filhos))
i = 1
for filho in filhos:
    print("filho", i, ": ", filho.name, filho.text)
    i += 1
print("---------------------------------")
pagina = BeautifulSoup('''
   <html>
       <body>
           <p>Teste de filhos <span> de parágrafos</span></p>
       </body>
   </html>
   ''', "html.parser")
tag = pagina.p
filhos = tag.contents
print("\nNum. filhos: ", len(filhos))
i = 1
for filho in filhos:
    print("filho", i, ": ", "name: ", filho.name, "; text: ", filho.text)
    i += 1
print("---------------------------------")
pagina = BeautifulSoup('''
<html>
<body>
<h1>um cabeçalho</h1>
<p>Um parágrafo</p>
</body>
</html>
''', "html.parser")
print("\n*** string")
print(type(pagina.h1.string))
print(pagina.h1.string)
print("\n*** text")
print(type(pagina.h1.text))
print(pagina.h1.text)
print("---------------------------------")
pagina = BeautifulSoup('''
<html>
<body>
<p>Teste de parágrafo com e sem span</p>
</body>
</html>
''', "html.parser")
tag = pagina.p
print("\n*** string")
print(type(tag.string))
print(tag.string)
print("\n*** text")
print(type(tag.text))
print(tag.text)
print("\n*** contents")
print(type(tag.contents))
print(tag.contents)
print("---------------------------------")
pagina = BeautifulSoup('''
    <html>
        <body>
            <p>Teste de parágrafo <span>com e sem span</span></p>
        </body>
    </html>
    ''', "html.parser")
tag = pagina.p
for texto in tag.strings:
    print(type(texto))
    print(repr(texto))
print("---------------------------------")
pagina = BeautifulSoup('''
    <html>
        <body>
            <p>Teste de parágrafo <span>com 
            e sem span</span></p>
        </body>
    </html>
    ''', "html.parser")
tag = pagina
for texto in tag.strings:
    print(type(texto))
    print(texto)
print("---------------------------------")
pagina = BeautifulSoup('''
    <html>
        <body>
            <p>Teste de parágrafo <span>com 
            e sem span</span></p>
        </body>
    </html>
    ''', "html.parser")
tag = pagina
for texto in tag.stripped_strings:
    print(type(texto))
    print(texto)
print("---------------------------------")
resp = requests.get('https://bsi.uniriotec.br')
pagina = BeautifulSoup(resp.text, "html.parser")
print("Tipo: ", type(pagina))
print("Título: ", pagina.title)
print("Nome da tag: ", pagina.title.name)
print("String do título: ", pagina.title.string)
print("Nome do pai do título: ",
      pagina.title.parent.name)
print("---------------------------------")
resp = requests.get('https://bsi.uniriotec.br')
pagina = BeautifulSoup(resp.text, "html.parser")
listaTags = dict()
# for tag in pagina.find_all():
for tag in pagina.find_all('h1'):
    if not listaTags.get(tag.name):
        listaTags[tag.name] = 1
    else:
        listaTags[tag.name] += 1
for tag in sorted(listaTags.keys()):
    print(tag, ":", listaTags[tag])
print("---------------------------------")
pagina = BeautifulSoup('''
    <html>
        <body>
            <h1>um cabeçalho </h1>
            <p><!-- Um parágrafo comentado --></p>
        </body>
    </html>
    ''', "html.parser")
tag = pagina.p
print("\n", tag)
comentario = tag.string
print(comentario)
print(type(comentario), "\n")
print("---------------------------------")


def eh_comentario(elemento):
    return isinstance(elemento, Comment)


pagina = BeautifulSoup('''
 <html>
 <!-- Comentário antes do body -->
 <body>
 <!-- Um comentário antes do H1 -->
 <h1>um cabeçalho </h1>
 <p><!-- Um parágrafo só com comentário --></p>
 <p>Teste de comentário <!-- ok? --></p>
 <!-- Fim da páagina -->
 </body>
 </html>
 ''', "html.parser")
comentarios = pagina.find_all(text=eh_comentario)
for comentario in comentarios:
    print(comentario)
    print("Número de comentários: ", len(comentarios))
    print("*** tipo:", type(comentarios[0]))
