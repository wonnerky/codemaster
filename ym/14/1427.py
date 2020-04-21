n=input()
s=[]
for i in n:
    i=int(i)
    s.append(i)

s.sort(reverse=True)

for i in s:
    print(i,end='')

