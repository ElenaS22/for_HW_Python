# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

Summ = int(input("Введите общее число журавликов (Summ), которое сделали дети: "))
if Summ % 6 == 0:
    PSCrane = Summ // 6
    KCrane = 4*PSCrane
    print(
        f"Всего журавликов {Summ}, из них Катя сделала {KCrane} штук Петя и Сережа сделали по {PSCrane} штук")
else:
    print("Сумма журавликов должна быть кратна 6 и являться четным числом")
