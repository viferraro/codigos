import requests, bs4

res = requests.get('http://bsi.uniriotec.br')
pagina = bs4.BeautifulSoup(res.text, "html.parser")
titulo = pagina.select('title')
print("\nTITULO: "  + str(titulo))
print("Conteudo do titulo:" + titulo[0].getText())