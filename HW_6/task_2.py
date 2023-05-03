# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)


import random

n_for_array = int(input("Ведите число N, которое соответствует числу элементов в массиве чисел: "))
min_indx = int(input("Ведите минимальное значение диапазона: "))
max_indx = int(input("Ведите максимальное значение диапазона: "))
array_num = [random.randint(0, 10) for i in range(n_for_array)]
print(array_num)

for i in range(len(array_num)):
    if min_indx<= array_num[i] <= max_indx:
        print(i)