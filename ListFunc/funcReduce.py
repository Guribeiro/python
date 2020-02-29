from random import *
from functools import reduce

def soma(x, y):
    return x + y

list1 = []

for i in range(0, 11):
    list1.append(randint(0, 99))

somaLista = reduce(soma, list1)

print(somaLista)
