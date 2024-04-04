import os
import requests
import bs4

# Crie um diretório chamado "output" na mesma pasta do arquivo .py
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Caminho completo para o arquivo de saída
output_file = os.path.join(output_dir, "links.txt")

# Realize a requisição HTTP e analise a página
r = requests.get('https://bsi.uniriotec.br')
pagina = bs4.BeautifulSoup(r.text, "html.parser")
links = pagina.find_all('a')

# Imprima a quantidade de links
print('Quantidade de links =', len(links))

# Abra o arquivo de saída em modo de anexação ("a")
with open(output_file, "a") as f:
    # Escreva a quantidade de links no arquivo
    f.write(f"Quantidade de links = {len(links)}\n")

    # Escreva cada link no arquivo
    for link in links:
        href = link.get('href')
        if href:
            print(href)
            # Escreva o link no arquivo de saída
            f.write(href + "\n")

print(f"Saídas salvas em {output_file}")

