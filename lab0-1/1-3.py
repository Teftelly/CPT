spisoc = [int(i) for i in input("Введите список из числовых  \
элементов :\n").split()]
s = 0
for i in range(1, len(spisoc)):
    if spisoc[i] > 10:
        s = spisoc[i]+s
print("Сумма элементов > 10 равна :\n", s)
