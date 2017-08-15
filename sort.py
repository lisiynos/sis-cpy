# TODO: random
src = "1 2 43 10 102 -1"
A_copy = list(map(int, src.split()))

# O(1) - константная сложность
# O(n) - линейная сложность. Не O(2n)
# O(log n) - логарифмическая
# O(n^2) - квадратичные
# O(n^3) - P полиномиальная сложность
# O(n^const + m^const + n*m)
# O(n log n) - большинство "быстрых" сортировок
# O(2^n) - эспоненциальная сложность
#   например: перебор всех подмножеств
# O(n^n)

# Сортировка выбором
# Ставим минимум из i..n-1 на i-ое место
A = A_copy.copy()
n = len(A)
for i in range(n - 1):
    min_value = A[i]
    min_idx = i
    for j in range(i + 1, n):
        if A[j] < min_value:
            min_value = A[j]
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]

assert A == sorted(A_copy)

A = A_copy.copy()

for i in range(n - 1, 0, -1):
    for j in range(i):
        if A[j] > A[i]:
            A[i], A[j] = A[j], A[i]

for i in range(n - 1):
    # A[i:n]    A[i] - min
    for j in range(i + 1, n):  # j > i
        if A[j] < A[i]:
            A[i], A[j] = A[j], A[i]

# Сортировка пузырьком
for i in range(n - 1, 0, -1):
    # Ставим максимум A[:i+1]
    for j in range(i):  # 0..i-1
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]

assert A == sorted(A_copy)
