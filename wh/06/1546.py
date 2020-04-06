import sys

n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
maxScore = max(score)
for i in range(len(score)):
    score[i] = score[i] / maxScore * 100
print(sum(score)/n)