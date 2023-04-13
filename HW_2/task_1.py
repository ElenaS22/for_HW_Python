# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

import random
from collections import Counter

n_coins = int(input("Ведите число монеток, которое лежит на столе: "))
count_a_side = count_b_side = 0
all_coins = [random.randint(0, 1) for i in range(n_coins)]
print(all_coins, end=' ')
for i in all_coins:
    if i == 1:
        count_a_side += 1
    else:
        count_b_side += 1
if count_a_side > count_b_side:
    print(f"нужно перевернуть {count_b_side} монеток")
else:
    print(f"Нужно перевернуть {count_a_side} монеток")
