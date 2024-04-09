import requests
r = requests.get('https://bsi.uniriotec.br')
if r:
    print('Resposta OK')
else:
    print('Resposta ERRO')
print("Codigo de retorno = " + str(r.status_code))