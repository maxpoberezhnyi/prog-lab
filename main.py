a = int(input("Сума депозиту: "))
b = int(input("Відсоток депозиту: "))
c = int(input("Кількість місяців: "))

for i in range(c):
    a += a*(b/100)
print("Сума депозиту становитиме", a)