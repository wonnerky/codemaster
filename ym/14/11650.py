<<<<<<< HEAD
import sys
read = lambda : sys.stdin.readline().strip()

ans = []
for _ in range(int(read())):
    m, n = map(int, read().split())
    ans.append((m,n))

for i in sorted(ans):
=======
import sys
read = lambda : sys.stdin.readline().strip()

ans = []
for _ in range(int(read())):
    m, n = map(int, read().split())
    ans.append((m,n))

for i in sorted(ans):
>>>>>>> 8893303b5576737fdd24129b31c136a7fd005dfe
    print(i[0], i[1])