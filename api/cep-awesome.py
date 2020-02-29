import requests
import json
import time
import datetime

cores = {
    'limpa': '\033[m',
    'boldblue':'\033[1;30m',
    'boldred':'\033[1;31m',
    'boldgreen':'\033[1;32m',
    'boldyellow':'\033[1;33m',
    'boldpink':'\033[1;34m',
    'boldpurple':'\033[1;35m',
    'boldoceanblue':'\033[1;36m',
    'boldwhite':'\033[1;37m',
}


print(f"{cores['boldwhite']}{' AWESOME CEP ':=^30}{cores['limpa']}")

usercep = str(input(f"{cores['boldoceanblue']}Digite seu CEP: {cores['limpa']}"))



#while True: 
timeCount = datetime.datetime.now()
api = requests.get(f'https://cep.awesomeapi.com.br/json/{usercep}')

#print('{}ENDEREÇO{}'.format('= ' * 20,' =' * 20))
print(f"{cores['boldwhite']}{'ENDEREÇO':^30}{cores['limpa']}")

datacep = json.loads(api.text)
cep = datacep['cep']
rua = datacep['address_name']
bairro = datacep['district']
cidade = datacep['city']
estado = datacep['state']


print(f"{cores['boldpink']}Cep: {usercep}\nRua: {rua}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}{cores['limpa']}")

print(f"{cores['boldred']}Time: {timeCount.hour}:{timeCount.minute}:{timeCount.second}{cores['limpa']}")
    #time.sleep(10)