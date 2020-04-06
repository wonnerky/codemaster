import sys

sum = 0
score = {'won':1, 'sea':2, 'sang':3, 'soung':0, 'kang':0}
for key in score:
    value = int(sys.stdin.readline())
    if value < 40: value = 40
    score[key] = value
for value in score.values():
    sum += value
print(int(sum/len(score)))