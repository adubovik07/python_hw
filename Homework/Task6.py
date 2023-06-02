# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

print("Введите шестизначное число: ")
n = int(input())

sum1 = 0
sum2 = 0

f = n // 1000
l = n % 1000

while f > 0:
    x = f % 10
    sum1 += x
    f = f // 10

while l > 0:
    x = l % 10
    sum2 += x
    l = l // 10

if sum1 == sum2:
    print("yes")
else:
    print("no")