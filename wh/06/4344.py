import sys

def calScore(result):
    n = result[0]
    p = 0
    del result[0]
    for i in result:
        if i > sum(result)/n: p += 1
    print('%.3f%%' % (p/n * 100))

score = []
c = int(sys.stdin.readline())
for i in range(c):
    score.append(list(map(int, sys.stdin.readline().split())))
for i in range(c):
    calScore(score[i])