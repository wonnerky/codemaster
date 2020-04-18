import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    H,W,N = map(int, sys.stdin.readline().split())
    if N % H == 0:
        room = N // H
        height = str(H)
    else:
        room = N // H + 1
        height = str(N % H)
    if room < 10:
        room = '0' + str(room)
    else:
        room = str(room)
    print(height+room)