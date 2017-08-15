import random


# Сортировка слиянием
def merge(A, B):
    res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    res += A[i:] + B[j:]
    return res


def MergeSort(A):
    if len(A) <= 1:
        return A
    else:
        L = A[: len(A) // 2]
        R = A[len(A) // 2:]
        return merge(MergeSort(L), MergeSort(R))


A = [random.randint(-10 ** 9, 10 ** 9) for i in range(1000)]
A_copy = A.copy()
A = MergeSort(A)

assert A == sorted(A_copy)
