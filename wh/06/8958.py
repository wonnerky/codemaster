import sys

def calScore(result):
    j = 0
    score = 0
    for i in result:
        if i == 'O':
            j += 1
            score = score + j
        else: j = 0
    print(score)

n = int(sys.stdin.readline())
for i in range(n):
    result = sys.stdin.readline()
    calScore(result)

