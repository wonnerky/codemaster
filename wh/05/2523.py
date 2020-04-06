import sys
n = int(sys.stdin.readline())
j = 0
for i in range(2*n-1):
    if i < n:
        j = i + 1
    else:
        j = j - 1
    print('*'*j)