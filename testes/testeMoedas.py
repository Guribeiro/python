
moedas = {
    '1':'USD',
    '2':'USDT',
    '3':'CAD',
    '4':'AUD',
    '5':'EUR',
    '6':'GBP',
    '7':'ARS',
    '8':'JPY',
    '9':'CHF',
    '10':'CNY',
    '11':'YLS',
    '12':'BTC',
    '13':'LTC',
    '14':'ETH',
    '15':'XRP',
}

print(f"{moedas['1']}")
'''
for index, valores in zip(moedas.keys(), moedas.values()):
    print(index, valores)
'''

'''
import requests
import json

api = requests.get('https://economia.awesomeapi.com.br/all')

data =  json.loads(api.text)

print(data['USD'])
'''