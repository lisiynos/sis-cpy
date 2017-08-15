# Читаем все строчки до конца файла
ID = 'problemname'
file_r = open(ID + '.in', 'r')
file_w = open(ID + '.out', 'w')

for line in file_r:
    a, b = map(int, line.split())
    print("%s => %d" % (line.strip(), a + b), file=file_w)

file_r.close()
file_w.close()

# Снова открываем файл и читаем по частям
file_r = open(ID + '.in', 'r')
line = file_r.readline()  # Читаем одну строку
n, b = map(int, line.split())
A = []
for i in range(n):
    A.append(list(map(int, line.split())))

"""
line = file_r.readline()
lines = file_r.readlines()
file_w.write('any string ')
print(1, '345 ', file=file_w)
file_r.close()
file_w.close()
for line in file_r.readlines():
    print(line, file=file_w)
"""
