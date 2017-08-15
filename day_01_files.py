#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Работа с файлами: стандартная шапка для работы с файлами
import sys

ID = "problemname"
sys.stdin = open(ID + ".in", 'r')
sys.stdout = open(ID + ".out", 'w')

#  22 3324

a, b = map(int, input().split())
print(a + b)

file_r = open('task.in', 'r')
file_w = open('task.out', 'w')

line = file_r.readline()
lines = file_r.readlines()
file_w.write('any string ')
print(1, '345 ', file=file_w)
file_r.close()
file_w.close()

# Читаем и выводим весь файл целиком
file_r = open('task.in', 'r')
for line in file_r.readlines():
    print(line)  # , file=file_w # <-- для копирования
file_r.close()
