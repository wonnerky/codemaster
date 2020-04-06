import sys

n = int(sys.stdin.readline())
value = list(map(int, sys.stdin.readline().split()))
print('%d %d' % (min(value), max(value)))