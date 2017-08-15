# Поиск
from math import factorial

factorial(2)


# Линейный поиск
def search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return True
    return False


def search2(A, key):
    for elem in A:
        if elem == key:
            return True
    return False


def search3(A, key):
    i = 0
    while i < len(A) and A[i] != key:
        i += 1
    return i < len(A)


# Поиск минимума
def FindMin(A):
    if len(A) == 0:
        return None
    min_a = A[0]
    for i in range(1, len(A)):
        if A[i] < min_a:
            min_a = A[i]
    return min_a


assert FindMin([1, -3, 2]) == -3
assert FindMin([]) == None

A = [1, 2, 2, 4]


# Правый поиск: [l, r)
def UpperBound(A, key):
    left = 0
    right = len(A)
    while left + 1 < right:
        middle = (left + right) // 2
        if A[middle] > key:
            right = middle
        else:
            left = middle
    return right


assert UpperBound(A, 1) == 1
assert UpperBound(A, 2) == 3
assert UpperBound(A, 4) == 4
# Отсутствующие элементы
assert UpperBound(A, 3) == 3
assert UpperBound(A, 5) == 4
assert UpperBound(A, -1) == 1


# Левый поиск: (l, r]
def LowerBound(A, key):
    left = -1
    right = len(A)
    while left + 1 < right:
        middle = (left + right) // 2
        if A[middle] >= key:
            right = middle
        else:
            assert left != middle
            left = middle
    return left


assert LowerBound(A, 1) == -1
assert LowerBound(A, 2) == 0
assert LowerBound(A, 4) == 2
# Отсутствующие элементы
assert LowerBound(A, 3) == 2, LowerBound(A, 3)
assert LowerBound(A, 5) == 3
assert LowerBound(A, -1) == -1, LowerBound(A, -1)


def BinarySearch(A, key):
    left = -1
    right = len(A)
    while right > left + 1:
        middle = (left + right) // 2
        if A[middle] > key:
            right = middle
        else:
            left = middle
    return left >= 0 and A[left] == key


assert not BinarySearch(A, -1)
assert BinarySearch(A, 1)
assert BinarySearch(A, 2)
assert not BinarySearch(A, 3)
assert BinarySearch(A, 4)
assert not BinarySearch(A, 10)

assert LowerBound(A, -10) == -1, LowerBound(A, -10)
B = [1, 2, 3, 4]
assert LowerBound(B, 1) == -1

assert UpperBound(A, -10) == 1, str(UpperBound(A, -10))

assert LowerBound(A, 1) == -1, LowerBound(A, 1)
assert UpperBound(A, 1) == 1, UpperBound(A, 1)
assert LowerBound(A, 2) == 0, LowerBound(A, 2)
assert UpperBound(A, 2) == 3, UpperBound(A, 2)


def check(m, A, x):
    return A[m] > x


def find_ind(A, x):
    l = 0
    r = len(A)
    while l + 1 < r:
        if x in A:  # DEBUG
            assert x in A[l:r + 1]
        m = (l + r) // 2
        if check(m, A, x):
            r = m
        else:
            l = m
    if A[l] == x:
        return l
    return False


A = [10, 20, 30, 40, 50]
assert find_ind(A, 10) == 0, find_ind(A, 1)
assert find_ind(A, 20) == 1, find_ind(A, 2)
assert find_ind(A, 30) == 2, find_ind(A, 3)
assert find_ind(A, 40) == 3, find_ind(A, 4)
assert find_ind(A, 50) == 4, find_ind(A, 5)
assert not find_ind(A, -1)
assert not find_ind(A, 10)
