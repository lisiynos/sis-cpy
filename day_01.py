a = 10
b = 15
a, b = 1, 2
print(a)
print(b)

print(2 * 3)

myDouble = 3.55
print(myDouble + 4.334)

# 2^101 * 0.01011111101110[101.....
#  6.5 * 10^3
s = '121'
i = int(s)
i += 2
s2 = str(i)
print("s2 = " + s2)

print(bool("1"))
print(bool("0"))
print(bool(None))  # None ''

myList = [4, 5, 6]
print(*myList)
b = [5, -100, 3, 12002, int("22"), True, 123, False]  # , [22, 332]
b.sort()
print(*b)

t = [(1, 2), (-1, 2), (1, 1), (2, -100), (1, 1)]
print(sorted(t))

a, b = (1, 2)

x = 700
y = 9
x, y = y, x
print("x = " + str(x))
print("y = " + str(y))

myVar = "myValue"
print("myVar = " + myVar)
del myVar
myVar = ""
print("myVar2 = " + myVar)

v = "12312"
# ...
v = 12312
# ...

print(bool(-1))
print(bool(0))

print(30 // 7)

print(pow(2.0, 200))
print(pow(2, 200))

print("super " * 8 + 'python!')

n = 10
A = [0] * n
A = [0 for i in range(10)]  # 2D
print(A)

S = """
    This is multiline
       comment 
        
"""
print(S)

# inp = input()
# print(int(inp) ** 2)

s = "2 3"  # input()  # "2 3"
arr = s.split()  # ['2', '3']
print(arr)
xs, ys = arr
print(int(xs) + int(ys))

# print(sum(map(int, input().split())))

print(xs, ys, 5, 6, end='_END_', sep='#SEP#')

print()
b = [3, 5, 20, 10]
for x in b:
    print(x, '^ 2 =', x ** 2, end=',  ')
print()

# Файловый ввод/вывод
import sys

# Сумма всех чисел
ID = 'myproblem'
sys.stdin = open(ID + ".in", 'r')
# if not DEBUG:
sys.stdout = open(ID + ".out", 'w')
# input()
# print()
print(sum(map(int, input().split())))

ID = 'myproblem'
sys.stdin = open(ID + ".in", 'r')
sys.stdout = open(ID + ".out", 'w')
# input() / print()  # как обычно
