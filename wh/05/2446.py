import sys
n = int(sys.stdin.readline())
j = 2*n+1
for i in range(2*n-1):
    if i < n:
        j = j - 2
        print(' ' * i + '*'*j)
    else:
        j = j + 2
        print(' ' * (2*n-2-i) + '*' * j )