import sys

a = int(sys.stdin.readline())

def seperate(n):
    nnum = list(str(n))
    snum = 0
    for i in range(len(nnum)):
        snum += int(nnum[i])
    return snum + n

gen = 0

for i in range(a):
    if seperate(i) == a:
        gen = i
        break

print(gen)
