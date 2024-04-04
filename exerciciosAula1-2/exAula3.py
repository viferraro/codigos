'''
1.	O código faz uma requisição GET para “https://example.com”. 
Se o status da resposta não for 200, ele levanta uma exceção personalizada. 
Se ocorrer um erro na requisição, ele imprime o erro. Se ocorrer a exceção personalizada, 
ele imprime a mensagem de erro.
'''
import requests  # Importa a biblioteca requests
class CustomException(Exception):  # Define uma classe de exceção personalizada
    pass
try:  # Inicia um bloco try
    response = requests.get("https://example.com")  # Faz uma requisição GET para "https://example.com"
    if response.status_code != 200:  # Verifica se o código de status da resposta é diferente de 200
        raise CustomException("Atenção - " + str(response.status_code))  # Se for, lança uma exceção personalizada
    print("Request successful!")  # Se o código de status for 200, imprime "Request successful!"
except requests.exceptions.RequestException as e:  # Se ocorrer uma exceção do tipo RequestException
    print("Um erro ocorreu:", e)  # Imprime a mensagem de erro
except CustomException as e:  # Se ocorrer uma exceção do tipo CustomException
    print("Erro :", e)  # Imprime a mensagem de erro

###################################################################################################
'''
2.	Este código faz uma requisição GET para “https://example.com” e 
registra qualquer erro em um arquivo de log chamado “erros.log”. S
e a requisição for bem-sucedida, ele imprime uma mensagem de sucesso.
'''
import requests  # Importa a biblioteca requests
import logging  # Importa a biblioteca logging
logging.basicConfig(filename="erros.log", level=logging.ERROR)  # Configura o logging para gravar erros em um arquivo chamado "erros.log"
try:  # Inicia um bloco try
    response = requests.get("https://example.com")  # Faz uma requisição GET para "https://example.com"
    response.raise_for_status()  # Lança uma exceção se o código de status HTTP for 4xx ou 5xx
    print("Página obtida com sucesso!")  # Se o código de status for 200, imprime "Página obtida com sucesso!"
except requests.exceptions.RequestException as e:  # Se ocorrer uma exceção do tipo RequestException
    logging.error("Um erro ocorreu: %s", e)  # Registra a mensagem de erro no arquivo de log

####################################################################################################
'''
3.	Este código tenta fazer uma requisição GET para ‘https://bsi.uniriotec.br’ 
com um tempo limite de 0.01 segundos. Se a requisição demorar mais do que o tempo limite, 
ele imprime ‘Timeout’.
'''
import requests  # Importa a biblioteca requests
from requests.exceptions import ConnectTimeout  # Importa a classe ConnectTimeout da biblioteca requests.exceptions
try:  # Inicia um bloco try
    tempo = requests.get('https://bsi.uniriotec.br', timeout=0.01).elapsed.total_seconds()  # Faz uma requisição GET para 'https://bsi.uniriotec.br' com um tempo limite de 0,01 segundos e obtém o tempo total em segundos
    print(tempo)  # Imprime o tempo total
except ConnectTimeout:  # Se ocorrer uma exceção do tipo ConnectTimeout
    print('Timeout')  # Imprime 'Timeout'

####################################################################################################
'''
4.	Este código faz uma requisição GET para ‘https://reqbin.com/echo’ com cabeçalhos 
personalizados e imprime todos os cabeçalhos da resposta.
'''
import requests  # Importa a biblioteca requests
url = 'https://reqbin.com/echo'  # Define a URL
headers = {'Accept': '*/*', 'X-User-IP': '1.1.1.1'}  # Define os cabeçalhos da requisição
r = requests.get(url, headers=headers)  # Faz uma requisição GET para a URL com os cabeçalhos definidos
for key, val in r.headers.items():  # Para cada par chave-valor nos cabeçalhos da resposta
    print(key, ':', val)  # Imprime a chave e o valor

####################################################################################################
'''
5.	Este código faz uma requisição GET para ‘http://httpbin.org/headers’ e imprime 
o status da resposta e o texto da resposta. O agente do usuário é uma string 
que o navegador envia ao servidor para informar qual é o navegador e 
o sistema operacional do cliente.
'''
import requests  # Importa a biblioteca requests
response = requests.get('http://httpbin.org/headers')  # Faz uma requisição GET para 'http://httpbin.org/headers'
print(response.status_code)  # Imprime o código de status da resposta
print(response.text)  # Imprime o corpo da resposta

#Pergunta: Quem é o agente do usuário? O agente do usuário é o software que está fazendo
''' 
a requisição HTTP. Ele é identificado pelo cabeçalho 'User-Agent' na requisição.
O agente do usuário é uma string que o navegador ou aplicativo envia para cada site visitado. 
Ele contém informações sobre o navegador e o sistema operacional do usuário. 
Isso é útil para os servidores web para fornecer conteúdo que seja compatível com o 
navegador ou dispositivo do usuário.
No código que você forneceu, o agente do usuário é definido pela biblioteca requests 
quando você faz uma requisição GET para ‘http://httpbin.org/headers’. 
A resposta desta requisição incluirá os cabeçalhos HTTP enviados na requisição, incluindo o ‘User-Agent’. Você pode ver o agente do usuário imprimindo response.text.
Aqui está um exemplo de como você pode extrair o agente do usuário da resposta:
'''
# import requests
# import json
# response = requests.get('http://httpbin.org/headers')
# data = json.loads(response.text)
# print("Agente do usuário:", data['headers']['User-Agent'])
'''
Este código fará uma requisição GET para ‘http://httpbin.org/headers’, converterá a resposta JSON 
em um dicionário Python e imprimirá o agente do usuário. Note que ‘User-Agent’ é case-sensitive.
'''
####################################################################################################
'''
6.	Este código faz uma requisição POST para “https://httpbin.org/post” com um corpo JSON e 
imprime o status da resposta e a resposta JSON.
'''
import requests  # Importa a biblioteca requests
import json  # Importa a biblioteca json
url = "https://httpbin.org/post"  # Define a URL
headers = {"Content-Type": "application/json; charset=utf-8"}  # Define os cabeçalhos da requisição
data = {  # Define os dados que serão enviados na requisição
    "id": 1001,
    "name": "geek",
    "passion": "coding",
}
response = requests.post(url, headers=headers, json=data)  # Faz uma requisição POST para a URL com os cabeçalhos e os dados definidos
print("Status Code:", response.status_code)  # Imprime o código de status da resposta
print("JSON Response: ", response.json())  # Imprime o corpo da resposta como JSON

####################################################################################################
'''
7.	Este código faz uma requisição GET para “http://www.example.com”, 
obtém os cookies da resposta e imprime os nomes e valores dos cookies.
'''
import requests  # Importa a biblioteca requests
response = requests.get("http://www.example.com")  # Faz uma requisição GET para "http://www.example.com"
cookies = response.cookies  # Obtém os cookies da resposta
print(cookies)  # Imprime os cookies
for cookie in cookies:  # Para cada cookie nos cookies
    print(cookie.name, cookie.value)  # Imprime o nome e o valor do cookie

####################################################################################################
'''
8.	Este código faz uma requisição POST para “http://httpbin.org/post” com 
um corpo JSON e imprime a resposta e os cabeçalhos da resposta.
'''
import requests  # Importa a biblioteca requests
import json  # Importa a biblioteca json
url = "http://httpbin.org/post"  # Define a URL
dados = {  # Define os dados que serão enviados na requisição
    "nome": "aluno",
    "email": "aluno@edu.unirio.br"
}
json_dados = json.dumps(dados)  # Converte os dados para JSON
resp = requests.post(url, data=json_dados)  # Faz uma requisição POST para a URL com os dados em JSON
print(resp.text)  # Imprime o corpo da resposta
print("******")
print(resp.headers)  # Imprime os cabeçalhos da resposta
print("******")

####################################################################################################
'''
9.	Este código faz uma requisição POST para “https://httpbin.org/post” 
com um corpo codificado em URL e imprime a resposta.
'''
import urllib.request  # Importa o módulo request da biblioteca urllib
import urllib.parse  # Importa o módulo parse da biblioteca urllib
url = "https://httpbin.org/post"  # Define a URL
dados = {'nome': 'Maria', 'email': 'maria@unirio,br'}  # Define os dados que serão enviados na requisição
codificacao = urllib.parse.urlencode(dados).encode('utf-8')  # Codifica os dados em URL e converte para bytes
req = urllib.request.Request(url, data=codificacao, method='POST')  # Cria uma requisição POST com a URL e os dados codificados
response = urllib.request.urlopen(req)  # Abre a URL com a requisição
resp = response.read()  # Lê a resposta
print(resp)  # Imprime a resposta

####################################################################################################
'''
10.	Este código analisa a URL “https://www.google.com.br/search?q=unirio” e 
imprime o esquema, o local na rede, o caminho e a consulta da URL.
'''
from urllib.parse import urlparse  # Importa a função urlparse da biblioteca urllib.parse
#url = "https://www.example.com/page?query=value"
url = "https://www.google.com.br/search?q=unirio"  # Define a URL
parsed_url = urlparse(url)  # Analisa a URL e retorna um objeto ParseResult
print("Scheme:", parsed_url.scheme)  # Imprime o esquema da URL (http, https, etc.)
print("Netloc:", parsed_url.netloc)  # Imprime a localização da rede da URL (domínio)
print("Path:", parsed_url.path)  # Imprime o caminho da URL
print("Query:", parsed_url.query)  # Imprime a query da URL

####################################################################################################
'''
11.	Este código analisa a URL ‘http://user:pass@NetLoc:80/path;parameters?query=argument#fragment’ 
e imprime várias partes da URL, incluindo o esquema, o local na rede, o caminho, os parâmetros, 
a consulta, o fragmento, o nome de usuário, a senha, o nome do host e a porta.
'''
from urllib.parse import urlparse  # Importa a função urlparse da biblioteca urllib.parse
parsed = urlparse('http://user:pass@NetLoc:80/path;parameters?query=argument#fragment')  # Analisa a URL e retorna um objeto ParseResult
print('scheme :', parsed.scheme)  # Imprime o esquema da URL (http, https, etc.)
print('netloc :', parsed.netloc)  # Imprime a localização da rede da URL (domínio)
print('path :', parsed.path)  # Imprime o caminho da URL
print('params :', parsed.params)  # Imprime os parâmetros da URL
print('query :', parsed.query)  # Imprime a query da URL
print('fragment:', parsed.fragment)  # Imprime o fragmento da URL
print('username:', parsed.username)  # Imprime o nome de usuário da URL
print('password:', parsed.password)  # Imprime a senha da URL
print('hostname:', parsed.hostname, '(netloc in lower case)')  # Imprime o nome do host da URL (localização da rede em minúsculas)
print('port :', parsed.port)  # Imprime a porta da URL

####################################################################################################
'''
12.	Este código analisa a URL ‘http://netloc/path;parameters?query=argument#fragment’, 
imprime a URL original, a URL analisada, a tupla da URL analisada e a nova URL gerada a 
partir da tupla.
'''
from urllib.parse import urlparse, urlunparse  # Importa as funções urlparse e urlunparse da biblioteca urllib.parse
original = 'http://netloc/path;parameters?query=argument#fragment'  # Define a URL original
print('ORIG :', original)  # Imprime a URL original
parsed = urlparse(original)  # Analisa a URL e retorna um objeto ParseResult
print('PARSED:', type(parsed), parsed)  # Imprime o tipo do objeto ParseResult e o objeto em si
t = parsed[:]  # Cria uma tupla a partir do objeto ParseResult
print('TUPLE :', type(t), t)  # Imprime o tipo da tupla e a tupla em si
print('NEW :', urlunparse(t))  # Reconstrói a URL a partir da tupla e imprime a nova URL

####################################################################################################
'''
13.	Este código codifica a URL ‘https://mail.google.com/mail/u/0/?tab = rm#inbox’ 
e depois decodifica a URL codificada.
'''
from urllib.parse import quote, unquote  # Importa as funções quote e unquote da biblioteca urllib.parse
url = 'https://mail.google.com/mail/u/0/?tab = rm#inbox'  # Define a URL
q = quote(url)  # Codifica a URL para uma string segura para ser incluída como parte de uma URL
print(q)  # Imprime a URL codificada
print(unquote(q))  # Decodifica a URL codificada e imprime a URL original

####################################################################################################
'''
14.	Este código analisa a URL ‘https://www.example.com/search?q=python&sort=recent’, 
imprime a consulta da URL e os parâmetros da consulta.
'''
from urllib.parse import urlparse  # Importa a função urlparse da biblioteca urllib.parse
url = 'https://www.example.com/search?q=python&sort=recent'  # Define a URL
parsed_url = urlparse(url)  # Analisa a URL e retorna um objeto ParseResult
print(parsed_url.query)  # Imprime a query da URL
query_params = dict(qc.split("=") for qc in parsed_url.query.split("&"))  # Cria um dicionário a partir da query da URL
print(query_params)  # Imprime o dicionário

####################################################################################################
'''
15.	Este código analisa a URL ‘https://www.example.com/about#history’ e imprime o fragmento da URL.
'''
from urllib.parse import urlparse  # Importa a função urlparse da biblioteca urllib.parse
url = 'https://www.example.com/about#history'  # Define a URL
parsed_url = urlparse(url)  # Analisa a URL e retorna um objeto ParseResult
print(parsed_url.fragment)  # Imprime o fragmento da URL

####################################################################################################
'''
16.	Este código gera uma URL a partir de uma lista de componentes de URL.
'''
from urllib.parse import urlunparse  # Importa a função urlunparse da biblioteca urllib.parse
data = ['https', 'www.example.com', '/path/to/page', None, 'key1=value1&key2=value2', 'Somewhere']  # Define uma lista com as partes de uma URL
print(urlunparse(data))  # Reconstrói a URL a partir da lista e imprime a URL

####################################################################################################
'''
17.	Este código analisa a URL “https://www.example.com/search?q=python&sort=recent”, 
verifica se o esquema é “https” e, em caso afirmativo, imprime o host e o caminho da URL.
'''
from urllib.parse import urlparse  # Importa a função urlparse da biblioteca urllib.parse
scheme, host, path, params, query, fragment = urlparse("https://www.example.com/search?q=python&sort=recent")  # Analisa a URL e desempacota o objeto ParseResult

if scheme == "https":  # Verifica se o esquema da URL é "https"
    print("host", "=>", host)  # Se for, imprime o host da URL
    if params:  # Verifica se a URL tem parâmetros
        path = path + ";" + params  # Se tiver, adiciona os parâmetros ao caminho
    if query:  # Verifica se a URL tem uma query
        path = path + "?" + query  # Se tiver, adiciona a query ao caminho
    print("path", "=>", path)  # Imprime o caminho

####################################################################################################
'''
18.	Este código divide a URL ‘https://www.example.com/search?q=python&sort=recent’ 
no caractere ‘?’ e imprime a parte da URL antes do ‘?’.
'''
test_str = 'https://www.example.com/search?q=python&sort=recent'  # Define a string de teste com uma URL
print("O string original: " + str(test_str))  # Imprime a string de teste
res = test_str.split('?')[0]  # Divide a string de teste no caractere '?' e pega a primeira parte (a base da URL)
print("A base da URL: " + res)  # Imprime a base da URL

