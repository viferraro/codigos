import requests
from bs4 import BeautifulSoup

# URL da página do BSI
url = 'https://bsi.uniriotec.br/'

# Fazemos uma requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Criamos um objeto BeautifulSoup para analisar o conteúdo HTML
soup = BeautifulSoup(response.content, 'html.parser')

# 1) Número de parágrafos com a palavra "BSI"
paragrafos_bsi = soup.find_all('p', string=lambda text: 'BSI' in text)
num_paragrafos_bsi = len(paragrafos_bsi)
print(f"1) Número de parágrafos com a palavra 'BSI': {num_paragrafos_bsi}")

# 2) Número de parágrafos sem a palavra "BSI"
num_paragrafos_sem_bsi = len(soup.find_all('p')) - num_paragrafos_bsi
print(f"2) Número de parágrafos sem a palavra 'BSI': {num_paragrafos_sem_bsi}")
# 3) Maior parágrafo da página
maior_paragrafo = max(paragrafos_bsi, key=lambda p: len(p.text)).text
print(f"3) Maior parágrafo da página: {maior_paragrafo}")
# 4) Menor parágrafo (não vazio) da página
paragrafos_nao_vazios = [p.text for p in soup.find_all('p') if p.text.strip()]
menor_paragrafo = min(paragrafos_nao_vazios, key=len)
print(f"4) Menor parágrafo (não vazio) da página: {menor_paragrafo}")
# 5) Quantidade de imagens na página
num_imagens = len(soup.find_all('img'))
print(f"5) Quantidade de imagens na página: {num_imagens}")

# 6) Quantidade de imagens com atributo alt
num_imagens_com_alt = len(soup.find_all('img', alt=True))
print(f"6) Quantidade de imagens com atributo alt: {num_imagens_com_alt}")

# 7) Número de comentários na página
num_comentarios = len(soup.find_all(string=lambda text: isinstance(text, Comment)))
print(f"7) Número de comentários na página: {num_comentarios}")

# 8) Quantidade de <span> filhos de <div>
num_span_filhos_div = len(soup.select('div span'))
print(f"8) Quantidade de <span> filhos de <div>: {num_span_filhos_div}")

# 9) Quantidade de âncoras (links) na página
num_ancoras = len(soup.find_all('a'))
print(f"9) Quantidade de âncoras na página: {num_ancoras}")

# 10) Quantidade total de links na página
num_links = len(soup.find_all(['a', 'link'])) 
print(f"10) Quantidade total de links na página: {num_links}")

# 11) Quantidade de links internos (que começam com "/")
num_links_internos = len(soup.find_all('a', href=True, href=lambda href: href.startswith('/')))
print(f"11) Quantidade de links internos: {num_links_internos}")

# 12) Quantidade de elementos com classe "menu-item"
num_menu_items = len(soup.find_all(class_='menu-item'))
print(f"12) Quantidade de elementos com a classe 'menu-item': {num_menu_items}")

# 13) Quantidade de cabeçalhos (h1 a h6) na página
num_cabecalhos = len(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']))
print(f"13) Quantidade de cabeçalhos na página: {num_cabecalhos}")

# 14) Quantidade de tags que não são parágrafos
num_tags_nao_paragrafos = len(soup.find_all(lambda tag: tag.name != 'p'))
print(f"14) Quantidade de tags que não são parágrafos: {num_tags_nao_paragrafos}")

# 15) Quantas vezes a palavra "BSI" aparece na página
ocorrencias_bsi = soup.body.text.count('BSI')
print(f"15) Quantidade de vezes que 'BSI' aparece na página: {ocorrencias_bsi}")

# 16) Quantidade de parágrafos que começam com a letra "O"
paragrafos_com_o = soup.find_all('p', string=lambda text: text.strip().lower().startswith('o'))
num_paragrafos_com_o = len(paragrafos_com_o)
print(f"16) Quantidade de parágrafos que começam com 'O': {num_paragrafos_com_o}")
'''
17) Cite e explique três atributos ou métodos do objeto Tag.
name: O atributo name de um objeto Tag retorna o nome da tag HTML. Por exemplo, se tivermos uma tag <p>, o atributo name retornará a string 'p'.
attrs: O atributo attrs é um dicionário que contém os atributos e seus valores associados à tag. Por exemplo, se tivermos a tag <a href="https://bsi.uniriotec.br/">BSI</a>, o atributo attrs será {'href': 'https://bsi.uniriotec.br/'}.
get_text(): O método get_text() retorna o conteúdo de texto dentro da tag, incluindo o texto de todas as tags filhas. Ele remove as tags e retorna apenas o texto. Por exemplo, se tivermos a tag <p>Olá, <b>mundo</b>!</p>, o método get_text() retornará 'Olá, mundo!'.

18) Explique as características da classe NavigableString.
A classe NavigableString representa o conteúdo de texto dentro de uma tag HTML. Algumas características importantes são:
Conteúdo de Texto: Um objeto NavigableString contém o texto puro (sem tags) dentro de uma tag.
Imutabilidade: Os objetos NavigableString são imutáveis, o que significa que não podemos modificar seu conteúdo após a criação.
Métodos Úteis: Além do próprio texto, os objetos NavigableString têm métodos como strip(), replace(), split(), etc., que podem ser usados para manipular o conteúdo de texto.
19) Qual a diferença entre find_all() e select()?
find_all(): É um método do BeautifulSoup que retorna uma lista de todas as ocorrências de uma tag específica (ou várias tags) no documento HTML. Pode ser usado com argumentos como nome da tag, atributos, expressões regulares, etc.
select(): É um método que permite selecionar elementos usando seletores CSS. Ele retorna uma lista de objetos Tag que correspondem ao seletor especificado. Por exemplo, soup.select('div.menu-item') seleciona todas as tags <div> com a classe “menu-item”.
20) Para que serve o atributo .string? O atributo .string de um objeto Tag retorna o conteúdo de texto dentro da tag, excluindo o texto de tags filhas. Se a tag contiver apenas texto direto (sem outras tags), o atributo .string retornará esse texto. Caso contrário, ele retornará None.
21) Para que serve o atributo .text? O atributo .text de um objeto Tag retorna todo o conteúdo de texto dentro da tag, incluindo o texto de tags filhas. Ele remove as tags e retorna apenas o texto. Por exemplo, se tivermos a tag <p>Olá, <b>mundo</b>!</p>, o atributo .text retornará 'Olá, mundo!'.
22) Qual a diferença entre os atributos .string e .text? A diferença entre os atributos .string e .text está na inclusão do texto de tags filhas:
.string: Retorna apenas o texto direto da tag (excluindo o texto de tags filhas).
.text: Retorna todo o conteúdo de texto dentro da tag, incluindo o texto de tags filhas.
23) Qual a diferença entre .string e .text? A diferença entre .string e .text é a seguinte:
.string: Retorna apenas o texto direto da tag (excluindo o texto de tags filhas).
.text: Retorna todo o conteúdo de texto dentro da tag, incluindo o texto de tags filhas.
24) Para que serve o atributo .contents? O atributo .contents de um objeto Tag retorna uma lista com todos os elementos filhos diretos da tag, incluindo tanto texto quanto outras tags. É útil para iterar sobre os elementos filhos e manipulá-los.

25) Para que serve o atributo .parent? O atributo .parent de um objeto Tag retorna o elemento pai (tag pai) da tag atual. Por exemplo, se tivermos a seguinte estrutura HTML:
<div>
    <p>Olá, mundo!</p>
</div>
Se selecionarmos a tag <p>, o atributo .parent retornará a tag <div>.

26) Qual a diferença entre .next_sibling e .next_element?
.next_sibling: Retorna o próximo irmão (elemento imediatamente após) da tag atual, incluindo tanto tags quanto texto.
.next_element: Retorna o próximo elemento (tag ou texto) que não é um irmão, mas está na mesma árvore de análise.
'''

# 27) Forneça um exemplo para find_next_siblings(). O método find_next_siblings() retorna #uma lista de todos os irmãos (elementos subsequentes) da tag atual. Por exemplo:
# Suponha que temos o seguinte HTML:
# <ul>
#     <li>Item 1</li>
#     <li>Item 2</li>
#     <li>Item 3</li>
# </ul>
ul_tag = soup.find('ul')
li_tags = ul_tag.find_all('li')
# Encontrar os irmãos do primeiro <li>
irmaos_do_primeiro_li = li_tags[0].find_next_siblings('li')
for irmao in irmaos_do_primeiro_li:
    print(irmao.text)
# Suponha que temos o seguinte HTML:
# <ul>
#     <li>Item 1</li>
#     <li>Item 2</li>
#     <li>Item 3</li>
# </ul>
ul_tag = soup.find('ul')
li_tags = ul_tag.find_all('li')
# Encontrar os irmãos do primeiro <li>
irmaos_do_primeiro_li = li_tags[0].find_next_siblings('li')
for irmao in irmaos_do_primeiro_li:
    print(irmao.text)
#Isso imprimirá os textos dos elementos irmãos subsequentes do primeiro <li> (ou seja, “Item 2” e “Item 3”).

'''
28) Para que serve o “html.parser”? O "html.parser" é um analisador HTML embutido no BeautifulSoup. Ele é usado para analisar documentos HTML e criar uma árvore de análise. É uma opção padrão quando você cria um objeto BeautifulSoup. No entanto, existem outras alternativas de analisadores, como lxml e html5lib.
29) Existem alternativas para o “html.parser”? Sim, existem alternativas para o "html.parser":
lxml: Um analisador rápido e eficiente que suporta tanto HTML quanto XML. Pode ser instalado com pip install lxml.
html5lib: Um analisador que segue as especificações do HTML5. É mais lento que o lxml, mas lida bem com HTML malformado. Pode ser instalado com pip install html5lib.
30) Para que serve o parâmetro “recursive=True” no método find()? O parâmetro recursive=True no método find() indica que a busca deve ser realizada em profundidade, ou seja, dentro dos filhos, netos, bisnetos e assim por diante da tag atual. Se definido como False, a busca será restrita apenas aos filhos diretos da tag.
'''
# 31) Grave a página do BSI em um arquivo local. Leia o arquivo e mostre o conteúdo da página. Para salvar a página do BSI em um arquivo local, podemos fazer o seguinte:
with open('bsi_page.html', 'w', encoding='utf-8') as arquivo:
    arquivo.write(response.content.decode('utf-8'))
# Depois de salvar o arquivo, podemos lê-lo e mostrar o conteúdo:
with open('bsi_page.html', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
# Isso exibirá o conteúdo HTML da página salva.
'''
32) Para que servem as expressões regulares? As expressões regulares (ou regex) são padrões de busca usados para encontrar e manipular strings de texto com base em regras específicas. Elas são amplamente utilizadas para:
Buscar e substituir padrões em texto.
Validar formatos de dados (por exemplo, verificar se um email está no formato correto).
Extrair informações específicas de um texto (por exemplo, encontrar números de telefone ou URLs).

33) Diferencie o WebBrowser e o BeautifulSoup.
WebBrowser:
É um navegador web real que permite aos usuários interagir com páginas da web, visualizar conteúdo, preencher formulários, clicar em links e executar ações semelhantes a um usuário humano.
Pode ser usado para testes automatizados, automação de tarefas, raspagem de dados, entre outros.
Exemplos de navegadores reais incluem Google Chrome, Mozilla Firefox, Microsoft Edge, etc.
BeautifulSoup:
É uma biblioteca Python usada para analisar e extrair informações de documentos HTML ou XML.
Não é um navegador real, mas sim um analisador de documentos. Ele não executa JavaScript, não carrega imagens ou estilos e não interage com páginas da web.
O BeautifulSoup permite que os desenvolvedores extraiam dados específicos de uma página, como texto, links, imagens e outras informações, sem a necessidade de renderizar a página completa.
É amplamente utilizado para web scraping, análise de dados e extração de informações de páginas da web.
Em resumo, o WebBrowser é um navegador real usado para interagir com páginas da web, enquanto o BeautifulSoup é uma ferramenta para analisar e extrair dados de documentos HTML ou XML.

34) Explique o que é e para que serve o XPath.
XPath é uma linguagem de consulta usada para navegar e selecionar elementos em documentos XML ou HTML.
Ele permite que você especifique caminhos para localizar elementos em uma árvore hierárquica de tags.
Com XPath, você pode:
Selecionar elementos por nome de tag, atributos, valores de atributos, posição, etc.
Navegar para cima (para o pai), para baixo (para os filhos) e para os lados (para os irmãos) na árvore de elementos.
Realizar consultas complexas para extrair informações específicas de um documento.
É amplamente usado em web scraping, testes automatizados, extração de dados e análise de documentos XML/HTML.
'''
