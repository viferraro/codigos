import os
import requests
import bs4

output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Caminho completo para o arquivo de saída
output_file = os.path.join(output_dir, "links3.txt")

r = requests.get('https://bsi.uniriotec.br') 
pagina = bs4.BeautifulSoup(r.text, "html.parser") 
paragrafos = pagina.select('p[class]') 
print("\nNúmero de parágrafos com classe CSS: " + 
str(len(paragrafos)))

# Abra o arquivo de saída em modo de anexação ("a")
with open(output_file, "a") as f:
    # Escreva a quantidade de links no arquivo
    f.write(f"\n 'Número de parágrafos com classe CSS: ' {str(len(paragrafos))}")

    for paragrafo in paragrafos: 
        print(paragrafo)
        f.write(f"{paragrafo}\n")

print(f"Saídas salvas em {output_file}")

    