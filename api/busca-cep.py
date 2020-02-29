import requests
import json

word = ' Busca-cep '

print(f'{word:=^30}')
usercep = str(input('Informe seu CEP: '))

api = requests.get(f'https://viacep.com.br/ws/{usercep}/json/')

#cepdata = json.loads(api.text)

print(api.text)