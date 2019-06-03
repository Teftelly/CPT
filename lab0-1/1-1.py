a = float(input("введите а: "))
b = float(input("введите b: "))
c = float(input("введите c: "))
k = float(input("введите k: "))
if (a == 0) or (b == 0):
    print("Знаменатель должен быть отличен от нуля")
elif a+b+c*(k-a/(b*b*b)) == 0:
    print("Знаменатель должен быть отличен от нуля")
else:
    ans = ((a*a)/(b*b)+c*c*a*a)/(a+b+c*(k-a/(b*b*b)))+c+(k/b-k/a)*c
    if ans < 0:
        ans = -ans
    print("Ответ:", ans)
