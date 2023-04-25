# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def stepen(num_a, num_b):
    # num_a = int(input("Ведите число A: "))
    # num_b = int(input("Ведите число B: "))
    if num_b == 1:
        return num_a
    elif num_b == 0:
        return 1
    elif num_b > 0  and num_b != 1:
        return num_a * (stepen(num_a, num_b - 1))
    elif num_b < 0:
        return " ошибка. Введите положительное число В"
    
a = int(input("Ведите число A: "))
b = int(input("Ведите число B: "))
print(f" Если возвести число {a} в степень {b} получится {stepen(a, b)}")

