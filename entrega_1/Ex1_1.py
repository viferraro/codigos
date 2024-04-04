import os
import requests
import bs4

r = requests.get('https://bsi.uniriotec.br')
pagina = bs4.BeautifulSoup(r.text, "html.parser")
links = pagina.find_all('a')

# Usando um conjunto para armazenar links únicos
links_unicos = set()

print('Quantidade de links =', len(links))

for link in links:
    href = link.get('href')
    if href and href not in links_unicos:
        links_unicos.add(href)
        if len(links_unicos) <= 6:  # Limita a quantidade de links únicos a 5
            print(f"Cinco primeiros links: {href}")
                


# output_dir = "output"
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# output_file = os.path.join(output_dir, "5links.txt")

# r = requests.get('https://bsi.uniriotec.br')
# pagina = bs4.BeautifulSoup(r.text, "html.parser")
# links = pagina.find_all('a')

# # Usando um conjunto para armazenar links únicos
# links_unicos = set()

# print('Quantidade de links =', len(links))

# with open(output_file, "w") as f:  # Mudar para "w" para sobrescrever o arquivo existente
#     f.write(f"Quantidade de links = {len(links)}\n")
#     for link in links:
#         href = link.get('href')
#         if href and href not in links_unicos:
#             links_unicos.add(href)
#             if len(links_unicos) <= 6:  # Limita a quantidade de links únicos a 5
#                 print(href)
#                 f.write(href + "\n")

# print(f"Saídas salvas em {output_file}")