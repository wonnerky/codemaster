import sys

n = int(sys.stdin.readline().strip())
listNum = []
for i in range(n):
    listNum.append(int(sys.stdin.readline().strip()))
listNum.sort()
for i in listNum:
    print(i)