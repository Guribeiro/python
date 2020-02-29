list1 = [1, 2, 3, 4, 5]

list2 = []

list3 = [pow(i, 2) for i in list1]

list4 = [i for i in list1 if i % 2 == 0]

list5 = [i for i in list1 if i % 2 == 1]


for index in list1:
    list2.append(pow(index, 2))


print(list1)
print(list2)
print(list3)
print(list4)
print(list5)