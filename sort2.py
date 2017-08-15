A = [2, 0, -1, 10, 99]
n = len(A)
A_copy = A.copy()

for i in range(n):
    for j in range(n - 1, i, -1):  # 0..i-1
        if A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
print(A)
assert A == sorted(A_copy)


def CountSort(A):
    K = max(A) + 1
    count = [0] * K
    for elem in A:
        count[elem] += 1
    result = []
    for val in range(K):
        result += [val] * count[val]
    return result


A = [0, 2, 10, 99]
A_copy = A.copy()
A = CountSort(A)
assert A == sorted(A_copy)
