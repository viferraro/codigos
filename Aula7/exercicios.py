import requests
from bs4 import BeautifulSoup
import re

# Faz a requisição HTTP para a página
url = 'https://bsi.uniriotec.br/institucional/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontra todos os textos na página
all_text = soup.get_text()

# Usa expressão regular para encontrar palavras que começam com letra maiúscula
#uppercase_words = re.findall(r'\b[A-Z][a-zA-Z]*\b', all_text)  #() o r significa que é uma expressão regular
uppercase_words = re.findall(r'\b[A-ZÀ-Ü][a-zà-ü]*\b', all_text)

# Conta o número de palavras encontradas
total_uppercase_words = len(uppercase_words)
print (uppercase_words)
print(f"Total de palavras que começam com letra maiúscula: {total_uppercase_words}")

# Usa expressão regular para encontrar palavras que começam com letra minúscula
lowercase_words = re.findall(r'\b[a-zà-ü][a-zà-ü]*\b', all_text)

# Conta o número de palavras encontradas
total_lowercase_words = len(lowercase_words)

print(f"Total de palavras que começam com letra minúscula: {total_lowercase_words}")

# Usa expressão regular para encontrar caracteres não alfanuméricos
non_alphanumeric_chars = re.findall(r'[^a-zà-üA-ZÀ-Ü0-9\s]', all_text)

# Remove duplicatas
unique_non_alphanumeric_chars = set(non_alphanumeric_chars)

print(f"Caracteres não alfanuméricos: {', '.join(unique_non_alphanumeric_chars)}")

# Usa expressão regular para encontrar dígitos numéricos
numeric_digits = re.findall(r'\d', all_text)

# Conta o número de dígitos encontrados
total_numeric_digits = len(numeric_digits)

print(f"Total de dígitos numéricos: {total_numeric_digits}")

# 6) Quantos links internos possuem a página? Para contar os links internos, precisaríamos inspecionar o código HTML da página e encontrar os elementos <a> que apontam para URLs dentro do mesmo domínio (por exemplo, ‘https://bsi.uniriotec.br/’). Infelizmente, como não tenho acesso à página em tempo real, não posso fazer isso diretamente aqui.
links = soup.select("a[href='https://bsi.uniriotec.br/institucional/']")
for link in links:
    print(link['href'])
print("Número de links internos:", len(links))

# 7) Quantos links externos possuem a página? Da mesma forma, para contar os links externos, precisaríamos encontrar os elementos <a> que apontam para URLs fora do domínio ‘https://bsi.uniriotec.br/’.
if response.status_code == 200:
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    links_externos = 0
    for link in soup.find_all('a'):
        if link.get('href') and not link.get('href').startswith('#') and not link.get('href').startswith('https://bsi.uniriotec.br'):
            links_externos +=1
            print(link['href'])
    print(f"\nA página possui {links_externos} links externos.")
else:
    print("Erro ao acessar a página.")

# 8) Quantos links usam o protocolo https? Para contar os links que usam o protocolo HTTPS, precisaríamos verificar o atributo href dos elementos <a> e verificar se eles começam com ‘https://’. Infelizmente, não posso fazer isso diretamente aqui.
links = soup.select("a[href]")
for link in links:
    if "https" in link['href']:
        print(link['href'])
# 9) Quantos links possuem o texto “unirio”? Para contar os links que possuem o texto “unirio”, podemos buscar os elementos <a> no código HTML da página e verificar se o atributo href contém a palavra “unirio”. Infelizmente, como não tenho acesso à página em tempo real, não posso fazer isso diretamente aqui.
links = soup.select("a[href]")
for link in links:
    if "unirio" in link['href']:
        print(link['href'])
print("Quantidade de links com unirio: ", len(links))

# 10 Usa expressão regular para encontrar as palavras "sistemas" e "informações"
sistemas_count = len(re.findall(r'\bsistemas\b', all_text, flags=re.IGNORECASE))
informacoes_count = len(re.findall(r'\binformações\b', all_text, flags=re.IGNORECASE))

print(f"Ocorrências da palavra 'sistemas': {sistemas_count}")
print(f"Ocorrências da palavra 'informações': {informacoes_count}")

# Usa expressão regular para encontrar caracteres em branco
whitespace_count = len(re.findall(r'\s', all_text))

print(f"Total de caracteres em branco: {whitespace_count}")

# Usa expressão regular para encontrar as palavras "tecnologia" e "tecnologias"
tecnologia_count = len(re.findall(r'\btecnologia\b', all_text, flags=re.IGNORECASE))
tecnologias_count = len(re.findall(r'\btecnologias\b', all_text, flags=re.IGNORECASE))

print(f"Ocorrências da palavra 'tecnologia': {tecnologia_count}")
print(f"Ocorrências da palavra 'tecnologias': {tecnologias_count}")

# Usa expressão regular para encontrar palavras que terminam com "esso"
words_ending_with_esso = re.findall(r'\b\w+esso\b', all_text, flags=re.IGNORECASE)

print(f"Palavras que terminam com 'esso': {', '.join(words_ending_with_esso)}")

# Usa expressão regular para encontrar palavras que começam com "tecno"
words_starting_with_tecno = re.findall(r'\btecno\w*\b', all_text, flags=re.IGNORECASE)

print(f"Palavras que começam com 'tecno': {', '.join(words_starting_with_tecno)}")

# Usa expressão regular para encontrar palavras que possuem "ver"
words_with_ver = re.findall(r'\b\w*ver\w*\b', all_text, flags=re.IGNORECASE)

print(f"Palavras que possuem 'ver': {', '.join(words_with_ver)}")

#16) Quantos parágrafos possuem as palavras “sistemas” e “curso”? Para contar os parágrafos que contêm ambas as palavras “sistemas” e “curso”, precisaríamos inspecionar o código HTML da página e verificar os elementos de parágrafo (<p>) que contêm essas palavras. Infelizmente, como não tenho acesso à página em tempo real, não posso fazer isso diretamente aqui.
paragrafos = soup.find_all('p')
cont = 0
for paragrafo in paragrafos:
    if "sistemas" in paragrafo.text.lower() and "curso" in paragrafo.text.lower():
        print("\n", paragrafo.text)
        cont += 1
print("Quantidade =", cont)

#17) Quantas siglas existem na página? Para contar as siglas (palavras escritas em letras maiúsculas), podemos usar a seguinte expressão regular:'''
texto = soup.get_text()
padrao = r'\b[A-ZÀ-Ü][A-ZÀ-Ü]+\b'
palavras = re.findall(padrao, texto)
siglas = set(palavras)
for sigla in siglas:
    print(sigla)
print("Quantidade = ", len(siglas))
# Usa expressão regular para encontrar siglas (letras maiúsculas)
acronyms = re.findall(r'\b[A-Z]{2,}\b', all_text)

print(f"Total de siglas na página: {len(acronyms)}")

