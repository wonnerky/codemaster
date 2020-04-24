import sys
import itertools

a, b = map(int, sys.stdin.readline().split())
A = []
for i in range(1, a+1):
    A.append(i)

p = itertools.combinations(A, b)
l = list(p)

for i in l:
    print(' '.join(map(str, i)))