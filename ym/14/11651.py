import sys
read = lambda : sys.stdin.readline().strip()

ans = []
for _ in range(int(read())):
    x, y = map(int, read().split())
    ans.append((y, x))

for y, x in sorted(ans):
    print(x, y)