# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

summ_num = int(input("Сумма чисел "))
proizv_num = int(input("Произведение чисел "))

for i in range(summ_num):
    for j in range(proizv_num):
        if summ_num == i + j and proizv_num == i * j:
            print(f" Первое число {i}, второе число {j}")
            break
    else:
        continue
    break
else:
    print("Решения нет")
    
