import sys

a, b = map(int, sys.stdin.readline().split())

<<<<<<< HEAD
for i in range(a):
    for j in range(b):
        if i !=
=======
x = 0

for i in range(a):
    x += 1
    y = 0
    for j in range(b):
        if x != j+1:
            print(j+1, end=" ")
>>>>>>> 8893303b5576737fdd24129b31c136a7fd005dfe
