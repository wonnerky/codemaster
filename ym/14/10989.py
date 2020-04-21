import sys

n= int(sys.stdin.readline())
s=[]
for i in range(n):
    a=int(sys.stdin.readline())
    s.append(a)

s=sorted(s)

for i in s:
    print(i)