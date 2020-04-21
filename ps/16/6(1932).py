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