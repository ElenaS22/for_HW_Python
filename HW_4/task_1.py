# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
n_for_array1 = int(input("Ведите число N, которое соответствует числу элементов в массиве чисел: "))
n_for_array2 = int(input("Ведите число N, которое соответствует числу элементов в массиве чисел: "))

array_1 = [random.randint(-100, 100) for i in range(n_for_array1)]
print(f"Полученный массив чисел {array_1}")
print(sorted(array_1))
#print(type(array_1))
array_2 = [random.randint(-100, 100) for i in range(n_for_array2)]
print(f"Полученный массив чисел {array_2}")
print(sorted(array_2))
#print(type(array_2))

list_1 = list()
for val in array_1:
    if val not in list_1:
       list_1.append(val)
#print(f"Массив итог1: {list_1}")
for val in array_2:
    if val not in list_1:
        list_1.append(val)
print(f"Массив итог: {sorted(list_1)}")

