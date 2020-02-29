
program = ' Cáculo média '
arr = []
soma = 0
state = ''

print(f'{program:=^30}')
countNotas = int(input('Quantas notas deseja inserir ?\n: '))

for item in range(1, countNotas + 1):
    nota = float(input(f'{item}º Nota: '))
    if nota < 0:
        print('Erro! Valores negativos não são aceitos ')
        
    elif nota > 10:
        print('Erro! Valores superiores a 10 não são aceitos')
    else:
        arr.append(nota)

for index in range(0, len(arr)):
    soma = soma + arr[index]

media = soma/len(arr)

if media < 6:
    state = 'REPROVADO'
    print(f'Status: {state}\nMédia: {media}')
else:
    state = 'APROVADO'
    print(f'Status: {state}\nMédia: {media}')

