import sys
read = lambda : sys.stdin.readline().strip()

ans = []
for _ in range(int(read())):
    m, n = map(int, read().split())
    ans.append((m,n))

for i in sorted(ans):

    print(i[0], i[1])