def dobro(x):
    return x * 2

list1 = []

for index in range(0, 11):
    list1.append(index)

listDobro = list(map(dobro, list1))

print(listDobro)

