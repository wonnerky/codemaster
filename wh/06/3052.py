import sys

divNum = []
for i in range(10):
    divNum.append(int(sys.stdin.readline())%42)
divNum = set(divNum)
print(len(divNum))