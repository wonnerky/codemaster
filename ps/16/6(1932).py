<<<<<<< HEAD
import sys

a = int(sys.stdin.readline())

l = []
for i in range(a):
    n = list(map(int, sys.stdin.readline().split()))
    l.append(n)

for i in range(1, a):
    l[i][0] = l[i - 1][0] + l[i][0]
    l[i][i] = l[i - 1][i - 1] + l[i][i]
    for j in range(1, i):
        l[i][j] = max(l[i-1][j-1]+l[i][j],l[i-1][j]+l[i][j])

print(max(max(l)))
=======
tri_f = int(input())

tri_a = []
for i in range(tri_f):
    tri_a.append(list(map(int, input().split())))

s = 0
f = 1
sum_list = []
for i in range(tri_f):
    for j in range(f):
        if i == 0:
            s = tri_a[i][i]
        elif i >= 1 and j

    f += 1


print(tri_a)
>>>>>>> 8893303b5576737fdd24129b31c136a7fd005dfe
