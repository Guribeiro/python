word = input('Digite algo: ')

print('Tipo primitivo: {}'.format(type(word)))
print('Apenas espaços: {}'.format(word.isspace()))
print('Numérico: {}'.format(word.isnumeric()))
print('Alfabético: {}'.format(word.isalpha()))
print('Alfanumérico: {}'.format(word.isalnum()))
print('Maiúsculas: {}'.format(word.isupper()))
print('Minúsculas: {}'.format(word.islower()))
print('Capitalizada: {}'.format(word.istitle()))  