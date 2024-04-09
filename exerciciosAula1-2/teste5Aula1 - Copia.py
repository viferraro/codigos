import webbrowser

pesquisa = input('Pesquisar no Google: ')
webbrowser.open('https://www.google.com.br/search?&q=%s' %pesquisa)