import sys

n=int(sys.stdin.readline())
big_list=[]
dict={}
for i in range(n):
    info=sys.stdin.readline().split() #[나이, 이름]
    info[0]=int(info[0])
    big_list.append(info) # [[나이,이름],[나이,이름]]

#print(big_list) ok

for k,v in enumerate(info):
    dict[k]=v

big_list.sort()

for i in range(n):
    if i==n:
        break
    #if big_list[i][0] == big_list[i+1][0] and dict.items()






