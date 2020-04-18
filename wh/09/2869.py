import sys
import math
A, B, V = map(int, sys.stdin.readline().split())
heightADay = A - B
day = math.ceil((V - A) / heightADay)
print(day + 1)