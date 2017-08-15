# Начнем мы с равенства:
assert 16 + 45 == 25 + 36
# которое перепишем в виде:
assert 16 + 9 * 5 == 25 + 9 * 4
# Перенесем некоторые слагаемые в другие части равенства —
# естественно, изменяя знаки на противоположные:
assert 16 - 9 * 4 == 25 - 9 * 5
# теперь к обеим частям добавим по 81/4.
assert 16 - 9 * 4 + 81 / 4 == 25 - 9 * 5 + 81 / 4

# Заметим, что в обеих частях стоят полные квадраты:
assert 16 - 9 * 4 + 81 / 4 == 16 - 2 * 4 * 9 / 2 + 81 / 4 == (4 - 9 / 2) ** 2
assert 25 - 9 * 5 + 81 / 4 == 25 - 2 * 5 * 9 / 2 + 81 / 4 == (5 - 9 / 2) ** 2

# Извлекая квадратный корень из обеих частей равенства, получаем что
assert 4 - 9 / 2 == - (5 - 9 / 2)
assert abs(4 - 9 / 2) == abs(5 - 9 / 2)