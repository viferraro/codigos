import os
import requests
import bs4

output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Caminho completo para o arquivo de saída
output_file = os.path.join(output_dir, "links2.txt")

r = requests.get('https://bsi.uniriotec.br')

# Realize a requisição HTTP e analise a página
pagina = bs4.BeautifulSoup(r.text, "html.parser")  
links = pagina.select('a[href]')

# Imprima a quantidade de links
print('Quantidade de links =', len(links))

# Abra o arquivo de saída em modo de anexação ("a")
with open(output_file, "w") as f:
    # Escreva a quantidade de links no arquivo
    f.write(f"Quantidade de links = {len(links)}\n")

    # Escreva cada link no arquivo   
    print("\nNúmero de links: " + str(len(links)))  
    for link in links:  
        print(link.get('href'))  # Modificado para imprimir apenas o atributo 'href' do link
        # Escreva o link no arquivo de saída
        f.write(f"{link.get('href')}\n")  # Modificado para escrever apenas o atributo 'href' do link

print(f"Saídas salvas em {output_file}")