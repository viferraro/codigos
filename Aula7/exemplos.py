import requests
from bs4 import BeautifulSoup
import re

# Faz a requisição HTTP para a página
url = 'https://bsi.uniriotec.br/institucional/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
pagina = BeautifulSoup(response.text, 'html.parser')

# Encontra todos os textos na página
all_text = soup.get_text()

# Encontra todos os links na página
all_links = soup.find_all('a')

# msg = "O Bacharelado em Sistemas de Informação da UNIRIO é um curso vespertino/noturno de graduação com duração prevista de 4 anos, com carga horária total de 3.240 horas-aula em regime de crédito semestral. Atualmente o curso BSI-UNIRIO oferece 72 vagas anuais, com duas entradas semestrais de 36 alunos através do Sistema de Seleção Unificado (SiSU), que é o processo seletivo baseado no resultado do Exame Nacional do Ensino Médio (ENEM)."
# palavra = input("\nDigite texto a ser pesquisado: ")
# if palavra.lower() in msg.lower():
#     print("Existe a palavra '" + palavra + "' na mensagem", )
# else:
#     print("A palavra '" + palavra + "' não existe na mensagem")
    
# tam_msg = len(msg)
# qtde = msg.count(palavra)
# print("A palavra ", palavra, "aparece", qtde, "vezes no texto")

# tam_palavra=len(palavra)
# num = 0
# for i in range(tam_msg):
#     texto = msg[i:i+tam_palavra]
#     if texto.lower() == palavra.lower():
#         num += 1
#         print(str(num) + " - palavra: " + texto + ", posição inicial: " + str(i))
# if num == 0:
#     print("Texto não encontrado")
# print('\n*** Fim da pesquisa\n')

# string = '' 
# for paragrafo in pagina.find_all("p"): 
#     string += paragrafo.text + ' '
# print("string: " + string)

print("------------------------------------------------------------------------")
msg='E agora, José? A festa acabou, a luz apagou, o povo sumiu, a noite esfriou, e agora, José? e agora, você? você que é sem nome, que zomba dos outros, você que faz versos, que ama, protesta? e agora, José?'
print('\n')
padrao = 'a.a.ou'
print('Padrão: "a.a.ou" onde 1 ponto = 1 caractere')
teste = re.findall(padrao, msg)
print(teste)
print('\n')

print('\n')
padrao = 'a[abc]a[abc]ou'
print('Padrão: "a[abc]a[abc]ou"')
teste = re.findall(padrao, msg)
print(teste)

print('\n')
padrao = 'a[a-z]a[bg]ou'
print('Padrão: "a[a-z]a[bg]ou"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')

print('\n')
padrao = 'a[a-z]a[^g]ou'
print('Padrão: "a[a-z]a[^g]ou"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')

print('\n')
padrao = r'a'
print("Padrão: r'a' - quantidade de letras 'a'")
teste = re.findall(padrao, msg)
print(teste)
print(len(teste))
print('\n')
padrao = r'[^a]'
print("Padrão: r'[^a]' - letras que não são 'a'")
teste = sorted(set(re.findall(padrao, msg)))
print(teste)
print('\n')
padrao = r'^a'
print("Padrão: r'^a' - a string começa com 'a'?")
teste = re.findall(padrao, msg)
print(teste)
print('\n')