def speed():
    print("Введите расстояние в километрах")
    s = float(input())
    print("Введите время в часах")
    t = float(input())
    v = s/t
    print("Скорость равна {0} км/ч".format(round(v, 2)))

def frequency():
    print("Введите период колебаний в секундах")
    T = float(input())
    v = 1 / T
    print("Частота колебаний равна {0} Гц".format(round(v, 2)))


print("Введите число для выбора задачи")
print("Задача 1: Определение скорости")
print("Задача 2: Определение массы")
print("Задача 3: Определение температуры по Цельсию")
print("Задача 4: Определение работы")
print("Задача 5: Определение кинетической энергии")
print("Задача 6: Определение потенциальной энергии")
print("Задача 7: Определение давления")
print("Задача 8: Определение теплоты")
print("Задача 9: Определение частоты")
print("Задача 10: Определение объема")

# functions = [speed, func2, func3, func4, func5, func6, func7, func8, func9, frequency]
functions = [speed, ]

number = int(input())
functions[number - 1]()

# if number == 1:
#     speed()
#
# if number == 9:
#     frequency()