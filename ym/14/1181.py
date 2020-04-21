import sys
s=[]

n=int(sys.stdin.readline())

for i in range(n):
    word=sys.stdin.readline()
    s.append(word)

s=set(s)
s=list(s)
s=sorted(s,key=len)
s=sorted(s,key=lambda s: (len(s), s))


for i in s:
    print(i,end='')