from random import randint

try:
    import random

    a = int(input('Количество строк: '))
    b = int(input('Количество столбцов:  '))
    x = int(input('Начало диапазона целых чисел: '))
    y = int(input('Конец диапазона целых чисел: '))
    matrix = [[randint(x, y) for f in range(a)] for f in range(b)]
    for f in matrix:
        print()
        for j in f:
            print(j, end=" ")
except ValueError:
    print("Ошибка!")
else:
    print("\nОшибок нет")
finally:
    print("Выполняется всегда!")
