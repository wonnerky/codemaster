import sys

a, b = map(int, sys.stdin.readline().split())

x = 0

for i in range(a):
    x += 1
    y = 0
    for j in range(b):
        if x != j+1:
            print(j+1, end=" ")
