n=(int(input("Введите число N элементов: ")))
num_list_1=[]
for i in range(n):
    num = int(input("Введите num "))
    num_list_1.append(num)
print(num_list_1)


m=(int(input("Введите число M элементов: ")))
num_list_2 = []
for i in range(m):
    num = int(input("Введите num "))
    num_list_2.append(num)
print(num_list_2)


num_list3 = num_list_1+num_list_2

for i in set(num_list3):
    if num_list3.count(i) > 1:
        print(i)
