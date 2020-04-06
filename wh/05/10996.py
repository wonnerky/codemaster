import sys

def plotStar(n):
    div = n // 2
    mod = n % 2
    print('* ' * (div + mod))
    if div > 0: print(' *' * div)

n = int(sys.stdin.readline())
for i in range(n): plotStar(n)