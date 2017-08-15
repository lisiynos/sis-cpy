fin = open("min.in", 'r')
fout = open("min.out", 'w')

# Space, Tab, Enter...
n = int(fin.readline().strip())
print(n)
A = list(map(int, fin.readline().split()))
# min
INF = 10 ** 10000
cur_min = INF
for x in A:
    if x < cur_min:
        cur_min = x
if cur_min == INF:
    fout.write("Массив пустой\n")
    print("Массив пустой", file=fout)
else:
    print(cur_min, file=fout)
# Закрывать файл
fout.close()
