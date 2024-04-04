import requests
from requests.exceptions import ConnectionError
import urllib.request
import json
from geopy.geocoders import Nominatim

# # teste 1

# import requests
# resp = requests.get('http://bsi.uniriotec.br')
# print("Codigo de retorno = " + str(resp.status_code))

# # teste 2
# resp = requests.get('http://bsi.uniriotec.br/professoras')
# print("Codigo de retorno = " + str(resp.status_code))

# # teste 3
# try:
#     requests.get("https://bsi2.uniriotec.br")
# except ConnectionError:
#     print("Site não existe")
# else:
#     print('Site existe')

# # teste 4
# r = requests.get('http://bsi.uniriotec.br')
# print("*** Conteúdo da página em bytes ***")
# print(r.content)
# print("\n*** Conteúdo da página codificado ***")
# print(r.text)

# # teste 5
# resp = requests.get('http://bsi.uniriotec.br')
# print("*** Cabeçalhos da página ***")
# print(resp.headers)

# teste 6
# resp = requests.get('https://bsi.uniriotec.br')
# print(resp.headers)
# print("*** Cabeçalhos da página ***")
# print("Data: " + resp.headers['Date'])
# print("Servidor: " + resp.headers['Server'])
# print("Link: " + resp.headers['Link'])
# print("Conteúdo: " + resp.headers['Content-Type'])

# # teste 7
# pagina = requests.get('http://bsi.uniriotec.br')
# print("Página: " + pagina.url)
# print("Codificação: " + pagina.encoding)

# arq = open("copia.html", "w")
# arq.write(pagina.text)
# arq.close()
# print('Arquivo ' + arq.name + ' gravado')

# # teste 8
# resp = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")
# obj = json.loads(resp.read())
# print(obj)
# latitude = obj['iss_position']['latitude']
# longitude = obj['iss_position']['longitude']
# #geoLoc = Nominatim(user_agent="GetPrayagraj")
# geoLoc = Nominatim(user_agent="my_app")
# coord = str(latitude + "," + longitude)
# locname = geoLoc.reverse(coord)
# print(locname)

#codigo que gera distancia entre duas coordenadas
from geopy.distance import geodesic
coord1 = (-40.3886, 138.31228)
coord2 = (-22.954729515024212, -43.16876723147655) # -22.954729515024212, -43.16876723147655
print(geodesic(coord1, coord2).kilometers, 'km')



