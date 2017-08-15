#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ленивая динамика

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


lazy_fib_cache = {}


def lazy_fib(n):
    if n in lazy_fib_cache:
        return lazy_fib_cache[n]
    lazy_fib_cache[n] = fib(n)
    return lazy_fib_cache[n]


def fib2(n):
    def stupid(n):
        if n < 2:
            return n
        return fib2(n - 1) + fib2(n - 2)

    if n in lazy_fib_cashe:
        return lazy_fib_cashe[n]
    lazy_fib_cashe[n] = stupid(n)
    return lazy_fib_cashe[n]


def lazy(func):
    def internal(*args, **kwargs):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]

    cache = {}
    return internal


def stupid_fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# Декоратор
@lazy
def fib2(n):
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)


fib = lazy(stupid_fib)
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
for i in range(len(fibs)):
    assert fib(i) == fibs[i]

print(', '.join([str(fib(i)) for i in range(13)]) + str())

print(fib(100))

from functools import lru_cache


# Декоратор
@lru_cache(maxsize=None)
def fib3(n):
    if n < 2:
        return n
    return fib3(n - 1) + fib3(n - 2)
