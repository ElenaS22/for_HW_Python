# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2 4 

def summa_num(num_a, num_b):
    if num_b == 1:
        return num_a + 1
    elif num_b == 0:
        return num_a
    elif num_b > 0  and num_b != 1:
        return (1 + (summa_num(num_a, num_b - 1)))
    elif num_b < 0:
        return " ошибка. Введите положительное число В"
    
a = int(input("Ведите число A: "))
b = int(input("Ведите число B: "))
print(f" Если к числу {a} прибавить число {b} получится {summa_num(a, b)}")