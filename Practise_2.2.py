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
def Energy_kin():
    print("Введите массу в килограммах")
    m = float(input())
    print("Введите скорость в метрах в секунду")
    v = float(input())
    Ek = m * (v)**2 / 2
    print("Кинетическая энергия равна {0} Дж".format(round(Ek, 2)))
def mass():
    print("Введите силу в ньютонах")
    F = float(input())
    print("Введите ускорение в метрах в секунду")
    a = float(input())
    m = F/a
    print("Масса равна {0} кг".format(round(m, 2)))
def Energy_pot():
    print("Введите массу в килограммах")
    m = float(input())
    print("Введите высоту в метрах")
    h = float(input())
    print("Введите ускорение свободного падения")
    g = float(input())
    Ep = m * g * h
    print("Потенциальная энергия равна {0} Дж".format(round(Ep, 2)))
def temp_from_F_to_C():
    print("Введите температуру в градусах Фаренгейта")
    t = float(input())
    T = (t - 32) * 5/9
    print("температура равна {0} гралусов по Цельсия".format(round(T, 2)))
def work():
    print("Введите силу в ньютонах")
    F = float(input())
    print("Введите расстояние в метрах")
    S = float(input())
    A = F * S
    print("Работа равна {0} Дж".format(round(A, 2)))
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
if number == 2:
    mass()
if number == 3:
    temp_from_F_to_C()
if number == 4:
    work()
if number == 5:
    Energy_kin()
if number == 6:
    Energy_pot()
if number == 7:
    pressure()
if number == 8:
    Heat()