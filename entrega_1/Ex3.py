import os
import requests
import bs4

output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Caminho completo para o arquivo de saída
output_file = os.path.join(output_dir, "links4.txt")

# Fazendo a requisição para a página 
r = requests.get('https://bsi.uniriotec.br') 
pagina = bs4.BeautifulSoup(r.text, "html.parser")

with open(output_file, "w") as f:
    # a) Mostrando a tag completa do primeiro parágrafo da página    
    primeiro_paragrafo = pagina.find('p') 
    print("Tag completa do primeiro parágrafo:")
    f.write(f"Tag completa do primeiro parágrafo:\n{primeiro_paragrafo}\n")
    # b) Mostrando apenas o texto do primeiro parágrafo 
    print("\nTexto do primeiro parágrafo:")
    f.write(f"Texto do primeiro parágrafo:\n{primeiro_paragrafo.text}\n")
    # c) Mostrando a quantidade de parágrafos que estão dentro de uma div 
    paragrafos_em_div = pagina.select('div p')
    print("\nQuantidade de parágrafos dentro de uma div: " + str(len(paragrafos_em_div)))
    f.write(f"Quantidade de parágrafos dentro de uma div: {str(len(paragrafos_em_div))}\n")

print(f"Saídas salvas em {output_file}")