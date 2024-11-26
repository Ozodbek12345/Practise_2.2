import math
def volume():
    print("Введите радиус цилиндра в метрах")
    r = float(input())
    print("Введите высоту цилиндра в метрах")
    h = float(input())
    V = h * math.pi * r**2
    print("Объем цилиндра равен {0} метр в кубе".format(round(V, 2)))
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


def Heat():
    print("Введите массу в килограммах")
    m = float(input())
    print("Введите удельную теплоемкость")
    c = float(input())
    print("Введите изменение температуры")
    delta_t = float(input())
    Q = c * m * delta_t
    print("Количество теплоты равно {0} Дж".format(round(Q, 2)))
def pressure():
    print("Введите силу в ньютонах")
    F = float(input())
    print("Введите площадь в квадратных метрах")
    S = float(input())
    p = F / S
    print("Давление равно {0} Па".format(round(p, 2)))
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
if number == 7:
    pressure()
if number == 8:
    Heat()