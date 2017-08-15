# День 4. Структуры данных множества и словари, хеши
# ==================================================
# Структура данных set: создание, поддерживаемые операции, примеры использования
# hashtable используется для реализации
import math

# Круги Эйлера - операции с множествами
set1 = {2, 4, 6, 8, 10, 12}  # Чётные
set2 = {3, 6, 9, 12}  # Делятся на 3

# Мощность множества - количество элементов
assert len(set1) == 6, len(set1)

# Вхождение в множество
assert 4 in set1
assert not (5 in set1)
assert 5 not in set1
assert 4 not in set2
assert 9 in set2

# Объединение
assert set1.union(set2) == {2, 3, 4, 6, 8, 9, 10, 12}
assert set1 | set2 == {2, 3, 4, 6, 8, 9, 10, 12}

# Пересечение
assert set1.intersection(set2) == {6, 12}
assert set1 & set2 == {6, 12}

# Разность
assert set1.difference(set2) == {8, 2, 10, 4}
assert set1 - set2 == {8, 2, 10, 4}
assert set2.difference(set1) == {3, 9}
assert set2 - set1 == {3, 9}

# Симметрическая разность двух множеств
assert set1.symmetric_difference(set2) == {2, 3, 4, 8, 9, 10}
assert set1 ^ set2 == {2, 3, 4, 8, 9, 10}

assert set1 and set2 == set2  # Возвращает 2-ой
assert set1 or set2 == set1  # Возвращает 1-ый

# Сортировки нет

# Мощность множества
assert len(set2) == 4
set2.add(10)
assert set2 == {3, 6, 9, 10, 12}
set2.add(10)
assert set2 == {3, 6, 9, 10, 12}
set2.add(11)
assert set2 == {3, 6, 9, 10, 11, 12}
set2.remove(10)
assert set2 == {3, 6, 9, 11, 12}

for x in set1:
    print(x, end=' ')

# Структура данных dict: создание, поддерживаемые операции, примеры использования
d = {1: 2, 3: 3}
for k in d:
    print(k)

# Все ключи словаря
assert d.keys() == {1, 3}, d.keys()
# Все значения словаря
assert list(d.values()) == [2, 3]

for key, value in d.items():
    print(key, value)

key = 10
if key in d:
    print("Есть в словаре")
    print(d[key])

assert dict(one=1, two=2) == {'one': 1, 'two': 2}, dict(one=1, two=2)
dict({'one': 1, 'two': 2})
dict(zip(('one', 'two'), (1, 2)))
dict([['two', 2], ['one', 1]])


# Хеширование.
# Хеш, как функция от объекта. Например, хеш от целых чисел – остаток от деления


# Проблема коллизий.
# Разрешение коллизий:
# - списки
# - открытая адресация

# Полиномиальный хеш от строки: для строки a0a1...an хеш это a0bn + a1bn-1+...anb0 mod N
# Системы счисления
# Взятие по модулю - модульная арифметика

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


# НОД = Наибольший общий делитель
# GCD = Greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


assert gcd(10, 15) == 5

# Красивые простые числа
assert is_prime(43)
assert is_prime(4243)
assert is_prime(424243)
assert is_prime(42424243)
assert is_prime(4242424243)

assert is_prime(10 ** 9 + 7)
assert is_prime(10 ** 9 + 9)

b = 27
assert is_prime(179)

# X = 10 ** 17
# for i in range(11):
#    x = X + i
#    if is_prime(x):
#        print("assert is_prime(10 ** 11 + " + str(i) + ")")

# M = 10 ** 17 + 3
M = 10 ** 9 + 7


# assert is_prime(M)


# Схема Горнера


def hash(S):
    h = 0
    for c in S:
        h = (h * b + ord(c)) % M
    return h


assert hash('a') == ord('a')
assert hash('ab') == ord('a') * b + ord('b')
assert hash('ba') == ord('b') * b + ord('a')
assert hash('abc') == (ord('a') * b ** 2 + ord('b') * b + ord('c')) % M

# Подсчет хешей на префиксах. Переход к следующему префиксу.
S = 'abc abc abc abc'

n = len(S)  # Длина строки
powers = [1] + [0] * n  # Степени b
H = [0] * (n + 1)  # Хеши
# Хеши всех префиксов и степени
for i in range(n):
    powers[i + 1] = (powers[i] * b) % M  # b^0 b^1 b^2... b^n
    H[i + 1] = (H[i] * b + ord(S[i])) % M  # Хеши префиксов


def sub_str_hash(i, j):  # хеш подстроки [i:j)
    assert i <= j
    return (H[j] - H[i] * powers[j - i]) % M


powers = [1] + [0] * n  # Степени b
for i in range(n):
    powers[i + 1] = (powers[i] * b) % M  # b^0 b^1 b^2... b^n
for i in range(n + 1):
    assert powers[i] == (b ** i) % M

print(H)

assert sub_str_hash(0, 1) == hash(S[0:1])
assert sub_str_hash(1, 3) == hash(S[1:3])
for i in range(n + 1):
    for j in range(i, n + 1):
        assert sub_str_hash(i, j) == hash(S[i:j])

# Подсчет хеша для подстроки, если известны хеши для всех префиксов.
# Предподсчет значений bi mod N
# Применения: проверка подстрок на равенство, проверка подстроки на палиндромность.

# Печать списка через запятые
b = [1, 2, 3, 4]
print(", ".join(str(x) for x in b))
