<<<<<<< HEAD
import sys
read = lambda : sys.stdin.readline().strip()

ans = []
for _ in range(int(read())):
    x, y = map(int, read().split())
    ans.append((y, x))

for y, x in sorted(ans):
=======
import sys
read = lambda : sys.stdin.readline().strip()

ans = []
for _ in range(int(read())):
    x, y = map(int, read().split())
    ans.append((y, x))

for y, x in sorted(ans):
>>>>>>> 8893303b5576737fdd24129b31c136a7fd005dfe
    print(x, y)