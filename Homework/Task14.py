# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число: "))

a = 2

print(1)
while a < n:
    a *= 2
    if a < n:
        print(a)
