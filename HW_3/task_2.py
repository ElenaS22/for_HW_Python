# Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X. Если таких элементов несколько, вы вывести один любой.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию).
# Последняя строка содержит число X
# *Пример:*
# 5
#     7 -2 3 5 1
#     6
#     -> 7

import random

n_for_array = int(input("Ведите число N, которое соответствует числу элементов в массиве чисел: "))
x_number = int(input("Ведите число X, которое требуется найти среди элементов в массиве чисел N: "))

array_a = [random.randint(0, 5) for i in range(n_for_array)]
#array_a = [2, 76, 74, 19, 38, 3, 78, 98, 56, 37, 49]
print(f"Полученный массив чисел {array_a}")

clos_num = clos_num1 = clos_num2 = temp_number = 0

for element in array_a:
   if element == x_number:
      clos_num = element
      print(f"Элемент равный искомому: {clos_num}")
      break
   if element < x_number:
      temp_number = element
      if temp_number > clos_num1:
         clos_num1 = temp_number
     
   # elif element > x_number:
   #    temp_number = element
   #    if temp_number > clos_num2:
   #       clos_num2 = temp_number
      
                     
   # elif x_number - clos_num1 < clos_num2 - x_number:
   #    print(f"Искомый элемент: {clos_num1}")
   # else:
   #    print(f"Искомый элемент: {clos_num2}")
else:
   print(f"Близкий к искомому элемент: {clos_num1}") 
   # print(f"Второй элемент: {clos_num2}") 

# if x_number - clos_num1 < clos_num2 - x_number:
#      print(clos_num1)
# else:
#      print(clos_num2)

   
#print(f"Искомый элемент: {clos_num_max}")

#print(f"Искомый элемент: {temp_number}")

# import random

# n_for_array = int(input("Ведите число N, которое соответствует числу элементов в массиве чисел: "))
# x_number = int(input("Ведите число X, которое требуется найти среди элементов в массиве чисел N: "))

# array_a = [random.randint(0, 5) for i in range(n_for_array)]
# print(f"Полученный массив чисел {array_a}")
# find_number = 0

# for i in array_a:
#    find_number = min(array_a, key = lambda i: abs(i - x_number))
# print(f"Искомый элемент: {find_number}")
