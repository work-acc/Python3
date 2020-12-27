#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def num():

    a = input('Первое значение: ')
    b = input('Второе значение: ')
    try:
        if int(a) and int(b):
            c = int(a) + int(b)
            print(f'Результат: {c}')
    except ValueError:
        print(f'Результат: {a + b}')


print(num())
