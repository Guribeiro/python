#Conversor de moedas

#REAIS PARA DÓLAR

import requests
import json


api = requests.get(f'https://economia.awesomeapi.com.br/all/USD')

data = json.loads(api.text)

valorDolar = float(data['USD']['high'])

print(f'Valor do Dólar Americano: R${valorDolar:.2f}')

valorReais = float(input('Valor em Real: '))

valorConvertido = valorReais / valorDolar

print(f'Com R${valorReais:.2f} você poderá comprar US${valorConvertido:.2f} ')
 

