def Heat():
    print("Введите массу в килограммах")
    m = float(input())
    print("Введите удельную теплоемкость")
    c = float(input())
    print("Введите изменение температуры")
    delta_t = float(input())
    Q = c * m * delta_t
    print("Количество теплоты равно {0} Дж".format(round(Q, 2)))
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
number = int(input())
if number == 8:
    Heat()