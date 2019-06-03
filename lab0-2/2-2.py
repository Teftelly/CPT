spisoc = [str(i) for i in input("Введите список строк через пробел :\n").split()]
print(*[i for i in spisoc if 5 <= len(i) <=10 ])
