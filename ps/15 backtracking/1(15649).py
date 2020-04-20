import sys

a, b = map(int, sys.stdin.readline().split())

l = []
for i in range(1, a+1):
    for j in range(1, a+1):
        if i != j:
            