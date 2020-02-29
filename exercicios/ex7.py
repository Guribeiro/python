#TABUADA

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

print(f"{cores['boldwhite']}{' TABUADA ':=^30}")

num = int(input('Digite um número: '))
#tab = int(input('Tabuada: '))

for index in range(0, 11):
    print(f'{num:2} X {index:2} = {num * index:2}')
    
    #if index > 10:
    #    print(f"{cores['limpa']}")
        
