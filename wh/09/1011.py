import sys
def nextStep(curStep, curDis, totalDis):
    minimumDis = (curStep * (curStep + 1)) / 2
    remainDis = totalDis - curDis
    if (remainDis - curStep - 1) >= minimumDis:
        return curStep+1, curDis+curStep+1
    elif remainDis >= minimumDis:
        return curStep, curDis+curStep
    else:
        return curStep-1, curDis+curStep-1


n = int(sys.stdin.readline().strip())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    curStep = 0
    curDis = 0
    count = 0
    while True:
        if curDis == (y - x):
            print(count)
            break
        count += 1
        curStep, curDis = nextStep(curStep, curDis, (y-x))

'''
다른 풀이
1234321 -> 4는 root(total distance)

import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    maxNum = int((y-x)**0.5)
    print(maxNum*2 - int((maxNum - (y-x)+maxNum**2)/maxNum))



'''