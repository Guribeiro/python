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
    f"\n{cores['boldred']}SELECIONE UM NÚMERO PARA CONSULTAR{cores['limpa']}\n")

for index, valores in zip(moedas.keys(), moedas.values()):
    print(
        f"{cores['boldwhite']}[{index}] - {cores['limpa']}{cores['boldblue']}{valores}{cores['limpa']}")
        

userInput = str(input(f"{cores['boldwhite']}CÓDIGO MOEDA: "))

codigoMoeda = moedas[userInput]

api = requests.get(f'https://economia.awesomeapi.com.br/all/{codigoMoeda}')

data = json.loads(api.text)

valorMoeda = float(data[codigoMoeda]['high'])

valorReais = float(input("Digite o valor em Reais R$ "))

valorConvertido = valorReais / valorMoeda

print(f"Com R${valorReais:.2f} você poderá comprar {codigoMoeda}$ {valorConvertido:.2f} ")



