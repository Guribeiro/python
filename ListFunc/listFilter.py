
list1 = []

def pares(i):
    if i % 2 == 0:
        return i


def impares(i):
    if i % 2 == 1:
        return i


for i in range(0, 11):
    list1.append(i)

'''
paresList = list(filter(pares, list1))
imparesList = list(filter(impares, list1))

print(list1)
print(paresList)
print(imparesList)
'''

listPar = list(filter(lambda index : index % 2 ==0, list1))

print(listPar)