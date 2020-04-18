import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    maxNum = int((y-x)**0.5)
    print(maxNum*2 - int((maxNum - (y-x)+maxNum**2)/maxNum))

'''
다른 풀이
1234321 -> 4는 root(total distance)




'''