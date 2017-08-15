#!/usr/bin/env python
# -*- coding: utf-8 -*-


# типы данных
i = int("2")
assert i == 2


# функции
def add(x, y):
    return x + y


assert add(1, 10) == 11
assert add('abc', 'def') == 'abcdef'


# Функция может быть любой сложности и
# возвращать любые объекты (списки, кортежи, и даже функции!)
def new_func(n):
    def add_n(x):
        return x + n

    return add_n


add100 = new_func(100)  # new - это функция
assert add100(200) == 300


def func(a, b, c=2):  # c - необязательный аргумент
    return a + b + c


assert func(1, 2) == 5  # a = 1, b = 2, c = 2 (по умолчанию)

# Анонимные функции, инструкция lambda
func = lambda x, y: x + y
assert func(1, 2) == 3


# Классы
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)


p1 = Point(2, 3)
p2 = Point(1, 5)
p3 = p1 + p2
assert p3.x == p1.x + p2.x
assert p3.y == p1.y + p2.y

# подключение модулей
