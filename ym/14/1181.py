<<<<<<< HEAD
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
=======
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
>>>>>>> 8893303b5576737fdd24129b31c136a7fd005dfe
    print(i,end='')