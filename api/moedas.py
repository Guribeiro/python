import requests
import json

cores = {
    'limpa': '\033[m',
    'boldblue': '\033[1;30m',
    'boldred': '\033[1;31m',
    'boldgreen': '\033[1;32m',
    'boldyellow': '\033[1;33m',
    'boldpink': '\033[1;34m',
    'boldpurple': '\033[1;35m',
    'boldoceanblue': '\033[1;36m',
    'boldwhite': '\033[1;37m',
}
moedas = {
    '1': 'USD',
    '2': 'USDT',
    '3': 'CAD',
    '4': 'AUD',
    '5': 'EUR',
    '6': 'GBP',
    '7': 'ARS',
    '8': 'JPY',
    '9': 'CHF',
    '10': 'CNY',
    '11': 'YLS',
    '12': 'BTC',
    '13': 'LTC',
    '14': 'ETH',
    '15': 'XRP',
}


print(f"{cores['boldoceanblue']}{' API DE MOEDAS ':=^30}{cores['limpa']}")

print(
    F"\n{cores['boldred']}SELECIONE UM NÚMERO PARA CONSULTAR{cores['limpa']}\n")

'''
print(f"{cores['boldwhite']}[1] - {cores['limpa']}{cores['boldblue']}USD-BRL (Dólar Comercial){cores['limpa']}")
print(f"{cores['boldwhite']}[2] - {cores['limpa']}{cores['boldblue']}USDT-BRL (Dólar Turismo){cores['limpa']}")
print(f"{cores['boldwhite']}[3] - {cores['limpa']}{cores['boldblue']}CAD-BRL (Dólar Canadense){cores['limpa']}")
print(f"{cores['boldwhite']}[4] - {cores['limpa']}{cores['boldblue']}AUD-BRL (Dólar Australiano){cores['limpa']}")
print(f"{cores['boldwhite']}[5] - {cores['limpa']}{cores['boldblue']}EUR-BRL (Euro){cores['limpa']}")
print(f"{cores['boldwhite']}[6] - {cores['limpa']}{cores['boldblue']}GBP-BRL (Libra Esterlina){cores['limpa']}")
print(f"{cores['boldwhite']}[7] - {cores['limpa']}{cores['boldblue']}ARS-BRL (Peso Argentino){cores['limpa']}")
print(f"{cores['boldwhite']}[8] - {cores['limpa']}{cores['boldblue']}JPY-BRL (Iene Japonês){cores['limpa']}")
print(f"{cores['boldwhite']}[9] - {cores['limpa']}{cores['boldblue']}CHF-BRL (Franco Suíço){cores['limpa']}")
print(f"{cores['boldwhite']}[10] - {cores['limpa']}{cores['boldblue']}CNY-BRL (Yuan Chinês){cores['limpa']}")
print(f"{cores['boldwhite']}[11] - {cores['limpa']}{cores['boldblue']}YLS-BRL (Novo Shekel Israelense){cores['limpa']}")
print(f"{cores['boldwhite']}[12] - {cores['limpa']}{cores['boldblue']}BTC-BRL (Bitcoin){cores['limpa']}")
print(f"{cores['boldwhite']}[13] - {cores['limpa']}{cores['boldblue']}LTC-BRL (Litecoin){cores['limpa']}")
print(f"{cores['boldwhite']}[14] - {cores['limpa']}{cores['boldblue']}ETH-BRL (Ethereum){cores['limpa']}")
print(f"{cores['boldwhite']}[15] - {cores['limpa']}{cores['boldblue']}XRP-BRL (Ripple){cores['limpa']}")
'''

for index, valores in zip(moedas.keys(), moedas.values()):
    print(
        f"{cores['boldwhite']}[{index}] - {cores['limpa']}{cores['boldblue']}{valores}{cores['limpa']}")

userInput = str(input(f"{cores['boldwhite']}CÓDIGO MOEDA: "))

codigoMoeda = moedas[userInput]

api = requests.get(f'https://economia.awesomeapi.com.br/all/{codigoMoeda}')

data = json.loads(api.text)

codeMoeda = data[codigoMoeda]['code']
codeinMoeda = data[codigoMoeda]['codein']
nameMoeda = data[codigoMoeda]['name']
highMoeda = data[codigoMoeda]['high']
lowMoeda = data[codigoMoeda]['low']

print(f"{' ':=^20}{cores['limpa']}")

print(f'''{cores['boldgreen']}CODE: {cores['limpa']} {cores['boldwhite']} {codeMoeda}{cores['limpa']}
         \n{cores['boldgreen']}CODEIN: {cores['limpa']} {cores['boldwhite']}{codeinMoeda}{cores['limpa']}
         \n{cores['boldgreen']}NAME: {cores['limpa']} {cores['boldwhite']} {nameMoeda} {cores['limpa']}
         \n{cores['boldgreen']}HIGH: {cores['limpa']} {cores['boldwhite']} {highMoeda} {cores['limpa']}
         \n{cores['boldgreen']}LOW: {cores['limpa']} {cores['boldwhite']} {lowMoeda} {cores['limpa']}
         ''')


# strip get 1st string element as key

#so far so good...